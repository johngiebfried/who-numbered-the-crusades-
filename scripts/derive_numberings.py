"""Derive data/numberings.csv (one row per work x expedition) from the slot columns of data/works.csv.

Since the reconciliation of 28 November 2026 the slot columns (H6, C, D, F, B, L1, L2, E) are the
record; the shorthand column is display text generated from them. Two expeditions with the same
ordinal in one row were counted as one, so each gets the other in `shared_with`.

Rows that number nothing in the slot columns but say they enumerate (or carry a legacy shorthand)
are written to data/numberings_unparsed.csv for hand-coding. MIT License.
"""
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1] / "data"
SLOTS = ["H6", "C", "D", "F", "B", "L1", "L2", "E"]
out, unparsed = [], []
with open(ROOT / "works.csv", newline="", encoding="utf-8") as f:
    for w in csv.DictReader(f):
        filled = {s: w[s] for s in SLOTS if w[s]}
        if not filled:
            if w["enumerates"] in ("yes", "partial") or (w["numbering_shorthand"] and w["source_tables"] == "works"):
                unparsed.append({"work_id": w["work_id"],
                                 "numbering_shorthand": w["numbering_shorthand"] or w["stated_phrase"]})
            continue
        # A cell may hold two ordinals ("5;6") when the source splits the expedition.
        pairs = [(s, n.strip()) for s, cell in filled.items() for n in cell.split(";") if n.strip()]
        for s, n in pairs:
            out.append({"work_id": w["work_id"], "expedition_id": s, "ordinal": n,
                        "shared_with": "+".join(t for t, m in pairs if m == n and t != s),
                        "source": "works.csv"})
cols = ["work_id", "expedition_id", "ordinal", "shared_with", "source"]
with open(ROOT / "numberings.csv", "w", newline="", encoding="utf-8") as f:
    wtr = csv.DictWriter(f, cols); wtr.writeheader(); wtr.writerows(out)
with open(ROOT / "numberings_unparsed.csv", "w", newline="", encoding="utf-8") as f:
    wtr = csv.DictWriter(f, ["work_id", "numbering_shorthand"]); wtr.writeheader(); wtr.writerows(unparsed)
print(f"{len(out)} numbering rows; {len(unparsed)} works need hand-coding")
