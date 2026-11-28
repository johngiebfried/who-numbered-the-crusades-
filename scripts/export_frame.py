"""Print a view of data/works.csv: the rows of one census frame, one source table or one language.

    python3 scripts/export_frame.py --frame strand_b_de_1780_1860 > /tmp/strand_b_de.csv
    python3 scripts/export_frame.py --source strand_a/entries
    python3 scripts/export_frame.py --language German --columns work_id,label,C,D,F,L1,L2,scheme_family

Views are for reading. Edit data/works.csv, never an exported view. MIT License.
"""
import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--frame", help="census_frame value (rows in several frames match any of them)")
ap.add_argument("--source", help="source table, e.g. strand_b/entries_de or works")
ap.add_argument("--language")
ap.add_argument("--columns", help="comma-separated column list")
a = ap.parse_args()
with open(ROOT / "data" / "works.csv", newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = a.columns.split(",") if a.columns else r.fieldnames
    w = csv.DictWriter(sys.stdout, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for row in r:
        if a.frame and a.frame not in row["census_frame"].split(";"):
            continue
        if a.source and a.source not in row["source_tables"].split(";"):
            continue
        if a.language and row["language"] != a.language:
            continue
        w.writerow(row)
