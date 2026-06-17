# 05 — Predictive AI (Orange Data Mining)

> Cumulative project, ESADE *Data-Driven Prototyping with AI*. Builds on the ontology (Customer + Mobile-App objects: accounts, transactions, invoices/receivables, goals, products, agents, decisions) and the client/evidence pass in [`docs/01`](01-client-and-evidence.md). This document answers the six required questions, then gives a widget-by-widget Orange build for the recommended first model.

---

## TL;DR

**Build first:** **Per-invoice late-payment risk** — for each open receivable, the probability the paying client settles it late. This *is* the closed-loop moat (every realized payment date retrains it), it is **non-credit** (it scores a business counterparty, not a person's creditworthiness → outside AI Act Annex III), and it is the parent dependency that feeds the cash-flow-gap forecast and the safe-to-borrow number.

**Two hard rules a faculty member will grill you on:**
1. **Clustered rows.** Many invoices per paying client → a plain random/stratified split leaks payer identity across train/test and inflates AUC. Orange has **no GroupKFold**. Use a **manual payer-grouped holdout** (below). *Show the leakage gap on a slide.*
2. **Target leakage & point-in-time correctness.** Every feature must be computable from data timestamped **before** the prediction point. The per-client reliability features must be an *as-of-issuance trailing snapshot*, computed **outside** Orange.

---

## Q1 — Which customer data is needed (maps to the ontology)

Two **clustered** tables are the spine, plus low-cardinality context:

- **Invoices / Receivables** *(one row per invoice, many per customer AND per paying client)* — `invoice_id`, `customer_id` (issuer), `client_id` (payer), `issue_date`, `due_date`, `amount_gross/net`, `terms` (30/60d), `status`, and — **as the LABEL source only** — `paid_date`.
- **Per-client reliability ledger** *(the closed-loop moat asset)* — each payer's accumulated realized payment dates, logged append-only in the Decisions/Agents object. This is the retraining substrate and the source of the grouping key.

Supporting, low-leakage context:

- **Customer firmographics / KYC** — `legal_form` (autónomo / SL), `sector_cnae`, `region`, `months_in_business`, `n_employees_band`.
- **Accounts / Transactions** — balances, signed amounts, MCC (for the secondary cash-flow model).
- **Goals** — target amount/date, `connected_data_depth`.
- **Tax/VAT state** — `next_vat_due_date`, `upcoming_vat_irpf_liability` (for safe-to-borrow netting).

External-but-commodity feeds: PSD2 open-banking, accounting tool (Holded/Quaderno), Verifactu/SII (once live), payroll / per-employee card (2–10-employee tier).

**Two export grains for Orange:** (a) **one-row-per-invoice** with point-in-time reliability features + an `is_test` split column + payer key — *the headline table*; (b) optionally one-row-per-client only for a separate summary model. **GDPR data-minimisation:** feed aggregates (ratios, lags, counts), not raw transaction-level personal data, wherever avoidable.

---

## Q2 — Which variables matter (features)

**Per-client reliability (the core — ALL `_asof_issuance`, trailing only):**

| Feature | Signal |
|---|---|
| `client_mean_days_late_asof_issuance` + `client_std_days_late_asof_issuance` | the single most predictive **pair** — average lateness *and its volatility* |
| `client_pct_on_time_asof_issuance`, % paid >30/>60/>90d late, longest delay | reliability shape |
| `n_payments_observed` | **cold-start caution** — lets the model be conservative at low n |
| recency of last payment, tenure, `invoice_size_vs_client_norm`, seasonality | context |

**Invoice-intrinsic:** `amount`, `terms`, AR-aging bucket (snapshot as-of issuance).

**Structural / customer:** `client_concentration_share` (*“one client = 60% of you”*), `inflow_volatility` (CV of monthly inflows), `net_burn_rate` (trailing 3m), `runway_days` (cash ÷ **trailing** burn), `committed_fixed_outflow`, `upcoming_vat_irpf_liability` (a *legitimate* known-at-decision forward outflow), `connected_data_depth`, `account_age_months`, `sector_cnae`.

> **Drop the black-box `client_reliability_score` single number** — replace it with the transparent trailing components so a reviewer can *see* it isn't leaking the target.

**🚨 Target-leakage variables to HARD-exclude** (role = *skip* in Select Columns; rule: every feature timestamp **< prediction point**):
`paid_date`, `days_late` / `days_to_pay_realized`, the paid/overdue **status flag** of the target invoice, post-default dunning/collections, balance-after-event, current open draw, any reliability aggregate that includes the target payment, and a SaaS-spend cut **concurrent** with the outcome (lag it). *Sanity check in Rank: a single feature near ~1.0 AUC is almost always leakage.*

**⚖️ Fairness-care features:** `sector_cnae` and `region/province` can **proxy** protected attributes — this is fair-lending / Annex III disparate-impact risk, *not* data leakage. Keep sector low-cardinality (group rare codes); **exclude `region` from any credit-side model** (weak lift, high proxy risk).

---

## Q3 — What to predict (the model)

**PRIMARY (build first): per-invoice late-payment risk.** Unit = one open receivable. ML type: **classification** (Logistic Regression baseline + Tree + Random Forest), optional regression head (predicted days-late) for pricing.

- **Label (proxy default — needs NO loan book):** `paid_late = 1` when `paid_date − due_date > 30 days` (or unpaid at horizon), else `0`. Built entirely from realized payment dates already in the AR ledger — the closed loop.

**Roadmap sequence:**
1. **Per-invoice late-payment** *(this — the moat)*.
2. **Cash-flow gap forecast** — classification (*“shortfall in next 30d: yes/no”*), consuming model 1's per-client probabilities as a feature; same grouped-holdout discipline at **customer-period** grain (no customer or period straddles the split).
3. **k-Means expense anomaly** — the **unsupervised** contrasting model (sidesteps leakage + grouped-split entirely).
4. **Loan/bridge default** — *defer* until there's a real book; present **behind the human-reviewed credit gate** only.

---

## Orange — widget-by-widget (no-code, group-aware)

> **Step 0 (pre-Orange, mandatory — Orange is not time-series-native).** In a pandas/script step, build the one-row-per-invoice CSV. For **each** invoice, compute every reliability feature strictly from that client's payments realized **before** this invoice's `issue_date` (trailing `_asof_issuance` snapshot). Add `is_test` = boolean assigning **~25–30 % of DISTINCT payer_ids ENTIRELY to test** (`hash(payer_id) mod k`; never split a payer across train/test). Compute `paid_late`, then **drop** `paid_date`/`days_late`.

| # | Widget | What you do |
|---|---|---|
| 1 | **File** | Load the one-row-per-**invoice** CSV. *(Not a client-level aggregate — that changes the prediction target and shrinks N.)* |
| 2 | **Feature Statistics / Distributions / Scatter Plot** | Sanity-check; eyeball the lateness/volatility split; hunt for any too-perfect separator. |
| 3 | **Select Columns** | `class = paid_late`; **`client_id`/`customer_id` → role META** (never a feature — a tree would memorize identity); **skip ALL post-outcome fields** (`paid_date`, `days_late`, status flag, collections, balance-after, open draw). Exclude `region` from credit-side variants. |
| 4 | **Rank** | Top features by info-gain/AUC. **Leakage alarm:** a single feature ~1.0 AUC → back to Select Columns. Confirm `_asof_issuance` features rank high. |
| 5 | **Preprocess (Normalize/Standardize)** | Required before **kNN / Logistic Regression / k-Means**; Tree/RF are scale-invariant. **Footgun fix:** do NOT place a standalone Preprocess *before* the split (fits scaler on test = leak) — **wire it into each learner**, or apply only on the train branch. |
| 6 | **THE GROUPED HOLDOUT** *(critical — Orange has no GroupKFold; Test&Score CV has no group param and WILL leak)* | Two **Select Rows** branches off File: `[is_test = false] →` learners (**Logistic Regression + Tree + Random Forest** + optional kNN, Preprocess wired in); `[is_test = true] →` test. Feed train-fitted models + test into **Predictions**. Read **Confusion Matrix / ROC / Calibration** off Predictions. **Do NOT run Test&Score stratified CV on the raw per-invoice table.** |
| 7 | **THE LEAKAGE-GAP SLIDE** | ALSO run the *same* models through **Test & Score** with naive stratified random CV; report both AUCs. The drop (e.g. **0.91 → 0.78**) **is the leakage you removed** — your strongest faculty-defense artifact. |
| 8 | **Confusion Matrix + ROC + Calibration Plot** | `paid_late` is the **minority class** → judge on AUC + confusion matrix with a **cost-sensitive threshold** (a missed late-payer costs more than a false alarm), **NOT accuracy**. **Calibration Plot is the centerpiece** — a well-calibrated probability is exactly what *prices the bridge*. |
| 9 | **Fairness check (one slide)** | Filter the Confusion Matrix by `sector_cnae` (and `region`); report **group error rates**. Recommend dropping `region` from the credit-side model. |
| 10 | **Predictions** | Score new open receivables → feeds the cash-flow-gap model and the human-on-the-loop credit screen. **Source the customer-facing reason from the interpretable Logistic Regression coefficients (or Tree paths)** even when Random Forest is the production scorer. |
| 11 | *(optional)* **k-Means + Scatter Plot + Distributions** | Reliability archetypes / expense anomalies — unsupervised, sidesteps leakage + grouped-split; clean second model to show range. |

### Why the grouped split, restated for the defense
Rows are clustered by paying client. A plain split lets the model memorize *“Studio Vermell pays at ~12 days”* instead of learning generalizable behavior — and that inflation **collapses on new clients**, the cold-start population you most need to score (the ATHENA2 lesson: GroupKFold on the natural cluster, never stratify-by-label). **`customer_id`/`client_id` is the GROUP key only — never a model feature.**

> ⚠️ **One-row-per-client aggregation is NOT the headline build.** It changes the prediction target away from the per-invoice receivable and shrinks N. Use Group By only for an explicitly-labelled *secondary client-level* model.

---

## Q4 — How the prediction improves the customer experience

One lying balance → three truths + a forecast:
- **Cash-low warning** — *“see the dry August before it hits,”* forecast from the customer's **clients'** real payment habits, not a generic average.
- **Specific-receivable bridge** — a late invoice bridged against a **96 %-reliable named receivable** at a price reflecting *that client's* reliability (often **cheaper** than a blunt personal score), not an *“erratic”* profile.
- **Honest “don't borrow”** branch when the model says the cash is genuinely coming.
- **Inverted flywheel:** she opens the app **less**, feels calmer, bridge-dependence **falls** — the objective rewards this, which an interchange/engagement incumbent is structurally disincentivized to copy.

Every prediction ships with a **confidence band** (*“low point ~Aug 12, ±4 days”*) and an **expandable plain-language reason** (*“Client ACME pays ~18d late on a €9k invoice; tax pot holds €2.1k”*) — simultaneously the **GDPR Art. 22 explanation** and a trust feature.

---

## Q5 — Product-market fit

Real and evidence-backed, with two honest qualifications.

- **The wound is quantified & sourced:** autónomo collection averages **>85 days** (CEPYME 2025) vs 30/60-day legal terms; **60 % weekly financial stress** (docs/01).
- **Structural differentiator:** a monthly-salary risk model has **no object** for an invoice or a per-client payment-lag distribution — incumbents won't build this model.
- **Re-anchor on the agency tier (docs/00 pivot):** the core is now **agencies + 2–10-employee companies (€10k–€1M, often an SL)**, solo autónomos as the wedge-in. Agencies have **more clients, more invoices, a richer per-client reliability signal, multi-seat cards, higher WTP** — the model's PMF is *densest* there. Keep the >85-day autónomo stat as the wedge, not the core.

**Two qualifications for the defense:**
1. **Two moat tiers, not one.** The **closed-loop DATA moat** (per-client reliability that compounds) is durable and hard to copy. The **financial-health OBJECTIVE moat** is real but **softer** (a well-capitalised entrant could run health-as-loss-leader and monetize on the card tier). Present them as different strength tiers.
2. **WTP is the project's #1 self-identified weakness** (docs/01 open-question 1). This model **de-risks the underwriting thesis** (proves the signal exists), **not the monetization thesis** (who pays, how). Say so plainly.

---

## Q6 — The role of human–AI interaction

The **human is the safety + legitimacy layer** where money meets a person's creditworthiness; the **AI is the speed + legibility layer** everywhere else. Attention is spent **only** where it changes an irreversible or regulated outcome.

| Decision | Human role | Why |
|---|---|---|
| Expense categorization | **out** | cheap, reversible, non-Annex III |
| Cash-flow / runway forecast | **out** | advisory information, reversible |
| Per-client invoice-reliability score *(this model)* | **out** | scores a **business counterparty**, not a person's creditworthiness |
| “Safe to borrow: €X” **display** | **out** | computing/showing a ceiling is **info**; the **grant** is the decision |
| Self-paycheck recommendation | **out** | pure advice; customer executes |
| Tax-sweep | **on → out** | own-money, reversible; graduates via the trust ladder |
| **THE CREDIT GRANT** / limit change / **decline** | **on (never out)** | Annex III §5(b) high-risk **+ GDPR Art. 22(1)** |

**Precise regulatory phrasing (don't say we “dodge Annex III”):**
- The per-invoice **forecast** is non-credit capacity/warning → outside Annex III.
- The **grant** *is* Annex III §5(b) high-risk → human-on-the-loop **by design**.
- **GDPR Art. 22 applies NOW** (not deferred) to natural-person autónomos; **Annex III obligations phase in by 2 Dec 2027** (Digital Omnibus, [docs/01 line 59](01-client-and-evidence.md)).
- **Exposure is heterogeneous:** Art. 22 is *legally mandatory* for the **autónomo (natural-person)** sub-segment; an **SL is a legal person**. State: *“human-on-the-loop applies to ALL grants as policy; it is legally mandatory for the autónomo sub-segment.”*
- **Hard architectural assertion:** the non-credit model **SIZES and WARNS; it never auto-grants or auto-declines.**

**The earned-trust ladder (the agentic answer vs a rules engine):**
`Rung 1 SUGGEST` (AI shows, human acts — every credit-adjacent action starts here) → `Rung 2 DO-WITH-UNDO` (cheap, reversible, own-money; earned per-customer after a low correction rate) → `Rung 3 AUTONOMOUS` (repeatedly-correct reversible actions, e.g. tax-sweep). The rung is **earned per-action from realized outcomes, shown to the user, and can DEMOTE** if correction rate rises. **HARD CEILING:** the credit grant can never climb past human-on-the-loop, no matter how much trust accrues.

**Guard against automation bias:** force the reviewer to see top-3 drivers + confidence band; require a typed reason on every decline/edit; inject low-confidence cases; alert if any reviewer's override rate collapses toward zero.

---

## How predictions are explained to the customer

Three legibility modes on every surface: **PREDICTING** shows a confidence band; **RECOMMENDING** shows *“you decide”*; **ACTING** shows *“done — undo.”* Every credit term is expandable — *“Why only €3.2k / why this rate?”* → top 2–3 drivers in plain language, sourced from the interpretable **Logistic Regression coefficients** (or Tree paths). A decline **always** carries a specific, **human-signed** reason — never a black-box *“no.”*

---

## The closed-loop feedback flywheel

1. AI predicts (will this invoice be paid on time / days-late / grant terms).
2. Prediction drives an action (a display, or a human-on-the-loop bridge grant).
3. **Reality lands** — the client pays on day D, or defaults; the customer corrects a category; the reviewer edits/declines.
4. Predicted-vs-realized + the human decision + reason is logged **append-only** in the Decisions/Agents object.
5. On a cadence, **re-aggregate the `_asof_issuance` features with new realized labels and RETRAIN** — *with the grouped holdout intact and a fresh leakage re-screen each cycle.*
6. Sharper reliability → better-priced, safer bridges → better outcomes → more trust → more data → back to 1.

Two streams: **automatic outcome labels** (payment dates, defaults, category corrections — high-volume, retrain the heads) and **human feedback** (approve/edit/decline + reason, customer undos — lower-volume, higher-value: catches drift, calibrates pricing, supplies signed decline reasons). The objective profits when bridge-dependence **falls** — which is what incumbents structurally won't copy.

---

## Failure modes to pre-empt (and mitigations)

| Failure mode | Mitigation |
|---|---|
| **Group leakage / inflated AUC** | Payer-grouped holdout; show the gap slide; never trust a single-feature Rank AUC ~1.0 |
| **Target leakage** | Timestamp discipline; skip all post-outcome fields; re-screen every retrain |
| **Self-fulfilling reliability feature** | All `_asof_issuance`, trailing-only; drop the black-box score |
| **Synthetic-data self-leak** | Keep the generative parameter hidden; derive features from PAST draws only |
| **Automation bias / rubber-stamping** | Force driver+band view; typed decline reason; inject low-confidence cases; track override rate |
| **Calibration failure → mis-pricing** | Watch Calibration Plot each cycle; widen bands when data is thin |
| **Survivorship / selection bias** | State the AR-payment→would-be-bridged generalization assumption; fund a small randomized marginal hold-out |
| **Adverse selection** | Price on the specific named receivable; cap via client-concentration limits; human backstop on anomalies |
| **Concept drift** | Recency-weighted features; scheduled retrain; drift alerts |
| **Fairness / proxy-discrimination** | Auditable LogReg reason-string; exclude region from credit-side; group-error-rate slide |

---

## Dataset options for the demo

1. **Synthetic receivables table (recommended)** — N distinct payers each with a *hidden* lateness parameter; 10–60 invoices each over time; `_asof_issuance` features from PAST invoices only; `hash(payer_id)` split. **Never expose the generative parameter as a feature** (or AUC → ~1.0, masking the lesson). Best for demonstrating the grouped split.
2. **German Credit (UCI/Statlog)** — clean imbalanced binary classification warm-up for the full pipeline + calibration; *no cluster column*, so not for the moat narrative.
3. **Lending Club (Kaggle)** — realistic loan-DEFAULT story (candidate 4); construct a group key; heavy survivorship bias + many post-origination leakage fields (good leakage-hunting exercise).
4. **PSD2-style synthetic transactions** — mock Account/Transaction objects for the secondary cash-flow-gap model; aggregate to customer-period grain before Orange.
5. **Spain-flavored invoice synthetic set** — keyed to the ontology (terms, `client_id`, `sector_cnae`, realized `paid_date`); most on-thesis; pair with firmographics for the fairness slide.
6. **Telco-style churn** *(mention only)* — trivially clean but **off-thesis** (optimizes the engagement signal the thesis rejects).

---

## Open questions

- First-euro revenue: subscription vs bridge fee vs B2B2C attestation (docs/01 OQ1) — this model proves the **signal**, not the **monetization**.
- Lender licensing: hold a credit licence vs originate-and-refer (changes risk & margin, docs/00).
- Real retrain cadence + drift thresholds once the closed loop is live.
- EU AI Act / data-protection counsel review of the non-credit/credit split (docs/01 OQ5).
- Per-client cold-start policy: how conservative under low `n_payments_observed`?
