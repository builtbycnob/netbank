# 13 — Instructor Deck: extraction + alignment/gap analysis

> **Source:** the instructor's own **Sessions 7 & 8 — "Designing the Netflix Bank"** deck (39 slides, *Data Driven AI prototyping*, 8 & 15 June, 11:30–13:30, Room 2D02). This is the **grading source-of-truth** — what the professor expects, the sprint spine, the canonical artifacts handed to us, and the final deliverable spec. Every gap below was **verified by grep against docs/00–12**.

## 0. The deliverable spec (don't miss these)
- **Final output = "prepare 20–25 slides"** (Slide 39). **We are at 11 (docs/09) — under target.** See the slide map in §5.
- **Final reflection** required (Slide 39): *what surprised you · what role did AI play · what remained uniquely human · what would you build next.*
- **Inspirations the prof uses throughout:** **Nubank · ImaginBank · Netflix.** The business-model slide (36) explicitly asks to **compare Netflix Bank vs ImaginBank vs Nubank**.

## 1. The sprint spine (Slides 2 & 18) — and where our docs land
The professor's 7-stage spine *is* the expected deck structure:

| # | Prof's stage | Our doc | Status |
|---|---|---|---|
| 1 | **Customer** — who, goals, financial problems | docs/00, 01 | ✅ strong (autónomo/agency, evidence-backed) |
| 2 | **App Design (Ontology)** — Mobile Experience / HMW / Marvel | docs/02, 03, 04 + mockups | ✅ strong (8 live screens + ontology) |
| 3 | **Prediction** — Predictive AI, Orange, confusion matrix | docs/05 + S5 | ✅ strong (leakage gap + calibration + cost-sensitive confusion matrix) |
| 4 | **Process** — Customer journey | docs/08 | ⚠️ have the *agentic* journey, but **not the before/after vs the prof's rigid 5-step** (§3.4) |
| 5 | **Agent** — Agentic AI | docs/08 (9 agents) | ⚠️ rich, but **missing the Conversational + Sentiment agents the prof templates** + no per-agent business value (§3.2/3.3) |
| 6 | **Operating Model & Scale** | docs/09 S9 | ✅ covered; ⚠️ reframe to the prof's **100 → 10k → 10M / disappears-changes-appears** lens (§3.6) |
| 7 | **Business Model & Value Prop + demo** | docs/09 S7/S8, mockups | ✅ strong; ⚠️ add the **explicit ImaginBank/Nubank comparison** (§3.5) |

## 2. Canonical artifacts the prof handed us (must appear or be answerable cold)

**A. "Netflix Logic Applied to Banking" (Slide 20)** — the namesake framing. Prof's table + our NetBank-ised version to put on a slide:

| Netflix | Prof's "Netflix Bank" | **Our NetBank version** |
|---|---|---|
| Movies | Financial products | Financial **actions** — bridge a named invoice · tax-sweep · re-date · "don't borrow" |
| Recommendations | Decisions / next-best offer | **Next-best decision** — incl. the honest *don't-borrow* verdict |
| Viewer profile | Customer profile | **Per-customer + per-Payer reliability** profile |
| AI ranking | AI decisions | **Calibrated** risk/affordability scoring (sizes & warns; human grants) |
| Continuous learning | Continuous financial advice | **The closed loop** — every realized payment date retrains the model |

**B. The 5 canonical agents (Slide 30)** — the prof's roster + the **blank "Business Value?" column we must fill**, mapped to our 9 agents:

| Prof's agent | Maps to our docs/08 | **Business value (fill this in)** |
|---|---|---|
| **Conversational** (UI & context capture) | ❌ **not in our 9 — ADD** | Fewer forms → higher completion/activation; captures context (not just data) → richer ontology |
| **Sentiment / Friction** (anxiety, abandonment) | ❌ **not in our 9 — ADD** | Lower drop-off; "reduce financial anxiety" HMW made real; earlier, calmer escalation |
| **Predictive AI** (risk & affordability) | ✅ #3 Reliability/Signals + #4 Capacity | Prices each bridge accurately → losses in the 1–3% band; "No → not yet / different path" |
| **Orchestration** (control & next-best-action) | ✅ routing across the 9 | Cost-to-serve down (no rigid workflow); right action at the right moment |
| **Escalation (Human-in-the-loop)** | ✅ #5 Credit-Decision gate | Annex III §5(b)/Art. 22 compliance *as* the design; humans only on the grant |

> Our extra agents (#2 contagion, #8 Servicing/"collections disappears", #9 Repayment/Limit) show depth **beyond** the prof's 5 — keep them, but make sure the **5 canonical roles are visibly present** and each has a one-line business value.

**C. The rigid 5-step journey the prof gives as the foil (Slide 27):** Application (long static form) → Eligibility (hard rules, binary) → Risk Scoring (one-shot, no explanation) → Decision (approve/reject, opaque) → Outcome (contract / drop-off). **We should show this as the BEFORE and our agentic loop as the AFTER, step by step.**

**D. Expected ontology objects (Slide 22):** Customer · Loan · Income · Transaction · Goal · Decision · Risk. **Our 7 objects** (docs/09 S4): Customer · Account/Transaction · Invoice/Receivable · **Payer** · Goal · Product/Loan · Decision/Agent. Coverage map: Customer✓ · Loan=Product/Loan✓ · Income≈Invoice/Receivable✓ · Transaction✓ · Goal✓ · Decision✓ · **Risk = in the Logic layer (M1–M3), not a named object** — say so · **Payer = our addition** (the moat join key). We over-deliver; just name-map "Risk" and "Income" when asked.

**E. HMW examples the prof expects (Slide 24)** — we already match: *reduce financial anxiety · better decisions · recommend-not-ask* (customer) and *reduce risk · scale without hiring · learn from every interaction · network effects · leverage an ecosystem* (bank). ✅ align to docs/02.

**F. Personas the prof lists (Slide 21):** Erasmus student · Junior consultant · **Freelancer** · Digital nomad · **Startup founder**. Note the skew to **young/individual** — including **"startup founder," which docs/11 deliberately excludes** (no invoice-loop). **Freelancer is on the list**, so our autónomo/agency choice is defensible; be ready to say *why freelancer over the consumer personas* (real revenue + invoice loop + WTP) and *why not the startup founder* (burns capital, no realized-payment signal).

**G. The synthesis "stack" (Slide 38):** Ontology (base) → Agentic loan process on Clients/Products → Predictive AI/Classification (Risk/Fraud) → Value Prop/Business/Operating Model (network · automation · learning · APIs) → **SuperApp**. We have every layer — worth **one synthesis-stack slide** that mirrors this exactly.

## 3. Prioritized gaps to close (verified)

> ✅ **STATUS (2026-06-15): all 8 gaps CLOSED.** docs/09 expanded **11 → 21 slides** (within the 20–25 target) — new slides 2 (Netflix-logic, G1), 4 (persona), 8 (rigid-journey, G4), 10 (agent system + business value, G2/G3), 11 (conversational, G2), 12 (sentiment, G2), 13 (Crazy-8s→pillars), 15 (ImaginBank/Nubank, G5), 18 (stack, G8), 21 (reflection, G7). Each was drafted + professor-red-teamed (workflow `netbank-deck-gapclose`).

| # | Gap | Why it matters | Fix → where |
|---|---|---|---|
| **G1** | **No Netflix-analogy slide** (grep: 0 hits for netflix/next-best/recommendation in docs/09) | It's the assignment's namesake framing; the prof templates it | Add a slide using §2.A → docs/09 |
| **G2** | **No Conversational + Sentiment/Friction agents** (grep: 0 hits) | Prof templates them (Slides 31/33); they answer the anxiety HMW | Add 2 agents to docs/08 + the deck agent slide |
| **G3** | **No per-agent business value** (grep: 0 hits for "business value" in docs/08) | Prof leaves that column blank to fill | Fill per §2.B → docs/08 |
| **G4** | **No before/after vs the rigid 5-step journey** | Prof gives the foil (Slide 27) for exactly this contrast | Add a before/after slide → docs/08/09 |
| **G5** | **ImaginBank never named; no 3-way comparison** | Prof's 2nd inspiration + Slide 36 asks for it | Add Netflix-Bank vs ImaginBank vs Nubank → docs/09 S7/business model |
| **G6** | **11 slides vs "20–25" deliverable** | Explicit requirement (Slide 39) | Expand per the §5 slide map |
| **G7** | **Reflection partial** (have "what we'd test"; missing surprised / uniquely-human) | Required (Slide 39) | Extend docs/09 S11 |
| **G8** | **No single stack-synthesis slide** | Prof's closing synthesis (Slide 38) | Add one stack slide |

*Note: G1, G2, G4, G5, G8 are exactly the new slides that also close G6 (the slide-count gap) — they are the same work.*

## 4. What we're already strong on (don't re-do)
Ontology depth (Palantir 3-layer, object boundaries = leakage/legal planes) · the Orange leakage-gap + calibration + **cost-sensitive confusion matrix** (the prof explicitly asks for the confusion matrix) · Crazy-8s → **pick 3** (our 3 pillars exactly match Slide 28's "pick 3 ideas") · the moat as closed-loop ("won't, not can't"; data is commodity) · human-on-the-loop / Annex III framing · 8 live mockups. These are competitive strengths — lead with them.

## 5. Proposed 20–25 slide map (hits the deliverable count)
1. Title · 2. Netflix-logic→banking analogy **(G1)** · 3. The customer & the wound · 4. Why this segment, not the consumer/startup personas **(persona defense)** · 5. Value proposition ("reads your invoices") · 6. The mobile app / 8 live screens · 7. HMW → decisions-not-screens · 8. Ontology (7 objects, Payer as join key) · 9. The rigid loan journey today **(G4 before)** · 10. The agentic loan journey **(G4 after)** · 11. The 5 agents + business value **(G2/G3)** · 12. Conversational agent · 13. Sentiment/Friction agent · 14. Predictive AI (Orange: leakage gap + confusion matrix) · 15. Calibration prices the bridge · 16. Crazy-8s → the 3 picked pillars · 17. Pillar 1 Tax-Sweep+ (WTP) · 18. Pillar 2 Concurso Radar (moat) · 19. Pillar 3 Bridge fee (paper-traded) · 20. Business model + **Netflix-Bank vs ImaginBank vs Nubank (G5)** · 21. Operating model & scale (100→10k→10M; disappears/changes/appears) · 22. Why hard to copy (closed loop) · 23. The stack synthesis **(G8)** · 24. What AI changes (3 things) · 25. Reflection **(G7)** + what we'd build next.

---

*Provenance: instructor deck (39 slides, Sessions 7–8) extracted 2026-06-15; gaps verified by grep against docs/00–12. Use §3 as the work queue and §5 as the deck target.*
