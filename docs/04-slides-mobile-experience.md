# NetBank — Mobile Experience: Designing Decisions, Not Screens

> ESADE — final deck, "Mobile Experience" section.
> Every slide: title · fixed bullets · [VISUAL] · SPEAKER NOTES · DEFENSE (professor Q + crisp answer).
> Numbers are locked to the team's evidence doc (`docs/01-client-and-evidence.md`) with the favorable-rounding and contradiction fixes applied from the defense pass.

---

## Slide 1 — Designing decisions, not screens

- We started from the **money decisions** a cash-flow-positive owner of a <10-person business makes — not from "we need a home tab."
- Chain: **Problem → How-Might-We → Decision → Moment → Screen.**
- A screen earns its place only if it serves a decision. **CUT: a stand-alone Settings/Profile tab and an income-chart "vanity" screen** — no money decision behind them.
- Two of our seven decisions resolve to **no screen at all** — because the best screen is sometimes none.

[VISUAL: Horizontal 5-node flow Problem → HMW → Decision → Moment → Screen. One worked example threaded underneath in grey — "income is lumpy" → "HMW: how do we pay a steady wage?" → "how much can I safely pay myself this month?" → 1st-of-month → a Self-pay **transfer** with a suggested €X. A second, dimmer branch shows the Moment resolving to NO screen — "tax set-aside + OCR capture just happen." Two struck-through chips float to the side: ~~Settings tab~~ ~~Income-chart screen~~.]

**SPEAKER NOTES:** This is the method slide and the section thesis. Faculty penalize decks that present screens as a foregone wishlist, so we invert it: design is a forcing function on decisions. The proof it's a method and not a slogan is the two struck-through chips — we killed a stand-alone Settings tab and a vanity income chart because no money decision sat behind them. We also show that the chain is **not** 1-screen-per-problem: some decisions resolve to no screen (tax-sweep, OCR), which pre-empts the "your linear diagram contradicts best-screen-is-no-screen" attack. The worked artifact is a **transfer**, not a card, because HMW "pay myself" resolves to a wage figure, not a payment instrument.

**DEFENSE — Q: "Prove this is a method, not a slogan you wrote after drawing the screens. Name one thing you actually cut."**
A: "We killed a stand-alone Settings tab and an income-chart vanity screen — no money decision sat behind either — and two of our seven decisions resolve to no screen at all, because the best screen is sometimes none."

---

## Slide 2 — The client and the wound

- Freelancers, agencies, bootstrapped startups: **<10 staff, ~€10k–€1M revenue**, cash-flow-positive.
- **3.43M autónomos in Spain** (Dec 2025) — solvent over the year.
- **Micro-firms collect in ~81 days** on average vs a **60-day legal limit** (CEPYME Observatorio de Morosidad, FY2025).
- The wound is **two-headed**: invoicers wait on booked-but-uncollected cash; project/SaaS businesses ride lumpy, seasonal income. Solvent annually, **blind week to week.**

[VISUAL: Left — segment band (solo → agency → <10-person startup) with the €10k–€1M revenue range. Right — split into two stacked timelines: (a) "invoicers": revenue booked vs cash arriving ~81 days later, the gap shaded red, with a dotted "60-day legal limit" line inside the gap; (b) "project/SaaS": a jagged lumpy-income curve dipping below a flat cost line in a "dry month." Small caption: "two pains, one segment band."]

**SPEAKER NOTES:** Two clean, checkable anchors. The **3.43M** is the exact 3,425,767 figure (lamoncloa.gob.es, Dec 2025, +1.2% YoY) — I round on the slide, exact orally. On the collection number I deliberately do **not** quote the inflated ">85 days" August headline; the defensible FY2025 micro figure is **~81 days against a 60-day legal limit**, and the 81-vs-60 gap is a stronger argument than an overstated 85. I split the wound into two anchors so it covers the whole band I drew — invoicers (receivables gap) and project/SaaS businesses (lumpy income) — rather than one B2B-invoicing claim that wouldn't cover bootstrapped startups. "Blind week to week" is our behavioral hypothesis; we treat it as testable and would back it with our own short autónomo interviews, not a UK proxy.

**DEFENSE — Q: "You wrote '>85 days' but CEPYME's year-end micro figure is ~81 and your notes said 85.6 — which is it, and why did every ambiguity round in your favor?"**
A: "Locked to one figure: ~81 days for micro-firms in FY2025 against a 60-day legal limit (CEPYME). I dropped the August headline because it rounds the pain up — the 81-vs-60 gap is the real, defensible wound."

---

## Slide 3 — North star: the Apple of banking

- Apple made complexity **disappear behind defaults** — that's a measurable bar, not a brag.
- **What disappears:** the non-credit core — forecast, categorization, OCR, safe-borrow capacity — runs behind sensible defaults.
- **What we make visible on purpose:** the credit grant — human-reviewed, "why only €X?" — because under **AI Act Annex III §5(b) + GDPR Art. 22** it's the one screen the user must see.
- Bar: **one primary action per screen**; dark, professional visual language — a deliberate fit for business owners.

[VISUAL: Split screen. Left — a cluttered legacy-banking screen, greyed, many widgets. Right — the NetBank home: dark, one hero number, one action. A divider labelled "same complexity underneath, invisible on top." A small "human-review badge" sits ONLY on the financing element of the right screen, captioned "the one thing we make visible on purpose (Annex III §5(b) / Art. 22)."]

**SPEAKER NOTES:** North-star slide, written to survive the obvious contradiction. The trap is claiming underwriting "disappears like an Apple default" — it doesn't, because the credit grant is human-on-the-loop. So I split "underneath" into two explicit layers: (1) the boring **non-credit core** genuinely disappears behind defaults — that's the Apple analogy; (2) the **credit grant is deliberately visible** with a human-review badge and explainability, because Annex III §5(b) makes credit-scoring high-risk and Art. 22 restricts fully-automated refusal. "Apple of banking" is therefore a commitment to a measurable bar — one primary action per screen — not a buzzword. On tabs I say "Mercury-style flat IA"; Mercury itself uses four, our map tests four-vs-five (next slides), so I don't assert a literal count here.

**DEFENSE — Q: "You said underwriting is 'hidden like an Apple default,' but you also say the credit grant is human-reviewed and explainable. Which is it?"**
A: "Both, on two layers: the non-credit core (forecast, categorization, OCR) disappears behind defaults; the regulated credit grant we keep deliberately visible — human-reviewed and explainable — because under Annex III and Art. 22 that's the one screen the user must see."

---

## Slide 4 — The inverted flywheel

- Our objective function is **customer financial health** — measured, not a vibe: realized-default rate + runway-warning lead-time.
- We're paid by **flat subscriptions** (benchmark Qonto €9/19/39/mo) **+ interest on credit our own model certifies as safe** — paid for accuracy, not volume.
- When health rises, **default losses fall** toward factoring's 1–3% (vs 5.4% EU consumer-credit NPL) — health and our P&L move the **same** direction.
- An interchange/engagement P&L is **structurally disincentivized** to copy this — adopting "borrow less" cannibalizes its core revenue.

[VISUAL: Two loops. Left (red): engagement bank — more time-in-app / more volume → more fees. Right (green, inverted): better forecasting → fewer needless loans → losses fall → more trust → more realized-payment data → sharper underwriting. The "win" arrow points OUT of the app, labelled "fewer needless logins / fewer needless loans." A passive feed (Verifactu/SII + settled transactions) drips into the data node, captioned "loop spins on outcomes, not screen-time." Footnote: "the data is NOT the moat — the closed loop + this P&L are."]

**SPEAKER NOTES:** The sharpest strategic claim and the one most likely to be grilled — so the slide now names the revenue line. We earn on flat subscription tiers plus interest on loans **our runway model certifies as safe**: we're paid for accuracy, not volume, which is exactly why our incentive is *not* identical to the bank's. The KPI is explicit — realized-default rate and runway-warning lead-time — not "calm." I say "structurally **disincentivized**," not "can't": Revolut could ship a runway widget tomorrow, but a borrow-less objective dilutes an interchange/engagement margin, so it's incentive lock-in. The moat is the **closed loop** (every realized payment date retrains a per-client reliability model that prices the next loan), not the objective — and not the data, because Verifactu/SII make invoice data commodity. The loop spins on passively-captured outcomes, so it doesn't need engagement to compound.

**DEFENSE — Q: "If customers borrow less and open the app less, what pays you — and how is that different from a bank that profits when they borrow more?"**
A: "Flat subscriptions plus interest only on loans our model certifies as safe — so when financial health rises, our losses fall toward factoring's 1–3% vs the market's 5.4% NPL: health and our P&L move together. The moat isn't the objective, it's the closed loop where every realized payment retrains the model that prices the next loan."

---

## Slide 5 — The 7 How-Might-We — decisions, AI role, who's on the hook

- **1** HMW know my cash/runway/burn at a glance? *(problem: balance ≠ what's mine)* — Predict
- **2** HMW make tax a non-event? *(problem: quarterly IVA panic)* — **Act, autonomous** (tax set-aside to a locked sub-account)
- **3** HMW see where money goes — bucket / employee / SaaS-AI? — Predict
- **4** HMW recognize & pay an invoice by photo? — Act (OCR) + **undo**
- **5** HMW stop overspend on team cards before it happens? — Recommend / Act + **undo**
- **6** HMW pay myself a steady wage from lumpy income? — Recommend
- **7** HMW reach a CFO / legal / compliance partner? — Act (route/book)
- **THE EXCEPTION — HMW lend safely?** safe-borrow PREDICTION is informational; the **GRANT is human-on-the-loop** — Annex III §5(b) + Art. 22.

[VISUAL: 8-row table, columns: Problem | HMW | AI role | Badge. AI-role color-coded — Predict (blue), Recommend (amber), Act (green). A SEPARATE right-most "Badge" column carries the legal/reversibility marker, NOT the color: credit GRANT row = padlock "human-on-the-loop"; rows 4 & 5 & the salary action = "↺ do-with-undo"; rows 1 & 3 (predict only) = no badge; tax-sweep = "↺ reversible, your own locked sub-account." Caption: "color = how autonomous the AI is; badge = who's legally on the hook."]

**SPEAKER NOTES:** The backbone — every screen maps to one row. Two fixes are load-bearing here. First, these are written as real **HMW questions tied to a problem**, not a relabeled feature list. Second — and this is the key defense — I separate the **autonomy color** from the **legal-risk badge**. Green "Act" is an autonomy level; it does not mean "outside the law." So a small right-most badge marks legal exposure independently: the credit **grant** gets the human padlock (Annex III §5(b) high-risk + Art. 22 solely-automated-adverse-decision); paying an invoice, moving a card limit, and setting salary get "do-with-undo" because they're **reversible**, not solely-automated decisions with legal effect; pure predictions get no badge. The autonomous **tax set-aside** is restored as the true "Act" exemplar — money moves into the user's own locked sub-account on a rule they set, never *leaves*. The clean perimeter: the safe-borrow number is an informational PREDICTION; only the GRANT is the regulated decision.

**DEFENSE — Q: "Why is only the credit grant high-risk? Your OCR pays invoices and your system moves money — why aren't those Annex III too? And these read like features, not HMWs."**
A: "Color is how autonomous the AI is; the badge is who's legally on the hook. Only the credit grant is both high-risk under Annex III §5(b) and a solely-automated decision under Art. 22 — so only it gets the human. Everything green either just predicts or acts with one-tap undo: reversible by design, not legally binding. And each row is a problem-anchored HMW, not a feature."

---

## Slide 6 — The app at a glance — Mercury-style bottom-tab IA, 4 vs 5

- Mercury-style flat bottom-tab IA, **decided live: 4 tabs vs 5.**
- **Home** — total cash, burn, runway, spend per bucket/employee, "safe to borrow €X" *(HMW 1,3,6)*.
- **Cards · Transactions · Invoices** — multi-account & per-seat cards; SaaS/AI spend broken out; OCR AP/AR *(HMW 4,5)*.
- **Financing** *(HMW: lend safely — human-review badge here)* · **Services** marketplace *(HMW 7)*.
- Decision rule: **promote Financing to its own tab only if >X% of sessions touch it** — else it's a Home hero card.

[VISUAL: Two dark phone frames side by side as an explicit A/B — Frame A: 4 tabs (Home · Transactions · Invoices · Services) with Financing as a Home hero card; Frame B: 5 tabs (Home · Cards · Transactions · Invoices · Financing). Each tab carries a tiny "HMW#" number badge. A small human-review badge sits on the Financing tab/card. The Transactions thumbnail calls out a separated "SaaS / AI spend" row. Caption: "one screen map, every tab traced to an HMW; the 4-vs-5 choice is a live A/B with a decision rule."]

**SPEAKER NOTES:** The screen map, with the self-contradiction removed. The title no longer asserts "4-tab" while drawing five — it presents the 4-vs-5 choice as a deliberate **A/B with a decision rule** (promote Financing only if >X% of sessions touch it). Every tab carries an **HMW number badge**, so the trace is visible, not asserted — an oral grader can point at any tab and I name its HMW. On SaaS/AI breakout I'm honest: it's a **segment-fit default**, copyable as a row in a sprint — *not* a moat. Its value is that it feeds the closed loop (burn → runway → safe-to-borrow); the defensibility is the loop, not the row. The human-review badge appears on the Financing surface on the very slide that introduces it, so the Annex III governance is visible throughout, not just on the deep flow.

**DEFENSE — Q: "Is it 4 tabs or 5? And what stops Qonto from copying your SaaS/AI-spend row next week?"**
A: "It's one screen map with every tab traced to an HMW; the 4-vs-5 tab count is an explicit live A/B with a decision rule. The SaaS/AI row is an honest segment default — copyable as a row, not as a loop. Our defensibility is the closed loop behind it, not any single row."

---

## Slide 7 — The home — decided: Command Center, financing as a secondary card

- The home answers one question first: **"How am I doing?"** — target **under 5 seconds** to read.
- **Decision: Concept A — Command Center** (cash, burn, runway, spend grid) is the home.
- The **"safe to borrow €X"** number is a **secondary card, not the hero** — financing is never the front door.
- Rule, traced to the inverted flywheel: **one primary action max, no feed, no gamification** — a good month means you never tap "borrow."

[VISUAL: One chosen dark home (Concept A — Command Center) shown large, with the "safe to borrow €X" demoted to a small secondary card lower down, carrying the "why only €X?" explainability chevron. To the right, two smaller greyed thumbnails labelled "Appendix: B Cash-flow Story / C One-Decision-Now — options we tested." A measurable-criteria strip under the main: time-to-answer "how am I doing?" (<5s) · clicks-to-primary-task · alignment-with-objective (nudges health, not borrowing).]

**SPEAKER NOTES:** We do **not** present an undecided vote on the final deck — that reads as indecision under oral grilling. We **decide**: Concept A (Command Center) is the home, with the safe-to-borrow number demoted to a secondary card. That resolves the inverted-flywheel contradiction — a home that screams "borrow €X" would be engagement-for-lending, the exact trap we claim to invert; instead the home answers "how am I doing?" and financing surfaces only when relevant. I retire the invented axes "glanceability/calm" and replace them with **measurable criteria**: time-to-answer under 5s (testable in a usability session), clicks-to-primary-task, and alignment-with-objective. "Calm" is a *consequence* of not optimizing engagement, not the objective — the objective is financial health. The "why only €X?" chevron supports trust and **previews** the explainability legally required at the grant step; the home number itself is non-credit, outside Annex III.

**DEFENSE — Q: "You put a vote on your FINAL deck — so you haven't decided your most important screen? And if you pick the 'borrow €X' hero, how is that consistent with 'success = borrow less'?"**
A: "We decided: Command Center is the home because it answers 'how am I doing?' in under five seconds, and safe-to-borrow is a secondary card, not the front door — consistent with our objective function, financial health, where a good month means you never tap 'borrow.'"

---

## Slide 8 — Hero flow — embedded lending, human-on-the-loop where the law bites

- **Safe-to-borrow €X → request → human-reviewed grant → disbursed → monitored → repay.**
- Capacity is computed **automatically** on live data we actually hold: **NetBank transactions + Verifactu/SII-visible invoices** — partial, not omniscient.
- **Tiered review:** auto-approve within pre-computed safe capacity; **a person reviews every decline or reduced offer** — Art. 22 bars a fully-automated *adverse* decision.
- **No rollover.** Limit rises on a rule: **N on-time repayments + runway sustained above X weeks.**

[VISUAL: Horizontal 6-step journey strip, a dark phone mockup at each step. Step 3 (grant) enlarged: a "a person reviews any adverse decision" badge + an explainability string e.g. "€8k safe — capped at 6 weeks of burn; 2 late client payments this quarter." Step 6 shows a repayment bar with NO rollover option and a small "limit +€X after 3 on-time repayments" note. Caption flags the perimeter: "auto-compute (outside Annex III) | grant decision human-on-the-loop (Annex III §5(b) / Art. 22)."]

**SPEAKER NOTES:** The deep flow — WeBank core plus the course's agentic loan journey — written to survive a lawyer. Two precise corrections. First, I **bound** "live data": we see NetBank transactions and SII-visible invoices, **not** funds routed through other banks, cash, or Stripe/PayPal — so the edge is the **closed loop** (we also disburse and watch repayment), not omniscient data. Second, I split the badge into what the law actually requires: Art. 22 protects against fully-automated **adverse** decisions, and Annex III is risk-management of a high-risk **system** — neither mandates a human rubber-stamp on every happy-path approval. So the human reviews **declines and reduced offers**, with auto-approval inside pre-computed safe capacity. That tiering also **resolves the unit-economics tension**: humans touch the minority of cases, consistent with the cost-to-serve story. "Trust" is a concrete rule (N on-time repayments + sustained runway), and the explainability string is shown, not asserted.

**DEFENSE — Q: "You say the human badge is 'by regulatory design' — show me where the law requires a human to grant each loan, and reconcile that with 118k customers/employee."**
A: "It doesn't require a human on every approval — Art. 22 bites on automated *adverse* decisions and Annex III on the *system*. So we auto-approve inside pre-computed safe capacity and put a human on every decline or reduced offer — the cases that matter — which is exactly why the badge and our cost-to-serve both hold."

---

## Slide 9 — AI made legible — predict / recommend / act, capped by law and objective

- Every AI moment shows its mode: **Predict** (confidence band, sourced) · **Recommend** (you decide) · **Act** (done, undo).
- **Earned-trust ladder, bounded:** Suggest = credit grant, pay-yourself amount *(never auto, by law/design)* · Do-with-undo = categorization, invoice match, card-limit nudge · Autonomous = OCR capture + **tax set-aside to your own locked sub-account** (money moves, never leaves; SCA-consented once; reversible).
- **Best screen is no screen:** OCR capture and the tax set-aside run in the background, surfacing a calm confirmation.
- **Explainability = meaningful info + one-tap human-review request** (real Art. 22 route), not a tooltip.

[VISUAL: Three UI chips — Predict / Recommend / Act — each on a mini-card: Predict shows a confidence band footnoted "band = runway model on your last-90-day burn, assumption shown, not a black box"; Recommend shows you-decide buttons; Act shows done+undo. Below, the trust ladder as three rungs with a per-action toggle and HARD CEILINGS: the credit chip sits where "autonomous" would be but is stamped "human-reviewed — cannot climb." Tax-sweep rung annotated "→ your own locked sub-account, reversible."]

**SPEAKER NOTES:** This answers "how is your agentic claim different from a rules engine?" — a **visible, per-action trust ladder** the user climbs deliberately, with the UI always labeling the mode. The fix from the defense pass: I **bound the ladder** so it can't be read as "autonomy is the goal." Each rung names real actions and a hard ceiling — the credit grant and the pay-yourself amount can **never** climb past Suggest (by law and by our objective); the only thing that runs unattended is moving the user's **own tax money into their own locked sub-account** on a rule they set, fully reversible, SCA-consented once — money *moves*, never *leaves*, which sidesteps the PSD2/SCA objection. "Best screen is no screen" is concrete: the tax set-aside and OCR surface a calm confirmation, the visible proof of friction removed. The confidence band is **sourced** (runway model on last-90-day burn, assumption shown), and the explainability chevron is reframed as meaningful-info **plus a one-tap human-review request**, which is what Art. 22 actually demands.

**DEFENSE — Q: "You put autonomy on a pedestal, but your north star is 'borrow less, open the app less' and your grant is human-on-the-loop. Which actions can reach 'autonomous,' which are forbidden, and what stops 'undo' from being meaningless once money has left?"**
A: "Autonomy is earned per action and capped by law and by us: the credit grant and pay-yourself amount can never climb past 'suggest' — human-reviewed by design — and the only thing that ever runs unattended is moving your own tax money into your own locked sub-account on a rule you set, fully reversible. The ladder makes the boundary visible; it doesn't push you up it."

---

## Slide 10 — Why structurally better than Mercury, Revolut, a bank

- **Unit economics:** target cost-to-income **below the incumbent baseline** — CaixaBank **38.5%** (audited FY24, ~443 customers/employee) — by running the non-credit core automatically and confining humans to the **credit grant only** (~Y% of journeys). *Nubank ~$0.80/customer-mo · WeBank ~118k customers/employee = digital-native ceiling, not our peer.*
- **Objective function:** Revolut/Mercury monetize interchange/engagement → a borrow-less objective is **margin-dilutive** for them. Incentive lock-in, not capability.
- **Risk:** we lend against a **named, SII-confirmed receivable** → loss band **1–3%** (factoring), structurally below **5.4%** unsecured consumer NPL (EBA, Jun 2025). *(Loss-rate to loss-rate.)*
- **Closed loop:** we see the realized repayment **and** its cash-flow context — the data is **not** the moat; this loop is.

[VISUAL: Three-row moat table, columns Bank | Neobank | NetBank. Row 1 "Unit economics" — Bank: 38.5% cost-to-income (audited baseline); Neobank: digital-native CEILING ($0.80 / 118k-per-employee), explicitly tagged "not our segment"; NetBank: "target <X%, humans on credit grant only." Row 2 "Objective function": Bank/Neobank = interchange/engagement (lock-in); NetBank = financial health. Row 3 "Risk": named SII-confirmed receivable → 1–3% loss vs 5.4% consumer NPL, tagged "loss-rate to loss-rate." NetBank column highlighted; footnote: "data is NOT the moat (Verifactu/SII) — the closed loop is."]

**SPEAKER NOTES:** The moat reframe, fully cited and with the unit-mixing fixed. The original row lined up three incompatible units — a P&L **ratio** (38.5% cost-to-income), an absolute **dollar** cost ($0.80/customer-month), and a **headcount** ratio (118k/employee). I split them: CaixaBank's audited **38.5%** is the incumbent **baseline**; Nubank/WeBank are explicitly the **digital-native ceiling, not our peer** — they're mass-consumer, fully-automated lenders, and our credit is human-on-the-loop, so I cite them as direction-of-travel, and I **own** the human-review cost by confining it to the grant only. I say Revolut/Mercury **won't**, not **can't** — incentive lock-in, since a borrow-less objective dilutes their interchange margin. On risk I match metric to metric (loss-rate to loss-rate) and condition it: the 1–3% band applies because we lend against a **named, SII-confirmed receivable**, not a profile. And I keep the honest caveat out loud: the data is commodity under Verifactu/SII — stating that is what earns the point rather than losing it.

**DEFENSE — Q: "Your cost row mixes a 38.5% ratio, a $0.80 figure, and 118k/employee — three different units. Give me NetBank's number, and why does Nubank's automation ceiling even apply when your credit is human-on-the-loop?"**
A: "CaixaBank's audited 38.5% is the incumbent baseline; Nubank/WeBank are the digital-native ceiling, not our peer. Our edge isn't matching their automation — it's that humans touch only the credit grant while the non-credit core runs automatically, and we lend against a confirmed receivable, so our losses sit in the factoring band (1–3%), not the consumer-NPL band (5.4%)."

---

### Appendix — Home concepts we tested (reference only)
- **B — Cash-flow Story:** a narrative timeline of past + forecast. Scored lower on time-to-answer "how am I doing?".
- **C — One Decision Now:** a single hero. Rejected as the home because a borrow-prompt front door contradicts the inverted-flywheel north star; its "one decision" pattern survives inside the Financing flow (Slide 8).

### Number-defense quick card (oral)
- **3,425,767** autónomos, Dec 2025, +1.2% YoY — lamoncloa.gob.es.
- **~81 days** micro-firm collection vs **60-day** legal limit — CEPYME Observatorio de Morosidad, FY2025 (NOT the August ">85" headline).
- **Qonto €9/19/39/mo** · gestor **€60–100/mo** — subscription benchmarks.
- **CaixaBank 38.5%** cost-to-income, 20.3M customers / 45,851 employees (FY24, audited).
- **Nubank ~$0.80**/customer-mo · **WeBank ~118k** customers/employee — digital-native ceiling, NOT our peer (avoid the unaudited "$5–10 cost-to-serve").
- **Factoring 1–3% loss vs 5.4% consumer-credit NPL** — EBA, Jun 2025 (loss-rate to loss-rate; conditioned on a named SII-confirmed receivable).
- **Annex III §5(b)** = credit-scoring high-risk · **GDPR Art. 22** = restricts solely-automated *adverse* credit decisions.
- **CAVEAT (say it):** "only we see invoice data" is FALSE in Spain (Verifactu/SII) — the moat is the closed loop + financial-health objective, not the data.
