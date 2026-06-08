# 06 — Predictive Data Frontier *(functional-priority scan, ethics deferred)*

> Cumulative project, ESADE MIM *Data-Driven Prototyping with AI*. Builds on the ontology and the recommended first model in [`docs/05`](05-predictive-ai.md) (per-invoice late-payment / per-client reliability; companions = cash-flow shortfall and SME default). **This document maps the FULL predictive-data frontier BEYOND what we already collect, to MAXIMIZE predictive power, precision and EARLINESS.**
>
> **Team framing — read before reading anything else.** This is a **functional-priority** scan. We do **NOT** pre-filter on ethics or consent here. Aggressive, cross-customer, third-party, purchased, scraped, behavioral, device and inbox data is **included if predictive** — and each item is **TAGGED** with its legal/ethics risk, never dropped. The ethics/consent cut is a **separate, later team discussion**; it lives in the clearly-walled-off **Deferred Ethics/Legality Ledger (§4)** the team will use to cut later. **Functional ranking (§1–§3) and ethics tagging (§4) are kept in DISTINCT sections on purpose.**
>
> **Two hard rules that override the framing (same as docs/05):**
> 1. **LEAKAGE is a modeling error, not ethics.** Any feature only known *after* the outcome (target leakage) is flagged `is_leakage=true` and **excluded from the model** — see the separate **Leakage-Excluded list (§5)**. This is kept entirely apart from the ethics ledger.
> 2. **Don't invent capabilities.** Every item carries an honest **feasibility** call — can we actually obtain *and join* this data? The load-bearing feasibility assumption for half this frontier is one **entity-resolution layer** (below); where it is unproven, the power score is conditional.

---

## TL;DR

- **What we already have (the spine, not repeated here):** PSD2 bank feed, invoicing/AR + per-client reliability ledger, expense intelligence, payroll/cards, tax/VAT, product/financing usage, goals, firmographics.
- **The one unlock that governs this whole frontier:** **join the same PAYER entity (NIF/CIF + payer IBAN) across the WHOLE NetBank base.** The single-customer reliability ledger of docs/05 is structurally blind at `n_payments_observed = 0` — the exact cold-start moment a customer most needs the warning. Pooling *how a payer pays everyone* kills that blind spot and pulls earliness from **due-date** all the way forward to **engagement/contract-date**. This is the closed-loop moat finally **realized** as a private positive+negative payment bureau Spanish registries (RAI/ASNEF are negative-only) cannot match.
- **The load-bearing feasibility assumption (rule 2):** an **entity-resolution layer** mapping every free-text "Bill To" / PSD2 remitter string to a canonical payer (ideally the Spanish NIF/CIF). AR invoices legally carry the payer NIF → **deterministic match, build this first**. PSD2 remitter strings do **not** → fuzzy name+IBAN resolution is the **long pole** and is **unproven on NetBank data**. Without this join, the four flagship items are unbuildable.
- **Ship order (the Quick Wins, §3):** (1) counterparty public-distress join by NIF; (2) all-accounts cash-flow shortfall; (3) look-alike cohort prior; (4) contract-terms forward object; (5) inbox payer-intent layer.
- **The moat move, real but conditional and ethics-heavy:** the cross-customer shared-payer prior + pre-issuance score (§2 #1–#2). Highest power **and** highest ethics load — carried in §2, flagged **red** in §4.
- **Overclaims to discount (honest power caveats):** the AEAT/Crea-y-Crece feed **ramps to ~2028–2029** for our SME/autónomo segment (not day-1); psychometric/keystroke and in-app-telemetry credit features are weak **and** radioactive (drop, don't quarantine); external-scrape power scores are real *citations* but on closure/consumer/equity populations, **unproven on EU SME default**.

---

## §1 — The full data frontier, ranked by predictive power × feasibility (by family)

> **Power** = evidence-informed lift on the three target models (M1 per-invoice late-payment / per-client reliability — *the first model today*; M2 cash-flow shortfall; M3 SME default), 1–5. **Feas** = can we obtain AND join it (easy / medium / hard). **`is_leakage` rows are NOT in this functional table** — they are quarantined in §5. **Ethics flag is metadata only** — it does **not** down-rank the row (that is §4's job, deferred).

### Family A — Cross-customer network (the moat realization)

> **Scope:** items BEYOND the single-customer ledger in docs/05. The unlock is the **shared-identity join**: the same payer owes MULTIPLE NetBank customers, so we pool a payer's behavior across the whole base and score an invoice **before** the issuing customer has any history with that payer. **Every network feature must be a trailing `_asof_issuance` snapshot** computed only from payments realized across the base **before** this invoice's `issue_date` — pooling other customers' *future* payments is the network-form of target leakage (§5). **Grouped-holdout upgrade:** the group key escalates from "payer within a customer" (docs/05) to the **GLOBAL payer entity** (a payer in train must not appear in test *anywhere* in the base); the contagion model needs a **connected-component-aware** split.

| # | Item | Power | Feas | Sharpens / unlocks | Ethics flag (deferred → §4) |
|---|---|:---:|:---:|---|---|
| A1 | **Shared-payer global reliability prior** — payer's trailing realized days-late pooled across the ENTIRE base (`global_mean_days_late_asof`, `pct_paid_over_30/60/90d`, `n_distinct_creditors`, `n_payments_global`) | **5** | medium | **M1** + the before-issuance score; kills the `n_payments_observed=0` cold-start docs/05 can't touch; feeds M2/M3 | cross-customer-consent + Art 6/9/22 profiling of a non-customer payer — **red** |
| A2 | **Pre-issuance payer score** — at quote/contract/calendar time, emit "expect ~22d late, 12% chance >60d" with zero issuing-customer history (the headline *use* of A1) | **5** | medium | New surface: pulls earliness from due-date → engagement-date; pre-priced bridge at contract time | cross-customer-consent + Art 22 pre-relationship profiling — **red** |
| A3 | **Payer concurrent-delinquency / cross-creditor stress** (trailing) — is this payer *already* paying its OTHER NetBank creditors late? (`payer_pct_creditors_currently_overdue_asof`, `payer_recent_trend_days_late_asof`) | **5** | medium | Earliness on M1 + M3: detect a deteriorating payer weeks before it hits *this* customer | cross-customer-consent (share A's overdue to warn B) — **red** |
| A11 | **Cross-customer dunning/dispute echo** — does this payer routinely dispute / partial-pay / take credit-notes across its creditors? (`payer_dispute_rate_asof`, `payer_partial_pay_rate_asof`, `payer_avg_haircut_asof`) | **4** | medium | Distinguishes slow-but-pays-full from chronic short-payer → **bridge LGD**, not just timing | cross-customer-consent + reputational (de-facto shared blocklist) — **red** |
| A4 | **Look-alike cohort trajectory prior** — embed a thin-file *issuing* customer's firmographics, borrow k-nearest existing customers' realized late/shortfall base rates (`cohort_base_late_rate_asof`) | **4** | easy | **Customer-side** cold-start (docs/05 only solves payer-side); shrink M1/M2/M3 toward cohort at low own-n | fine-to-medium (aggregate); fair-lending if cohort key proxies protected — **green** |
| A6 | **Second-degree / contagion exposure** (your payer's payers) — propagate the biggest payer's own inflow health one hop (`my_payer_inflow_stress_asof`) | **4** | hard | Deepest earliness lever: "your client ACME is about to be squeezed because ITS client stopped paying" | cross-customer-consent, chains two hops; special-care if a hop is a natural person — **red** |
| A12 | **Payer-IBAN / remitter behavioral key** — resolve PSD2 inbound remitter name+IBAN to a payer even with NO invoice (cash/recurring clients) | 3 | medium | Coverage + hardens entity resolution (IBAN is a hard key); feeds every shared-payer feature | cross-customer-consent + GDPR silent-party data — **amber** |
| A5 | **Payer betweenness / hub position** in the who-pays-whom graph (`payer_in_degree_asof`, `payer_is_hub`) | 3 | medium | Hubs have idiosyncratic behavior a per-pair model misses; a hub going late = systemic portfolio risk | cross-customer-consent + competition-sensitive relationship map — **red** |
| A9 | **Network-implied effective concentration** — is the customer's #1 payer *itself* concentrated AND fragile? (`effective_concentration_asof`) | 3 | medium | Upgrades docs/05 `client_concentration_share` with network context for M2/M3 | cross-customer-consent (payer fragility from others' data) — **red** |
| A7 | **Cluster-default / connected-component contagion** — is this payer inside a component where realized delinquency is rising? (`component_recent_late_rate_asof`) | 3 | hard | Portfolio M3 + correlated-loss / concentration-limit warning (the bridge book's tail) | cross-customer-consent + special-category if component = sensitive sector — **red** |
| A10 | **First-time-payer population base rate** — realized late-rate of FIRST invoices to never-seen payers, by payer segment (`new_pair_base_late_rate_by_segment_asof`) | 3 | easy | Hardest cold-start (both customer-payer pair new): calibrated prior vs flat | fine (coarse aggregate); fair-lending if segment = protected proxy — **green** |

### Family B — Real-time third-party / purchased / bureau feeds

> **Scope:** real-time + third-party/purchased/joinable feeds beyond the first-party stack. **Spain has NO unified company-data API** — feasibility is honest per item. BORME is reachable via `data.boe.es` (JSON/XML); Cuentas Anuales are scanned PDFs across 52 provincial registries (hard, or buy from Informa/Iberinform); RAI/ASNEF are bureau-licensed feeds (a lender plausibly qualifies on legitimate interest), **not scrapes**.

| # | Item | Power | Feas | Sharpens / unlocks | Ethics flag (deferred → §4) |
|---|---|:---:|:---:|---|---|
| B1 | **Counterparty concurso/insolvency match** (BORME + Registro Público Concursal) joined by NIF to each client in the AR ledger | **5** | medium | **M1**: a counterparty's *public* distress is an ex-ante predictor of whether THAT client pays THIS invoice (no leakage); M2 concentration | **green** — public gazette; subject is the counterparty, not our customer |
| B3 | **Cross-customer payer-reliability graph** — aggregate every customer's AR + AEAT-confirmed payments by DEBTOR into a private positive+negative bureau | **5** | medium | **M1** most directly; M3 via concentration; **the closed-loop moat** (positive signal bureaus lack) | cross-customer-consent + GDPR purpose-limitation; payer is a non-customer subject — **red** |
| B2 | **AEAT / Crea-y-Crece per-invoice lifecycle feed** — accept/reject + **actual payment date** reported per B2B e-invoice (official late-payment monitoring tool) | **5** | medium | **M1** transformed from self-reported AR → AEAT-verified payer history; M3 aggregate distress. ⚠️ *paid-date of the scored invoice = target (§5); GOLD only over PRIOR invoices* | GDPR tax-data + AEAT-access-rights-uncertain; **phased — ramps ~2028–2029 for our segment** — **amber** |
| B11 | **Commercial-bureau composite scores & financials** (Iberinform RiskScore, Informa D&B, Axesor — RAI/ASNEF/filed accounts/25 alert types, daily) | **4** | easy | M3 ready-made PD prior/challenger + orthogonal financials; M1 via payer score; alerts add earliness (concurso filing before payment stops) | fine / licensed (~€1k+ APIs); validate vintage — score may embed current arrears (partial-leakage, §5) — **green** |
| B4 | **CIRBE** (Banco de España central credit register) — system-wide loan+guarantee exposure >€1k, monthly | 4 | medium | **M3** over-indebtedness; M2 debt-service burden — leverage NetBank can't see | fine-with-borrower-consent (access needs data-subject authorization; autónomo special handling) — **amber** |
| B5 | **RAI** (unpaid accepted-bills register) on payers AND borrowers, ≥€300.51 | 4 | easy | **M1** (payer defaulting on signed paper) + M3; legal entities only (excludes autónomos) | fine for legitimate-interest credit use; a RAI entry dated *after* the scored invoice's due-date = leakage for that invoice (§5) — **amber** |
| B6 | **ASNEF-Empresas (Equifax) + EBE/Experian** default files via API | 4 | easy | **M3** screening gate; M1 payer-side enrichment for payers outside the network | fine (regulated reference use); negative-only → limited earliness — **amber** |
| B8 | **BOE/BORME + concurso + Registro Mercantil corporate-event monitoring** on borrowers AND payers (insolvency, embargo, director/ownership change, charges, filing delays) | 4 | easy | **M3** + M1 payer-collapse; **high earliness** (insolvency filing precedes non-payment); joinable by NIF | fine (public legal gazette); a filing after the outcome window = leakage for that invoice (§5) — **green** |
| B9 | **Real-time open-banking aggregation of ALL connectable accounts** (secondary banks, autónomo personal accounts, savings) beyond the primary PSD2 feed | **5** | medium | **M2 + M3**: overdraft/NSF frequency + income + balances explain most variance and **PRECEDE bureau/missed-payment events by weeks** | fine-under-PSD2 (permissioned); autónomo personal-account access blurs B2C — **amber** (green for business accounts) |
| B10 | **Stripe / payment-processor webhooks** — gross volume, dispute/chargeback rate, refund rate, processing consistency, payment-success rate, customer-base breadth | 4 | medium | **M2 + M3** (revenue decline, rising disputes = early distress); M1 issuer health — exactly what Stripe Capital underwrites on | fine-with-merchant-OAuth-consent — **green** |
| B12 | **AEAT/SII near-real-time VAT ledger** — declared sales/purchases VAT-base trajectory, VAT-deregistration / non-filing | 3 | hard | **M2** revenue contraction + **M3** (deregistration = strong distress); cross-checks M1 invoice authenticity | tax-secrecy; access only via customer authorization/Cl@ve; third-party VAT not accessible — **amber** |
| B13 | **Data-broker firmographic-risk datasets** — sector growth, employee-count deltas, web/traffic presence, trade-payment indices, hiring signals | 2 | medium | **M3** + macro overlay for M2; modest orthogonal lift, thin-file payers, sector concentration | ToS/data-broker provenance + GDPR lawful-basis for purchased data — **amber** |

### Family C — Deep behavioral / inbox / device

> **The one big idea:** the highest-value unlock here is **NOT** device/psychometrics — it is **parsing the customer's OWN inbox/docs for PAYER-SIDE intent.** The structured spine is blind to a payer until a payment is late (a lagging label); the payer's promises/excuses/disputes land in the **customer's** mailbox **days-to-weeks earlier**. **Asymmetry that governs feasibility:** NetBank can OAuth its *own customer's* inbox/calendar/drive; it almost never sees the *paying client's*. So payer signal is reconstructed from artifacts arriving in the customer's mailbox — never from instrumenting the payer (that is a fantasy). **Distill inbox signal into the same trailing reliability ledger** (`payer_promise_break_rate`, `avg_days_from_promise_to_pay`, `payer_dispute_rate_asof`), not raw text — preserving the grouped-payer holdout and point-in-time discipline. **Anti-hype:** in-app telemetry, typing dynamics, geolocation and psychometric proxies are LOW signal for B2B receivable/repayment risk (the outcome depends on the *payer* and on cash flows already in PSD2); their honest use is the **quarantined fraud lane** at onboarding, never the credit-capacity model.

| # | Item | Power | Feas | Sharpens / unlocks | Ethics flag (deferred → §4) |
|---|---|:---:|:---:|---|---|
| C1 | **Connected inbox — PAYER reply-thread intent** (promise-to-pay dates, "cash is tight / waiting on our own client", dispute / "we never received it", change-of-AP-contact) extracted per receivable | **4** | medium | **M1 earliness** (anticipates lateness before PSD2/AR shows it); feeds `payer_promise_break_rate` / `avg_days_from_promise_to_pay` into the ledger; M2 timing | Art-9-adjacent distress inference + third-party email content + restricted-Gmail (CASA) + AI-Act profiling — **red** |
| C11 | **Inbox-derived PAYER firmographic/distress enrichment** aggregated across many customers' mailboxes (same payer domain bouncing / going silent / layoff auto-replies) — a consortium payer-intelligence network | **4** | hard | **M1 + M3** for any customer exposed to that payer; strengthens the moat into a multi-tenant network | cross-customer-consent + third-party payer data + competition/data-sharing review — **red** |
| C3 | **Uploaded CONTRACTS / POs / SOWs** (doc upload + OCR/LLM term extraction) — payment-terms-vs-invoiced mismatch, milestone/retention %, penalty/late-interest clauses, contract end/renewal | **4** | medium | **Unlocks a contract-terms object**: true expected-pay schedule (M2), bridge sizing vs committed milestones, concentration on *committed backlog*, non-renewal warning | third-party-consent (counterparty terms) + NDA/confidentiality; otherwise low (customer-owned) — **green** |
| C9 | **Device fingerprint + network/IP intelligence** (device ID, OS/integrity, emulator/root, IP reputation, SIM/eSIM, velocity across accounts) | 4 | easy | **Onboarding FRAUD / synthetic-identity** (legitimate, non-credit lane); near-zero value for repayment CAPACITY | fine for fraud/security lane; **MUST NOT enter the credit model** (proxy/fair-lending) — **green** (fraud-lane-only) |
| C4 | **Connected inbox — supplier / order-confirmation / SaaS-renewal parsing** (Amazon Business, AWS/GCP/OpenAI bills, supplier ARs) | 3 | easy | **M2**: forward committed OUTFLOWS + input-cost inflation not yet in PSD2; net-burn forward estimate | restricted-Gmail (CASA) + some third-party content; mostly own commercial mail — **amber** |
| C13 | **Connected DRIVE mining beyond contracts** — other-account statements, tax filings, management P&L, prior-lender term sheets (debt-stacking) | 3 | medium | **M3** true leverage / **debt-stacking detection**; completes the balance sheet PSD2 misses | broad-Drive scope (CASA) + third-party personal data in docs; data-minimisation — **amber** |
| C5 | **Connected CALENDAR** — invoiceable-work cadence, client-meeting density, milestone/delivery dates, end-of-engagement signals | 2 | easy | **M2** forward inflow timing; client-churn / revenue-cliff early warning. Weak on a *specific* payer's lateness | third-party-consent (attendee data) + behavioral-surveillance optics if fed to credit — **amber** |
| C7 | **In-app telemetry** — "what they check before payday", balance-refresh frequency, pre-payroll checking, time-of-day usage | 2 | easy | Marginal cold-start nudge — but **PSD2 already shows the thin runway**; confounded by engagement (which the product's anti-engagement objective suppresses) | behavioral-profiling + dark-pattern optics; contradicts product objective — **red** |
| C8 | **Application-flow micro-behavior** — time-on-field, edits, retries, copy-paste of income, back-and-forth on amount | 2 | medium | Application-**FRAUD** / first-payment-default screen at onboarding; NOT the credit-capacity model | behavioral-profiling; fair-lending-toxic if it leaks into credit — quarantine to fraud lane — **red** (credit) / green (fraud) |
| C10 | **Geolocation** — business-location consistency & impossible-travel (login geo vs KYC vs IP) | 2 | medium | **Onboarding fraud / ATO**. As a credit feature it proxies REGION — already excluded by docs/05 → fraud-lane only | GDPR location + region-proxy / fair-lending-toxic in credit lane — **red** (credit) / amber (fraud) |
| C14 | **Psychometric / typing-dynamics / linguistic-style scoring** (keystroke biometrics, conscientiousness proxies) | 1 | hard | Theoretically thin-file M3 — but for cash-flow-positive businesses with PSD2+AR the lift collapses; evidence is consumer/unbanked, segment-mismatched. **Mostly noise** | Art-9 biometric + AI-Act profiling + fair-lending-toxic + reputationally radioactive — **red, recommend DROP** |

### Family D — External / scraped / alternative

> **The big idea — two uses of the same data, opposite leakage status.** Almost every registry/scrape signal can point at (a) the **borrower** or (b) the borrower's **counterparties** (the clients already named in NetBank's AR ledger — NetBank's unique join). Pointed at a **counterparty**, these are clean **ex-ante** predictors of whether *that client* pays *this invoice* (no leakage); pointed at the **borrower itself**, a formal insolvency/RAI listing **IS** the default outcome (leakage, §5). **Feasibility honesty:** entity-resolving a micro-firm/freelancer to its Google/Trustpilot/LinkedIn/web presence is the real bottleneck; coverage is biased toward digitally-visible firms — itself a fair-lending concern. **Power-grounding:** scores are **evidence-informed** from cited literature on **closure/equity/consumer** signals (Berg et al. 2020 RFS; Naumzik et al. 2022 Marketing Science), **NOT field-proven on NetBank's own EU-SME default label** — treat as hypotheses to validate.

| # | Item | Power | Feas | Sharpens / unlocks | Ethics flag (deferred → §4) |
|---|---|:---:|:---:|---|---|
| D1 | **Counterparty concurso/insolvency match** (BORME + RPC) joined to AR ledger *(= B1, the external-family framing of the highest-value item)* | **5** | medium | **M1** primary + M2 concentration; counterparty distress predicts whether THIS client pays | **green** — public registry; counterparty is the subject |
| D4 | **Counterparty RAI listing** joined to AR ledger (legal persons, ≥€300) | **5** | medium | **M1**: a client newly in RAI is failing on commercial paper → predicts paying our customer late | special-category-adjacent / legitimate-interest; bureau feed not scrape; derived-data fairness flag — **amber** |
| D3 | **Leading corporate-distress events on the BORROWER in BORME** (capital reduction, director churn, registered-office change, auditor change) | 4 | medium | **M3** + M2 — genuine *leading* indicators available before the terminal event → usable ex-ante | fine (public registry; benign corporate events) — **green** |
| D13 | **Director/UBO cross-firm network** (BORME officer graph) — serial-failure links, related-party / circular-invoicing | 4 | hard | **M3** + fraud + M1 related-party detection | GDPR guilt-by-association on natural-person directors; entity resolution error-prone — **red** |
| D7 | **Litigation & embargo signals** (court executions, *monitorio*, BOE edictos, AEAT Art.95 + Seguridad Social debtor lists) | 4 | hard | **M3** + M1 counterparty — strong leading distress signal preceding insolvency | GDPR-sensitive + court-data ToS limits; debtor lists politically sensitive in lending — **amber** |
| D9 | **Online-review SEQUENCE & VOLATILITY** (Google/Trustpilot/TripAdvisor) — *volatility*, not mean rating | 4 | medium | **M3** early warning (~78% balanced-acc failure prediction in lit.); M1 for consumer-facing clients | ToS-scraping (Trustpilot has API); segment bias vs B2B/invisible firms — **amber** |
| D11 | **Commercial-bureau composite scores & financials** *(= B11)* — Informa D&B / Iberinform / Axesor + Law 16/2022 insolvency-risk class | 4 | easy | **M3** benchmark/challenger; M1 counterparty score; thin-file backfill; cleanest path to structured Cuentas Anuales | fine / licensed; watch embedded-arrears partial-leakage (§5) — **green** |
| D5 | **Missing / late annual-accounts filing** (Cuentas Anuales depósito gap) | 3 | hard | **M3** + M1 counterparty — filing-behavior-as-feature works even when financials are unparseable | fine (public status); coverage bias — micro-firms file late routinely → fair-lending false positives — **amber** |
| D8 | **Hiring-trend signals** (careers page + LinkedIn/InfoJobs/Indeed via PredictLeads/Aura) — direction & volatility of open roles | 3 | medium | **M2** + M3 early warning; growth/limit-increase eligibility | ToS-scraping (buy via licensed providers); thin coverage for <10-employee firms — **amber** |
| D10 | **Review TEXT content & velocity** (NLP on review corpus) | 3 | hard | **M3** short-horizon closure prediction (~70% at 3 months in lit.) | ToS-scraping + special-category leakage in free text (needs scrubbing) — **amber** |
| D14 | **Web-presence existence & quality** (live site, SSL, recent updates, e-commerce/booking stack via BuiltWith/Wappalyzer) | 3 | easy | **M3** + thin-file underwriting (digital footprint matched bureau scores in Berg et al.) | fine for own-site fetch; penalizes offline-but-healthy traditional firms → digital-divide proxy — **amber** |
| D12 | **Website-traffic & app-store trend** (SimilarWeb/Semrush/Apptopia) | 3 | medium | **M2** + M3 + growth/limit-increase for digitally-monetizing firms | ToS/licensed; coverage cliff below a traffic threshold → bias toward larger/digital firms — **amber** |
| D16 | **News / adverse-media & sector-sentiment** (RavenPack-style NLP + NACE-sector aggregate) | 2 | medium | **M3** + M2 sector shock + portfolio concentration; cheap high-coverage prior when firm-level data is thin | ToS/fair-lending — sector-as-feature can proxy protected attributes / redline-by-industry — **amber** |

---

## §2 — The ranked game-changer predictions (the honest uplift story)

> **Functional ranking by `game_changer` score (5 = step-change). Ethics tags carried, NOT down-ranked** (that is §4). Each prediction states the honest **precision vs earliness** story and its **feasibility conditionality**. All respect docs/05's two hard rules: every prediction **SIZES and WARNS — none auto-grants**; the credit grant stays **human-on-the-loop** (Annex III §5(b) + GDPR Art 22) with a plain-language top-drivers explanation.

### 🥇 #1 — Before-you-send-it invoice score (pre-issuance late-payment forecast) — `game_changer 5`
- **Predicts:** at contract/quote/calendar time — *before an invoice exists* — expected days-late and P(>30/60d) for billing a specific payer, with **zero issuing-customer history**. Output: "expect ~22d late, 12% chance >60d" + a pre-priced bridge at engagement-date.
- **Enabled by:** A1 shared-payer global reliability prior. **Load-bearing dependency = entity resolution** (AR NIF deterministic match first; PSD2 remitter fuzzy name+IBAN is the long pole). B2 AEAT feed later upgrades self-reported AR → government-verified history.
- **ML type:** classification `P(paid_late)` + regression head (expected days-late) for bridge pricing; **Bayesian shrinkage toward the global prior** when own-n is small.
- **Uplift:** **EARLINESS** — moves the prediction point from due-date to engagement-date (weeks-to-months earlier) and turns the cold-start from a flat prior into a calibrated payer-specific forecast. **PRECISION** — largest single AUC lift on the cold-pair population the single-customer model *cannot score at all*.
- **Feasibility:** **medium, CONDITIONAL** — real for the AR-covered (deterministic-NIF) population; demote to "real-but-bounded" until fuzzy PSD2 resolution is proven on NetBank data.
- **Ethics (deferred → §4 red):** cross-customer-consent + Art 6/9/22 profiling of a non-consenting, often natural-person autónomo payer. **Highest power AND highest ethics load.**

### 🥈 #2 — Cross-creditor payer-deterioration early warning (contagion radar) — `game_changer 5`
- **Predicts:** as of issuance, that a payer is *already* going bad — slowing / paying its OTHER NetBank creditors late RIGHT NOW — weeks before that deterioration reaches THIS customer.
- **Enabled by:** A3 cross-creditor stress + C11 inbox-derived payer-distress + B8/B5/D7 public corporate-event monitoring (BORME concurso, capital reduction, RAI, litigation joined by NIF). **Strict `_asof_issuance`:** only PAST cross-customer outcomes admissible (the future-delinquency join is the §5 trap).
- **ML type:** classification / survival (time-to-deterioration); change-point / trend detection on pooled trailing payer behavior; feeds M1 and M3.
- **Uplift:** **EARLINESS** — a payer going bad shows against the whole base at once; inbox/registry leading events add days-to-months over the AR ledger flipping overdue. The most **actionable** early-warning in the product.
- **Feasibility:** **medium** — power=5 holds for the cross-creditor AR component (density-dependent → weaker early in NetBank's life); inbox-bounce + registry sub-signals are hard/medium.
- **Ethics (deferred → §4 red):** cross-customer-consent + third-party-payer profiling + inbox third-party content + restricted-Gmail (CASA). Registry sub-signals are green; the cross-creditor + inbox layers are the red ones.

### 🥉 #3 — Counterparty public-distress join (registry-fed per-client reliability) — `game_changer 5`
- **Predicts:** that a named client in the AR ledger pays THIS invoice late or not at all, because that client's **public** distress (concurso/pre-concurso, RAI, embargo/litigation, missing accounts, capital reduction) is matched by NIF as an ex-ante feature.
- **Enabled by:** B1/D1 BORME+RPC, B5/D4 RAI, D7 litigation, D5 missing-accounts, B11 bureau alerts. **Load-bearing edge = NetBank already knows each customer's clients by tax ID. CRITICAL leakage split:** these signals on a **COUNTERPARTY** are NOT leakage; the SAME signal on the **BORROWER ITSELF** is the default event (`is_leakage=true`, §5) — label/monitoring only.
- **ML type:** feature-enrichment into M1 + a real-time monitoring/alert stream feeding limits + collections triage.
- **Uplift:** **EARLINESS** — insolvency filing / RAI / litigation precedes non-payment, often by months. **PRECISION** — hard confirmation on the tail.
- **Feasibility:** **medium, buildable today** — BORME via `data.boe.es`; bureau feeds buyable (Iberinform ~52 DaaS APIs, entry ~€1k).
- **Ethics (deferred → §4 green/amber):** **green** for public-registry counterparty data; **amber** for RAI/ASNEF (bureau-licensed, legitimate-interest). **Highest-power, LOWEST-ethics-friction play in the whole frontier.** *(Leakage discipline: a filing dated after the scored invoice's due-date is leakage for THAT invoice, §5.)*

### #4 — Complete-balance-sheet cash-flow shortfall forecast — `game_changer 4`
- **Predicts:** P(shortfall in next 30d) + the dated low-point, using the customer's **true total liquidity across every connectable account** (not just the primary feed) plus live processor revenue.
- **Enabled by:** B9 all-accounts open banking + B10 Stripe webhooks + B12 VAT trajectory. Chargeback/dispute on the *specific scored transaction* excluded (§5).
- **ML type:** classification (shortfall y/n) + time-series low-point forecast; consumes M1 per-client probabilities as features; **customer-period grouped holdout**.
- **Uplift:** **EARLINESS** — cash-flow stress is the CAUSE; missed payments the EFFECT — overdraft/income/balances explain most variance and precede bureau events by weeks. **PRECISION** from completeness (the second bank / autónomo personal account is where hidden stress lives).
- **Feasibility:** **medium** — PSD2-permissioned; the variance driver is completeness of accounts NetBank doesn't hold.
- **Ethics (deferred → §4 green/amber):** **green** for business accounts + Stripe OAuth; **amber** for autónomo personal-account reach (B2C / natural-person line).

### #5 — Inbox payer-intent earliness layer (promise-to-pay & dispute radar) — `game_changer 4`
- **Predicts:** that THIS receivable settles late (and updates the payer's general reliability) by reading the payer's own words in the **customer's** mailbox — promise-to-pay, "cash is tight", disputes, "we never received it", change-of-AP-contact.
- **Enabled by:** C1, **distilled into trailing ledger features** (`payer_promise_break_rate`, `avg_days_from_promise_to_pay`, `payer_dispute_rate_asof`), NOT raw text. **HARD leakage gate:** the customer's OWN outbound dunning, renegotiated due dates, credit-notes and remittance-advice for the SAME invoice are post-outcome (§5) — usable only for the NEXT invoice; gate on `artifact_timestamp < issue_date`.
- **ML type:** NLP/LLM extraction → distilled trailing reliability features feeding M1 + bridge-LGD; strict as-of-issuance join.
- **Uplift:** **EARLINESS** — payer intent appears days-to-weeks before PSD2/AR shows overdue; this is **data Verifactu/SII/Holded do NOT have** (defends the moat). **PRECISION** — dispute/promise-break sharpen expected-recovery and **bridge LGD** beyond pure timing.
- **Feasibility:** **medium** — restricted-Gmail scope requires an annual Google **CASA** security assessment (real eng/legal cost, not free).
- **Ethics (deferred → §4 red):** Art-9-adjacent distress inference + third-party email content + CASA + AI-Act profiling if it touches the autónomo credit lane.

### #6 — Contract-terms forward cash-flow object — `game_changer 4`
- **Predicts:** the TRUE expected-payment schedule and committed backlog from uploaded contracts/POs/SOWs — terms-vs-invoiced mismatch, milestone/retention %, penalty clauses, end/renewal windows.
- **Enabled by:** C3 OCR/LLM term extraction + C5 calendar cadence + C4 inbox supplier/renewal parsing for committed OUTFLOWS.
- **ML type:** document IE → structured contract object feeding the M2 cash-flow forecast + concentration features.
- **Uplift:** **EARLINESS** — forward-dated milestones + renewal/notice windows give weeks-to-months of advance timing and a revenue-cliff/non-renewal warning before the AR gap appears. **PRECISION** — confirmed contractual terms replace inferred ones; concentration measured on **committed backlog**, not just past invoices.
- **Feasibility:** **medium** — customer-owned documents, low third-party load.
- **Ethics (deferred → §4 green):** third-party-consent (counterparty terms) + NDA exposure; otherwise low.

### #7 — Look-alike cohort prior for thin-file customers — `game_changer 4`
- **Predicts:** a calibrated base late-rate + shortfall frequency for a brand-NEW issuing customer with 2 invoices, by borrowing its k-nearest existing customers' realized outcomes.
- **Enabled by:** A4 + A10 (pure aggregates over the base — **lowest-consent-risk cross-customer features**). Shrink toward cohort when own-n is small.
- **ML type:** kNN/embedding Bayesian prior + hierarchical shrinkage into M1/M2/M3.
- **Uplift:** **PRECISION/CALIBRATION** — replaces a flat prior with a cohort-calibrated start at low-n; gives a usable score on **day one** instead of "after enough history". Solves the **customer-side** cold-start docs/05 omits.
- **Feasibility:** **easy.**
- **Ethics (deferred → §4 green):** aggregated cohort priors are low-risk; fair-lending flag if the cohort key (sector/region) proxies protected — keep sector low-cardinality, exclude region per docs/05.

### #8 — Network concentration & contagion-cluster portfolio risk — `game_changer 3`
- **Predicts:** portfolio-level correlated-loss + per-customer single-point-of-failure — `effective_concentration_asof`, hub in-degree, `component_recent_late_rate_asof`.
- **Enabled by:** A5/A9/A6/A7 graph features + D13 director/UBO graph. Needs **connected-component-aware splitting** so graph neighbors don't leak across the holdout.
- **ML type:** graph features (centrality, component stats) + GNN/network propagation into M3 + portfolio concentration.
- **Uplift:** **EARLINESS** on systemic risk (a hub/cluster deteriorating warns the whole exposed portfolio); **PRECISION** on tail/correlated loss + concentration limits, not marginal per-invoice AUC.
- **Feasibility:** **hard, UNPROVEN** — second-degree requires the hop to be in-base (sparse); director/UBO is legally fraught + entity-resolution-error-prone. **Research bet, validate against NetBank's realized loss label.**
- **Ethics (deferred → §4 red):** cross-customer-consent + competition-sensitivity + guilt-by-association on natural-person directors.

### #9 — Onboarding fraud / synthetic-identity screen (quarantined fraud lane) — `game_changer 3`
- **Predicts:** at onboarding — synthetic-identity, ATO, first-party / multi-account fraud (one device opening many businesses, emulator/datacenter IP, impossible-travel, device reuse, form hesitation).
- **Enabled by:** C9 device fingerprint + C8/C10 behavioral/geo. **Strong, well-established for FRAUD; weak/emerging for direct default.**
- **ML type:** fraud classification / anomaly detection, **strictly separated** from the credit-capacity pipeline.
- **Uplift:** **PRECISION on fraud loss** (protects the whole loan book); **near-zero legitimate lift on repayment CAPACITY** — deliberately NOT a credit-precision claim.
- **Feasibility:** **easy.**
- **Ethics (deferred → §4 green/red):** **green** in the fraud/security lane (legitimate-interest); **fair-lending-TOXIC and Art-9/AI-Act-radioactive if it leaks into the credit lane** (geo proxies region; biometrics = Art-9). Psychometric/keystroke scoring (C14) should be **dropped**, not just quarantined.

---

## §3 — QUICK WINS (highest power-per-effort, lowest-risk to ship first)

> Ranked by **power-per-effort × low ethics/leakage friction**. Ship in this order.

1. **Counterparty public-distress join by NIF** (B1/D1 + D3 + B8) — **highest power, lowest ethics friction (green), buildable today.** BORME via `data.boe.es` JSON; match each AR-ledger client's tax ID against concurso/pre-concurso + leading corporate-distress events. Public data, the counterparty is the subject, and it sharpens the **first model (M1)** directly. The cleanest faculty-defense (public + counterparty, leakage-split enforced).
2. **All-accounts cash-flow shortfall** (B9 business accounts + B10 Stripe webhooks) — **green / PSD2-permissioned**, drives most M2/M3 variance, leads missed-payment events by weeks. Powers the "safe-to-borrow: €X" hero directly. *(Defer the autónomo personal-account reach to the amber pass.)*
3. **Look-alike cohort prior** (A4 + A10) — **easy, green, pure aggregate.** The safest cross-customer feature and the **customer-side cold-start docs/05 omits** — de-risks the low-history population with almost no consent load.
4. **Contract-terms forward object** (C3) — **green, customer-owned documents.** Net-new committed-backlog object; OCR/LLM extraction is feasible; sharpens M2 + bridge sizing more than any behavioral micro-signal.
5. **Commercial-bureau composite score / financials** (B11/D11 — Iberinform/Informa) — **easy, licensed, ~€1k entry.** Orthogonal M3 challenger + cleanest path to structured Cuentas Anuales + alerts add earliness. *(Validate score vintage — embedded current arrears = partial leakage on the borrower, §5.)*
6. **Inbox payer-intent layer** (C1, distilled) — slightly higher effort (CASA assessment) and **red** ethics, but the **genuine earliness lever** — flagged here because the *engineering* payoff is high; gate it behind the ethics pass.

**Deliberately NOT a quick win:** the cross-customer shared-payer prior / pre-issuance score (#1–#2 in §2). It is the biggest *power* lift but it depends on the unproven fuzzy-resolution long pole AND carries the heaviest (red) ethics load — sequence it after the entity-resolution layer is proven and the ethics pass is done.

---

## §4 — DEFERRED ETHICS / LEGALITY LEDGER *(separate later team discussion — the cut list)*

> ⚠️ **This section is the ONLY place ethics gates a decision. It is deferred — the team uses it to cut later.** Power/feasibility in §1–§3 was **not** down-ranked for anything here; these tags are **metadata**. Tiers: 🟢 **green** = low friction, ship; 🟡 **amber** = lawful with a specific basis/consent/contract, needs a path; 🔴 **red** = heavy consent/profiling/special-category load — explicit later call (some recommend-drop). **The ethics GRADIENT, not a verdict.**

### 🟢 GREEN — low friction, defensible, ship first
| Item | Why green |
|---|---|
| **Counterparty public-distress join** (BORME / RPC / concurso) matched by NIF (B1/D1/D3) | Official public-gazette data; the data subject is the **counterparty**, not our customer. Minor fair-lending note (penalizing a borrower for a client's distress). |
| **Look-alike cohort prior + first-time-payer base rates** (A4/A10) | Aggregated cohort priors are low-risk. Only flag: fair-lending if the cohort key (sector/region) proxies protected — keep sector low-cardinality, exclude region per docs/05. |
| **All-accounts open banking — BUSINESS accounts + Stripe merchant-OAuth** (B9 business / B10) | PSD2 / merchant-OAuth **permissioned** data; data-minimisation + consent-scope are routine. Lowest-friction high-power credit-side feature. |
| **Uploaded contracts / POs / SOWs** (C3) | Customer-owned; residual is only third-party counterparty terms / NDA-confidentiality. |
| **Commercial-bureau composite scores & financials** via licensed API (B11/D11) | Vendor-licensed, GDPR-covered by the bureau; routine credit-reference use. *(Watch embedded-arrears partial-leakage — a modeling concern, §5, not ethics.)* |
| **Device fingerprint + IP/geo in a hard-quarantined FRAUD lane only** (C9) | Legitimate-interest + security purpose for synthetic-ID/ATO at onboarding — green **only** while strictly walled off from the credit-capacity model (same signals are red the moment they touch credit). |
| **BORME leading corporate-distress events on the borrower** (D3) | Public registry; benign corporate events (capital reduction, director change), low sensitivity; genuine ex-ante leading indicators. |

### 🟡 AMBER — lawful with a specific basis / consent / contract; needs a path
| Item | The path / the catch |
|---|---|
| **AEAT / Crea-y-Crece per-invoice payment-status feed** (B2) | GDPR tax-data + third-party-payer purpose-limitation; **AEAT-repository third-party access rights unconfirmed**; phased mandate → partial/biased coverage until ~2028–2029 for our segment. Lawful basis hinges on the published repository access terms. |
| **RAI / ASNEF-Empresas counterparty listings** (B5/B6/D4) | Bureau-licensed: needs legitimate-interest membership (a lender plausibly qualifies — a **contracted feed, NOT a scrape**). Derived-data fairness flag. Negative-only → limited earliness. |
| **Litigation / embargo / AEAT Art.95 + Seguridad Social debtor lists** (D7) | Public but court-data scraping has ToS/access limits in Spain; debtor lists politically sensitive in lending; special-category leakage in free-text. Needs a lawful-access path, not a scrape. |
| **CIRBE total-leverage report on the borrower** (B4) | Lawful but access requires the **data-subject's explicit authorization**; autónomo (natural-person) special handling. |
| **All-accounts open banking incl. autónomo PERSONAL accounts** (B9 personal) | PSD2-permissioned, but pulling a natural-person autónomo's *personal* account blurs the B2C/GDPR line — tight consent-scope + data-minimisation. The lift is real; the personal-account reach is the amber part. |
| **Connected calendar / drive mining** (C5 / C13 / C4) | Broad-Drive/Calendar OAuth scope (CASA) + third-party personal data in documents + behavioral-surveillance optics if fed to credit. Debt-stacking detection is valuable but purpose-limited. |
| **Hiring-trend / review-volatility / web-traffic scraped alt-data** (D8/D9/D10/D12/D14/D16) | ToS-scraping (LinkedIn/Indeed/Google/TripAdvisor prohibit — **buy via licensed providers**); free-text can surface Art-9 attributes (scrub); coverage bias toward digitally-visible firms is a fair-lending selection problem for the <10-employee/freelancer target. |
| **Payer-IBAN / remitter behavioral key** (A12) | Cross-customer + GDPR silent-party (PSD2) data on natural-person remitters; aggregate-only mitigations. |

### 🔴 RED — heavy consent / profiling / special-category load; explicit later call
| Item | The load |
|---|---|
| **Shared-payer global reliability prior** (A1) | cross-customer-consent: A's data prices B's invoice; payer is a non-customer who never consented, frequently a natural-person autónomo → GDPR Art 6 (no basis from the payer), Art 9 (if distress inferred), Art 22 (profiling affecting the issuing customer). Aggregation does NOT cure re-identification when one dominant payer drives a small-n aggregate. **Highest-power AND highest-ethics-load — carried, not dropped.** |
| **Pre-issuance payer score** (A2) | Profiling a non-consenting third-party payer **pre-relationship** + Art 22 + data-minimisation (scoring a payer who may never be billed). |
| **Cross-creditor payer-deterioration / contagion radar** (A3) | cross-customer-consent + third-party profiling; effectively a private shared delinquency register on non-consenting payers; competition/data-sharing review. *(Its registry sub-signals are green; the cross-creditor AR + inbox layers are the red ones.)* |
| **Cross-customer dunning/dispute echo / shared blocklist** (A11) | cross-customer-consent + reputational — a de-facto shared blocklist of bad-paying counterparties. |
| **Inbox payer-intent layer** (C1) | third-party-consent (the payer's email the customer cannot waive) + Art-9-adjacent distress inference + restricted-Gmail CASA + AI-Act profiling if it touches the autónomo credit lane. |
| **Inbox-derived payer enrichment across many mailboxes (consortium network)** (C11) | cross-customer-consent (A's inbox scores B's payer) + third-party payer data + significant purpose-limitation + competition review. Heaviest combined consent load. |
| **Payer betweenness / hub + network effective concentration** (A5/A9/A7) | cross-customer-consent + competition-sensitive who-owes-whom mapping + special-category if a component maps to a sensitive sector. |
| **Second-degree contagion + director/UBO graph** (A6/D13) | Chains consent two hops; guilt-by-association profiling of natural-person directors risks discrimination claims; commercially sensitive. *(Also feasibility-weak — see §2 #8.)* |
| **In-app telemetry as a credit feature** (C7) | behavioral-profiling + dark-pattern optics; **contradicts the product's stated anti-engagement objective** (signal degrades by design); fair-lending if priced on. |
| **Device/geo/behavioral in the CREDIT lane** (C8/C10 credit) | Fair-lending-toxic if it drives a credit decision: geo proxies region (already excluded by docs/05); behavioral biometrics = Art-9; ePrivacy consent for fingerprinting. Acceptable ONLY hard-quarantined to the fraud lane. |
| **Psychometric / keystroke-biometric / typing-dynamics credit scoring** (C14) | GDPR Art-9 biometric + AI-Act profiling + fair-lending-toxic + reputationally radioactive, AND power≈1. **Recommend DROP in the ethics pass, not merely quarantine.** |

---

## §5 — LEAKAGE-EXCLUDED list *(modeling-invalid — separate from ethics)*

> 🚫 **Rule 1: leakage is a MODELING ERROR, not ethics.** Each item below is only knowable *after* the outcome (or hides a future outcome inside an aggregate). Flagged `is_leakage=true` and **excluded as a MODEL FEATURE**. Several are still valid as the **LABEL**, a **monitoring trigger**, or — critically — **the SAME source is non-leaky when pointed at a COUNTERPARTY or lagged to PRIOR events.** Kept entirely apart from §4.

1. **Live-recomputed pooled cross-customer aggregate spanning the outcome window** — any payer global-mean-days-late / contagion-cluster rate recomputed live to include payments realized AT OR AFTER the target invoice's due/outcome window. The **network-form of target leakage** — invisible because it hides inside an aggregate over other customers. → Enforce a hard `_asof_issuance` cutoff on **every** pooled aggregate.
2. **Forward "who else this payer will pay late next month" join** — built from the payer's FUTURE realized delinquencies against other customers within the prediction horizon. Temporal-causality leakage; only PAST pooled outcomes are admissible.
3. **Actual `paid_date` / paid-flag / `days_late` of the SPECIFIC scored invoice**, from ANY source (AEAT/Crea-y-Crece, Stripe, AR) — **this IS the M1 label**, never a feature.
4. **Inbox remittance-advice / payment-confirmation email for the SAME scored invoice** ("payment of €X sent ref INV-123") — defines the outcome; **label-quality input only**, leakage as a feature for that invoice.
5. **Customer's OWN outbound dunning / reminders / renegotiated due dates / credit-notes / dispute resolutions for the SAME invoice** — they exist BECAUSE the invoice went bad (post-outcome). Usable only to update the payer's trailing ledger for the **NEXT** invoice; gate on `artifact_timestamp < issue_date`.
6. **Chargeback / dispute notification on the specific scored transaction or within the scored outcome window** — co-occurs with / follows the outcome.
7. **Borrower's OWN concurso / pre-concurso (Art. 583 LC) declaration used to predict that same borrower's default** — it IS the default event / its immediate antecedent. **Label / monitoring / exit-trigger only.** ✅ NON-leaky and KEEP when the SAME signal is a **COUNTERPARTY** feature, or a leading sub-event (capital reduction, director churn, missing filing) that *precedes* the terminal event.
8. **Borrower's OWN RAI / ASNEF-Empresas listing used to predict that same borrower's default** — it is the morosity construct itself (= default). **Label / limit-cut trigger only.** ✅ NON-leaky and KEEP as a **COUNTERPARTY** feature predicting whether that client pays.
9. **Support-chat / in-app distress language about an OPEN NetBank loan** ("can I pause repayment", "lower my limit") used in the GRANT decision — contemporaneous to the loan's own repayment outcome and post-decision. **Servicing / early-collections triage only**, not a grant feature.
10. **Commercial-bureau composite score that already embeds the borrower's CURRENT arrears/morosity, used on the borrower itself** — partial leakage; validate score vintage and exclude any component reflecting present delinquency from the borrower's own PD model. *(A modeling, not ethics, concern.)*
11. **A counterparty insolvency / RAI / litigation filing whose date falls AFTER the scored invoice's due-date** — leakage for THAT specific invoice even though the source is otherwise a valid ex-ante counterparty feature. Enforce `filing_date < issue_date`.

> **Critical non-over-exclusion (the defense-grade subtlety):** items 7–8 are leakage **only** for the *borrower's own* default model. The **same** concurso/RAI signal is a **valid, non-leaky** feature when pointed at a **COUNTERPARTY**, and the leading sub-events are admissible ex-ante. Do not blanket-ban the source.

---

## Modeling-discipline carry-over (so the frontier stays leakage-clean)

- **Grouped-holdout upgrade:** escalate docs/05's per-customer-payer key to a **GLOBAL-payer key** (a payer in train must not appear in test *anywhere* in the base), and **connected-component-aware** for any network model (§2 #8). The **naive-CV-vs-grouped-AUC gap slide** (docs/05 step 7) remains the strongest faculty defense.
- **`_asof_issuance` everywhere:** every pooled aggregate AND every inbox/registry artifact gated on `timestamp < issue_date`, exactly as docs/05 mandates.
- **Non-credit / credit split holds:** every prediction here **SIZES and WARNS — none auto-grants or auto-declines.** The grant stays **human-on-the-loop** (Annex III §5(b) + GDPR Art 22, legally mandatory for the autónomo natural-person sub-segment), shipped with the plain-language top-drivers + confidence-band explanation sourced from interpretable coefficients/tree paths even when an ensemble is the production scorer.
- **Honest power caveat:** network/cross-customer power scores assume the entity-resolution join works at scale (fuzzy match unproven on NetBank data). External-scrape power scores are **evidence-informed** from cited closure/equity/consumer literature — **validate against NetBank's own realized closed-loop label** before trusting power-3–5 ratings.

---

## Open questions (frontier-specific)

- **Entity resolution at scale:** does fuzzy name+IBAN resolution of PSD2 remitter strings hit usable precision/recall on real NetBank data? (Gates A1/A2/A3 — the whole moat move.)
- **AEAT repository access:** do third-party access rights to the Crea-y-Crece payment-status repository materialize, and on what timeline for the SME/autónomo segment (realistically ~2029)?
- **Cross-customer lawful basis:** is there a defensible GDPR basis for the shared-payer prior on non-consenting natural-person payers, or does it require anonymization that destroys the small-n signal?
- **Network-feature validation:** do graph/contagion features (§2 #8) survive a connected-component-aware split with real lift, or collapse like a leaky CV?
- **CASA cost/benefit:** is the annual Google CASA assessment (for restricted-Gmail inbox ingestion) worth the earliness lift of the inbox payer-intent layer?
- **Scrape-vs-buy provenance:** which alt-data signals (hiring, reviews, traffic) can be licensed cleanly vs must be dropped on ToS/coverage-bias grounds?
