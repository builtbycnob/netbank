# CLAUDE.md

> **Read this first.** Every agent or contributor starting any task in this repo must read this file before touching anything else.

## What this project is

NetBank (working name) is the cumulative project for the ESADE MIM course Data-Driven Prototyping with AI. It is an AI-native business neobank and embedded lender for VAT-registered Spanish micro-firms with late-paid B2B invoice income: autonomos, agencies, and bootstrapped revenue firms from solo to about 10 employees. Geography: Spain/EU first.

The core product insight: a single account balance lies to a freelancer. It conflates money that is hers, money owed to the tax office, and money booked but not yet arrived. NetBank resolves that with three live truths, a per-Payer reliability model, and a financial-health objective that wins when the customer borrows less.

The deck is a 22-slide oral defense covering all 8 rubric dimensions. See docs/09-final-deck.md for the master slide content and docs/15-task-tracker.md for the live task board.

Live prototype: https://builtbycnob.github.io/netbank/ (8 dark mobile screens)

---

## File map

### Root

| File | What it contains | When to read |
|------|-----------------|--------------|
| README.md | Project overview, architecture split, status checklist, repo structure notes | Always first - 2-minute orientation |
| index.html | Redirect to design/mockups/index.html | Only if debugging the GitHub Pages redirect |
| CLAUDE.md | This file - agent init, file map, locked decisions, update rules | Always, before anything else |

### docs/

| File | What it contains | When to read |
|------|-----------------|--------------|
| 00-product-definition.md | Original working brief from team kickoff | Background only - segment superseded by docs/11, do not cite VC-startup framing |
| 01-client-and-evidence.md | Chosen client, value proposition, all sourced numbers with URLs | Any task touching claims, numbers, or the customer segment |
| 02-mobile-experience.md | HMW questions, design principles, screen map, key UX decisions | Any design or UX task |
| 03-design-spec.md | Decision-driven screen specs and the hero flow | Detailed screen or interaction work |
| 04-slides-mobile-experience.md | Slide deck (mobile UX section) with speaker notes and professor Q&A | Deck or presentation prep |
| 05-predictive-ai.md | Predictive AI architecture: Payer-object, flywheel, per-Payer model | Any ML, AI, or underwriting task |
| 06-predictive-frontier.md | Data sources, external signals, registry events used as leading indicators | Data sourcing or signal-design tasks |
| 07-services-marketplace.md | Services marketplace design, pricing model, legal constraints on fee-sharing | Services tab, marketplace, or business-model tasks |
| 08-agentic-loan-journey.md | 9-agent agentic loan system; the collections thesis; drop-in slide | Any task on the Role of AI rubric dimension |
| 09-final-deck.md | Master deck - 22 slides, all 8 rubric dimensions, oral defense notes, master number-defense card | Any deck, presentation, or slide task. Contains the only blessed numbers |
| 10-value-ideas.md | Crazy-8s idea shortlist, pre-evaluation | Historical context only; read docs/11 for the decisions that followed |
| 11-team-ideas-evaluation.md | Locked segment and pillar decisions. 18 ideas scored; adopt/fold/defer/drop verdict | Any product-direction or strategy task. Supersedes docs/00 on the segment |
| 12-tax-sweep-wtp-test.md | Primary-research plan for willingness-to-pay validation on Tax-Sweep+ | WTP, pricing, or research tasks |
| 13-instructor-deck-alignment.md | Instructor sessions 7-8 sprint spine; gap queue G1-G8 | Checking whether the deck covers the professor rubric |
| 14-differentiation-and-roadmap.md | Adversarial stress-test on differentiation; product roadmap; what survives each attack | Any differentiation, moat, or roadmap task |
| 15-task-tracker.md | Live task board - claim, update, and complete tasks here | Every task. Update it when you start, change status, or finish |
| 16-deck-design-principles.md | Gold-standard slide-design contract (assertion-evidence, action titles, on-slide/notes split, inline-SVG system, glance gates), cited | Any deck/slide design or build task |
| 17-deck-rebuild-plan.md | Deck rebuild plan: pitch-spine running order (16 slides) × 8-rubric map, timing, per-slide spec, new-content list, build_deck.py/theme.css changes | Any deck rebuild, running-order, or NET-05 task |

### design/mockups/

| File | What it contains | When to read |
|------|-----------------|--------------|
| index.html | 8 dark mobile screens in HTML (3 home concepts A/B/C plus Financing, Transactions, Cards, Invoices/OCR, Services) | Any UI, mockup, or visual-design task |
| styles.css | Mockup stylesheet (Geist + Bricolage Grotesque, dark theme, Mercury-structured) | CSS or visual-polish tasks |
| image-briefs.json | Structured image-brief definitions for mockup assets | Mockup-generation or asset tasks |

---

## Locked decisions - do not drift from these

### Segment (locked in docs/11)

VAT-registered Spanish micro-firms with late-paid B2B invoice income: autonomos, agencies, bootstrapped revenue firms, solo to about 10 employees. VC-backed or capital-burning startups are explicitly excluded. If a suggestion re-introduces startup-CFO framing (burn rate as the core object, card-per-employee as the pitch, runway for a VC-funded team), flag it and refer back to docs/11.

### The three pillars (locked in docs/11)

1. Tax-Sweep+ - revenue pillar; auto set-aside of VAT/IRPF into a locked sub-account, one-tap gestor readiness pack. Never automated filing (regulated-advice perimeter).
2. Concurso Radar - moat and acquisition wedge; distress-registry gate wired into bridge pricing. Concede it is not defensible as a standalone scrape - its role is INTEGRATION DEPTH.
3. Bridge fee on a named receivable - margin pillar; presented as a paper-traded thesis, not a live book.

### Differentiation framing (locked in docs/14)

Differentiation is a system, not standalone features. Always state in three tiers:

- T0 (demonstrated today): Payer-as-object + payer-grouped CV methodology + regulatory architecture.
- T1 (compounding mechanism, not yet a present moat): the closed loop that retrains on realized payment dates.
- T2 (softer, incentive-conflict): the health objective - won't, not can't.

Never claim "only we see invoice data" - it is FALSE (Verifactu/SII make it commodity). Never cite the deferred cross-customer bureau as current differentiation. Never say "collections disappears" without qualifying it as disclosed, covenant-clean care.

### The only blessed numbers (from docs/09 master number-defense card)

- About 80.5 days (round to about 81 days on slides) average payment period, 2025, vs 60-day legal limit - CEPYME. Do NOT use ">85 days" unless clearly labeled as a mid-2025 micro spot.
- 3,425,767 autonomos in Spain, Dec 2025 - round to 3.43M on slides.
- Qonto 9 / 19 / 39 EUR/mo subscription tiers.
- CaixaBank 38.5% cost-to-income, audited FY24.
- Factoring 1-3% loss band vs 5.4% unsecured consumer NPL (EBA Jun 2025).
- Nubank approx $0.80/cust-mo, WeBank approx 118k cust/employee - digital-native ceiling, NOT peer benchmarks.
- Annex III section 5(b) = credit-scoring high-risk; GDPR Art. 22 = restricts solely-automated adverse decisions; Annex III phases in by 2 Dec 2027.

---

## How to do any task

1. Read this file first.
2. Check docs/15-task-tracker.md - claim the task (set owner, started date, status In progress).
3. Read the relevant docs from the file map above - use the "When to read" column.
4. Do the work. Defend every number you use. Tag anything unverified as [to validate].
5. Update docs/15-task-tracker.md when done (status Done, completed date, final note naming the deliverable).
6. If you add a new file, update CLAUDE.md - add a row to the correct file map section. Keep the description to one line.

---

## How to keep this file current

- New file added to the repo: add a row to the file map table in the correct section.
- New locked decision: add it to the Locked decisions section with a reference to where it was established.
- Blessed number changes: update the number-defense list with the new figure, source, and date.
- Keep entries concise. Every file map row must have a one-line description and a When to read note.
- Target length: under 200 lines. If it grows beyond that, move detail into the referenced doc and link from here.

---

## Team

ESADE MIM cohort - Corrado, Navid, Rui, Marti.
Course: Data-Driven Prototyping with AI.
This repo is public - do not commit the course syllabus or any confidential material.