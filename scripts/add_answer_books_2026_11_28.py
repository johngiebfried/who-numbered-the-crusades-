"""Direction D1: the question-14 answer books of 1829-36 (28 Nov 2026).

First session script under the reconciled model: edits data/works.csv directly, then
data/citations.csv, data/reasons/reasons.csv and data/search_log.csv. Idempotent.
Run scripts/derive_numberings.py afterwards. MIT License.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"
D = "2026-11-28"
WHO = "Claude (main session, browser)"
BASE = dict(language="French", tradition="France", genre="School", census_frame="strand_b_fr_1800_1842",
            organized_by="answers to the official question list (q. XIV, Histoire du moyen âge)",
            research_pass="strand_b", source_tables="", checked_on=D, access="Google Books text layer (browser)")

ROWS = [
    dict(BASE, work_id="sb-1829-delavigne-manuel",
         label="A. C. Delavigne, Manuel complet des aspirants au baccalauréat", author="A. C. Delavigne",
         work="Manuel complet des aspirants [au baccalauréat ès lettres]", year_label="1829", year_sort="1829",
         pages="207-208", url="https://books.google.com/books?id=S_fcziEXGj8C&pg=PA207",
         how_verified="Google Books text layer, q. XIV answer read in full", verification_level="full_text",
         title_page_checked="no", enumerates="partial",
         stated_phrase="Les cinquième et sixième croisades ... Les deux dernières, entreprises par Louis IX",
         D="5", F="6", highest_ordinal="6", numbering_shorthand="D 5, F 6", scheme_family="modern_eight",
         quote="(1217-1228) Les cinquième et sixième croisades ne furent signalées par aucun événement remarquable. (1248-1270) Les deux dernières, entreprises par Louis IX ...",
         notes="Numbers the first and second, narrates 1189 and 1202-04 without numbers, then 'cinquième et sixième' for 1217-1228 and 'les deux dernières' for Louis IX: the modern sequence by implication (C 4, L1 7, L2 8 implied, not stated). D 5 with F 6 is diagnostic of modern_eight. Does not copy Desmichels's wording. Title page not in the text layer; author and year from the Google record (National Library of Israel copy)."),
    dict(BASE, work_id="sb-1835-delavigne-manuel",
         label="A. C. Delavigne, Manuel complet des aspirants au baccalauréat", author="A. C. Delavigne",
         work="Manuel complet des aspirants [au baccalauréat ès lettres]", year_label="1835", year_sort="1835",
         pages="197-198", url="https://books.google.com/books?id=X7xLAAAAcAAJ&pg=PA197",
         how_verified="Google Books text layer, q. XIV answer read", verification_level="full_text",
         title_page_checked="no", enumerates="partial",
         stated_phrase="Les cinquième et sixième croisades dirigées par André, roi de Hongrie, et par l'empereur Frédéric",
         D="5", F="6", highest_ordinal="6", numbering_shorthand="D 5, F 6", scheme_family="modern_eight",
         quote="Les cinquième et sixième croisades dirigées par André, roi de Hongrie, et par l'empereur Frédéric, n'offrent de remarquable que la décadence rapide des colonies chrétiennes",
         notes="Revised from 1829: names Andrew of Hungary as leader of the fifth and Frederick II of the sixth. 'Les deux dernières' (1248-1270) for Louis IX (OCR 'Louis XII'). Same implied modern sequence as 1829."),
    dict(BASE, work_id="sb-1836-bouchitte-manuel",
         label="Bouchitté, Charma, Saigey and Lesieur, Manuel des aspirants au baccalauréat",
         author="Bouchitté and Charma, professeurs; Saigey and Lesieur, anciens élèves de l'École normale",
         work="Manuel des aspirants au baccalauréat ès-lettres, renfermant les réponses à toutes les questions ... contenues dans le Programme publié par l'Académie de Paris",
         year_label="1836", year_sort="1836", place_publisher="Paris: L. Hachette (impr. Mme Huzard)",
         pages="second pagination, pp. 157-163; footnote p. 158",
         url="https://books.google.com/books?id=-Tej2l1vxU4C&pg=RA1-PA159",
         how_verified="Google Books text layer, q. XIV answer read; footnote page image viewed (p. 158); title page by OCR",
         verification_level="full_text", title_page_checked="by OCR", enumerates="yes", stated_count="8",
         stated_phrase="8e et dernière croisade", C="4", D="5", F="6", L1="7", L2="8", highest_ordinal="8",
         numbering_shorthand="C 4, D 5, F 6, L1 7, L2 8", scheme_family="modern_eight", signature_match="modern",
         stemma_parent="sb-1827-desmichels-precis",
         parent_evidence="documented: footnote 'Nous avons adopté la division des croisades indiquée dans le Précis d'histoire du moyen-âge de M. Desmichels' (edition not stated)",
         quote="(1) Nous avons adopté la division des croisades indiquée dans le Précis d'histoire du moyen-âge de M. Desmichels.",
         organized_by="answers to the official question list (q. XIV), numbered section headings (2o croisade ... 7o croisade, 8e et dernière croisade)",
         notes="Headings 2o-7o and '8e et dernière croisade' (OCR 'Se et dernière'). The 4o heading opens with the crusade preached under Celestine III and 'interrompue à la mort de Henri VI', unnumbered, then 1202-04. 5o = the Lateran crusade led by the king of Hungary; 6o Frederick II; 7o Louis IX 1248; 8e Tunis. The co-author Saigey is probably J.-F. Saigey of the Traité de métrologie (1834; sb-1834-saigey-metrologie), which has Koch's slots; identity not checked."),
    dict(BASE, work_id="sb-1829-ponelle-manuel",
         label="Edme Ponelle, Manuel complet des aspirans au baccalauréat", author="[Edme Ponelle]",
         work="Manuel complet des aspirans au baccalauréat ès-lettres, renfermant les réponses à toutes les questions ... contenues dans le manuel publié par l'Académie de Paris",
         year_label="1829", year_sort="1829", place_publisher="Paris: Mansut fils (impr. C. Thuau)",
         pages="pp. 325-333", url="https://books.google.com/books?id=hltFAAAAIAAJ&pg=PA325",
         how_verified="Google Books text layer, q. XIV answer read; title page by OCR (no author or date in the excerpt)",
         verification_level="full_text", title_page_checked="by OCR", enumerates="partial",
         stated_phrase="lors de la quatrième croisade", C="4", highest_ordinal="4", numbering_shorthand="C 4",
         scheme_family="", quote="Les Français avaient, lors de la quatrième croisade, 1204 ...",
         notes="As in Ponelle 1826 (sb-1826-ponelle-nouveau-manuel): the q. XIV answer numbers nothing; the fourth (1204) and second appear in passing in neighboring answers. C 4 alone is not diagnostic. Author and year from the Google record."),
]

CITATION = {"citing_work_id": "sb-1836-bouchitte-manuel", "cited": "Desmichels, Précis de l'histoire du moyen âge (sb-1827-desmichels-precis; edition not stated)",
            "relation": "adopts its division of the crusades",
            "evidence": "Footnote 1, second pagination p. 158 (page image viewed): 'Nous avons adopté la division des croisades indiquée dans le Précis d'histoire du moyen-âge de M. Desmichels.'",
            "confidence": "documented"}

REASON = {"reason_id": "r28", "year": "1836", "work": "Manuel des aspirants au baccalauréat ès-lettres",
          "author": "Bouchitté, Charma, Saigey, Lesieur", "language": "fr", "entry_id": "sb-1836-bouchitte-manuel",
          "kind": "attribution", "target": "scheme", "expeditions_affected": "all",
          "phrase": "Nous avons adopté la division des croisades indiquée dans le Précis d'histoire du moyen-âge de M. Desmichels.",
          "verification": "full_text", "source": "D1 pass 2026-11-28 (Google Books -Tej2l1vxU4C, p. 158, image viewed)",
          "notes": "Earliest explicit attribution of the modern eight to a source. New kind 'attribution' (proposed)."}

LOG = [
    ["Google Books in-book search and text layer (browser)", "Delavigne, Manuel complet 1829 (S_fcziEXGj8C): croisade; q. XIV pp. 207-208", "1829", "2", "2", "sb-1829-delavigne-manuel"],
    ["Google Books in-book search and text layer (browser)", "Delavigne, Manuel complet 1835 (X7xLAAAAcAAJ): croisade; q. XIV pp. 197-198", "1835", "2", "2", "sb-1835-delavigne-manuel"],
    ["Google Books in-book search, text layer and page image (browser)", 'Bouchitté et al., Manuel des aspirants 1836 (-Tej2l1vxU4C): croisade; "division des croisades"', "1836", "2; 2", "4", "sb-1836-bouchitte-manuel; footnote naming Desmichels (p. 158)"],
    ["Google Books text layer (browser)", "Ponelle, Manuel complet 1829 (hltFAAAAIAAJ): q. XIV pp. 325-333", "1829", "3 chunks", "3", "sb-1829-ponelle-manuel"],
]


def rw(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def ww(path, cols, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


cols, works = rw(ROOT / "works.csv")
have = {w["work_id"] for w in works}
for r in ROWS:
    if r["work_id"] not in have:
        row = {c: "" for c in cols}
        for k, v in r.items():
            assert k in cols, k
            row[k] = v
        works.append(row)
works.sort(key=lambda w: (w["year_sort"] or "9999", w["work_id"]))
ww(ROOT / "works.csv", cols, works)

# citations.csv and reasons.csv are hand-kept LF files: append, do not rewrite.
for path, row, key in [(ROOT / "citations.csv", CITATION, "citing_work_id"),
                       (ROOT / "reasons" / "reasons.csv", REASON, "reason_id")]:
    cols, rows = rw(path)
    if not any(r[key] == row[key] for r in rows):
        with open(path, "a", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerow([row.get(c, "") for c in cols])

with open(ROOT / "search_log.csv", newline="", encoding="utf-8") as f:
    seen = {(x[0], x[1], x[2]) for x in csv.reader(f)}
add = [[D, c, q, df, h, he, wa, WHO] for c, q, df, h, he, wa in LOG if (D, c, q) not in seen]
with open(ROOT / "search_log.csv", "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(add)
print(f"works.csv {len(works)} rows; search_log +{len(add)}")
