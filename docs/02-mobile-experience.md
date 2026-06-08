# 02 — Mobile Experience Design

## North star: the Apple of banking

Apple didn't make the smartphone *more powerful* — it made the existing complexity **disappear** behind sensible defaults, progressive disclosure, and one obvious thing to do. NetBank does the same for a freelancer's money: the tax engine, the receivables model, the cash-flow forecast are all *complex underneath and invisible on top*.

**The inverted flywheel:** success = she opens the app **less** and feels calmer, not more "engaged." This is the single sharpest weaponization of the Netflix metaphor — it makes the metaphor argue *against* watch-time maximization, which is exactly what separates NetBank from a neobank whose P&L *is* engagement.

## Method: Problem → HMW → Decision → Moment → Screen

Never start from "we need a home, a profile, settings." Start from the **decisions** the user (and the AI *for* her) makes. Each decision is a moment; screens are only the surface where moments live. Every element on every screen must trace to a decision and a user problem — orphans get killed.

## The 7 How-Might-We (problems → opportunities, framed on decisions)

| # | HMW | Decision | AI role |
|---|---|---|---|
| 1 | …make the single balance tell the truth, so she always knows which euros are actually hers? | *how much can I safely spend/commit now?* | Predict |
| 2 | …make the quarterly IVA/IRPF a non-event she never braces for? | *(ideally none)* — auto-swept | **Act** |
| 3 | …let her see the dry month before it hits, from her clients' real habits? | *do I act now to cover August?* | Predict |
| 4 | …turn a late-paying client into a solved problem, not a panic? | *bridge this invoice, or wait?* | Recommend → Act (human-on-loop) |
| 5 | …price her credit on the reliability of a *specific* invoice, not her "erratic" profile? | per-receivable underwriting | Predict (high-risk → human) |
| 6 | …make lumpy income feel like a steady paycheck without hiding the truth? | *how much do I pay myself this month?* | Recommend |
| 7 | …prove her real earning power to a landlord/lender who only trusts payslips? | *generate the attestation?* | Generate |

*(+ candidate 8: surface client-concentration risk — "one client = 60% of you" — before it becomes a crisis.)*

## 6 design principles

1. **Home = "Am I okay?" answered at a glance, calm.** Three truths (*mine / tax's / incoming*) + next cash-low + **one** primary action max. Not a feed, no gamification.
2. **The best screen is sometimes no screen.** The tax-sweep just happens; she gets a calm confirmation, not a task — the visible proof of "what friction disappeared."
3. **Earned-trust ladder as a UI pattern:** *suggest → do-with-undo → autonomous*, visible and per-action. Answers "how is your agentic claim different from a rules engine?"
4. **The bridge flow shows the human-on-the-loop** ("a person reviewed this in Xs") — turns a regulatory constraint into a trust feature.
5. **Explainability inside the UI:** "why is only €3.2k free?" is expandable — serves GDPR/AI Act *and* trust.
6. **Make the AI legible on every screen** — predicting (confidence band) / recommending (you decide) / acting (done, undo).

## Screen map (decision-driven)

| Screen | Decision it serves | Primary action | AI shown |
|---|---|---|---|
| Onboarding | connect PSD2 + invoicing tool, set up the three truths | connect | — |
| **Home "Am I okay?"** | how am I doing right now? | (calm) one nudge | Predict |
| Forecast / cash-flow | do I act to cover the dry month? | act / dismiss | Predict |
| Tax pot | is my tax handled? | (mostly invisible) | Act |
| **Bridge (per-invoice)** | bridge this invoice or wait? | request bridge | Recommend + human |
| Clients / receivables | who's reliable? am I concentrated? | — | Predict |
| Self-paycheck | how much do I pay myself? | set / adjust | Recommend |
| Income attestation | prove my income | generate & share | Generate |
| Goals ("watchlist") | survive August / pre-fund Q3 IVA | set goal | — |

**Hero flow (go deep here — the syllabus's "one flow"):** the **late-invoice → bridge** journey, end to end, showing per-client reliability, the honest "don't borrow, this self-resolves", the human-on-the-loop review, explainable terms, and repayment-without-rollover.

## Locked decisions (2026-06-08)

- **Output:** decision-driven spec **+ premium visual mockups** for the deck.
- **Scope:** **full screen map** + **one deep hero flow** (late-invoice → bridge).
- **Home:** **3 competing concepts**, scored — the team chooses in class.

## Inspiration

- **Mercury** (mercury.com) — business banking that feels calm and legible despite real complexity: restrained palette, strong hierarchy, "dashboard that answers a question" rather than a wall of widgets. *(Being studied in depth by the design workflow.)*
- **Apple HIG** — progressive disclosure, sensible defaults, one primary action, "it just works."
- **Freelancer fintech** (Lili, Kontist, Found, Qonto) — how they surface tax-reserve, cash-flow and invoices simply.
