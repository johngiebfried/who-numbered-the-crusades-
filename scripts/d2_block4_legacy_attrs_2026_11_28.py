"""Strand D2, block 4 (28 November 2026): D2 attributes for the English rows of earlier strands that were
not re-read in this session, derived from their slot columns and imprints.

Every row written here says so in `notes` ("derived from slots; not re-read in D2"). Gibbon citation is
`unchecked` unless an earlier note documents it. Rows already in attributes.csv are left alone. MIT License.
"""
import d2_lib as L

D = "2026-11-28"
works = {w["work_id"]: w for w in L._read(L.WORKS)[1]}
have = {a["work_id"] for a in L._read(L.ATTR)[1]}

FOLLOW = {"moreri_eight": "moreri", "moreri_eight_variant": "moreri", "nine_H6": "michaud_mills",
          "nine_F7": "michaud_mills", "modern_eight": "modern", "near_modern": "modern", "gibbon_seven": "gibbon",
          "frederick_fifth_seven": "german", "frederick_fifth_seven_variant": "german", "german_six": "german",
          "barons_sixth": "own", "barons_sixth_variant": "own"}
GIBBON = {"1885-p-v-n-myers": ("preface;footnote", "Myers names Gibbon as a lesser authority (citations.csv)"),
          "sd-1847-milner-sketches": ("named_in_text", "'By Gibbon, this fifth Crusade seems to be considered as a "
                                                       "continuation' (row quote)"),
          "1842-george-proctor": ("footnote", "")}


def country(w):
    p = (w["place_publisher"] or "").lower()
    if "edinburgh" in p and "london" not in p:
        return "Scotland"
    if any(c in p for c in ("london", "cambridge", "oxford")):
        return "England"
    if any(c in p for c in ("new york", "philadelphia", "boston", "baltimore", "hartford", "chicago", "[us]")):
        return "US"
    if any(c in p for c in ("toronto", "montreal", "halifax", "quebec")):
        return "Canada"
    if "dublin" in p:
        return "Ireland"
    t = w["tradition"]
    if w["work_id"].startswith("sa-") and "eb" in w["work_id"]:
        return "Scotland"
    return {"US": "US", "Britain": "England"}.get(t, "")


def ords(cell):
    return [x for x in (cell or "").split(";") if x]


def fourth(w):
    h6, c = "4" in ords(w["H6"]), "4" in ords(w["C"])
    if h6 and c:
        return "both"
    if h6:
        return "H6"
    if c:
        return "C"
    if "5" in ords(w["C"]) and not ords(w["H6"]):
        return "other"
    return "none"


def fifth(w):
    f = [s for s in ("C", "D", "F") if "5" in ords(w[s])]
    if f == ["D", "F"]:
        return "D+F"
    return f[0] if len(f) == 1 else ("none" if not f else "other")


def edward(w):
    e, l2 = ords(w["E"]), ords(w["L2"])
    if not e:
        return ""
    if l2 and e == l2:
        return "ninth_with_tunis" if e == ["9"] else "inside_last"
    if e == ["9"]:
        return "ninth_alone"
    return "other_number"


def ninth(w):
    hits = [s for s in ("H6", "C", "D", "F", "B", "L1", "L2", "E") if "9" in ords(w[s])]
    if not hits:
        return ""
    if set(hits) == {"L2", "E"}:
        return "tunis+edward"
    if hits == ["L2"]:
        return "tunis"
    if hits == ["E"]:
        return "edward"
    return "other"


rows = []
for wid, w in works.items():
    if wid in have or w["language"] != "English":
        continue
    try:
        y = int(w["year_sort"][:4])
    except ValueError:
        continue
    if not 1788 <= y <= 1945:
        continue
    fam = w["scheme_family"]
    gc, gnote = GIBBON.get(wid, ("unchecked", ""))
    note = "derived from slots; not re-read in D2"
    if gnote:
        note += "; " + gnote
    rows.append(dict(work_id=wid, frame_id="", country_pub=country(w), fourth_identity=fourth(w),
                     fifth_identity=fifth(w), edward_status=edward(w), ninth_referent=ninth(w),
                     gibbon_cited=gc, gibbon_numbers=L.gibbon_numbers(w),
                     numbers_follow=(FOLLOW[fam] + ";inferred") if fam in FOLLOW else "unclear;inferred",
                     notes=note, checked_on=D))
L.upsert_attrs(rows)
print(len(rows), "derived attribute rows")

# Overrides after review: Edinburgh firms whose imprints put London first; the 1923 Barker reprint keeps
# EB11's text, so Edward is unnumbered there too.
L.upsert_attrs([
    dict(work_id="sd-1868-chambers-enc", country_pub="Scotland",
         notes="derived from slots; not re-read in D2; W. and R. Chambers, Edinburgh (imprint London and Edinburgh)"),
    dict(work_id="sd-1901-chambers-enc", country_pub="Scotland",
         notes="derived from slots; not re-read in D2; W. and R. Chambers, Edinburgh (imprint London and Edinburgh)"),
    dict(work_id="sd-1860-collier-great-events", country_pub="Scotland",
         notes="derived from slots; not re-read in D2; T. Nelson, Edinburgh (imprint London, Edinburgh and New York)"),
    dict(work_id="1923-ernest-barker", edward_status="named_unnumbered",
         notes="derived from slots; not re-read in D2; reprint of the EB11 article, so E cleared as there"),
])
L.upsert_works([dict(work_id="1923-ernest-barker",
                     notes=(works["1923-ernest-barker"]["notes"] + " | " if works["1923-ernest-barker"]["notes"]
                            else "") + "[D2 2026-11-28] E cleared with EB11 (same text)."
                     if "E cleared with EB11" not in works["1923-ernest-barker"]["notes"]
                     else works["1923-ernest-barker"]["notes"])],
               clear_slots=[("1923-ernest-barker", "E")])
print("overrides applied")
