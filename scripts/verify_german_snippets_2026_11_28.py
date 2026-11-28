"""Verify the five German schoolbook rows left at snippet level (28 Nov 2026).

Read in archive.org djvu text (BSB/MDZ and Polish library scans) through the browser.
Idempotent: updates rows by entry_id, adds one row if absent, appends search-log rows if absent.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DE = ROOT / "data" / "strand_b" / "entries_de.csv"
LOG = ROOT / "data" / "search_log.csv"
D = "2026-11-28"
WHO = "Claude (main session, browser)"
SEVEN = dict(C="4", F="5", L1="6", L2="7", highest_ordinal="7", enumerates="yes",
             scheme_family="frederick_fifth_seven", verification_level="full_text", checked_on=D,
             access="archive.org djvu text (browser)")

UPDATES = {
    "sb-de-1853-beitelrock-grundriss": dict(SEVEN,
        edition="2. Aufl.", place_publisher="Dillingen: Joseph Friedrich",
        url="https://archive.org/details/10031114bsb", title_page_checked="by OCR",
        pages="Zeittafel, Vierte Periode (pp. 434-435 by OCR)",
        stated_phrase="Der siebente Kreuzzug",
        quote="1204 Der vierte Kreuzzug ... 1228 Friedrich II. erlangt auf dem fünft. Kreuzzuge durch Vertrag Jerusalem ... 1248 Der sechste Kreuzzug unter Ludwig IX. v. Frankreich ... 1270 Der siebente Kreuzzug. Ludwig IX. stirbt vor Tunis.",
        notes="Full base form in the Zeittafel. The narrative (pp. 194-197) numbers only the second and third; 1203-04, Andrew (1217), Frederick II and Louis IX are narrated without numbers. Children's crusade 1213 unnumbered. Family code confirmed (was L1 6 only from a snippet)."),
    "sb-de-1854-dietsch-grundriss": dict(SEVEN,
        edition="Zweiter Theil", place_publisher="Leipzig: B. G. Teubner",
        url="https://archive.org/details/10031690bsb", title_page_checked="by OCR",
        pages="§§ 79-86; Zeittafel",
        stated_phrase="Der sechste (1248-1254) und siebente Kreuzzug 1270",
        quote="§ 84. Der vierte Kreuzzug 1202-1204 ... § 85. Der fünfte Kreuzzug 1227-29. Friedrich II. ... Der sechste (1248-1254) und siebente Kreuzzug 1270",
        notes="Damietta 1219-21 narrated without a number between §§ 84 and 85. Zeittafel agrees: 1202 vierter, 1228-29 fünfter, 1248-54 sechster Kreuzzug. Imprint from the Theil 3 title page (bub_gb_WpADAAAAcAAJ, Leipzig: Teubner, 1854); Theil 2 OCR has only the half-title."),
    "sb-de-1844-haas-kirchengeschichte": dict(SEVEN,
        url="https://archive.org/details/11287230bsb", title_page_checked="no",
        pages="Zeittafel, pp. 348-350 by OCR; narrative pp. 121-124",
        stated_phrase="Siebenter und letzter Kreuzzug",
        quote="1187. Dritter Kreuzzug. 1204. Vierter Kreuzzug. ... 1228. Fünfter Kreuzzug. ... 1248. Sechster Kreuzzug. Ludwig der [Heilige] ... 1270. Siebenter und letzter Kreuzzug.",
        notes="Title page OCR illegible; title and year from the BSB record ('nebst Namen-Sachregister und Zeittafel', für Schule und Volk). Narrative numbers the second and third; Andrew (1217) narrated without a number; Louis IX's 1248 expedition called 'seinem ersten Kreuzzuge' and 1270 'einen Zug'. Also 1846 ed. (not read)."),
    "sb-de-1860-kurts-tabellen": dict(SEVEN,
        place_publisher="Leipzig: T. O. Weigel",
        url="https://archive.org/details/10348116bsb", title_page_checked="by OCR",
        pages="Tables of the Dritter Zeitraum (1096-)",
        stated_phrase="Siebenter Kreuzzug 1270",
        quote="Erster Kreuzzug 1096 ... Dritter Kreuzzug [1189] ... Vierter Kreuzzug 1202 ... Erfolgloser Kreuzzug des Königs Andreas II. von Ungarn [1217] ... Fünfter Kreuzzug 1228. Kaiser Friedrich II. ... [S]echster [Kr]euzzu[g] 1248 ... Siebenter Kreuzzug 1270",
        notes="Synchronistic table; OCR runs across columns. The sixth is read from OCR split across columns and should be checked on the page image. The 1147 crusade appears as '1147 Kreuzzug' in the OCR. Andrew II named without a number."),
    "sb-de-1842-streit-atlas": dict(
        work="Neuer Atlas der ganzen Erde: German history table",
        author_editor="C. G. D. Stein (atlas; maps by Streit and others); tables by K. Th. Wagner per the 1847 and 1854 title pages",
        place_publisher="Leipzig: J. C. Hinrichs", url="https://archive.org/details/jbc.bj.uj.edu.pl.NDIGKART022297",
        access="archive.org djvu text (browser)", verification_level="full_text", title_page_checked="no",
        enumerates="partial", scheme_family="", highest_ordinal="5",
        quote="1096. Erster Kreuzzug ... 1147. Zweiter Kreuzzug ... 1189. Dritter Kreuzzug ... 1228. Fünfter Kreuzzug - 1229. Friedrich II. im Banne durch Gregor IX., gewinnt Jerusalem.",
        notes="German table only; no fourth in it, Louis IX not in it. F 5 alone is not diagnostic (german_six and larousse_eight share it), so the family code is cleared. The same atlas's universal-history table counts differently: see sb-de-1842-stein-atlas-universal. Title page OCR illegible; imprint and year from the archive.org record. Also 1852 ed. (rcin.org.pl copy, table dated 1849), same wording.",
        checked_on=D),
}

NEW = {
    "entry_id": "sb-de-1842-stein-atlas-universal",
    "work": "Neuer Atlas der ganzen Erde: universal-history table",
    "author_editor": "C. G. D. Stein (atlas); tables by K. Th. Wagner per the 1847 and 1854 title pages",
    "year_read": "1842", "place_publisher": "Leipzig: J. C. Hinrichs", "language": "de",
    "access": "archive.org djvu text (browser)", "url": "https://archive.org/details/jbc.bj.uj.edu.pl.NDIGKART022297",
    "verification_level": "full_text", "title_page_checked": "no", "census_frame": "strand_b_de_1780_1860",
    "enumerates": "yes", "stated_count": "5", "stated_phrase": "Fünfter u. letzter Kreuzzug",
    "F": "4", "L1": "5", "highest_ordinal": "5", "organized_by": "school history or table", "scheme_family": "other",
    "differing_slots": "fourth, fifth",
    "quote": "1096. Erster Kreuzzug ... 1147. Zweiter Kreuzzug ... 1189. Dritter Kreuzzug ... 1228. Vierter Kreuzzug. Erneuerung des Königr. Jerusalem (- 1244). ... 1248. Fünfter u. letzter Kreuzzug nach Ägypten (- 1250). Ludwig IX.",
    "notes": "Five crusades, Frederick II fourth, Louis IX's 1248 crusade the fifth and last. 1202-04 appears only in the Italian table as the conquest of Constantinople by the crusaders, unnumbered; Damietta and Andrew absent; Tunis appears in the French table as 'Kreuzzug gegen Tunis', unnumbered. The 1842 OCR misreads 1228 as 1298; the 1852 copy (table dated Leipzig 1849) reads 1228 and has the same wording. Conflicts with the same atlas's German table (sb-de-1842-streit-atlas, F 5).",
    "checked_on": D,
}

LOG_ROWS = [
    ["archive.org advancedsearch and djvu text (browser)", "Beitelrock, Grundriß 1853 (10031114bsb): ordinals with Kreuzzug; Zeittafel", "1853", "1", "1", "sb-de-1853-beitelrock-grundriss upgraded to full_text; family code confirmed"],
    ["archive.org advancedsearch and djvu text (browser)", "Dietsch, Grundriß 1854 Theil 2 (10031690bsb), Theil 3 (bub_gb_WpADAAAAcAAJ)", "1854", "2", "2", "sb-de-1854-dietsch-grundriss upgraded to full_text"],
    ["archive.org advancedsearch and djvu text (browser)", "Haas, Populäre Kirchengeschichte 1844 (11287230bsb)", "1844", "1", "1", "sb-de-1844-haas-kirchengeschichte upgraded to full_text"],
    ["archive.org advancedsearch and djvu text (browser)", "Kurts, Geschichtstabellen 1860 (10348116bsb)", "1860", "2", "1", "sb-de-1860-kurts-tabellen upgraded to full_text (sixth from split OCR)"],
    ["archive.org advancedsearch and djvu text (browser)", 'title:("Atlas der ganzen Erde") AND mediatype:texts; creator:(Streit) AND title:(Atlas)', "none", "4; 30+", "2", "Stein, Neuer Atlas 1842 (jbc.bj.uj.edu.pl.NDIGKART022297) and 1852 (rcin.org.pl) read; row split into German table and new sb-de-1842-stein-atlas-universal"],
]


def main():
    with DE.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols, rows = r.fieldnames, list(r)
    ids = {row["entry_id"]: row for row in rows}
    for eid, upd in UPDATES.items():
        assert eid in ids, eid
        for k, v in upd.items():
            assert k in cols, k
            ids[eid][k] = v
    if NEW["entry_id"] not in ids:
        new = {c: "" for c in cols}
        new.update(NEW)
        i = rows.index(ids["sb-de-1842-streit-atlas"])
        rows.insert(i + 1, new)
    with DE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    with LOG.open(newline="", encoding="utf-8") as f:
        have = {(x[0], x[1], x[2]) for x in csv.reader(f)}
    add = [[D, c, q, df, h, he, wa, WHO] for c, q, df, h, he, wa in LOG_ROWS if (D, c, q) not in have]
    with LOG.open("a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(add)
    print(f"updated {len(UPDATES)}, search_log +{len(add)}")


if __name__ == "__main__":
    main()
