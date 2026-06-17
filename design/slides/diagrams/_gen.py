#!/usr/bin/env python3
"""Generate the 11 NetBank deck diagrams as inline SVG, one shared visual language.

Run:  uv run --no-project python design/slides/diagrams/_gen.py
Out:  design/slides/diagrams/<name>.svg  (consumed by build_deck.py -> .evidence)

Every diagram draws with the theme classes in theme.css (.d-node, .d-edge, .d-label,
.d-tier--t0, etc.), so colours resolve from the dark-instrument-panel tokens and one
token re-themes the whole deck. viewBox is the design space; build_deck sizes the svg
to the slide's evidence area (preserveAspectRatio meet). The S7 charts are generated
from synthetic points whose trapezoidal AUC equals the labelled 0.91 / 0.78.

Authoring contract (docs/16): plain-English on the wall, the rigorous term one glance
away; ONE mint focal element per slide; honesty encoded in the visual (dashed/hatched/
red), never buried. Spine = one object (S3-5) · one loop (S6-7) · one objective (S8-9).
"""
import html
from pathlib import Path

OUT = Path(__file__).resolve().parent
W, H = 1120, 520           # standard design space


# ---------- svg primitives ----------
def esc(s): return html.escape(str(s), quote=True)


def T(x, y, s, cls="d-label", anchor="start", size=None):
    st = f' font-size="{size}"' if size else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{st}>{esc(s)}</text>'


def Tw(x, y, lines, cls="d-label", anchor="start", lh=22, size=None):
    st = f' font-size="{size}"' if size else ""
    out = [f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{st}>']
    for i, ln in enumerate(lines):
        dy = 0 if i == 0 else lh
        out.append(f'<tspan x="{x}" dy="{dy}">{esc(ln)}</tspan>')
    out.append("</text>")
    return "".join(out)


def R(x, y, w, h, cls="d-node", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>'


def L(x1, y1, x2, y2, cls="d-edge"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>'


def PATH(d, cls="d-edge"):
    return f'<path d="{d}" class="{cls}"/>'


def C(cx, cy, r, cls="d-node"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls}"/>'


def chip(x, y, w, h, label, cls="d-node", sub=None, tcls="d-label", lh=20):
    g = [R(x, y, w, h, cls)]
    cy = y + h / 2 + 6 if not sub else y + h / 2 - 4
    g.append(T(x + w / 2, cy, label, tcls, "middle"))
    if sub:
        g.append(T(x + w / 2, y + h / 2 + 18, sub, "d-sub", "middle"))
    return "".join(g)


def padlock(x, y, label=None, s=1.0):
    """small red human-gate padlock at (x,y) center — reserved for 'a human decides'."""
    bw, bh = 30 * s, 24 * s
    bx, by = x - bw / 2, y - bh / 2 + 6 * s
    shackle = (f'<path d="M {x-9*s} {by} v {-7*s} a {9*s} {9*s} 0 0 1 {18*s} 0 v {7*s}" '
               f'class="d-padlock" fill="none"/>')
    body = R(bx, by, bw, bh, "d-padlock", 5)
    out = [shackle, body]
    if label:
        out.append(T(x, y + 30 * s, label, "d-cap", "middle"))
    return "".join(out)


def clock(cx, cy, r=11):
    """hollow clock glyph — 'test not yet run' (kept distinct from the human-gate padlock)."""
    g = [C(cx, cy, r, "d-node--ghost")]
    g.append(L(cx, cy, cx, cy - r * 0.55, "d-axis"))      # minute hand
    g.append(L(cx, cy, cx + r * 0.45, cy + r * 0.1, "d-axis"))  # hour hand
    return "".join(g)


def svg(body, vb_w=W, vb_h=H):
    return (f'<svg viewBox="0 0 {vb_w} {vb_h}" preserveAspectRatio="xMidYMid meet" '
            f'xmlns="http://www.w3.org/2000/svg">\n{body}\n</svg>\n')


def write(name, body, vb_w=W, vb_h=H):
    (OUT / f"{name}.svg").write_text(svg(body, vb_w, vb_h), encoding="utf-8")
    print(f"  wrote {name}.svg")


# ============================================================ COVER
def cover():
    """One balance that lies -> three honest slices + the win-arrow OUT; plants the spine."""
    b = []
    b.append(R(60, 108, 160, 64, "d-node--ghost"))
    b.append(T(140, 138, "€ 23,400", "d-num", "middle", 22))
    b.append(T(140, 160, "one balance — it lies", "d-cap", "middle"))
    bands = [("mine", "d-node--mint"), ("the tax office's", "d-node--amber"), ("not here yet", "d-node--blue")]
    yy = 74
    for lab, cl in bands:
        b.append(PATH(f"M 224 140 C 282 140, 302 {yy+22}, 360 {yy+22}", "d-edge"))
        b.append(R(360, yy, 250, 44, cl))
        b.append(T(485, yy + 28, lab, "d-label", "middle"))
        yy += 64
    # inverted flywheel: the win-arrow points OUT of the app
    b.append(PATH("M 640 140 H 900", "d-edge--loop"))
    b.append(T(772, 122, "good month = you borrow LESS", "d-cap", "middle"))
    # plant the three-word spine
    b.append(T(560, 296, "one object   ·   one loop   ·   one objective", "d-title", "middle"))
    return write("cover", "".join(b), 1120, 320)


# ============================================================ S2 PROBLEM + WHY NOW
def problem_whynow():
    b = []
    # left: hero ~81d vs 60d bar
    b.append(T(60, 70, "Spanish firms get paid in", "d-sub"))
    b.append(T(60, 150, "~81", "hero-num-svg d-num", "start", 110))
    b.append(T(250, 150, "days", "d-label", "start", 34))
    b.append(T(60, 200, "vs a 60-day legal limit — 34% over (CEPYME 2025)", "d-cap"))
    bx, by, scale = 60, 250, 5.6
    b.append(R(bx, by, 60 * scale, 26, "d-node--ghost", 6))
    b.append(T(bx + 60 * scale + 10, by + 18, "60d legal", "d-cap"))
    b.append(R(bx, by + 38, 81 * scale, 26, "d-node--amber", 6))
    b.append(T(bx + 81 * scale + 10, by + 56, "~81d actual", "d-cap"))
    b.append(T(60, by + 120, "micro-firms = the MOST EXPOSED segment", "d-sub"))
    # right: 3-clock why-now rail — plain English titles, citations demoted to grey sub-text
    rx = 640
    b.append(T(rx, 60, "WHY NOW — THREE CLOCKS STRIKE", "d-title"))
    clocks = [
        ("1", "Invoice data goes public", "new e-invoicing law · Verifactu 2027 · SII", "d-node--blue"),
        ("2", "Rules for AI lending get written", "AI-Act §5(b) + GDPR Art. 22 · by 2 Dec 2027", "d-node--amber"),
        ("3", "Late payment hits a record", "and rising · micro-firms most exposed (CEPYME 2025)", "d-node--mint"),
    ]
    cy = 90
    for n, t, s, cl in clocks:
        b.append(C(rx + 26, cy + 42, 26, cl))
        b.append(T(rx + 26, cy + 50, n, "d-num", "middle", 22))
        b.append(T(rx + 72, cy + 34, t, "d-label"))
        b.append(T(rx + 72, cy + 62, s, "d-sub"))
        cy += 110
    b.append(T(rx + 72, cy + 8, "data · rules · pain peak together", "d-cap"))
    return write("problem-whynow", "".join(b))


# ============================================================ S3 VALUE / THREE TRUTHS (OBJECT)
def value_truths():
    b = []
    # left: one lying balance splits into 3 truths (the deck's clearest idea — untouched)
    b.append(T(60, 60, "ONE BALANCE THAT LIES", "d-title"))
    b.append(R(60, 86, 150, 64, "d-node--ghost"))
    b.append(T(135, 116, "€ 23,400", "d-num", "middle", 22))
    b.append(T(135, 138, "the single balance", "d-cap", "middle"))
    bands = [("mine", "d-node--mint"), ("the tax office's", "d-node--amber"), ("not here yet", "d-node--blue")]
    yy = 86
    for lab, cl in bands:
        b.append(PATH(f"M 215 118 C 260 118, 270 {yy+24}, 320 {yy+24}", "d-edge"))
        b.append(R(320, yy, 200, 44, cl))
        b.append(T(420, yy + 28, lab, "d-label", "middle"))
        yy += 60
    # right: a model of how each CLIENT pays (simplified — no false-precision %, no 'bridge €X')
    b.append(T(600, 60, "WE LEARN HOW EACH CLIENT PAYS", "d-title"))
    b.append(R(600, 86, 460, 80, "d-node--payer"))
    b.append(T(620, 118, "Client ACME", "d-label"))
    b.append(T(620, 144, "reliable (illustrative) → safe to advance €9k", "d-sub"))
    b.append(R(600, 184, 220, 64, "d-node--ghost"))
    b.append(T(620, 214, "Client B · erratic", "d-sub"))
    b.append(T(620, 236, "→ don't advance", "d-cap"))
    # the one mint focal element = the inverted-incentive lede
    b.append(R(840, 184, 220, 64, "d-node--mint"))
    b.append(T(950, 212, "cash is coming", "d-label", "middle"))
    b.append(T(950, 236, "→ don't borrow", "d-cap", "middle"))
    b.append(T(600, 300, "the honest branch: we win when you borrow less", "d-sub"))
    b.append(L(60, 360, 1060, 360, "d-grid"))
    b.append(T(60, 392, "the model sizes & warns — a human signs every loan", "d-cap"))
    return write("value-truths", "".join(b))


# ============================================================ S4 NETFLIX + APP (OBJECT, shipped)
def netflix_app():
    b = []
    # left: phone still (Command Center) — the 8 live screens
    px, py, pw, ph = 60, 40, 230, 440
    b.append(R(px, py, pw, ph, "d-node", 28))
    b.append(R(px + 16, py + 22, pw - 32, 40, "d-node--ghost", 8))
    b.append(T(px + 28, py + 47, "Command Center", "d-sub"))
    b.append(R(px + 16, py + 74, pw - 32, 70, "d-node--mint", 8))
    b.append(T(px + 28, py + 104, "safe runway", "d-cap"))
    b.append(T(px + 28, py + 130, "€ 12,400", "d-num", "start", 20))
    for i, lab in enumerate(["bridge €9k · ACME", "sweep to tax pot", "re-date a payment", "don't borrow ✓"]):
        yy = py + 160 + i * 56
        cls = "d-node--blue" if i == 0 else ("d-node--amber" if i == 2 else "d-node")
        b.append(R(px + 16, yy, pw - 32, 44, cls, 8))
        b.append(T(px + 28, yy + 28, lab, "d-sub"))
    b.append(T(px + pw / 2, py + ph + 28, "8 live screens — open them now", "d-cap", "middle"))
    # right: Netflix -> NetBank, the TWO load-bearing rows (the other 3 -> notes)
    lx, rx, top, rh = 360, 730, 150, 120
    b.append(T(lx + 130, 110, "NETFLIX", "d-title", "middle"))
    b.append(T(rx + 175, 110, "NETBANK", "d-title", "middle"))
    rows = [
        ("movies", "financial ACTIONS, not products", False),
        ("keep watching ↺", "the loop: each payment → a sharper next call", True),
    ]
    for i, (lft, rgt, hot) in enumerate(rows):
        yy = top + i * rh
        b.append(R(lx, yy, 260, 64, "d-node--ghost"))
        b.append(T(lx + 130, yy + 38, lft, "d-sub", "middle"))
        b.append(R(rx, yy, 350, 64, "d-node--mint" if hot else "d-node"))
        b.append(T(rx + 175, yy + 38, rgt, "d-label" if hot else "d-sub", "middle"))
        b.append(PATH(f"M {lx+260} {yy+32} H {rx}", "d-edge--loop" if hot else "d-edge"))
    b.append(T(rx + 175, top + 2 * rh + 14, "recommendation, not application — the win-arrow points OUT", "d-cap", "middle"))
    return write("netflix-app", "".join(b))


# ============================================================ S5 ONTOLOGY (OBJECT built right)
def ontology():
    b = []
    # plain-English band names; the rigorous term lives in notes
    bands = [("WHAT WE STORE", 60), ("THE BRAINS", 220), ("WHAT IT DOES", 360)]
    for lab, yy in bands:
        b.append(R(40, yy, 880, 120, "d-band"))
        b.append(T(56, yy + 26, lab, "d-title"))
    # objects row — Payer is the highlighted join
    objs = ["Customer", "Account", "Invoice", "Payer", "Goal", "Loan", "Decision"]
    ox = 70
    for o in objs:
        cls = "d-node--payer" if o == "Payer" else "d-node"
        b.append(chip(ox, 96, 112, 56, o, cls, tcls="d-sub"))
        ox += 122
    b.append(T(492, 174, "the join", "d-cap", "middle"))
    # the brains row — plain model names
    for i, p in enumerate(["predict late-pay", "forecast cash", "safe-to-borrow"]):
        b.append(chip(70 + i * 150, 256, 136, 52, p, "d-node--blue", tcls="d-sub"))
    b.append(chip(540, 256, 360, 52, "a human signs every loan — by law", "d-node--red", tcls="d-sub"))
    # what it does row — the agents (loop arrow lives on S6, removed here)
    b.append(chip(70, 396, 830, 52, "9 agents: intake → reliability → grant → servicing → repay", "d-node", tcls="d-sub"))
    # red dashed boundary slicing all bands — captioned at the line, not orphaned
    b.append(L(465, 50, 465, 446, "d-divider"))
    b.append(T(474, 64, "a boundary", "d-cap"))
    b.append(T(120, 500, "separate boxes = the model can't cheat, and we stay legal", "d-cap"))
    return write("ontology", "".join(b), 960, 520)


# ============================================================ S6 ROLE: RIGID -> LOOP (the turn)
def role_turn():
    b = []
    steps = ["Application", "Eligibility", "Risk", "Decision", "Outcome"]
    sx, sw, gap = 70, 170, 30
    # top: rigid pipeline (grey, straight, no path back)
    b.append(T(60, 50, "TODAY — rigid, one-shot", "d-title"))
    for i, s in enumerate(steps):
        x = sx + i * (sw + gap)
        b.append(chip(x, 74, sw, 56, s, "d-node--ghost", tcls="d-sub"))
        if i < len(steps) - 1:
            b.append(PATH(f"M {x+sw} 102 H {x+sw+gap}", "d-edge"))
    b.append(T(70, 168, "no path back · the bank throws away every realized outcome", "d-cap"))
    # bottom: same five as a learning loop. Neutral chips; the ONE mint element = the return arrow.
    b.append(T(60, 240, "NETBANK — a learning loop", "d-title"))
    ly = 280
    for i, s in enumerate(steps):
        x = sx + i * (sw + gap)
        cls = "d-node--red" if s == "Decision" else "d-node"
        b.append(chip(x, ly, sw, 56, s, cls, tcls="d-sub"))
        if i < len(steps) - 1:
            b.append(PATH(f"M {x+sw} {ly+28} H {x+sw+gap}", "d-edge"))
    # the one human gate, plain-language label
    dec_x = sx + 3 * (sw + gap) + sw / 2
    b.append(padlock(dec_x, ly - 18, "a human signs every loan — by law (EU)", 1.0))
    # the mint return arrow — the slide's single new idea
    out_x = sx + 4 * (sw + gap) + sw / 2
    risk_x = sx + 2 * (sw + gap) + sw / 2
    b.append(PATH(f"M {out_x} {ly+56} C {out_x} {ly+150}, {risk_x} {ly+150}, {risk_x} {ly+56}", "d-edge--loop"))
    b.append(T((out_x + risk_x) / 2, ly + 168, "every payment teaches the model", "d-cap", "middle"))
    b.append(T(70, 500, "a separate human runs the AML / identity check — AI sizes & warns, never grants", "d-cap"))
    return write("role-turn", "".join(b))


# ============================================================ S7 MODEL PROOF (LOOP, honest)
def _roc_points(target, n=80):
    """TPR = FPR**c, tune c so trapezoidal AUC == target."""
    def auc_of(c):
        xs = [i / n for i in range(n + 1)]
        ys = [x ** c for x in xs]
        return sum((xs[i + 1] - xs[i]) * (ys[i] + ys[i + 1]) / 2 for i in range(n))
    lo, hi = 0.001, 6.0           # AUC is DECREASING in c (auc≈1/(c+1))
    for _ in range(60):
        mid = (lo + hi) / 2
        if auc_of(mid) > target:   # auc too high -> need a LARGER c
            lo = mid
        else:
            hi = mid
    c = (lo + hi) / 2
    xs = [i / n for i in range(n + 1)]
    return [(x, x ** c) for x in xs], auc_of(c)


def model_proof():
    import math
    b = []
    # the banner the eye hits first — flips the "lower = worse" misread
    b.append(T(60, 32, "THE HONEST SCORE IS THE LOWER ONE — 0.78 · THE GAP = THE LEAKAGE WE DELETED", "d-title"))
    PW, PH = 470, 348
    ax, ay = 70, 92
    # ---- panel A: ROC ----
    b.append(T(ax, ay - 16, "ROC — naive vs payer-grouped", "d-title"))
    b.append(L(ax, ay, ax, ay + PH, "d-axis"))
    b.append(L(ax, ay + PH, ax + PW, ay + PH, "d-axis"))
    b.append(T(ax + PW / 2, ay + PH + 32, "false-positive rate", "d-cap", "middle"))
    b.append(f'<text x="{ax-44}" y="{ay+PH/2}" class="d-cap" text-anchor="middle" transform="rotate(-90 {ax-44} {ay+PH/2})">true-positive rate</text>')
    b.append(L(ax, ay + PH, ax + PW, ay, "d-ref"))

    def to_xy(px, py):
        return ax + px * PW, ay + PH - py * PH
    naive, auc_n = _roc_points(0.91)
    grouped, auc_g = _roc_points(0.78)
    top = " ".join(f"{x:.1f},{y:.1f}" for x, y in (to_xy(px, py) for px, py in naive))
    bot = " ".join(f"{x:.1f},{y:.1f}" for x, y in (to_xy(px, py) for px, py in reversed(grouped)))
    b.append(f'<polygon points="{top} {bot}" class="d-wedge"/>')

    def poly(pts, cls):
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in (to_xy(px, py) for px, py in pts))
        return PATH(d, cls)
    b.append(poly(naive, "d-curve d-curve--naive"))
    b.append(poly(grouped, "d-curve d-curve--grouped"))
    b.append(T(ax + PW - 6, ay + 66, f"naive {auc_n:.2f} — memorised the client", "d-cap", "end"))
    b.append(T(ax + PW - 6, ay + 150, f"payer-grouped {auc_g:.2f} — honest", "d-cap", "end"))
    b.append(Tw(ax + 96, ay + PH - 84, ["= the leakage we deleted", "(“leakage” = the model cheating)"], "d-cap", "start", 18))
    # ---- panel B: calibration ----
    bx, by = 640, 92
    b.append(T(bx, by - 16, "Calibration", "d-title"))
    b.append(L(bx, by, bx, by + PH, "d-axis"))
    b.append(L(bx, by + PH, bx + PW, by + PH, "d-axis"))
    b.append(T(bx + PW / 2, by + PH + 32, "predicted probability", "d-cap", "middle"))
    b.append(L(bx, by + PH, bx + PW, by, "d-ref"))
    b.append(T(bx + PW - 6, by + 22, "perfect", "d-cap", "end"))
    cal = []
    for i in range(21):
        x = i / 20
        y = min(1, max(0, x + 0.06 * math.sin(2 * math.pi * x)))
        cal.append((bx + x * PW, by + PH - y * PH))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in cal)
    b.append(PATH(d, "d-curve d-curve--calib"))
    b.append(Tw(bx + 26, by + 54, ["the model knows how", "sure it is — this prices", "the bridge"], "d-cap", "start", 18))
    # the synthetic chip, same visual weight as the numbers (centred under both panels)
    b.append(R(440, 484, 300, 30, "d-node--amber", 6))
    b.append(T(590, 504, "ILLUSTRATIVE · SYNTHETIC — proves the method", "d-cap", "middle"))
    return write("model-proof", "".join(b), 1180, 520)


# ============================================================ S8 MARKET + MODEL (OBJECTIVE pays)
def market_model():
    b = []
    # TAM hero + scale axes (rubric 7 stays on the wall)
    b.append(T(60, 70, "TAM", "d-title"))
    b.append(T(60, 150, "3.43M", "d-num", "start", 92))
    b.append(T(60, 188, "autónomos · Spain (Dec 2025)", "d-sub"))
    b.append(T(60, 220, "scales: autónomo→agency · Spain→EU · same-Payer network", "d-cap"))
    # GTM rail
    b.append(T(60, 280, "GO-TO-MARKET — CHANNELS OVER TIME", "d-title"))
    phases = [
        ("Phase 0", "Distress wedge", "Concurso/Watchtower · free public data"),
        ("Phase 1", "Gestoría channel", "cheapest in-ICP recruiting · density probe"),
        ("Phase 2+", "Services panel", "flat-fee · CAC + retention + cross-sell"),
    ]
    px = 60
    for i, (ph, t, s) in enumerate(phases):
        b.append(R(px, 304, 300, 78, "d-node" if i else "d-node--mint"))
        b.append(T(px + 16, 330, ph, "d-cap"))
        b.append(T(px + 16, 354, t, "d-label"))
        b.append(T(px + 16, 376, s, "d-sub"))
        if i < 2:
            b.append(PATH(f"M {px+300} 343 H {px+340}", "d-edge--loop"))
        px += 340
    # 3 pillars (right)
    b.append(T(720, 70, "THREE PILLARS · ONE OBJECTIVE", "d-title"))
    pillars = [("Tax-Sweep+", "revenue", "d-node--mint"), ("Concurso", "distress gate", "d-node--blue"), ("Bridge fee", "margin (paper)", "d-node--amber")]
    for i, (t, s, cl) in enumerate(pillars):
        x = 720 + i * 150
        b.append(R(x, 96, 130, 96, cl))
        b.append(T(x + 65, 138, t, "d-label", "middle"))
        b.append(T(x + 65, 164, s, "d-sub", "middle"))
    b.append(T(720, 232, "humans on grant only → target cost-to-income below CaixaBank 38.5%", "d-cap"))
    b.append(T(720, 254, "(38.5% = audited FY24 baseline · our ratio comes from the pilot)", "d-cap"))
    b.append(T(720, 276, "Concurso = public data — the moat is the gate wired into pricing, not the scrape", "d-cap"))
    return write("market-model", "".join(b), 1180, 420)


# ============================================================ S9 MOAT TIERS (OBJECTIVE)
def moat_tiers():
    b = []
    # left: small-multiple compare — one header replaces the repeated "copyable" tags
    b.append(T(60, 56, "THEY CAN COPY THE SCREENS…", "d-title"))
    rivals = [("ImaginBank", "interchange + funnel"), ("Nubank", "cost curve at scale"),
              ("Qonto", "free tax pot widget"), ("Factoring", "one-off advance")]
    yy = 84
    for r, s in rivals:
        b.append(R(60, yy, 420, 46, "d-node"))
        b.append(T(78, yy + 22, r, "d-label"))
        b.append(T(78, yy + 40, s, "d-sub"))
        yy += 56
    b.append(R(60, yy + 6, 420, 52, "d-node--mint"))
    b.append(T(78, yy + 28, "…not a bank that profits when you borrow less", "d-label"))
    b.append(T(78, yy + 48, "won't, not can't", "d-cap"))
    # right: 3-rung tier bar — self-describing labels, codenames off the wall
    b.append(T(620, 56, "WHAT'S HARD TO COPY — HONESTLY", "d-title"))
    tiers = [
        ("What we prove TODAY", "the Payer model + the leakage-clean method", "d-tier--t0"),
        ("What compounds LATER (worth ~0 today)", "the learning loop — not yet a moat", "d-tier--t1"),
        ("What they WON'T copy", "a bank that profits when you borrow less", "d-tier--t2"),
    ]
    yy = 100
    for title, sub, cl in tiers:
        b.append(R(620, yy, 70, 56, cl, 8))
        b.append(T(706, yy + 25, title, "d-label"))
        b.append(T(706, yy + 47, sub, "d-sub"))
        yy += 76
    b.append(T(620, yy + 16, "data is NOT the moat (Verifactu/SII) ·", "d-cap"))
    b.append(T(620, yy + 38, "cross-customer bureau = roadmap-only, 2 gates", "d-cap"))
    return write("moat-tiers", "".join(b))


# ============================================================ S10 VALIDATION RAIL
def validation_rail():
    b = []
    b.append(T(60, 56, "FOUR FALSIFIABLE TESTS — EACH PRE-SET TO KILL ITS OWN CLAIM", "d-title"))
    stations = [
        ("Leakage gap", ["DONE · 0.91 → 0.78"], "illustrative · synthetic", True),
        ("WTP test", ["enough pay €12 · authorize", "a real charge · beat free"],
         "fast & falsifiable — the cheapest answer your money buys", False),
        ("Concurso backtest", ["write-offs pre-flagged"], "median lead-time = weeks", False),
        ("Bridge paper-trade", ["fee 1–3% > loss + cost of money"], "per-Payer lift on a real cohort", False),
    ]
    x = 60
    sw, gap = 230, 30
    railY = 150
    b.append(L(60, railY + 40, 60 + 4 * sw + 3 * gap, railY + 40, "d-grid"))
    for i, (t, thr, sub, done) in enumerate(stations):
        cls = "d-node--mint" if done else "d-node"
        b.append(R(x, railY, sw, 130, cls))
        b.append(T(x + 16, railY + 28, t, "d-label"))
        b.append(Tw(x + 16, railY + 54, thr, "d-sub", "start", 18))
        b.append(T(x + 16, railY + 110, sub, "d-cap"))
        if done:
            b.append(T(x + sw - 16, railY + 28, "✓", "d-num", "end", 22))
        else:
            b.append(clock(x + sw - 24, railY + 24))
        if i < 3:
            b.append(PATH(f"M {x+sw} {railY+65} H {x+sw+gap}", "d-edge"))
        x += sw + gap
    # fenced-off illustrative band
    b.append(R(60, 330, 4 * sw + 3 * gap, 70, "d-node--ghost"))
    b.append(T(80, 360, "pipeline · design-partner gestorías · endorsers", "d-sub"))
    b.append(T(80, 384, "ILLUSTRATIVE · not yet measured — fenced off, no invented numbers", "d-cap"))
    b.append(T(60, 440, "we proved the SIGNAL, not the business — every other claim has a test it can fail", "d-cap"))
    return write("validation-rail", "".join(b), 1060, 470)


# ============================================================ S11 CLOSE BOARD
def close_board():
    b = []
    # team row — neutral rings (the reserved mint join-key ring is NOT for avatars)
    b.append(T(60, 56, "TEAM", "d-title"))
    names = ["Corrado", "Navid", "Manon", "Marti", "Rui", "Tim"]
    x = 60
    for n in names:
        b.append(C(x + 28, 110, 26, "d-node"))
        b.append(T(x + 28, 116, n[0], "d-num", "middle", 20))
        b.append(T(x + 28, 156, n, "d-cap", "middle"))
        x += 90
    b.append(C(x + 28, 110, 26, "d-edge--dash"))
    b.append(T(x + 28, 116, "+", "d-num", "middle", 22))
    b.append(Tw(x + 70, 104, ["credit-risk hire", "owns the grant"], "d-sub", "start", 18))
    # what AI changes / what stays human
    b.append(T(60, 220, "WHAT AI CHANGES", "d-title"))
    for i, t in enumerate(["balance → live data", "chasing late payers → helping, openly", "engagement → financial health"]):
        b.append(R(60, 244 + i * 56, 400, 44, "d-node--mint"))
        b.append(T(80, 272 + i * 56, t, "d-label"))
    b.append(T(540, 220, "WHAT STAYS HUMAN", "d-title"))
    b.append(R(540, 244, 360, 100, "d-node--red"))
    b.append(padlock(580, 282, None, 1.0))
    b.append(Tw(620, 270, ["a human always signs the loan", "— never the AI", "+ the empathy / restructure call"], "d-label", "start", 22))
    b.append(T(540, 372, "AI sizes · warns · orchestrates — never auto-grants", "d-cap"))
    # funding card — concrete, gate-tied, ILLUSTRATIVE kept
    b.append(T(940, 220, "THE ASK", "d-title"))
    b.append(R(940, 244, 180, 130, "d-node--amber"))
    b.append(Tw(956, 272, ["raise (ILLUSTRATIVE)", "to clear 3 gates:", "WTP · real-cohort", "lift · Concurso"], "d-sub", "start", 22))
    b.append(T(60, 432, "We win when you borrow less — judge the honesty, fund the gates. #1 weakness = WTP.", "d-cap"))
    return write("close-board", "".join(b), 1160, 470)


if __name__ == "__main__":
    print("generating diagrams…")
    cover(); problem_whynow(); value_truths(); netflix_app(); ontology()
    role_turn(); model_proof(); market_model(); moat_tiers(); validation_rail(); close_board()
    print("done.")
