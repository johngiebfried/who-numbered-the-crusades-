#!/usr/bin/env python3
"""Write site/wikipedia-timeline.html: a self-contained chart page with the data
from site/data/wikipedia_timeline.json embedded. Run after build_wikipedia.py."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(ROOT, "site", "data", "wikipedia_timeline.json"), encoding="utf-8"))
# the grid shows the 1 July samples; the 8 Nov 2026 check goes to the table only
TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>How Wikipedia numbers the crusades, 2001–2026</title>
<style>
.viz-root {
  color-scheme: light;
  --surface-1: #fcfcfb; --page: #f9f9f7;
  --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
  --grid: #e1e0d9; --axis: #c3c2b7; --ring: rgba(11,11,11,0.10);
  --nine: #2a78d6; --eight: #eb6834; --seven: #1baf7a; --partial: #c3c2b7;
  --on-fill: #ffffff; --on-partial: #0b0b0b; --empty: #f1f0ec;
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) .viz-root {
    color-scheme: dark;
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #f0efec; --text-secondary: #c3c2b7; --text-muted: #898781;
    --grid: #2c2c2a; --axis: #383835; --ring: rgba(255,255,255,0.10);
    --nine: #3987e5; --eight: #d95926; --seven: #199e70; --partial: #5c5b56;
    --on-fill: #ffffff; --on-partial: #f0efec; --empty: #232322;
  }
}
:root[data-theme="dark"] .viz-root {
  color-scheme: dark;
  --surface-1: #1a1a19; --page: #0d0d0d;
  --text-primary: #f0efec; --text-secondary: #c3c2b7; --text-muted: #898781;
  --grid: #2c2c2a; --axis: #383835; --ring: rgba(255,255,255,0.10);
  --nine: #3987e5; --eight: #d95926; --seven: #199e70; --partial: #5c5b56;
  --on-fill: #ffffff; --on-partial: #f0efec; --empty: #232322;
}
html, body { margin: 0; background: var(--page, #f9f9f7); }
.viz-root { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: var(--text-primary);
  background: var(--page); padding: 24px 16px 40px; }
.card { max-width: 1060px; margin: 0 auto; background: var(--surface-1); border: 1px solid var(--ring);
  border-radius: 12px; padding: 24px 24px 20px; }
h1 { font-size: 20px; font-weight: 600; margin: 0 0 6px; }
.sub { color: var(--text-secondary); font-size: 14px; line-height: 1.45; margin: 0 0 16px; max-width: 760px; }
.legend { display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; }
.legend span { display: inline-flex; align-items: center; gap: 6px; }
.sw { width: 14px; height: 12px; border-radius: 3px; display: inline-block; }
.chart-wrap { position: relative; overflow-x: auto; }
svg { display: block; width: 100%; min-width: 860px; height: auto; }
svg text { font-family: inherit; }
.cell { cursor: pointer; }
.cell:hover, .cell.active { filter: brightness(1.12); }
.cell.active { stroke: var(--text-primary); stroke-width: 1.5; }
#tip { position: absolute; pointer-events: none; background: var(--surface-1); border: 1px solid var(--ring);
  box-shadow: 0 4px 16px rgba(0,0,0,0.12); border-radius: 8px; padding: 10px 12px; font-size: 13px;
  max-width: 320px; display: none; z-index: 5; line-height: 1.4; }
#tip .v { font-weight: 600; font-size: 14px; color: var(--text-primary); display: flex; align-items: center; gap: 8px; }
#tip .k { width: 14px; height: 3px; border-radius: 2px; display: inline-block; }
#tip .s { color: var(--text-secondary); }
#tip .m { color: var(--text-muted); font-size: 12px; }
.controls { display: flex; gap: 12px; align-items: center; margin: 14px 0 0; font-size: 13px; color: var(--text-secondary); }
button { font: inherit; font-size: 13px; color: var(--text-primary); background: var(--surface-1);
  border: 1px solid var(--axis); border-radius: 6px; padding: 5px 10px; cursor: pointer; }
button:focus-visible, .chart-wrap:focus-visible { outline: 2px solid var(--nine); outline-offset: 2px; }
.events { margin: 20px 0 0; border-top: 1px solid var(--grid); padding-top: 14px; }
.events h2, .tablewrap h2 { font-size: 14px; font-weight: 600; margin: 0 0 8px; }
.events ol { margin: 0; padding: 0; list-style: none; font-size: 13px; color: var(--text-secondary); columns: 2 420px; column-gap: 28px; }
.events li { break-inside: avoid; margin: 0 0 7px; line-height: 1.4; }
.events b { color: var(--text-primary); font-weight: 600; font-variant-numeric: tabular-nums; }
.tablewrap { display: none; margin-top: 16px; overflow-x: auto; }
table { border-collapse: collapse; font-size: 12px; width: 100%; }
th, td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); vertical-align: top; }
th { color: var(--text-secondary); font-weight: 600; position: sticky; top: 0; background: var(--surface-1); }
td.n { font-variant-numeric: tabular-nums; }
a { color: var(--nine); }
.foot { font-size: 12px; color: var(--text-muted); margin-top: 16px; line-height: 1.45; }
</style>
</head>
<body>
<div class="viz-root">
<div class="card">
  <h1>How Wikipedia numbers the crusades, 2001–2026</h1>
  <p class="sub">The highest crusade number each page uses, as the page stood on 1 July of each year, in ten language editions. German Wikipedia has kept its own seven since 2004; the others settled on nine, Arabic last (2011–13), and English dropped back to eight after its Ninth Crusade was renamed in 2019.</p>
  <div class="legend" id="legend"></div>
  <div class="chart-wrap" id="wrap" tabindex="0" aria-label="Timeline grid. Use arrow keys to move between cells.">
    <svg id="chart" role="img" aria-labelledby="chart-title"><title id="chart-title">Highest crusade ordinal by page and year, ten Wikipedia languages</title></svg>
    <div id="tip" role="status"></div>
  </div>
  <div class="controls"><button id="tbl" aria-expanded="false">Show as table</button><span>Click a cell to open that revision.</span></div>
  <div class="tablewrap" id="tablewrap"><h2>All samples</h2><table id="table"></table></div>
  <div class="events"><h2>Key edits</h2><ol id="events"></ol></div>
  <p class="foot" id="foot"></p>
</div>
</div>
<script>
const DATA = __DATA__;
const FAM = {
  nine:   {label: "Nine (First to Ninth)", color: "var(--nine)", text: "var(--on-fill)"},
  eight:  {label: "Eight (First to Eighth)", color: "var(--eight)", text: "var(--on-fill)"},
  german_seven: {label: "German seven (Damietta and Frederick II both fifth)", color: "var(--seven)", text: "var(--on-fill)"},
  german_seven_bracketed: {label: "German seven, modern count in brackets", color: "url(#hatch)", key: "var(--seven)", text: "var(--on-fill)"},
  partial: {label: "No full sequence on the page", color: "var(--partial)", text: "var(--on-partial)"}
};
const PAGE_LABEL = {main_article: "Main article", navbox: "Navigation box", navbox_2: "Second navbox", list_article: "List article"};
const Y0 = 2001, Y1 = 2026;
const LABEL_W = 210, CW = 28, CH = 18, GAP = 2, GROUP_GAP = 12, TOP = 34;
const svgNS = "http://www.w3.org/2000/svg";
const svg = document.getElementById("chart");
const el = (n, a, p) => { const e = document.createElementNS(svgNS, n); for (const k in a) e.setAttribute(k, a[k]); (p || svg).appendChild(e); return e; };

// legend
const leg = document.getElementById("legend");
for (const [k, f] of Object.entries(FAM)) {
  const s = document.createElement("span"); const sw = document.createElement("i"); sw.className = "sw";
  sw.style.background = k === "german_seven_bracketed"
    ? "repeating-linear-gradient(135deg, var(--seven) 0 3px, var(--surface-1) 3px 5px)" : f.color;
  s.appendChild(sw); s.appendChild(document.createTextNode(f.label)); leg.appendChild(s);
}
{ const s = document.createElement("span"); s.innerHTML = '<svg width="14" height="14" viewBox="0 0 14 14" style="min-width:0;width:14px"><path d="M7 1 L13 7 L7 13 L1 7Z" fill="var(--text-primary)" stroke="var(--surface-1)" stroke-width="2"/></svg>';
  s.appendChild(document.createTextNode("Barons' Crusade article created")); leg.appendChild(s); }

// layout
const lanes = DATA.lanes.map(l => ({...l, points: l.points.filter(p => p.date.endsWith("-07-01"))}));
let y = TOP; const rows = []; let lastLang = null; const groupTop = {};
for (const l of lanes) {
  if (l.language !== lastLang) { if (lastLang) y += GROUP_GAP; groupTop[l.language] = y; lastLang = l.language; }
  rows.push({...l, y}); y += CH + GAP;
}
const W = LABEL_W + (Y1 - Y0 + 1) * (CW + GAP) + 8, H = y + 8;
svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
const defs = el("defs", {});
const pat = el("pattern", {id: "hatch", width: 6, height: 6, patternUnits: "userSpaceOnUse", patternTransform: "rotate(45)"}, defs);
el("rect", {width: 6, height: 6, fill: "var(--seven)"}, pat);
el("rect", {x: 0, width: 2, height: 6, fill: "var(--surface-1)", opacity: 0.85}, pat);
const xOf = yr => LABEL_W + (yr - Y0) * (CW + GAP);

// year axis
for (let yr = Y0; yr <= Y1; yr++) {
  if ((yr % 5 === 0 && Y1 - yr > 2) || yr === Y0 || yr === Y1) {
    el("text", {x: xOf(yr) + CW / 2, y: TOP - 12, "text-anchor": "middle", "font-size": 11, fill: "var(--text-muted)", "font-variant-numeric": "tabular-nums"}).textContent = yr;
    el("line", {x1: xOf(yr) + CW / 2, x2: xOf(yr) + CW / 2, y1: TOP - 7, y2: H - 6, stroke: "var(--grid)", "stroke-width": 1});
  }
}
// rows
const cells = [];
let prevLang = null;
for (const r of rows) {
  if (r.language !== prevLang) {
    el("text", {x: 0, y: r.y + CH - 5, "font-size": 13, "font-weight": 600, fill: "var(--text-primary)"}).textContent = r.language_name;
    prevLang = r.language;
  }
  el("text", {x: LABEL_W - 10, y: r.y + CH - 5, "text-anchor": "end", "font-size": 12, fill: "var(--text-secondary)"}).textContent = PAGE_LABEL[r.page];
  for (let yr = Y0; yr <= Y1; yr++) el("rect", {x: xOf(yr), y: r.y, width: CW, height: CH, rx: 3, fill: "var(--empty)"});
  let prevFam = null;
  r.points.forEach(p => {
    const yr = +p.date.slice(0, 4); const f = FAM[p.family] || FAM.partial;
    const c = el("rect", {x: xOf(yr), y: r.y, width: CW, height: CH, rx: 3, fill: f.color, class: "cell", "data-i": cells.length});
    cells.push({rect: c, p, lane: r, yr});
    if (p.family !== prevFam && p.highest) {
      const t = el("text", {x: xOf(yr) + CW / 2, y: r.y + CH - 5, "text-anchor": "middle", "font-size": 11, "font-weight": 600, fill: f.text, "pointer-events": "none"});
      t.textContent = p.highest;
    }
    prevFam = p.family;
  });
}
// Barons' article markers on the language's first row
for (const [lang, date] of Object.entries(DATA.barons_article)) {
  const top = groupTop[lang]; if (top === undefined) continue;
  const yr = +date.slice(0, 4), frac = (new Date(date) - new Date(yr + "-01-01")) / 31536000000;
  const cx = xOf(yr) + frac * (CW + GAP) - (CW + GAP) / 2 + CW / 2, cy = top - 1;
  const d = el("path", {d: `M${cx} ${cy - 6} L${cx + 6} ${cy} L${cx} ${cy + 6} L${cx - 6} ${cy}Z`, fill: "var(--text-primary)", stroke: "var(--surface-1)", "stroke-width": 2});
  const tt = el("title", {}, d); tt.textContent = `Barons' Crusade article created ${date}`;
}

// tooltip
const tip = document.getElementById("tip"), wrap = document.getElementById("wrap");
function famLine(p) { return (FAM[p.family] || FAM.partial).label; }
function show(i) {
  cells.forEach(c => c.rect.classList.remove("active"));
  const c = cells[i]; if (!c) return; c.rect.classList.add("active"); cur = i;
  tip.replaceChildren();
  const v = document.createElement("div"); v.className = "v";
  const k = document.createElement("i"); k.className = "k"; k.style.background = (FAM[c.p.family] || FAM.partial).key || (FAM[c.p.family] || FAM.partial).color; v.appendChild(k);
  v.appendChild(document.createTextNode(c.p.highest ? `Up to ${c.p.highest} · ${famLine(c.p)}` : famLine(c.p)));
  tip.appendChild(v);
  const add = (cls, txt) => { if (!txt) return; const d = document.createElement("div"); d.className = cls; d.textContent = txt; tip.appendChild(d); };
  add("s", `${c.lane.language_name} ${PAGE_LABEL[c.lane.page].toLowerCase()} (${c.lane.title}), 1 July ${c.yr}`);
  add("s", c.p.shorthand ? `Coded: ${c.p.shorthand}` : "");
  add("s", c.p.stated ? `Count stated in the text: ${c.p.stated}` : "");
  add("s", c.p.barons ? "Names the Barons' Crusade (1239–41)" : "");
  add("m", c.p.note);
  add("m", `Revision ${c.p.revid} · click to open`);
  tip.style.display = "block";
  const wr = wrap.getBoundingClientRect(), rr = c.rect.getBoundingClientRect();
  let left = rr.left - wr.left + wrap.scrollLeft + rr.width + 8, top = rr.top - wr.top - 4;
  if (left + 330 > wrap.scrollLeft + wr.width) left = rr.left - wr.left + wrap.scrollLeft - 330;
  tip.style.left = Math.max(0, left) + "px"; tip.style.top = top + "px";
}
let cur = -1;
svg.addEventListener("pointermove", e => { const i = e.target.getAttribute && e.target.getAttribute("data-i"); if (i !== null && i !== undefined) show(+i); });
svg.addEventListener("pointerleave", () => { tip.style.display = "none"; cells.forEach(c => c.rect.classList.remove("active")); });
svg.addEventListener("click", e => { const i = e.target.getAttribute && e.target.getAttribute("data-i"); if (i !== null) window.open(cells[+i].p.url, "_blank", "noopener"); });
wrap.addEventListener("keydown", e => {
  if (!cells.length) return;
  if (cur < 0) { show(0); e.preventDefault(); return; }
  const c = cells[cur]; let best = null;
  const pick = (f) => { let b = null, bd = 1e9; cells.forEach((o, j) => { const d = f(o); if (d !== null && d < bd) { bd = d; b = j; } }); return b; };
  const ri = rows.indexOf(c.lane);
  if (e.key === "ArrowRight") best = pick(o => o.lane === c.lane && o.yr > c.yr ? o.yr - c.yr : null);
  if (e.key === "ArrowLeft") best = pick(o => o.lane === c.lane && o.yr < c.yr ? c.yr - o.yr : null);
  if (e.key === "ArrowDown") best = pick(o => rows.indexOf(o.lane) > ri ? (rows.indexOf(o.lane) - ri) * 100 + Math.abs(o.yr - c.yr) : null);
  if (e.key === "ArrowUp") best = pick(o => rows.indexOf(o.lane) < ri ? (ri - rows.indexOf(o.lane)) * 100 + Math.abs(o.yr - c.yr) : null);
  if (e.key === "Enter") { window.open(c.p.url, "_blank", "noopener"); }
  if (e.key === "Escape") { tip.style.display = "none"; }
  if (best !== null) { show(best); e.preventDefault(); }
});
wrap.addEventListener("blur", () => { tip.style.display = "none"; });

// table
const tbtn = document.getElementById("tbl"), tw = document.getElementById("tablewrap"), table = document.getElementById("table");
tbtn.addEventListener("click", () => {
  const open = tw.style.display === "block"; tw.style.display = open ? "none" : "block";
  tbtn.textContent = open ? "Show as table" : "Hide table"; tbtn.setAttribute("aria-expanded", String(!open));
  if (!table.rows.length) {
    const head = table.createTHead().insertRow(); ["Language", "Page", "Sample", "Highest", "Family", "Coded numbering", "Stated", "Barons'", "Revision"].forEach(h => { const th = document.createElement("th"); th.textContent = h; head.appendChild(th); });
    const tb = table.createTBody();
    DATA.lanes.forEach(l => l.points.forEach(p => {
      const r = tb.insertRow();
      [l.language_name, PAGE_LABEL[l.page], p.date, p.highest || "", (FAM[p.family] || FAM.partial).label, p.shorthand, p.stated, p.barons ? "yes" : ""].forEach((t, j) => { const td = r.insertCell(); td.textContent = t; if (j === 3) td.className = "n"; });
      const td = r.insertCell(); const a = document.createElement("a"); a.href = p.url; a.target = "_blank"; a.rel = "noopener"; a.textContent = p.revid; td.appendChild(a);
    }));
  }
});
// events
const ev = document.getElementById("events");
const LN = {en: "English", de: "German", fr: "French", it: "Italian", es: "Spanish", nl: "Dutch", el: "Greek", ar: "Arabic", fa: "Persian", he: "Hebrew"};
DATA.events.forEach(e => {
  const li = document.createElement("li"); const b = document.createElement("b"); b.textContent = e.date; li.appendChild(b);
  li.appendChild(document.createTextNode(` ${LN[e.language]}, ${e.page}. ${e.change}`)); ev.appendChild(li);
});
document.getElementById("foot").textContent =
  `Source: MediaWiki API, retrieved ${DATA.retrieved}. Each cell is the revision in force at 00:00 UTC on 1 July. "Highest" is the highest crusade ordinal the page uses as a name; the coded numbering maps each ordinal to an expedition (E1 First, E2 Second, E3 Third, C 1202–04, D Damietta, F Frederick II, L1 and L2 Louis IX, E Lord Edward). German rows are hand-coded. Data: data/wikipedia/ in the project repository (CC BY 4.0); Wikipedia text is CC BY-SA.`;
</script>
</body>
</html>
"""
html = TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
out = os.path.join(ROOT, "site", "wikipedia-timeline.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", out, len(html))
