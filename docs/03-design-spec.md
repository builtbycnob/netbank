# 03 — Hero Flow Spec: Embedded Lending / Safe-to-Borrow Journey

> The one flow we go deep on. This is simultaneously NetBank's **moat** (more-embedded → better-data → better-underwriting → safer-loans → more-trust → more-data) and the course's **agentic loan journey**. It is the single place where the compliance-critical architectural split becomes tangible on screen: **sizing** runs on the autonomous non-credit core (predict, human-loop OUT, 310-speed, *outside* AI Act Annex III); the **grant** is human-on-the-loop (recommend, human-loop IN, Annex III §5(b) + GDPR Art. 22) carrying a visible **"Human-reviewed"** badge.
>
> Inheritance: this builds directly on [`02-mobile-experience.md`](02-mobile-experience.md) (HMW #4/#5, the 6 design principles, the earned-trust ladder as a UI pattern) and the architecture table in the [README](../README.md). Where this doc says "bridge," it means the same per-receivable credit product `02` calls the *bridge*, generalized to the embedded line.

---

## 0. Reading the flow

```
1. SAFE TO BORROW   →  2. REQUEST          →  3. HUMAN-REVIEWED GRANT
   (always-on,          (one tap,              (the Annex III gate —
    no application)      cost-transparent)      AI recommends, human decides)
        ↑                                              ↓
6. REPAY            ←  5. MONITORED         ←  4. DISBURSED
   (revolving,          (continuous, calm,      (one-tap confirm,
    line refills)        mission-aligned)        funds land, Undo window)
```

The loop is the product. Step 6 visibly raises the ceiling shown in step 1 — clean repayment + more connected data move the earned-trust ladder up, which is the moat made legible.

**Two non-negotiable framings carried through every step:**

1. **The split is signposted, never hidden.** Sizing is autonomous and instant; the *grant* is human-reviewed. The UI says so in plain language at the exact moment it matters (step 3), so the human-on-the-loop becomes a *trust feature*, not a disclosed limitation (principle 4, `02`).
2. **The honest "you don't need to borrow" moment is a first-class branch, not an edge case** (§7 below). Objective function = customer financial health, not loan-volume extraction. If a forecast inflow closes the gap before the cost of borrowing is justified, NetBank says so and offers *not* to lend.

---

## 1. STEP — Safe to Borrow *(always-on, no application)*

| Field | Value |
|---|---|
| **Surface** | Home hero tile + the Financing destination hub (same number, two entry points) |
| **Decision served** | *Do I have headroom, and how much can I safely draw right now — without filling in a form?* |
| **AI role** | **PREDICTING — human-loop OUT.** Sized continuously by the non-credit autonomous core at 310-speed. Outside AI Act Annex III (this is capacity *estimation*, not a credit *decision* on a natural person). |
| **Human-on-the-loop?** | **No.** Pre-qualification only. The grant gate is step 3. |

### What data/signal drives it
The safe-to-borrow figure is a **synthesized number**, computed live from:
- **Cash-flow + runway + burn** (the Home metrics, `02` §Home).
- **AR aging + per-client reliability model** — the closed-loop asset: each realized payment date retrains how reliably *this* client pays, so a bridge is priced against a *specific reliable invoice*, not an "erratic" profile (`01` moat).
- **>95%-target cash-flow forecast** (MYbank/BaiLing-class) — the forward projection that *justifies* the number; inspectable via an "assumptions" disclosure.
- **Connected-data depth** — PSD2 bank feeds, VAT/AEAT, second account, payroll. This is the elasticity lever: embedded transaction visibility underwrites a credit-use elasticity of **0.407** vs **0.090** when the flow is opaque (NBER w30160 / Princeton). The meter makes that gap *visible*.

### Key elements
- **Hero = pre-computed "Safe to borrow: €X"** (tabular numerals), framed *"already approved up to €X — draw in seconds"*. **Decoration-blue wash**, never an "Apply" button (recon: WeBank pre-approved 100M+ users passively; the number sits dormant until tapped).
- **Data-elastic limit meter.** A calm progress element with explicit deltas: *"Connect payroll → +€1,800"*, *"Connect your VAT account → +€2,400"*, *"Add your 2nd bank → +€900"*. Each connection visibly bumps the headline — the more-data→safer-loans loop, on screen. (Elasticity 0.407 vs 0.090 made legible.)
- **Earned-trust ladder** (the UI pattern from `02` principle 3), shown as 4 rungs with the next-rung €-delta:
  - **Tier 0 — Banking only:** limit *estimated*, conservative.
  - **Tier 1 — Cash-flow connected:** PSD2 + categorization live → first real limit.
  - **Tier 2 — Invoices / AR connected:** per-receivable underwriting unlocks → larger limit, cheaper bridge.
  - **Tier 3 — Clean repayment history:** demonstrated repayment → highest ceiling + best rate.
  Each rung shows *what unlocks it* and *the € it adds*. Downside is framed symmetrically and gently (a missed repayment temporarily lowers the safe limit) — **never** the real-world abrupt ~77%-on-overdue cut (recon pitfall: that is pro-cyclical and anti-mission; we soften it to graduated/recoverable, §5).
- **Forecast-justification chip** — *"Why €X? See the 90-day projection →"* expands the inspectable forecast (principle 5: explainability inside the UI, serves GDPR/AI Act *and* trust).
- **Split signage (priming):** a quiet micro-label — *"Sizing is instant. Any draw is reviewed by a person before it's granted."* Sets up step 3 so the human review reads as a feature, not a delay.
- **Single-voltage CTA:** exactly one filled-accent button — *"Request a draw"*. Everything else is text/ghost.

### Honest branch entry (see §7)
If the live forecast shows the user's **next inflow closes the gap before borrowing pays off**, this tile inverts: the CTA softens to a ghost *"You likely don't need this — here's why →"* and the recommendation becomes *don't borrow*. This is the mission's sharpest moment, surfaced at the very top of the funnel.

---

## 2. STEP — Request *(one tap, cost-transparent)*

| Field | Value |
|---|---|
| **Surface** | Slide-over from the Financing hub (not a full-page nav — minimize clicks) |
| **Decision served** | *How much do I draw, on what repayment shape, and what does it actually cost me?* |
| **AI role** | **RECOMMENDING — human-in begins here.** An accent-outline card recommends amount + terms with grounded reasoning. The user still drives the slider. |
| **Human-on-the-loop?** | **Not yet** — this is still pre-grant. The recommendation is generated; the *decision* is step 3. |

### What data/signal drives it
- The pre-computed ceiling from step 1 caps the slider.
- **All-in cost** is computed before anything confirms: per-day interest (line accrues per-day-outstanding, no early-repayment penalty — revolving-utility model) **and** the total. **Headline limit and the real drawable price must never diverge** (recon pitfall: dormant-limit expectation gap erodes trust).
- **AR aging + per-client reliability** shape the recommended repayment structure — *cash-flow / invoice-cycle-aligned*, not a fixed monthly schedule. Concretely: *"Repay when invoice #1042 (Studio Vermell, pays in ~12 days, 96% on-time) lands"* — bridging the specific reliable receivable, the 85-day collection gap made into a solved problem (`01`; HMW #4/#5).

### Key elements
- **Amount slider** to €X, with the live cost readout updating in tabular numerals as you drag (*"≈ €1.40/day · €38 total over 27 days"*).
- **AI recommendation card** (accent-outline = *recommending*, principle 6): *"Recommend drawing €3,000, repaid on invoice #1042. In line with your cash flow and a 96%-reliable payer."* with grounded reasoning expandable (cash flow, AR aging, repayment history).
- **Repayment-shape selector:** *Bridge an invoice* (default, recommended) · *Fixed term* · *Open line*. Default is the cash-flow-aligned bridge.
- **"Why is only €X free?"-style explainability** carried over from `02` principle 5 — one tap opens the assumptions behind both the limit and the price.
- **Single filled CTA:** *"Continue to review"* — explicitly naming that a review follows (not "Get money now"; honesty over urgency).

### Honest branch (see §7)
If the requested amount is **larger than the user needs given the forecast**, the recommendation card gently counter-offers a smaller draw or *no draw*: *"You only need €900 to cover the 9-day gap, not €3,000 — drawing less saves you €52."* The AI recommends *against* its own revenue. This is the objective-function proof point in front of faculty.

---

## 3. STEP — Human-Reviewed Grant *(the Annex III gate)*

| Field | Value |
|---|---|
| **Surface** | A calm "In review" state in the slide-over, resolving to a grant decision screen |
| **Decision served** | *Do we grant this specific loan, at these terms, to this business?* (AI recommends — **a human decides**) |
| **AI role** | **RECOMMENDING — human-loop IN.** The AI produces a recommendation + reasoning; it does **not** decide. |
| **Human-on-the-loop?** | **YES — this is the gate.** Credit-scoring of a natural person = high-risk, **AI Act Annex III §5(b)**; **GDPR Art. 22(1)** restricts a solely-automated credit refusal. A qualified human reviewer makes the credit decision. (`01` Regulatory spine; README architecture table.) |

### Why this step exists at all — and is *deliberately* not 310-zero-human
The Chinese 3-1-0 model approves with **0 human interaction**. We copy zero-human **pre-qualification** (steps 1–2) and explicitly **do not** copy zero-human **granting**. This is both our compliance posture and a differentiator vs the WeBank/MYbank model. **Marketing must never imply autonomous lending.** Only the *sizing* was autonomous; the *grant* is reviewed.

### What data/signal drives the human's decision
The reviewer sees the **AI recommendation card, fully grounded**:
- Live cash flow, runway, burn.
- The specific receivable being bridged + its per-client reliability score (the closed-loop asset).
- Repayment history / earned-trust tier.
- The forecast and its assumptions.
- A plain-language **recommendation** (approve / approve-with-different-terms / decline) **with reasons** — the human can override in either direction, and the override is logged.

### Key elements
- **Calm "In review" state** — *"A person is reviewing this. Usually under a minute."* (turns the regulatory constraint into the trust feature, principle 4; `02` "a person reviewed this in Xs"). No spinner-anxiety; show the median review time honestly.
- **Distinct, verified "Human-reviewed" badge** — visually *separate* from the predicting/recommending/acting chips, locked to the credit decision. This badge appears **nowhere else** in the app, so it carries real signal.
- **AI recommendation card** preserved on the result screen, so the user sees *what the AI suggested* and *that a human confirmed/adjusted it* — explainability + Art. 22 "right to human intervention / to contest" surfaced as UI.
- **Decline / counter-terms path** is graceful and explained: if the human declines or changes terms, the user gets the *reason* and a route to contest/ask (Art. 22 right), not a dead end.
- **Audit-trail link** — *"See how this decision was made →"* deep-links to the AI-activity / decision log (More tab), satisfying auditability.

### The two-clock honesty rule
Show **two truths** at this step: *"Sizing was instant (the safe-to-borrow number)."* and *"This draw was reviewed by a person before approval."* Never blur them into a single "approved instantly" claim.

---

## 4. STEP — Disbursed *(one-tap confirm → live)*

| Field | Value |
|---|---|
| **Surface** | Confirmation in the slide-over → Financing hub flips to live-line state |
| **Decision served** | *Confirm the draw and put the money where I need it.* |
| **AI role** | **ACTING — with an Undo window.** The autonomous disbursement action is shown as *acting* (principle 6: acting = done, undo). |
| **Human-on-the-loop?** | Grant already cleared (step 3). The *confirm* is the user's one tap; disbursement is the automated act. |

### What data/signal drives it
The cleared grant from step 3 + the destination account chosen by the user. Funds land **instantly** in the selected account (revolving-utility feel).

### Key elements
- **All-in cost shown one last time before the one-tap confirm** — per-day interest + total — so the price the user agreed to in step 2 is the price they confirm. No divergence.
- **One-tap "Confirm draw"** → funds land instantly.
- **Financing hub flips to a revolving "available / drawn" bar** — a single bar that will refill as the user repays (the line is a *utility*, not a re-applied product).
- **Live per-day readout** — *"You're paying ≈ €1.40/day."* Honest, always-visible running cost.
- **Undo window** on the disbursement action (acting = undo, principle 6) — a short, clearly-timed window to reverse before the day's interest is meaningful.
- **Plain-language confirmation, not a task** — calm receipt, in the spirit of "the best screen is sometimes no screen" (`02` principle 2).

---

## 5. STEP — Monitored *(continuous, calm, mission-aligned)*

| Field | Value |
|---|---|
| **Surface** | Ambient across Home + Financing hub; proactive nudges via the CFO-style assistant |
| **Decision served** | *Am I still okay — and is the line still right-sized for me?* |
| **AI role** | **PREDICTING / RECOMMENDING — human-loop OUT for monitoring, IN for any limit change that functions as a credit decision.** |
| **Human-on-the-loop?** | Monitoring is autonomous. **A limit *increase offer* is recommended by AI but the increase is granted human-on-the-loop** (same Annex III gate as step 3). A limit *decrease* that materially restricts credit is graduated, explained, and recoverable — and routed through human review when it functions as an adverse credit decision (Art. 22). |

### What data/signal drives it
The non-credit core watches cash flow, runway, and AR in **real time**, refreshing the forecast and the safe-to-borrow headroom continuously. Monitoring is the engine behind both directions of the limit.

### Key elements
- **Headroom refreshes live** — the safe-to-borrow number on Home updates as inflows land and the forecast sharpens.
- **Graduated, explained, recoverable limit changes** — this is the **mission guardrail** and an explicit *anti-pattern correction* of the source model. The real WeBank/MYbank model cuts the log credit limit by **~77% on a single overdue** (NBER w30160). For a *customer-financial-health* objective function, hard-yanking a runway-critical limit at the worst moment is the opposite of the mission. NetBank instead steps the limit down gradually, **explains why**, shows the **path back**, and never blindsides. (Recon pitfall: survivorship/pro-cyclicality.)
- **Proactive CFO-style assistant** (cf. MYbank "Lark", reported +€-equivalent uplift) — when forecasted inflows support it, it *offers* a limit increase: *"Your last 3 months support a higher line — want me to request +€2,000?"* AI shown = **recommending**, with Undo; the increase itself goes through the human grant gate.
- **Contextual cross-surface nudge** — may surface a Services-marketplace partner against a real signal (*"VAT deadline in 9 days — book a tax partner?"*), deep-linked, never spammy.
- **Mission-aligned tone** — calm nudges, not alarms (positive prompting; `02` anti-engagement stance).

---

## 6. STEP — Repay *(revolving utility, not re-application)*

| Field | Value |
|---|---|
| **Surface** | Financing hub (the available/drawn bar) — one-tap, or automatic on the bridged invoice landing |
| **Decision served** | *Settle the draw — and get my headroom back.* |
| **AI role** | **ACTING — auto-repay on the bridged invoice (with undo) — or one-tap manual.** |
| **Human-on-the-loop?** | None needed — repayment is not an adverse credit decision. |

### What data/signal drives it
- The **bridged receivable landing** (default repayment trigger) — when invoice #1042 is paid, the bridge auto-settles; the user gets a calm confirmation, not a task.
- Or a **one-tap manual repayment** at any time — **interest accrues per-day-outstanding, no early-repayment penalty** (revolving-utility model). Repaying early is always cheaper and never penalized.

### Key elements
- **The "available / drawn" bar refills in real time** on repayment — the line restores instantly; no re-application, no new form (recon: revolving line restores in real time).
- **Clean repayment advances the earned-trust ladder** — visibly. A small, honest moment: *"Repaid on time → Tier 3 unlocked → your safe-to-borrow ceiling rose to €X, rate dropped to Y%."* This **closes the loop back to step 1** (more trust + more data → more headroom + cheaper credit).
- **No rollover trap** — the product never rolls an unpaid bridge into a bigger, costlier one (the explicit anti-pattern from `02`'s hero-flow brief: "repayment-without-rollover"). If a bridged invoice slips, the *honest* path is a graduated, explained extension — surfaced, not silently compounded.
- **The inverted-flywheel proof** — if the user's *dependence on the bridge falls over time*, that is shown as a **win** (calmer, more runway), never as churn. Declining bridge-use is the mission succeeding (README objective function).

---

## 7. The honest "you don't need to borrow — this gap self-resolves" moment *(first-class, not an edge case)*

This is the single sharpest expression of the objective function, and it must be **designed as a primary branch of the hero flow**, reachable from steps 1 and 2.

### When it fires
The live forecast (the closed-loop, per-client reliability model) predicts a **reliable inflow that closes the user's cash gap before the cost of borrowing is justified** — e.g. a 96%-on-time client's invoice lands in 9 days, covering a gap the user was about to bridge for 27 days.

### What it looks like
- **The safe-to-borrow hero inverts** from "draw in seconds" to a calm advisory card: *"You probably don't need to borrow. Studio Vermell (pays 96% on time) covers this in ~9 days — bridging would cost you €38 for nothing."*
- **The primary action de-escalates** — the filled "Request a draw" CTA becomes a **ghost** *"Set a reminder for the 9th instead"* / *"Watch this gap"* — the cheapest, healthiest action is the most prominent one.
- **The number is inspectable** — *"Why are we so sure? See the 90-day forecast and this client's payment history →"* (explainability; the forecast must *earn* the "don't borrow" advice, principle 5).
- **A safety net remains one tap away** — *"If it slips, your €X line is still here, instantly."* Honesty about uncertainty without nagging toward a loan.
- **The moment is logged as a saved cost** — a quiet running tally (*"NetBank has saved you €310 in avoided borrowing this year"*) reframes restraint as the product's value, the inverted-flywheel made visible (`02` north star).

### Why it matters for the defense
> Copying the data pipe is a sprint; copying a P&L that profits when bridge-dependence *falls* means cannibalizing your own revenue model (`01` moat). This screen **is** that P&L, rendered. An interchange/engagement-driven incumbent is structurally disincentivized to ship it. That is the moat you can point at on a slide.

---

## 8. AI-legibility & human-on-the-loop map (one glance)

| Step | AI role (chip) | Human-on-the-loop? | Regulatory anchor |
|---|---|---|---|
| 1. Safe to Borrow | **Predicting** (ghost) | No — sizing only | Outside Annex III (capacity estimate, not a decision) |
| 2. Request | **Recommending** (accent-outline) | No — pre-grant recommendation | — |
| 3. **Grant** | **Recommending** → **Human-reviewed** badge | **YES — the gate** | **Annex III §5(b) + GDPR Art. 22** |
| 4. Disbursed | **Acting** (+ Undo) | No — executes cleared grant | — |
| 5. Monitored | **Predicting / Recommending** | Increase = human-grant; adverse cut = human-reviewed, graduated | Annex III / Art. 22 for adverse decisions |
| 6. Repay | **Acting** (+ Undo) | No | — |

**Three distinct visual vocabularies, never blurred:** (a) the predicting/recommending/acting **chip** for autonomous AI states with Undo on "acting"; (b) the separate, verified **"Human-reviewed" badge** that appears *only* on the credit grant; (c) the **earned-trust ladder** rungs that explain *why the number is what it is*.

---

## 9. Image briefs — the 2–3 key screens of this flow

> Shared art direction (lock for every screen). **Dark, professional, premium — not OLED-cheap.** Canvas = violet-tinted near-black (~`#0E1116`, never `#000`); elevated surfaces via *lightening* (~+4–6% lightness) not drop-shadows; hairline borders at low white-alpha. **One** filled-accent CTA per screen (single-voltage) — pick NetBank's own accent (a **green/teal** signals the *financial-health* objective, deliberately **not** Mercury indigo); decoration-blue washes reserved for the hero number and charts, **never** on buttons. Typography: Inter / Inter Display, light-to-regular weights, negative tracking on display; **tabular numerals (`tnum`) on every figure** so money never jitters. Gains/losses encoded **blue=gain / amber=loss + glyph + sign** (never red/green alone). Mobile portrait, 9pt grid, generous spacing, ruthless above-the-fold priority (no single giant chart eating the viewport — Mercury's documented Home flaw). Subtle, trust-building motion only; no bounce. Show realistic Spanish-freelancer data (€, EU formatting).

### Brief A — "Safe to Borrow" hub *(step 1 — the moat hero)*
A dark mobile screen, top→bottom: a compact synthesized-number band (Total cash, Burn, Runway in tabular numerals, small and calm); below it the **dominant hero tile** — *"Safe to borrow: €4,200"* in a decoration-blue wash with a quiet micro-label *"already approved · no application · sizing is instant"*; beneath it a horizontal **data-elastic limit meter** with three explicit unlock chips (*Connect payroll → +€1,800*, *Connect VAT → +€2,400*, *Add 2nd bank → +€900*); a 4-rung **earned-trust ladder** (Tier 0→3) with the current rung lit and the next-rung € delta; a single filled **green/teal CTA "Request a draw"** at the thumb zone; a quiet *"Why €4,200? See the 90-day forecast →"* link. A ghost **"Predicting"** chip near the hero. Everything else text/ghost. Calm, dense-but-uncluttered, premium.

### Brief B — "Human-Reviewed Grant" *(step 3 — the Annex III gate, the differentiator)*
Same dark language. Centerpiece: a calm **"In review — a person is checking this. Usually under a minute"** state resolving into an approved card that carries a **distinct, verified "Human-reviewed" badge** (a checkmark-shield treatment, visually unlike the AI chips — this badge appears nowhere else in the app). Below it, the preserved **AI recommendation card** (accent-outline *"Recommending"*): *"Recommended €3,000, repaid on invoice #1042 — 96%-reliable payer,"* with an expandable "reasons" affordance. A **two-clock honesty strip**: *"Sizing was instant · This draw was reviewed by a person."* A quiet *"See how this decision was made →"* audit link. The single filled CTA = *"Confirm draw · €3,000"* with the all-in cost (*≈ €1.40/day · €38 total*) shown right above it in tabular numerals. The emotional read: a regulatory constraint rendered as a *trust feature*.

### Brief C — "You don't need to borrow" *(step 7 — the objective-function proof)*
Same dark language but **inverted intent**. The hero is *not* a CTA to borrow — it's a calm advisory card: *"You probably don't need to borrow."* with the reasoning in plain language: *"Studio Vermell (pays 96% on time) covers this in ~9 days — bridging would cost €38 for nothing,"* a small inline sparkline of the forecast (blue=incoming, amber=the gap, glyphs not just color) showing the inflow landing *before* the gap. The **primary action is a ghost** *"Remind me on the 9th"* / *"Watch this gap"* (the healthy action is the prominent one); a smaller text link *"If it slips, your €4,200 line is still here →"*. A quiet running tally chip: *"Saved €310 in avoided borrowing this year."* No filled CTA pushing a loan — the screen's whole point is that the most prominent, most beautiful path is the one that makes NetBank *no* money today. This is the slide that proves the moat.
