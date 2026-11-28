"""Reconcile the print tables into one master table, data/works.csv (28 Nov 2026).

Inputs (frozen copies, never edited again):
    data/archive/2026-11-28-pre-reconciliation/
        works.csv, numberings.csv            legacy works (85) and their derived numbers
        strand_a/entries.csv, entries_de.csv strand A (dictionaries)
        strand_b/entries.csv, entries_de.csv strand B (French and German schoolbooks, roots)
        strand_d/entries_en.csv              strand D (English)
        panel/entries_fr.csv                 French panel and school series

Outputs:
    data/works.csv                       one row per edition read; the single source from now on
    data/reconciliation/id_map.csv       every input id -> work_id
    data/reconciliation/conflicts.csv    slot disagreements inside merged rows
    data/reconciliation/ledger_map.csv   ledger_print rows -> work_id, with slot disagreements
    data/reconciliation/hand_coding.csv  rows missing genre, tradition or year_sort

Then run scripts/derive_numberings.py, which now derives numberings.csv from the slot columns.

Merge rule. Rows that record the same edition are merged (the clusters are listed by hand below).
The slot vector comes from the best-verified source (full_text > contents > snippet > paper_table >
secondary > unverified). If two sources tie, the strand row wins, but a value the other source has
and the winner leaves blank is kept and flagged, because a blank in a strand row can mean "not
recorded". If the winner is better verified, its blanks stand and the other value is flagged.
Every disagreement goes to conflicts.csv. MIT License.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "data" / "archive" / "2026-11-28-pre-reconciliation"
OUT = ROOT / "data"
REC = OUT / "reconciliation"
SLOTS = ["H6", "C", "D", "F", "B", "L1", "L2", "E"]
RANK = {"full_text": 6, "contents": 5, "snippet": 4, "paper_table": 3, "secondary": 2, "unverified": 1, "": 0}
LANG = {"fr": "French", "en": "English", "de": "German"}

STRAND_FILES = [
    ("strand_a/entries", ARC / "strand_a" / "entries.csv"),
    ("strand_a/entries_de", ARC / "strand_a" / "entries_de.csv"),
    ("strand_b/entries", ARC / "strand_b" / "entries.csv"),
    ("strand_b/entries_de", ARC / "strand_b" / "entries_de.csv"),
    ("strand_d/entries_en", ARC / "strand_d" / "entries_en.csv"),
    ("panel/entries_fr", ARC / "panel" / "entries_fr.csv"),
]

# Same edition recorded twice or three times. Primary id first: the legacy work_id if there is one
# (citations.csv and the findings notes use it), else the strand row read first.
CLUSTERS = [
    ["1842-marie-nicolas-bouillet", "sa-1842-bouillet", "pn-fr-1842-bouillet"],
    ["sa-1863-dezobry", "pn-fr-1863-dezobry"],
    ["sa-1869-larousse", "pn-fr-1869-larousse-gdu"],
    ["1788-edward-gibbon", "sd-1788-gibbon-ch59"],
    ["1877-eb9-crusades", "sd-1877-eb9-cox"],
    ["1908-louis-brehier", "sd-1908-brehier-catholic-enc"],
    ["1911-ernest-barker", "sd-1911-eb11-barker"],
    ["1907-david-s-schaff", "sd-1907-schaff-hcc5"],
    ["1891-victor-duruy", "ss-fr-1891-duruy-moyen-age-en"],
    ["1861-victor-duruy", "ss-fr-1861-duruy-moyen-age"],
    ["1816-saint-allais", "sa-1816-saint-allais"],
]

# Tradition and genre where the frame or the row settles them; everything else is left blank
# and listed in hand_coding.csv rather than guessed.
TRADITION_EN = {
    "sa-1728-chambers": "Britain", "sa-1771-eb1": "Britain", "sa-1778-eb2": "Britain", "sa-1797-eb3": "Britain",
    "sa-1810-eb4": "Britain", "sa-1815-eb5": "Britain", "sa-1823-eb6": "Britain", "sa-1842-eb7": "Britain",
    "sa-1854-eb8": "Britain", "sa-1808-rees": "Britain", "sa-1837-penny": "Britain", "sa-1844-haydn": "Britain",
    "sa-1830-americana": "US", "sa-1859-newamerican": "US",
}
COUNTRY = {"US": "US", "GB": "Britain", "UK": "Britain", "GB?": "Britain"}
FRAME_GENRE = {"strand_a_fr_en": "Reference", "strand_a_de": "Reference", "panel_1770_1930": "Reference",
               "school_series": "School"}

# Legacy rows whose shorthand was free text that derive_numberings could not parse; the ledger
# (hand-coded 9 Nov 2026 from the same corpus rows) had already parsed them. Each value checked
# against the legacy shorthand quoted beside it. EB9's E 9 is not taken: the strand D full-text
# read leaves Edward out of the ninth, and the disagreement stays in conflicts.csv.
LEDGER_FILL = {
    "1639-thomas-fuller": ({"L1": "12", "L2": "13"}, "12th and 13th Louis IX"),
    "1820-charles-mills": ({"B": "7", "L1": "8"}, "B and L1 as 7 and 8"),
    "1893-greek-ministry-of-education": ({"C": "4"}, "Second, Third, Fourth named"),
    "1907-w-b-stevenson": ({"C": "4"}, '"fourth crusade" in quotation marks'),
    "1962-k-m-setton-ed": ({"C": "4", "D": "5"}, '"Fourth" and "Fifth"'),
}

COLS = ["work_id", "alt_ids", "source_tables", "label", "author", "work", "edition", "year_label", "year_sort",
        "place_publisher", "volume", "pages", "headword", "language", "tradition", "genre", "census_frame",
        "enumerates", "stated_count", "stated_phrase", "numbering_shorthand", *SLOTS, "highest_ordinal",
        "organized_by", "scheme_family", "signature_match", "differing_slots", "stemma_parent", "parent_evidence",
        "quote", "how_verified", "access", "url", "verification_level", "title_page_checked", "research_pass",
        "country", "channel", "notes", "checked_on"]


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def year_sort(s):
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", s or "")
    return m.group(1) if m else ""


def ords(cell):
    """A slot cell holds one ordinal, or two separated by ';' when a source splits the expedition
    (Cantù 1842: Andrew II's 1217 expedition fifth, Damietta from 1218 sixth)."""
    return [int(x) for x in (cell or "").split(";") if x.strip()]


def highest(row):
    vals = [o for s in SLOTS for o in ords(row[s])]
    return str(max(vals)) if vals else ""


def shorthand(slots):
    groups = {}
    for s in SLOTS:
        for o in ords(slots.get(s, "")):
            groups.setdefault(o, []).append(s)
    return ", ".join(f"{'+'.join(v)} {k}" for k, v in sorted(groups.items()))


def short(text, n=60):
    t = re.split(r"[:;(]| - ", text or "")[0].strip().rstrip(",.")
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def author_short(a):
    a = re.split(r"[;,(]", re.sub(r"\([^)]*\)", "", a or ""))[0].strip()
    return "" if a.lower().startswith(("anon", "[")) else a


def from_strand(table, r):
    row = {c: "" for c in COLS}
    for c in COLS:
        if c in r:
            row[c] = r[c]
    row["work_id"] = r["entry_id"]
    row["source_tables"] = table
    row["author"] = r["author_editor"]
    row["year_label"] = r["year_read"]
    row["year_sort"] = year_sort(r["year_read"])
    row["language"] = LANG.get(r["language"], r["language"])
    a = author_short(r["author_editor"])
    row["label"] = re.sub(r"\s+", " ", f"{a}, {short(r['work'])}" if a else short(r["work"]))
    row["numbering_shorthand"] = shorthand(r)
    row["how_verified"] = "; ".join(x for x in [r.get("access", ""), r.get("edition", ""), r.get("pages", "")] if x)
    row["research_pass"] = table.split("/")[0]
    eid = r["entry_id"]
    if row["language"] == "French":
        row["tradition"] = "France"
    elif row["language"] == "German":
        row["tradition"] = "Germany"
    elif eid in TRADITION_EN:
        row["tradition"] = TRADITION_EN[eid]
    elif r.get("country"):
        row["tradition"] = COUNTRY.get(r["country"], "")
    if eid.startswith("pn-"):
        row["genre"] = "Reference"
    else:
        row["genre"] = FRAME_GENRE.get(r.get("census_frame", ""), "")
    return row


def from_legacy(r, nums):
    row = {c: "" for c in COLS}
    for c in ["work_id", "label", "author", "year_label", "year_sort", "language", "tradition", "genre",
              "numbering_shorthand", "how_verified", "verification_level", "research_pass", "notes"]:
        row[c] = r[c]
    row["source_tables"] = "works"
    for s, v in nums.get(r["work_id"], {}).items():
        if s in SLOTS:
            row[s] = ";".join(v)
    if r["work_id"] in LEDGER_FILL:
        fill, quoted = LEDGER_FILL[r["work_id"]]
        for s, v in fill.items():
            assert not row[s], (r["work_id"], s)
            row[s] = v
        row["notes"] = (row["notes"] + " | " if row["notes"] else "") + \
            f"Slots {', '.join(f'{s} {v}' for s, v in fill.items())} parsed from the shorthand ({quoted}) at the reconciliation, as in the ledger."
    row["highest_ordinal"] = highest(row)
    return row


def merge(cluster, rows, conflicts):
    members = [rows[i] for i in cluster]
    best = max(members, key=lambda m: (RANK.get(m["verification_level"], 0), m["source_tables"] != "works"))
    out = dict(best)
    out["work_id"] = cluster[0]
    out["alt_ids"] = ";".join(i for i in cluster[1:])
    out["source_tables"] = ";".join(m["source_tables"] for m in members)
    legacy = rows[cluster[0]] if rows[cluster[0]]["source_tables"] == "works" else None
    if legacy:
        for c in ["label", "tradition", "genre", "research_pass"]:
            out[c] = legacy[c] or out[c]
    for c in COLS:
        if not out[c]:
            for m in members:
                if m[c] and c not in SLOTS and c not in ("highest_ordinal",):
                    out[c] = m[c]
                    break
    out["census_frame"] = ";".join(sorted({m["census_frame"] for m in members if m["census_frame"]}))
    out["how_verified"] = " | ".join(dict.fromkeys(m["how_verified"] for m in members if m["how_verified"]))
    out["notes"] = " | ".join(dict.fromkeys(f"[{m['source_tables']}] {m['notes']}" for m in members if m["notes"]))
    for m in members:
        if m is best:
            continue
        tie = RANK.get(m["verification_level"], 0) == RANK.get(best["verification_level"], 0)
        for s in SLOTS:
            a, b = best[s], m[s]
            if a == b:
                continue
            if not a and b and tie:
                out[s] = b
                action = "kept other value (tie; winner blank)"
            elif not a and b:
                action = "winner's blank stands"
            elif a and not b:
                action = "winner's value stands"
            else:
                action = "winner's value stands (values differ)"
            conflicts.append({"work_id": cluster[0], "slot": s, "winner": best["source_tables"],
                              "winner_level": best["verification_level"], "winner_value": a,
                              "other": m["source_tables"], "other_level": m["verification_level"],
                              "other_value": b, "action": action})
    out["highest_ordinal"] = highest(out) or out["highest_ordinal"]
    gen = shorthand(out)
    if legacy and legacy["numbering_shorthand"] and legacy["numbering_shorthand"] != gen:
        out["notes"] += f" | [works] old shorthand: {legacy['numbering_shorthand']}"
    out["numbering_shorthand"] = gen or out["numbering_shorthand"]
    return out


def ledger_map(works):
    led = read(OUT / "ledger" / "ledger_print.csv")
    by_year = {}
    for w in works:
        by_year.setdefault(w["year_sort"], []).append(w)
    tok = lambda s: {t for t in re.findall(r"[a-zà-ÿ]{3,}", (s or "").lower())} - {"the", "and", "des", "der", "von", "for"}
    out = []
    for l in led:
        y = int(l["year_sort"])
        cands = [w for d in (0, 1, -1) for w in by_year.get(str(y + d), [])]
        lt = tok(l["source"])
        scored = sorted(((len(lt & tok(w["label"] + " " + w["author"] + " " + w["work"])) * 2
                          - (w["year_sort"] != l["year_sort"]), w) for w in cands), key=lambda x: -x[0])
        if scored and scored[0][0] > 0:
            w = scored[0][1]
            diffs = [f"{s}: ledger {l[s]} / works {w[s] or '-'}" for s in SLOTS
                     if re.fullmatch(r"\d+", l[s] or "") and int(l[s]) not in ords(w[s])]
            out.append({"ledger_source": l["source"], "year_sort": l["year_sort"], "work_id": w["work_id"],
                        "match_score": scored[0][0], "slot_disagreements": "; ".join(diffs)})
        else:
            out.append({"ledger_source": l["source"], "year_sort": l["year_sort"], "work_id": "",
                        "match_score": 0, "slot_disagreements": ""})
    return out


def main():
    legacy = read(ARC / "works.csv")
    nums = {}
    for n in read(ARC / "numberings.csv"):
        nums.setdefault(n["work_id"], {}).setdefault(n["expedition_id"], []).append(n["ordinal"])
    rows, order, id_map = {}, [], []
    for r in legacy:
        rows[r["work_id"]] = from_legacy(r, nums)
        order.append(r["work_id"])
        id_map.append({"old_id": r["work_id"], "source_table": "works", "work_id": r["work_id"]})
    for table, path in STRAND_FILES:
        for r in read(path):
            assert r["entry_id"] not in rows, r["entry_id"]
            rows[r["entry_id"]] = from_strand(table, r)
            order.append(r["entry_id"])
            id_map.append({"old_id": r["entry_id"], "source_table": table, "work_id": r["entry_id"]})
    conflicts, merged_away = [], set()
    for cl in CLUSTERS:
        for i in cl:
            assert i in rows, i
        rows[cl[0]] = merge(cl, rows, conflicts)
        merged_away.update(cl[1:])
    for m in id_map:
        for cl in CLUSTERS:
            if m["old_id"] in cl:
                m["work_id"] = cl[0]
    works = [rows[i] for i in order if i not in merged_away]
    works.sort(key=lambda w: (w["year_sort"] or "9999", w["work_id"]))

    REC.mkdir(exist_ok=True)

    def write(path, fields, data):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(data)

    write(OUT / "works.csv", COLS, works)
    write(REC / "id_map.csv", ["old_id", "source_table", "work_id"], id_map)
    write(REC / "conflicts.csv", ["work_id", "slot", "winner", "winner_level", "winner_value", "other",
                                  "other_level", "other_value", "action"], conflicts)
    lm = ledger_map(works)
    write(REC / "ledger_map.csv", ["ledger_source", "year_sort", "work_id", "match_score", "slot_disagreements"], lm)
    hc = [{"work_id": w["work_id"], "label": w["label"],
           "missing": ";".join(c for c in ("year_sort", "tradition", "genre") if not w[c])}
          for w in works if not (w["year_sort"] and w["tradition"] and w["genre"])]
    write(REC / "hand_coding.csv", ["work_id", "label", "missing"], hc)
    print(f"works.csv: {len(works)} rows from {len(id_map)} input rows ({len(merged_away)} merged away); "
          f"{len(conflicts)} slot conflicts; ledger rows matched {sum(1 for x in lm if x['work_id'])}/{len(lm)}; "
          f"{len(hc)} rows need hand-coding")


if __name__ == "__main__":
    main()
