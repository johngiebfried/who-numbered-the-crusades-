"""Strand D2 analyses: derived tables from data/works.csv and data/strand_d2/attributes.csv.

Writes, in data/strand_d2/:
  fourth_by_decade.csv    fourth_identity by decade, frame and country of publication (D2 rows and the
                          English rows of earlier strands that have the same coding)
  gibbon_table.csv        every row whose crusade chapter, preface or bibliography names Gibbon, with its numbers
  edward_timeline.csv     every row with an Edward status or a ninth, in date order, and the first and last
                          witness of each value
  conversation_edges.csv  citation edges among English rows, with the tradition each side follows and a flag
                          where a work cites a source whose numbers it does not use
  national.csv            scheme family by country of publication and genre
  fourth_pivot.csv        the Fourth by decade and genre, with the share of decided rows whose fourth is Henry VI's
  fourth_series.csv       the Fourth and the family, edition by edition, for the main series
Rerun after any data change. MIT License.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"
OUT = ROOT / "strand_d2"


def read(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(p, cols, rows):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


works = {w["work_id"]: w for w in read(ROOT / "works.csv")}
attrs = {a["work_id"]: a for a in read(OUT / "attributes.csv")}
cites = read(ROOT / "citations.csv")

GENRE = {"d2_reference_en": "reference", "d2_school_en": "school", "d2_popular_en": "popular",
         "d2_scholarly_en": "scholarly", "d2_church_en": "church_national"}


def genre(w):
    if w["census_frame"] in GENRE:
        return GENRE[w["census_frame"]]
    g = (w["genre"] or "").lower()
    for k, v in (("reference", "reference"), ("school", "school"), ("popular", "popular"),
                 ("scholar", "scholarly"), ("church", "church_national"), ("history", "popular")):
        if k in g:
            return v
    return "other"


def year(w):
    try:
        return int((w["year_sort"] or "")[:4])
    except ValueError:
        return None


def country(w, a):
    c = (a or {}).get("country_pub", "")
    if c:
        return c
    return {"GB": "England", "UK": "England", "US": "US", "CA": "Canada"}.get(w["country"], w["country"] or "unknown")


def fourth(w, a):
    if a and a.get("fourth_identity"):
        return a["fourth_identity"]
    h6, c = "4" in w["H6"].split(";"), "4" in w["C"].split(";")
    if h6 and c:
        return "both"
    if h6:
        return "H6"
    if c:
        return "C"
    if a is not None and not a.get("fourth_identity"):
        return "unknown"
    return "none" if w["enumerates"] in ("no", "") else "other"


# English rows 1788-1945
eng = [w for w in works.values() if w["language"] == "English" and year(w) and 1788 <= year(w) <= 1945]

# 1. Fourth by decade
cnt = Counter()
for w in eng:
    a = attrs.get(w["work_id"])
    d = year(w) // 10 * 10
    cnt[(d, genre(w), country(w, a), fourth(w, a))] += 1
rows = [dict(decade=f"{d}s", genre=g, country_pub=c, fourth_identity=f, rows=n)
        for (d, g, c, f), n in sorted(cnt.items())]
write(OUT / "fourth_by_decade.csv", ["decade", "genre", "country_pub", "fourth_identity", "rows"], rows)

# 2. Gibbon table
gt = []
for wid, a in attrs.items():
    gc = a.get("gibbon_cited", "")
    if gc and gc not in ("none", "unchecked") and wid in works:
        w = works[wid]
        gt.append(dict(work_id=wid, year=w["year_sort"], genre=genre(w), country_pub=country(w, a), gibbon_cited=gc,
                       gibbon_edition=a.get("gibbon_edition", ""), numbering=w["numbering_shorthand"],
                       scheme_family=w["scheme_family"], gibbon_numbers=a.get("gibbon_numbers", ""),
                       numbers_follow=a.get("numbers_follow", "")))
gt.sort(key=lambda r: (r["year"], r["work_id"]))
write(OUT / "gibbon_table.csv", list(gt[0].keys()), gt)

# 3. Edward timeline
et = []
for w in eng:
    a = attrs.get(w["work_id"], {})
    es, nr = a.get("edward_status", ""), a.get("ninth_referent", "")
    nine = any("9" in w[s].split(";") for s in ("H6", "C", "D", "F", "B", "L1", "L2", "E"))
    if es or nr or w["E"] or nine:
        et.append(dict(year=w["year_sort"], work_id=w["work_id"], genre=genre(w), country_pub=country(w, a),
                       edward_status=es, ninth_referent=nr, E=w["E"], L1=w["L1"], L2=w["L2"],
                       scheme_family=w["scheme_family"], verification=w["verification_level"]))
et.sort(key=lambda r: (r["year"], r["work_id"]))
write(OUT / "edward_timeline.csv", list(et[0].keys()), et)
firsts = []
for field in ("edward_status", "ninth_referent"):
    seen = defaultdict(list)
    for r in et:
        if r[field]:
            seen[r[field]].append(r)
    for val, rs in sorted(seen.items()):
        firsts.append(dict(field=field, value=val, rows=len(rs), first_year=rs[0]["year"], first=rs[0]["work_id"],
                           last_year=rs[-1]["year"], last=rs[-1]["work_id"]))
write(OUT / "edward_firsts.csv", list(firsts[0].keys()), firsts)

# 4. Conversation edges among English rows
SL = ["H6", "C", "D", "F", "B", "L1", "L2", "E"]
REFSLOTS = {"Gibbon": {"C": "4", "D": "5", "L1": "6", "L2": "7"},
            "Michaud": {"H6": "4", "C": "5", "D": "6", "L1": "7", "L2": "8"},
            "Mills": {"H6": "4", "C": "5", "D": "6", "F": "6", "B": "7", "L1": "8"},
            "Cox": {"H6": "4", "C": "5", "D": "6", "F": "6", "B": "7", "L1": "8", "L2": "9"},
            "Proctor": {"C": "4", "D": "5", "F": "5", "B": "6", "L1": "7", "L2": "8"}}


def slots(wid_or_name):
    if wid_or_name in REFSLOTS:
        return REFSLOTS[wid_or_name]
    w = works.get(wid_or_name)
    if not w:
        return {}
    return {s: w[s].split(";")[0] for s in SL if w[s] and s != "E"}


edges = []
for e in cites:
    a = attrs.get(e["citing_work_id"])
    w = works.get(e["citing_work_id"])
    if not w or w["language"] != "English":
        continue
    mine = slots(e["citing_work_id"])
    theirs = slots(e["cited"])
    shared = [s for s in mine if s in theirs]
    if not shared:
        verdict = "no shared slot" if theirs else ""
    elif all(mine[s] == theirs[s] for s in shared):
        verdict = "agrees"
    elif any(mine[s] == theirs[s] for s in shared):
        verdict = "partly agrees"
    else:
        verdict = "disagrees"
    edges.append(dict(citing=e["citing_work_id"], citing_year=w["year_sort"],
                      citing_follows=(a or {}).get("numbers_follow", "").split(";")[0], cited=e["cited"],
                      relation=e["relation"], confidence=e["confidence"], shared_slots=" ".join(shared),
                      numbers_vs_cited=verdict))
edges.sort(key=lambda r: (r["citing_year"], r["citing"]))
write(OUT / "conversation_edges.csv", list(edges[0].keys()), edges)

# 5. National differences
nat = Counter()
for w in eng:
    if year(w) < 1800:
        continue
    a = attrs.get(w["work_id"])
    nat[(country(w, a), genre(w), w["scheme_family"] or "(none coded)")] += 1
write(OUT / "national.csv", ["country_pub", "genre", "scheme_family", "rows"],
      [dict(country_pub=c, genre=g, scheme_family=s, rows=n) for (c, g, s), n in sorted(nat.items())])

# 6. Fourth pivot: decade by genre, with the share of decided rows whose fourth is Henry VI's
piv = defaultdict(Counter)
for w in eng:
    a = attrs.get(w["work_id"])
    f = fourth(w, a) or "unknown"
    d = f"{year(w) // 10 * 10}s"
    for g in ("all", genre(w)):
        piv[(d, g)][f] += 1
prow = []
for (d, g), c in sorted(piv.items()):
    decided = c["C"] + c["H6"] + c["both"]
    prow.append(dict(decade=d, genre=g, C=c["C"], H6=c["H6"], both=c["both"], none=c["none"], other=c["other"],
                     unknown=c["unknown"], rows=sum(c.values()),
                     h6_share_of_decided=f"{(c['H6'] + c['both']) / decided:.2f}" if decided else ""))
write(OUT / "fourth_pivot.csv", list(prow[0].keys()), prow)

# 7. Series: the Fourth and the family, edition by edition, for the reference and textbook series
SERIES = {
    "Encyclopaedia Britannica": ["sa-1797-eb3", "sa-1810-eb4", "sa-1815-eb5", "sa-1823-eb6", "sa-1842-eb7",
                                 "sa-1854-eb8", "1877-eb9-crusades", "1911-ernest-barker", "sd2-1929-eb14-crusades"],
    "Haydn's Dictionary of Dates": ["sa-1844-haydn", "sd2-1866-haydn-moxon", "sd2-1869-haydn-harper",
                                    "sd2-1883-haydn-harper", "sd2-1898-haydn-toronto", "sd-1910-haydn-dates-25"],
    "Chambers's": ["sd2-1848-chambers-information", "sd-1868-chambers-enc", "sd2-1871-chambers-lippincott",
                   "sd-1901-chambers-enc"],
    "Encyclopaedia Americana": ["sa-1830-americana", "sd2-1831-americana-chron-table", "sd-1924-americana"],
    "Appleton's American Cyclopaedia": ["sa-1859-newamerican", "1873-american-cyclopaedia-crusades"],
    "Johnson's": ["sd-1898-johnsons-universal"],
    "New International": ["sd-1902-new-international"],
    "Nuttall": ["1907-nuttall-encyclopaedia", "sd2-1923-nuttall-encyclopaedia"],
    "Ploetz and Langer": ["1883-carl-ploetz", "sd2-1940-langer-encyclopedia"],
    "Michaud in English": ["1852-michaud-trans-william-robson", "sd2-1900-michaud-robson-ny"],
    "Mills and his reuse": ["1820-charles-mills", "sd2-1904-historians-history-v8"],
    "Procter": ["1842-george-proctor", "sd2-1856-procter-philadelphia"],
    "Cox": ["1874-george-w-cox", "sd-1901-cox-crusades-12"],
    "Collier": ["sd-1860-collier-great-events", "sd2-1872-collier-outlines-toronto"],
    "Swinton": ["1874-william-swinton", "sd2-1883-swinton-canadian"],
    "W. C. Taylor": ["sd2-1844-taylor-manual-us", "sd2-1858-taylor-students-manual"],
    "Myers": ["1885-p-v-n-myers", "sd2-1889-myers-general-history"],
    "Gibbon and his abridgments": ["1788-edward-gibbon", "sd2-1868-students-gibbon",
                                   "sd2-1869-gibbon-crusades-extract"],
    "Barker": ["1911-ernest-barker", "1923-ernest-barker"],
}
srow = []
for s, ids in SERIES.items():
    for wid in ids:
        w = works.get(wid)
        if not w:
            continue
        a = attrs.get(wid)
        srow.append(dict(series=s, year=w["year_sort"], work_id=wid, country_pub=country(w, a),
                         fourth_identity=fourth(w, a), scheme_family=w["scheme_family"],
                         numbering=w["numbering_shorthand"], verification=w["verification_level"]))
write(OUT / "fourth_series.csv", list(srow[0].keys()), srow)

print(len(eng), "English rows 1788-1945;", len(gt), "Gibbon rows;", len(et), "Edward/ninth rows;", len(edges),
      "edges;", len(srow), "series rows")
