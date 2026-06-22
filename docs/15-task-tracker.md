# 15 - Task Tracker

This file is the shared task board for the NetBank project. It is meant to be edited directly by teammates or by an agent whenever someone claims, updates, blocks, or completes a task.

## How to use this file

When someone starts a task:

1. Change `Claimed / in progress` from `[ ]` to `[x]`.
2. Set `Status` to `In progress`.
3. Fill in `Owner` with the person's name.
4. Fill in `Started` using `YYYY-MM-DD`.
5. Add a short `Current note` with what they are doing next.

When someone updates a task:

1. Keep the owner and start date.
2. Update `Last updated` using `YYYY-MM-DD`.
3. Replace `Current note` with the latest useful status.
4. Add a branch, PR, deck link, or output path when one exists.

When a task is finished:

1. Change `Done` from `[ ]` to `[x]`.
2. Set `Status` to `Done`.
3. Fill in `Completed` using `YYYY-MM-DD`.
4. Leave a short final note naming the deliverable.

If a task is blocked, set `Status` to `Blocked` and write the blocker in `Current note`. Do not remove another person's owner/start date unless the team agrees the task is abandoned or reassigned.

Suggested agent prompt:

```text
Update docs/15-task-tracker.md: claim NET-03 for <name>, started <YYYY-MM-DD>, and set the current note to "<what they are doing>".
```

## Status key

- `Not started` - no one has claimed it yet.
- `In progress` - someone is actively working on it.
- `Blocked` - claimed, but waiting on a decision, data, access, or review.
- `Review` - deliverable exists and needs team/professor review.
- `Done` - accepted or merged.

---

## NET-01 - UI Mobile App / Demo

- [x] Claimed / in progress
- [x] Done
- Status: Review
- Owner: Claude session (cnob)
- Started: 2026-06-22
- Last updated: 2026-06-22
- Completed: 2026-06-22
- Branch / PR / output: `design/demo/` (index.html + demo.css + demo.js) · linked as the featured card on the root landing page · live: https://builtbycnob.github.io/netbank/design/demo/
- Source docs: `docs/02-mobile-experience.md`, `docs/03-design-spec.md`, `docs/04-slides-mobile-experience.md`, `docs/09-final-deck.md`
- Current note: **DONE 2026-06-22.** Built an INTERACTIVE single-phone clickable prototype (vs the static 8-frame gallery in `design/mockups/`). Spec extracted from canonical docs via a 5-agent workflow; foregrounds the CURRENT locked thesis. Real tab nav (Home · Money · Scan/Pay · Financing · More) + 11 views + a 90-second guided tour with spotlight/coach. **Six scripted product moments, all Playwright-verified live:** (1) three-truths reveal — tap the lying €27,420 → splits into mine/tax/not-here-yet; (2) Tax-Sweep+ auto-sweep animation (pot €2,340→€2,760 + IVA toast, "estimate" tag); (3) Concurso Radar flip → bridge interlock (Caixa flips red, "won't bridge"); (4) per-Payer reliability detail (transparent components + payment-history sparkline + expandable Art.22 "why" + flywheel "predicted vs actual → model updated"); (5) nine-agent bridge sequence ending deliberately at the human-review gate (AML + grant padlocks, _asof tag, sizes-&-warns); (6) honest don't-borrow verdict + avoided-borrowing tally. Honesty visible by construction: AI-legibility chips, human-reviewed shield locked to the grant, illustrative/synthetic labels, blessed-numbers-only. Mobile-responsive (rail stacks). **Open: team review.** Avoided burn/runway-as-core-object per docs/11 locked decisions.

Build the mobile app/demo experience with only the basic backend or mocked functionality needed to make the concept understandable. The demo should prioritize the decision-driven flow already specified in the docs: Home / Command Center, Money, Scan/Pay, Financing, Invoices, Services, and the late-invoice to safe-to-borrow / bridge flow.

Expected scope:

- Show the dark, professional mobile design system and the "Command Center" home concept.
- Use realistic synthetic NetBank data: cash, burn/runway, invoices, tax pot, payer reliability, safe-to-borrow amount, and service nudges.
- Keep backend functionality minimal: mock API, local JSON, or simple persistence is enough unless the team decides otherwise.
- Make the AI modes visible in the UI: Predicting, Recommending, Acting + Undo, and Human-reviewed only on the credit grant.
- Do not make the demo a generic banking dashboard; it should make the NetBank thesis visible in the first screen.

Definition of done:

- The app can be run or opened by the team.
- The main demo flow is clickable enough for presentation use.
- The UI reflects the current docs and does not contradict the regulatory split.

---

## NET-02 - App Features / Product Backlog

- [ ] Claimed / in progress
- [ ] Done
- Status: Not started
- Owner:
- Started:
- Last updated:
- Completed:
- Branch / PR / output:
- Source docs: `docs/02-mobile-experience.md`, `docs/03-design-spec.md`, `docs/07-services-marketplace.md`, `docs/10-value-ideas.md`, `docs/11-team-ideas-evaluation.md`, `docs/14-differentiation-and-roadmap.md`
- Current note:

Turn the scattered product ideas into a clean feature backlog with priorities, dependencies, and what belongs in the demo versus the roadmap. The docs already converge on three pillars plus supporting features.

Suggested priority spine:

- Tax-Sweep+: locked VAT/IRPF set-aside, readiness export, gestor handoff, never automated filing.
- Concurso Radar / Client Health Badge: public counterparty distress signal wired into receivables and bridge pricing.
- Named-receivable bridge: transparent bridge fee, human-reviewed grant, don't-borrow branch.
- Servicing re-date: "collections as care" with disclosed, borrower-confirmed re-date.
- Services marketplace: route-don't-own partner panel for gestor, CFO, legal, compliance, payroll, grants, collections.
- Calm Score / concentration watch / first-invoice confidence band as experience or roadmap features.

Definition of done:

- Features are grouped by MVP, demo-only, near-term build, and deferred/gated roadmap.
- Each feature has a customer value, NetBank value, and a dependency or data source.
- Off-segment startup features are either removed or explicitly reframed for the locked ICP.

---

## NET-03 - Ontology

- [ ] Claimed / in progress
- [ ] Done
- Status: Not started
- Owner:
- Started:
- Last updated:
- Completed:
- Branch / PR / output:
- Source docs: `docs/05-predictive-ai.md`, `docs/08-agentic-loan-journey.md`, `docs/09-final-deck.md`, `docs/13-instructor-deck-alignment.md`, `docs/14-differentiation-and-roadmap.md`
- Current note:

Define the project ontology clearly enough that the app, Orange workflow, agentic workflow, and deck all use the same objects. The important addition versus a generic banking ontology is the first-class `Payer` object: it is both the underwriting feature and the leakage-grouping key.

Expected ontology objects:

- `Customer`: autonomo, agency, or bootstrapped revenue firm.
- `Account` and `Transaction`: balances, inflows, outflows, spend buckets, tax set-aside events.
- `Invoice` / `Receivable`: issue date, due date, amount, terms, status, paid date as label only.
- `Payer`: named client/counterparty, NIF/CIF when available, trailing payment behavior, public distress signals.
- `Goal`: runway, tax reserve, bridge need, payment timing.
- `Product` / `Loan`: Tax-Sweep+, bridge, Watchtower, services marketplace.
- `Decision` / `Agent`: predictions, recommendations, actions, human review, audit trail.
- `Risk`: likely a logic layer across M1/M2/M3, not necessarily a standalone object.

Definition of done:

- The ontology is documented as a diagram and/or table.
- Each object lists key fields, data source, owner, and what model or UI surface uses it.
- The ontology explicitly separates non-credit sizing/warning from credit grant decisions.

---

## NET-04 - Orange.ai / Orange Data Mining Predictions

- [ ] Claimed / in progress
- [ ] Done
- Status: Not started
- Owner:
- Started:
- Last updated:
- Completed:
- Branch / PR / output:
- Source docs: `docs/05-predictive-ai.md`, `docs/06-predictive-frontier.md`, `docs/08-agentic-loan-journey.md`, `docs/13-instructor-deck-alignment.md`, `docs/14-differentiation-and-roadmap.md`
- Current note:

Create 2-5 Orange predictions using AI-generated or synthetic data based on the ontology. The primary model should be per-invoice late-payment risk because it is the closest match to the NetBank thesis and the docs already specify the Orange workflow.

Recommended prediction set:

1. Per-invoice late-payment risk: `paid_late = paid more than 30 days after due date`.
2. Cash-flow shortfall forecast: shortfall in the next 30 days, using expected receivable timing and outflows.
3. Safe-to-borrow / bridge approval recommendation: informational capacity estimate, not the final credit grant.
4. Profit margin threshold analysis: approve only above a chosen model confidence / expected-margin threshold; calculate expected fee revenue minus expected loss, cost of capital, and review cost.
5. Optional anomaly or segmentation model: expense anomaly, payer reliability archetypes, or customer cohort prior.

Hard requirements:

- Generate data at the right grain: one row per invoice for the headline model.
- Use trailing `_asof_issuance` features only. Do not use `paid_date`, realized `days_late`, or current status as features for the target invoice.
- Use a payer-grouped holdout. Do not use naive random CV as the final model score.
- Include a leakage-gap slide or screenshot: naive CV versus grouped holdout.
- Include confusion matrix, ROC/AUC, calibration, and a cost-sensitive threshold discussion.
- Explain profit margin based on the Orange approval threshold.

Definition of done:

- Synthetic dataset exists and matches the ontology.
- Orange workflow exists or is clearly documented step-by-step.
- Outputs include at least two predictions and a threshold/profit-margin explanation.
- The model is described as sizing/warning/recommending, not auto-granting credit.

---

## NET-05 - Presentation PowerPoint

- [x] Claimed / in progress
- [ ] Done
- Status: Review
- Owner: Claude session (cnob)
- Started: 2026-06-17
- Last updated: 2026-06-18
- Completed:
- Branch / PR / output: `design/slides/` (gold-standard reveal.js deck, manifest-driven `build_deck.py` + `diagrams/_gen.py` + self-hosted fonts) · live: https://builtbycnob.github.io/netbank/design/slides/
- Source docs: `docs/04-slides-mobile-experience.md`, `docs/08-agentic-loan-journey.md`, `docs/09-final-deck.md`, `docs/13-instructor-deck-alignment.md`, `docs/14-differentiation-and-roadmap.md`, `docs/16-deck-design-principles.md`, `docs/17-deck-rebuild-plan.md`
- Current note: **CLARITY REVIEW + APPLY DONE 2026-06-18.** Ran a 14-agent adversarial clarity workflow (7 diagnostic lenses → 3 alternative framings → synthesis → 3 critics). User picked the **"one object · one loop · one objective" mechanism spine + plain-English relabel** (scope: everything). **Applied across all 11 slides:** S5 ontology re-titled + bands → WHAT WE STORE/THE BRAINS/WHAT IT DOES (satellite + loop-arrow deleted); S6 dropped absolutist "only", neutral chips so the lone mint return-arrow pops; S7 "the honest score is the LOWER one — 0.78" banner + glosses + synthetic chip; **S8 unit error cost-to-serve → cost-to-income** (wall + all feeding notes); S9 tiers in self-describing words (no "only moat" overclaim); S10 WTP kill-line in words + clock glyphs; S11 neutral team rings + concrete ILLUSTRATIVE ask + bookend; deck-wide quiet OBJECT/LOOP/OBJECTIVE breadcrumb. Re-audited (4-agent: Numbers+Segment PASS; Rubric/Honesty/Comprehension pass-with-fixes → all residual fixes applied). All 11 slides Playwright-verified; build = 0 warnings. **Prior milestone (2026-06-17, @3c9b825):** gold-standard rebuild (11-slide pitch spine, assertion-evidence, real S7 charts, scale-hack deleted, self-hosted fonts). **Pending: team review + oral rehearsal.** Open: editable **.pptx** (DoD; current handout = offline PDF via `?print-pdf`); deferred polish = P10 fragments/auto-animate pacing; pick home concept (A); WTP test (docs/12).

Create or finalize the PowerPoint deck for the course presentation. The existing docs already define a 20-25 slide target and a strong `docs/09-final-deck.md` structure with bullets, visuals, speaker notes, and defense answers.

Expected deck requirements:

- 20-25 slides, not an underbuilt short deck.
- Include the professor-aligned spine: customer, app/ontology, prediction, process, agents, operating model/scale, business model, demo, reflection.
- Include NetBank's Netflix logic slide: recommendations become next-best financial decisions, not product browsing.
- Include the ontology and the first-class Payer object.
- Include the Orange leakage-gap / confusion-matrix / calibration story.
- Include before/after loan journey and the nine-agent system.
- Include the business model and comparison to ImaginBank / Nubank / generic "Netflix Bank".
- Include the reflection: what surprised us, what AI did, what stayed human, and what we would build next.

Definition of done:

- Editable `.pptx` exists.
- Slides have visuals or clear visual directions.
- Key numbers match the locked number-defense card.
- Speaker notes or oral-defense answers are available.

---

## NET-06 - Value Prop, Business Model, Financial Model, Token Costs, and Financial Reasoning

- [ ] Claimed / in progress
- [ ] Done
- Status: Not started
- Owner:
- Started:
- Last updated:
- Completed:
- Branch / PR / output:
- Source docs: `README.md`, `docs/01-client-and-evidence.md`, `docs/07-services-marketplace.md`, `docs/10-value-ideas.md`, `docs/11-team-ideas-evaluation.md`, `docs/12-tax-sweep-wtp-test.md`, `docs/14-differentiation-and-roadmap.md`
- Current note:

Turn the value proposition and financial story into a clear, defensible model. This should connect the product thesis to revenue, cost, risk, and AI operating cost.

Required pieces:

- Value proposition: "Your bank reads your invoices, not just your balance."
- Revenue lines: Tax-Sweep+ subscription, bridge fee on named receivables, Watchtower / Concurso paid tier, partner-paid marketplace leads, possible payment rail economics.
- Cost lines: model/API/token cost, OCR or document extraction, human credit review, compliance, data sources, customer support, infrastructure, cost of capital.
- Lending economics: bridge fee, expected loss, cost of capital, human review cost, default/loss assumptions, and margin sensitivity.
- Token / AI cost model: estimate the number of AI calls per customer/month by workflow, classify which parts use LLMs versus cheaper ML/rules, and compute low/base/high monthly cost per active customer.
- WTP plan: Tax-Sweep+ test from `docs/12`, including the free-toggle control and charge-authorization threshold.

Definition of done:

- A spreadsheet, model table, or financial memo exists.
- Assumptions are labeled as sourced, estimated, or to validate.
- Token costs are included instead of hand-waved.
- The model does not mix unlike units without explaining them.

---

## NET-07 - Workflow Classification: Agent vs Machine Learning vs Other AI

- [ ] Claimed / in progress
- [ ] Done
- Status: Not started
- Owner:
- Started:
- Last updated:
- Completed:
- Branch / PR / output:
- Source docs: `docs/03-design-spec.md`, `docs/05-predictive-ai.md`, `docs/06-predictive-frontier.md`, `docs/08-agentic-loan-journey.md`, `docs/13-instructor-deck-alignment.md`
- Current note:

Define exactly what parts of the product are agentic, what parts are machine learning, what parts are LLM/OCR/other AI, and what parts are rules or ordinary software. This is important for the "Role of AI" rubric and for avoiding vague "AI does everything" claims.

Suggested classification:

- Machine learning: per-invoice late-payment risk, cash-flow shortfall, calibration, thresholding, cohort prior, anomaly detection.
- Agentic workflow: intake, identity/fraud gate, reliability/signals, capacity, credit decision handoff, offer/pricing, disbursement, servicing, repayment/limit, plus conversational and sentiment/friction agents if the deck includes them.
- LLM / generative AI: invoice/document field extraction assistance, plain-language explanations, customer support / conversational context, slide/demo copy generation, maybe contract term extraction.
- Rules and deterministic software: tax set-aside percentage, date arithmetic, NIF/CIF matching where deterministic, status transitions, audit log, notification rules.
- Human-in-the-loop: AML/fraud officer where required and credit reviewer for declines/reduced offers/restructures or whatever counsel requires.

Definition of done:

- A table maps every major workflow step to AI type, autonomy level, human role, data source, and regulatory posture.
- The credit grant is never described as fully autonomous.
- The agentic claim is tied to bounded goals, signals, actions, handoffs, and escalation rules.

---

## NET-08 - Differentiation: How We Are Different and Why the System Is Better

- [x] Claimed / in progress
- [ ] Done
- Status: Review
- Owner: Claude session (cnob)
- Started: 2026-06-17
- Last updated: 2026-06-17
- Completed:
- Branch / PR / output: docs/09 Slides 13/16/17 (+ consistency across the deck) · @aef9df4
- Source docs: `docs/01-client-and-evidence.md`, `docs/05-predictive-ai.md`, `docs/08-agentic-loan-journey.md`, `docs/09-final-deck.md`, `docs/11-team-ideas-evaluation.md`, `docs/14-differentiation-and-roadmap.md`
- Current note: Differentiation REFRAME applied to docs/09 per docs/14 verdict — "one object, one loop, one objective" in three honest tiers (T0 demonstrated today: Payer-object + grouped-CV + reg-arch · T1 the loop = compounding mechanism, NOT yet present · T2 softer objective); concede-then-pivot on S16, gated roadmap S17, deferred cross-customer bureau dropped from present differentiation. Standalone-feature overclaims removed; whole-deck adversarial audit (professor + Qonto VP + factor) = clean. Needs team review.

Write the differentiation argument in a way that is strong but not overclaimed. The docs are clear that Tax-Sweep+, BORME/Concurso checks, and factoring-style bridges are not defensible as standalone features. The stronger argument is the system: one object, one loop, one objective.

Recommended framing:

- One object: the Payer / named receivable is a first-class underwriting object, not just a balance or borrower profile.
- One loop: every predicted-vs-realized payment date becomes an outcome label that can retrain the reliability model.
- One objective: customer financial health, visible through don't-borrow verdicts, lower bridge dependence, and care-based servicing.
- Present strength today: Payer object, grouped-holdout discipline, and regulatory architecture.
- Roadmap strength: closed loop on real labels, then possibly the gated cross-customer payer bureau if both fuzzy entity resolution and GDPR/legal gates clear.

Comparisons to cover:

- Generic bank / neobank: optimizes engagement, interchange, product attach, or partner referrals.
- Qonto/Revolut/Mercury: can copy screens and tax pots, but copying the health objective hurts their economics.
- Invoice finance / factoring player: can advance invoices, but does not own the full retained banking relationship and tax/runway context.
- NetBank: prices a specific reliable receivable net of tax/runway context, while showing when not to borrow.

Definition of done:

- Differentiation is written as a deck slide or memo with a crisp one-sentence version.
- Standalone-feature overclaims are removed.
- Current proof, hypotheses, and gated roadmap are separated.
- The answer to "why are we better?" is tied to user outcomes, not just technical novelty.

---

## Update log

| Date | Change | By |
|---|---|---|
| 2026-06-17 | Created initial tracker from README and docs/00-14. | Codex |
| 2026-06-17 | NET-08 differentiation reframe applied to docs/09 (3-tier honest moat, @aef9df4); NET-05 reveal.js HTML deck v1 built (design/slides, @cf18031) — not gold-standard yet, rebuild next. | Claude session (cnob) |
| 2026-06-17 | NET-05 Task A done: deck-design research + plan (docs/16 principles + docs/17 pitch-spine×rubric rebuild plan, 11 slides / 10-12 min, labeled-hypothetical traction/funding). Awaiting team sign-off before rebuild. Added collaborator RUISR (Rui, write). | Claude session (cnob) |
| 2026-06-17 | NET-05 Task B done: gold-standard deck rebuilt (@edf704c) + adversarial-audit fixes (@3c9b825). 11-slide pitch spine, assertion-evidence, real SVG diagrams + AUC-accurate S7 charts, scale-hack deleted, self-hosted fonts. 3 workflows (research / content-draft+verify / audit). Status → Review (team review + .pptx open). | Claude session (cnob) |
| 2026-06-17 | Late fixes: course label **ESADE MIM → ESADE** (not a MIM course) across deck/landing/README/CLAUDE.md/docs (@c70767d); **team is SIX** Corrado/Navid/Manon/Marti/Rui/Tim — close slide + S26 + CLAUDE.md (@a7d652c). NEXT (post session-relay) = **big adversarial clarity/quality/gap review** of the deck (user: can be much clearer / explained differently). Manon needs a GitHub username to be invited. | Claude session (cnob) |
| 2026-06-22 | NET-01 **DONE** → interactive clickable demo at `design/demo/` (index.html + demo.css + demo.js), featured on the landing page. One navigable phone + guided tour; 6 scripted moments (three-truths reveal, Tax-Sweep+ animation, Concurso Radar→bridge interlock, per-Payer reliability + flywheel, 9-agent bridge→human gate, don't-borrow verdict). Spec extracted via 5-agent workflow; honesty-by-construction (chips, grant-only shield, illustrative/synthetic, blessed numbers); all moments Playwright-verified. Status → Review (team review). | Claude session (cnob) |
| 2026-06-18 | NET-05 **clarity review + apply**: 14-agent clarity workflow → user picked **"one object · one loop · one objective" mechanism spine + plain-English relabel** (all 11 slides). Applied: S5 plain bands (satellite/loop-arrow deleted), S6 dropped "only" + mint-discipline, S7 "lower=honest" banner, **S8 cost-to-serve→cost-to-income unit fix**, S9 self-describing tiers (no "only moat"), S10 WTP-in-words, S11 neutral team + bookend, deck-wide breadcrumb. 4-agent re-audit (Numbers PASS; Rubric/Honesty/Comprehension pass-with-fixes, all applied). 11/11 Playwright-verified, build 0 warnings. Manon still needs a GitHub username to be invited. | Claude session (cnob) |
