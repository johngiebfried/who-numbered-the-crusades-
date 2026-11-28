"""Helpers for Strand D2 (English-language print, 1800-1945) session scripts.

Each session script defines rows and calls these functions. All writes are idempotent:
rows are upserted by key, appends skip rows already present. works.csv keeps its CRLF line
endings (as written by reconcile_works.py); the hand-kept LF files stay LF. MIT License.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"
WORKS = ROOT / "works.csv"
ATTR = ROOT / "strand_d2" / "attributes.csv"
FRAME = ROOT / "strand_d2" / "frame.csv"
CIT = ROOT / "citations.csv"
REA = ROOT / "reasons" / "reasons.csv"
LOG = ROOT / "search_log.csv"
SLOTS = ["H6", "C", "D", "F", "B", "L1", "L2", "E"]
WHO = "Claude (main session, browser)"


def _read(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def _ords(cell):
    return [int(x) for x in (cell or "").split(";") if x.strip()]


def shorthand(row):
    groups = {}
    for s in SLOTS:
        for o in _ords(row.get(s, "")):
            groups.setdefault(o, []).append(s)
    return ", ".join(f"{'+'.join(v)} {k}" for k, v in sorted(groups.items()))


def upsert_works(rows, clear_slots=()):
    """rows: dicts keyed by works.csv columns; must include work_id. Existing rows are updated
    field by field (only the keys given). Slots listed in clear_slots as (work_id, slot) are blanked.
    The shorthand and highest_ordinal are regenerated for every touched row."""
    cols, works = _read(WORKS)
    by = {w["work_id"]: w for w in works}
    touched = set()
    for r in rows:
        unknown = [k for k in r if k not in cols]
        assert not unknown, (r["work_id"], unknown)
        if r["work_id"] in by:
            by[r["work_id"]].update(r)
        else:
            new = {c: "" for c in cols}
            new.update(r)
            works.append(new)
            by[r["work_id"]] = new
        touched.add(r["work_id"])
    for wid, slot in clear_slots:
        by[wid][slot] = ""
        touched.add(wid)
    for wid in touched:
        w = by[wid]
        sh = shorthand(w)
        if sh:
            w["numbering_shorthand"] = sh
        vals = [o for s in SLOTS for o in _ords(w[s])]
        w["highest_ordinal"] = str(max(vals)) if vals else w["highest_ordinal"]
    works.sort(key=lambda w: (w["year_sort"] or "9999", w["work_id"]))
    with open(WORKS, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=cols)  # CRLF, as reconcile_works.py wrote it
        wr.writeheader()
        wr.writerows(works)
    return len(touched)


def upsert_attrs(rows):
    cols, attrs = _read(ATTR)
    by = {a["work_id"]: a for a in attrs}
    for r in rows:
        unknown = [k for k in r if k not in cols]
        assert not unknown, (r["work_id"], unknown)
        if r["work_id"] in by:
            by[r["work_id"]].update(r)
        else:
            new = {c: "" for c in cols}
            new.update(r)
            attrs.append(new)
            by[r["work_id"]] = new
    attrs.sort(key=lambda a: a["work_id"])
    with open(ATTR, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        wr.writeheader()
        wr.writerows(attrs)


def append_rows(path, rows, key_fields):
    cols, existing = _read(path)
    have = {tuple(e.get(k, "") for k in key_fields) for e in existing}
    add = [r for r in rows if tuple(r.get(k, "") for k in key_fields) not in have]
    if add:
        with open(path, "a", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerows([[r.get(c, "") for c in cols] for r in add])
    return len(add)


def append_citations(rows):
    return append_rows(CIT, rows, ["citing_work_id", "cited", "relation"])


def append_reasons(rows):
    return append_rows(REA, rows, ["reason_id"])


def append_log(date, rows):
    """rows: (corpus, query, date_filter, hits, hits_examined, works_added). search_log.csv is CRLF."""
    with open(LOG, newline="", encoding="utf-8") as f:
        have = {(x[0], x[1], x[2]) for x in csv.reader(f)}
    add = [[date, c, q, df, h, he, wa, WHO] for c, q, df, h, he, wa in rows if (date, c, q) not in have]
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(add)
    return len(add)


def set_frame_status(updates):
    """updates: {frame_id: (status, work_ids, note)}"""
    cols, frame = _read(FRAME)
    for fr in frame:
        if fr["frame_id"] in updates:
            st, ids, note = updates[fr["frame_id"]]
            fr["status"] = st
            if ids:
                old = [x for x in fr["existing_work_ids"].split(";") if x]
                fr["existing_work_ids"] = ";".join(dict.fromkeys(old + ids.split(";")))
            if note:
                fr["notes"] = (fr["notes"] + " | " if fr["notes"] else "") + note
    with open(FRAME, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        wr.writeheader()
        wr.writerows(frame)


def add_frame_rows(rows):
    cols, frame = _read(FRAME)
    have = {fr["frame_id"] for fr in frame}
    for r in rows:
        if r["frame_id"] not in have:
            frame.append({c: r.get(c, "") for c in cols})
    with open(FRAME, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        wr.writeheader()
        wr.writerows(frame)


def gibbon_numbers(row):
    """Compare C, D, L1, L2 with Gibbon's (C 4, D 5, L1 6, L2 7)."""
    g = {"C": 4, "D": 5, "L1": 6, "L2": 7}
    seen = [(s, _ords(row.get(s, ""))) for s in g if _ords(row.get(s, ""))]
    if not seen:
        return ""
    agree = [s for s, v in seen if g[s] in v]
    return "all" if len(agree) == len(seen) else ("some" if agree else "none")
