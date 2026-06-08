# 00 — Product Definition *(working brief, from team discussion 2026-06-08)*

> Captured from the team's voice discussion. **Not locked** — open to change. This is the source-of-truth the design works from.

## What we're building

A **data-driven business neobank + embedded lender** for **freelancers, agencies, and bootstrapped startups** — from a **solo freelancer up to a 2–10-employee company**, small **cash-flow-positive** businesses (**~€10k–€1M revenue**) that have real revenue but **lack fast, flexible, intelligent financing**. **Geography: Spain / EU first.**

**Inspiration:** **Mercury** (the dashboard, the calm/structured business-banking experience) + **WeBank / MyBank** (live-data underwriting and financial inclusion at near-zero decision cost). Visual baseline: **Stripe + Revolut**, **dark**, professional.

## The core loop (the moat)

```
more embedded product → better data → better underwriting →
safer loans → better customer outcomes → more trust → more data
```

We sit inside the customer's financial operations — bank accounts, accounting, payment processors, invoices, payroll, SaaS / AI-cloud spend — to assess financial health, predict repayment ability, calculate **safe borrowing capacity**, and offer **small flexible loans** better and faster than a traditional bank.

## What the product combines

1. **Business banking** — multiple accounts, **a card per employee** (Revolut-style), payments.
2. **Expense intelligence** — spend **per bucket** (operations, marketing…), **per employee**, and a clean view of **SaaS / AI spend** (Claude, OpenAI tokens, etc.), heavily filterable.
3. **Invoicing (AP/AR) with OCR** — scan an invoice with the phone → auto-recognized, categorized, and placed.
4. **Live cash-flow & financial health** — total cash, **burn rate**, revenue trajectory, runway.
5. **Financing (the core)** — **safe-borrowing-capacity** + flexible loans, underwritten on live data, with **CFO-style guidance**.
6. **Additional Services marketplace** — book external **CFO, legal, compliance** partners over the platform (a search-bar tab).
7. **Ongoing monitoring** — continuously reduce default risk and raise limits as trust/data grow.

## Design direction

- **Dark, professional.** Stripe/Revolut polish, **Mercury's structure** (Mercury's app has only **4 clean bottom tabs** — very legible).
- **UI/UX is the #1 priority.** As **few clicks as possible** per task; very intuitive — the *Apple-of-banking* principle (hide complexity behind sensible defaults).
- Data-dense but never cluttered: clean, minimal, strong hierarchy, good filters.

### Proposed bottom navigation (Mercury-style, 4–5 tabs — to finalize)
`Home` · `Transactions` · `Invoices & Payments` · `Financing` · `Services`
*(Mercury uses 4 — we may merge Financing into Home as a hero card and keep Cards/Accounts inside Home. The design workflow will test options.)*

### Screen list (v1)
- **Home / dashboard** — total cash, burn rate, runway, spend-per-bucket, spend-per-employee, revenue trajectory, **"safe to borrow: €X"** hero, multiple accounts.
- **Accounts & Cards** — multi-account, card-per-employee, limits.
- **Transactions** — clean, filterable; SaaS/AI-spend view separated.
- **Invoices & Payments** — OCR scan, AP/AR, pay/schedule.
- **Financing** — safe-borrowing capacity, request/manage a flexible loan, repayment, CFO guidance (human-on-the-loop on the credit decision).
- **Services** — marketplace search: CFO / legal / compliance partners.

## How this evolves the earlier converged client

| Earlier (evidence pass) | Now |
|---|---|
| Solo *autónomo* with lumpy invoice income | **Freelancer = the small end**; **agencies + bootstrapped <10-employee companies = the core** |
| Invoice **bridge** as the one paid product | **Financing is THE core product** (business loans), embedded-lender model |
| "The balance lies / three truths / tax-sweep" | Reframed to **business cash-flow: runway, burn, where the cash goes, safe-to-borrow** |
| Calm/light, anti-engagement | **Dark, professional** (Stripe/Revolut/Mercury); "few clicks" intuitiveness still the principle |

**Still holds:** financial-health objective (not fee/engagement extraction); **non-credit autonomous core + human-on-the-loop on the credit decision** (EU AI Act Annex III); the WeBank/MyBank cost-economics case; the underserved-but-real-revenue target.

## Decisions

**Confirmed (2026-06-08)**
- ✅ **Segment:** solo freelancer **up to 2–10 employees** (both ends in scope; multi-seat/cards matter for the 2–10 tier).
- ✅ **Geography:** **Spain / EU first.**
- ✅ **Differentiation:** the underserved-but-real-revenue / embedded-lender angle is good — **keep exploring additional differentiators** (the design recon will surface more).

**Still open**
- **Final bottom-nav tabs** (4 vs 5; is Financing its own tab or a Home hero?).
- **Name** — "NetBank" is a placeholder.
- **Lender licensing** — hold a credit licence vs originate-and-refer to a partner (changes risk & margin).
