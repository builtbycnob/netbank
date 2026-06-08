# 08 — The Agentic Loan Journey *(Role of AI)*

> Cumulative project, ESADE MIM *Data-Driven Prototyping with AI*. Answers the **Role of AI** rubric dimension. Builds on the models in [`docs/05`](05-predictive-ai.md) (M1 per-invoice late-payment / per-client reliability, M2 cash-flow shortfall, M3 SME default), the data frontier in [`docs/06`](06-predictive-frontier.md), and the lending flow already sketched in [`docs/04`](04-slides-mobile-experience.md) Slides 8–9. This document turns that flow into a **named multi-agent system** and states the thesis a well-run loop earns: **collections disappears.**
>
> **The framing that beats the buzzword grade.** "We use AI" scores nothing. So every stage below is a **goal-directed agent** that owns one sub-objective, consumes a **named signal**, takes a **bounded action**, **hands off** to the next agent, and **escalates to a specific human** exactly where the law or irreversibility demands it — never elsewhere. The agent boundaries are not cosmetic: **they enforce the compliance boundaries** (§"Why agentic").

---

## TL;DR

- **Nine agents**, application → repayment, joined by explicit handoffs. **Exactly two human gates**, and they are *different people under different law*: an **AML/fraud officer** (onboarding) and a **credit reviewer** (the grant).
- Each agent is a **six-field contract**: `objective · signal-in · action-out · autonomy rung · handoff · escalation`.
- **Autonomy is earned per-action from realized outcomes and capped.** The credit **grant can never climb past human-on-the-loop** (Annex III §5(b) + GDPR Art. 22), no matter how much trust accrues — the same hard ceiling as [`docs/04`](04-slides-mobile-experience.md) Slide 9.
- **"Collections disappears":** the *same* underwriting signals keep running after disbursement, so deterioration is **pre-empted weeks early as a reschedule/restructure (care)** instead of chased as dunning. Defaults don't go to zero — the **adversarial collections phase** does.
- **Two hard rules carry over unchanged** ([`docs/05`](05-predictive-ai.md)/[`06`](06-predictive-frontier.md)): leakage is hard-excluded (`_asof_issuance` on every signal, the scored repayment is the *label*, never a feature) and the holdout groups by **global payer**. Across the whole journey, every agent **SIZES and WARNS; the human GRANTS** on every *adverse* outcome (decline / reduced offer / restructure). The happy path *inside pre-computed safe capacity* auto-approves — which Art. 22 does **not** treat as a solely-automated *adverse* decision (§"The grant").

---

## Why "agentic" — and not a workflow with a label glued on (the defense, up front)

A faculty member will open with *"this is a flowchart; where is the agency?"* Four answers, each load-bearing:

1. **Goal-directed, not script-following.** Each agent owns a sub-objective and *chooses* among bounded actions on live signals (approve-in-capacity / counter / hold / escalate), it doesn't execute a fixed branch.
2. **Bounded autonomy, earned and revocable.** Every credit-adjacent action starts at `Suggest`; it climbs the trust ladder only on a **realized-outcome track record**, and it **demotes** if the correction/override rate rises ([`docs/05`](05-predictive-ai.md) Q6). A rules engine has no notion of *earning* or *losing* autonomy — that ladder **is** the agentic core.
3. **It adapts.** The Servicing agent **re-plans** the loan as the payer network moves (§"Collections, disappeared") — the loop reshapes itself, which a static dunning calendar cannot.
4. **The agent boundaries enforce the legal/leakage boundaries.** This is *why* it is multi-agent, not over-engineering: the **fraud lane is quarantined** from credit (fair-lending — [`docs/06`](06-predictive-frontier.md) C8–C10), the **network signal is `_asof`-separated** (leakage — [`docs/06`](06-predictive-frontier.md) §5), the **grant is human-gated** (Annex III §5(b) + Art. 22). Drawing one model would dissolve exactly the boundaries the regulator and the leakage discipline force us to keep. **A separation of agents carries a separation of legal regimes and leakage planes.**

---

## The agent contract (the ontology tie-in)

Three layers, Palantir-style ([[reference_palantir_ontology_framework]]): **Objects** (`Customer`, `Receivable`, `Payer`, `Loan`, `Decision`) · **Logic** (the M1/M2/M3 models + the autonomy & legal rules) · **Actions** (the agents). Every agent declares the same contract so an oral grader can point at any one and get a straight answer:

```
objective    — the single sub-goal it is accountable for
signal-in    — the named inputs it reads (all _asof_issuance)
action-out   — the bounded set of moves it may make
autonomy     — Predict (blue) | Recommend (amber) | Act (green)  +  trust rung  +  hard ceiling
handoff      — which agent / surface it passes control to
escalation   — the trigger that stops it and the specific human it calls (+ legal basis)
```

`Predict / Recommend / Act` is the **mode** the UI always shows; `Suggest → Do-with-undo → Autonomous` is the **trust rung**, identical to [`docs/04`](04-slides-mobile-experience.md) Slide 9.

---

## The journey — nine agents, one human gate (+ one compliance gate)

| # | Stage · **Agent** | Signal in *(all `_asof`)* | Action out | Mode · rung *(ceiling)* | Handoff → | **Escalation → human** |
|--|--|--|--|--|--|--|
| 1 | Application · **Onboarding/Intake** | OAuth grants (PSD2, accounting, Stripe), declared NIF/CIF, account links | Orchestrate consent + connect sources; run **entity resolution** (AR-NIF deterministic first — [`docs/06`](06-predictive-frontier.md)) | **Act** · Do-with-undo | Identity&Fraud | Broken/ambiguous resolution, missing mandate → **ops** (operational, not a credit call) |
| 2 | KYC/AML · **Identity & Fraud** | Doc + biometric match, sanctions/PEP lists, **device/IP/geo, velocity** ([`docs/06`](06-predictive-frontier.md) C9/#9) | Verify identity; AML/synthetic-ID screen; **pass/hold** | **Predict** + gate · *fraud lane only* | Reliability/Signals (on pass) | Sanctions/PEP/fraud flag → **AML & compliance officer** *(AML duty under Ley 10/2010 / EU AMLD — NOT a credit decision; a different human under different law)* |
| 3 | Underwriting data · **Reliability/Signals** | M1 per-client reliability ([`docs/05`](05-predictive-ai.md)); network prior + contagion ([`docs/06`](06-predictive-frontier.md) A1/A3); **counterparty public-distress** by NIF (B1/#3); inbox payer-intent (#5); look-alike cohort (#7) | Emit calibrated `P(paid_late)`, expected days-late, **confidence band**, top-3 drivers | **Predict** (display/feed only) | Capacity | Calibration/leakage drift alarm (single feature ~1.0 AUC; band collapse) → **ML-ops** *(system integrity, internal)* |
| 4 | Capacity · **Safe-to-Borrow** | M2 all-accounts shortfall (#4) + reliability-weighted receivables + committed outflows (VAT/IRPF, contract milestones #6) | **Compute & DISPLAY** the safe-to-borrow ceiling; warn on the dated low-point | **Predict** *(outside Annex III — it sizes, never grants)* | Customer → Credit-Decision | Requested amount **> ceiling** → routes the case to the human gate (#5) |
| 5 | **THE GRANT · Credit-Decision** | The assembled underwriting packet (drivers + band + suggested limit & price) | **Auto-approve within pre-computed safe capacity**; *human* on every **decline / reduced offer / restructure** | **Recommend** · **Suggest — HARD CEILING, can never climb** | Offer&Pricing (on grant) | **The credit reviewer** — *Annex III §5(b) high-risk + GDPR Art. 22 adverse-decision*; automation-bias guards on (below) |
| 6 | Offer · **Offer & Pricing** | Grant decision + reliability score + the **named receivable** | Price the bridge off the regression head (expected days-late → rate); render the **Art. 22 "why only €X / why this rate"** string (LogReg coefficients) | **Recommend** *(customer decides)* | Disbursement (on accept) | Customer disputes the explanation → one-tap **human-review request** (the real Art. 22 route) |
| 7 | Disbursement · **Disbursement** | Signed acceptance + **SCA** consent | Move funds; create a **no-rollover** schedule pegged to the receivable's expected pay-date | **Act** · Do-with-undo *(executes a consented decision)* | Servicing | SCA failure / sanctions re-hit at settlement → **ops/compliance** |
| 8 | Monitoring · **Servicing & Early-Warning** | Live contagion radar (#2), all-accounts shortfall (#4), inbox payer-intent (#5, *gated — post-ethics pass*), counterparty distress (#3) on the **outstanding** receivable + borrower runway | **Pre-empt**: *offer* a re-date to a now-later realized pay-date, suggest a top-up, warn the owner, flag | **Predict** → **Recommend** *(a re-date is a term change → borrower taps; never an unattended Act)* | Repayment / back to #5 for a restructure | Real distress (runway collapse, payer **concurso**) **or** any term-change beyond a same-amount date-shift → **credit reviewer** *(a restructure IS a new credit decision → human-on-the-loop)* |
| 9 | Repayment · **Repayment & Limit** | Realized repayment + refreshed runway | Log **predicted-vs-realized append-only** (closes the loop); trigger retrain; **raise** limit on the rule (N on-time + sustained runway) | **Act** · Do-with-undo | → #3 (retrain) — the loop closes | A limit **CUT** (adverse) → **credit reviewer** *(Art. 22)*; a raise is favorable → no human needed |

Three agents carry the nuance worth saying aloud:

- **#3 Reliability/Signals** is the moat engine. It is the one place the [`docs/06`](06-predictive-frontier.md) frontier lands operationally — but it ships **only the green/quick-win signals first** (counterparty public-distress, look-alike cohort, all-accounts liquidity, contract terms); the **red** cross-customer prior and inbox layers stay gated behind the deferred ethics ledger ([`docs/06`](06-predictive-frontier.md) §4). It **predicts and explains; it never decides.**
- **#5 Credit-Decision** is the only regulated gate (zoomed below).
- **#8 Servicing** is where "collections" is engineered out of existence (its own section below).

---

## The grant — the one human gate, zoomed

The agent does the **legible** work; the human does the **legitimacy** work — and nowhere else, so attention is spent only where an irreversible, regulated outcome turns.

- **The packet, not the verdict.** The agent hands the reviewer the **top-3 drivers + confidence band + suggested limit & price**, sourced from interpretable LogReg coefficients even when a Random Forest is the production scorer ([`docs/05`](05-predictive-ai.md) Q4). It **suggests**; it cannot grant.
- **Tiered, per our reading of the law (pending counsel — [`docs/01`](01-client-and-evidence.md) OQ5).** Art. 22 bites on a **solely-automated *adverse*** decision; Annex III is risk-management of the **system**. On that reading, neither mandates a human rubber-stamp on a happy-path approval — so: **auto-approve inside pre-computed safe capacity; a person reviews every decline, reduced offer, and restructure** — the minority of cases, which is also what keeps the cost-to-serve story honest ([`docs/04`](04-slides-mobile-experience.md) Slides 8/10). *(If counsel reads a favourable automated grant as also in-scope for Art. 22, the tier just widens to cover approvals too — the architecture is unchanged.)*
- **Two humans, not one — a clean defensible split.** The **AML/fraud officer** (#2) and the **credit reviewer** (#5) are different roles under different legal duties (AML obligation under **Ley 10/2010 / EU AMLD** vs Annex III §5(b)/Art. 22). Conflating them is the mistake; separating them is the design.
- **Automation-bias guards** ([`docs/05`](05-predictive-ai.md) Q6): force the driver+band view, require a **typed reason on every decline/edit**, inject low-confidence cases, and **alert if a reviewer's override rate collapses toward zero** (rubber-stamping).
- **Exposure is heterogeneous, stated precisely:** human-on-the-loop is **policy for all grants**; it is **legally mandatory for the autónomo (natural-person) sub-segment** (Art. 22) — an SL is a legal person. *(Don't say "we dodge Annex III"; say the non-credit core sizes/warns and the grant is high-risk by design.)*

---

## Collections, disappeared (the adaptive thesis)

**The claim, bounded honestly:** we do not claim zero defaults. We claim the **adversarial collections phase** — a dunning department chasing a missed payment after the fact — is replaced by **continuous early intervention** that begins *before* the miss.

**The mechanism is just the underwriting, left running.** The Servicing agent (#8) keeps the *same* signals that priced the loan pointed at the *outstanding* receivable:

| Old world (dunning) | NetBank (servicing that pre-empts) | Signal reused |
|---|---|---|
| Wait for the due date to pass, then call | See the payer slowing across the **whole base** weeks early | Contagion radar — [`docs/06`](06-predictive-frontier.md) #2 (A3) |
| Discover the shortfall when a direct debit bounces | Forecast the dated low-point from **all** accounts + processor revenue | All-accounts shortfall — #4 |
| Learn of a dispute when the customer complains | Read "cash is tight / we dispute this" in the **payer's own reply** | Inbox payer-intent — #5 *(gated — post-ethics pass)* |
| Find out about insolvency from the loss | Match the payer's **concurso/RAI filing by NIF** as it posts | Public-distress join — #3 |

So the action when a receivable is going bad is a **borrower-confirmed reschedule** (offer a re-date to the now-later realized pay-date — a term change, so it is a `Recommend` the borrower taps, *never* an unattended `Act`), a **top-up suggestion** (a `Recommend`), or, when the borrower is genuinely distressed, a **restructure** — and a restructure **is a new credit decision, so it escalates straight back to the human grant gate (#5)**. Collections doesn't vanish by magic; it is **re-cast as care and routed through the same legal perimeter**. The honest residual: structural defaults still occur, but they are **rarer, seen earlier, and handled as a credit conversation rather than a chase** — and because we both disburse *and* watch the realized outcome, every one of them **retrains #3** (the closed loop). The honest bound on "earlier": the *direction* is sourced (leading registry/inbox events precede the AR flip by weeks — [`docs/06`](06-predictive-frontier.md)); the *magnitude* on NetBank's own realized-loss label is **to be validated, not asserted**. This is the inverted flywheel made operational: a healthy customer triggers *fewer* servicing events, which is exactly what our P&L rewards ([`docs/04`](04-slides-mobile-experience.md) Slide 4).

---

## Leakage & grouping discipline across the journey *(modeling validity, not ethics)*

The journey adds three places to trip on leakage; all three are closed the same way ([`docs/06`](06-predictive-frontier.md) §5):

1. **Monitoring uses `_asof` only.** The realized repayment of the **scored** receivable is the **label**, never a feature; #8 reads the payer's *other* obligations and *forward* indicators, gated on `timestamp < issue_date`.
2. **Restructure data is post-outcome for *this* loan.** A renegotiated due-date / dunning thread exists *because* the invoice went bad — usable only for the **next** invoice's trailing ledger, never to score the current one.
3. **Network features group by the GLOBAL payer**, and any contagion/graph feature needs a **connected-component-aware** split so neighbors don't straddle the holdout. The naive-CV-vs-grouped-AUC **gap slide** ([`docs/05`](05-predictive-ai.md) step 7) remains the strongest faculty-defense artifact.

---

## Journey-specific failure modes (and mitigations)

| Failure mode | Mitigation |
|---|---|
| **"It's just a workflow"** | The trust ladder *earns and demotes* autonomy; #8 *re-plans*; agent boundaries = legal/leakage boundaries. Agency is demonstrable, not asserted. |
| **Automation bias at the grant** | Force driver+band; typed decline reason; inject low-confidence cases; alert on override-rate collapse. |
| **Fraud signal leaks into credit** | Hard-quarantined fraud lane (#2); device/geo/behavioral **MUST NOT** enter the credit model (fair-lending — [`docs/06`](06-predictive-frontier.md) C8–C10). |
| **"Collections disappears" overclaim** | Bounded explicitly: defaults persist; only the *adversarial phase* is removed; restructure re-enters the human gate. |
| **Monitoring leakage** | `_asof` cutoff on every Servicing signal; scored repayment is label-only. |
| **Cross-customer ethics creep** | #3 ships green/quick-win signals first; red cross-customer prior + inbox stay behind the deferred ethics ledger ([`docs/06`](06-predictive-frontier.md) §4). |
| **Cost-to-serve blows up** | Humans touch only declines/reduced/restructures (the minority) — consistent with the unit-economics row ([`docs/04`](04-slides-mobile-experience.md) Slide 10). |

---

## Deck slide — *Role of AI: the loan that watches itself — and escalates the moment it can't* (drop-in, [`docs/04`](04-slides-mobile-experience.md) format)

> Slots into the master deck as the **Role of AI** centerpiece, after the Mobile-Experience section. Same contract as every other slide: title · bullets · [VISUAL] · SPEAKER NOTES · DEFENSE. *(Title bounds itself: "watches" — autonomous sensing/routing — not "decides"; the irreversible call always escalates.)*

- **Nine agents**, application → repayment, each a contract: *signal in → bounded action → handoff → escalation.* One human gate (the **grant**) + one separate **AML** gate.
- **Autonomy is earned and capped:** every credit-adjacent action starts at *Suggest*; the **grant can never climb past human-on-the-loop** (Annex III §5(b) + Art. 22).
- **Collections disappears:** the same signals that priced the loan keep running, so a souring receivable is **pre-empted as a reschedule/restructure (care)** — not chased as dunning. Defaults persist; the *dunning phase* doesn't.
- **The agent boundaries enforce the compliance boundaries:** fraud quarantined from credit, network signal `_asof`-separated, grant human-gated. That's *why* multi-agent — not decoration.

[VISUAL: A horizontal 9-node agent strip (Intake → Identity&Fraud → **Reliability** → Capacity → **GRANT** → Offer → Disburse → **Servicing** → Repayment) curving back from Repayment into Reliability to close the loop. Node color = mode (Predict blue / Recommend amber / Act green). TWO padlock badges only: a red "AML officer" lock on Identity&Fraud and a red "human-on-the-loop — Annex III §5(b)/Art. 22, cannot climb" lock on GRANT. The Servicing node fans out three pre-emption arrows — "re-date · top-up · restructure↑grant" — over a greyed, struck-through "~~collections / dunning~~" box. A small `_asof` tag sits on every inbound signal arrow; the return loop is labelled "every realized payment retrains Reliability."]

**SPEAKER NOTES:** This is the Role-of-AI backbone and it is written to survive the two attacks. First, *"where's the agency?"* — the ladder **earns and demotes** autonomy from realized outcomes and the Servicing agent **re-plans** the loan, neither of which a rules engine does; and crucially the agent boundaries **enforce** the legal/leakage boundaries (fraud quarantined, network `_asof`-separated, grant human-gated), which is the reason it's multi-agent rather than one model. The honest precision is that the agency is **autonomous sensing and routing, not autonomous granting** — the high-stakes call is human by design, and that is the point, not a gap. Second, *"collections disappears is hype"* — I bound it out loud: defaults don't go to zero, the **adversarial dunning phase** does, because the same underwriting signals keep running and a souring receivable surfaces ahead of the AR flip as a reschedule or a restructure, and a restructure is itself a credit decision so it routes back through the human grant. The only two humans are an AML officer and a credit reviewer — different people, different law — and the grant carries the hard ceiling it can never climb. Every number on adjacent slides is sourced; this slide adds **no new numbers**, only architecture.

**DEFENSE — Q: "Strip the word 'agent' and isn't this just a loan pipeline with a human in the middle? Your autonomy never touches the grant, and the one autonomous move — re-dating a payment — you admit might be illegal. So what *consequential* thing runs unattended that a rules engine with an approver doesn't?"**
A: "The agency isn't autonomous *granting* — it's autonomous *sensing and routing*. Three things a rules engine can't do: it **re-aims** the same underwriting signals at the live receivable; it **earns and demotes** trust on the reversible, own-money actions from realized drift; and every irreversible or adverse turn it **escalates by design** — the re-date is a borrower-confirmed `Recommend`, not an unattended `Act`, precisely so no term changes without a human, and a restructure goes back to the human grant. 'Watches itself' is bounded: defaults still happen — what disappears is the *dunning chase*, because a souring receivable is caught ahead of the miss and handled as care, under the same legal perimeter."

---

## Open questions

- **Servicing reschedule boundary:** we cap an autonomous re-date at a borrower-confirmed `Recommend` (never an unattended `Act`); the open detail is the exact line between a same-amount date-shift (borrower tap) and a term change material enough to route to the #5 human gate.
- **Restructure threshold:** the exact rule that flips a Servicing nudge into a #5 human-gated credit decision (delta in limit / term / rate).
- **Reviewer capacity model:** declines+restructures as a % of journeys at scale — the input that makes or breaks the cost-to-serve row ([`docs/04`](04-slides-mobile-experience.md) Slide 10).
- **Inbox/contagion sequencing:** which §06 red signals (if any) the ethics pass clears for #8, and on what timeline.
- **Two-human handoff in practice:** does the AML→credit boundary hold operationally, or do edge cases (e.g. fraud-adjacent distress) need a joint review path?
