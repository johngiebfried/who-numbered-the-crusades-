"""Derive data/numberings.csv (one row per work x expedition) from the
shorthand column in data/works.csv.

Shorthand: expedition codes from data/expeditions.csv followed by an ordinal,
e.g. "C 4, D+F 5, L1 6". "D+F 5" means both expeditions share the fifth.
Rows that do not parse are listed in data/numberings_unparsed.csv for
hand-coding. Hand-coded rows in data/numberings_manual.csv override derived
ones. MIT License.
"""
import csv, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1] / "data"
codes = {r["expedition_id"] for r in csv.DictReader(open(ROOT / "expeditions.csv", encoding="utf-8"))}
pat = re.compile(r"\b((?:[A-Z][A-Z0-9]*)(?:\+[A-Z][A-Z0-9]*)*)\s+(\d{1,2})\b")
out, unparsed = [], []
for w in csv.DictReader(open(ROOT / "works.csv", encoding="utf-8")):
    hits = [(g, int(n)) for g, n in pat.findall(w["numbering_shorthand"])
            if all(c in codes for c in g.split("+"))]
    if not hits:
        unparsed.append({"work_id": w["work_id"], "numbering_shorthand": w["numbering_shorthand"]})
        continue
    for group, n in hits:
        members = group.split("+")
        for c in members:
            out.append({"work_id": w["work_id"], "expedition_id": c, "ordinal": n,
                        "shared_with": "+".join(m for m in members if m != c),
                        "source": "derived"})
manual = ROOT / "numberings_manual.csv"
if manual.exists():
    man = list(csv.DictReader(open(manual, encoding="utf-8")))
    keys = {(m["work_id"], m["expedition_id"]) for m in man}
    out = [r for r in out if (r["work_id"], r["expedition_id"]) not in keys] + man
cols = ["work_id", "expedition_id", "ordinal", "shared_with", "source"]
with open(ROOT / "numberings.csv", "w", newline="", encoding="utf-8") as f:
    wtr = csv.DictWriter(f, cols); wtr.writeheader(); wtr.writerows(out)
with open(ROOT / "numberings_unparsed.csv", "w", newline="", encoding="utf-8") as f:
    wtr = csv.DictWriter(f, ["work_id", "numbering_shorthand"]); wtr.writeheader(); wtr.writerows(unparsed)
print(f"{len(out)} numbering rows; {len(unparsed)} works need hand-coding")
