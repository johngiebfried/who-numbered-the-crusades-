"""27 Nov 2026 session: the 1820-23 window (direction A) and the verification
pass (direction B). Idempotent.

1. Renames the print scheme family `german_seven` to `frederick_fifth_seven`
   (and `german_seven_variant` to `frederick_fifth_seven_variant`) in the
   strand tables. The Wikipedia lane keeps its own `count_family` labels.
2. Updates verified rows in place (by entry_id).
3. Appends new rows, not-reached rows and search-log rows, skipping any
   already present.
"""
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = '2026-11-27'
WHO = 'Claude (main session, browser)'

RENAME = {'german_seven': 'frederick_fifth_seven',
          'german_seven_variant': 'frederick_fifth_seven_variant'}
STRAND_TABLES = ['data/strand_a/entries.csv', 'data/strand_a/entries_de.csv',
                 'data/strand_b/entries.csv', 'data/strand_b/entries_de.csv',
                 'data/strand_d/entries_en.csv', 'data/panel/entries_fr.csv']

GB = 'Google Books text layer (output=text, browser)'
DJ = 'archive.org djvu text of BSB copy (browser)'


def load(path):
    with open(os.path.join(ROOT, path), newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def save(path, cols, rows):
    with open(os.path.join(ROOT, path), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, cols)
        w.writeheader()
        w.writerows(rows)


def blank(cols, **k):
    r = {c: '' for c in cols}
    r.update({c: str(v) for c, v in k.items()})
    r['checked_on'] = D
    return r


# ---------------------------------------------------------------- updates
UPDATES = {
 'data/strand_b/entries.csv': {
  'sb-1820-desmichels-trognon-tableau-sommaire': dict(
    organized_by='official course outline (Commission d\'instruction publique)',
    notes="Title page (ALTO view 3): 'COMMISSION D'INSTRUCTION PUBLIQUE. TABLEAU SOMMAIRE DU COURS D'HISTOIRE GÉNÉRALE. PARIS, CHEZ L. COLAS ... 1820.' View 4: 'Ce tableau historique a été rédigé par MM. Desmichels et Auguste Trognon, professeurs d'histoire aux colléges royaux de Henri IV et Louis-le-Grand'; the avertissement says the authors 'ont cru devoir excéder les limites d'un simple programme'. Registered in the Bibliographie de la France, April 1820, no. 1350, next to no. 1351 'Programme du cours de l'Histoire de France dans les collèges royaux' and no. 1352 'Programme pour l'enseignement de l'histoire ancienne dans les collèges royaux' (same printer, Fain; same publisher, Colas; all in-4). The course runs from 395 into the 18th century (ch. XXXIX). Ch. XIV 'De l'Orient et des croisades' re-read 2026-11-27 (views 17-18): Andrew II's expedition named, not numbered; 'Résultats généraux des croisades' closes the chapter. Scheme coded frederick_fifth_seven (formerly german_seven), attested here in an official Paris programme."),
  'sb-1823-desmichels-tableau-chronologique': dict(
    notes="Earliest complete modern eight found. Title page image viewed 2026-11-23 (Complutense copy); title page text re-read 2026-11-27: no 'autorisé par le Conseil royal' line. Registered in the Bibliographie de la France, N° 51, Saturday 21 December 1822, no. 5716 ('In-8° de 11 feuilles 1/4. Imprimerie de Fain ... chez Louis Colas'), so the 1823 title-page date is a post-date and Larousse's 'Paris, 1822' is best read as the registration year. BnF holds only the 1823-dated printing (G-22668; Arsenal 8-NF-44836). Half-title verso lists the Colas series for the collèges royaux: Poirson and Caix, du Rozoir, Trognon and Desmichels, Boismilon, Ragon. The Revue encyclopédique (1823, no. 142, p. 359) calls the series works 'que l'Université ... a commandées' and says this volume 'complète cette collection'. Voss (1972, p. 92) calls it the first French school textbook on the Middle Ages. No preface; no authority cited for the numbering."),
  'sb-1824-manuel-aspirans-bac': dict(
    title_page_checked='yes (images: t. I and t. I, part III title pages, Paris: Auguste Delalain, 1824)',
    notes="Bibliographic data from the Google Books about page (Lyon, Bibliothèque jésuite des Fontaines copy); dates confirmed from the title-page images 2026-11-27. The history part is organized by the numbered questions of the baccalauréat table: the crusades are its '§ XIV', the answer to question 14 ('Précis historique des croisades'), and that answer copies Desmichels's 1823 list. Shows the 1823 scheme in a baccalauréat cram manual one year later."),
 },
 'data/strand_a/entries.csv': {
  'sa-1842-complement-academie': dict(
    pages='295 (MDZ canvas 335)', access='MDZ hOCR and IIIF page images (browser)',
    url='https://www.digitale-sammlungen.de/en/view/bsb10627876?page=335',
    verification_level='full_text',
    title_page_checked='yes (image, MDZ canvas 7: Paris, Firmin Didot frères, 1842)',
    notes="Third Paris reference work of 1842 with the modern eight, and the first statement of custom about SLOTS, not just the total: the Henry VI fourth is named as the minority usage. Whole entry read in hOCR 2026-11-27 and checked against the page image (fourth to eighth and the closing statement). The fourth is said to be 'commandée par Thibaud IV, comte de Champagne' (sic); the sixth is dated 1227; Tunis is 'Croisade de saint Louis ou huitième croisade'. Publisher Didot = Le Bas's publisher. Title page lists Narcisse Landois, professeur au collège royal de Bourbon (Bouillet's collège), among the collaborators."),
 },
 'data/strand_a/entries_de.csv': {
  'sa-de-1756-broughton-lexicon': dict(
    volume='2 (K-Z)',
    title_page_checked="no title page in Theil 2: half-title 'Broughtons Historisches Lexicon aller Religionen. Zweyter Theil. K bis Z.' viewed (archive.org leaf n7); imprint Dresden und Leipzig: Walther, 1756, from the BSB record",
    notes="Fifth = the 1202-04 contingent that reached Acre (ends 1204). Sixth fuses Damietta and Frederick II under 1228 (Moréri's D+F sixth). Seventh = Louis IX 1249. Tail not read. Entry re-read in OCR 2026-11-27. Hoff, Historisch-kritische Encyklopädie (1787) copies the sixth-crusade sentence (with 1328 for 1228)."),
 },
 'data/strand_d/entries_en.csv': {
  'sd-1908-brehier-catholic-enc': dict(
    access='archive.org djvu text of the 1908 Robert Appleton printing (browser); New Advent transcription',
    url='https://archive.org/details/07470918.4.emory.edu',
    pages="'Division' paragraph, end of p. 544 (p. 545 follows)",
    title_page_checked='yes (OCR text of title page and verso: New York, Robert Appleton Company; Copyright, 1908)',
    notes="French author; source of Wikipedia 2001 date ranges. Quote re-checked 2026-11-27 against the OCR of the 1908 Appleton printing (Emory copy; also b33397491_0004): the sixth is Frederick II's (1228-29) 'also Thibaud de Champagne and Richard of Cornwall (1239)', hence B 6. The Knights of Columbus special edition (catholicencyclop04herbuoft) has the same text and pagination."),
 },
 'data/strand_b/entries_de.csv': {
  'sb-de-1834-fiedler-tafeln': dict(
    work='Historisch-genealogische Tafeln der wichtigsten Regentenhäuser in dem Mittelalter und in der neueren Zeit, besonders für den historischen Unterricht in Gymnasien und Militairschulen',
    author_editor='Franz Fiedler, Oberlehrer am Gymnasium in Wesel', place_publisher='Wesel: Joh. Ad. Klönne',
    access=DJ.replace('of BSB copy ', 'of Google scan '), url='https://archive.org/details/bub_gb_z6ZBAAAAcAAJ',
    pages='table of popes (Gregory VII to Boniface VIII)', verification_level='full_text',
    title_page_checked='yes (OCR text: Wesel 1834, Klönne)', enumerates='yes',
    stated_phrase='Siebenter u. letzter Kreuzzug', C='4', D='', F='5', L1='6', L2='7', highest_ordinal='7',
    organized_by='genealogical and chronological tables', scheme_family='frederick_fifth_seven',
    quote='Vierter Kreuzzug 1201 ... Fünfter Kreuzzug 1228. Friedrich II. im Bann ... Sechster Kreuzzug 1247 ... Siebenter u. letzter Kreuzzug 1270',
    notes="Full base form of the Frederick-fifth seven, ending 'Siebenter u. letzter'. Quote normalized from OCR ('Kreuzzng', 'Krcu/.ziig'); years as printed in the OCR (1201, 1247), not checked against the page image. Andrew II's 'Kreuzzug 1217' appears unnumbered in the Hungarian table. Read 2026-11-27; the 2026-11-23 snippet row had only F 5 and L1 6."),
  'sb-de-1835-handbuch-schule-haus': dict(
    work='Handbuch der allgemeinen Weltgeschichte für Schule und Haus',
    author_editor="anon.; 'bearbeitet nach den Werken von Annegarn, Döllinger, Hortig, Wiedemann u. A.'",
    place_publisher='Regensburg and Landshut: G. Joseph Manz', access=DJ,
    url='https://archive.org/details/10032020bsb', pages='contents, ch. XVIII; pp. c. 270-285',
    verification_level='full_text', title_page_checked='yes (OCR text: Regensburg und Landshut, 1835, Manz)',
    enumerates='yes', C='4', D='5', F='5', L1='6', L2='7', highest_ordinal='7',
    organized_by='school history, numbered sections', scheme_family='frederick_fifth_seven',
    quote='6. Der fünfte Kreuzzug. Andreas II. Johann von Brienne — Friedrich II. 7. Der sechste Kreuzzug. Ludwig der Heilige. 8. Der siebente Kreuzzug. Ludwig der Heilige.',
    notes="Merged-fifth form (Andrew, John of Brienne and Frederick II under one fifth). Quote from the contents, normalized from OCR ('Andreas 1.', 'Friedrich IJ.'). The fourth section ('Der vierte Kreuzzug 1202-1204') opens with Henry VI's army of 1196 without counting it. A Catholic compilation from Annegarn's and Wiedemann's world histories 'für die katholische Jugend' (preface), so the seven is not a Protestant-only count. Same contents in the 1838 edition (10032021bsb). Read 2026-11-27."),
  'sb-de-1839-uschold-grundriss': dict(
    work='Grundriß der allgemeinen Geschichte für lateinische Schulen und Anfänger',
    author_editor='Joh. Nep. Uschold, Professor am königl. bayer. Gymnasium in Straubing',
    edition='2nd (Zweite, verbesserte Auflage)', place_publisher='München: Joseph Lindauer', pages='75 (§ 73)',
    access=DJ, url='https://archive.org/details/10034254bsb', verification_level='full_text',
    title_page_checked='yes (OCR text: München, 1839, Lindauer)', enumerates='partial',
    C='4', D='5', F='5', L1='', L2='', highest_ordinal='5', organized_by='school history',
    scheme_family='frederick_fifth_seven', quote='Der fünfte Kreuzzug dauerte von 1217 — 1229',
    notes="Merged fifth (1217-1229). The fourth is 'der vierte Zug' (Constantinople 1204). Louis IX's crusades (1248-54, Tunis) are narrated without numbers. Correction: the 2026-11-23 row gave L1 6, which comes from Mertl's 1847 school version ('Der sechste Kreuzzug unter Ludwig IX.'), not from Uschold 1839. Bavarian Latin schools. Read 2026-11-27."),
  'sb-de-1849-weber-lehrbuch': dict(
    work='Lehrbuch der Weltgeschichte mit besonderer Rücksicht auf Cultur, Literatur und Religionswesen, Bd. 1',
    author_editor='Georg Weber, Professor ... bei der höhern Bürgerschule in Heidelberg',
    edition='3rd (Dritte erweiterte ... Auflage)', place_publisher='Leipzig: Wilhelm Engelmann',
    pages='§§ 323-326 (pp. 365 ff.); contents §§ 333-335', access=DJ,
    url='https://archive.org/details/10034275bsb', verification_level='full_text',
    title_page_checked='yes (OCR text: Leipzig, Engelmann, 1849)', enumerates='partial',
    C='4', D='', F='5', L1='', L2='', highest_ordinal='5', organized_by='school history, numbered sections',
    scheme_family='frederick_fifth_seven',
    quote='Nach solchen Vorgängen unternahm endlich der mit dem Bannfluch beladene Kaiser Friedrich II. den fünften Kreuzzug',
    notes="Section title 'Vierter und fünfter Kreuzzug (1203-1229)'. Quote normalized from OCR ('Bann' illegible in 1849; read in 1847). The fifth is Frederick II's (§ 326); Andrew II's expedition and Damietta are narrated in § 325 without a number; Louis IX's crusades are 'Ludwigs (IX.) des Heiligen Unternehmungen' (§§ 333-335). No 'sechster' or 'siebenter Kreuzzug' anywhere in the volume's text. Correction: the 2026-11-23 row coded D 5 from the section title. First edition 1847: see sb-de-1847-weber-lehrbuch-1. Read 2026-11-27."),
 },
}

# ---------------------------------------------------------------- new rows
def new_rows(cols_b, cols_bde):
    fr = [
     blank(cols_b, entry_id='sb-1826-hubert-tableau-questions-bac',
       work="Tableau des questions [du baccalauréat ès lettres], deuxième série, deuxième section: Histoire du Moyen Age",
       author_editor="Université royale de France (question table in force under the règlement of 13 March 1821), printed in L. Hubert, Manuel des lois et règlemens sur les études et l'exercice des diverses parties de la médecine",
       edition='as printed by Hubert', year_read='1826', place_publisher='Paris: Gabon et Cie',
       pages='3 (règlement note); 14-16 (q. 14 on p. 16)', headword='q. 14', language='fr',
       access='Google Books page images and text layer (browser)',
       url='https://books.google.at/books?id=JBI7AAAAcAAJ&pg=PA16', verification_level='full_text',
       title_page_checked='yes (image of printed wrapper: Paris, Gabon et Cie, 1826)',
       census_frame='strand_b_fr_1800_1842', enumerates='no', organized_by='official examination question list',
       scheme_family='none', signature_match='no',
       quote="État de l'empire d'Orient et de l'Asie, à la fin du XIe siècle. — Précis historique des croisades. — Résultats généraux des guerres saintes.",
       notes="Series 2 (history and geography), section 2 'Histoire du Moyen Age', nos. 1-25; 'Histoire moderne' from no. 26. Hubert's note on p. 3 refers the drawing of questions by lot to the 'Règlement du 13 mars 1821, art. 6'. Question 14 asks for a 'précis historique des croisades' and numbers none. It follows the topics of ch. XIV of the 1820 Tableau sommaire without its ordinals. Same wording in Ponelle 1826 (q. XIV), Delavigne 1829 and 1835, Bouchitté 1836 and Ponelle 1829 (not coded). The history questions were printed as 'Questions sur l'histoire ancienne, l'histoire romaine, l'histoire du moyen âge, l'histoire moderne' by Brunot-Labbe, libraire de l'Université (Bibliographie de la France 15 June 1822, no. 2839; again 28 Dec 1822, no. 5792); the 1822 printing (BnF G-31078, 44 p.) is unread, so the 1822 wording is not confirmed. Page images of pp. 3 and 16 viewed."),
     blank(cols_b, entry_id='sb-1826-ponelle-nouveau-manuel',
       work="Nouveau manuel complet des aspirans au baccalauréat ès-lettres, renfermant les réponses à toutes les questions ... contenues dans le Manuel publié par l'Académie de Paris",
       author_editor='Edme Ponelle', edition='Partie 1', year_read='1826', place_publisher='Paris: Mansut fils',
       pages='168-170 (q. XIV)', language='fr', access='Gallica ALTO and ContentSearch (browser)',
       url='https://gallica.bnf.fr/ark:/12148/bpt6k97585500', verification_level='full_text',
       title_page_checked='yes (ALTO text, view 7: Paris, Mansut fils, 1826)',
       census_frame='strand_b_fr_1800_1842', enumerates='partial', C='4', highest_ordinal='4',
       organized_by='answers to the official question list', signature_match='no',
       quote='Les Français avaient, lors de la quatrième croisade, pris Constantinople',
       notes="Reprints q. XIV of the baccalauréat table as its heading and answers it with a narrative that numbers nothing but the fourth (1204), in passing. The 1824 Delalain Manuel answers the same question with Desmichels's numbered list, so the numbers were not required by the examination."),
    ]
    de = [
     blank(cols_bde, entry_id='sb-de-1847-weber-lehrbuch-1',
       work='Lehrbuch der Weltgeschichte mit Rücksicht auf Cultur, Literatur und Religionswesen',
       author_editor='Georg Weber, Hauptlehrer bei der höhern Bürgerschule in Heidelberg', edition='1st',
       year_read='1847', place_publisher='Leipzig: Wilhelm Engelmann', pages='§ 323 ff. (pp. 218-220)', language='de',
       access=DJ, url='https://archive.org/details/10034274bsb', verification_level='full_text',
       title_page_checked='yes (OCR text: Leipzig, Engelmann, 1847)', census_frame='strand_b_de_1780_1860',
       enumerates='partial', C='4', F='5', highest_ordinal='5', organized_by='school history, numbered sections',
       scheme_family='frederick_fifth_seven', quote='Kaiser Friedrich II. den fünften Kreuzzug',
       notes="First edition of Weber's Lehrbuch (the 2026-11-23 row dated the work by its 1849 third edition). Same scheme as 1849: fifth = Frederick II; Andrew's expedition unnumbered; no sixth or seventh in the text. OCR poor (left margin cropped); read 2026-11-27."),
    ]
    return fr, de

NOT_REACHED_B = [
 ["Questions sur l'histoire ancienne, l'histoire romaine, l'histoire du moyen âge, l'histoire moderne (Paris: Brunot-Labbe, libraire de l'Université; impr. Fain)",
  "1822, 44 p. (BnF G-31078; Bibliographie de la France 15 June 1822, no. 2839; reissued 28 Dec 1822, no. 5792); 1823, 48 p. (BnF 16-G-434); 1823 (BnF J-24079, missing at récolement)",
  "Not digitized (Gallica, Google Books, archive.org searched 2026-11-27)",
  "Highest. The 1822 wording of the crusade question (Middle Ages q. 14) decides whether the Université's examination numbered the crusades before Desmichels's Tableau chronologique (registered 21 Dec 1822)."],
 ["Trognon and Desmichels, Tableau sommaire pour servir à l'enseignement de l'histoire moderne, 2e éd., 'Ouvrage autorisé par le conseil royal de l'instruction publique'",
  "Paris: L. Colas, 1822 (Bibliographie de la France 26 Oct 1822, no. 4729; in-8 de 4 f. 1/2)",
  "No copy found: not in BnF catalogue général or SUDOC; not digitized; WorldCat not searched (terms gate)",
  "High. Second edition of the official 1820 outline. Shows whether the October 1822 revision kept the Middle Ages and, if so, which count."],
 ["Programme du cours de l'Histoire de France dans les collèges royaux; Programme pour l'enseignement de l'histoire ancienne dans les collèges royaux",
  "Paris: L. Colas, 1820 (Bibliographie de la France 1820, nos. 1351-1352, in-4)",
  "Not digitized; BnF holdings not checked",
  "Low for numbering. Confirms the 1820 set of official programmes for the history courses."],
 ["Boismilon, Tables synchroniques à l'usage des cours d'histoire ancienne et moderne",
  "Paris: Colas, 1820, in-4, 36 p. (Journal des savants 1820, p. 761)",
  "Not digitized (Gallica SRU, Google Books)",
  "Low to medium. Synchronic tables for the same course may number the crusades."],
]

S = 'Gallica SRU (browser)'
LOG = [
 [D, S, "gallica all \"Commission d'instruction publique\" and gallica all \"cours d'histoire\"", '1818-1822', '1452', '50', 'none (noise)'],
 [D, S, 'dc.title all "tableau sommaire du cours"', '', '4', '4', 'none new (1820 Tableau sommaire)'],
 [D, S, 'dc.creator all "Desmichels"; dc.creator all "Trognon"', '', '13; 8', '21', 'none new'],
 [D, S, 'dc.title all "recueil" "instruction publique" "règlemens"; dc.title all "lois et règlemens" "instruction publique"', '', '5; 27', '32', 'none before 1830 (Brunot-Labbe Recueil 1814-28 not on Gallica)'],
 [D, S, 'dc.title all "statut" and dc.title all "collèges"', '1819-1824', '0', '0', 'none'],
 [D, S, 'dc.title all "cours d\'histoire"', '1818-1824', '16', '16', 'none new'],
 [D, S, 'dc.publisher all "Colas"', '1819-1825', '35', '35', 'Michelet, Tableau chronologique de l\'histoire moderne (1825) noted, not coded'],
 [D, S, 'dc.title all "baccalauréat"', '1819-1826', '2', '2', 'sb-1826-ponelle-nouveau-manuel'],
 [D, S, 'dc.creator all "Boismilon"; dc.title all "tables synchroniques" (to 1830); dc.title all "programme" and "histoire" (1818-1823)', '', '0; 0; 0', '0', 'none'],
 [D, S, 'dc.creator all "Poirson" (to 1830); dc.creator all "Ragon" (to 1835)', '', '224; 60', '50', 'none (noise)'],
 [D, S, 'dc.creator all "Ponelle"', '', '12', '12', 'Ponelle 1826 Partie 1'],
 [D, 'Gallica ContentSearch (browser)', 'Bibliographie de la France 1822 (bpt6k64262646): Desmichels; "Questions sur l\'histoire"; SAMEDI (issue headers)', '1822', '5; 3; 65', 'all', 'nos. 2839 (15 June), 4729 (26 Oct), 5716 (21 Dec), 5792 (28 Dec 1822); not_reached rows'],
 [D, 'Gallica ContentSearch (browser)', 'Almanach de l\'Université royale 1822 (bd6t54187029w): Desmichels; Trognon; histoire; programme', '1822', '0; 1; ~40; ~14', '~20', 'none for numbering'],
 [D, 'Gallica ContentSearch (browser)', 'Ponelle 1826 (bpt6k97585500): croisade; questions', '1826', '14; 10', 'all', 'q. XIV and its answer read'],
 [D, 'Google Books (browser)', '"Tableau chronologique de l\'histoire du moyen âge" Desmichels', '1820-1826', '~10', '~10', 'Bibliographie de la France 1822 index; Revue encyclopédique 1823 p. 359; Michelet 1825-26'],
 [D, 'Google Books (browser)', 'Desmichels "Tableau chronologique"', '1821-1822', '6', '6', 'Bibliographie de la France 1822, no. 5716 (no 1822-dated printing found)'],
 [D, 'Google Books in-book search (browser)', 'Bibliographie de la France 1822 (6DAGAAAAQAAJ): Desmichels; 5716; "histoire du moyen âge"; "Questions sur l\'histoire"; Colas', '1822', 'n/a', 'n/a', 'entries 2839, 4729, 5716, 5792 read'],
 [D, 'Google Books (browser)', '"Tableau sommaire du cours d\'histoire"', '1819-1824', '7', '7', 'Bibliographie de la France 1820, nos. 1350-1352; Censeur européen 1820 advertisement'],
 [D, 'Google Books (browser)', '"Tableau sommaire pour servir à l\'enseignement de l\'histoire moderne"', '', '4', '4', 'no copy (not_reached)'],
 [D, 'Google Books (browser)', '"Questions sur l\'histoire ancienne" "moyen âge" croisade; "questions sur l\'histoire ancienne, l\'histoire romaine"', '1819-1835', '0; 4', '4', 'no copy (not_reached)'],
 [D, 'Google Books (browser)', '"4 septembre 1821" statut collèges histoire "moyen âge"; "histoire du moyen âge" "collèges royaux" statut 1821 classe "histoire moderne"', '1821-1835', '2; 1', '3', 'none (1821 statute text not found)'],
 [D, 'Google Books (browser)', '"Résultats généraux des guerres saintes"', '1819-1840', '8', '8', 'sb-1826-hubert-tableau-questions-bac (Hubert 1826); leads: Delavigne 1829, 1835; Bouchitté 1836; Ponelle 1829'],
 [D, 'Google Books (browser)', 'Boismilon "tables synchroniques"', '1820-1830', '9', '9', 'Journal des savants 1820 p. 761; Revue encyclopédique 1823 p. 359 (not_reached)'],
 [D, 'BnF catalogue général (browser)', 'Trognon Desmichels tableau sommaire; tableau sommaire enseignement histoire moderne; Desmichels tableau chronologique moyen age; questions histoire ancienne histoire romaine moyen age histoire moderne', '', '1; 0; 1; 4', 'all', 'Tableau chronologique only 1823 (G-22668); Questions 1822 G-31078, 1823 16-G-434, J-24079 (missing)'],
 [D, 'SUDOC (browser)', 'Trognon tableau sommaire', '', '1', '1', '1820 edition only'],
 [D, 'WorldCat (browser)', 'ti:tableau sommaire au:trognon', '1819-1830', 'n/a', '0', 'not reached: terms-of-service gate not accepted'],
 [D, 'archive.org FTS (browser)', '"Fünfter Kreuzzug" Fiedler (1830-40); "fünfte Kreuzzug" "Johann von Brienne" "Friedrich II" (1834-46); "fünfte Kreuzzug dauerte" (1835-50); "Vierter und fünfter Kreuzzug" (1845-55)', '1830-1855', '1; 3; 1; 7', '12', 'located Fiedler 1834, Handbuch 1838, Uschold 1839, Weber 1847-54; rows verified'],
 [D, 'archive.org FTS (browser)', '"fünfte Kreuzzug" "Andreas II" (1830-37); "Schule und Haus" Weltgeschichte Kreuzzug (1834-36)', '1830-1837', '0; 19', '19', 'Handbuch 1835 (10032020bsb)'],
 [D, 'archive.org advancedsearch (browser)', 'Catholic Encyclopedia vol. 4, 1907-1909', '1907-1909', '6', '4', '1908 Appleton printing (07470918.4.emory.edu); Bréhier row re-checked'],
 [D, 'MDZ IIIF manifest and hOCR (browser)', 'Complément du Dictionnaire de l\'Académie 1842 (bsb10627876), canvases 5-9, 334-336', '1842', 'n/a', 'n/a', 'sa-1842-complement-academie upgraded to full_text'],
]


def main():
    # 1. rename the family code in the strand tables
    renamed = 0
    for path in STRAND_TABLES:
        if not os.path.exists(os.path.join(ROOT, path)):
            continue
        cols, rows = load(path)
        for r in rows:
            v = r.get('scheme_family', '')
            if v in RENAME:
                r['scheme_family'] = RENAME[v]
                renamed += 1
        save(path, cols, rows)

    # 2. in-place updates
    updated = 0
    for path, edits in UPDATES.items():
        cols, rows = load(path)
        for r in rows:
            if r['entry_id'] in edits:
                for k, v in edits[r['entry_id']].items():
                    assert k in cols, (path, k)
                    r[k] = v
                r['checked_on'] = D
                updated += 1
        save(path, cols, rows)

    # 3. new rows
    cols_b, rows_b = load('data/strand_b/entries.csv')
    cols_bde, rows_bde = load('data/strand_b/entries_de.csv')
    fr, de = new_rows(cols_b, cols_bde)
    have = {r['entry_id'] for r in rows_b}
    rows_b += [r for r in fr if r['entry_id'] not in have]
    save('data/strand_b/entries.csv', cols_b, rows_b)
    have = {r['entry_id'] for r in rows_bde}
    rows_bde += [r for r in de if r['entry_id'] not in have]
    save('data/strand_b/entries_de.csv', cols_bde, rows_bde)

    cols_nr, nr = load('data/strand_b/not_reached.csv')
    have = {r['work'] for r in nr}
    for w in NOT_REACHED_B:
        if w[0] not in have:
            nr.append(dict(zip(cols_nr, w)))
    save('data/strand_b/not_reached.csv', cols_nr, nr)

    cols_l, log = load('data/search_log.csv')
    have = {(r['date'], r['query']) for r in log}
    for row in LOG:
        rec = dict(zip(cols_l, row + [WHO]))
        if (rec['date'], rec['query']) not in have:
            log.append(rec)
    save('data/search_log.csv', cols_l, log)
    print(f'renamed {renamed}, updated {updated}, strand_b rows {len(rows_b)}, strand_b_de rows {len(rows_bde)}, search_log rows {len(log)}')


if __name__ == '__main__':
    main()
