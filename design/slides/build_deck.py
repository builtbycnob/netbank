#!/usr/bin/env python3
"""Build the NetBank reveal.js deck from docs/09-final-deck.md (single source of truth).

Run:  uv run --no-project python design/slides/build_deck.py
Out:  design/slides/index.html   (links vendor/reveal.* + theme.css + Google Fonts)

Per slide: title + bullets + tables render on the slide; the [VISUAL: ...] brief is a
collapsed <details> (designer-facing) and also goes into the presenter notes; SPEAKER
NOTES + DEFENSE Q/A become reveal speaker notes (press 'S'). Cover = Slide 1; a coverage
slide is built from the rubric map; the master number-card + oral-defense appendix become
appendix slides at the end.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "docs" / "09-final-deck.md"
OUT = Path(__file__).resolve().parent / "index.html"


# ---------- inline markdown ----------
def inline(s: str) -> str:
    s = html.escape(s, quote=False)            # & < >  (content has <10, >30d, P&L, etc.)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)   # bold (may wrap inner *italic*)
    s = re.sub(r"(?<!\*)\*([^*\s][^*]*?)\*(?!\*)", r"<em>\1</em>", s)  # remaining single-* italics
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)   # [text](url) -> text (drop doc links)
    return s


def render_table(rows: list[str]) -> str:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head, body = cells[0], cells[2:]            # row 1 = header, row 2 = |---| separator
    th = "".join(f"<th>{inline(c)}</th>" for c in head)
    out = [f"<table><thead><tr>{th}</tr></thead><tbody>"]
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def render_body(lines: list[str]) -> str:
    """Ordered render of bullets and tables as they appear."""
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
            flush_ul()
            tbl.append(s)
        elif s.startswith("- "):
            flush_tbl()
            ul.append(s[2:])
        elif not s.strip():
            continue
        else:                                    # stray prose line -> its own bullet-less para
            flush_ul()
            flush_tbl()
            parts.append(f"<p class='lead'>{inline(s)}</p>")
    flush_ul()
    flush_tbl()
    return "\n".join(parts)


# ---------- parse docs/09 ----------
text = SRC.read_text(encoding="utf-8")
hdr = re.compile(r"(?m)^## Slide (\d+) — (.+)$")
matches = list(hdr.finditer(text))
preamble = text[: matches[0].start()]
tail = text[matches[-1].start():]

slides = []
for i, m in enumerate(matches):
    num, title = int(m.group(1)), m.group(2).strip()
    end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
    block = text[m.start(): end]
    body_lines, visual, notes, defenses = [], None, None, []
    cur_q = None
    state = "body"
    for ln in block.splitlines()[1:]:
        st = ln.strip()
        if st.startswith("[VISUAL:"):
            mv = re.match(r"\[VISUAL:\s*(.*)\]\s*$", st)
            visual = mv.group(1) if mv else st[8:].rstrip("]")
            state = "post"
        elif st.startswith("**SPEAKER NOTES:**"):
            notes = st[len("**SPEAKER NOTES:**"):].strip()
            state = "notes"
        elif st.startswith("**DEFENSE"):
            q = re.sub(r"^\*\*DEFENSE\s*—\s*", "", st).rstrip("*").strip()
            cur_q = q
            state = "defense"
        elif st.startswith("A:") and cur_q is not None:
            defenses.append((cur_q, st[2:].strip()))
            cur_q = None
        elif st == "---":
            continue
        elif state == "body":
            body_lines.append(ln)
        elif state == "notes" and st:
            notes = (notes + " " + st).strip() if notes else st
    slides.append(dict(num=num, title=title, body=body_lines, visual=visual,
                       notes=notes, defenses=defenses))

# rubric-coverage table from preamble
rub = re.search(r"## Rubric-coverage map\s*\n(.*?)\n\n", preamble, re.S)
rubric_rows = [l for l in rub.group(1).splitlines() if l.strip().startswith("|")] if rub else []
run = re.search(r"\*\*Running order:\*\*\s*(.+)", preamble)
running = run.group(1).strip() if run else ""

# master number-defense card bullets
card = re.search(r"## Master number-defense card.*?\n(.*?)\n\n---", preamble, re.S)
card_lines = [l for l in card.group(1).splitlines() if l.strip().startswith("- ")] if card else []

# oral-defense appendix table from tail
oda = re.search(r"## Oral-defense appendix.*?\n(.*)$", tail, re.S)
oda_rows = [l for l in oda.group(1).splitlines() if l.strip().startswith("|")] if oda else []


# ---------- render sections ----------
def notes_block(s):
    if not s["notes"] and not s["defenses"]:
        return ""
    out = ['<aside class="notes">']
    if s["notes"]:
        out.append(f"<p>{inline(s['notes'])}</p>")
    if s["visual"]:
        out.append(f"<p><strong>VISUAL:</strong> {inline(s['visual'])}</p>")
    for q, a in s["defenses"]:
        out.append(f"<p><strong>{inline(q)}</strong><br>{inline(a)}</p>")
    out.append("</aside>")
    return "\n".join(out)


def visual_details(s):
    if not s["visual"]:
        return ""
    return (f'<details class="visual"><summary>visual direction</summary>'
            f"<p>{inline(s['visual'])}</p></details>")


sections = []

# cover = Slide 1
s1 = slides[0]
cover_bullets = [b[2:] for b in s1["body"] if b.strip().startswith("- ")]
cover_title = re.sub(r"^\*\*|\*\*$", "", cover_bullets[0]).strip() if cover_bullets else "NetBank"
# split "NetBank — your bank reads your invoices, not your balance."
if "—" in cover_title:
    pre, post = cover_title.split("—", 1)
    cover_h1 = f"{inline(pre.strip())} — <em>{inline(post.strip())}</em>"
else:
    cover_h1 = inline(cover_title)
cover_sub = "".join(f"<p class='sub'>{inline(b)}</p>" for b in cover_bullets[1:])
sections.append(f"""<section class="cover" data-slide="1">
  <div class="brand"><div class="mark">N</div><b>NetBank</b><span>ESADE MIM · Data-Driven Prototyping with AI</span></div>
  <h1>{cover_h1}</h1>
  {cover_sub}
  <div class="meta"><span class="pill">22 slides</span><span class="pill">business neobank + embedded lender</span><span class="pill">autónomos &amp; agencies · Spain/EU</span></div>
  {notes_block(s1)}
</section>""")

# coverage map slide
if rubric_rows:
    sections.append(f"""<section class="appendix" data-slide="map">
  <div class="eyebrow">Coverage</div>
  <h2>Eight rubric dimensions, one running order</h2>
  <div class="slide-body"><div class="fit">{render_table(rubric_rows)}
  <p class="lead" style="margin-top:14px">{inline(running)}</p></div></div>
</section>""")

# content slides 2..22
for s in slides[1:]:
    sections.append(f"""<section data-slide="{s['num']}">
  <div class="slide-head"><span class="num">{s['num']} / 22</span><h2>{inline(s['title'])}</h2></div>
  <div class="slide-body"><div class="fit">{render_body(s['body'])}</div></div>
  {visual_details(s)}
  {notes_block(s)}
</section>""")

# appendix: master number card
if card_lines:
    body = "<ul>" + "".join(f"<li>{inline(b[2:])}</li>" for b in card_lines) + "</ul>"
    sections.append(f"""<section class="appendix" data-slide="appx-A">
  <div class="eyebrow">Appendix A · oral reference</div>
  <h2>Master number-defense card — the only blessed numbers</h2>
  <div class="slide-body"><div class="fit">{body}</div></div>
</section>""")

# appendix: oral-defense
if oda_rows:
    sections.append(f"""<section class="appendix" data-slide="appx-B">
  <div class="eyebrow">Appendix B · oral reference</div>
  <h2>Known soft spots — the crisp answer</h2>
  <div class="slide-body"><div class="fit">{render_table(oda_rows)}</div></div>
</section>""")

# ---------- assemble ----------
_here = Path(__file__).resolve().parent
ver = format(int(max(SRC.stat().st_mtime, Path(__file__).stat().st_mtime,
                     (_here / "theme.css").stat().st_mtime)), "x")
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NetBank — Final Deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Geist:wght@400..700&family=Geist+Mono:wght@400..600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="vendor/reveal.css?v={ver}">
<link rel="stylesheet" href="theme.css?v={ver}">
</head>
<body>
<div class="reveal"><div class="slides">
{chr(10).join(sections)}
</div></div>
<script src="vendor/reveal.js?v={ver}"></script>
<script src="vendor/notes/notes.js?v={ver}"></script>
<script>
Reveal.initialize({{
  width:1280, height:840, margin:0.045, minScale:0.2, maxScale:1.6,
  center:false, hash:true, slideNumber:'c/t', progress:true, transition:'fade',
  plugins:[RevealNotes]
}});

// auto-fit: scale each slide's body so the whole slide is visible on one screen (no below-fold)
function fit(section){{
  if(!section) return;
  var body=section.querySelector('.slide-body'); if(!body) return;
  var inner=body.querySelector('.fit'); if(!inner) return;
  inner.style.transform='none'; inner.style.width='100%';
  // available height = fixed 840 canvas minus vertical padding minus every sibling block
  var used=86;  // padding 46 top + 40 bottom
  Array.prototype.forEach.call(section.children, function(c){{
    if(c===body || c.offsetParent===null) return;
    var cs=getComputedStyle(c);
    used += c.offsetHeight + parseFloat(cs.marginTop||0) + parseFloat(cs.marginBottom||0);
  }});
  var avail=840-used, need=inner.scrollHeight;
  if(need>avail+1){{
    var k=Math.max(0.5, avail/need);
    inner.style.transform='scale('+k+')';
    inner.style.transformOrigin='top left';
    inner.style.width=(100/k)+'%';
  }}
}}
Reveal.on('ready', function(e){{ fit(e.currentSlide); }});
Reveal.on('slidechanged', function(e){{ fit(e.currentSlide); }});
Reveal.on('resize', function(){{ setTimeout(function(){{ fit(Reveal.getCurrentSlide()); }}, 60); }});
</script>
</body>
</html>
"""
OUT.write_text(html_doc, encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}  ({len(sections)} sections, {OUT.stat().st_size} bytes)")
print("sections:", ", ".join(s["title"][:28] for s in slides[:1]) + f" … +{len(sections)-1}")
