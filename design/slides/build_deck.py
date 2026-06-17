#!/usr/bin/env python3
"""Build the NetBank reveal.js deck from docs/09-final-deck.md (single source of truth).

Run:  uv run --no-project python design/slides/build_deck.py [--strict]
Out:  design/slides/index.html

Gold-standard rebuild (see docs/16 + docs/17). The deck is ASSERTION-EVIDENCE:
each spoken slide shows ONE action-title assertion + ONE inline-SVG visual + <=3
labels; ALL prose / numbers / DEFENSE Q&A move to <aside class="notes">. The
spoken running order, per-slide assertion, diagram name, rubric kicker and labels
come from the "## Presentation manifest" table in docs/09. Slides not in the
manifest become appendix/backup slides (reachable only if the professor grills).

- Diagrams: design/slides/diagrams/<name>.svg, inlined into .evidence and wrapped
  for a11y (role=img + <title>=assertion + <desc>=spoken line). Missing svg -> a
  visible placeholder so the build never blocks the author.
- The fit() scale hack is GONE: slides are authored to the fixed 1280x840 canvas;
  overflow is an authoring error (move prose to notes), never a scale-down.
- Glance gates (no <li>/<table> on stage, assertion 8-14 words, <=3 labels) print
  warnings; pass --strict to make them fatal.
- Fonts self-host from ./fonts/fonts.css if present, else fall back to the CDN.
- Print/leave-behind: vendor/pdf.css is linked for ?print-pdf when present.
"""
import html
import re
import sys
from pathlib import Path

STRICT = "--strict" in sys.argv
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SRC = ROOT / "docs" / "09-final-deck.md"
OUT = HERE / "index.html"
DGM = HERE / "diagrams"
WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)


# ---------- inline markdown ----------
def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"==(.+?)==", r'<span class="hi">\1</span>', s)   # ==mint phrase==
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\s][^*]*?)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s


def strip_md(s: str) -> str:
    """plain text (for word counts / a11y desc)."""
    s = re.sub(r"[=*`]+", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.strip()


def word_count(s: str) -> int:
    # count real words; ignore standalone punctuation tokens (— · → ; etc.)
    return len([t for t in strip_md(s).split() if any(c.isalnum() for c in t)])


def render_table(rows: list[str]) -> str:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head, body = cells[0], cells[2:]
    th = "".join(f"<th>{inline(c)}</th>" for c in head)
    out = [f"<table><thead><tr>{th}</tr></thead><tbody>"]
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def render_body(lines: list[str]) -> str:
    """Ordered render of bullets and tables (used for appendix + notes prose)."""
    parts, ul, tbl = [], [], []

    def flush_ul():
        if ul:
            parts.append("<ul>" + "".join(f"<li>{inline(b)}</li>" for b in ul) + "</ul>")
            ul.clear()

    def flush_tbl():
        if tbl:
            parts.append(render_table(tbl))
            tbl.clear()

    for ln in lines:
        s = ln.rstrip()
        if s.startswith("|"):
            flush_ul(); tbl.append(s)
        elif s.startswith("- "):
            flush_tbl(); ul.append(s[2:])
        elif not s.strip():
            continue
        else:
            flush_ul(); flush_tbl(); parts.append(f"<p class='lead'>{inline(s)}</p>")
    flush_ul(); flush_tbl()
    return "\n".join(parts)


# ---------- parse docs/09 ----------
text = SRC.read_text(encoding="utf-8")
hdr = re.compile(r"(?m)^## Slide (\d+) — (.+)$")
matches = list(hdr.finditer(text))
preamble = text[: matches[0].start()]
tail = text[matches[-1].start():]
all_h = [mm.start() for mm in re.finditer(r"(?m)^## ", text)]   # any ## section header

slides: dict[int, dict] = {}
for i, m in enumerate(matches):
    num, title = int(m.group(1)), m.group(2).strip()
    nexts = [p for p in all_h if p > m.start()]          # bound the block at the NEXT ## header
    end = min(nexts) if nexts else len(text)             # (slide OR manifest/appendix) — no swallow
    block = text[m.start(): end]
    body_lines, visual, notes, defenses = [], None, None, []
    assertion, diagram, labels, rubric = None, None, [], None
    cur_q, state = None, "body"
    for ln in block.splitlines()[1:]:
        st = ln.strip()
        if st.startswith("ASSERTION:"):
            assertion = st[len("ASSERTION:"):].strip(); state = "post"
        elif st.startswith("{DIAGRAM:") or st.startswith("{CHART:"):
            diagram = re.sub(r"^\{(DIAGRAM|CHART):\s*", "", st).rstrip("}").strip(); state = "post"
        elif st.startswith("LABELS:"):
            labels = [x.strip() for x in st[len("LABELS:"):].split(";") if x.strip()]
        elif st.startswith("RUBRIC-KICKER:"):
            rubric = st[len("RUBRIC-KICKER:"):].strip()
        elif st.startswith("[VISUAL:"):
            mv = re.match(r"\[VISUAL:\s*(.*)\]\s*$", st)
            visual = mv.group(1) if mv else st[8:].rstrip("]"); state = "post"
        elif st.startswith("**SPEAKER NOTES:**"):
            notes = st[len("**SPEAKER NOTES:**"):].strip(); state = "notes"
        elif st.startswith("**DEFENSE"):
            cur_q = re.sub(r"^\*\*DEFENSE\s*—\s*", "", st).rstrip("*").strip(); state = "defense"
        elif st.startswith("A:") and cur_q is not None:
            defenses.append((cur_q, st[2:].strip())); cur_q = None
        elif st == "---":
            continue
        elif state == "body":
            body_lines.append(ln)
        elif state == "notes" and st:
            notes = (notes + " " + st).strip() if notes else st
    slides[num] = dict(num=num, title=title, body=body_lines, visual=visual,
                       notes=notes, defenses=defenses, assertion=assertion,
                       diagram=diagram, labels=labels, rubric=rubric)

# rubric-coverage table + master number card + oral-defense appendix
rub = re.search(r"## Rubric-coverage map\s*\n(.*?)\n\n", preamble, re.S)
rubric_rows = [l for l in rub.group(1).splitlines() if l.strip().startswith("|")] if rub else []
card = re.search(r"## Master number-defense card.*?\n(.*?)\n\n---", preamble, re.S)
card_lines = [l for l in card.group(1).splitlines() if l.strip().startswith("- ")] if card else []
oda = re.search(r"## Oral-defense appendix.*?\n(.*)$", tail, re.S)
oda_rows = [l for l in oda.group(1).splitlines() if l.strip().startswith("|")] if oda else []

# presentation manifest: | Slide | Sources | Diagram | Kicker | Assertion | Labels |
manifest = []
mblock = re.search(r"## Presentation manifest\s*\n(.*?)(?:\n## |\n---|\Z)", text, re.S)
if mblock:
    rows = [l for l in mblock.group(1).splitlines() if l.strip().startswith("|")]
    for r in rows[2:]:  # skip header + separator
        c = [x.strip() for x in r.strip().strip("|").split("|")]
        if len(c) < 5 or not c[0].isdigit():
            continue
        srcs = [int(x) for x in re.findall(r"\d+", c[1])]
        labs = [x.strip() for x in c[5].split(";") if x.strip()] if len(c) > 5 else []
        manifest.append(dict(pos=int(c[0]), sources=srcs, diagram=c[2] or None,
                             kicker=c[3], assertion=c[4], labels=labs))


# ---------- render helpers ----------
def notes_block(srcs: list[int]) -> str:
    narr, defs = [], []
    for n in srcs:
        s = slides.get(n)
        if not s:
            continue
        if s["notes"]:
            narr.append(s["notes"])
        defs.extend(s["defenses"])
    if not narr and not defs:
        return ""
    out = ['<aside class="notes">']
    if narr:
        out.append('<div class="n-narration"><b>NARRATION</b>')
        out += [f"<p>{inline(p)}</p>" for p in narr]
        out.append("</div>")
    if defs:
        out.append('<div class="n-defense"><b>DEFENSE</b>')
        out += [f"<p><strong>{inline(q)}</strong><br>{inline(a)}</p>" for q, a in defs]
        out.append("</div>")
    out.append("</aside>")
    return "\n".join(out)


def diagram_svg(name: str | None, assertion_txt: str) -> str:
    if not name:
        return ('<div class="evidence"><div class="dgm-missing">'
                '<span>no diagram named</span></div></div>')
    f = DGM / f"{name}.svg"
    if not f.exists():
        warn(f"diagram missing: diagrams/{name}.svg")
        return (f'<div class="evidence"><div class="dgm-missing">'
                f'<span>◆ diagram: {html.escape(name)}.svg</span>'
                f'<small>{html.escape(strip_md(assertion_txt))}</small></div></div>')
    raw = f.read_text(encoding="utf-8")
    # ensure the <svg> is a11y-labelled and uses viewBox-driven sizing
    if "role=" not in raw[:400]:
        desc = html.escape(strip_md(assertion_txt))
        raw = re.sub(r"<svg\b",
                     f'<svg role="img" aria-label="{desc}"', raw, count=1)
    return f'<div class="evidence dgm">{raw}</div>'


def stage_section(item: dict) -> str:
    pos, srcs = item["pos"], item["sources"]
    assertion = item["assertion"] or (slides.get(srcs[0], {}).get("assertion") if srcs else "") or ""
    diagram = item["diagram"] or (slides.get(srcs[0], {}).get("diagram") if srcs else None)
    kicker = item["kicker"] or ""
    labels = item["labels"] or (slides.get(srcs[0], {}).get("labels", []) if srcs else [])
    # glance gates
    wc = word_count(assertion)
    if assertion and not (8 <= wc <= 14):
        warn(f"slide {pos}: assertion is {wc} words (want 8-14): “{strip_md(assertion)[:70]}…”")
    if len(labels) > 3:
        warn(f"slide {pos}: {len(labels)} on-stage labels (max 3)")
    if not assertion:
        warn(f"slide {pos}: no assertion")
    kick = f'<span class="kicker">{inline(kicker)}</span>' if kicker else ""
    labs = ("<ul class='labels'>" + "".join(f"<li>{inline(x)}</li>" for x in labels) + "</ul>") if labels else ""
    return (f'<section class="stage" data-slide="{pos}">\n'
            f'  <div class="shead">{kick}<h2 class="assertion">{inline(assertion)}</h2></div>\n'
            f'  {diagram_svg(diagram, assertion)}\n'
            f'  {labs}\n'
            f'  {notes_block(srcs)}\n'
            f'</section>')


# ---------- assemble sections ----------
sections = []
used = set()

# cover = slide 1 (special)
if manifest and manifest[0]["pos"] == 1:
    cover = manifest[0]
    used.update(cover["sources"])
    s1 = slides.get(cover["sources"][0], {}) if cover["sources"] else {}
    h1 = cover["assertion"] or "NetBank"
    if "—" in h1:
        pre, post = h1.split("—", 1)
        h1html = f"{inline(pre.strip())} — <em>{inline(post.strip())}</em>"
    else:
        h1html = inline(h1)
    sub = "".join(f"<p class='sub'>{inline(b[2:])}</p>" for b in s1.get("body", [])
                  if b.strip().startswith("- "))
    sections.append(f"""<section class="cover" data-slide="1">
  <div class="brand"><div class="mark">N</div><b>NetBank</b><span>ESADE MIM · Data-Driven Prototyping with AI</span></div>
  <h1>{h1html}</h1>
  {diagram_svg(cover['diagram'], h1) if cover['diagram'] else ""}
  <div class="meta"><span class="pill">business neobank + embedded lender</span><span class="pill">autónomos &amp; agencies · Spain/EU</span></div>
  {notes_block(cover['sources'])}
</section>""")
    spoken = manifest[1:]
else:
    spoken = manifest

# spoken slides 2..N
for item in spoken:
    used.update(item["sources"])
    sections.append(stage_section(item))

n_spoken = len(manifest) if manifest else 0

# ----- appendix -----
# coverage map
if rubric_rows:
    sections.append(f"""<section class="appendix" data-slide="appx-map">
  <div class="eyebrow">Appendix · rubric coverage</div>
  <h2>Eight rubric dimensions, one running order</h2>
  <div class="slide-body">{render_table(rubric_rows)}</div>
</section>""")

# unused source slides -> backup slides (full detail, reference)
for n in sorted(slides):
    if n in used:
        continue
    s = slides[n]
    sections.append(f"""<section class="appendix" data-slide="bk-{n}">
  <div class="eyebrow">Backup · source slide {n}</div>
  <h2>{inline(s['title'])}</h2>
  <div class="slide-body">{render_body(s['body'])}</div>
  {notes_block([n])}
</section>""")

# number card
if card_lines:
    body = "<ul>" + "".join(f"<li>{inline(b[2:])}</li>" for b in card_lines) + "</ul>"
    sections.append(f"""<section class="appendix" data-slide="appx-numbers">
  <div class="eyebrow">Appendix · oral reference</div>
  <h2>Master number-defense card — the only blessed numbers</h2>
  <div class="slide-body">{body}</div>
</section>""")

# oral-defense soft spots
if oda_rows:
    sections.append(f"""<section class="appendix" data-slide="appx-defense">
  <div class="eyebrow">Appendix · oral reference</div>
  <h2>Known soft spots — the crisp answer</h2>
  <div class="slide-body">{render_table(oda_rows)}</div>
</section>""")

# ---------- shared svg defs (arrow markers + hatch) ----------
DEFS = """<svg class="dgm-defs" aria-hidden="true" focusable="false"><defs>
<marker id="ah-mint" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#7FE7A6"/></marker>
<marker id="ah-grey" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#5E6772"/></marker>
<marker id="ah-red" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#FF8585"/></marker>
<pattern id="hatch-mint" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="7" stroke="#7FE7A6" stroke-width="2.4"/></pattern>
</defs></svg>"""

# ---------- fonts + print stylesheet ----------
_local_fonts = HERE / "fonts" / "fonts.css"
if _local_fonts.exists():
    font_link = '<link rel="stylesheet" href="fonts/fonts.css?v=VER">'
else:
    font_link = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
                 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                 '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Geist:wght@400..700&family=Geist+Mono:wght@400..600&display=swap" rel="stylesheet">')
    warn("fonts/fonts.css not found — using Google Fonts CDN (offline hole). Run the font-vendoring step.")
# reveal.js 5.x bundles print styles into reveal.css + PrintView in the core, so
# no separate pdf.css is needed; ?print-pdf is offline-safe with the vendored files.

# ---------- assemble document ----------
ver = format(int(max(SRC.stat().st_mtime, Path(__file__).stat().st_mtime,
                     (HERE / "theme.css").stat().st_mtime)), "x")
font_link = font_link.replace("VER", ver)

html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NetBank — Final Deck</title>
{font_link}
<link rel="stylesheet" href="vendor/reveal.css?v={ver}">
<link rel="stylesheet" href="theme.css?v={ver}">
</head>
<body>
{DEFS}
<div class="reveal"><div class="slides">
{chr(10).join(sections)}
</div></div>
<script src="vendor/reveal.js?v={ver}"></script>
<script src="vendor/notes/notes.js?v={ver}"></script>
<script>
Reveal.initialize({{
  width:1280, height:840, margin:0.04, minScale:1, maxScale:1,
  center:false, hash:true, slideNumber:'c/t', progress:true, transition:'fade',
  autoAnimateDuration:0.7, autoAnimateEasing:'cubic-bezier(.25,.1,.25,1)',
  pdfSeparateFragments:false, pdfMaxPagesPerSlide:1, showNotes:false,
  plugins:[RevealNotes]
}});
</script>
</body>
</html>
"""
OUT.write_text(html_doc, encoding="utf-8")

# ---------- report ----------
print(f"wrote {OUT.relative_to(ROOT)}  ({len(sections)} sections, {OUT.stat().st_size} bytes)")
print(f"  spoken slides: {n_spoken} (manifest) · appendix/backup: {len(sections) - n_spoken}")
if WARNINGS:
    print(f"\n⚠ {len(WARNINGS)} glance/build warnings:")
    for w in WARNINGS:
        print(f"  - {w}")
    if STRICT:
        sys.exit(f"\n--strict: failing on {len(WARNINGS)} warning(s)")
else:
    print("  ✓ no glance/build warnings")
