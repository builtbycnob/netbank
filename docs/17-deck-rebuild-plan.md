# 17 — Deck Rebuild Plan *(pitch spine × rubric, gold-standard)*

> **What this is.** The concrete, approval-ready plan to rebuild the NetBank deck. Design rules = [`docs/16`](16-deck-design-principles.md). Content = [`docs/09`](09-final-deck.md) (single source). This doc fixes the **running order, rubric mapping, timing, per-slide spec, new-content list, and build changes**.
>
> **Two locked decisions (from the team, 2026-06-17):**
> 1. **Pitch spine, rubric mapped on** — the teammates' 12-section pitch structure is the *narrative order*; all 8 ESADE rubric dimensions (the grading source of truth, docs/13) must visibly land inside it.
> 2. **Labeled hypotheticals** — Traction / pipeline / funding-ask appear as *"what success would look like,"* with a persistent `ILLUSTRATIVE · not yet measured` tag (same discipline the deck already uses for the AUC numbers). Never claimed as real. No invented numbers.
>
> **Time budget:** 10–12 min target, **15 min hard cap** → an **11-slide spoken core** (~1 min each, leaving margin for the 4-way handoffs and Q&A) + an **appendix** (number-defense card, DEFENSE Q&A, the deep dimension slides, full comparison tables, conversational/sentiment detail, the stack-synthesis slide) reached only if the professor grills. This is the docs/16 "stage deck vs leave-behind" split made literal. *(16 was too many for the time; the merges below get to 11. A 12th — a dedicated Reflection slide split off from #11 — is a cheap option if the team wants to foreground rubric dimension 8 for the grade.)*

---

## The teammates' 12-section pitch spine → 11 NetBank slides

Merges from the first 16-slide draft: Netflix logic folds **into** the product/app slide (4); the before/after *turn* folds **into** the agents slide (6); Market joins Business model (8); Team + Funding + CTA + Reflection collapse into the close (11). The merged-out depth lives in the appendix.

| # | Pitch section(s) | Action-title assertion *(draft — final wording at build)* | Rubric | Primary visual primitive | Source |
|--|--|--|--|--|--|
| 1 | **Intro / WHY** | *NetBank — your bank reads your invoices, not your balance.* | frame | brand mark + inverted-flywheel glyph (win-arrow **out**) | 09·S1 |
| 2 | **Problem + Why now** | *Solvent over the year, blind week to week — paid at ~81 days vs a 60-day law, just as three clocks strike (Verifactu/SII · the AI-Act · record late payment).* | **1 · 8** | hero **~81d** vs 60-day line + "balance that lies" 3-way split + a 3-clock rail | 09·S3 + **new** |
| 3 | **Solution / VP** | *We read your invoices, forecast per-payer, and tell you when **not** to borrow.* | **1 Value prop** | three-live-truths panel + per-Payer reliability card + don't-borrow branch | 09·S5 |
| 4 | **Product — app + Netflix logic** | *Like Netflix we recommend the next **decision** — not a loan to apply for — shipped in 8 live screens.* | **6 · 8** | Netflix→NetBank split (2 rows lit) + phone still; **live demo = vertical sub-slide** | 09·S2 + S7-app |
| 5 | **Product — ontology** | *Object boundaries do regulatory and statistical work a flat table can't — the Payer is first-class.* | **4 Structure** | three-band Palantir stack + Payer ring + red dashed boundary | 09·S6 |
| 6 | **Product — Role of AI** | *We rebuild today's rigid 5-step pipeline into an agent loop — and humans touch only the credit grant.* | **5 Role of AI** | **S8→S9 auto-animate morph** + 2-band agent diagram + red grant padlock | 09·S8–S12 |
| 7 | **Product — the model (proof)** | *Our headline isn't a high AUC — it's the leakage we removed: 0.91 → 0.78.* | **6 Prototype** | **real** twin-ROC leakage-gap chart + calibration plot (AUC-accurate SVG) | 09·S7-model |
| 8 | **Market + Business model** | *3.43M autónomos via a distress-registry wedge — three pillars at a cost-to-serve below CaixaBank's 38.5%.* | **3 · 7** | TAM figure + GTM-channels rail + 3-pillar revenue diagram + unit-economics strip | 09·S4/S13/S14/S18 |
| 9 | **Competition + moat** | *Rivals copy the screens; the health objective dilutes their P&L — and only Tier 0 is a moat today.* | **2 Competitive adv** | small-multiple compare (hard-to-copy row lit) **+** 3-rung tier bar (T0/T1/T2) | 09·S15 + S16 |
| 10 | **Traction / Validation** | *No customers yet — but a falsifiable validation plan and an honest "what success looks like."* | validation | gated roadmap rail (real) **+** `ILLUSTRATIVE` pipeline/endorsers (hypothetical) | 09·S17 + docs/12 |
| 11 | **Team · Funding · CTA · reflection** | *An ESADE team plus one hire; a hypothetical raise tied to the gates; what AI changes, what stays human.* | **8 AI-banking** | team row + funding card (`ILLUSTRATIVE`) + "what surprised us \| what stays human" board + CTA | 09·S20/S22 + **new** |

**Rubric coverage (all 8 land, provable from the titles):** 1→S2,S3 · 2→S9 · 3→S8 · 4→S5 · 5→S6 · 6→S4,S7 · 7→S8 · 8→S2,S4,S11. Each spoken slide carries a mono kicker chip, e.g. `RUBRIC 6 · PROTOTYPE`.

---

## Timing budget (≈11 min, ~1 min/slide)

- **Act I — Why (slides 1–3):** ~2.5 min. The villain + why-now + the VP.
- **Act II — Product & AI (4–7):** ~4.5 min. The deepest act (this is "Data-Driven Prototyping with **AI**"); the S8→S9 morph on slide 6 is the emotional turn.
- **Act III — Business (8–9):** ~2.5 min. Market/model + competition/moat.
- **Act IV — Ask & close (10–11):** ~1.5 min. Validation honesty, then team/funding/CTA/reflection.

Appendix slides are **excluded from the running order** and from the count; each is one backup answer to a likely DEFENSE question (incl. the conversational/sentiment agents, the full comparison tables, and the stack-synthesis slide for prof gap G8).

---

## New / thin content the rebuild must author *(not just re-render)*

This is the part that is **more than re-skinning** — flag for the team:

1. **Slide 4 "Why now?"** — new slide. Sourced from the number card (Verifactu/SII; Annex III phases in by 2 Dec 2027; PMP ~81d 2025) + docs/01. Any non-sourced framing tagged `[to validate]`.
2. **Slide 11 Market / GTM-over-time** — the "marketing plan (channels over time)" the pitch asks for is only partial in docs/07/14 (Concurso + gestoría as CAC wedges). Needs a small channel-timeline; no invented CAC/conversion numbers.
3. **Slide 13 unit economics / margins / sensitivity / KPIs** — **NET-06 is not built.** Keep this slide to the *defended* figures (cost-to-serve vs CaixaBank 38.5%, factoring 1–3% vs 5.4% NPL, the 3 pillars' revenue lines, north-star = health composite); mark deeper unit-economics as `[needs NET-06]`. Do **not** fabricate margins/sensitivity tables.
4. **Slides 14–15 Traction / Funding (hypothetical)** — pipeline, endorsers, and the raise are `ILLUSTRATIVE`. The *real* evidence is the validation plan: the Orange leakage-gap proof, the WTP test (docs/12), the Concurso backtest, the paper-traded bridge. Funding ask is a hypothetical figure tied to reaching the roadmap gates.

---

## Per-slide visual notes (the hero diagrams)

Reuse one inline-SVG symbol set (docs/16 component vocabulary). Slide numbers below are the **new running order**; `09·Sn` = the docs/09 content source. Highlights beyond the table above:

- **Slide 4 — Netflix + app** (09·S2 + S7-app) — greyed NETFLIX column / mint NETBANK column, 5 aligned rows, fragment-revealed; **mint only on rows 1 (recommendation-not-application) and 5 (the loop)**; a phone still beside it; the 5-col table → notes; live demo = vertical sub-slide.
- **Slide 5 — ontology** (09·S6) — OBJECTS / LOGIC / ACTIONS bands; Payer chip mint-ringed as join key; one **red dashed** line slicing all three = "object boundary = leakage plane = legal regime"; fragment in the `_asof_issuance` tag + struck-through `paid_date = LABEL, never a feature`; cross-customer bureau shown **roadmap-only**.
- **Slide 6 — the turn + agents** (09·S8→S9 + S10–S12) — adjacent `data-auto-animate` sections, matching `data-id` on the 5 step nodes; surviving nodes glide into the agent loop, manual steps fade, the **mint return arrow** ("every realized payment date retrains the model") is the final fragment (the deck's sparkline turn); the 2-band agent diagram (CX surface / underwriting) with the red grant padlock assembles via fragments; conversational/sentiment detail → notes/appendix.
- **Slide 7 — the model** (09·S7) — Chart A twin-ROC: naive 0.91 dim/dashed vs grouped 0.78 mint/solid, **amber-shaded wedge** in-frame "= the leakage we removed · illustrative · synthetic"; Chart B calibration vs y=x "this is what prices the bridge." Synthetic JSON **must integrate to 0.91 / 0.78** (build-checked); visually-hidden data table for a11y + "show me your data."
- **Slide 9 — competition + moat** (09·S15 + S16) — small-multiple compare board (the hard-to-copy row lit mint) leads into the concede→pivot fragment (3 grey commodity chips collapse into one mint "retained account, net of tax pot, gated on Concurso" node) + **3-rung tier bar** (T0 solid-mint *demonstrated* / T1 grey-dashed *compounding, not yet present · ~0 today* / T2 hatched *softer · won't-not-can't*); red footnote "data is NOT the moat (Verifactu/SII); cross-customer bureau = roadmap-only, two gates."
- **Slide 10 — roadmap** (09·S17) — gated rail, 5 stations (Concurso → Tax-Sweep+ → Paper-trade → Live+Servicing → Bureau), each gate a **red padlock stamped with its falsifiable test**; tier ribbon stays grey for T1 until station 3; servicing node fans `re-date · top-up · restructure` over struck-through `collections/dunning`.

The remaining slides (1 cover, 2 problem+why-now, 3 solution/VP, 8 market+business-model, 11 close) each get: action-title + one primitive (hero-number / 3-clock rail / three-truths panel / pillar-diagram + GTM rail / two-column board) + ≤3 labels; prose → notes.

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

- [ ] 11 spoken slides (or 12 with a dedicated Reflection), pitch-spine order; all 8 rubric dimensions provable from the titles + the kicker map; appendix excluded from the count.
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
