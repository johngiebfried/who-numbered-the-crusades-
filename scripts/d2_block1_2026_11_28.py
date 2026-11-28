"""Strand D2, block 1 (28 November 2026): reference works, popular histories and scholarly works read
in the archive.org text layer through the built-in browser.

Writes works.csv rows (new and corrected), the D2 attributes, citation edges, reasons, search-log rows
and frame status. Idempotent: rerunning changes nothing. Corrections to legacy rows are listed in
docs/DECISIONS.md under 28 November 2026 (D2). MIT License.
"""
import csv
from pathlib import Path

import d2_lib as L

D = "2026-11-28"
TXT = "archive.org djvu text via built-in browser"
IA = "https://archive.org/details/"


def cur():
    return {w["work_id"]: w for w in L._read(L.WORKS)[1]}


def app(wid, field, text, works):
    """Append text to a field once (idempotent)."""
    old = works[wid][field] if wid in works else ""
    if text in old:
        return old
    return (old + " | " if old else "") + text


def new(wid, **kw):
    base = dict(work_id=wid, language="English", research_pass="strand_d2", checked_on=D,
                how_verified=TXT, access=TXT)
    base.update(kw)
    return base


def merge_rows(dup, into):
    """Fold duplicate row `dup` into `into`: alt_ids, source_tables, id_map. Idempotent."""
    cols, works = L._read(L.WORKS)
    by = {w["work_id"]: w for w in works}
    if dup in by:
        d, t = by[dup], by[into]
        t["alt_ids"] = ";".join(dict.fromkeys([x for x in t["alt_ids"].split(";") if x] + [dup]))
        t["source_tables"] = ";".join(dict.fromkeys(
            [x for x in (t["source_tables"] + ";" + d["source_tables"]).split(";") if x]))
        works = [w for w in works if w["work_id"] != dup]
        with open(L.WORKS, "w", newline="", encoding="utf-8") as f:
            wr = csv.DictWriter(f, fieldnames=cols)
            wr.writeheader()
            wr.writerows(works)
    idmap = L.ROOT / "reconciliation" / "id_map.csv"
    with open(idmap, newline="", encoding="utf-8") as f:
        text = f.read()
    nl = "\r\n" if "\r\n" in text else "\n"
    rows = list(csv.reader(text.splitlines()))
    changed = False
    for r in rows[1:]:
        if len(r) == 3 and r[2] == dup:
            r[2] = into
            changed = True
    if changed:
        with open(idmap, "w", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator=nl).writerows(rows)


W = cur()

# ---------------------------------------------------------------- reference works
works = [
    dict(work_id="1877-eb9-crusades", E="9", research_pass="review;strand_d2", checked_on=D,
         notes=app("1877-eb9-crusades", "notes",
                   "[D2 2026-11-28] Read in the US reprint encyclopaediabri0006unse_b8h3 (vol. 6) and in the 1902 "
                   "Werner reprint 'Original Ninth Edition ... New American Supplement' (encyclopaediabri06kell): same "
                   "text. Fourth: 'an enterprise set on foot by the knights of St John, 1198 [1193], seconded by Pope "
                   "Celestine III in the hopes of getting rid of the Emperor Henry VI'. Edward reaches Acre, makes a ten "
                   "years' peace, 'and the ninth and last crusade was at an end': E 9 with Tunis. Bibliography: Gibbon, "
                   "Michaud, Mills.", W)),
    dict(work_id="1911-ernest-barker", research_pass="review;strand_d2", checked_on=D,
         notes=app("1911-ernest-barker", "notes",
                   "[D2 2026-11-28] E cleared: the footnote names 'that of Edward I. in 1271-1272' among 'famous "
                   "Crusades, which are not reckoned in the usual numbering', and the text says Edward 'only arrived on "
                   "the eve of the conclusion of the treaty' and 'conducted a Crusade of his own to Acre in the spring of "
                   "1271'. Read in encyclopaediabrit07chisrich (vol. 7). Same article and footnote in the 1922 and 1926 "
                   "printings (encyclopaediabri0007unse; encyclopediabrit0000unse_a5j5). Gibbon not cited in the article.",
                   W)),
    new("sd2-1929-eb14-crusades", label="Encyclopaedia Britannica, 14th ed., Crusades",
        author="[Ernest Barker, revised; signature not located]",
        work="Encyclopaedia Britannica, 14th ed., CRUSADES", edition="14th", year_label="1929", year_sort="1929",
        place_publisher="London and New York: Encyclopaedia Britannica Co.", volume="vol. 6", headword="CRUSADES",
        tradition="Britain", genre="Reference", census_frame="d2_reference_en", enumerates="yes",
        C="4", D="5", F="6", L1="7", L2="8", scheme_family="modern_eight", signature_match="modern",
        stemma_parent="1911-ernest-barker",
        parent_evidence="documented: the EB11 article revised; its numbering footnote moved into the text",
        quote="THE FOURTH CRUSADE (1202-1204) ... THE FIFTH CRUSADE (1218-1221)",
        url=IA + "encyclopediabrit0006unse_q8m5", verification_level="full_text",
        title_page_checked="no (archive.org metadata: 1929, vol. 6)", country="GB", channel="EB11 (Barker)",
        notes="Lower-case section heads; Barker's footnote now in the text under 'The Second Crusade' ('We speak of "
              "first, second and third crusades ... not reckoned in the usual numbering'). 'The negotiations between "
              "Richard and Saladin contain the germs of the sixth' (F 6). Henry VI's crusade of 1195 is told as "
              "anticipating 'the fourth crusade of 1202-04', unnumbered. The 1938 and 1944 printings "
              "(encyclopaediabri0006vari; encyclopediabrit0006vari_b3q2) are lending copies without a text layer: "
              "not reached."),
    new("sd2-1831-americana-chron-table",
        label="Encyclopaedia Americana, HISTORY: A General Chronological Table",
        author="Francis Lieber (ed.)", work="Encyclopaedia Americana", edition="1st ed.",
        year_label="1831? (vol. 6; set 1829-33)", year_sort="1831",
        place_publisher="Philadelphia: Carey, Lea & Carey", volume="vol. 6", pages="347 ff.",
        headword="HISTORY (A General Chronological Table)", tradition="US", genre="Reference",
        census_frame="d2_reference_en", enumerates="yes", stated_phrase="Ninth crusade (Thibaut)",
        C="5", D="7", F="8", B="9", scheme_family="other", signature_match="no",
        differing_slots="fourth, fifth, sixth, seventh, eighth",
        quote="Crusade against the Albigenses (the sixth) ... Seventh crusade (Andrew II of Hungary ... Eighth "
              "Crusade (Frederic II) ... Ninth crusade (Thibaut) ... Last crusade (Louis IX)",
        url=IA + "encyclopaediaam00bradgoog", verification_level="full_text",
        title_page_checked="partly (OCR imprint Philadelphia; volume date not legible)", country="US",
        channel="Conversations-Lexikon (probable)",
        notes="The chronological table, not the CRUSADES article (sa-1830-americana, German six). Entries: 'First "
              "Crusade' (Jerusalem taken); 'Second crusade' placed after Henry I's accession, so the crusade of "
              "1101; 'Third crusade' with Conrad III (1147); 'Fourth crusade (Richard I, Coeur de Lion, Philip "
              "Augustus of France, emperor Frederic)'; 'Fifth crusade' with Innocent III and the capture of "
              "Constantinople; 'Crusade against the Albigenses (the sixth)'; Andrew II the seventh; Frederick II the "
              "eighth; Thibaut the ninth; Louis IX 'Last crusade'. Every number from the second on is one higher "
              "than usual, and the Albigensian crusade is counted. Source probably a chronological table of the "
              "Conversations-Lexikon (not checked). Also in encyclopdiaamer08bradgoog and 00110080RX6.nlm.nih.gov."),
    dict(work_id="sa-1830-americana",
         notes=app("sa-1830-americana", "notes",
                   "[D2 2026-11-28] The same encyclopedia's chronological table (vol. 6, HISTORY) numbers differently: "
                   "sd2-1831-americana-chron-table.", W)),
]

# ---------------------------------------------------------------- popular histories
works += [
    dict(work_id="1820-charles-mills", place_publisher="London: Longman et al.",
         edition="1st ed. 1820; also read 1821, 1828 (4th ed.), Philadelphia 1844",
         quote="CHAP. III. THE FOURTH AND FIFTH CRUSADES. Death and character of Saladin ... Pope Celestine III. "
               "promotes a Crusade",
         url=IA + "in.ernet.dli.2015.110073", verification_level="full_text",
         title_page_checked="partly (OCR title and author; date from metadata)", country="GB",
         research_pass=W["1820-charles-mills"]["research_pass"] + ";strand_d2", checked_on=D,
         how_verified=TXT, access=TXT,
         notes=app("1820-charles-mills", "notes",
                   "[D2 2026-11-28] Chapter heads read in the 1820 (vol. 2), 1821, 1828 and Philadelphia 1844 texts "
                   "(in.ernet.dli.2015.110073; historyofcrusade02milluoft; historyofcrusade02mill; "
                   "historycrusades03millgoog): 'THE FOURTH AND FIFTH CRUSADES' (Celestine III's crusade, then "
                   "Innocent III's); 'THE SIXTH CRUSADE' (Courçon, Lateran IV, Hungary; Frederick II in the same "
                   "chapter); 'THE SEVENTH AND EIGHTH CRUSADES' (the eighth born of the Khwarazmian sack; Council of "
                   "Lyons); 'THE LAST CRUSADE, AND THE LOSS OF THE HOLY LAND' (Tunis and Prince Edward). Note N: 'For "
                   "the fourth crusade, that of the German lords'. Preface: Gibbon's sketches 'principally taken from "
                   "Vertot ... and from Mailly'; 'The fourth, sixth, and seventh Crusades are altogether unnoticed by "
                   "Mr. Gibbon'; Sharon Turner 'the only author who appears to have justly appreciated the subject'.",
                   W)),
    new("sd2-1830-stebbing-chivalry", label="Henry Stebbing, The History of Chivalry and the Crusades",
        author="Henry Stebbing", work="The History of Chivalry and the Crusades (Constable's Miscellany)",
        year_label="1830", year_sort="1830", place_publisher="Edinburgh: Constable", volume="2 vols.",
        tradition="Britain", genre="Popular history", census_frame="d2_popular_en", enumerates="no",
        scheme_family="none", url=IA + "historyofchivalr01stebuoft", verification_level="full_text",
        title_page_checked="yes (OCR: EDINBURGH ... CONSTABLE; date from metadata)", country="GB",
        notes="No ordinal crusade numbers in the text layer of vol. 1 (historyofchivalr01stebuoft) or vol. 2 "
              "(historychivalry02stebgoog). Footnotes '* Gibbon.' on the First Crusade."),
    new("sd2-1830-james-chivalry", label="G. P. R. James, The History of Chivalry",
        author="G. P. R. James", work="The History of Chivalry", edition="2nd ed.", year_label="1830",
        year_sort="1830", place_publisher="London: Henry Colburn and Richard Bentley", tradition="Britain",
        genre="Popular history", census_frame="d2_popular_en", enumerates="partial", C="5",
        quote="THE fifth crusade had ended, as we have seen, without producing any other benefit to Palestine, than "
              "a deep depression in the minds of the Turks, from the knowledge that the weak dynasty of the Greeks "
              "had been replaced by a power of greater energy",
        url=IA + "historyofchivalr00jameuoft", verification_level="full_text",
        title_page_checked="yes (OCR: SECOND EDITION ... HENRY COLBURN AND RICHARD BENTLEY ... 1830)", country="GB",
        channel="Mills",
        notes="Chapter XIII heads: 'Celestine III. preaches a new crusade - Henry of Germany takes the cross - "
              "Abandons his purpose - Crusaders proceed without him' (unnumbered). Last chapter: 'Second crusade of St. "
              "Louis - Takes Carthage - His death - Crusade of Prince Edward'. Mills named 38 times and Vertot 21 "
              "times in the text layer; Gibbon not named within 3,000 characters of 'crusade'."),
    new("sd2-1834-keightley-crusaders",
        label="Thomas Keightley, The Crusaders; or, Scenes, Events, and Characters",
        author="Thomas Keightley",
        work="The Crusaders; or, Scenes, Events, and Characters, from the Times of the Crusades",
        year_label="1834", year_sort="1834", place_publisher="London: J. W. Parker", tradition="Britain",
        genre="Popular history", census_frame="d2_popular_en", enumerates="no", scheme_family="none",
        url=IA + "crusadersorscen01keiggoog", verification_level="full_text",
        title_page_checked="no (metadata: J. W. Parker, 1834)", country="GB",
        notes="Read 1834 vol. 1 and the 1859 edition (crusadersorscene00keig, Committee of General Literature and "
              "Education). Ordinals only 'second and third crusade'. Footnote: 'Gibbon and others very improperly "
              "style Conrad emperor'. Names Wilken, Michaud, Mills."),
    dict(work_id="1852-michaud-trans-william-robson", C="5", D="6", L1="7", L2="8", E="8",
         scheme_family="moreri_eight", signature_match="no", country="GB",
         url=IA + "historycrusades02michgoog", checked_on=D,
         research_pass=W["1852-michaud-trans-william-robson"]["research_pass"] + ";strand_d2",
         quote="The Fourth Crusade, a.d. 1195-1198 ... The Fifth Crusade, a.d. 1198-1204 ... The Seventh Crusade, "
               "a.d. 1242-1245 ... The Eighth Crusade, a.d. 1255-1270",
         notes=app("1852-michaud-trans-william-robson", "notes",
                   "[D2 2026-11-28] Index and vol. 3 contents read in the 1852 text (historycrusades02michgoog) and "
                   "the New York reissues of 1891 and 1900 (HistoryOfTheCrusadesV3; historyofcrusad03mich, A. C. "
                   "Armstrong, 'A New Edition (From New Plates)'). Andrew II 'engages in the sixth crusade'; 'Louis IX. "
                   "and several distinguished personages engage in the seventh crusade'; vol. 3: 'Edward prince of "
                   "England, engage in the crusade ... Prince Edward of England arrives in Palestine' inside Book XV, "
                   "'EIGHTH CRUSADE'. Frederick II's place not checked. Michaud's own note: 'For the siege of "
                   "Constantinople, the very detailed account of Gibbon'.", W)),
    new("sd2-1900-michaud-robson-ny", label="Michaud, The History of the Crusades, tr. Robson (New York)",
        author="J.-F. Michaud; trans. William Robson",
        work="The History of the Crusades (new edition, with preface by Hamilton W. Mabie)", year_label="1900",
        year_sort="1900", place_publisher="New York: A. C. Armstrong & Son", volume="vol. 3",
        tradition="US", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        H6="4", C="5", D="6", L1="7", L2="8", E="8", scheme_family="moreri_eight", signature_match="no",
        stemma_parent="1852-michaud-trans-william-robson", parent_evidence="documented: reissue of the translation",
        quote="The Fourth Crusade, a.d. 1195-1198",
        url=IA + "historyofcrusad03mich", verification_level="contents",
        title_page_checked="yes (OCR: TRANSLATED BY W. ROBSON. A NEW EDITION; metadata 1900)", country="US",
        channel="Michaud",
        notes="US printing of the Robson translation, same index entries as 1852. Row kept as the edition read for "
              "the US (edition policy)."),
    dict(work_id="1842-george-proctor", scheme_family="barons_sixth", signature_match="no", E="8", checked_on=D,
         research_pass=W["1842-george-proctor"]["research_pass"] + ";strand_d2",
         notes=app("1842-george-proctor", "notes",
                   "[D2 2026-11-28] Read in the Philadelphia printing (Lindsay & Blakiston, 1856; "
                   "historycrusades00procgoog, archive.org metadata 'London: R. Griffin 1854') and the New York reprint "
                   "retitled 'Fighting their way; or, The history of the Crusades' (World Publishing House, 1876). "
                   "Sections: 'THE FOURTH CRUSADE' (1202-04), 'THE FIFTH CRUSADE' (Damietta, Frederick II), 'THE SIXTH "
                   "CRUSADE' (1238, the barons at Northampton, Richard of Cornwall), 'THE SEVENTH CRUSADE' (St Louis in "
                   "Egypt), 'THE EIGHTH CRUSADE' ('the Eighth and last Crusade', Tunis, with Edward I inside it). "
                   "Footnote on 1195-97: 'some writers have dignified the abortive result with the title of the Fourth "
                   "Crusade; and numbered the subsequent expedition ... as the Fifth of Nine. But the more usual, which "
                   "seems also the more convenient division, restricts the term of distinct Crusades to Seven, or at "
                   "most Eight, great efforts, which were either produced by some signal occasion, such as the loss of "
                   "Edessa or Jerusalem, or else productive of some considerable event.'", W)),
    new("sd2-1856-procter-philadelphia", label="Procter, History of the Crusades (Philadelphia)",
        author="George Procter", work="History of the Crusades: Their Rise, Progress, and Results",
        year_label="1856", year_sort="1856", place_publisher="Philadelphia: Lindsay & Blakiston",
        tradition="US", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        C="4", D="5", F="5", B="6", L1="7", L2="8", E="8", stated_phrase="the Eighth and last Crusade",
        scheme_family="barons_sixth", signature_match="no", stemma_parent="1842-george-proctor",
        parent_evidence="documented: reprint", quote="Let us now return to the progress of the Eighth and last Crusade",
        url=IA + "historycrusades00procgoog", verification_level="full_text",
        title_page_checked="yes (OCR: PHILADELPHIA: LINDSAY & BLAKISTON. 1856)", country="US", channel="Procter",
        notes="The edition read for the US. Retitled New York reprint 1876 ('Fighting their way'). Text as "
              "1842-george-proctor."),
    new("sd2-1853-bloss-heroines", label="C. A. Bloss, Heroines of the Crusades",
        author="Celestia Angenette Bloss", work="Heroines of the Crusades", year_label="1853", year_sort="1853",
        place_publisher="Auburn and Buffalo: John E. Beardsley (Alden, Beardsley; Rochester: Wanzer, Beardsley)",
        tradition="US", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        H6="4", C="5", D="6", F="6", L1="7", L2="8", E="8", scheme_family="moreri_eight", signature_match="no",
        quote="Fourth Crusade, A.D. 1198 ... Fifth Crusade, a.d. 1203 ... Sixth Crusade, A.D. 1215 ... Seventh "
              "Crusade, a.d. 1249 ... Eighth Crusade, a.d. 1272",
        url=IA + "heroinesofcrusad00blos", verification_level="full_text",
        title_page_checked="yes (OCR: HEROINES OF THE CRUSADES. BY C. A. BLOSS ... AUBURN AND BUFFALO)", country="US",
        notes="One heroine per numbered crusade. The fourth is the one 'which the French monarch regarded with "
              "indifference'; Dandolo 'is already embarked to repeat the Fifth Crusade'; the sixth is preached before "
              "the Lateran council and its heroine is 'Violante, Queen of Jerusalem, Empress of Germany' (so D+F); the "
              "eighth is dated 1272 and told through Eleanor of Castile, Edward's wife, with Louis's death at Tunis "
              "inside it. Names Mills, Michelet, Hume, Lingard; Gibbon not named near 'crusade'."),
    new("sd2-1849-sargent-sketches", label="G. E. Sargent, Sketches of the Crusades",
        author="George Etell Sargent", work="Sketches of the Crusades", year_label="[c. 1849]", year_sort="1849",
        place_publisher="London: Partridge and Oakey", tradition="Britain", genre="Popular history",
        census_frame="d2_popular_en", enumerates="partial", H6="4", D="6",
        quote="This massacre closed the fourth Crusade. The same year (1197) ended the life of Henry of Champagne",
        url=IA + "sketchescrusade00sarggoog", verification_level="full_text",
        title_page_checked="partly (OCR imprint Partridge and Oakey, no date; archive.org dates copies 1849 and 1860)",
        country="GB", channel="Mills",
        notes="'The fourth was almost entirely a German Crusade. Its patron was Henry VI.'; 'A sixth Crusade was "
              "proclaimed by Pope Innocent, and preached by Robert de Courçon'; 'the Inquisition, established "
              "between the fourth and fifth Crusades, by Innocent III'; Edward 'In 1272 ... withdrew his army from "
              "Palestine, and returned to England. Thus terminated the last Crusade.' Quotes Gibbon ('Gibbon "
              "declares that ...'); names Mills. The other copy (sketchescrusade01sarggoog, 1849) has no text layer."),
    dict(work_id="1865-walter-c-perry", author="George Gresley Perry",
         label="G. G. Perry, A History of the Crusades", work="A History of the Crusades", F="6",
         place_publisher="London: Longmans (1865); read in the New York printing, Carlton & Lanahan, n.d.",
         scheme_family="nine_H6", signature_match="no", country="GB", channel="Michaud (preface); Mills",
         quote="Causes which led to the Fourth Crusade ... Pope Innocent brings about the Fifth Crusade ... Returns "
               "to France - The Ninth Crusade - Death of Louis",
         url=IA + "historyofcrusade00perr", how_verified=TXT, access=TXT,
         title_page_checked="no (metadata: Perry, G. G. (George Gresley), 1820-1897; New York: Carlton & Lanahan; "
                            "'1840')",
         research_pass="review;strand_d2", checked_on=D,
         notes="[D2 2026-11-28] Author corrected. The paper's table and the legacy label had 'Perry, The Franks' "
               "(Walter C. Perry), but this numbering is G. G. Perry's A History of the Crusades (1865): 'Causes which "
               "led to the Fourth Crusade - Successes of the Germans in Palestine'; 'Pope Innocent brings about the "
               "Fifth Crusade - The French Barons seek aid from Venice'; 'The Sixth Crusade commanded by the King of "
               "Hungary', with 'Frederick II. goes to Palestine' in the same chapter; 'Seventh Crusade opposed "
               "violently by the Pope - Events of the First Expedition under the King of Navarre - The Expedition of "
               "Richard, Earl of Cornwall'; 'His Expedition to Egypt - The Eighth Crusade'; 'The Ninth Crusade - Death "
               "of Louis'; then 'Expedition of Prince Edward of England' in a chapter of its own. Preface: 'chiefly "
               "based' on Michaud (and Wilken); 'For the Fifth Crusade no other writer can take the place of Gibbon'. "
               "archive.org's date 1840 is impossible: the preface cites Milman's Latin Christianity (1854-55). Row "
               "sd-1840-perry-history-crusades (same copy) merged here."),
    dict(work_id="1874-george-w-cox", checked_on=D,
         notes=app("1874-george-w-cox", "notes",
                   "[D2 2026-11-28] Read in the 1874 and 1890 Epochs of History texts (crusades02coxg; crusades01coxg): "
                   "'THE FOURTH CRUSADE' (1193, death of Saladin), 'THE FIFTH CRUSADE' (1198 Innocent III; 1201 "
                   "mission to Venice), 'THE SIXTH CRUSADE', 'THE SEVENTH CRUSADE' (Richard of Cornwall), 'THE EIGHTH "
                   "CRUSADE' (1245 Council of Lyons; Louis IX), 'THE NINTH CRUSADE' (with '1271 Capture of Nazareth by "
                   "Edward' and '1272 Return of Edward to Europe'). Gibbon not named within 3,000 characters of "
                   "'crusade'.", W)),
    new("sd2-1860-edgar-crusaders", label="John G. Edgar, The Crusades and the Crusaders (Boston)",
        author="John G. Edgar", work="The Crusades and the Crusaders", year_label="1860", year_sort="1860",
        place_publisher="Boston: Ticknor and Fields", tradition="US", genre="Popular history",
        census_frame="d2_popular_en", enumerates="no", scheme_family="none",
        url=IA + "crusadesandcrus00edgagoog", verification_level="full_text",
        title_page_checked="yes (OCR: BOSTON: TICKNOR AND FIELDS MDCCCLX)", country="US",
        notes="Juvenile narrative by a British author (first published London 1860); this is the Boston printing. No "
              "ordinal numbers; 'Otho de Grandison, who had accompanied the great Edward in the last crusade'."),
    new("sd2-1871-besant-palmer-jerusalem", label="Besant and Palmer, Jerusalem, the City of Herod and Saladin",
        author="Walter Besant; E. H. Palmer", work="Jerusalem, the City of Herod and Saladin",
        year_label="1871", year_sort="1871", place_publisher="London: Bentley", tradition="Britain",
        genre="Popular history", census_frame="d2_popular_en", enumerates="no", scheme_family="none",
        url=IA + "jerusalemcityofh00besarich", verification_level="full_text",
        title_page_checked="no (edition of the copy not checked)", country="GB",
        notes="No ordinal numbers. 'Louis led another Crusade and met his death at Tunis. Edward of England ... came "
              "to Acre'."),
    dict(work_id="1894-t-a-archer-c-l-kingsford", verification_level="full_text", checked_on=D,
         url=IA + "crusadesstoryla00kinggoog",
         notes=app("1894-t-a-archer-c-l-kingsford", "notes",
                   "[D2 2026-11-28] Contents read in the text layer: 'The German Crusade, 369 - The Fourth Crusade, 371 "
                   "- John de Brienne, 373 - The Fifth Crusade, 375 - The Siege of Damietta, 377 - Frederick II., 379'; "
                   "chapter XXV 'The Crusades of St. Louis and Edward I.'; Louis's Egyptian expedition is 'the last "
                   "Crusade but one'. Gibbon not named within 3,000 characters of 'crusade'.", W)),
    dict(work_id="1894-j-i-mombert", verification_level="full_text", E="8", checked_on=D,
         url=IA + "ashorthistorycr00mombgoog",
         notes=app("1894-j-i-mombert", "notes",
                   "[D2 2026-11-28] Contents: 'VIII. Henry VI.'s Expedition. A.D. 1194-1197'; 'IX. Fourth Crusade. A.D. "
                   "1202-1204'; 'XI. The Albigeois Crusade'; 'XII. Fifth Crusade. A.D. 1217-1221'; 'XIII. Sixth Crusade. "
                   "A.D. 1228-1229'; 'XIV. Seventh Crusade. A.D. 1248-1254'; 'XV. Eighth Crusade. A.D. 1270', in which "
                   "'Louis IX ... acting in concert with Prince Edward of England ... undertook a new Crusade'. Preface "
                   "names 'Gibbon, Heeren, Milman, Guizot, and Ranke as my chosen counselors'.", W)),
    dict(work_id="1896-j-m-ludlow", checked_on=D, url=IA + "agecrusades00ludlgoog",
         notes=app("1896-j-m-ludlow", "notes",
                   "[D2 2026-11-28] Chapter heads read: 'THE FOURTH CRUSADE' (Constantinople), 'BETWEEN THE FOURTH AND "
                   "FIFTH CRUSADES - THE CHILDREN'S CRUSADE', 'THE FIFTH CRUSADE' (Damietta), 'THE SIXTH CRUSADE' "
                   "(Frederick II and Gregory IX), 'THE SEVENTH CRUSADE' (St Louis), 'THE EIGHTH CRUSADE' (death of St "
                   "Louis, fall of Acre). Henry VI appears among 'Various Minor Crusades'. Bibliography lists Gibbon "
                   "(London 1776-81); quotes Gibbon and Pears ('The crime of the fourth crusade handed over "
                   "Constantinople and the Balkan peninsula to six centuries of barbarism').", W)),
    new("sd2-1913-blyth-jerusalem", label="Estelle Blyth, Jerusalem and the Crusades",
        author="Estelle Blyth", work="Jerusalem and the Crusades", year_label="1913", year_sort="1913",
        place_publisher="London and Edinburgh: T. C. & E. C. Jack", tradition="Britain",
        genre="Popular history (juvenile)", census_frame="d2_popular_en", enumerates="partial", L1="9",
        stated_phrase="the Ninth Crusade - that of Louis IX, King of France, and Saint (1248)",
        quote="Out of all this darkness and unrest arose at last the Ninth Crusade - that of Louis IX, King of "
              "France, and Saint (1248)",
        url=IA + "jerusalemcrusade00blyt", verification_level="full_text",
        title_page_checked="yes (OCR: LONDON: T. C. & E. C. JACK ... AND EDINBURGH; date from metadata)",
        country="GB",
        notes="Contents number only the first three crusades, then 'THE CHILDREN'S CRUSADE, 1212' and 'THE LAST "
              "CRUSADES'; index 'Ninth Crusade, the, 211'. A ninth for Louis IX's first crusade (1248) implies a count "
              "with two extra expeditions before 1248; the text does not say which. Edward's army is told inside "
              "Louis's second crusade, unnumbered."),
    new("sd2-1930-lamb-flame-islam", label="Harold Lamb, The Crusades: The Flame of Islam",
        author="Harold Lamb", work="The Crusades: The Flame of Islam", year_label="1930", year_sort="1930",
        place_publisher="Garden City: Doubleday, Doran", tradition="US", genre="Popular history",
        census_frame="d2_popular_en", enumerates="no", scheme_family="none",
        url=IA + "cruasadestheflam006191mbp", verification_level="full_text",
        title_page_checked="no (date from metadata)", country="US",
        notes="No ordinal numbers. Names Röhricht, Riant, Barker, Stevenson, Stubbs; Gibbon not named near "
              "'crusade'. The companion volume Iron Men and Saints (crusadesironmens00lamb) is a lending copy: not "
              "reached."),
    new("sd2-1904-historians-history-v8", label="The Historians' History of the World, vol. 8",
        author="Henry Smith Williams (ed.)", work="The Historians' History of the World", year_label="1904",
        year_sort="1904", place_publisher="New York: The Outlook Company; London: The History Association",
        volume="vol. 8", tradition="US", genre="Popular history (anthology)", census_frame="d2_popular_en",
        enumerates="yes", H6="4", C="5", D="6", F="6", B="7", L1="8", L2="9", E="9",
        scheme_family="nine_H6", signature_match="no", stemma_parent="1820-charles-mills; 1877-eb9-crusades",
        parent_evidence="documented: narrative extracts reprint Mills ('the successes of the savage Khwarizmians, gave "
                        "birth to the Eighth Crusade. Pope Innocent IV convoked'); the outline of the Fourth follows "
                        "EB9 (Knights of St John 1193, Celestine III's hopes of Henry VI)",
        quote="THE FOURTH CRUSADE (1195-1198 A.D.) The Knights of St. John start in 1193 to organise a crusade. They "
              "are encouraged by Pope Celestine III, who hopes that the troublesome emperor Henry VI will be induced "
              "to take part in it",
        url=IA + "historianshistor08willuoft", verification_level="full_text",
        title_page_checked="partly (OCR title; imprint and date from metadata)", country="US",
        channel="Mills; EB9",
        notes="Chapter V 'THE FOURTH TO THE SIXTH CRUSADES (1195-1229 A.D.)': 'The Fourth (or German) Crusade', 'The "
              "Fifth Crusade' (1201-1204), 'The Children's Crusade', 'The Sixth Crusade' (Frederick II 'at the head of "
              "the Sixth Crusade'; Damietta inside it by position). Chapter VI 'THE LAST CRUSADES (1239-1314 A.D.)': "
              "'Richard of Cornwall's Crusade (the Seventh)', 'THE EIGHTH CRUSADE (1248-1264 A.D.)', 'THE NINTH "
              "CRUSADE (1270-1272 A.D.)' with Prince Edward. Quotes Gibbon on Muhammad and on the results of the "
              "crusades. Printed in New York and London."),
]

# ---------------------------------------------------------------- scholarly works
works += [
    dict(work_id="1885-edwin-pears", verification_level="full_text", url=IA + "fallconstantino00peargoog",
         checked_on=D,
         notes=app("1885-edwin-pears", "notes",
                   "[D2 2026-11-28] Text layer read: half-title 'THE STORY OF THE FOURTH CRUSADE'; Henry VI's "
                   "expedition of 1196-97 told unnumbered ('Henry the Sixth's crusaders'). Main authority Riant (14 "
                   "mentions); Gibbon named in the text ('taken from Gibbon to Finlay').", W)),
    dict(work_id="1788-edward-gibbon",
         notes=app("1788-edward-gibbon", "notes",
                   "[D2 2026-11-28] Numbering unchanged in the annotated editions read: Bohn's variorum edition (Bell "
                   "& Sons reissue, vol. 6; historyofdecline06gibb), whose marginal summary has '1203. The Fourth "
                   "Crusade', '1218. The Fifth Crusade', '1248-1254. St. Louis and the Sixth Crusade', '1270. His Death "
                   "before Tunis, in the Seventh Crusade'; the Bury edition (Methuen 1906 reissue, vol. 6; "
                   "historyofdecline0006unse), whose notes cite Stubbs, Röhricht, Riant, Sybel, Kugler, Pears and "
                   "Lane-Poole without renumbering. The Bohn notes cite Wilken 29 times.", W)),
    new("sd2-1868-students-gibbon", label="William Smith (ed.), The Student's Gibbon",
        author="William Smith (ed.)", work="The Student's Gibbon: The History of the Decline and Fall of the "
                                            "Roman Empire, abridged",
        year_label="1868 (printing read)", year_sort="1868", place_publisher="London: John Murray",
        tradition="Britain", genre="School", census_frame="d2_school_en", enumerates="yes",
        C="4", D="5", L1="6", L2="7", E="7", stated_phrase="the seventh and last of the crusades",
        scheme_family="gibbon_seven", signature_match="no", stemma_parent="1788-edward-gibbon",
        parent_evidence="documented: abridgment",
        quote="IV. V. Fourth and Fifth Crusades, a.d. 1203 and 1218 ... VI. Sixth Crusade, a.d. 1249-1254 ... VII. "
              "Seventh Crusade, a.d. 1269-1272",
        url=IA + "studentsgibbonh00smitgoog", verification_level="full_text",
        title_page_checked="no (date from metadata; earliest copy found 1862, studentsgibbonh01smitgoog)",
        country="GB", channel="Gibbon",
        notes="Murray's Student's Manuals. Smith turns Gibbon's narrative into a numbered list (I-VII) of section "
              "heads. 'to undertake the seventh and last of the crusades. The cross was also assumed by Prince "
              "Edward': Edward inside the seventh."),
    new("sd2-1818-hallam-middle-ages", label="Henry Hallam, View of the State of Europe during the Middle Ages",
        author="Henry Hallam", work="View of the State of Europe during the Middle Ages",
        year_label="1818 (read New York 1857, 'from the sixth London edition')", year_sort="1818",
        place_publisher="London: John Murray; read New York: Derby & Jackson", tradition="Britain",
        genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial", C="4",
        quote="recorded the capture of Constantinople in the fourth crusade",
        url=IA + "cu31924027794639", verification_level="full_text",
        title_page_checked="yes (OCR: FROM THE SIXTH LONDON EDITION ... NEW YORK: DERBY & JACKSON ... 1857)",
        country="GB", channel="Gibbon",
        notes="'The two last crusades were undertaken by St. Louis' (unnumbered). Note on authorities: 'Gibbon's two "
              "chapters on the crusades, though not without inaccuracies, are a brilliant portion' of his work."),
    new("sd2-1830-turner-middle-ages", label="Sharon Turner, The History of England during the Middle Ages",
        author="Sharon Turner", work="The History of England during the Middle Ages",
        year_label="1830 printing (first published 1814-23)", year_sort="1830", place_publisher="London: Longman",
        tradition="Britain", genre="Church and national history", census_frame="d2_church_en",
        enumerates="partial", L2="7",
        quote="He died before Tunis, in what is called the seventh Crusade, in 1270",
        url=IA + "historyenglandd00turngoog", verification_level="full_text",
        title_page_checked="no (date from metadata)", country="GB", channel="Gibbon (probable)",
        notes="'in what is called the seventh Crusade': the number reported as usage, Gibbon's L2 7. Edward: 'St. "
              "Louis, desirous to begin his second crusade, invited Edward to join him. The prince ... sailed to the "
              "coast of Africa' (unnumbered). Cites Gibbon 15 times, mostly on Muhammad."),
    new("sd2-1854-milman-latin-christianity", label="H. H. Milman, History of Latin Christianity",
        author="H. H. Milman", work="History of Latin Christianity", year_label="1854-55 (read vols. 4-5, "
                                                                             "1860-61 printing)",
        year_sort="1854", place_publisher="London: John Murray (read US printing)", tradition="Britain",
        genre="Church and national history", census_frame="d2_church_en", enumerates="no", scheme_family="none",
        url=IA + "historyoflatin04milm", verification_level="full_text",
        title_page_checked="no", country="GB",
        notes="No ordinal crusade numbers in the text layer of vols. 4 and 5 (historyoflatin04milm; "
              "unset0005unse_c0j0); 'the last crusade' only as a figure (the Armada). Names Michaud, Wilken, Raumer, "
              "Heeren, Guizot, Gieseler. Milman also edited Gibbon (1838-39)."),
    new("sd2-1886-stubbs-lectures", label="William Stubbs, Seventeen Lectures",
        author="William Stubbs",
        work="Seventeen Lectures on the Study of Medieval and Modern History (lectures on Cyprus and the "
             "Latin kingdom)",
        year_label="1886 (read 1887)", year_sort="1886", place_publisher="Oxford: Clarendon Press",
        tradition="Britain", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial",
        C="4", D="5",
        quote="a Flemish knight, who came to the East in the fourth crusade in the retinue of John de Neesle",
        url=IA + "seventeenlecture00stubuoft", verification_level="full_text",
        title_page_checked="yes (OCR: HENRY FROWDE, OXFORD UNIVERSITY PRESS)", country="GB",
        notes="Running head 'THE FIFTH CRUSADE' over the years after 1205 (D 5). 'Hugh III then was King of Jerusalem "
              "when Edward I made his crusade. In May 1271' (unnumbered). Gibbon not named near 'crusade'."),
    new("sd2-1897-conder-latin-kingdom", label="C. R. Conder, The Latin Kingdom of Jerusalem",
        author="C. R. Conder", work="The Latin Kingdom of Jerusalem, 1099 to 1291 A.D.", year_label="1897",
        year_sort="1897", place_publisher="London: Committee of the Palestine Exploration Fund",
        tradition="Britain", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="yes",
        H6="4", C="5", D="6", B="7", L1="8",
        quote="When the peace expired Pope Celestin III, now ninety years of age, preached a Fourth Crusade",
        url=IA + "latinkingdomofje00conduoft", verification_level="full_text",
        title_page_checked="yes (OCR: PALESTINE EXPLORATION FUND ... LONDON. 1897)", country="GB",
        channel="Michaud/Mills (inferred)",
        notes="'This fifth Crusade was heralded by a miracle' (1200, Fulk of Neuilly); 'The sixth Crusade was led by "
              "Andrew II'; 'The Duke of Brittany raided to Damascus in this seventh Crusade' (1239); 'So ended the "
              "sixth Crusade, and so also the eighth was to end' (Louis IX in Egypt). Same slots as Mills and the "
              "nine_H6 rows through L1 8; no ninth found. Bibliography: 'Gibbon's History of the Crusades. Michaud's "
              "Histoire des Croisades. Edit. 1877'; Röhricht and Archer cited."),
    new("sd2-1898-lane-poole-saladin", label="Stanley Lane-Poole, Saladin and the Fall of the Kingdom of Jerusalem",
        author="Stanley Lane-Poole", work="Saladin and the Fall of the Kingdom of Jerusalem (Heroes of the Nations)",
        year_label="1898", year_sort="1898", place_publisher="New York and London: Putnam",
        tradition="Britain", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="no",
        scheme_family="none", url=IA + "saladinandfallk00lanegoog", verification_level="full_text",
        title_page_checked="no", country="GB",
        notes="No ordinal numbers. Names Archer (13), Conder, Stubbs, Mills; Gibbon not named near 'crusade'."),
    dict(work_id="1907-w-b-stevenson", verification_level="full_text", C="4", D="5", B="7", L1="8",
         stated_count="8", stated_phrase="\"the eight crusades\"", url=IA + "crusadersineastb00stevuoft", checked_on=D,
         notes=app("1907-w-b-stevenson", "notes",
                   "[D2 2026-11-28] Index: '\"Second crusade\" 158 ff.'; '\"Third crusade\" 3, 260 ff.'; '\"Fourth "
                   "crusade\" 290, 296, 301' (running head 'THE \"FOURTH CRUSADE\" A.D. 1198-1203', the contingents that "
                   "reached Syria); '\"Fifth crusade\" 3, 301 ff.'; '\"Seventh crusade\" 3, 335 ff. (or 343 ff.)'; "
                   "'\"Eighth crusade\" 3, 343 ff.'. So B 7 and L1 8, with the alternative L1 7 noted. Page 3: 'The "
                   "crusades have been numbered as if they were a series well-defined and easily counted ... Only the "
                   "first crusade is rightly defined by the numeral attached.' Cites Wilken, Röhricht, Kugler, Riant, "
                   "Stubbs; no Gibbon.", W)),
]

L.upsert_works(works, clear_slots=[("1911-ernest-barker", "E")])
merge_rows("sd-1840-perry-history-crusades", "1865-walter-c-perry")
L.upsert_works([])  # regenerate shorthand and sort after the merge

# ---------------------------------------------------------------- attributes
W = cur()


def attr(wid, **kw):
    kw["work_id"] = wid
    kw.setdefault("checked_on", D)
    if wid in W and "gibbon_numbers" not in kw:
        kw["gibbon_numbers"] = L.gibbon_numbers(W[wid])
    return kw


A = [
    attr("1877-eb9-crusades", frame_id="R01", country_pub="Scotland", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="bibliography", gibbon_edition="unspecified", sources_named="Gibbon;Michaud;Mills",
         numbers_follow="michaud_mills;documented",
         notes="Bibliography names Michaud and Mills; H6 4 to L1 8 as Mills, L2 9 as Perry 1865 and Cox 1874."),
    attr("1911-ernest-barker", frame_id="R01", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Röhricht;Kugler;Prutz;Stevenson", numbers_follow="modern;inferred",
         notes="Footnote explains numbering and excludes Edward's crusade (reasons r29)."),
    attr("sd2-1929-eb14-crusades", frame_id="R01", country_pub="England", fourth_identity="C",
         fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="unchecked",
         numbers_follow="modern;documented", notes="Revision of EB11; numbering unchanged."),
    attr("sd2-1831-americana-chron-table", frame_id="R08", country_pub="US", author_origin="Germany",
         fourth_identity="other", fifth_identity="C", edward_status="absent", ninth_referent="other",
         gibbon_cited="none", numbers_follow="german;inferred",
         notes="Ninth = Barons' Crusade (Thibaut); fourth = 1189; Albigensian sixth. Editor Lieber German-born."),
    attr("sa-1830-americana", frame_id="R08", country_pub="US", author_origin="Germany", fourth_identity="other",
         fifth_identity="F", edward_status="absent", gibbon_cited="unchecked",
         numbers_follow="german;documented",
         notes="Built on the Conversations-Lexikon (title page). Fourth = Andrew II, 1217."),
    attr("1820-charles-mills", frame_id="P01", country_pub="England", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="last_unnumbered", gibbon_cited="preface;footnote",
         gibbon_edition="unspecified",
         sources_named="Gibbon;Vertot;Mailly;Sharon Turner;Michaud;Fuller;Heeren;Sismondi;Voltaire;Hume;Mosheim",
         numbers_follow="michaud_mills;inferred",
         notes="Head of the English H6-fourth line. Agrees with Michaud on H6 4, C 5, D 6; adds B 7, L1 8 and an "
               "unnumbered last crusade. Names Michaud. Preface sets his count against Gibbon's."),
    attr("sd2-1830-stebbing-chivalry", frame_id="P02", country_pub="Scotland", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="absent", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Gibbon;Michaud;Robertson;Fuller;Sharon Turner",
         numbers_follow="unclear;inferred", notes="No numbers. Edward not found in the passages read."),
    attr("sd2-1830-james-chivalry", frame_id="P03", country_pub="England", author_origin="England",
         fourth_identity="other", fifth_identity="C", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Mills;Vertot;Guizot;Robertson;Voltaire;Fuller;Sharon Turner",
         numbers_follow="michaud_mills;documented",
         notes="C 5 as Mills; names Mills 38 times. Fourth not numbered (H6 told unnumbered)."),
    attr("sd2-1834-keightley-crusaders", frame_id="P04", country_pub="England", author_origin="Ireland",
         fourth_identity="none", fifth_identity="none", edward_status="absent", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Wilken;Michaud;Mills;Gibbon", numbers_follow="unclear;inferred",
         notes="Stops at the Third Crusade's numbers."),
    attr("1852-michaud-trans-william-robson", frame_id="P07", country_pub="England", author_origin="France",
         fourth_identity="H6", fifth_identity="C", edward_status="inside_last", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Gibbon;Salaberry", numbers_follow="own;documented",
         notes="Translation: Michaud's own numbering."),
    attr("sd2-1900-michaud-robson-ny", frame_id="P07", country_pub="US", author_origin="France",
         fourth_identity="H6", fifth_identity="C", edward_status="inside_last", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Gibbon", numbers_follow="own;documented",
         notes="US printing of the translation."),
    attr("1842-george-proctor", frame_id="P08", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D+F", edward_status="inside_last", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Gibbon;Mills;Michaud;Hallam;Heeren;Robertson;Mosheim;Vertot",
         numbers_follow="own;documented",
         notes="Footnote rejects the H6-fourth count of nine and states the custom of seven or eight (r30, r31)."),
    attr("sd2-1856-procter-philadelphia", frame_id="P08", country_pub="US", author_origin="England",
         fourth_identity="C", fifth_identity="D+F", edward_status="inside_last", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Gibbon;Mills;Michaud;Hallam;Heeren",
         numbers_follow="own;documented", notes="US printing."),
    attr("sd2-1853-bloss-heroines", frame_id="P09", country_pub="US", author_origin="US",
         fourth_identity="H6", fifth_identity="C", edward_status="inside_last", gibbon_cited="none",
         sources_named="Mills;Michelet;Hume;Lingard;Fuller", numbers_follow="moreri;inferred",
         notes="moreri_eight slots, shared with Michaud (Robson 1852) and EB2-8; names neither. The eighth is dated "
               "1272 and centered on Edward and Eleanor."),
    attr("sd2-1849-sargent-sketches", frame_id="P10", country_pub="England", fourth_identity="H6",
         fifth_identity="other", edward_status="last_unnumbered", gibbon_cited="quoted;footnote",
         gibbon_edition="unspecified", sources_named="Gibbon;Mills;Robertson;Fuller",
         numbers_follow="michaud_mills;inferred",
         notes="Fifth placed between Henry VI's crusade and Innocent III's Inquisition; its identity not stated."),
    attr("1865-walter-c-perry", frame_id="P11", country_pub="England", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="named_unnumbered", ninth_referent="tunis",
         gibbon_cited="preface;footnote", gibbon_edition="unspecified",
         sources_named="Michaud;Wilken;Gibbon;Milman;Heeren;Mills", numbers_follow="michaud_mills;documented",
         notes="Preface: chiefly based on Michaud; Gibbon the authority for the Fifth (1202-04), yet numbered fifth. "
               "Mills's slots, with Mills's 'last crusade' numbered ninth."),
    attr("1874-george-w-cox", frame_id="P12", country_pub="England", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="none", numbers_follow="michaud_mills;inferred",
         notes="Same slots as Perry 1865 with Edward inside the ninth."),
    attr("sd2-1860-edgar-crusaders", frame_id="P15", country_pub="US", author_origin="Scotland",
         fourth_identity="none", fifth_identity="none", edward_status="last_unnumbered", gibbon_cited="none",
         sources_named="Fuller;Michaud", numbers_follow="unclear;inferred"),
    attr("sd2-1871-besant-palmer-jerusalem", frame_id="P16", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Michaud;Milman", numbers_follow="unclear;inferred"),
    attr("1894-t-a-archer-c-l-kingsford", frame_id="P17", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Lane-Poole;Kugler;Prutz;Besant", numbers_follow="unclear;inferred",
         notes="H6 called 'the German Crusade', unnumbered."),
    attr("1894-j-i-mombert", frame_id="P18", country_pub="US", author_origin="Germany", fourth_identity="C",
         fifth_identity="D", edward_status="inside_last", gibbon_cited="preface;named_in_text",
         gibbon_edition="unspecified", sources_named="Gibbon;Heeren;Milman;Guizot;Ranke;Michaud",
         numbers_follow="modern;inferred", notes="Modern eight; H6 'Henry VI.'s Expedition' unnumbered."),
    attr("1896-j-m-ludlow", frame_id="P19", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="D", gibbon_cited="bibliography;quoted", gibbon_edition="unspecified",
         sources_named="Gibbon;Pears;Michaud", numbers_follow="modern;documented",
         notes="Quotes Pears on 'the crime of the fourth crusade'. Edward not checked."),
    attr("sd2-1913-blyth-jerusalem", frame_id="P22", country_pub="England", fourth_identity="none",
         fifth_identity="none", edward_status="last_unnumbered", ninth_referent="other", gibbon_cited="none",
         sources_named="Lane-Poole", numbers_follow="unclear;inferred",
         notes="Ninth = Louis IX's first crusade (1248)."),
    attr("sd2-1930-lamb-flame-islam", frame_id="P26", country_pub="US", author_origin="US",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Röhricht;Riant;Barker;Stevenson;Stubbs", numbers_follow="unclear;inferred"),
    attr("sd2-1904-historians-history-v8", frame_id="P20", country_pub="US", author_origin="US",
         fourth_identity="H6", fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="quoted", gibbon_edition="unspecified", sources_named="Mills;Gibbon;Herder",
         numbers_follow="michaud_mills;documented",
         notes="Copies Mills's wording; outline of the Fourth follows EB9."),
    attr("1885-edwin-pears", frame_id="H04", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="none", edward_status="absent", gibbon_cited="named_in_text",
         gibbon_edition="unspecified", sources_named="Riant;Gibbon;Cox;Michaud;Sismondi;Mills;Milman;Stubbs",
         numbers_follow="french_school;inferred",
         notes="'The Story of the Fourth Crusade'; main authority Riant, whose 1875 article title speaks of 'la "
               "quatrième croisade' (title not checked in this pass)."),
    attr("sd2-1868-students-gibbon", frame_id="S08", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="inside_last", gibbon_cited="named_in_text",
         gibbon_edition="Student's Gibbon", sources_named="Gibbon", numbers_follow="gibbon;documented"),
    attr("sd2-1818-hallam-middle-ages", frame_id="H01", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="none", edward_status="absent", gibbon_cited="footnote",
         gibbon_edition="unspecified",
         sources_named="Gibbon;Sismondi;Heeren;Robertson;Mosheim;Fleury;Vertot;Lingard;Sharon Turner",
         numbers_follow="gibbon;inferred", notes="Read in the New York 1857 printing."),
    attr("sd2-1830-turner-middle-ages", frame_id="C15", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="footnote",
         gibbon_edition="unspecified", sources_named="Gibbon;Mills;Sismondi", numbers_follow="gibbon;inferred",
         notes="L2 7 'what is called'."),
    attr("sd2-1854-milman-latin-christianity", frame_id="H02", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", gibbon_cited="none",
         sources_named="Michaud;Wilken;Raumer;Heeren;Guizot;Gieseler", numbers_follow="unclear;inferred",
         notes="The one Gibbon mention near 'crusade' concerns the Paulicians, outside the crusade narrative."),
    attr("sd2-1886-stubbs-lectures", frame_id="H03", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred", notes="C 4, D 5 fit both Gibbon and the modern eight."),
    attr("sd2-1897-conder-latin-kingdom", frame_id="H05", country_pub="England", author_origin="England",
         fourth_identity="H6", fifth_identity="C", gibbon_cited="bibliography", gibbon_edition="unspecified",
         sources_named="Gibbon;Michaud;Röhricht;Archer;Besant;Guizot", numbers_follow="michaud_mills;inferred",
         notes="Bibliography lists 'Gibbon's History of the Crusades', the separately printed extract of chapters "
               "58-60, and Michaud ed. 1877. Edward not checked."),
    attr("sd2-1898-lane-poole-saladin", frame_id="H06", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="absent", gibbon_cited="none",
         sources_named="Archer;Conder;Stubbs;Mills", numbers_follow="unclear;inferred"),
    attr("1907-w-b-stevenson", frame_id="H09", country_pub="England", author_origin="Scotland",
         fourth_identity="C", fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Wilken;Röhricht;Kugler;Riant;Stubbs;Guizot", numbers_follow="unclear;documented",
         notes="Numbers only in quotation marks; rejects the numbering (r33)."),
    attr("1788-edward-gibbon", frame_id="H21", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", gibbon_cited="", numbers_follow="own;documented",
         notes="Reference row for the Gibbon comparison."),
]
L.upsert_attrs(A)

# ---------------------------------------------------------------- citations
C = [
    ("1820-charles-mills", "Gibbon", "criticizes coverage in preface",
     "Preface: Gibbon's sketches 'principally taken from Vertot ... and from Mailly'; 'The fourth, sixth, and seventh "
     "Crusades are altogether unnoticed by Mr. Gibbon'", "documented"),
    ("1820-charles-mills", "Sharon Turner", "praises in preface",
     "'the only author who appears to have justly appreciated the subject'", "documented"),
    ("1820-charles-mills", "Michaud", "names", "1820 and 1828 text layers", "documented"),
    ("1865-walter-c-perry", "Michaud", "chiefly based on (preface)", "Preface, New York printing", "documented"),
    ("1865-walter-c-perry", "Wilken", "names as a principal history (preface)", "Preface", "documented"),
    ("1865-walter-c-perry", "Gibbon", "follows for the Fifth Crusade (1202-04) (preface)",
     "'For the Fifth Crusade no other writer can take the place of Gibbon'", "documented"),
    ("1865-walter-c-perry", "Milman", "freely used (preface)", "Preface", "documented"),
    ("1865-walter-c-perry", "Heeren", "freely used (preface)", "Preface", "documented"),
    ("1865-walter-c-perry", "Mills", "names", "9 mentions in the text layer", "documented"),
    ("1877-eb9-crusades", "Gibbon", "lists in bibliography", "US reprint, vol. 6", "documented"),
    ("1877-eb9-crusades", "Michaud", "lists in bibliography", "US reprint, vol. 6", "documented"),
    ("1877-eb9-crusades", "Mills", "lists in bibliography", "US reprint, vol. 6", "documented"),
    ("1911-ernest-barker", "1842-george-proctor", "echoes footnote on why crusades were numbered",
     "Procter: 'dignified the abortive result with the title of the Fourth Crusade' ... occasions 'such as the loss of "
     "Edessa or Jerusalem'; Barker: 'dignified by numbers when they followed some crushing disaster - the loss of "
     "Edessa in 1144, or the fall of Jerusalem in 1187'. Under eight consecutive words: not copying by rule 4",
     "inferred"),
    ("sd2-1830-james-chivalry", "Mills", "cites", "38 mentions in the text layer", "documented"),
    ("sd2-1830-james-chivalry", "Vertot", "cites", "21 mentions in the text layer", "documented"),
    ("sd2-1853-bloss-heroines", "Mills", "names", "6 mentions in the text layer", "documented"),
    ("sd2-1849-sargent-sketches", "Gibbon", "quotes", "'Gibbon declares that ...'", "documented"),
    ("sd2-1849-sargent-sketches", "Mills", "names", "2 mentions", "documented"),
    ("sd2-1897-conder-latin-kingdom", "Gibbon", "lists in bibliography", "'Gibbon's History of the Crusades'",
     "documented"),
    ("sd2-1897-conder-latin-kingdom", "Michaud", "lists in bibliography", "'Michaud's Histoire des Croisades. Edit. "
                                                                          "1877'", "documented"),
    ("sd2-1818-hallam-middle-ages", "Gibbon", "assesses in note on authorities",
     "'Gibbon's two chapters on the crusades, though not without inaccuracies, are a brilliant portion'", "documented"),
    ("1885-edwin-pears", "Riant", "principal authority", "14 mentions in the text layer", "documented"),
    ("1896-j-m-ludlow", "1885-edwin-pears", "quotes on the fourth crusade",
     "'The crime of the fourth crusade handed over Constantinople and the Balkan peninsula to six centuries of "
     "barbarism'", "documented"),
    ("1896-j-m-ludlow", "Gibbon", "lists in bibliography; quotes", "Bibliography: London, 1776-81, 6 vols.",
     "documented"),
    ("1894-j-i-mombert", "Gibbon", "names as counselor (preface)",
     "'Gibbon, Heeren, Milman, Guizot, and Ranke as my chosen counselors'", "documented"),
    ("sd2-1868-students-gibbon", "1788-edward-gibbon", "abridges", "Title and text", "documented"),
    ("sd2-1904-historians-history-v8", "1820-charles-mills", "reprints extracts",
     "'the successes of the savage Khwarizmians, gave birth to the Eighth Crusade. Pope Innocent IV convoked' (Mills: "
     "'Korasmians')", "documented"),
    ("sd2-1904-historians-history-v8", "1877-eb9-crusades", "outline of the Fourth follows",
     "Knights of St John in 1193; Celestine III's hopes of Henry VI", "inferred"),
    ("sd2-1929-eb14-crusades", "1911-ernest-barker", "revises", "Same article, revised", "documented"),
]
L.append_citations([dict(citing_work_id=a, cited=b, relation=c, evidence=d, confidence=e) for a, b, c, d, e in C])

# ---------------------------------------------------------------- reasons
R = [
    dict(reason_id="r29", year="1911", work="Encyclopaedia Britannica, 11th ed., Crusades", author="Ernest Barker",
         language="en", entry_id="1911-ernest-barker", kind="explanation", target="scheme",
         expeditions_affected="E; Henry the Lion 1172; 1101; 1123-24",
         phrase="Crusades appear to have been dignified by numbers when they followed some crushing disaster - the "
                "loss of Edessa in 1144, or the fall of Jerusalem in 1187 - and were led by kings and emperors; or "
                "when, like the Fourth and Fifth Crusades, they achieved some conspicuous success or failure.",
         verification="full_text", source="archive.org encyclopaediabrit07chisrich (vol. 7)",
         notes="Same footnote names the crusades of 1101, 1123-24, Henry the Lion 1172 and Edward I 1271-72 as 'not "
               "reckoned in the usual numbering'. Kept in EB14 (1929), moved into the text. Echoes Procter (r31)."),
    dict(reason_id="r30", year="1842", work="History of the Crusades", author="George Procter", language="en",
         entry_id="1842-george-proctor", kind="rejection", target="H6 as fourth; count of nine",
         expeditions_affected="H6;C",
         phrase="some writers have dignified the abortive result with the title of the Fourth Crusade; and numbered "
                "the subsequent expedition, which was directed against the Byzantine Empire, as the Fifth of Nine.",
         verification="full_text", source="archive.org historycrusades00procgoog (Philadelphia 1856)",
         notes="Footnote to the German expedition of 1195-97."),
    dict(reason_id="r31", year="1842", work="History of the Crusades", author="George Procter", language="en",
         entry_id="1842-george-proctor", kind="explanation", target="scheme", expeditions_affected="all",
         phrase="the more usual, which seems also the more convenient division, restricts the term of distinct "
                "Crusades to Seven, or at most Eight, great efforts, which were either produced by some signal "
                "occasion, such as the loss of Edessa or Jerusalem, or else productive of some considerable event.",
         verification="full_text", source="archive.org historycrusades00procgoog (Philadelphia 1856)",
         notes="Also a statement of custom (seven or eight). Barker 1911 (r29) gives the same two criteria."),
    dict(reason_id="r32", year="1907", work="The Crusaders in the East", author="W. B. Stevenson", language="en",
         entry_id="1907-w-b-stevenson", kind="rejection", target="scheme", expeditions_affected="all",
         phrase="The crusades have been numbered as if they were a series well-defined and easily counted. Some eight "
                "... have been selected as \"the eight crusades.\" They are chosen on no clear principle.",
         verification="full_text", source="archive.org crusadersineastb00stevuoft, p. 3",
         notes="Continues: 'Only the first crusade is rightly defined by the numeral attached.' Uses the numbers "
               "only in quotation marks."),
    dict(reason_id="r33", year="1830", work="The History of England during the Middle Ages", author="Sharon Turner",
         language="en", entry_id="sd2-1830-turner-middle-ages", kind="statement_of_custom", target="L2",
         expeditions_affected="L2", phrase="He died before Tunis, in what is called the seventh Crusade, in 1270.",
         verification="full_text", source="archive.org historyenglandd00turngoog",
         notes="Gibbon's L2 7 reported as usage."),
]
L.append_reasons(R)

# ---------------------------------------------------------------- search log
B = "archive.org metadata and djvu text (browser)"
LOG = [
    (B, "Britannica CRUSADES: 9th ed. US reprints (encyclopaediabri0006unse_b8h3; encyclopaediabri06kell), 11th "
        "(encyclopaediabrit07chisrich), 1922, 1926, 1929, 1938, 1944 printings", "1875-1944", "8 items", "8",
     "1877-eb9-crusades; 1911-ernest-barker; sd2-1929-eb14-crusades; 1938 and 1944 lending copies not reached"),
    (B, "Encyclopaedia Americana 1829-33, HISTORY chronological table (encyclopaediaam00bradgoog): crusade "
        "ordinals", "1829-33", "11 entries", "11", "sd2-1831-americana-chron-table"),
    (B, "Popular histories batch 1: Mills (4 eds.), Stebbing (2 vols.), G. P. R. James, Keightley (2 eds.), "
        "Michaud abridged, Michaud/Robson 1852 and 1900, Procter 1856 and 1876, Bloss, Sargent (2 copies), Perry",
     "1820-1900", "18 items", "17",
     "1820-charles-mills; sd2-1830-stebbing-chivalry; sd2-1830-james-chivalry; sd2-1834-keightley-crusaders; "
     "1852-michaud-trans-william-robson; sd2-1900-michaud-robson-ny; 1842-george-proctor; "
     "sd2-1856-procter-philadelphia; sd2-1853-bloss-heroines; sd2-1849-sargent-sketches; 1865-walter-c-perry; "
     "excluded: history-of-the-crusades-abridged-j.-f.-michaud (a modern generated translation)"),
    (B, "Popular histories batch 2: Cox 1874 and 1890, W. H. D. Adams, Edgar 1860, Besant and Palmer, Archer and "
        "Kingsford, Mombert, Ludlow, Blyth, Lamb, Historians' History vol. 8, Ridpath vol. 1, Michaud 1891, "
        "Procter (Princeton copy)", "1860-1930", "14 items", "14",
     "1874-george-w-cox; sd2-1860-edgar-crusaders; sd2-1871-besant-palmer-jerusalem; "
     "1894-t-a-archer-c-l-kingsford; 1894-j-i-mombert; 1896-j-m-ludlow; sd2-1913-blyth-jerusalem; "
     "sd2-1930-lamb-flame-islam; sd2-1904-historians-history-v8; not usable: Adams (wrong title), Ridpath "
     "(wrong volume)"),
    (B, "Scholarly and Gibbon batch 1: Gibbon (Bohn variorum vol. 6, Milman ed. vol. 5, Methuen vol. 6, 1820 ed. "
        "vol. 6), Student's Gibbon, Hallam, Sharon Turner, Milman (vols. 4-5), Robertson vol. 5, Joseph Milner "
        "vol. 17, Stubbs, Conder, Lane-Poole, Pears, Stevenson", "1820-1907", "16 items", "16",
     "1788-edward-gibbon; sd2-1868-students-gibbon; sd2-1818-hallam-middle-ages; sd2-1830-turner-middle-ages; "
     "sd2-1854-milman-latin-christianity; sd2-1886-stubbs-lectures; sd2-1897-conder-latin-kingdom; "
     "sd2-1898-lane-poole-saladin; 1885-edwin-pears; 1907-w-b-stevenson; not usable: Robertson vol. 5 and Milner "
     "vol. 17 (wrong volumes), 1820 Gibbon vol. 6 (no text layer)"),
    ("archive.org advancedsearch (browser)", "identifier searches for 32 scholarly, church and school titles "
                                             "(Gibbon, Hallam, Turner, Milman, Robertson, Mosheim, Milner, Lingard, "
                                             "Tytler, Keightley, Yonge, Freeman, Tout, White, Dickens, Stubbs, ...)",
     "1800-1945", "32 queries", "32", "identifiers for batches"),
    ("archive.org advancedsearch (browser)", "identifier searches for 24 school-text titles (Goodrich, Willson, "
                                             "Worcester, Fredet, Fisher, Anderson, West, Robinson, Breasted, "
                                             "Webster, Thatcher, Pinnock, Mangnall, Tout, Emerton, Adams, Duruy, "
                                             "Greene, Gilman, Barnes, Sanderson, Ransome, Irish, Canadian)",
     "1800-1945", "24 queries", "24", "identifiers for batches"),
]
L.append_log(D, LOG)

# ---------------------------------------------------------------- frame status
L.set_frame_status({
    "R01": ("partial", "1877-eb9-crusades;1911-ernest-barker;sd2-1929-eb14-crusades",
            "D2: 9th (US reprints), 11th, 1922, 1926, 1929 read; 1938 and 1944 lending copies not reached"),
    "R08": ("partial", "sd2-1831-americana-chron-table", "D2: 1829-33 chronological table read"),
    "P01": ("read", "", "D2: 1820, 1821, 1828, 1844 texts"),
    "P02": ("read", "sd2-1830-stebbing-chivalry", ""),
    "P03": ("read", "sd2-1830-james-chivalry", ""),
    "P04": ("read", "sd2-1834-keightley-crusaders", ""),
    "P07": ("read", "sd2-1900-michaud-robson-ny", "D2: index and vol. 3 contents; Frederick II not checked"),
    "P08": ("read", "sd2-1856-procter-philadelphia", "D2: Philadelphia 1856 and New York 1876"),
    "P09": ("read", "sd2-1853-bloss-heroines", ""),
    "P10": ("read", "sd2-1849-sargent-sketches", ""),
    "P11": ("read", "", "D2: author corrected (G. G. Perry, not Walter C. Perry)"),
    "P12": ("read", "", "D2: 1874 and 1890 texts"),
    "P14": ("not_reached", "", "D2: The Wars of the Cross not found; Heroes of the Cross is a different book"),
    "P15": ("read", "sd2-1860-edgar-crusaders", "D2: Boston 1860 printing"),
    "P16": ("read", "sd2-1871-besant-palmer-jerusalem", ""),
    "P17": ("read", "", ""),
    "P18": ("read", "", ""),
    "P19": ("read", "", ""),
    "P20": ("read", "sd2-1904-historians-history-v8", ""),
    "P22": ("read", "sd2-1913-blyth-jerusalem", ""),
    "P23": ("not_reached", "", "D2: only vol. 1 of the Cyclopaedia of Universal History had a text layer"),
    "P26": ("partial", "sd2-1930-lamb-flame-islam", "D2: Iron Men and Saints is a lending copy"),
    "P27": ("not_reached", "", "D2: Belloc, The Crusade (1937) is a lending copy without text"),
    "P32": ("merged", "1865-walter-c-perry", "D2: same copy as P11; archive.org date 1840 wrong"),
    "H01": ("read", "sd2-1818-hallam-middle-ages", "D2: New York 1857 printing"),
    "H02": ("read", "sd2-1854-milman-latin-christianity", "D2: vols. 4-5"),
    "H03": ("read", "sd2-1886-stubbs-lectures", ""),
    "H04": ("read", "", ""),
    "H05": ("read", "sd2-1897-conder-latin-kingdom", ""),
    "H06": ("read", "sd2-1898-lane-poole-saladin", ""),
    "H09": ("read", "", ""),
    "H21": ("partial", "", "D2: Bohn variorum vol. 6 and Methuen (Bury) vol. 6 read; Milman ed. crusade volume "
                          "not reached"),
    "S08": ("partial", "sd2-1868-students-gibbon", "D2: Student's Gibbon read; other Student's manuals pending"),
    "C15": ("read", "sd2-1830-turner-middle-ages", ""),
})
print("block 1 written")
