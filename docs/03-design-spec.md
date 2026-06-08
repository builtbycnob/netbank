# 03 — Design Spec: NetBank Mobile

> **Decision-driven spec for the v1 mobile product.** This consolidates the full screen map, the dark visual system, the recommended Home concept (scored), and the one deep hero flow into a single committable reference. It inherits directly from [`00-product-definition.md`](00-product-definition.md) (the team brief), [`02-mobile-experience.md`](02-mobile-experience.md) (north star, HMWs, 6 design principles), and the architecture table in the [README](../README.md).
>
> **Method (non-negotiable):** *Problem → HMW → Decision → Moment → Screen.* We never start from "we need a home, settings, a profile." Every element on every screen traces to a **decision** the user (or the AI *for* her) makes. Orphans get killed. This doc therefore documents **decisions, not screens** — the screens are just where the decisions live (see the traceability note in §6).

---

## 1. North star & the load-bearing constraints

### 1.1 The Apple-of-banking principle
Apple didn't make the smartphone more *powerful* — it made complexity **disappear** behind sensible defaults, progressive disclosure, and one obvious thing to do. NetBank does the same for a small business's money: the tax engine, the receivables model, the cash-flow forecast are **complex underneath and invisible on top**. As few clicks as possible per task. Data-dense, never cluttered.

### 1.2 The inverted flywheel (the objective function)
Success = the customer opens the app **less** and feels calmer, not more "engaged." The objective function is **customer financial health, not fee/engagement extraction**. Declining dependence on a credit bridge is a **win, not churn**. This is the sharpest weapon against the engagement-driven-neobank default — and it must be visible on screen (e.g. the *avoided-borrowing tally*, the *"you don't need to borrow"* moment).

### 1.3 The compliance-critical architectural split (carried through every screen)
| Layer | What it does | Autonomy | Regulatory posture |
|---|---|---|---|
| **Non-credit autonomous core** | cash-flow / runway / burn, categorization, OCR, tax-sweep, **safe-borrowing *sizing*** | fully automated, 310-speed, **human-loop OUT** | **outside** AI Act Annex III & GDPR Art. 22 |
| **Credit grant** (the bridge / draw) | granting an actual loan against the line | **human-on-the-loop, human-loop IN** | credit-scoring of a natural person = **Annex III §5(b)** high-risk; **GDPR Art. 22(1)** restricts solely-automated refusal |

The split is **signposted, never hidden**: *sizing is autonomous and instant; the grant is human-reviewed.* This turns the human-on-the-loop into a **trust feature**, not a disclosed limitation. **Marketing must never imply autonomous lending.** Only the WeBank/MYbank *pre-qualification* is copied (zero-human); the *granting* is deliberately not.

### 1.4 The 6 design principles (from `02`, reaffirmed)
1. **Home = "Are we okay?" answered at a glance, calm.** Synthesized truth first, one primary action max. Not a feed, no gamification.
2. **The best screen is sometimes no screen.** The tax-sweep / auto-match just happens; the user gets a calm confirmation, not a task.
3. **Earned-trust ladder as a UI pattern:** *suggest → do-with-undo → autonomous*, visible and per-action.
4. **The credit flow shows the human-on-the-loop** ("a person reviewed this in Xs") — regulatory constraint rendered as trust.
5. **Explainability inside the UI:** "why is only €X free?" is expandable — serves GDPR/AI Act **and** trust.
6. **Make the AI legible on every screen** — predicting / recommending / acting, with undo on autonomous actions.

---

## 2. Dark visual system (tokens)

> Reference axis: **Mercury** (structural calm, single-voltage CTA) pushed **darker and more neutral** + **Stripe** (tabular numerals, financial DNA) + **Revolut** (controlled data accents) + **Linear** (monochrome discipline). **Dark by default, premium, never OLED-cheap.**

### 2.1 Surface & elevation (depth by *lightening*, never drop-shadows)
| Token | Value | Use |
|---|---|---|
| `--canvas` | **`#0E1116`** (navy/violet-tinted near-black, **never `#000`**) | app background, nav slot 1–2 |
| `--surface` | `#161A22` (≈ +4–6% L) | cards, metric tiles, hero tiles |
| `--surface-elevated` | `#1A1F27` | nested panels, slide-overs |
| `--surface-overlay` | `#1E2430` + 4–8% white overlay | modals, tooltips, toasts |
| `--border-subtle` | `#232834` (hairline, "melts into bg") | dividers, card edges |
| `--border-strong` | `#2C3340` | focused/active edges |

Higher z-index = **lighter** surface + a 4–8% white overlay. No heavy shadows, no glow, no gradients faking depth.

### 2.2 Text (off-white, opacity tiers — never pure white)
| Token | Value | Emphasis |
|---|---|---|
| `--text-primary` | `#E0E0E0` @ 87% | balances, headings |
| `--text-secondary` | `#C3C3CC` @ 60% | labels, meta |
| `--text-disabled` | @ 38% | placeholder, disabled |

### 2.3 Accent — single voltage, **NetBank's own**
- **`--accent` = a desaturated teal/green** (the *financial-health* signal — deliberately **not** Mercury indigo `#5266eb`, which screams "Mercury"). Desaturate ~15% for dark so it doesn't optically vibrate; must pass WCAG 4.5:1 on `--canvas`.
- **Single-voltage rule:** exactly **one filled-accent element per screen** (the primary action). Everything else is text/ghost/outline.
- **Decoration-blue** (periwinkle `#9CB4E8` / mist `#CDDDFF`) is reserved for **the hero number wash and charts ONLY — never on buttons.** Keeps "this is clickable" unambiguous on a dense dashboard.

### 2.4 Numbers are the product
`.num { font-feature-settings: 'tnum' 1, 'ss01' 1; letter-spacing: -0.01em; }` — applied to **every** balance, burn, runway, per-bucket, per-employee, safe-to-borrow and transaction amount, so digits align in columns and **never jitter on live update** (Stripe's financial-DNA tell).

### 2.5 Gains / losses (survives 1-in-12 colorblindness)
- **gain = desaturated blue/teal**, **loss = amber/orange** — **never red/green** (and never *pastel* red/green, which collapses to identical gray for deuteranopes).
- **Always** paired with a glyph (▲/▼) **and** explicit sign (+/−). Color is never load-bearing alone.

### 2.6 Typography
- **Inter / Inter Display** (OSS, ships cleanly; the Mercury-Arcadia look without the licensing dead end). Optionally **Space Grotesk** for display titles. Light-to-regular weights; **negative tracking on display**; enable `ss01`.
- Inter Display only above ~24px optical size.

### 2.7 Data-viz on dark
- **Invert the sequential convention: high = brighter** (bright pops on dark; muted disappears). Gridlines = white @ 5–8% alpha (no "prison-bar" cage). ≤7 categorical hues; ≤5 on the bucket bars.

### 2.8 Motion (subtle, trust-building, **no bounce**)
`--dur-fast 120ms` (press) · `--dur-base 180ms` (hover/dropdown) · `--dur-slow 280ms` (modal/slide-over). `--ease-out cubic-bezier(0,0,0.2,1)` entrances, `--ease-in cubic-bezier(0.4,0,1,1)` exits. **No bounce/elastic/spring overshoot** (reads toylike, erodes bank trust). Animate `transform`/`opacity` only. Honor `prefers-reduced-motion` (~15% of users) with a 150ms fade fallback.

### 2.9 Density, grid, targets
- **8pt grid** (4pt half-step), named space tokens in rem. Tables compact: 14px/20px body, 32–36px control height, melt-into-bg dividers, **reveal row-actions on hover/focus** only, **persisted** density toggle.
- **Touch targets:** WCAG 2.2 AA = **24×24px legal floor** (EAA in force since 28 Jun 2025); keep the *visible* control 32–36px but extend the **hit area to 44px** via invisible padding.
- **Focus ring token:** `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }` on every interactive element.
- **Radii:** 4px base (financial/serious), 12/32px only on pills/CTAs.
- **CI audit:** check **both** WCAG 2.x ratios **and** APCA (Lc75 body / Lc45 large-bold) since dark/OLED reads differently.

---

## 3. Bottom navigation — 4 destinations + 1 center action

```
┌───────────────────────────────────────────────────────────┐
│  ⌂ Home    ⤢ Money   (＋ Scan/Pay)   € Financing   ⋯ More │
└───────────────────────────────────────────────────────────┘
   destination  destination   ACTION      destination   destination
```

**Slots:** `Home` · `Money` · **`Scan/Pay`** (center action) · `Financing` · `More`.

### Rationale
Mercury's mobile bar is genuinely **4 destinations + 1 center action** (the "Move Money" double-arrow) — 5 visual slots, 4 of them *places*. We copy that **structure**, not the literal count:

- **Home** — the synthesized *"are we okay?"* surface (total cash, burn, runway, safe-to-borrow).
- **Money** — an aggressive grouping of **Accounts + Cards + Transactions** as *sub-tabs* (the recon's explicit anti-over-stuffing rule: Mercury's web sidebar has 7+ items; mobile must group hard).
- **Financing** — earns its own destination *against* the grouping instinct, **because it is the moat.** The always-present *"Safe to borrow: €X"* must never sit below the fold or behind an "Apply" form (WeBank/MYbank pre-underwriting validation).
- **More** — low-frequency surfaces (Services marketplace, Invoices AP/AR, Settings, team admin, AI-activity/audit log), reachable also via universal search and contextual deep-links.
- **Scan/Pay (center action)** — the highest-frequency repetitive task for a finance-staff-less micro-business: phone-snap OCR invoice capture + Pay/Schedule, collapsed to one thumb-tap. This is NetBank's equivalent of Mercury's center "Move Money."

**Single-voltage in the chrome:** the **center Scan/Pay action is the only filled-accent slot.** Plain-language labels throughout (*Money, Financing, Scan/Pay*), never jargon (*Treasury, Facility*).

---

## 4. Screen specs

> Each spec lists the **decision served**, layout, key components, **AI-legibility** (the predicting/recommending/acting chip system + the human-review badge placement), **explainability**, and the **fewest-clicks move**. Shared dark tokens from §2 apply everywhere.

### 4.0 The AI-legibility chip system (cross-app standard — locked)
Three visual vocabularies, **never blurred**, identical on every screen:
- **PREDICTING** — *ghost / subtle chip.* A computed estimate (runway, forecast, sizing). Inspectable via an "assumptions" disclosure. No action implied.
- **RECOMMENDING** — *accent-outline chip.* The AI suggests; **the human's tap is the decision.** Visually distinct from the one filled CTA so "suggestion" ≠ "the app is acting."
- **ACTING (+ Undo)** — *accent-fill chip + Undo affordance.* The system already did something autonomous (OCR extraction, auto-match, auto-categorize, disbursement, tax-sweep). **Undo is mandatory and visible.**
- **"Human-reviewed" badge** — a **distinct, verified checkmark-shield**, visually unlike the three chips, **locked exclusively to the credit grant** (§5, Financing). It appears **nowhere else** in the app, so it carries real signal.

---

### 4.1 Home / Dashboard — the daily "are we okay?" surface
**Decision served:** *Is my business financially healthy today, and how many months of runway do I have?* — answered in under 3 seconds, **zero taps**.

**Layout (top→bottom, ruthless above-the-fold, NO single giant chart — Mercury's documented Home flaw):**
1. **Sticky greeting row** — plain-language greeting + date; universal search + avatar/notification dot.
2. **Verdict strip** *(grafted from the Cash-Flow Story concept)* — one calm sentence read **before** the grid: *"You're OK — 7.9 mo runway, next tight spot ~22 Jul · ▲ on track."* Trajectory glyph + sign, tabular.
3. **Hero band A — "Are we okay?"** — **Total cash** (lead figure, `.num`) across all accounts incl. pending → paired **Burn rate** + **Runway** stats. Runway carries a ghost *Predicting* chip and a calm color band (green >6mo / amber 3–6 / soft-red <2). Then stop.
4. **Hero band B — "Safe to borrow: €X"** *(demoted per Home Judge)* — pre-computed, decoration-blue wash, micro-label *"Pre-qualified · no application,"* and a signpost *"Sizing is automatic — any loan is human-reviewed."* Rendered as a **secondary card with a "why only €X?" chevron**, **NOT** a filled-CTA hero — so the **only filled-accent element is the center Scan/Pay action**, keeping Home consistent with the inverted-flywheel north star.
5. **Revenue trajectory sparkline** — compact, with a dashed forward-forecast segment (blue/amber + glyph). Not viewport-eating.
6. **Spend-per-bucket strip** — 4 tappable tiles (Operations / Marketing / SaaS & AI / Payroll), each deep-linking to a pre-filtered Transactions view. Header: *"Where your money went."*
7. **Spend-per-employee mini-list** — top 3 + "See all," fed from card-level tagging.
8. **Optional AI-nudge row** — accent-outline *Recommending* chips, dismissible, render only when a real signal exists.
9. **Avoided-borrowing tally chip** *(grafted from One Decision Now)* — quiet footer: *"Saved €310 in avoided borrowing this year ↗"* — the inverted-flywheel P&L on screen, proof the home is not a lending funnel.

**AI legibility:** Home operates in the **PREDICTING** register (runway, forecast, sizing) — no human-review badge belongs here (it's locked to the grant). The safe-to-borrow card's "why €X?" disclosure surfaces the **per-client reliability** framing (*"Studio Vermell pays 96% on-time"*), the closed-loop moat made legible. Nudges are *Recommending* (outline). Nothing on Home autonomously moves money → no *Acting* chip by default (the restraint is itself legibility).

**Explainability:** every figure is one tap from its inputs — Runway → slide-over (cash ÷ avg burn + scheduled outflows + expected AR); Burn → breakdown by the same 4 buckets so headline burn ties out with the tiles; Safe-to-borrow → Financing's elasticity meter + forecast.

**Fewest-clicks move:** **zero-click answer + one-tap moat.** The "are we okay?" decision is answered with no tap (cash/burn/runway are first on screen, no chart to scroll past). Complexity is hidden behind progressive disclosure.

---

### 4.2 Money — Overview (Accounts hub)
**Decision served:** *How much do I have, where is it spread, and is anything off?*

**Layout:** sticky "Money" header + **sub-tab switcher (Accounts | Cards | Transactions** — accent-underline, not filled); **synthesized total-available hero** (rollup incl. pending out, `.num`, day-delta with blue/amber + ▲/▼); an **"Is anything off?" AI insight strip** (0–N accent-outline *Recommending* chips → each deep-links to its filtered view; calm *"All clear"* fallback); a **nested account list** (each account a lifted surface card with masked IBAN, balance, 7-day decoration-blue sparkline, low-balance amber dot+glyph); a **collapsible bucket-distribution bar** (≤5 desaturated hues, tappable segments); **single filled "Move money" CTA** + ghost "Open an account."

**AI legibility:** PREDICTING (the hero total carries a ghost "computed across N accounts" chip + "how this is calculated") + RECOMMENDING (anomaly chips). **No Acting, no human-review badge** — this screen observes and suggests, it never moves money.

**Explainability:** each anomaly chip expands to *signal + baseline + magnitude + "View transactions"* deep-link to the exact rows. Forecast-derived flags link to the same projection that drives Home runway and Financing safe-to-borrow (one consistent model).

**Fewest-clicks move:** the screen **is** the answer (zero taps); every diagnostic doubles as a one-tap shortcut to its fix; exactly one filled action.

---

### 4.3 Money — Cards (per-employee control surface)
**Decision served:** *What can each employee's card spend on, and which flagged transactions need my attention?*

**Layout:** Money sub-tab switcher (Cards active); a **"Needs your attention" band** (0–3 accent-outline flag cards: *missing receipt + auto-freeze countdown*, *bucket overspend vs forecast*, *duplicate vendor across cards* — each with € impact + one inline action; calm *"All cards healthy"* all-clear state); a **spend-this-month micro-strip** (one tabular MTD figure + blue/amber delta + a single thin per-bucket segmented bar, each segment deep-linking); **single filled "Issue card" CTA** (opens an instant-issue slide-over); the **card-per-employee list** (avatar + name, card-type glyph, masked PAN, tabular limit with used/limit hairline, glyph+label receipt-compliance status ✓/⚠N/🔒, left accent-edge on flagged rows). **Controls checklist** (MCC allow/block, merchant-lock, amount + time-period); **one-card / multiple-budgets** tagging; **instant virtual cards**; **configurable auto-freeze** (7/14/30 days). Density toggle persisted.

**AI legibility:** **PREDICTING** (ghost) on spend-vs-forecast; **RECOMMENDING** (outline) on AI-suggested limits (*"recommend €800/mo — in line with this role"*, accept/adjust/dismiss) + duplicate-vendor flags; **ACTING (+Undo)** on the **soft auto-freeze** — the one autonomous action, with the countdown shown *before* it acts and instant un-freeze on receipt upload (graduated, recoverable, never punitive). **No human-review badge** — card limits/freezes are operational controls in the non-credit core, outside Annex III; a note states *"Card limits are automated; loans are human-reviewed."*

**Explainability:** every chip expands to its grounding (limit math, freeze trigger, the 3 duplicate charges); each card's full autonomous-action history is in the AI-activity log.

**Fewest-clicks move:** exceptions-first default (Qonto-inbox applied to cards); the common fix is a single inline tap on the flag card; issuing a fully-controlled card collapses to one slide-over with an AI-pre-filled limit + MCC checklist.

---

### 4.4 Money — Transactions (the analytical heart)
**Decision served:** *Where did the money actually go, and which bucket / employee / vendor is driving spend?*

**Layout:** **chart-on-top, list-below** (Mercury "single source of financial truth") — a **"Money in / out" cashflow chart** defaulting to current month (in = teal/▲, out = amber/▼, net line, gridlines @6%), a net/burn readout that wires back to Home; a **status-tab table** (*Needs review (n)* default / All / Reconciled — **Qonto inbox**: matched items auto-clear); a **filter row** (Bucket / Employee / Vendor / Amount chips + **"Exclude from analytics"** toggle); **Saved Views** (Ramp model: filter+sort+columns persisted as named tabs); the **list** (merchant logo, name+meta, **auto-category chip with inline AI-suggested badge**, receipt-status icon, sign-colored tabular amount; sticky day sub-headers with running totals; row actions reveal on hover/long-press); a **bulk-edit toolbar** (select-across-pages + contextual "Set category" + filter-then-apply); density toggle. Deep-links into the **SaaS & AI Spend** lane.

**AI legibility:** PREDICTING (ghost "computed" on the chart) · GENERATING/RECOMMENDING (per-row category badge; confidence style-encoded — solid = high, dotted-underline = low) · ACTING+Undo on accept/correct (*"Learning from your fix — Undo"*; bulk: *"Re-categorized 23 Amazon charges · Undo"*; Exclude toasts with Undo). **No human-review badge** — categorization is non-credit core.

**Explainability:** chart "computed" → assumptions sheet; each suggestion tappable to its grounding (*"matched on MCC + your past 3 fixes"*); Exclude annotates the row so headline burn never diverges from raw sum unexplained; bulk actions state scope before/after.

**Fewest-clicks move:** **filter-then-bulk-apply as one gesture** — default to "Needs review," tap a vendor chip → tap "Set category" → pick = the entire vendor history re-categorized **and** a forward rule learned, in 3 taps, reversible.

---

### 4.5 SaaS & AI Spend — separated lane (deep-link from Transactions)
**Decision served:** *Is this recurring vendor still worth paying for, and should I cap or cancel it?* — turns the invisible bleed of stacked subscriptions and metered AI/cloud spend into one-tap decisions. **The wedge no incumbent in the EU micro/agency segment ships** (Mercury reviewers explicitly ask for a separate subscriptions tab).

**Layout:** **synthesized-number hero** (total monthly recurring spend + amber/▲ delta + ghost *predicting* annualized projection); a **subscription-trend chart** (6-month default, decoration-blue wash, segmented **[All · AI/Compute · SaaS tools · Infra]** with **AI/Compute** as the differentiating default); a **savings-summary strip** (*"AI found €486/mo you could cut · Review 4 flags"*); a **filter/sort bar** (default sort "Needs attention," flagged float to top); **vendor ROW CARDS** (logo + plain name + billing card/owner + tabular cost + trend sparkline + flag chip with € impact), each with **one contextual accent action** — *Cap with virtual card* / *Cancel* / chevron; **Undo toast** with timer ring after any action.

**AI legibility:** PREDICTING (annualized projection, trend) · RECOMMENDING (every flag: *duplicate / unused license / price ▲*, each with € impact + one-tap action) · **ACTING+Undo** on *Cap with virtual card* (issues a preset-limit virtual card that **auto-declines overages** — recommendation becomes a hard control). **No human-review badge**; a footer states *"These flags don't affect your safe-to-borrow."*

**Explainability:** each flag expands to plain-language "Why?" (*"Notion billed to Maria's card €240 AND company card €190 — same workspace family"*; *"Figma €144→€170 (+18%) on 2 May, prior 6-mo avg €144"*). Scope honestly bounded: **spend-side signals only**, not true license/seat-usage governance.

**Fewest-clicks move:** flags pre-computed and floated to the top; each flagged row carries its single correct action inline → cutting €430/mo of duplicate Notion or capping a price hike is **one safe (Undo-backed) tap**, no confirmation modal, no cancellation-portal hunt.

---

### 4.6 Scan / Pay — center action, phone-camera OCR capture → Pay/Schedule
**Decision served:** *Is this invoice captured correctly, and do I pay or schedule it now?* — the highest-frequency repetitive task, collapsed to one thumb-tap from any screen.

**Layout:** opens **camera-first** (full-bleed sheet, not a destination page). **Capture band:** live viewfinder with auto edge-detection + a confidence ring that **auto-fires** when the page is confidently framed (the shutter is the single voltage on this band); flash, gallery/PDF import, "choose existing file" for forwarded invoices. On capture it slides up to **Review:** a zoomable **captured-document strip** (with an *Acting · Undo* chip); an **extracted-fields list** (Merchant, Invoice #, Issue/Due date, Net, VAT rate+€, **Total** as the largest tabular figure, IBAN/payee, auto Category) — every field inline-editable, **per-field confidence styling** (solid = high; amber underline + "verify" glyph only on low-confidence fields); a **match & route band** (*Recommending*: auto-match to a pending transaction OR route as new **AP/AR** — explicitly separated, never mixed) with a **runway-context note** (*"Paying now leaves €38,200 · runway 6.1 mo"*); a sticky **"Pay now | Schedule"** segmented control where exactly one option is the filled CTA, with the all-in debit detail above it. Lost-receipt affidavit / itemized reconstruction; fast manual-match fallback (never hard-block).

**AI legibility:** extraction is **ACTING+Undo** (the *Acting* chip on the strip; Undo reverts to the raw scan with empty fields); auto-match + category are **RECOMMENDING** (await a tap, never silently committed). **No human-review badge** — Scan/Pay is the non-credit core (OCR, categorization, matching, payment execution), explicitly outside Annex III; its absence here is meaningful.

**Explainability:** tapping the *Acting* chip / long-pressing a field opens "How we read this" with a **bounding-box overlay** on the thumbnail; low-confidence fields self-explain (*"VAT rate unclear — non-standard layout"*); the runway note expands to the post-debit consequence; corrections = *"learning from your fix."* All executions/undos write to the AI-activity log.

**Fewest-clicks move:** the happy path is **zero deliberate clicks until the final commit** — center action opens straight to the viewfinder, edge-detection auto-fires, AI auto-fills + auto-matches, and the Pay/Schedule default is pre-selected from context → the user's only required tap is the single **Confirm**.

---

### 4.7 Invoices (AP / AR) — in More
**Decision served:** *What do I owe, what am I owed, and what's overdue?*

**Layout:** sticky "Invoices" header (inline *predicting* "forecast updated 2m ago"); a **synthesized net-position hero** (*"owed €X / owe €Y / +€Z net"* — blue/▲ owed, amber/▼ owe) with an **overdue pill** (*"€W overdue · 3 invoices"*) and a compact **AR-aging micro-strip** (Current / 1–30 / 31–60 / 60+, brighter = more at risk); an **AP/AR segmented control** (*Needs action* default; **AP and AR clearly separated, never mixed**); a **Qonto-style inbox list** (matched/paid auto-clears, overdue-first, each row = counterparty + tabular amount column + status/due chip + **one context action**: Pay / Schedule / Chase / Remind); a contextual **"Bridge the gap" banner** (only on material AR overdue → deep-links the overdue AR amount into Financing → human-reviewed Loan Request — the **moat hand-off**).

**AI legibility:** PREDICT (collection-date forecast against the 85-day Spanish reality; ghost "may slip" chips) · ACT+Undo (items from Scan-OCR show *Auto-matched*; inbox auto-clearing carries a 5-sec Undo) · RECOMMEND (suggested chase timing, the Bridge nudge). **No human-review badge on the inbox** — it appears only after the user follows "Bridge the gap" into the downstream grant.

**Explainability:** forecast chips → assumptions (this client's lag, days overdue, 85-day baseline, seasonality, "feeds runway and safe-to-borrow"); auto-match → the matched transaction + re-match fallback; net-position hero → "how is this computed?"; aging ramp legend with glyph+label redundancy.

**Fewest-clicks move:** an **action inbox, not a ledger** — auto-clears the paid, overdue-first, one pre-decided primary button per row; turning an overdue receivable into cash is one tap that deep-links the exact amount into a prefilled, human-reviewed draw (no re-keying). New invoices enter via the global Scan/Pay action (no competing "+Add" FAB).

---

### 4.8 Financing — Safe to Borrow (the moat hub)
**Decision served:** *Do I have headroom, and what loan amount is safe for my business right now?* — answered as a calm always-on state, **never a form**.

**Layout:** sticky "Financing" header (ghost "How this works"); the **safe-to-borrow hero** (pre-computed €X, `.num`, decoration-blue wash **behind the number only**, *"Pre-qualified · no application,"* the **single filled "Request a draw" CTA**, micro-line *"Sizing is automatic. Any loan is human-reviewed."*); a **data-elastic limit meter** (accent-outline unlock chips: *Connect payroll → +€Y*, *Connect VAT/AEAT → +€Y*, *Add 2nd account → +€Y* — elasticity 0.407 embedded vs 0.090 opaque made visible); a **revolving available/drawn bar** (refills on repayment, live *"≈€7.40/day"* readout, one-tap Repay); the **earned-trust ladder** (Tier 0 Banking → 1 Cash-flow → 2 Invoices/AR → 3 Clean repayment, next-tier € delta + single requirement; downside *graduated, never all at once*); a collapsed **forecast-justification** row (*"Why €X? See the forecast"* → inspectable projection + assumptions); footer GDPR Art. 22 + "Talk to a CFO partner" links.

**AI legibility:** **SIZING is PREDICTING, human-loop OUT** (310-speed, non-credit core, outside Annex III) — ghost chips on hero/meter/forecast; connect nudges are **RECOMMENDING**. **No Acting / no Undo here** (sizing only displays a number; recompute is non-destructive). The **"Human-reviewed" badge is intentionally ABSENT** and only *promised* (*"any loan is human-reviewed"*), then **locked onto the next screen** (the grant) — that separation **is** the legibility message.

**Explainability:** three layers — glanceable ("pre-qualified, sizing automatic, human reviews any loan") → one-tap "Why €X? See the forecast" (inspectable cash-flow projection + which inflows/AR/burn drove it) → the meter itself (which missing data caps the limit and the exact € each unlocks). Footer exposes "How your limit is calculated" + the Art. 22 right-to-explanation path.

**Fewest-clicks move:** the answer is **already on screen, zero clicks**; the draw collapses to **tap CTA → nudge slider (optional) → confirm** in a slide-over (never an "Apply" page); repayment auto-aligns to the invoice cycle; raising the limit is a one-tap chip.

---

### 4.9 Loan Request & Grant — human-reviewed (the Annex III gate)
**Decision served:** *Do we grant this specific loan, at these terms, to this business?* — **AI recommends, a human decides.** *(Full step-by-step in the Hero Flow, §5.)*

**Layout:** an **amount slider** to the pre-computed ceiling with a **live all-in cost readout** (per-day + total, `.num`) shown **before** anything confirms (headline limit and drawable price never diverge); an **AI recommendation card** (accent-outline *Recommending*, grounded: cash flow, the specific bridged receivable + its per-client reliability, repayment history) with a cash-flow/invoice-cycle-aligned repayment shape (*"Bridge invoice #1042 — Studio Vermell, ~12 days, 96% on-time"*); a calm **"In review — usually under a minute"** state; the **distinct verified "Human-reviewed" badge** on approval; a graceful, explained **decline/counter-terms** path (Art. 22 contest route); a one-tap **Confirm draw**; an **audit-trail link** to the AI-activity/decision log.

**AI legibility:** **RECOMMENDING → Human-reviewed badge** (the badge lives here and **nowhere else**). Limit increases are AI-recommended but human-granted; adverse cuts are graduated/explained/recoverable and human-reviewed when they function as a credit decision.

**Fewest-clicks move:** the dormant pre-approved number means **no credit application** — slide amount (cost updates live) → Confirm after review clears → funds land; repayment is zero-tap (auto-settles on the bridged invoice) or one-tap, no early-repayment penalty.

---

### 4.10 Services Marketplace — in More
**Decision served:** *Do I need outside CFO / legal / compliance help right now, and which partner do I book?*

**Layout:** a **searchable marketplace** of vetted CFO / legal / compliance partners (contextual, not a bottom tab); **contextual triggers** deep-linked from Home/Financing/Invoices (*"VAT deadline in 9 days — book a tax partner?"*); value framing vs the gestor baseline (€60–100/mo) and seconds-not-weeks speed; **single-voltage CTA per partner card** (Book).

**AI legibility:** **RECOMMENDING** — the AI recommends the right partner + timing from real signals (forecast shortfall, VAT deadline, financing prep) as accent-outline chips; booking is the human's contextual one-tap. **No human-review badge.**

**Fewest-clicks move:** the need is surfaced contextually with the right partner pre-matched → booking is one tap, not an off-platform hunt.

---

## 5. The hero flow — Embedded Lending (go deep here)

> **Safe-to-Borrow → Request → Human-Reviewed Grant → Disbursed → Monitored → Repay.** This is simultaneously the **moat** (more-embedded → better-data → better-underwriting → safer-loans → more-trust → more-data) and the course's **agentic loan journey**, and the one place where the compliance split (§1.3) becomes tangible on screen. No EU incumbent in the micro/agency segment owns this loop (Qonto/Finom route credit to partners). *(Detailed field-by-field spec also preserved in the prior hero-flow draft; this section is the canonical summary.)*

```
1. SAFE TO BORROW   →  2. REQUEST          →  3. HUMAN-REVIEWED GRANT
   (always-on,          (one tap,              (the Annex III gate —
    no application)      cost-transparent)      AI recommends, human decides)
        ↑                                              ↓
6. REPAY            ←  5. MONITORED         ←  4. DISBURSED
   (revolving,          (continuous, calm,      (one-tap confirm,
    line refills)        mission-aligned)        funds land, Undo window)
```

| # | Step | AI role (chip) | Human-on-the-loop? | Regulatory anchor |
|---|---|---|---|---|
| 1 | **Safe to Borrow** | **Predicting** (ghost) | **No** — sizing only, 310-speed | **Outside** Annex III (capacity estimate, not a decision) |
| 2 | **Request** | **Recommending** (outline) | No — pre-grant recommendation | — |
| 3 | **Grant** | **Recommending → Human-reviewed badge** | **YES — the gate** | **Annex III §5(b) + GDPR Art. 22** |
| 4 | **Disbursed** | **Acting** (+ Undo) | No — executes the cleared grant | — |
| 5 | **Monitored** | **Predicting / Recommending** | Increase = human-grant; adverse cut = human-reviewed, graduated | Annex III / Art. 22 for adverse decisions |
| 6 | **Repay** | **Acting** (+ Undo, auto-settles on bridged invoice) | No | — |

**Two non-negotiable framings carried through every step:**
1. **The split is signposted, never hidden** (sizing instant; grant human-reviewed). The "two-clock honesty rule" at step 3: show *both* truths — *"Sizing was instant"* **and** *"This draw was reviewed by a person"* — never blurred into "approved instantly."
2. **The honest "you don't need to borrow" moment is a first-class branch** (§5.1), not an edge case.

**Mission guardrails:** revolving line refills in real time on repayment (line as utility, interest per-day-outstanding, **no early-repayment penalty**); the real-world **~77%-on-overdue limit cut is explicitly softened** to graduated, explained, recoverable steps (a customer-financial-health objective never yanks runway at the worst moment); the all-in per-day cost is shown **before both** the request-confirm and the disburse-confirm (headline ≠ drawable price is banned).

### 5.1 The honest "this gap self-resolves" branch (the objective-function proof)
When the closed-loop forecast predicts a **reliable inflow that closes the gap before borrowing pays off** (a 96%-on-time client's invoice lands in 9 days vs a 27-day bridge): the safe-to-borrow hero **inverts** to an advisory card (*"You probably don't need to borrow. Studio Vermell covers this in ~9 days — bridging would cost €38 for nothing."*); the primary action **de-escalates to a ghost** *"Remind me on the 9th"* (the healthiest action is the most prominent, and **NetBank makes no money today**); a one-tap safety net remains (*"If it slips, your €X line is still here"*); and it's logged in the **avoided-borrowing tally**. This screen **is** the P&L that an interchange/engagement-driven incumbent is structurally disincentivized to ship — the moat, rendered.

---

## 6. The recommended Home concept (scored) + "decisions, not screens" note

### 6.1 Three competing Home concepts — judged
| Concept | Score | Verdict |
|---|---|---|
| **Command Center** (stat-grid cockpit) | **8.7** | **Recommended.** Wins the home's #1 job — answers *"how am I doing?"* in <5s because cash+burn+runway+spend are simultaneously legible, no chart to read. Strongest Mercury-restraint / Revolut-polish balance; fewest clicks to broad situational awareness. |
| **Cash-Flow Story** (narrative timeline) | 7.4 | Best thesis-storytelling (the forecast *is* the hero; *"reads your invoices, not just your balance"* made literal) but a scrubbable timeline is **slower** to answer "am I okay?" and risks one big chart eating the viewport. **Not the home — the ideal Financing-hub / forecast-detail surface** and the canvas for the "you don't need to borrow" moment. |
| **One Decision Now** (single-card triage) | 6.9 | Lowest cognitive load and purest inverted-flywheel expression, but **hides at-a-glance breadth** a 2–10-employee owner wants, lives or dies on the priority-ranker, and is structurally tempting to become a "borrow €X" front door. **Not the home — the Decision Card pattern survives verbatim inside the Financing/bridge flow.** |

### 6.2 Recommended Home: **Command Center** (with one mandated edit)
A single-glance *"are we okay?"* cockpit: a **synthesized truth band** on top (total cash → burn + runway), the **demoted** safe-to-borrow card beside/below it, then a dense-but-calm grid of where-the-money-went buckets and per-employee spend. **The mandated edit:** the safe-to-borrow tile is **NOT** a co-equal filled-CTA hero — demote it to a **secondary card with a "why only €X?" chevron**, so the **only filled-accent element on Home is the center Scan/Pay action.** This keeps the home consistent with the inverted-flywheel north star (financing is never the front door; success = borrow less).

**Grafts (best-of from the runners-up):**
- **Verdict strip** (from Cash-Flow Story) at the very top — the plain-sentence <5s answer.
- **Per-client reliability tag** (from Cash-Flow Story) inside the safe-to-borrow "why €X?" disclosure — the closed-loop moat on the home.
- **The full narrative timeline + confidence cone** (Cash-Flow Story) lives one tap in, as the Financing/forecast surface and the "don't borrow" canvas.
- **Avoided-borrowing tally chip** (from One Decision Now) — the inverted-flywheel P&L on screen.
- **The polymorphic Decision Card + inline "Why now?"** (One Decision Now) reused verbatim inside the Financing/bridge request→grant steps; the "Human-reviewed" badge lives there and nowhere else.

### 6.3 Decisions, not screens — traceability
This spec is organized around the **decisions** the user (and the AI for her) makes, per the `02` method. The mapping that keeps every screen honest:

| Decision (HMW) | Surface | AI role | Human-loop |
|---|---|---|---|
| Are we financially healthy / how much runway? | Home | Predict | on |
| Can I afford this commitment over the runway? | Home forecast / Financing | Predict | on |
| Where did the money go (bucket/employee/SaaS)? | Transactions / SaaS lane | Generate | on |
| Is this recurring vendor worth it — cap or cancel? | SaaS & AI Spend | Recommend | in |
| Do I have safe headroom right now? | Financing (sizing) | Predict | **out** |
| Do we grant this specific loan, at these terms? | Loan Grant | Recommend | **in** (Annex III gate) |
| Is this invoice captured / pay or schedule? | Scan/Pay | Act | on |
| What can each card spend on / what's flagged? | Cards | Recommend | in |
| What do I owe / am owed / overdue? | Invoices AP/AR | Predict / Act | on |
| Do I need a CFO/legal/compliance partner now? | Services | Recommend | in |

**Every element on every screen traces to a row above. Orphans get killed.**

---

## 7. Open design questions
*(carried to the team — see the structured list in the deliverable; mirrors the still-open decisions in `00` §Decisions.)*

