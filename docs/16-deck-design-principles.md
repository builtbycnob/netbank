# 16 — Gold-Standard Deck Design Principles

> **What this is.** The design contract for rebuilding the NetBank presentation deck from a faithful-but-text-dense *script renderer* into a *stage deck*. These principles are **structure-agnostic** — they hold whatever the running order. The concrete rebuild (new pitch-spine running order, rubric map, per-slide spec, build changes) lives in [`docs/17-deck-rebuild-plan.md`](17-deck-rebuild-plan.md).
>
> **How it was produced.** A research workflow (`netbank-deck-design-research`): 7 parallel agents (one per design dimension) → synthesis → an adversarial critic that fact-checked the synthesis against the real repo. Every principle below carries its mechanism and a named source; the critic's corrections (table inventory, feasibility errors, citation fixes, contrast) are folded in. Sources are listed at the foot.
>
> **The one-line diagnosis of deck v1.** `build_deck.py` turns every docs/09 `- ` bullet into a 21px full-sentence `<li>` (max-width 60ch) and every comparison into a 5-column 15px table, then a JS `fit()` hack shrinks the densest slides to ~0.5×. It is a 250–400-word *document* projected on a wall — a teleprompter script the audience reads while the presenter talks. The fix is not "fewer words"; it is a different **kind** of slide.

---

## North star

A NetBank oral-defense deck is **gold-standard** when:

1. **Every content slide = one Minto action-title assertion (8–14 words, single fixed size, ≤2 lines) + exactly one custom dark-theme visual** built from a shared inline-SVG symbol vocabulary, with ≤3 short on-visual labels. **Zero prose `<li>`. Zero on-stage tables.**
2. **Numbers that *are* the evidence stay on the visual** (the 0.91→0.78 leakage wedge, the "ceiling, not peer" benchmark tags, the ~81-day villain), labelled, with provenance *spoken*. All narration and secondary numbers and the DEFENSE Q&A live in a structured `<aside class="notes">`.
3. **Reading the action titles alone reproduces the whole argument** *and* a checked-in map proves each of the 8 rubric dimensions is landed by a named headline.
4. **One source builds two artifacts offline** — a sparse stage deck and a one-notes-page-per-slide leave-behind PDF — with the `fit()` scale hack deleted, so overflow is resolved by **moving prose to notes, never by shrinking type**.
5. **Every slide passes build-time-checkable glance rules** (below), not a subjective look-away test.

So the room watches defensible evidence the presenter narrates, and the deck survives a **−1-per-undefended-claim** grilling.

---

## The principles

### P1 — Assertion-Evidence is the authoring contract
Every content slide is a **full-sentence headline stating the slide's single claim** + a **visual evidence object** (chart/diagram/labelled image) — *not* a topic label + bullets. If the headline runs past two lines, **edit the words; never shrink the font.**
*Why:* controlled studies show A-E slides beat topic+bullet on comprehension and one-week recall, specifically for **complex, multi-step** material — exactly NetBank's causal/comparative content (leakage planes, the loop, the tiers). The sentence headline is a "safety rope" that re-anchors a distracted grader in one glance. This deletes **no** locked content — the prose just moves to notes.
*Source:* Alley, Schreiber & Muffo 2005 (the significance result); Garner & Alley 2013 (the n≈110 cognitive-load study); assertion-evidence.com / Penn State AE instruction set.

### P2 — Action titles carry the so-what (Minto)
Rewrite every title from a **topic** ("The ontology that makes the AI possible") into a **conclusion** ("Object boundaries do regulatory and statistical work a flat table can't"). **Headline test:** reading only the titles in order must reproduce the argument *and* visibly land each of the 8 rubric dimensions.
*Why:* the title is the most-read real estate and the first thing a time-boxed grader parses; topic labels forfeit it and hide undefended claims in body text. A slide you cannot title in one clean claim is doing too much and must be split.
*Source:* Minto, *The Pyramid Principle*; McKinsey/BCG action-title convention.

### P3 — Slides are glance media, not documents
Each slide must be grokkable in ~3s. Duarte's thresholds: **>50 on-slide words = a teleprompter; >75 = a document.** Deck v1's dense slides carry 250–400 words.
*Why:* working memory cannot read dense text and listen at once; the instant a slide demands decoding, the audience stops listening and the presenter loses narrative control.
*Source:* Duarte, *slide:ology* (glance test, 50/75-word thresholds); Medina, *Brain Rules*.

### P4 — Reasoning is diagrams, not bullet lists
A bulleted list can encode only sequence, priority, or set-membership — it **cannot show causal, comparative, or conditional relationships**, which is most of NetBank's argument. Render those as nodes+arrows, before/after rails, tier bars, small multiples.
*Why:* Tufte — "as analysis becomes more causal, multivariate, comparative… the more damaging the bullet list becomes." Bullets flatten logical structure (the named failure mode in the Columbia accident report).
*Source:* Tufte, *The Cognitive Style of PowerPoint*; *The Visual Display of Quantitative Information* (small multiples).

### P5 — Split one source into two channels
On-slide layer = assertion + visual + ≤3 labels. Spoken layer = the full prose body, every sourced number, and the DEFENSE Q&A, routed to `<aside class="notes">`. Ship a clean **stage deck** and a **leave-behind PDF** from the one source.
*Why:* Duarte's "slideument" — a slide that must also be read serves neither purpose. Mayer's redundancy effect: identical spoken+printed full sentences is measurably **worse** than narration alone. (Boundary condition — see P7 — short labels *at* the diagram part *help*.)
*Source:* Duarte, *Slidedocs*; Mayer, *Multimedia Learning* / Kalyuga redundancy effect; reveal.js Speaker View + PDF export.

### P6 — Delete the scale hack; author to the fixed canvas
Remove `fit()` (build_deck.py 238–261) and its three `Reveal.on` handlers. Set `minScale:1, maxScale:1, center:false` on the 1280×840 canvas. Treat overflow as a **content-editing problem** — and since content is locked, "edit down" means **move more prose to `<aside>`**, never shrink.
*Why:* uniform 0.5× scaling shrinks signal and noise equally → sub-10px projected type the back row can't read, and inconsistent cross-slide sizes (the #1 cheapness tell). It hides overstuffing instead of fixing it. reveal.js `r-stretch` / `r-fit-text` size **one** evidence object to the canvas instead.
*Source:* Tufte (low-resolution / Columbia board); reveal.js Layout docs.

### P7 — One inline-SVG symbol system; no Mermaid, no raster, no charting lib
Build a reusable `<defs>` symbol vocabulary wired to `theme.css` tokens and render every structural slide from it. **Never** ship live Mermaid, raster PNG charts, or tool screenshots as primary evidence.
*Why:* inline SVG is vector (crisp fullscreen, ~0KB dependency), its fills/strokes are CSS variables (one token re-themes the deck), and each node is a DOM element reveal.js fragments/auto-animate can drive. Mermaid bakes its palette in and re-adds a runtime dependency the vendored-offline deck exists to avoid; a bitmap chart blurs and invites "is this *your* data?" — fatal in a grilling. One symbol set turns nine figures into one visual language, not clip-art. **Short labels placed at the relevant diagram part improve retention** (Mayer & Johnson) — this is what licenses the ≤3 on-visual labels.
*Source:* CSS-Tricks "How to Scale SVG"; Duarte Diagrammer taxonomy (Flow/Network/Stack/Segment/Join); Mayer & Johnson (signaling).

### P8 — S7's charts must be real, annotated vector charts, and the data must integrate to the stated AUC
Render the prototype's two charts as a small-multiple pair of inline SVGs from a **checked-in synthetic-points JSON**: a twin-ROC with the **0.91→0.78 leakage wedge shaded and labelled in-frame** ("= the leakage we removed · illustrative · synthetic"), and a calibration plot vs the y=x diagonal ("this is what prices the bridge"). **The headline is the GAP, never a high AUC.** The JSON must be generated so the trapezoidal AUC of each curve **equals** its labelled value (0.91 / 0.78); the shaded region **is** the 0.13 gap. Add a visually-hidden data `<table>` for a11y and for the "show me your data" answer.
*Why:* S7 currently has **no** charts, only bullets describing charts — the worst of both worlds. The deck's own thesis *is* the gap; a single 0.78 throws away the story. A made-up curve that doesn't integrate to the stated AUC is a −1 waiting to happen on the slide *built to invite* the leakage attack.
*Source:* Knaflic, *Storytelling With Data* (annotate on the chart); Tufte data-ink.

### P9 — Strict pre-attentive color discipline (one job per accent)
Keep the locked palette; enforce one role per colour: **mint `#7FE7A6`** = the single takeaway / health-positive / "demonstrated today" / the outward win-loop *only*; **blue `#74B2FF`** = secondary signal / Predict; **amber `#F5C265`** = caution / "sizes & warns, never grants"; **red `#FF8585`** = risk / concession / human-gate padlock / "roadmap-only · unproven"; grey (text-2/text-3) = all context. **Never bold more than the one phrase that is the slide's point.** Encode the moat **honesty** visually (T0 lit-mint vs T1 grey-dashed) instead of in a bullet.
*Why:* pre-attentive attributes (colour/size/position) are processed before conscious attention — one bright element on a neutral field is seen in <0.5s. Deck v1 bolds dozens of phrases per slide, so nothing is pre-attentive.
*Source:* Knaflic (declutter then focus; pre-attentive); Tufte data-ink ratio.

### P10 — Pace with fragments; morph before/after with auto-animate
Reveal multi-part slides one logical beat at a time with `class="fragment"`. Morph every before/after with `data-auto-animate` on adjacent `<section>`s using matching `data-id` — reserve the global `fade` transition for act breaks only.
*Why:* progressive disclosure paces cognitive load to the narration. auto-animate uses FLIP for **object constancy** — a node that visibly *moves* reads as the *same* object, so the rigid-pipeline → agentic-loop transition reads as one continuous transformation, not two unrelated diagrams. This is the mechanism that replaces the scale hack for genuinely multi-claim slides.
*Source:* reveal.js Fragments + Auto-Animate; Reynolds, *Presentation Zen* (one idea per slide).

### P11 — Steepen the type scale and tighten the craft
Replace the flat 32px-title / 21px-body (= 1.52×) with a ~1.3 modular scale at **~2.5–3× display:body contrast**: title 56–72px Bricolage 700 (tracking −0.035em, ≤2 lines), lead 28px, body 21px (**notes/appendix only**), label 14–16px, caption 13px, mono 12px. **All numbers in Geist Mono with tabular figures (`tnum`)** so columns never go ragged. Hairline borders held at 8% white; small radii; **left-set asymmetric** layouts (true centering only on cover + dividers).
*Why:* stage slides are billboards, not reading interfaces — flatness itself reads as an AI/template deck. The most-cited premium-UI imitation failures are measurable (loose tracking, borders too visible, radii too large, proportional figures making ragged number columns, centered-everything).
*Source:* Bringhurst/Brown modular scale; Vercel Geist typography. *(Heuristics, not research: "centered-everything / flatness are AI tells" — treat as craft guidance.)*

### P12 — Narrative spine: Duarte sparkline, one named villain, answer-first
Sequence as a sparkline that oscillates "what is" vs "what could be"; name **one villain** — *the single balance that lies* — and lead each slide **answer-first** (conclusion in the headline, evidence beneath). The before/after (rigid pipeline → agentic loop) is the natural emotional turn. This is **sequencing**, not a content rewrite — the words are locked; the order and headline framing are the lever.
*Source:* Duarte, *Resonate* (sparkline); Minto (answer-first).

---

## Anti-patterns to refuse

**AI-generic tells**
- Topic-label title + tidy 3–5 bullet list + stock-icon row, all centered.
- "Illustrative chart goes here" / grey placeholder boxes / a pasted bitmap of a chart / stock "diverse team at a screen" / abstract-network-globe hero.
- Gradient-filled bars, 3D, drop-shadowed KPI cards, glossy chart frames, gridline clutter, decorative motion (spin/zoom/fly-in).
- "Complying" with a 6×6 / 7×7 word rule — folklore with no research behind the counts; it just yields a shorter bullet document.

**Deck-v1 sins (verified against the repo)**
- `render_body()` dumps every `- ` source sentence as a 21px `<li>` at 60ch — 250–400 words/slide projected.
- `fit()` (build_deck.py 238–261) scales dense bodies uniformly to 0.5× → sub-legible ~10px type + inconsistent sizes.
- The production-ready `[VISUAL:]` briefs are buried in a collapsed designer-only `<details>` while the bullets fill the slide — the exact teleprompter-on-a-wall inversion.
- **11 slides** carry tables (S2, S4, S8, S10, S11, S12, S13, S15, S17, S19, **S22 = 18 rows**) at 15px/th-11px as primary on-stage evidence — below legible projection thresholds. S22 (the closing reflection) is the single densest slide.
- Topic-phrase titles forfeit the headline test; flat 1.52× hierarchy; only `RevealNotes` loaded (no fragments/auto-animate/highlight); Google Fonts via CDN (offline hole); **S7 has no real charts**.

**Honesty anti-pattern (rubric-fatal here):** burying the load-bearing concessions in grey sub-bullets — *T1 is grey until Phase 3, data is commodity / not the moat, sizes-&-warns-never-grants, WTP is the #1 open question, illustrative/synthetic.* These must be **visible in the visual** (dashed / hatched / struck-through / red-padlock encodings), because an undefended *or* over-claimed point is a −1.

---

## The layout system

**Type scale (CSS tokens, replace the flat 1.52×):** `--t-title` 60px clamp(56–72) Bricolage 700 / tracking −0.035em / ≤2 lines = the assertion at one fixed size across all slides · `--t-lead` 28px · `--t-body` 21px (notes/appendix only) · `--t-label` 14–16px · `--t-cap` 13px · `--t-mono` 12px Geist Mono +0.14em uppercase (kicker + all chart/diagram labels). Numbers everywhere use Geist Mono `font-feature-settings:'tnum'`. Hero numbers via `r-fit-text` — **but see the feasibility note: the realistic ceiling is ~0.8×canvas, so only short tokens (`~81 days`, `38.5%`) reach billboard scale; long numbers (`3,425,767`) auto-size *down*.**

**Grid:** fixed 1280×840, `minScale:1 / maxScale:1`, `center:false`. 12-column, ~24px gutter. **Sanctioned layouts (pick from a small set of 2–3, do not freely vary):** (a) left-set headline + large right/full evidence (5/7 split); (b) headline-over-full-bleed-evidence (`r-stretch`); (c) centered cover/divider. Consistency across 22 slides > per-slide novelty.

**Spacing:** 8px base (4/8/16/24/40/64); outer margins **72–88px** (up from 46/64). Negative space as a tempo tool, bounded by the fixed canvas (not "double it").

**Colour roles:** as P9. **Contrast rule (a11y):** `text-3 #5E6772` on `#090B0E` is ~3:1 — **large display only (≥24px)**; all ≤16px labels/captions use `text-2 #99A2AD` minimum (~4.5:1) so the back row can read them. Surfaces flat — the only gradients are the existing background radial glows (the cover **reuses** the viewport glow; it does **not** stack a second gradient).

**Component vocabulary (the reusable `<defs>` + CSS classes):**
- sentence-headline (h2 @ `--t-title`, left-set, ≤2 lines)
- mono kicker carrying the rubric chip, e.g. `RUBRIC 6 · PROTOTYPE`
- SVG symbols: `.node` / `.node--payer` (mint ring = join key) / `.edge` / `.edge--loop` (outward win-arrow) / `.gate` / `.padlock` (red, human-gate) + mode-colour legend (Predict=blue, Recommend=amber, Act/health=mint)
- **tier-strength bar** (T0 solid-mint / T1 grey-dashed / T2 hatched-half-lit) — the honesty-encoding primitive
- **small-multiple comparison board** (identical mini-frames, one highlighted differentiating cell) — the table replacement
- **hero-number billboard** (`r-fit-text` figure + ≤6-word caption + one faint comparison glyph; source spoken)
- **gated-rail station + padlock-gate-with-test glyph** (roadmap)
- `r-stretch` evidence container (one chart/diagram fills the space under the headline)
- structured `<aside class="notes">` (see below)
- appendix backup slide (one per likely defense question, excluded from running order)

---

## reveal.js capabilities to use (with feasibility corrections)

| Feature | Use | Feasibility note |
|--|--|--|
| `<aside class="notes">` + Speaker View (`S`) | On-slide = headline+visual; route all prose + numbers + DEFENSE to notes | Already vendored (`notes/notes.js`). ✓ |
| Fragments (`fade-in/-up`, `highlight-current`, `data-fragment-index`) | Assemble the ontology layer-by-layer; reveal the three tiers as reached; light roadmap stations L→R | Core. ✓ |
| Auto-Animate (matching `data-id`, FLIP morph) | The rigid-pipeline → agentic-loop **turn** as one continuous morph | Core. Set `autoAnimateDuration:0.7`. ✓ |
| `r-stretch` / `r-fit-text` | Size the one chart/diagram to the canvas; hero numbers | Core. **`r-fit-text` caps at ~0.8×canvasWidth** — long numbers scale *down*, not up to 300px. |
| `data-background-iframe` (`data-preload`, `data-background-interactive`) | The **live prototype** full-bleed as actual demo | Make it a **vertical sub-slide of the prototype slide** (reached only if the prof says "show me") — a new horizontal slide would break the locked count. |
| Vertical/nested `<section>` stacks | Push defense/detail **down** (leakage detail, AML-vs-credit two-gates), reachable only if asked | Core. ✓ |
| PDF export `?print-pdf` + `showNotes:'separate-page'`, `pdfSeparateFragments:false`, `pdfMaxPagesPerSlide:1` | One-notes-page-per-slide **leave-behind** | **`css/print/pdf.css` is NOT vendored and the builder injects no print stylesheet — must vendor + inject it**, or the offline PDF silently breaks. |
| RevealHighlight (code/config walks) | — | **NOT vendored** (only reveal.js/reveal.css/notes). Drop the code-walk feature *or* budget vendoring the plugin offline. |
| Charting library (Chart.js etc.) | — | **Do not add.** Inline SVG from JSON is sufficient; a JS lib re-adds a runtime dependency the vendored-offline deck avoids. |

---

## Build-time glance gates (operationalized acceptance)

The build script asserts these per rendered `<section>` (fail the build, not the eyeball):
1. **Zero prose `<li>` and zero `<table>`** in the on-stage `<section>` (all in `<aside>`/appendix). *The one sanctioned exception: the ≤3 on-visual labels render as `<ul class="labels"><li>` — these are short fragments (P1/P7), not prose, and the build exempts `ul.labels`.*
2. **Action-title 8–14 words** (token count).
3. **≤12 words of non-headline on-slide text**, OR ≤3 short labels.
4. **Exactly one mint focal element** on the focal layer (count `fill/stroke=mint`).
5. **Self-hosted fonts** (no external `<link>`); **print stylesheet present** when `?print-pdf`.

---

## The notes / leave-behind convention

Each slide's `<aside class="notes">` is **three labelled blocks** so Speaker View and the PDF stay readable and the −1-per-claim defense maps 1:1:
- **NARRATION** — the spoken prose (the current SPEAKER NOTES).
- **NUMBERS + SOURCES** — every sourced figure with its provenance (the master number-defense card, per-slide).
- **DEFENSE** — the Q/A blocks.

Per-note length sanity bound so a single `<aside>` (e.g. S22) never becomes one unusable notes pane.

---

## Font asset bundle (self-hosting, to close the last offline hole)

Vendor woff2 subsets, OFL/SIL sourced, Latin + the few symbols the deck uses (`€ § →`):
- **Bricolage Grotesque** (display) — weights 400/700 (opsz axis if shipping the variable font).
- **Geist** (sans) — 400/500/600/700.
- **Geist Mono** (mono) — 400/500 + `tnum` feature.

Replaces the Google Fonts `<link>` (build_deck.py line 221).

---

## Sources

- Michael Alley — *The Craft of Scientific Presentations* / assertion-evidence.com. Alley, Schreiber & Muffo 2005 (significance result); Garner & Alley 2013 (cognitive-load study); Mayer & Johnson (signaling — short labels-on-diagram help).
- Barbara Minto — *The Pyramid Principle* (action titles, answer-first). McKinsey/BCG action-title convention.
- Nancy Duarte — *slide:ology* (glance test, 50/75-word thresholds), *Resonate* (sparkline), *Slidedocs* (present vs read artifacts).
- Garr Reynolds — *Presentation Zen* (one idea per slide, restraint, whitespace).
- Edward Tufte — *The Cognitive Style of PowerPoint*, *The Visual Display of Quantitative Information* (data-ink, small multiples).
- Cole Nussbaumer Knaflic — *Storytelling With Data* (declutter then focus; pre-attentive; annotate on the chart).
- Richard Mayer — *Multimedia Learning* (redundancy effect + its boundary condition); Kalyuga/Chandler/Sweller.
- John Medina — *Brain Rules* (the multitasking myth).
- Stephen Few — *Show Me the Numbers* (table-to-look-up vs chart-to-reveal).
- Bringhurst / Brown — modular type scale; Vercel Geist typography.
- reveal.js docs — Layout (`r-stretch`/`r-fit-text`), Fragments, Auto-Animate, Backgrounds, Speaker View, PDF export.
