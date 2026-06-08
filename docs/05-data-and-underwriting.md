# 05 — Data & Underwriting Spec *(the moat, specified)*

> **The artifact the moat was missing.** `docs/01`–`04` cover the client, the UX, and the regulatory posture. None of them specify the thing we actually sell: *how we decide it is safe to lend.* This doc does. It lists every data input, its source, its legal basis, and its exact role in the score; defines what "safe to borrow €X" means; and sequences the **cold-start → closed-loop** transition so the model is solvent on day one and differentiated by year two.
>
> **Inherits from:** the architecture split in the [README](../README.md) (non-credit autonomous core vs. human-reviewed grant), the closed-loop moat in [`01-client-and-evidence.md`](01-client-and-evidence.md), and the Financing / Loan-Grant screens in [`03-design-spec.md`](03-design-spec.md) §4.8–4.9 & §5.
>
> **Defend-every-number rule applies here too.** Every external data source below carries a source URL. Read §7 (caveats) before the oral defense.

---

## 1. What "safe to borrow" actually means (definitions, locked)

Before any data, the targets must be unambiguous — an undefined objective is the fastest way to lose the underwriting defense.

| Term | Definition |
|---|---|
| **Exposure** | Euros outstanding (drawn) against a customer at a point in time. |
| **Default** | A bridged receivable **>90 days past its expected collection date** with no repayment, **or** a CIRBE/ASNEF default event on the borrower. (90d aligns with the EBA default definition; state it, don't invent our own.) |
| **PD** (probability of default) | Modelled probability the customer defaults on a draw within its term. |
| **LGD** (loss given default) | Expected loss if default occurs. For a **named, verified, SII-confirmed receivable**, LGD is structurally low because the asset is a specific debt we can pursue — this is the source of the 1–3% factoring loss band ([EBA](https://www.eba.europa.eu/publications-and-media/publications/risk-assessment-report-december-2025)). For an **unsecured cash-flow draw**, LGD is high — price and cap accordingly. |
| **Safe-to-borrow €X** | The pre-computed ceiling such that **expected loss (PD × LGD × exposure) stays inside our target loss band** *and* the draw does not push forecast runway below a floor. It is a **capacity estimate**, not a grant — sizing is autonomous; the grant is human-reviewed (README split). |
| **Repayment rate** | Realized: share of drawn euros repaid on schedule. This is the **KPI the inverted-flywheel P&L optimizes** (slide 4) — we are paid for accuracy, not volume. |

**The split, restated for data purposes:** *sizing* (PD/LGD/capacity, autonomous, outside Annex III) consumes the full data stack below; the *grant* (human-on-the-loop, Annex III §5(b) + GDPR Art. 22) consumes the sizing output **plus** the hard gates in §4.

---

## 2. The data stack — every input, source, legal basis, role

Grouped by what each layer is *for*. **"Held"** = we already have/claim it. **"Close"** = reachable now, not yet wired. **"Gate"** = must block a grant if it fails, regardless of score.

### 2.1 Proprietary / closed-loop (our differentiated data — but cold-start-limited)

| Input | Source | Legal basis | Role in score | Status |
|---|---|---|---|---|
| Own-account transactions | NetBank ledger | Contract | Inflow stability, burn, runway | Held |
| **Realized payment dates per invoice** | Settlement into a visible account (NetBank **or** PSD2-aggregated) | Contract / PSD2 consent | **The label that trains per-client reliability** — the moat | Partial → see §3 |
| OCR'd AP/AR | Scan/Pay (§4.6–4.7) | Contract | Receivables base, payables schedule | Held |
| Card / SaaS / AI spend | NetBank cards | Contract | Burn decomposition, discretionary-cut headroom | Held |

> ⚠️ **The label problem (§3 fixes it):** SII/Verifactu proves an invoice was *issued*, never *paid* or *when* — submission is tied to issuance/accounting date, there is no settlement field ([Marosa VAT](https://marosavat.com/vat-news/verifactu-and-sii-understanding-spains-invoicing-e-reporting-systems)). The realized payment date — the entire closed-loop thesis — is only observable when money lands in an account we can see. That makes PSD2 AIS existential, not optional.

### 2.2 Commodity context (cheap, useful, NOT a moat)

| Input | Source | Legal basis | Role in score | Status |
|---|---|---|---|---|
| Issued/received invoices | Verifactu / SII (AEAT) | User-authorized AEAT access | Receivables & payables *existence*, counterparty list, VAT exposure | Held (commodity) |
| Sector / activity (CNAE) | AEAT / Registro Mercantil | Public / authorized | Sector default-rate prior, seasonality | Close |

### 2.3 External underwriting stack (the outlier-catchers we are missing)

| Input | Source | Legal basis | Role in score | Status |
|---|---|---|---|---|
| **Total existing debt, all lenders (>€1,000)** | **CIRBE — Banco de España** | Solvency-assessment duty + borrower consent | **Total-leverage gate; #1 adverse-selection defense** | **Close — Gate** |
| **Prior default events** | **ASNEF (Equifax) / BADEXCUG (Experian)** | Legitimate-interest credit-risk file | Hard negative; near-automatic decline on hit | **Close — Gate** |
| **Tax compliance** (*al corriente*) | AEAT *certificado* | User-authorized | Early-distress signal; grant gate | Close — Gate |
| **Social-security / RETA cuota status** | Seguridad Social | User-authorized | Earliest distress signal (precedes commercial default) | Close — Gate |
| **Cross-bank transactions & indebtedness** | **PSD2 AIS** (own AISP or aggregator) | PSD2 explicit consent | Income/debt routed through *other* banks; **payment labels** | **Close — high value** |

### 2.4 Counterparty / fraud layer (the real tail risk)

| Input | Source | Legal basis | Role in score | Status |
|---|---|---|---|---|
| **Payer identity & existence** | Registro Mercantil + counterparty SII footprint | Public / authorized | Anti-fabrication: is the receivable arm's-length and real? | **Close — Gate** |
| **Client concentration** | Our own invoice/settlement data | Contract | "One client = 60% of you" → hard cap, not a UX nicety | Held (un-used) |
| Payer reliability (the bridged debtor) | Closed loop + cross-customer | Contract | Per-receivable PD — prices the specific bridge | Partial (cold-start) |

---

## 3. The label & cold-start problem (why the model works on day one *and* compounds)

The closed loop only produces labels **after** we have lent and observed repayment. On day one we have ≈zero defaults to learn from. A model trained on no labels cannot underwrite. The fix is an **explicit hand-off**, not a single model:

```
Phase 0 (launch)      Phase 1 (ramp)              Phase 2 (moat)
external stack +      external + early            closed loop dominant,
sector priors  ──►    realized labels      ──►    external = gate + check
[CIRBE, ASNEF,        [reweight as labels         [per-client reliability
 AEAT/SS, AIS]         accumulate]                  prices each bridge]
```

- **Phase 0:** PD comes from the **external stack** (§2.3) + sector priors. CIRBE/ASNEF/AEAT/SS act as gates; AIS supplies cross-bank cash-flow. This is what keeps loss inside the band before we have proprietary labels.
- **Phase 1:** every realized payment date (now observable via §3-fixed settlement visibility) becomes a label; the per-client reliability model is reweighted up as `n` grows.
- **Phase 2:** the closed loop dominates pricing; the external stack **never leaves** — it stays as the leverage/fraud gate and an out-of-model check.

**Defense line:** *"The data is not the moat (Verifactu/SII is commodity). The moat is the closed loop. But the closed loop has a cold start, so the external Spanish underwriting stack underwrites Phase 0 and remains the gate forever — we are differentiated by year two, solvent from day one."*

---

## 4. The grant gates (hard rules, independent of the score)

Sizing produces a number; the **grant** (human-on-the-loop, §4.9) may not exceed it **and** must clear every gate. A gate failure blocks or reduces the draw regardless of how good the cash-flow score looks — this is where the dangerous outliers are caught.

1. **Leverage gate — CIRBE.** Total existing debt across all lenders + the proposed draw must keep total leverage under a policy ceiling. *Catches the applicant who looks healthy in our data but is maxed out everywhere else — the classic adverse-selection trap that most threatens the 1–3% loss band.*
2. **Negative-file gate — ASNEF/BADEXCUG.** A current default record is a near-automatic decline (note: these files record **defaults only — no positive history, no score**, [ASNEF](https://www.asnef.com/servicios/fichero-asnef/)).
3. **Public-obligation gate — AEAT + Seguridad Social.** Not *al corriente* on tax, or behind on the RETA cuota → reduce or hold. Earliest distress signal available.
4. **Counterparty gate — fraud.** Bridged receivables must be against a **verified, independent, existing** payer (Registro Mercantil + their own SII footprint). "SII-confirmed" proves the invoice exists for VAT — it does **not** prove arm's-length or collectability.
5. **Concentration gate.** No single client above a policy share of the bridged book for one customer.
6. **Runway-floor gate.** The draw must not push forecast runway below the floor — a financial-health objective never yanks runway at the worst moment (slide 4 / §5.1 "you don't need to borrow").

---

## 5. Mapping data → the screens (traceability)

Keeps this spec honest against the "decisions, not screens" method — every gate and input surfaces somewhere legible.

| Data / gate | Surfaces on | AI register | Human-loop |
|---|---|---|---|
| Cash-flow / runway / burn | Home, Forecast | Predict | on |
| Safe-to-borrow capacity (PD/LGD/runway) | Financing §4.8 | Predict (sizing, loop **out**) | out |
| CIRBE / ASNEF / AEAT / SS gates | Loan Grant §4.9 (the human's evidence) | Recommend → Human-reviewed badge | **in (Annex III gate)** |
| Per-client reliability (closed loop) | Financing "why €X?" + Grant card | Predict | on |
| Counterparty / concentration | Clients/receivables; Grant gate | Predict | in |
| "Connect payroll / VAT / 2nd account → +€Y" | Financing limit-meter (§4.8) | Recommend | out |

The limit-meter's unlock chips (*Connect VAT +€4,500*, *Connect payroll +€6,000*) are the **user-facing handle on this data stack** — each connection adds an input above and visibly raises capacity (data-elasticity made legible).

---

## 6. Licensing consequence (ties to the open decision in `00` §Decisions)

The "hold a credit licence vs. originate-and-refer" decision is now **data-driven, not just margin-driven**, because access to the critical inputs depends on it:

- **CIRBE reporting/query access** is a function of being a declarante to Banco de España (or pulling borrower-consented reports). ([Banco de España](https://www.bde.es/wbe/en/para-ciudadano/gestiones/informacion-riesgos-cir/))
- **PSD2 AIS** requires an AISP licence **or** a regulated aggregator (Tink / TrueLayer / Enable Banking) — the faster path for a prototype.
- Hold-licence → full CIRBE participation + own underwriting; refer → the partner owns the gate and we lose the closed-loop label feed. **The moat argues for holding the licence.**

---

## 7. Caveats (read before the oral defense)

- **SII ≠ payment data.** Do not claim invoice data shows repayment behavior — it shows issuance only ([Marosa VAT](https://marosavat.com/vat-news/verifactu-and-sii-understanding-spains-invoicing-e-reporting-systems)). The label comes from settlement visibility (NetBank account or PSD2 AIS).
- **CIRBE has a floor and a lag.** It captures debt **>€1,000** and is not real-time; it catches structural over-leverage, not a loan taken yesterday ([Banco de España](https://www.bde.es/wbe/en/para-ciudadano/gestiones/informacion-riesgos-cir/), [Bankinter](https://www.bankinter.com/banca/en/financial-dictionary/central-credit-register-of-the-bank-of-spain)).
- **ASNEF/BADEXCUG are negative-only.** No score, no positive history, no on-time data ([ASNEF](https://www.asnef.com/servicios/fichero-asnef/)) — which is *why* our closed-loop positive-repayment data is genuinely differentiated, and why bureaus can't underwrite the "safe" side alone.
- **GDPR & AI Act.** Every external pull needs a lawful basis and the borrower's consent at onboarding; the grant decision is Annex III §5(b) high-risk + Art. 22 (human review on adverse/automated decisions). The gates feed the human reviewer — they do not auto-decline silently.
- **Fraud is the tail, not the mean.** Self-issued invoices to a colluding counterparty are the sharpest negative outlier; the counterparty gate (§4.4) is load-bearing, not optional.

## 8. Open questions for the team

1. Set the **policy ceilings**: total-leverage cap, concentration cap, runway floor — with what evidence?
2. **AISP licence vs. aggregator** for the prototype — speed vs. control.
3. **CIRBE access path** — declarante vs. consented pull — and how it gates the hold-vs-refer decision.
4. Default definition: adopt EBA 90-day uniformly, or a shorter internal trigger for the bridge product?
5. Which inputs are **gates** vs. **score features** — and which gate failures *reduce* vs. *block*?

---

*Sources:* [Banco de España — CIRBE](https://www.bde.es/wbe/en/para-ciudadano/gestiones/informacion-riesgos-cir/) · [CIRBE for autónomos, Mar 2026](https://www.autonomosyemprendedor.es/articulo/pymes/banco-espana-permite-autonomos-ver-todas-deudas-creditos-avales-asociados-negocio/20260306151923052402.html) · [ASNEF / Equifax](https://www.asnef.com/servicios/fichero-asnef/) · [SII scope — Marosa VAT](https://marosavat.com/vat-news/verifactu-and-sii-understanding-spains-invoicing-e-reporting-systems) · [PSD2 AIS for lending — BBVA](https://www.bbvaapimarket.com/en/api-world/how-account-information-services-ais-work-psd2/) · [EBA Risk Assessment, Dec 2025](https://www.eba.europa.eu/publications-and-media/publications/risk-assessment-report-december-2025)
