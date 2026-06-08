# 06 — Proprietary Data Moat *(the niche, controlled)*

> **The companion to [`05`](05-data-and-underwriting.md).** `05` specifies the data that keeps us *solvent* — the commodity underwriting stack every licensed lender in Spain holds. This doc specifies the data that makes us *win* — the proprietary, compounding signal no incumbent or Verifactu reseller can copy. **`05` = don't-lose-money gates. `06` = win-the-niche signal.**
>
> **The thesis in one line:** we do not win by collecting *more* data. We win by being the only ones accumulating the **realized cross-payer behavioural graph** that the default outlier hides inside.

---

## 1. The distinction the rest of the data plan must respect

| Tier | Examples | Who has it | What it buys |
|---|---|---|---|
| **Tier 1 — commodity** | CIRBE, ASNEF, PSD2 AIS, AEAT/Seguridad-Social status, own-account transactions ([`05`](05-data-and-underwriting.md) §2) | **Every** licensed lender | Keeps us *alive* — solvency gates. **Zero niche control**: a checklist anyone clones. |
| **Tier 2 — proprietary** | the payer-reliability graph, realized payment-lag tails, dispute/dunning behaviour, income structure (this doc) | **Only us**, by virtue of where we sit | *Wins* the niche. Compounds. Cannot be bought or scraped. |

A bank with a CIRBE feed and a cash-flow model is **not in our niche — it is just a bank.** Our specialisation must live entirely in Tier 2. `05` is ~80% Tier 1 by necessity; this doc is the counterweight.

---

## 2. The organising principle: the outlier lives in the *tail*

Our specialisation is **predicting the strongest outlier** — deciding whom we can safely fund. Stated statistically: **the outlier is the tail of the per-payer payment-lag distribution.**

> *"Studio Vermell pays in ~12 days, 96% on-time"* is the **mean**. The default risk is the **tail** — the 1-in-25 case where they pay at day 95, or never.

**The structural trap this creates:** a single freelancer never bills one payer enough times to estimate that tail. Six invoices to one client cannot reveal a 1-in-25 event. An underwriter looking at **one** customer's data therefore *cannot* price the outlier — no matter how good the model.

**The structural advantage only we have:** we sit across thousands of freelancers billing an **overlapping set** of Spanish SMB payers. If 40 of our customers have billed Studio Vermell, we hold ~240 realized payment events on that single payer — enough to actually estimate the tail. That cross-payer graph is:

- **specialised** — it exists only because of the embedded, multi-tenant position;
- **compounding** — every new customer sharpens the tail estimate for every other customer exposed to the same payer;
- **defensible** — Verifactu/SII gives competitors invoice *issuance*, never the realized cross-payer *settlement* graph ([`05`](05-data-and-underwriting.md) §2.1: SII has no settlement field);
- **the cold-start cure** — the network supplies labels on a payer before *we* have lent against that payer even once ([`05`](05-data-and-underwriting.md) §3).

**This graph is the asset to build the niche around.** Everything below is how.

---

## 3. The core modelling decision: the payer is a first-class entity

Today an invoice's payer is a **string on a document**. To control the niche it must become a **persistent, NIF-keyed record that accumulates observations across all customers.** This one decision is the difference between a banking app and a **debtor-reliability bureau we own.**

### 3.1 The `Payer` entity (proposed)

| Field | Type | Notes |
|---|---|---|
| `payer_nif` | id (key) | The cross-customer join key. Resolve aliases (trading name vs. legal name) to one NIF. |
| `sector_cnae` | code | Payer's activity — drives sector/seasonality priors. |
| `size_band` | enum | Micro / small / mid — from Registro Mercantil where available. |
| `realized_events[]` | list | One per settled invoice, across **all** our customers (see §3.2). |
| `lag_distribution` | derived | Mean, variance, **tail/p95–p99**, trend, seasonality (see §4). |
| `dispute_rate` | derived | Share of invoices disputed / partially paid / re-issued. |
| `dunning_profile` | derived | Response latency, promise-to-pay kept rate (see §4.5). |
| `exposure_concentration` | derived | How many of our customers depend on this payer (systemic-payer flag). |

### 3.2 The `RealizedSettlement` event — log this from day one

The atomic observation. **Capture it from first launch even if v1 ignores it** — the asset compounds, and a late start cannot be recovered (§6).

```
RealizedSettlement {
  payer_nif, customer_id, invoice_id,
  sector_cnae, stated_terms_days, issue_date,
  realized_payment_date,           // the LABEL — from settlement visibility, not SII
  realized_lag_days,               // realized_payment_date − due_date
  amount, partial_paid_flag,
  dispute_flag, reissue_flag,
  dunning_fired, dunning_outcome   // see §4.5
}
```

> **Where the label comes from:** `realized_payment_date` is observable **only** when money lands in an account we can see — NetBank account or PSD2-aggregated ([`05`](05-data-and-underwriting.md) §3). This is why PSD2 AIS is existential, not optional: it is both cross-bank visibility *and* the label feed for this graph.

---

## 4. The Tier-2 features we *definitely* need (each: why it predicts the outlier · why it's proprietary)

**4.1 Per-payer payment-lag distribution — the full shape, not the mean.**
Mean & variance, but critically the **tail (p95–p99 / worst-case lag)** — that *is* the outlier — plus the **trend** (a payer whose lag is *deteriorating* quarter-over-quarter is the leading indicator of a coming default) and **seasonality** (construction pays worse in August; public-sector payers pay on budget cycles).
*Proprietary because* only the cross-customer graph (§2) has the observation count to estimate a tail.

**4.2 Cross-customer payer observations — the network effect.**
Each new freelancer billing an existing payer sharpens the tail estimate for everyone exposed to that payer.
*Proprietary because* it is a direct function of multi-tenant embedded position — unbuyable, unscrapeable.

**4.3 Dispute / partial-payment / re-issue events.**
A disputed or partially-paid invoice is a far stronger default signal than a merely late one.
*Proprietary because* visible to us and to almost no one else; absent entirely from SII.

**4.4 Income structure of the borrower — not just income level.**
Retainer / recurring-contract revenue vs. project vs. one-off (recurring is dramatically more predictive — it is MRR for freelancers); repeat-client ratio; pipeline depth; and **substitutability** of concentrated income (HMW-8 "one client = 60%" *with context* — one client + full pipeline is a different risk than one client + dry funnel).
*Proprietary because* it is derived from the realized invoice/settlement history we hold.

**4.5 Dunning responsiveness.**
When the "Chase" action fires (already in the Invoices screen, `03` §4.7), log the outcome: did the payer respond, promise to pay, and **keep** the promise? Promise-broken is among the highest-information default signals in receivables finance.
*Proprietary because* it is a behavioural signal **we generate** — unambiguously ours.

**4.6 Recommendation-calibration loop.**
Every time we warn "dry month ~22 Jul" or predict "pays in 9 days," log whether it *actually happened*. Calibration of our own forecasts is a meta-signal.
*Proprietary because* no competitor has our forecasts, so none can calibrate them.

---

## 5. How this becomes *control* of the niche (the defensibility argument)

1. **Data network effect.** Value per customer rises with customer count (shared payers) — the classic defensible flywheel, and the literal mechanism behind the README's *"more data → better underwriting → safer loans → more trust → more data."*
2. **Cold-start asymmetry.** A new entrant starts with an empty graph; we start with years of cross-payer tails. Even with identical models, they cannot price the outlier on a payer they have never observed — and we can.
3. **Commodity-proof.** Verifactu/SII makes invoice data free for everyone (`01` caveat). It does **not** make the realized cross-payer settlement-behaviour graph free. That graph is the one thing the commoditisation cannot reach.
4. **Incentive-proof.** An interchange/engagement neobank is structurally disincentivised to optimise for "borrow less" (slide 4) — so even if it could build the graph, it would not point it at our objective.

**The one-line defense:** *"Controlling the niche is not collecting more data — it is being the only one accumulating the realized cross-payer behavioural graph the default outlier hides inside. Commoditised invoice data can't reach it; a cold-started entrant can't price against it."*

---

## 6. The urgent mandate: instrument from day one

The payer-graph asset has a brutal property — **it only has value if logged from the first transaction.** The tail we can estimate in year three depends on observations captured *now*, before any model consumes them.

> **Requirement (model-independent):** from first launch, persist every `RealizedSettlement` (§3.2) as a cross-customer, NIF-keyed `Payer` record (§3.1). Log it even if v1 ignores it in scoring. The asset compounds; a late start cannot be recovered.

This is the single most time-sensitive item in the entire data plan — it costs little now and is irrecoverable later.

---

## 7. Open questions for the team

1. **Payer identity resolution** — how do we de-dupe trading name vs. legal name to one `payer_nif` reliably?
2. **Privacy/GDPR of a third-party debtor graph** — the payer is a data subject we have no contract with; what is the lawful basis (legitimate interest? the same basis ASNEF uses?) and what are the limits? *(Counsel review — pairs with `05` §7.)*
3. **Minimum observation count** before a per-payer tail estimate is trusted vs. backed off to a sector prior.
4. **Systemic-payer risk** — when one payer is concentrated across many of *our* customers, that is correlated exposure on our book, not just per-customer risk. How do we cap it?
5. Which Tier-2 features are **score inputs** vs. which gate the grant alongside `05` §4?

---

*See also:* [`05-data-and-underwriting.md`](05-data-and-underwriting.md) (the commodity gates), [`01-client-and-evidence.md`](01-client-and-evidence.md) (the closed-loop moat statement), [`03-design-spec.md`](03-design-spec.md) §4.7–4.9 & §5 (Invoices / Financing / hero flow where this signal surfaces).
