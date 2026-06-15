# NetBank *(working name)*

**An AI-native bank that does for the complexity of money what Apple did for the smartphone: make it simple, calm, and obvious.**

Cumulative project for the ESADE MIM course *Data-Driven Prototyping with AI*. NetBank is an AI-native financial service designed for people whose income is **lumpy** — Spanish *autónomos*, freelancers and micro-creators whose money arrives in invoice-tied lumps, not a monthly salary.

> **The one-liner:** *"Your bank reads your invoices, not just your balance."*

---

## The idea in one paragraph

A single account balance **lies** to a freelancer: it mixes money that is already hers, money that belongs to the tax office, and money that hasn't arrived yet. NetBank keeps three live truths — **what's actually mine / what's the tax office's (auto-swept the moment a client pays) / what's real but not here yet** (receivables, scored by how reliably each client pays) — forecasts the next cash low-point from her clients' *real* payment habits, and bridges a late invoice against a *specific reliable receivable* instead of an "erratic" profile.

Its objective function is **customer financial health, not engagement or fees** — so, unlike Netflix's watch-time logic, NetBank succeeds when you open it **less**. Declining dependence on a credit bridge is a *win*, not churn.

## Architecture (the load-bearing design choice)

| Layer | What it does | Autonomy | Regulatory posture |
|---|---|---|---|
| **Non-credit autonomous core** | tax-sweep, cash-flow forecast, "what's mine", allocation | fully automated | outside AI Act Annex III & GDPR Art. 22 |
| **Receivable bridge** (credit) | advance against a named invoice | **human-on-the-loop** | credit-scoring = high-risk → human review required |

This split is what lets the "AI-factory" cost economics and EU compliance coexist without contradiction.

## Why this client (converged from two independent analyses)

- Only segment scoring high on **both** willingness-to-pay **and** EU regulatory feasibility.
- The differentiator is structural: a monthly-salary risk model has **no object** for an invoice or a per-client payment-lag distribution.
- The moat is **not** "we see invoice data" (false in Spain — Verifactu/SII make it commodity). It is the **closed loop** (every realized payment date retrains a per-client reliability model) **+ a financial-health objective an interchange/fee-driven incumbent structurally will not adopt.**

## Status

- ✅ Client + value proposition — **converged & evidence-backed** ([`docs/01`](docs/01-client-and-evidence.md))
- ✅ Mobile experience — HMW + decision map + screen map ([`docs/02`](docs/02-mobile-experience.md)) · design spec ([`docs/03`](docs/03-design-spec.md)) · slides ([`docs/04`](docs/04-slides-mobile-experience.md))
- ✅ **8 dark mockups live** → https://builtbycnob.github.io/netbank/ (3 home concepts A/B/C — **A "Command Center" recommended**)
- ✅ Predictive AI ([`docs/05`](docs/05-predictive-ai.md)) · data frontier ([`docs/06`](docs/06-predictive-frontier.md)) · services marketplace ([`docs/07`](docs/07-services-marketplace.md))
- ✅ **Agentic loan journey** — Role of AI: 9-agent system + the "collections disappears" thesis + drop-in deck slide ([`docs/08`](docs/08-agentic-loan-journey.md))
- ✅ **Final deck assembled** — all 8 rubric dimensions, per-slide oral defenses + a known-soft-spots appendix ([`docs/09`](docs/09-final-deck.md))
- ⬜ Team picks home concept · rehearse the oral defense

## Repo structure

```
README.md                      ← you are here
docs/
  01-client-and-evidence.md    ← chosen client, VP, verified numbers + sources
  02-mobile-experience.md      ← HMW, design principles, screen map, decisions
  03-design-spec.md            ← (generated) decision-driven screen specs + hero flow
design/                        ← (coming) mockups / image briefs
```

## Notes for the team

- **Working name only.** "NetBank" is a placeholder — naming is a later decision.
- **Defend every number.** Each figure in `docs/01` has a source URL. Faculty grill every team member and dock 1 point per undefended claim — read the **caveats** section before citing.
- ⚠️ **This repo is public.** Other ESADE teams could find it. If you'd rather not expose the design, ask to flip it to **private + collaborators** (one command). The confidential course syllabus is intentionally **not** committed here.
