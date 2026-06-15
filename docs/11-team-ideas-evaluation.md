# 11 — Team-Ideas Evaluation: adopt · fold · defer · drop — NetBank

> **Question the team asked:** of all the ideas raised (the docs/10 Crazy-8s shortlist **plus** the new teammate proposals), *which to adopt, which are synergistic, and how to proceed.*
> **Method:** one multi-agent workflow — **18 ideas scored independently** (implied-segment · ICP-fit 0–10 · moat-synergy 0–10 · WTP · feasibility · regulatory · redundancy · reframe), synthesised into a single decision, then **professor-red-teamed** for coherence. Every load-bearing claim below was **verified against the actual repo docs** (docs/00/01/07/09), not taken on the agents' word.
> **Sourcing discipline unchanged:** numbers are sourced or tagged `[to validate]`. The locked collection figure is **~81 days vs the 60-day legal limit (CEPYME FY2025)** per docs/09 — the inflated ">85" headline is retired.

---

## 0. TL;DR — the decision

- **Adopt as the 3 pillars (one product, one segment):** **Tax-Sweep+** (revenue), **Concurso Radar** (moat-made-cheap + acquisition wedge), **Bridge fee on a named receivable** (margin) — *Bridge presented as a **paper-traded thesis pillar**, not a live book.*
- **Hold the already-locked segment** = **VAT-registered Spanish micro-firms, solo → 2–10 employees, with late-paid B2B invoice income** (autónomos · agencies · bootstrapped *revenue* firms). The agency end **strengthens** the moat. The one line we won't cross: **silently re-segmenting to VC-backed, capital-burning startups.**
- **Fold the popular teammate ideas in where a real autónomo-native kernel exists** (7 ideas) — as *host-triggered features of the pillars,* not new product lines.
- **Defer 1** (tax-localisation = post-PMF expansion) · **Drop 7** (the VC-startup suite) — but salvage every usable kernel so no contributor loses their idea outright.

**How they fit (deck one-liner):** *Tax-Sweep+ = revenue · Bridge = margin · Concurso Radar = moat + acquisition; the closed loop binds all three — every realized payment date prices the next bridge, every distress filing sharpens the next warning.*

---

## 1. Vote map (what the team actually picked)

| Idea | Votes | Who |
|---|---|---|
| **Concurso Radar** ("Claude idea 2") | **4** | Corrado · Navid · Rui · Marti — **only consensus** |
| **Spend-benchmark / templates** (Rui idea 4) | 3 | Rui (author) · Navid · Corrado (floated) |
| **Legal/financial AI API (Harvey)** | 2 | Navid · Marti |
| Find investors through the bank | 1 (Marti's #1) | Marti |
| Revenue-per-salesperson · White-label | 1 each | Rui · Navid (Navid self-flagged "might be complicated") |
| Tax-Sweep+ · Bridge fee | championed by | Corrado / the deck |

**Signal in the votes:** the three non-Corrado teammates converged on **Concurso Radar** and otherwise gravitated to a **startup-CFO / services suite** — *not* to Tax-Sweep+ or Bridge. That divergence is the segment question in §3.

---

## 2. The verdict table (all 18 ideas)

`seg`: AUT = autónomo/agency-native · VC = assumes VC-backed startup · INFRA = infrastructure/BaaS. Scores are ICP-fit / moat-synergy (0–10).

| Idea | seg | ICP | moat | Verdict | Where it goes |
|---|---|---|---|---|---|
| **Tax-Sweep+** | AUT | 9.5 | 6 | **ADOPT — pillar #1** | revenue; scope = set-aside + readiness export (not filing) |
| **Concurso Radar** | AUT | 9 | 9 | **ADOPT — pillar #2** | one primitive, four surfaces (badge/agent/feature/paid Watchtower) |
| **Bridge fee (named receivable)** | AUT | 9 | 9 | **ADOPT — pillar #3 (paper-traded)** | margin; GRANT human-on-the-loop |
| Automate/predict tax | AUT | 9 | 6 | fold | → Tax-Sweep+ forecast engine |
| CFO-as-a-service | VC | 3 | 4 | fold | → docs/07 route-don't-own CFO panel (partner-paid) |
| Legal/financial API (Harvey) | INFRA | 3 | 2 | fold | → docs/07 legal/iguala panel, vetted-human + optional AI-assist |
| Spend-benchmark / templates | VC | 2.5 | 2 | fold | → categorization feeds Calm Score + Dry-Month Rehearsal |
| Hiring calculator (runway) | VC | 2.5 | 1.5 | fold | → "can I afford this hire?" SS-loaded check at first-hire trigger |
| FICO score for startups | VC | 2 | 4 | fold | → per-client reliability model, **pointed at payers** (green) |
| Klarna-like BNPL | VC | 2 | 1 | **drop** | lends against *spend* → induces borrowing (anti–north-star) |
| Connect startups for partnerships | VC | 2 | 1 | **drop** | matchmaker, no loop signal; concentration kernel owned by Concurso |
| Financial data lake | INFRA | 1 | 3 | fold | → purpose-bound `_asof` store in docs/05/06 (not a horizontal "lake") |
| Per-person / per-unit burn | VC | 1 | 1 | **drop** | salvage → Concentration Watch (per-**client**, not per-employee) |
| Revenue-per-salesperson | VC | 1 | 1 | **drop** | salvage → Concentration Watch |
| White-label "Amazon Basics" | INFRA | 1 | 1 | **drop** | inverts the moat (severs the customer relationship the loop needs) |
| Find investors through the bank | VC | 1 | 1 | **drop** | no autónomo kernel; nearest cousin = Runway Certificate |
| Tax localisation (per market) | INFRA | 1 | 1 | **defer** | legitimate only as post-PMF one-market-at-a-time expansion |
| One-button data-room → VCs | VC | 0.5 | 0.5 | **drop** | pure VC-startup; zero ICP/loop fit |

---

## 3. The decision that matters: **segment coherence**

**Recommendation: HOLD the already-locked shared kernel — *VAT-registered Spanish micro-firms, solo → 2–10 employees, with late-paid B2B invoice income.* Do not expand to VC-backed startups.**

Three reasons, each defensible under grilling:

1. **Evidence.** Every slide-safe number is *invoice-economy* specific: **3.43M autónomos** (Dec 2025, lamoncloa.gob.es), **~81-day collection vs 60-day legal limit** (CEPYME FY2025), the **€25–100/mo gestor** benchmark, the **Verifactu July-2027** mandate, single-client concentration. The VC-startup suite (data-room, find-investors, FICO-for-startups, per-person burn, runway, per-salesperson revenue) has **zero grounding** in that base — adopting it strands the only defended evidence and invites the −1pt-per-undefended-claim dock.
2. **Moat.** The closed loop retrains a per-client reliability model on **realized invoice-payment dates**. Firms that *issue invoices to recurring named clients* generate exactly that data; companies *burning a capital pile* do not. Every VC-suite idea scored **moat-synergy 0.5–1** — they cannot feed the one asset an interchange/engagement incumbent can't copy.
3. **WTP (our #1 weakness).** The two strongest payer/price/pain triples in the deck — **Tax-Sweep+** (€9–15/mo vs a real €25–100/mo gestor line) and the **Bridge fee** (1.5–3% at the acute moment) — are autónomo-native. The VC-suite has weak or inverted WTP (a borrower won't pay to be scored; VCs won't pay for auto-spam).

**Nuance the red-team caught (and verified):** the locked position is **not** pure solo-autónomo. docs/00 line 62 stamps the segment **Confirmed (2026-06-08): "solo freelancer up to 2–10 employees, both ends in scope"**; docs/09 pitches "autónomos, agencies and bootstrapped <10-employee companies." So the move is **hold the broad kernel**, not snap back to solo. This *helps* us: an **agency with a recurring client roster generates denser realized-payment data than a lumpy solo autónomo**, so the moat is *stronger* at the 2–10 end (docs/09 line 165 already books this as a `[to validate]` hypothesis). The only thing we exclude is the **VC-backed / capital-burning** framing — bootstrapped *revenue* firms stay in.

> **"Why not startups?" — the one-sentence answer for the oral:** *"We hold VAT-registered Spanish micro-firms with late-paid invoice income, because that's where our evidence, our closed-loop moat, and our best willingness-to-pay all live — switching to VC-backed startups would delete all three at once."*

---

## 4. Cluster synergies (build the primitive once)

- **A — Counterparty public-distress (BORME/concurso by NIF, green) → `concurso-radar`.** One public-data primitive, **four surfaces**: model feature (M1) · free client badge · standing agent (docs/08 #3) · **paid Watchtower tier** (the WTP sibling, sellable to non-borrowers + gestorías). Keep the free badge as the near-zero-CAC wedge; monetise via the Watchtower, **not** by gating the light. Keep it **event-triggered / silent-when-green** so it never becomes an engagement feed.
- **D — Tax engine + sweep (WTP anchor) → `tax-sweep` + `tax-predict`.** tax-predict is the *forecast engine* of Tax-Sweep+, not a separate idea. Scope = set-aside + one-tap modelo-303/IRPF **readiness export** + gestor handoff. **Never an automated filing** (regulated-advice perimeter). Graduate to silent autopilot to honour the calm north-star.
- **G — Named-receivable bridge (lending P&L) → `bridge-fee`.** Price on the *specific named receivable* (sizing stays non-credit, often cheaper for the customer); **GRANT stays human-on-the-loop** (Annex III §5(b) + Art.22). Pair the deck slide with the **Don't-Borrow Verdict** screen as the credibility proof.
- **Services marketplace (route-don't-own, flat-fee) → `cfo-as-service` + `legal-fin-api`.** Already specified in docs/07 (lines 59/82/90): NetBank routes to **vetted human partners** (legal/iguala, gestor, fractional CFO) on objective cash-flow signals, **flat per-lead, partner pays, customer aligned**; deliver optionally **AI-assisted behind a human** (mirrors the credit posture). **Drop the "Harvey passthrough" framing** — an un-owned model imports liability + AI-Act exposure and yields no proprietary loop signal.
- **Spend/insights (engagement-feed risk) → fold only the kernel of `spend-benchmark`.** Drop the cohort benchmark + "startup advisor templates" (a Brex/Ramp trope; a solo autónomo has ~5 cost lines, so a peer benchmark is a vanity dashboard, and a daily insights feed fights the calm objective). **Reuse only the categorization the bank already runs** to feed runway/burn into Calm Score and to power the Dry-Month Dress Rehearsal's "trim these subscriptions" nudge.
- **VC-startup suite (re-segmentation risk) → DROP framings, salvage kernels.** `fico-startups` → per-client reliability scored on **payers** (green, Annex-III-clean) — already the moat. `hiring-calculator` → first-hire **SS-loaded affordability check** at the first-payroll trigger. `per-person-burn` / `revenue-per-salesperson` → **Concentration Watch** (per-**client**, the real concentration pain). `find-investors` / `dataroom-vc` → no fit; **Runway Certificate** is the nearest in-ICP cousin.
- **Infra / BaaS (no autónomo payer) → fold/drop.** `data-lake` → fold the minimal purpose-bound `_asof` reliability store into docs/05/06 (built incrementally per surface; **never** a speculative horizontal lake — GDPR purpose-limitation). `white-label-basics` → **drop** (inverts the moat). `tax-localisation` → **defer** (post-PMF expansion playbook, not a feature).

---

## 5. How to proceed (sequenced roadmap)

**STEP 0 — Fix the live deck's internal consistency *before* any new slide.** The deck must say one thing about the segment and one thing about the number:
- **Segment:** confirm the **shared kernel** wording (solo→2–10, invoice income); make the "we exclude VC-backed startups" exclusion explicit so "why not startups?" is *answered*, not avoided.
- **Number:** docs/09 already locked **~81 days (CEPYME FY2025)** and retired ">85" (with a defense slide). **Align docs/01 line 35 (still ">85 / 85.6") and docs/10's mixed usage to the locked ~81 figure** — this is the residual −1pt risk.

**STEP 1 — Concurso Radar FIRST** (cheapest moat · the consensus · zero ethics gate). Build the public-data primitive (daily NIF/CIF match of AR clients against data.boe.es BORME/concurso/RAI), enforcing **filing-date < invoice-issue-date** to stay leakage-clean. **First test = BACKTEST:** over held-out historical receivables, what share of eventual write-offs were preceded by a public filing, and the median lead-time? Defensible if lead-time is weeks at usable precision. Slide: free red/amber/green light + the paid Watchtower as the WTP sibling.

**STEP 2 — Tax-Sweep+ WTP test** (strongest WTP · attacks the #1 weakness). Fold tax-predict in as the forecast engine. **First test = FAKE-DOOR PRICING:** show €9 / €12 / €15 tiers to a beta cohort of VAT-registered autónomos + a smoke-test charge; **target >15% choosing a paid tier `[hypothesis to validate — not yet run]`.** Slide: "VAT, handled," price anchored to the real €25–100/mo gestor line.

**STEP 3 — Bridge fee, paper-trade now / live underwriting later** (the heaviest reg surface). Build the thesis + per-invoice reliability model; **defer the loan-default model** until a real/referred book exists. **First test = PAPER-TRADE:** on historical receivables, compute the model-priced 1.5–3% fee and check it covers realized late/loss + cost-of-capital with positive margin. Slide must state out loud: **(a)** hold-license-vs-originate-and-refer is **OPEN** (docs/00:69, docs/01:73); **(b)** the "1–3% factoring vs 5.4% NPL" band is honest **only conditioned on a named SII-confirmed receivable**; **(c)** new-customer pricing **cold-starts on a cohort prior**.

**STEP 4 — Wire the fold-ins as host-triggered features, not new builds.** Each ships only when its host pillar needs it: reliability score fires **inside** Bridge; categorization feeds Calm Score later; first-hire check fires at first payroll; CFO/legal panel fires on Concurso/cash-flow signals.

---

## 6. Team-dynamics script (how to tell the team — honor every vote)

> **Do not silently bury teammate ideas; the votes will resurface in the oral.** Give each popular idea a real home where it fits, and redirect — *out loud, with a reason* — where it doesn't.

- **Concurso Radar (4 votes):** lead with full agreement — "your consensus pick is correct, it's locked as Pillar #2, and it's the most ICP-native idea in the deck." Then make the **"one primitive, four surfaces"** point so nobody re-litigates badge vs agent vs paid Watchtower as separate features.
- **Spend-benchmark (3 votes, the biggest non-Concurso bloc):** concede the useful half — *"we ARE using your categorization engine; it feeds Calm Score and the Dry-Month Rehearsal."* Redirect the rest: a solo autónomo has ~5 cost lines, so a peer benchmark is a vanity dashboard, and a daily feed fights our calm north-star. **Engine ships; cohort-benchmark + templates framing doesn't.**
- **Harvey legal/financial API (2 votes):** honor the need (autónomos do need a lawyer/gestor/CFO) — it's **already in docs/07** as the route-don't-own marketplace (flat per-lead, optionally AI-assisted behind a vetted human). Redirect only the **passthrough** framing (liability + AI-Act + no owned loop signal).
- **The startup-suite (find-investors #1, revenue-per-salesperson, data-room, FICO, CFO-with-data, per-person burn, hiring calc):** name the shared assumption *kindly and directly* — these quietly assume a VC-backed startup, a **different segment**. Then **salvage the kernels** so contributors keep a win (FICO → per-client reliability on *payers*; per-person/per-salesperson → Concentration Watch; hiring → first-hire affordability; CFO → route-don't-own panel + Calm Score "CFO brain" at gestor prices).
- **White-label (Navid, self-flagged "might be complicated"):** use his own instinct as the close — it's a separate company (BaaS licence/ops/sales) and inverts the moat.

> **Framing line:** *"We're keeping ONE product for ONE segment because that's what the rubric rewards and what re-segmenting would break. Every idea you raised is in the plan — most as a working part of a pillar, a few redirected to where they actually pay off for an autónomo. The single line we won't cross is silently switching to a startup customer, because it deletes our evidence, our moat, and our best WTP answer all at once."*

---

## 7. Professor red-team — sharpest questions + required fixes

**Coherence verdict:** the **segment and moat are coherent**; the risk is that **seven fold-ins read as a suite**. On the graded deck, show the **3 pillars as the spine** and explicitly **time-box every fold-in** as a later, host-triggered feature with a named trigger. Cut the words "data lake" from the narrative (say "a purpose-bound `_asof` store, built incrementally").

**The three sharpest questions to be ready for:**
1. *"Your deck sells 'freelancers, agencies and bootstrapped <10-employee companies' — but if your moat retrains on per-client payment dates, doesn't a solo autónomo with three lumpy invoices a year starve the model while an agency feeds it? So doesn't your own moat argue for the wider end of the segment?"* → **Yes — that's the point; the autónomo is the wedge, the 2–10 agency is the core, denser signal is our `[to validate]` hypothesis (docs/09:165).**
2. *"You wrote '>85 days' in docs/01 and '~81' in the deck — which is the locked figure, and what's the exact CEPYME source/year? And '1–3% factoring vs 5.4% NPL' are two different products — defend it as like-for-like or cut it."* → **Lock ~81 vs 60 (CEPYME FY2025); fix docs/01. Band is honest only conditioned on a named SII-confirmed receivable.**
3. *"You call seven items 'fold-ins, not new lines' — but a route-don't-own marketplace, a categorization engine, an affordability calculator and a reliability score are four build surfaces. What actually ships in the prototype vs a one-sentence promise, and which would you cut if you could only build the three pillars?"* → **Pillars ship; fold-ins are time-boxed, host-triggered. If forced to cut: keep the three pillars; everything else is later.**

**Required fixes (acceptance checklist):**
- [ ] **Segment** — make the shared-kernel wording + the VC-startup exclusion explicit on docs/09 Slide 2 and in docs/00 (it currently reads "bootstrapped startups" without the exclusion).
- [ ] **Number discipline** — align **docs/01 line 35** (and docs/10's mixed usage) to the locked **~81 days (CEPYME FY2025)**; docs/09 is already correct.
- [ ] **Bridge** — present as **thesis pillar, paper-traded**; state the hold-license-vs-refer OPEN question, the conditioned loss-band, and the cold-start prior on the slide.
- [ ] **CFO rationale** — drop the "retainer out of reach" objection (it's a strawman vs docs/07's partner-paid flat-per-lead model); keep route-don't-own, drop only the "CFO-with-data-access for a startup" framing.
- [ ] **Fold-in sprawl** — 3 pillars as the spine; every fold-in time-boxed with a named trigger; cut "data lake."
- [ ] **Moat honesty** — keep "data is commodity (Verifactu/SII); moat = closed loop + (softer) health objective ('won't, not can't')"; cut any line implying "only we see invoice data" (docs/01 flags it FALSE).
- [ ] **WTP** — either run the Tax-Sweep+ fake-door price test, or label the **>15% target as a hypothesis-to-validate**, never as a result.

---

*Provenance: workflow `netbank-team-ideas-eval` (20 agents, ~1.09M tokens, 2026-06-15); claims verified against docs/00/01/07/09. Supersedes the "final 3–5 pick pending" line in docs/10 — the pick is locked here.*
