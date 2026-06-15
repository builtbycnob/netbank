# 12 — Tax-Sweep+ WTP Test Plan (attacking the #1 weakness)

> **Why this doc:** willingness-to-pay is NetBank's self-identified #1 weakness — the deck *proves the signal, not who pays* (docs/09 Slides 5/7). Tax-Sweep+ is the pillar with the clearest payer/price/pain triple, so it's the right place to convert "we have a benchmark" into "we have evidence." This is a **primary-research plan**, not a result. Every target below is tagged `[hypothesis to validate]` until the test runs.

## 0. The claim under test

**Tax-Sweep+** = every incoming payment auto-sets-aside the VAT/IRPF slice into a **locked sub-account**; at quarter-end the money is already there and a **one-tap modelo-303/IRPF readiness pack** goes to the gestor. Scope is **set-aside + readiness export + handoff — never an automated filing** (regulated-advice perimeter, docs/11 §4).

**Pricing anchor (sourced):** priced against the **€60–100/mo gestor** line autónomos already pay (docs/01), benchmarked to **Qonto €9 / €19 / €39** tiers (docs/01). Reality check: most top-25 neobanks earn **<$30/customer/year** (Simon-Kucher, docs/09) — so the subscription must be *genuinely* willingly paid, not assumed.

**The real risk to disprove (docs/10):** Qonto/Revolut **bundle a free tax pot**. So the test must prove customers pay €9–15/mo for Tax-Sweep+ **over a free toggle** — not just that they like tax pots.

## 1. Hypotheses

| # | Hypothesis | Metric | Target `[to validate]` |
|---|---|---|---|
| **H1** | A first-euro subscription converts | Paid-tier selection rate (reach the payment step) among VAT-registered autónomos shown the offer | **≥ 15%** |
| **H2** | Intent is real, not a click | Smoke-test **charge-authorization completion** among those who selected a tier | **≥ 50%** of selectors |
| **H3** | It beats free | Paid selection in the **paid arm** vs opt-in rate in a **free-toggle control arm** | Paid arm WTP **materially > 0** after subtracting "I'd take it free" |
| **H4** | Price is in band | Van Westendorp acceptable-price range brackets €9–15 | OPP within **€9–15** |

If **H1 ≥15% AND H2 ≥50% AND H3 positive**, greenlight the build. Otherwise reprice / rescope / fold Tax-Sweep+ into a bundle (decision rule in §6).

## 2. Method — three stages, cheapest first

**Stage A — Van Westendorp price survey (cheap pre-test, ~1 week).**
Recruit ~120–150 VAT-registered autónomos; show the Tax-Sweep+ value prop; ask the 4 standard questions (too cheap / cheap / expensive / too expensive). Output: the **acceptable price band**, the Optimal Price Point (OPP) and Indifference Price Point (IPP). *Purpose: confirm €9–15 is sane before spending on behavioral arms.*

**Stage B — Monadic fake-door pricing test (the behavioral core, ~2 weeks).**
A hosted "Tax-Sweep+ — VAT, handled" page / in-app upsell. **Monadic design:** each visitor is randomized to see **one** price (avoids anchoring) across **four arms**:

| Arm | What the visitor sees |
|---|---|
| €9/mo | paid tier only |
| €12/mo | paid tier only |
| €15/mo | paid tier only |
| **Free-toggle (control)** | the same tax-pot as a free switch |

Click "Start free trial / Subscribe" → **Stage C**. Measure **selection rate per arm** (H1) and the elasticity €9→€15. The free arm (H3) tells us how much of the demand is "I'd just take it free."

**Stage C — Smoke-test charge + Wizard-of-Oz (truth test, runs inside B).**
Selectors hit a **real Stripe payment step** (authorize, immediately voided / converted to "early-access — you won't be charged yet"). **Charge-authorization completion = true WTP (H2)** — the gap between selecting and authorizing is the honesty filter.
For the handful who complete, **deliver Tax-Sweep+ manually** (Wizard-of-Oz): we compute and "set aside" the slice and hand-assemble a modelo-303 readiness pack for one quarter. *Purpose: learn the real felt value + early retention before writing code.*

## 3. Sample size & recruiting

- **Power (Stage B primary):** to estimate a ~15% conversion with **±5% at 95% CI** needs **n ≈ 196 exposed per arm** → ~**600–800** across the 3 price arms + control. A directional read is fine at **~100/arm** (±7%).
- **Recruiting channels** (also tests CAC, doubling as a docs/11 fold-in probe):
  1. **Gestoría pilots** (docs/11 Gestoría channel) — warm, in-ICP, cheapest.
  2. Autónomo communities / subreddits / Infoautónomos-style audiences.
  3. A small paid-ads arm (€ low) to get a clean cold cohort.
- **Screen:** VAT-registered (alta censal / modelo 303 filer), Spain, solo→10. Exclude non-VAT and pure-employee respondents.

## 4. Bias & validity controls

- **Monadic, randomized prices** — no price ladder visible (kills anchoring).
- **Real charge authorization**, not a hypothetical "would you pay?" — intent inflation is the classic fake-door failure.
- **Free-toggle control arm** — the decisive test vs the Qonto/Revolut free-pot risk.
- **No leading copy** — neutral value statement; A/B the headline only as a secondary.
- **Ethics:** the smoke-test charge is **authorized then voided** (or a fully-disclosed "early access, not charged yet"); refund any captured amount immediately; GDPR-clean consent on the survey.

## 5. Readout template (fill after the run)

| Arm | Exposed n | Selected % (H1) | Charge-auth % (H2) | Net-of-free WTP (H3) |
|---|---|---|---|---|
| €9 |  |  |  |  |
| €12 |  |  |  |  |
| €15 |  |  |  |  |
| Free toggle | — | opt-in % | — | — |

Van Westendorp (Stage A): OPP **€__**, IPP **€__**, acceptable range **€__–€__**.
**Verdict:** greenlight / reprice to €__ / rescope / bundle.

## 6. Decision rule

- **Greenlight build** if €12 arm: selection ≥ **15%** AND charge-auth ≥ **50%** AND paid arm beats free-toggle on net WTP.
- **Reprice** to the arm that maximizes `selection% × price` if the €12 point underperforms but €9 clears.
- **Rescope / bundle** (fold Tax-Sweep+ into a single subscription with Concurso Radar's Watchtower + the bridge relationship) if no standalone arm clears — i.e. the feature is a retention driver, not a standalone first-euro line.

## 7. Cost & timeline

~**3–4 weeks**, low cash: a landing page + Stripe test mode + a survey tool + small ad/recruiting spend. The expensive input is **access to ~600 VAT-registered autónomos** — which is exactly why the **gestoría channel** (docs/11) is the cheapest recruiting path and should be piloted in parallel.

---

*Plan only — no arm has run yet; all targets are `[hypothesis to validate]`. Closes docs/11 §7 required-fix (e): the >15% conversion is stated here as a hypothesis with a decision rule, never as a result. Sources: Qonto/gestor benchmarks (docs/01), Simon-Kucher <$30/cust/yr (docs/09), van Westendorp price-sensitivity method.*
