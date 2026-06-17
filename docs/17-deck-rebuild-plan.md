# 17 — Deck Rebuild Plan *(pitch spine × rubric, gold-standard)*

> **What this is.** The concrete, approval-ready plan to rebuild the NetBank deck. Design rules = [`docs/16`](16-deck-design-principles.md). Content = [`docs/09`](09-final-deck.md) (single source). This doc fixes the **running order, rubric mapping, timing, per-slide spec, new-content list, and build changes**.
>
> **Two locked decisions (from the team, 2026-06-17):**
> 1. **Pitch spine, rubric mapped on** — the teammates' 12-section pitch structure is the *narrative order*; all 8 ESADE rubric dimensions (the grading source of truth, docs/13) must visibly land inside it.
> 2. **Labeled hypotheticals** — Traction / pipeline / funding-ask appear as *"what success would look like,"* with a persistent `ILLUSTRATIVE · not yet measured` tag (same discipline the deck already uses for the AUC numbers). Never claimed as real. No invented numbers.
>
> **Time budget:** 10–12 min target, **15 min hard cap** → a **16-slide spoken core** (~40s each) + an **appendix** (number-defense card, DEFENSE Q&A, the deep dimension slides, full comparison tables, conversational/sentiment detail) reached only if the professor grills. This is the docs/16 "stage deck vs leave-behind" split made literal.

---

## The teammates' 12-section pitch spine → 16 NetBank slides

| # | Pitch section | Action-title assertion *(draft — final wording at build)* | Rubric | Primary visual primitive | Source |
|--|--|--|--|--|--|
| 1 | **Intro / WHY** | *NetBank — your bank reads your invoices, not your balance.* | frame | brand mark + inverted-flywheel glyph (win-arrow **out**) | 09·S1 |
| 2 | **Problem** | *Spain's micro-firms are solvent over the year but blind week to week — paid at ~81 days against a 60-day law.* | **1 Value prop** | hero number (**~81d** vs 60-day line) + the "balance that lies" 3-way split; villain named | 09·S3 + S1 |
| 3 | **Solution / VP** | *We read your invoices, forecast per-payer, and tell you when **not** to borrow.* | **1 Value prop** | three-live-truths panel + per-Payer reliability card + don't-borrow branch | 09·S5 |
| 4 | **Why now?** ⟂*new* | *Three clocks struck at once: invoice data went live (Verifactu/SII), the AI-Act drew the credit line, late payment hit a record.* | **8 AI-banking** | three-clock / timeline rail | **new** (docs/01 + number card) |
| 5 | **Product — the app** | *The whole thesis ships in eight live screens — a Command Center, not a balance.* | **6 Prototype** | phone still (Command Center) + AI-mode legend; **live demo = vertical sub-slide** | 09·S7 (app half) |
| 6 | **Product — Netflix logic** | *Like Netflix, we recommend the next **decision** — not a catalog of loans to apply for.* | **8 AI-banking** | Netflix→NetBank split board, mint-light **only** the 2 load-bearing rows | 09·S2 |
| 7 | **Product — ontology** | *Object boundaries do regulatory and statistical work a flat table can't — the Payer is first-class.* | **4 Structure** | three-band Palantir stack + Payer ring + red dashed boundary | 09·S6 |
| 8 | **Product — Role of AI (the turn)** | *We rebuild today's rigid 5-step pipeline and add the one return arrow it can't have.* | **5 Role of AI** | **S8→S9 auto-animate morph** (grey boxes → mint loop + red grant padlock + mint retrain-arrow) | 09·S8 + S9 |
| 9 | **Product — the agents** | *Five agents earn their seat in the P&L or the law — and humans touch only the credit grant.* | **5 Role of AI** | 2-band node diagram (CX surface / underwriting) + red padlock; CX agents as fragments | 09·S10–S12 |
| 10 | **Product — the model (proof)** | *Our headline isn't a high AUC — it's the leakage we removed: 0.91 → 0.78.* | **6 Prototype** | **real** twin-ROC leakage-gap chart + calibration plot (AUC-accurate SVG) | 09·S7 (model half) |
| 11 | **Market** | *3.43M autónomos, entered through the cheapest wedge — distress-registry and gestor channels.* | **7 Scale** | TAM figure + a GTM-channels-over-time rail | 09·S4/S18 + docs/07/14 |
| 12 | **Competition + moat** | *Rivals can copy the screens; copying the health objective dilutes their P&L — and only Tier 0 is a moat today.* | **2 Competitive adv** | small-multiple compare (hard-to-copy row lit) **+** 3-rung tier bar (T0/T1/T2) | 09·S15 + S16 |
| 13 | **Business model + customer** | *Three pillars, one retained account; we win at a cost-to-serve below CaixaBank's 38.5%.* | **3 Bus model · 7 Scale** | 3-pillar revenue diagram + unit-economics strip + risks/mitigation chips | 09·S13/S14 + S18 |
| 14 | **Traction / Validation** | *No customers yet — but a falsifiable validation plan and an honest "what success looks like."* | validation | gated roadmap rail (real) **+** `ILLUSTRATIVE` pipeline/endorsers (hypothetical) | 09·S17 + docs/12 |
| 15 | **Team + Funding** | *An ESADE team plus the one hire we'd add (credit/risk); a hypothetical raise tied to the gates.* | pitch | team row + funding-ask card stamped `ILLUSTRATIVE` against the roadmap gates | **new** (cohort + docs/14) |
| 16 | **Call to action + reflection** | *What AI changes here, what stays human — and the one thing we'd build next.* | **8 AI-banking** | "what surprised us \| what stays human" two-column board + CTA | 09·S20 + S22 |

**Rubric coverage (all 8 land, provable from the titles):** 1→S2,S3 · 2→S12 · 3→S13 · 4→S7 · 5→S8,S9 · 6→S5,S10 · 7→S11,S13 · 8→S4,S6,S16. Each spoken slide carries a mono kicker chip, e.g. `RUBRIC 6 · PROTOTYPE`.

---

## Timing budget (≈11 min)

- **Act I — Why (slides 1–4):** ~2.5 min. The villain + the VP + why-now.
- **Act II — Product & AI (5–10):** ~4.5 min. The deepest act (this is "Data-Driven Prototyping with **AI**"); the S8→S9 turn is the emotional beat.
- **Act III — Business (11–13):** ~2.5 min. Market, competition/moat, model.
- **Act IV — Ask & close (14–16):** ~1.5 min. Validation honesty, team/funding (fast), CTA + reflection.

Appendix slides are **excluded from the running order** and from the count; each is one backup answer to a likely DEFENSE question.

---

## New / thin content the rebuild must author *(not just re-render)*

This is the part that is **more than re-skinning** — flag for the team:

1. **Slide 4 "Why now?"** — new slide. Sourced from the number card (Verifactu/SII; Annex III phases in by 2 Dec 2027; PMP ~81d 2025) + docs/01. Any non-sourced framing tagged `[to validate]`.
2. **Slide 11 Market / GTM-over-time** — the "marketing plan (channels over time)" the pitch asks for is only partial in docs/07/14 (Concurso + gestoría as CAC wedges). Needs a small channel-timeline; no invented CAC/conversion numbers.
3. **Slide 13 unit economics / margins / sensitivity / KPIs** — **NET-06 is not built.** Keep this slide to the *defended* figures (cost-to-serve vs CaixaBank 38.5%, factoring 1–3% vs 5.4% NPL, the 3 pillars' revenue lines, north-star = health composite); mark deeper unit-economics as `[needs NET-06]`. Do **not** fabricate margins/sensitivity tables.
4. **Slides 14–15 Traction / Funding (hypothetical)** — pipeline, endorsers, and the raise are `ILLUSTRATIVE`. The *real* evidence is the validation plan: the Orange leakage-gap proof, the WTP test (docs/12), the Concurso backtest, the paper-traded bridge. Funding ask is a hypothetical figure tied to reaching the roadmap gates.

---

## Per-slide visual notes (the hero diagrams)

Reuse one inline-SVG symbol set (docs/16 component vocabulary). Highlights beyond the table above:

- **S2 Netflix** — greyed NETFLIX column / mint NETBANK column, 5 aligned rows, fragment-revealed; **mint only on rows 1 (recommendation-not-application) and 5 (the loop)**; the 5-col table → notes.
- **S6 ontology** — OBJECTS / LOGIC / ACTIONS bands; Payer chip mint-ringed as join key; one **red dashed** line slicing all three = "object boundary = leakage plane = legal regime"; fragment in the `_asof_issuance` tag + struck-through `paid_date = LABEL, never a feature`; cross-customer bureau shown **roadmap-only**.
- **S8→S9 turn** — adjacent `data-auto-animate` sections, matching `data-id` on the 5 step nodes; surviving nodes glide into the loop, manual steps fade, the **mint return arrow** ("every realized payment date retrains the model") is the final fragment. The deck's sparkline turn.
- **S10 model** — Chart A twin-ROC: naive 0.91 dim/dashed vs grouped 0.78 mint/solid, **amber-shaded wedge** in-frame "= the leakage we removed · illustrative · synthetic"; Chart B calibration vs y=x "this is what prices the bridge." Synthetic JSON **must integrate to 0.91 / 0.78** (build-checked); visually-hidden data table for a11y + "show me your data."
- **S12 moat** — concede→pivot fragment (3 grey commodity chips collapse into one mint "retained account, net of tax pot, gated on Concurso" node) + **3-rung tier bar** (T0 solid-mint *demonstrated* / T1 grey-dashed *compounding, not yet present · ~0 today* / T2 hatched *softer · won't-not-can't*); red footnote "data is NOT the moat (Verifactu/SII); cross-customer bureau = roadmap-only, two gates."
- **S14 roadmap** — gated rail, 5 stations (Concurso → Tax-Sweep+ → Paper-trade → Live+Servicing → Bureau), each gate a **red padlock stamped with its falsifiable test**; tier ribbon stays grey for T1 until station 3; servicing node fans `re-date · top-up · restructure` over struck-through `collections/dunning`.

The remaining slides (S3, S4, S5, S7-app, S9-agents, S11, S13, S15, S16) each get: action-title + one primitive (hero-number / split-panel / channel-rail / pillar-diagram / segment-matrix / two-column board) + ≤3 labels; prose → notes.

---

## Build changes (`build_deck.py` · `theme.css` · authoring · assets)

In dependency order. None of it rewrites locked content — it adds channels and changes rendering.

**1. Authoring convention (docs/09, non-destructive):**
- Each `## Slide` block gains an **`ASSERTION:`** line (the on-slide sentence headline, 8–14 words) and a **`{DIAGRAM: name}`** or **`{CHART: name}`** token naming its artifact; the `## Slide N — …` heading is rewritten from a topic label to an action title.
- Add a preamble **`Presentation order:`** manifest listing the 16 spoken slides in pitch order (with the S8+S9 and S10–S12 merges noted) + the rubric kicker per slide. Slides not in the manifest render as **appendix/backup** (excluded from the count).
- Add the 4 new/thin blocks (Why-now, GTM, Funding, and the reflection consolidation).
- Restructure each `<aside>` source into 3 labelled blocks: **NARRATION / NUMBERS+SOURCES / DEFENSE**.

**2. `build_deck.py`:**
- Parser: extract `ASSERTION`, `{DIAGRAM/CHART}`, `RUBRIC`, and the presentation-order manifest (same way `[VISUAL:]`/`SPEAKER NOTES` are pulled today).
- Render: emit **only** the assertion headline + the inlined diagram/chart partial + ≤3 labels into the `<section>`; route the entire prose `body` **and every table** into `notes_block()`. **Delete** `render_body()`'s on-slide `<ul>/<li>` path and `visual_details()`'s `<details>`.
- **Delete `fit()` + its 3 `Reveal.on` handlers (238–261).** Set `Reveal.initialize` to `minScale:1, maxScale:1, center:false` at 1280×840; register auto-animate defaults (`autoAnimateDuration:0.7`); keep `transition:'fade'` for act breaks only.
- Add a **diagram expander**: inlines `design/slides/diagrams/<name>.svg` (theme-token colours), auto-wraps `role="img"` + `<title>`=assertion + `<desc>`=spoken sentence + `aria-labelledby`, plus a visually-hidden data `<table>` for charts.
- Add **build-time glance gates** (docs/16): fail the build if a `<section>` contains `<li>`/`<table>`, headline ∉ 8–14 words, >12 words non-headline text, or ≠1 mint focal element.
- Add a **two-PDF build flag**: `present` (clean) and `leavebehind` (`?print-pdf` + `showNotes:'separate-page'`, `pdfSeparateFragments:false`, `pdfMaxPagesPerSlide:1`).
- **Replace the Google Fonts `<link>`** (line 221) with self-hosted `@font-face` woff2.

**3. `theme.css`:**
- Add the modular type-scale tokens (`--t-title` 60 / `--t-lead` 28 / `--t-body` 21 / `--t-cap` 13 / `--t-mono` 12, ~1.3 ratio); refactor `h2` 32px → `var(--t-title)` tracking −0.035em; bump section padding to ~72/88px.
- Add the reusable SVG `<defs>` symbol vocabulary + the tier-bar / small-multiple / hero-number / gated-rail / channel-rail component classes; `shape-rendering:geometricPrecision` + `text-rendering:optimizeLegibility` on `.diagram svg`; `tnum` on all numbers.
- Apply the **contrast rule**: `text-3` large-display-only (≥24px); ≤16px → `text-2` minimum.

**4. Assets / feasibility fixes (from the adversarial review):**
- **Vendor `css/print/pdf.css`** and inject it on `?print-pdf` — currently absent; the leave-behind PDF breaks offline without it.
- **RevealHighlight is not vendored** — **drop** the code-walk feature (no code slides in this spine) rather than add a dependency.
- **`r-fit-text` ceiling** ~0.8×canvas — billboard only short tokens (`~81 days`, `38.5%`); long numbers (`3,425,767`) auto-size down, so present them as "3.43M" at normal scale.
- **Live prototype = vertical sub-slide of S5** (`data-background-iframe`, `data-preload`), not a 17th horizontal slide.
- **No charting lib** — inline SVG only.
- **Self-hosted fonts**: vendor woff2 subsets of Bricolage Grotesque (400/700), Geist (400–700), Geist Mono (400/500 + `tnum`).

---

## Acceptance gates (Task B "done")

- [ ] 16 spoken slides, pitch-spine order; all 8 rubric dimensions provable from the titles + the kicker map; appendix excluded from the count.
- [ ] Build-time glance gates pass (no `<li>`/`<table>` on stage; headline 8–14 words; ≤3 labels; one mint focal element).
- [ ] S10 charts are real SVG and integrate to AUC 0.91 / 0.78 (checked in build).
- [ ] Traction/Funding visibly `ILLUSTRATIVE`; numbers consistent (gestor €60–100, ~81d / no ">85", €9/12/15 ≠ €9/19/39); differentiation = system + 3 tiers; bureau roadmap-only.
- [ ] Two artifacts build **offline** (stage deck + leave-behind PDF); fonts self-hosted; pdf.css vendored.
- [ ] Verified via `http.server :8011` + Playwright (`file://` blocked); screenshots of the hero slides.
- [ ] docs/09 grep-clean if edited (artifacts = 0); docs/15 NET-05 updated; committed + pushed.

---

## Out of scope / open for the team

- The dark instrument-panel aesthetic is **kept** (tokens locked). The pillar pick (docs/11), the segment, and the 3-tier moat framing are **not** reopened.
- `.pptx` export (NET-05 DoD) — the leave-behind PDF covers the "editable handout" need; a true `.pptx` is a separate optional step (no clean reveal.js→pptx path that preserves the SVG system). **Decide with the team.**
- Unit-economics depth (slide 13) depends on **NET-06**; kept to defended figures until then.
