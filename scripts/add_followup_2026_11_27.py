"""Follow-up of 27 Nov 2026: Marchand t. 1, Recueil t. 7, catalog search for the
1822 Tableau sommaire, BnF reproduction prices for G-31078.

Idempotent: appends search-log rows only if absent, rewrites two not_reached rows.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "data" / "search_log.csv"
NR = ROOT / "data" / "strand_b" / "not_reached.csv"
WHO = "Claude (main session, browser)"
D = "2026-11-27"

LOG_ROWS = [
    ["Persée page text (browser)", "Marchand (ed.), L'histoire et la géographie dans l'enseignement secondaire: textes officiels, t. 1 (INRP 2000): texts 17, 20, 21, 23, 24; introduction pp. 29-31", "1818-1826", "5 texts", "5", "Curriculum dates confirmed (circular 4 July 1820; statute 4 Sept 1821 arts. 172, 176); no question table printed; Desmichels not mentioned"],
    ["Google Books search (browser)", '"Recueil de lois et règlemens concernant l\'instruction publique" "13 mars 1821"', "1824", "3", "3", "R.L.R. t. 7 in full view (--Ek8YYtTQ4C; 5qzeAAAAMAAJ; 4wNSAAAAcAAJ)"],
    ["Google Books text layer and in-book search (browser)", "R.L.R. t. 7 (--Ek8YYtTQ4C): règlement 13 March 1821; in-book: croisades, \"tableau des questions\", \"15 janvier 1822\", \"Histoire du moyen âge\"", "1824", "n/a", "4 pages", "Règlement read: art. 6 orders a question table, none printed; arrêté 15 Jan 1822 on formalities only"],
    ["Google Books search (browser)", '"Tableau sommaire pour servir à l\'enseignement de l\'histoire moderne"', "none", "3", "3", "None; references only (Desmichels 1823 ad; BdF 1822; Misan 1985 p. 27)"],
    ["BnF catalogue général SRU (browser)", 'bib.author all "Trognon Auguste"', "none", "36", "36", "None; Trognon, Discours ... cours d'histoire moderne, 18 Apr 1822 (cb314979812) noted"],
    ["BnF catalogue général SRU (browser)", 'bib.title all "tableau sommaire" and bib.publisher all "Colas"; bib.title all "histoire moderne" and bib.publisher all "Colas"', "none", "2; 7", "9", "None; 1820 Tableau sommaire only; Michelet, Tableau chronologique de l'histoire moderne (Colas 1825) noted"],
    ["SUDOC (browser)", "Trognon Desmichels tableau; tableau sommaire histoire moderne", "none", "1; 2", "3", "None; 1820 edition only (PPN 098106228)"],
    ["KVK (browser)", "TI tableau sommaire histoire moderne, AU Trognon (BVB, K10plus, SWB, Jisc, BNE; BnF and BL failed)", "none", "0", "0", "None"],
    ["CCFr federated (browser)", "Trognon Desmichels tableau sommaire; Trognon tableau", "none", "0", "0", "None; zero even for the 1820 edition, so the scripted search is not trusted"],
    ["HathiTrust catalog; Emmanuelle (browser)", "Trognon tableau sommaire", "none", "not reached", "0", "HathiTrust bot check; inrp.fr/emma did not load"],
    ["BnF reproduction cart (browser)", "G-31078 product options and prices", "1822", "n/a", "n/a", "Full PDF EUR 45 excl. VAT; per-page PDF EUR 0.70/page excl. VAT; nothing ordered"],
]

NR_UPDATES = {
    "Questions sur l'histoire ancienne": (
        "Not digitized (Gallica, Google Books, archive.org searched 2026-11-27). BnF reproduction: per-page PDF EUR 0.70/page excl. VAT (3-4 weeks), full PDF EUR 45 excl. VAT (5-7 weeks); not ordered",
        "Highest. Probably the first printing of the official baccalauréat question table ordered by the règlement of 13 March 1821, art. 6 (R.L.R. t. 7). Its Middle Ages q. 14 decides whether the Université's examination numbered the crusades before Desmichels's Tableau chronologique (registered 21 Dec 1822).",
    ),
    "Trognon and Desmichels, Tableau sommaire pour servir": (
        "No copy found: not in BnF catalogue général (SRU), SUDOC, BVB, K10plus, SWB, Jisc, BNE; not digitized (Google Books, Gallica). Not reached: WorldCat (terms gate), CCFr (scripted search unreliable), HathiTrust (bot check), Emmanuelle (did not load)",
        "High. Second edition of the official 1820 outline, retitled for seconde's histoire moderne under the statute of 4 Sept 1821 (art. 176). Shows whether the October 1822 revision kept any Middle Ages and, if so, which count.",
    ),
}


def main():
    with LOG.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    have = {(r[0], r[1], r[2]) for r in rows[1:]}
    new = [[D, c, q, df, h, he, w, WHO] for c, q, df, h, he, w in LOG_ROWS if (D, c, q) not in have]
    with LOG.open("a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(new)

    with NR.open(newline="", encoding="utf-8") as f:
        nr = list(csv.reader(f))
    for r in nr[1:]:
        for key, (why, prio) in NR_UPDATES.items():
            if r[0].startswith(key):
                r[2], r[3] = why, prio
    with NR.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(nr)
    print(f"search_log +{len(new)}; not_reached updated")


if __name__ == "__main__":
    main()
