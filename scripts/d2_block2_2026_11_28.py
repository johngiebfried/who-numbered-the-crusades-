"""Strand D2, block 2 (28 November 2026): school texts, chronologies and the works found by the
"ninth crusade" sweep, read in the archive.org text layer through the built-in browser.

Same conventions as d2_block1_2026_11_28.py. Adds the family code nine_B7 (protocol amendment 1,
docs/DECISIONS.md). MIT License.
"""
import d2_lib as L

D = "2026-11-28"
TXT = "archive.org djvu text via built-in browser"
IA = "https://archive.org/details/"


def cur():
    return {w["work_id"]: w for w in L._read(L.WORKS)[1]}


def app(wid, field, text, works):
    old = works[wid][field] if wid in works else ""
    if text in old:
        return old
    return (old + " | " if old else "") + text


def new(wid, **kw):
    base = dict(work_id=wid, language="English", research_pass="strand_d2", checked_on=D,
                how_verified=TXT, access=TXT)
    base.update(kw)
    return base

W = cur()


def school(wid, **kw):
    kw.setdefault("genre", "School")
    kw.setdefault("census_frame", "d2_school_en")
    return new(wid, **kw)


works = [
    school("sd2-1801-tytler-elements", label="A. F. Tytler, Elements of General History",
           author="Alexander Fraser Tytler", work="Elements of General History, Ancient and Modern",
           year_label="1801 (read New York 1819 printing with Robbins's continuation; also 1837, Nares 1839)",
           year_sort="1801", place_publisher="Edinburgh (first ed.); read New York: E. Duyckinck et al.",
           tradition="Britain", enumerates="partial", C="4", D="5",
           quote="A fourth crusade was fitted out in 1202, under Baldwin Count of Flanders, of which the object was "
                 "not the extirpation of",
           url=IA + "elementsgeneral00woodgoog", verification_level="full_text",
           title_page_checked="no (metadata: 1819, E. Duyckinck, D. D. Smith & G. Long)", country="GB",
           notes="'The object of a fifth crusade was to lay waste Egypt, in revenge for an attack on Palestine, by its "
                 "sultan Saphadin' (D 5). Louis IX's expedition of 1248 is 'the last crusade under Lewis IX.', while "
                 "the chronological table has '1248 The fifth Crusade under St. Lewis' (a list of five that skips "
                 "Damietta). 'Ptolemais taken by the Turks. End of the Crusades.' Same text in the 1837 printing "
                 "(elementsofgenera08wood) and Nares's 1839 edition (elementsgeneral00naregoog)."),
    school("sd2-1830-keightley-outlines", label="Thomas Keightley, Outlines of History (Lardner)",
           author="Thomas Keightley", work="Outlines of History (Lardner's Cabinet Cyclopaedia)", year_label="1830",
           year_sort="1830", place_publisher="London: Longman", tradition="Britain", enumerates="partial",
           C="4", D="5",
           quote="The fifth crusade was chiefly composed of Germans and the neighbouring people; Andrew II., king of "
                 "Hungary, was its commander",
           url=IA + "outlineshistory00lardgoog", verification_level="full_text",
           title_page_checked="no (metadata: London, Longman, 1830)", country="GB",
           notes="'as the fourth crusade was then preparing to set out for Asia, he persuaded its commanders to assist "
                 "in restoring his father' (C 4). After Louis IX's death 'died the spirit of the crusades. Edward, son "
                 "of our Henry III., revived the fame of Richard' (unnumbered)."),
    school("sd2-1864-yonge-landmarks", label="C. M. Yonge, Landmarks of History: Middle Ages",
           author="Charlotte M. Yonge", work="Landmarks of History: Middle Ages", year_label="1864 (printing read)",
           year_sort="1864", place_publisher="London: Mozley", tradition="Britain", enumerates="yes",
           C="4", D="5", F="6", L1="7", scheme_family="near_modern", signature_match="near_modern",
           quote="PART II. THE FOURTH CRUSADE. 1201-1203 ... The Fifth and Sixth Crusades ... PART III. THE SEVENTH "
                 "CRUSADE. 1248-1254 ... PART II. THE LAST CRUSADE. 1270-1272",
           url=IA + "landmarksofhisto00yonguoft", verification_level="full_text",
           title_page_checked="no (metadata: London, Mozley, 1864)", country="GB",
           notes="'In 1217, Andrew King of Hungary undertook a fifth Crusade'; Frederick II in 'The Fifth and Sixth "
                 "Crusades'. The expedition of 1270-72 is 'THE LAST CRUSADE', unnumbered. First edition date not "
                 "checked."),
    school("sd2-1872-freeman-sketch", label="E. A. Freeman, General Sketch of European History",
           author="Edward A. Freeman", work="General Sketch of European History (Historical Course for Schools)",
           year_label="1872", year_sort="1872", place_publisher="London: Macmillan", tradition="Britain",
           enumerates="partial", C="4",
           quote="Fourth Crusade; taking of Constantinople by the Franks and Venetians",
           url=IA + "generalsketcheu00freegoog", verification_level="full_text",
           title_page_checked="no", country="GB",
           notes="Only the Fourth is numbered. 'Crusades of Saint Louis and of Edward the First' (unnumbered)."),
    school("sd2-1858-white-eighteen-centuries", label="James White, The Eighteen Christian Centuries",
           author="James White", work="The Eighteen Christian Centuries", year_label="1858 (read Philadelphia 1859)",
           year_sort="1858", place_publisher="Edinburgh: Blackwood; read Philadelphia: Parry & McMillan",
           tradition="Britain", enumerates="yes", C="4", D="5", F="6", L1="7", L2="8",
           stated_phrase="Eighth and Last Crusade", scheme_family="modern_eight", signature_match="modern",
           quote="Fourth Crusade. 1248. Seventh Crusade. Fifth Crusade. 1270. Eighth and Last Crusade, 1228. Sixth "
                 "Crusade. by St. Louis against Tunis",
           url=IA + "eighteenchristia00whit_0", verification_level="full_text",
           title_page_checked="no (metadata: Philadelphia, Parry & McMillan, 1859)", country="GB",
           notes="Chronological table at the head of the thirteenth century (OCR scrambles the columns; the order by "
                 "date is C 4, D 5 (1217), F 6 (1228), L1 7 (1248), L2 8 (1270)). Text: 'in the year 1248 the seventh "
                 "and last crusade to the Holy Land took its way from Aigues-Mortes'. With Beale (London 1858), the "
                 "earliest British modern eight found."),
    school("sd2-1853-goodrich-all-nations", label="S. G. Goodrich, A History of All Nations",
           author="Samuel G. Goodrich", work="A History of All Nations, from the Earliest Periods to the Present Time",
           year_label="1853 (printing read)", year_sort="1853", place_publisher="Auburn, N.Y.: Derby and Miller",
           tradition="US", enumerates="yes", C="4", D="5", L1="6", L2="7",
           stated_phrase="the Seventh and last Crusade", scheme_family="gibbon_seven", signature_match="no",
           quote="he took Damietta, but was obliged to surrender; and thus ended the Fifth Crusade ... this was the "
                 "Sixth Crusade ... Thus ended the Seventh and last Crusade",
           url=IA + "ahistoryallnati00goodgoog", verification_level="full_text",
           title_page_checked="no (metadata: Auburn, N.Y., Derby and Miller, 1853)", country="US",
           notes="Baldwin of Flanders 'set out with an immense army on a Fourth Crusade, but took possession of "
                 "Constantinople'; Louis IX's Egyptian crusade the sixth, Tunis the seventh and last. Then: 'Some "
                 "writers make ten, namely, in 1096, 1110, '50, '90, '95, 1909, '17, '98, '40, '48' (OCR; read "
                 "1096, 1101?, 1147, 1189, 1195, 1202, 1217, 1228, 1240, 1248: reasons r34)."),
    school("sd2-1854-willson-outlines", label="Marcius Willson, Outlines of History",
           author="Marcius Willson", work="Outlines of History", year_label="1854", year_sort="1854",
           place_publisher="New York: Ivison & Phinney", tradition="US", enumerates="partial", C="4", D="5",
           quote="The fourth crusade ended without producing any benefit to Palestine. 28. The fifth crusade, "
                 "undertaken fourteen years after the fall of the Byzantine empire, was at first conducted by Andrew",
           url=IA + "outlineshistory08willgoog", verification_level="full_text",
           title_page_checked="no (metadata: New York, Ivison & Phinney, 1854)", country="US",
           notes="Edward I 'was absent on the last crusade to the Holy Land (A.D. 1272)'. Footnotes cite Gibbon "
                 "('Gibbon, iv. 116-133'). The sentence on the Fourth echoes G. P. R. James's on his fifth ('THE fifth "
                 "crusade had ended, as we have seen, without producing any other benefit to Palestine'), with the "
                 "number changed."),
    school("sd2-1843-worcester-elements", label="J. E. Worcester, Elements of History",
           author="Joseph Emerson Worcester", work="Elements of History, Ancient and Modern",
           year_label="1843 printing (first ed. 1826)", year_sort="1843", place_publisher="Boston: W. J. Reynolds",
           tradition="US", enumerates="partial", C="4",
           quote="Baldwin, count of Flanders, collected an army to act against the Mahometans in a fourth crusade",
           url=IA + "elementshistory00unkngoog", verification_level="full_text",
           title_page_checked="no (metadata: W. J. Reynolds, 1843)", country="US",
           notes="Table: '1270 Last Crusade, under St. Louis IX.' Edward not mentioned with the crusades."),
    school("sd2-1842-fredet-modern-history", label="Peter Fredet, Modern History",
           author="Peter Fredet", work="Modern History; from the Coming of Christ", year_label="1842",
           year_sort="1842", place_publisher="Baltimore: J. Murphy", tradition="US", enumerates="yes",
           H6="4", C="5", B="6", L1="7", L2="8", E="8", stated_phrase="Eighth and last Crusade",
           scheme_family="moreri_eight", signature_match="no",
           quote="Third Crusade, 39 Fourth Crusade, 48 Fifth Crusade. - Foundation of the Latin empire of "
                 "Constantinople, 50 ... Sixth Crusade, 66 Seventh Crusade. - St. Louis, 69 ... Eighth and last "
                 "Crusade, 75",
           url=IA + "modernhistoryfro00fre", verification_level="full_text",
           title_page_checked="no (metadata: Baltimore, J. Murphy, 1842)", country="US",
           notes="Catholic college text (St Mary's, Baltimore). The fourth opens with Celestine III; the sixth "
                 "includes 'Palestine was next visited by Theobaldus, king of Navarre' (D and F placement not "
                 "checked). Edward shares 'in the second crusade of St. Louis - the eighth and last of the crusades'."),
    school("sd2-1870-anderson-manual", label="J. J. Anderson, A Manual of General History",
           author="John J. Anderson", work="A Manual of General History", year_label="1870", year_sort="1870",
           place_publisher="New York: Clark & Maynard", tradition="US", enumerates="yes",
           C="4", F="5", L1="6", L2="7", E="7", scheme_family="frederick_fifth_seven", signature_match="no",
           quote="The Fourth Crusade was enjoined by Pope Innocent III. (1203) ... The Fifth Crusade was led by "
                 "Frederick II ... The Sixth Crusade was undertaken by Louis IX ... The Seventh Crusade was undertaken "
                 "by St. Louis in alliance with Prince Edward",
           url=IA + "manualofgeneralh01ande", verification_level="full_text",
           title_page_checked="no (metadata: New York, Clark & Maynard, 1870)", country="US",
           notes="Andrew II and Damietta not numbered. Review questions repeat the numbers. Frederick-fifth seven in a "
                 "US school text; the British witness of the shape is Chambers's Encyclopaedia (1868)."),
    school("sd2-1915-west-modern-world", label="W. M. West, The Modern World",
           author="Willis Mason West", work="The Modern World, from Charlemagne to the Present Time",
           year_label="1915", year_sort="1915", place_publisher="Boston: Allyn and Bacon", tradition="US",
           enumerates="partial", C="4", L1="7",
           quote="Then, in 1249, Louis IX of France organized the Seventh Crusade",
           url=IA + "modernworldfrom00westgoog", verification_level="full_text", title_page_checked="no",
           country="US",
           notes="'the Fourth Crusade was diverted from its purpose into a commercial war upon a Christian state'; "
                 "'after a terrible loss of life in the Fifth and Sixth Crusades, the Emperor Frederick II recovered "
                 "Jerusalem'; Tunis unnumbered ('another expedition, twenty years later')."),
    school("sd2-1903-robinson-western-europe", label="J. H. Robinson, An Introduction to the History of Western "
                                                   "Europe",
           author="James Harvey Robinson", work="An Introduction to the History of Western Europe",
           year_label="1903", year_sort="1903", place_publisher="Boston: Ginn", tradition="US", enumerates="no",
           scheme_family="none", url=IA + "anintroductiont06robigoog", verification_level="full_text",
           title_page_checked="no", country="US",
           notes="No ordinal in the narrative; 'The Fourth Crusade' only as the title of Munro's Translations and "
                 "Reprints III.1 in the reading list, beside Archer and Kingsford."),
    school("sd2-1920-breasted-robinson", label="Breasted and Robinson, History of Europe, Ancient and Medieval",
           author="James Henry Breasted; James Harvey Robinson",
           work="History of Europe, Ancient and Medieval", year_label="1920", year_sort="1920",
           place_publisher="Boston: Ginn", tradition="US", enumerates="no", scheme_family="none",
           url=IA + "historyofeuropea00brea", verification_level="full_text", title_page_checked="no", country="US",
           notes="No ordinals. Additional reading: 'Archer and Kingsford, The Crusades. Gibbon, Decline and Fall of "
                 "the Roman Empire, chaps. lviii-lix. See \"Crusades,\" in Encyclopaedia Britannica'."),
    school("sd2-1917-webster-early-european", label="Hutton Webster, Early European History",
           author="Hutton Webster", work="Early European History", year_label="1917", year_sort="1917",
           place_publisher="Boston: D. C. Heath", tradition="US", enumerates="partial", C="4",
           quote="Fourth Crusade and the Latin Empire of Constantinople, 1202-1261 A.D.",
           url=IA + "earlyeuropeanhis00webs", verification_level="full_text", title_page_checked="no", country="US",
           notes="Section heads number the Second, Third and Fourth only. Bibliography: Gibbon 'edited by J. B. "
                 "Bury'."),
    school("sd2-1896-thatcher-schwill", label="Thatcher and Schwill, Europe in the Middle Age",
           author="Oliver J. Thatcher; Ferdinand Schwill", work="Europe in the Middle Age", year_label="1896",
           year_sort="1896", place_publisher="New York: Scribner", tradition="US", enumerates="partial",
           C="4", F="6", scheme_family="modern_eight", signature_match="modern",
           quote="The expedition which is called the fourth crusade (1202-1204) did not proceed against the "
                 "Mohammedans",
           url=IA + "europeinmiddlea01mcnegoog", verification_level="full_text", title_page_checked="no",
           country="US",
           notes="Henry VI's crusade of 1195-97 told unnumbered just before. 'The sixth crusade (1228-1229) was "
                 "remarkable in that, without fighting, it resulted in the acquisition of Jerusalem'."),
    school("sd2-1814-mangnall-questions", label="Richmal Mangnall, Historical and Miscellaneous Questions",
           author="Richmal Mangnall", work="Historical and Miscellaneous Questions, for the Use of Young People",
           year_label="1814 printing (first ed. c. 1800; also read 1857)", year_sort="1814",
           place_publisher="London: Longman", tradition="Britain", enumerates="no", scheme_family="none",
           url=IA + "historicalandmi01manggoog", verification_level="full_text", title_page_checked="no",
           country="GB",
           notes="No crusade numbers in the 1814 or 1857 (historicalandmi03manggoog) text layers."),
    school("sd2-1898-tout-empire-papacy", label="T. F. Tout, The Empire and the Papacy, 918-1273",
           author="T. F. Tout", work="The Empire and the Papacy, 918-1273 (Periods of European History)",
           year_label="1898 (read 1909 printing)", year_sort="1898", place_publisher="London: Rivingtons",
           tradition="Britain", enumerates="yes", C="4", D="5", L1="6", L2="7",
           scheme_family="gibbon_seven", signature_match="no",
           quote="Started in 1217 for what is generally called the Fifth Crusade",
           url=IA + "empirepapacy00toutiala", verification_level="full_text", title_page_checked="no",
           country="GB",
           notes="Chapter XIX summary: 'The Sixth Crusade - St Louis in Egypt ... The Seventh Crusade - Death of St "
                 "Louis at Tunis - Crusade of Edward I.' Frederick II's crusade not numbered in the passages found. "
                 "Gibbon's seven in an Oxford-school textbook of 1898."),
    school("sd2-1894-emerton-mediaeval-europe", label="Ephraim Emerton, Mediaeval Europe (814-1300)",
           author="Ephraim Emerton", work="Mediaeval Europe (814-1300)", year_label="1894", year_sort="1894",
           place_publisher="Boston: Ginn", tradition="US", enumerates="yes", C="4", D="5", F="5", L1="6", L2="6",
           scheme_family="frederick_fifth_seven_variant", signature_match="no",
           quote="The phrase \"fifth crusade\" includes the long series of expeditions and negotiations that went on "
                 "between the years 1217 and 1230",
           url=IA + "mediaevaleurope02emergoog", verification_level="full_text", title_page_checked="no",
           country="US",
           notes="'The result of the fourth Crusade ... ended in the capture of' Constantinople; 'the so-called sixth "
                 "crusade' is Louis IX's two crusades, 1248-1270. Emerton was trained at Leipzig."),
    school("sd2-1894-adams-civilization", label="G. B. Adams, Civilization during the Middle Ages",
           author="George Burton Adams", work="Civilization during the Middle Ages", year_label="1894",
           year_sort="1894", place_publisher="New York: Scribner", tradition="US", enumerates="partial", C="4",
           quote="under the greatest of the popes, Innocent III., the fourth crusade assembled",
           url=IA + "civilizationduri00adam_1", verification_level="full_text", title_page_checked="no",
           country="US", notes="Only the Fourth numbered."),
    school("sd2-1888-ransome-short-history", label="Cyril Ransome, A Short History of England",
           author="Cyril Ransome", work="A Short History of England", year_label="1888", year_sort="1888",
           place_publisher="London: Rivingtons; read New York: E. P. Dutton printing", tradition="Britain",
           enumerates="no", scheme_family="none", url=IA + "shorthistoryofen00rans", verification_level="full_text",
           title_page_checked="no", country="GB",
           notes="'Prince Edward went on a Crusade, and while he was away his father died, in 1272' (unnumbered)."),
    school("sd2-1874-gilman-first-steps", label="Arthur Gilman, First Steps in General History",
           author="Arthur Gilman", work="First Steps in General History", year_label="1874", year_sort="1874",
           place_publisher="New York", tradition="US", enumerates="yes", H6="4", C="4", D="5", F="6", L1="7",
           L2="8", E="8", stated_phrase="the eighth and last Crusade", scheme_family="modern_eight",
           signature_match="modern",
           quote="Fourth Crusade. - After the death of Saladin in 1193 ... the Pope, Celestine III., preached a fourth "
                 "Crusade. He was only able to arouse Henry of Germany",
           url=IA + "firststepsingene00gilm", verification_level="full_text",
           title_page_checked="no (metadata gives the later American Book Company imprint)", country="US",
           notes="The paragraph headed 'Fourth Crusade' runs on from Henry VI's bands to Fulk of Neuilly and the French "
                 "expedition of 1202 (both under one fourth). 'Fifth Crusade' (Andrew II, 1217), 'Sixth Crusade' "
                 "(Frederic II), 'Seventh Crusade' (1248-1254); Edward 'returned to England, and the eighth and last "
                 "Crusade was ended'. Table: 'Fourth Crusade, preached by Foulkes'. Names Proctor, Cox, Hallam, "
                 "Milman, Guizot, Lingard."),
    school("sd2-1910-ontario-ps-history", label="Ontario Public School History of England",
           author="", work="Ontario Public School History of England (authorized)", year_label="1910",
           year_sort="1910", place_publisher="Toronto: Morang Educational Co.", tradition="Canada",
           enumerates="no", scheme_family="none", url=IA + "ontariopublicsch00unse_1",
           verification_level="full_text", title_page_checked="no (metadata: Toronto, Morang, 1910)",
           country="CA", notes="No crusade numbers in the text layer."),
    school("sd2-1844-taylor-manual-us", label="W. C. Taylor, A Manual of Ancient and Modern History (New York)",
           author="W. C. Taylor; American edition by C. S. Henry", work="A Manual of Ancient and Modern History",
           year_label="1844", year_sort="1844", place_publisher="New York: D. Appleton", tradition="US",
           enumerates="partial", C="4", D="5", L1="9",
           stated_phrase="Louis IX., of France, commonly called St. Louis, led the ninth crusade",
           quote="Louis IX., of France, commonly called St. Louis, led the ninth crusade. Egypt was the scene of his "
                 "operations",
           url=IA + "amanualancienta00henrgoog", verification_level="full_text",
           title_page_checked="no (metadata: New York, D. Appleton, 1844)", country="US",
           notes="'The fourth crusade was undertaken at the instigation of Innocent III. (a.d. 1202)'; 'The fifth "
                 "crusade was conducted by the king of Hungary'; then Louis IX's Egyptian expedition 'the ninth "
                 "crusade', with no sixth, seventh or eighth in between. Edward 'led an armament to the Holy Land, in "
                 "aid of the last crusade of St. Louis'. The ninth may come from Louis's regnal number."),
    school("sd2-1858-taylor-students-manual", label="W. C. Taylor, The Student's Manual of Modern History",
           author="W. C. Taylor", work="The Student's Manual of Modern History", year_label="1858 (printing read)",
           year_sort="1858", place_publisher="London: John W. Parker and Son", tradition="Britain",
           enumerates="yes", C="4", D="5", F="6", L1="7", L2="8", scheme_family="modern_eight",
           signature_match="modern",
           quote="1228 The sixth Crusade ... 1250 The seventh Crusade ... The eighth Crusade. Death of St. Louis",
           url=IA + "studentsmanualm00taylgoog", verification_level="full_text",
           title_page_checked="no (metadata: London, John W. Parker and Son, 1858)", country="GB",
           notes="Slots from the chronological table (list outranks the aside); the text keeps the American "
                 "edition's 'Louis IX. of France, commonly called St. Louis, led the ninth crusade' for the Egyptian "
                 "expedition. Text: 'The fourth crusade was undertaken at the instigation of Innocent III. (A.D. "
                 "1202)'; 'The fifth crusade was conducted by the king of Hungary'. Four Indian copies of the 4th ed. "
                 "dated 1847 carry the same sentence."),
    school("sd2-1857-chepmell-short-course", label="H. Le M. Chepmell, A Short Course of History",
           author="Havilland Le Mesurier Chepmell", work="A Short Course of History, First Series",
           year_label="1857 (printing read)", year_sort="1857", place_publisher="London: Whittaker",
           tradition="Britain", enumerates="yes", C="4", D="5", L1="6", L2="7", scheme_family="gibbon_seven",
           signature_match="no",
           stated_phrase="The Crusade of the Germans (or the Fourth Crusade) ... The Seventh (or Ninth) Crusade",
           quote="The Crusade of the Germans (or the Fourth Crusade) 68 The Fourth (or Fifth) Crusade 69 The Fifth "
                 "(or Sixth) Crusade 71 The Crusade of Frederic",
           url=IA + "ashortcoursehis00chepgoog", verification_level="full_text",
           title_page_checked="no (metadata: Chepmell, 1857)", country="GB", channel="Gibbon",
           notes="Two numberings side by side: Gibbon's seven (C 4, D 5, L1 6, L2 7, Frederick II unnumbered) with the "
                 "nine-count in parentheses ('Sixth (or Eighth) Crusade', '1270. The Seventh (or Ninth) Crusade, St. "
                 "Lewis dies at Tunis. 1271. Prince Edward goes to Palestine'). Preface against 'inaccurate educational "
                 "books, unworthy of the country which has produced Gibbon and Hallam'."),
    new("sd2-1862-townsend-manual-dates", label="G. H. Townsend, The Manual of Dates",
        author="George Henry Townsend", work="The Manual of Dates: A Dictionary of Reference",
        year_label="1862", year_sort="1862", place_publisher="London and New York: Routledge, Warne, & Routledge",
        headword="CRUSADES", tradition="Britain", genre="Reference", census_frame="d2_reference_en",
        enumerates="yes", C="5", D="6", B="7", L2="9", E="9", scheme_family="nine_H6", signature_match="no",
        quote="1268. Louis IX. and Edward, prince of Wales, resolve to undertake a ninth Crusade. 1270. Departure of "
              "Louis IX.",
        url=IA + "manualofdatesdic00town", verification_level="full_text",
        title_page_checked="no (metadata: London, Routledge, Warne, & Routledge, 1862)", country="GB",
        notes="CRUSADES: '1199. Innocent III. commissions Fulk of Neuilly to preach the fifth Crusade'; '1216. The "
              "Germans and Hungarians commence the sixth Crusade'; '1239. Thibaud, count of Champagne, commences the "
              "seventh Crusade'; the ninth as quoted, then '1271. April. Prince Edward arrives at Acre'. Other "
              "entries differ: CONSTANTINOPLE 'taken by the Latins, during the fourth crusade' (1203); AIGUES-MORTES "
              "'on the 7th crusade' (1248) and 'on the 8th and last crusade' (1270). 'Edward, prince of Wales' is an "
              "error (the title dates from 1301). Same text in the 1867 Warne printing (bub_gb_LtBCAAAAIAAJ)."),
    new("sd2-1880-johnston-atlas", label="Johnston's Historical Atlas", author="W. & A. K. Johnston",
        work="Johnston's Historical Atlas", year_label="1880", year_sort="1880",
        place_publisher="Edinburgh and London: W. & A. K. Johnston", tradition="Britain", genre="Reference",
        census_frame="d2_reference_en", enumerates="yes", H6="4", C="5", D="6", F="7", L1="8", L2="9", E="9",
        scheme_family="nine_F7", signature_match="no",
        quote="The NINTH CRUSADE (1270-1272) occasioned by the loss of Antioch (1268) was undertaken by the same "
              "monarch",
        url=IA + "johnstonshistor01limigoog", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="'The FOURTH CRUSADE (1195-1197) was organized by the emperor, Henry VI.'; 'During the Fifth Crusade "
              "(1198-1204) Constantinople was twice taken'; the sixth ends at Damietta; 'The SEVENTH CRUSADE "
              "(1227-1229) was undertaken by Frederick II.'; Louis IX 'led the EIGHTH CRUSADE (1248-1254)'. The ninth's "
              "dates include Edward's expedition; the England section has 'Prince Edward went on a crusade (1270)'."),
    school("sd2-1883-swinton-canadian", label="Swinton's Outlines of the World's History, Revised Canadian Edition",
           author="William Swinton", work="Swinton's Outlines of the World's History (Revised Canadian Edition)",
           year_label="1883", year_sort="1883", place_publisher="Halifax, N.S.: A. & W. Mackinlay",
           tradition="Canada", enumerates="yes", H6="4", C="5", D="6", B="7", L1="8", L2="9", E="9",
           stated_phrase="what proved to be the Ninth and last", scheme_family="nine_H6", signature_match="no",
           stemma_parent="1877-eb9-crusades",
           parent_evidence="documented: 'It was an enterprise set on foot by the Knights of St. John' (EB9: 'an "
                           "enterprise set on foot by the knights of St John'), ten consecutive words",
           quote="Fourth Crusade.-This Crusade may be dismissed in a few words. It was an enterprise set on foot by "
                 "the Knights of St. John",
           url=IA + "cihm_13979", verification_level="full_text",
           title_page_checked="yes (OCR: Rebised Canadian Edition ... PRESCRIBED BY THE COUNCIL OF PUBLIC "
                              "INSTRUCTION ... HALIFAX, N.S.: A. & W. MACKINLAY ... 1883)",
           country="CA", channel="EB9",
           notes="'Fifth Crusade.-The chiefs of this Crusade embraced none of the crowned heads'; 'Egypt was the scene "
                 "of the Sixth Crusade (A.D. 1216-1220)'; 'Seventh Crusade.-This expedition, undertaken in A.D. 1238 "
                 "by the French under the King of Navarre and by the English'; 'Eighth Crusade' (Louis IX); 'Twenty-one "
                 "years afterwards (A.D. 1270) Saint Louis undertook what proved to be the Ninth and last', Edward "
                 "inside it. The 1874 US text (1874-william-swinton) has Procter's eight; whether the US text was also "
                 "revised is not checked."),
    new("sd2-1884-boyce-introduction", label="W. B. Boyce, Introduction to the Study of History",
        author="William Binnington Boyce", work="Introduction to the Study of History: Civil, Ecclesiastical, and "
                                                "Literary",
        year_label="1884", year_sort="1884", place_publisher="London: T. Woolmer", tradition="Britain",
        genre="School", census_frame="d2_school_en", enumerates="yes", H6="4", C="5", D="6", F="6", B="7",
        L1="8", L2="9", E="9", scheme_family="nine_H6", signature_match="no",
        quote="The Fourth Crusade, 1197 A.D., consisted of bands sent out by the Emperor Henry VI ... The Fifth "
              "Crusade, 1202-4",
        url=IA + "introductiontost00boycuoft", verification_level="full_text",
        title_page_checked="yes (OCR: BY W. B. BOYCE. LON[DON]; metadata T. Woolmer 1884)", country="GB",
        channel="Cox",
        notes="'The Sixth Crusade was undertaken by Andrew II., of Hungary, 1216 A.D., and by Frederick II.'; 'The "
              "Seventh Crusade, by Richard, Earl of Cornwall, and some French nobles'; Louis IX's Egyptian expedition "
              "the Eighth; 'The Ninth Crusade. St. Louis IX. besieged Tunis ... Prince Edward ... 1271 A.D., took "
              "Nazareth'. Reading list includes Cox's Crusades (Epochs). Boyce, a Wesleyan missionary, writes "
              "against Gibbon's 'libels' on Byzantium."),
    new("sd2-1897-desmond-mooted", label="H. J. Desmond, Mooted Questions of History",
        author="Humphrey J. Desmond", work="Mooted Questions of History", year_label="1902 (printing read)",
        year_sort="1902", place_publisher="Boston: Marlier", tradition="US", genre="Popular history",
        census_frame="d2_popular_en", enumerates="partial", F="6", L2="9",
        stated_phrase="The last or ninth Crusade went out, A.D. 1270, under St. Louis",
        quote="The last or ninth Crusade went out, A.D. 1270, under St. Louis, King of France",
        url=IA + "mootedquestions00desmgoog", verification_level="full_text", title_page_checked="no",
        country="US",
        notes="Catholic apologetic essays. 'Jerusalem again came into the possession of the Christians by treaty in "
              "1229 (as a result of the sixth Crusade)'. Names Cox twice."),
    new("sd2-1882-universal-self-instructor", label="A. E. Berg (ed.), The Universal Self-Instructor",
        author="Albert Ellery Berg (ed.)", work="The Universal Self-Instructor and Manual of General Reference",
        year_label="1882 (read Melbourne 1883 printing)", year_sort="1882",
        place_publisher="New York (1882); read Melbourne: Samuel McCardel", tradition="US", genre="Reference",
        census_frame="d2_reference_en", enumerates="yes", C="4", D="5", F="6", B="7", L1="8", L2="9", E="9",
        scheme_family="nine_B7", signature_match="no", stemma_parent="sd2-1862-townsend-manual-dates",
        parent_evidence="documented: shared error 'Edward, Prince of Wales'; 'Germans and Hungarians'; numbering "
                        "shifted",
        quote="Fifth Crusade, by Germans and Hungarians ... Sixth Crusade; Frederick II. at Acre ... Seventh Crusade, "
              "by Thibaud, Count of Champagne ... Eighth Crusade, under Louis IX. of France ... Ninth Crusade, by "
              "Louis IX. and Edward, Prince of Wales",
        url=IA + "universalselfins00berg", verification_level="full_text",
        title_page_checked="no (metadata: Melbourne, Samuel McCardel, Australian Publishing Co., 1883)",
        country="US",
        notes="Chronology of the thirteenth century: '1203 Fourth Crusade; capture of Zara'. The New York printing "
              "(dli.bengal.10689.15459, 1882) has the same entry in the full-text search."),
    new("sd2-1891-gays-circle", label="Gay's Illustrated Circle of Knowledge", author="",
        work="Gay's Illustrated Circle of Knowledge", year_label="1891", year_sort="1891",
        place_publisher="New York: Gay Brothers", tradition="US", genre="Reference",
        census_frame="d2_reference_en", enumerates="yes", C="4", D="5", F="6", B="7", L1="8", L2="9", E="9",
        scheme_family="nine_B7", signature_match="no", stemma_parent="sd2-1882-universal-self-instructor",
        parent_evidence="documented: same entries and the same error ('prince of Wales')",
        quote="1202- Fourth crusade ... 17- Fifth crusade by Hungarians and Germans ... 28- Sixth crusade ... 39- "
              "Seventh crusade ... 48- Eighth crusade under LOUIS IX ... 68- Ninth crusade by LOUIS IX. and prince "
              "of Wales",
        url=IA + "gaysillustratedc00unse", verification_level="full_text", title_page_checked="no", country="US"),
    new("sd2-1892-atlas-chronology", label="Chronology in The Home Knowledge Atlas and the Ogle Standard Atlases",
        author="", work="'History of the World' chronology in The Home Knowledge Atlas (1892) and Geo. A. Ogle & "
                        "Co.'s Standard Atlases of US counties (1896-1936)",
        year_label="1892-1936", year_sort="1892", place_publisher="Chicago and elsewhere", tradition="US",
        genre="Reference", census_frame="d2_reference_en", enumerates="partial", L2="9", E="9",
        stated_phrase="1268 Ninth Crusade, by Louis IX. and Edward, Prince of Wales",
        quote="Sicily conquered by Charles of Anjou. 1268 Ninth Crusade, by Louis IX. and Edward, Prince of Wales",
        url=IA + "homeknowledgeatl02home", verification_level="snippet", title_page_checked="no", country="US",
        stemma_parent="sd2-1882-universal-self-instructor",
        parent_evidence="documented: same sequence and error",
        notes="Archive.org full-text search, 'ninth crusade': about 40 county atlases of Michigan, Indiana, Iowa, "
              "Kansas and Minnesota, 1896-1936, print the same chronology. They account for most 'ninth crusade' "
              "items of the 1900s and 1910s."),
    new("sd2-1904-harbottle-battles", label="T. B. Harbottle, Dictionary of Battles",
        author="Thomas Benfield Harbottle", work="Dictionary of Battles from the Earliest Date to the Present Time",
        year_label="1904", year_sort="1904", place_publisher="London: Swan Sonnenschein", tradition="Britain",
        genre="Reference", census_frame="d2_reference_en", enumerates="partial", L1="5", L2="9",
        scheme_family="other", signature_match="no",
        quote="Tunis (Ninth Crusade). This city was besieged by the French Crusaders, under Louis IX in 1270",
        url=IA + "dictionarybattl00harbgoog", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="'Mensourah (Fifth Crusade). Fought 1249, between the French, under Louis IX, and the Moslems.' The two "
              "entries come from different counts."),
    new("sd2-1894-smith-historical-geography", label="G. A. Smith, The Historical Geography of the Holy Land",
        author="George Adam Smith", work="The Historical Geography of the Holy Land",
        year_label="1894 (read 1897)", year_sort="1894", place_publisher="London: Hodder and Stoughton",
        tradition="Britain", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial",
        D="6", L2="8", scheme_family="moreri_eight", signature_match="no",
        quote="Andrew in 1217, the Sixth Crusade; Louis in 1270, the Eighth Crusade",
        url=IA + "historicalgeogra1897smit", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="Footnote as quoted. The text has 'in the Ninth Crusade, when an expedition of Louis of France conquered "
              "all the Jordan Valley' (Louis's Palestine years, after 1250): a different count. Reading list: "
              "'Gibbon; Cox's little manual in the Epochs of History; Sybel', Röhricht, Prutz. Reprinted to the "
              "1930s."),
    school("sd2-1883-lupton-concise", label="W. M. Lupton, A Concise English History", author="W. M. Lupton",
           work="A Concise English History", year_label="1883", year_sort="1883",
           place_publisher="London: Longmans, Green", tradition="Britain", enumerates="partial", L2="9", E="9",
           stated_phrase="set out for the Ninth Crusade",
           quote="Prince Edward ... set out for the Ninth Crusade, accompanied by his wife Eleanor and a large "
                 "retinue, July 1270. Louis IX., who had preceded Edward, died at Tunis",
           url=IA + "aconciseenglish00luptgoog", verification_level="full_text", title_page_checked="no",
           country="GB",
           notes="Index: 'Louis IX ... Joins the Ninth Crusade and dies at Tunis'. In this English history the ninth "
                 "is Edward's crusade, which Louis joins."),
    new("sd2-1887-cox-concise-england", label="G. W. Cox, A Concise History of England",
        author="George W. Cox", work="A Concise History of England and the English People", year_label="1887",
        year_sort="1887", place_publisher="London: J. Hughes", tradition="Britain", genre="School",
        census_frame="d2_school_en", enumerates="partial", E="9",
        quote="had only reached Capua on his return from the ninth crusade",
        url=IA + "aconcisehistory00coxgoog", verification_level="full_text", title_page_checked="no",
        country="GB", stemma_parent="1874-george-w-cox", parent_evidence="documented: same author",
        notes="Edward I's accession: 'he was far away, and had only reached Capua on his return from the ninth "
              "crusade'. Cox's own count (1874) puts Tunis and Edward in one ninth."),
    new("sd2-1920-parry-pilgrim", label="O. H. Parry, The Pilgrim in Jerusalem", author="Oswald Hutton Parry",
        work="The Pilgrim in Jerusalem", year_label="1920", year_sort="1920",
        place_publisher="London: SPCK; New York: Macmillan", tradition="Britain", genre="Popular history",
        census_frame="d2_popular_en", enumerates="partial", L1="8", E="9",
        quote="1248-1254. Eighth Crusade: S. Louis. ... 1270-1272. Ninth Crusade: Edward I of England",
        url=IA + "pilgriminjerusal0000parr", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="Chronology of Jerusalem. Tunis is not mentioned: the ninth, dated 1270-1272, is Edward's. Earliest "
              "Edward-alone ninth found in a reference list."),
    new("sd2-1935-outhwaite-unrolling", label="Leonard Outhwaite, Unrolling the Map", author="Leonard Outhwaite",
        work="Unrolling the Map: The Story of Exploration", year_label="1935", year_sort="1935",
        place_publisher="New York: Reynal & Hitchcock", tradition="US", genre="Popular history",
        census_frame="d2_popular_en", enumerates="partial", E="9",
        quote="Prince Edward of England at the end of the Ninth Crusade finally gave up and sailed home",
        url=IA + "unrollingmapstor0000leon", verification_level="snippet", title_page_checked="no", country="US",
        notes="Full-text search highlight; four copies (1935-38)."),
    dict(work_id="sd-1831-russell-palestine", checked_on=D,
         notes=app("sd-1831-russell-palestine", "notes",
                   "[D2 2026-11-28] Contents line in ten copies, 1831-37 (Edinburgh Cabinet Library and the New York "
                   "Harper printings): 'takes Damietta - His Losses and Return to Europe - Ninth Crusade - Louis IX. "
                   "and Edward I. - Death of Louis'.", W)),
    dict(work_id="sd2-1831-americana-chron-table",
         notes=app("sd2-1831-americana-chron-table", "notes",
                   "Same table, 'Ninth crusade (Thibaut)', in the 1835, 1838 and 1851 Americana printings "
                   "(b2933164x_0006; encyclopdiaamer12bradgoog; encyclopdiaamer06unkngoog) and in Jenks's Supplement "
                   "to the Comprehensive Commentary (1860; supplementtocomp0000jenk). A Chicago Daily Tribune item of "
                   "30 April 1907 repeats it: 'The rose was unknown in Europe prior to the ninth crusade, but was "
                   "brought back by Thibaut'.", cur())),
]
L.upsert_works(works)

W = cur()


def attr(wid, **kw):
    kw["work_id"] = wid
    kw.setdefault("checked_on", D)
    if wid in W and "gibbon_numbers" not in kw:
        kw["gibbon_numbers"] = L.gibbon_numbers(W[wid])
    return kw


A = [
    attr("sd2-1801-tytler-elements", frame_id="S01", country_pub="Scotland", author_origin="Scotland",
         fourth_identity="C", fifth_identity="D", edward_status="absent", gibbon_cited="none",
         numbers_follow="gibbon;inferred", notes="Read in a New York printing; the table's fifth is 1248."),
    attr("sd2-1830-keightley-outlines", frame_id="S04", country_pub="England", author_origin="Ireland",
         fourth_identity="C", fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="gibbon;inferred"),
    attr("sd2-1864-yonge-landmarks", frame_id="S06", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="last_unnumbered", gibbon_cited="none",
         numbers_follow="modern;inferred"),
    attr("sd2-1872-freeman-sketch", frame_id="S07", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred"),
    attr("sd2-1858-white-eighteen-centuries", frame_id="S11", country_pub="Scotland", author_origin="Scotland",
         fourth_identity="C", fifth_identity="D", edward_status="absent", gibbon_cited="none",
         sources_named="Michelet", numbers_follow="modern;inferred", notes="Read in a Philadelphia printing."),
    attr("sd2-1853-goodrich-all-nations", frame_id="S15", country_pub="US", author_origin="US",
         fourth_identity="C", fifth_identity="D", edward_status="absent", gibbon_cited="none",
         numbers_follow="gibbon;inferred", notes="Reports a count of ten (r34)."),
    attr("sd2-1854-willson-outlines", frame_id="S16", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="D", edward_status="last_unnumbered", gibbon_cited="footnote", gibbon_edition="unspecified",
         sources_named="Gibbon", numbers_follow="gibbon;inferred",
         notes="Echoes G. P. R. James's sentence on the expedition of 1202-04, renumbered."),
    attr("sd2-1843-worcester-elements", frame_id="S17", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="none", edward_status="absent", gibbon_cited="none", sources_named="Hallam;Robertson",
         numbers_follow="unclear;inferred"),
    attr("sd2-1842-fredet-modern-history", frame_id="S21", country_pub="US", author_origin="France",
         fourth_identity="H6", fifth_identity="C", edward_status="inside_last", gibbon_cited="none",
         sources_named="Voltaire;Maimbourg;Lingard", numbers_follow="moreri;inferred",
         notes="French Sulpician in Baltimore; the French reference count in a US Catholic text."),
    attr("sd2-1870-anderson-manual", frame_id="S27", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="F", edward_status="inside_last", gibbon_cited="none", numbers_follow="german;inferred",
         notes="Frederick-fifth seven; possible channel Chambers's Encyclopaedia (1868), not documented."),
    attr("sd2-1915-west-modern-world", frame_id="S29", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="other", gibbon_cited="none", sources_named="Pears;Lane-Poole;Archer;Cox;Munro;Duruy",
         numbers_follow="modern;inferred"),
    attr("sd2-1903-robinson-western-europe", frame_id="S30", country_pub="US", author_origin="US",
         fourth_identity="none", fifth_identity="none", gibbon_cited="none", sources_named="Munro;Archer",
         numbers_follow="unclear;inferred", notes="Avoids numbers."),
    attr("sd2-1920-breasted-robinson", frame_id="S31", country_pub="US", author_origin="US",
         fourth_identity="none", fifth_identity="none", gibbon_cited="bibliography", gibbon_edition="unspecified",
         sources_named="Archer;Gibbon;Munro", numbers_follow="unclear;inferred"),
    attr("sd2-1917-webster-early-european", frame_id="S32", country_pub="US", author_origin="US",
         fourth_identity="C", fifth_identity="none", gibbon_cited="bibliography", gibbon_edition="Bury",
         sources_named="Gibbon;Archer", numbers_follow="modern;inferred"),
    attr("sd2-1896-thatcher-schwill", frame_id="S33", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="none", gibbon_cited="none",
         sources_named="Milman;Kugler;Sybel;Pears;Stubbs;Lane-Poole;Archer;Cox;Munro;Mombert",
         numbers_follow="modern;inferred", notes="'which is called the fourth crusade' (r37)."),
    attr("sd2-1814-mangnall-questions", frame_id="S03", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
    attr("sd2-1898-tout-empire-papacy", frame_id="S10", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Riant", numbers_follow="gibbon;inferred",
         notes="Gibbon's seven; 'what is generally called the Fifth Crusade' (r38)."),
    attr("sd2-1894-emerton-mediaeval-europe", frame_id="H18", country_pub="US", author_origin="US",
         fourth_identity="C", fifth_identity="D+F", gibbon_cited="none",
         sources_named="Heeren;Guizot;Kugler;Sybel;Prutz;Pears;Archer;Cox;Michelet",
         numbers_follow="german;inferred", notes="'The phrase \"fifth crusade\" includes ...' (r36)."),
    attr("sd2-1894-adams-civilization", frame_id="H19", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="none", gibbon_cited="none", sources_named="Kugler;Pears;Archer;Cox",
         numbers_follow="unclear;inferred"),
    attr("sd2-1888-ransome-short-history", frame_id="S40", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Stubbs", numbers_follow="unclear;inferred", notes="Added during reading (school, England)."),
    attr("sd2-1874-gilman-first-steps", frame_id="S38", country_pub="US", author_origin="US", fourth_identity="both",
         fifth_identity="D", edward_status="inside_last", gibbon_cited="bibliography", gibbon_edition="unspecified",
         sources_named="Gibbon;Hallam;Proctor;Cox;Milman;Guizot;Lingard", numbers_follow="modern;inferred",
         notes="Added during reading. Henry VI's bands and the 1202 expedition under one fourth."),
    attr("sd2-1910-ontario-ps-history", frame_id="S34", country_pub="Canada", fourth_identity="none",
         fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
    attr("sd2-1844-taylor-manual-us", frame_id="S36", country_pub="US", author_origin="Ireland", fourth_identity="C",
         fifth_identity="D", edward_status="last_unnumbered", ninth_referent="other", gibbon_cited="none",
         numbers_follow="unclear;inferred",
         notes="Added during reading. Ninth = Louis IX's Egyptian crusade (1248)."),
    attr("sd2-1858-taylor-students-manual", frame_id="S36", country_pub="England", author_origin="Ireland",
         fourth_identity="C", fifth_identity="D", ninth_referent="other", gibbon_cited="none",
         numbers_follow="modern;inferred",
         notes="Added during reading. Table modern eight; text keeps 'led the ninth crusade'."),
    attr("sd2-1857-chepmell-short-course", frame_id="S37", country_pub="England", author_origin="Guernsey",
         fourth_identity="both", fifth_identity="D", edward_status="named_unnumbered", ninth_referent="tunis",
         gibbon_cited="preface", gibbon_edition="unspecified", sources_named="Gibbon;Hallam;Sismondi;Milman",
         numbers_follow="gibbon;documented",
         notes="Added during reading. Gibbon's seven with the nine in parentheses (r35); 'fourth' names both, one "
               "in each count."),
    attr("sd2-1862-townsend-manual-dates", frame_id="R14", country_pub="England", author_origin="England",
         fourth_identity="both", fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="none", numbers_follow="michaud_mills;inferred",
         notes="CRUSADES entry nine_H6; CONSTANTINOPLE entry C 4. Source of the 'Prince of Wales' error."),
    attr("sd2-1880-johnston-atlas", frame_id="R37", country_pub="Scotland", fourth_identity="H6", fifth_identity="C",
         edward_status="ninth_with_tunis", ninth_referent="tunis+edward", gibbon_cited="none",
         numbers_follow="unclear;inferred", notes="Added during reading. nine_F7 as Rees 1808 and Mary Milner 1847."),
    attr("sd2-1883-swinton-canadian", frame_id="S34", country_pub="Canada", author_origin="Scotland",
         fourth_identity="H6", fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="none", sources_named="Hallam;Hume", numbers_follow="michaud_mills;documented",
         notes="Copies EB9 on the Fourth; the 1874 US text followed Procter."),
    attr("sd2-1884-boyce-introduction", frame_id="S39", country_pub="England", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="named_in_text", gibbon_edition="unspecified",
         sources_named="Cox;Stubbs;Freeman;Hallam;Gibbon;Michaud;Mosheim;Sismondi",
         numbers_follow="michaud_mills;documented", notes="Added during reading. Lists Cox's Crusades."),
    attr("sd2-1897-desmond-mooted", frame_id="P33", country_pub="US", author_origin="US", fourth_identity="none",
         fifth_identity="none", ninth_referent="tunis", gibbon_cited="none",
         sources_named="Michaud;Hallam;Stubbs;Cox;Lingard;Duruy", numbers_follow="michaud_mills;inferred",
         notes="Added during reading."),
    attr("sd2-1882-universal-self-instructor", frame_id="R38", country_pub="US", fourth_identity="C",
         fifth_identity="D", edward_status="ninth_with_tunis", ninth_referent="tunis+edward", gibbon_cited="none",
         numbers_follow="own;documented",
         notes="Added during reading. Townsend's entries with the Fourth moved to 1202-04 and Frederick given a "
               "number: nine_B7."),
    attr("sd2-1891-gays-circle", frame_id="R38", country_pub="US", fourth_identity="C", fifth_identity="D",
         edward_status="ninth_with_tunis", ninth_referent="tunis+edward", gibbon_cited="none",
         numbers_follow="own;documented", notes="Added during reading. Copies the Self-Instructor."),
    attr("sd2-1892-atlas-chronology", frame_id="R38", country_pub="US", edward_status="ninth_with_tunis",
         ninth_referent="tunis+edward", gibbon_cited="unchecked", numbers_follow="own;documented",
         notes="Added during reading. Snippet level; one row for the series."),
    attr("sd2-1904-harbottle-battles", frame_id="R39", country_pub="England", fourth_identity="none",
         fifth_identity="other", ninth_referent="tunis", gibbon_cited="none", numbers_follow="unclear;inferred",
         notes="Added during reading. Fifth = Mansurah 1249."),
    attr("sd2-1894-smith-historical-geography", frame_id="H23", country_pub="England", author_origin="Scotland",
         fourth_identity="none", fifth_identity="none", ninth_referent="other", gibbon_cited="bibliography",
         gibbon_edition="unspecified", sources_named="Gibbon;Cox;Sybel;Röhricht;Prutz",
         numbers_follow="unclear;inferred", notes="Added during reading. Footnote and text use different counts."),
    attr("sd2-1883-lupton-concise", frame_id="S40", country_pub="England", fourth_identity="none",
         fifth_identity="none", edward_status="ninth_with_tunis", ninth_referent="tunis+edward", gibbon_cited="none",
         numbers_follow="unclear;inferred", notes="Added during reading. The ninth told as Edward's, Louis joining."),
    attr("sd2-1887-cox-concise-england", frame_id="S40", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="ninth_with_tunis", ninth_referent="edward",
         gibbon_cited="none", numbers_follow="own;documented",
         notes="Added during reading. The passage names only Edward."),
    attr("sd2-1920-parry-pilgrim", frame_id="P33", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="ninth_alone", ninth_referent="edward",
         gibbon_cited="none", numbers_follow="unclear;inferred", notes="Added during reading."),
    attr("sd2-1935-outhwaite-unrolling", frame_id="P33", country_pub="US", edward_status="ninth_alone",
         ninth_referent="edward", gibbon_cited="unchecked", numbers_follow="unclear;inferred",
         notes="Added during reading; snippet level. Edward's expedition 'at the end of the Ninth Crusade'."),
    attr("sd-1831-russell-palestine", frame_id="P28", country_pub="Scotland", author_origin="Scotland",
         edward_status="ninth_with_tunis", ninth_referent="tunis+edward", gibbon_cited="unchecked",
         numbers_follow="unclear;inferred"),
]
L.upsert_attrs(A)

C = [
    ("sd2-1883-swinton-canadian", "1877-eb9-crusades", "copies wording on the Fourth",
     "'an enterprise set on foot by the Knights of St. John' (EB9: 'an enterprise set on foot by the knights of St "
     "John')", "documented"),
    ("sd2-1884-boyce-introduction", "1874-george-w-cox", "lists in reading list", "'... the Crusades, small "
                                                                                    "(Longman & Co.)'", "documented"),
    ("sd2-1882-universal-self-instructor", "sd2-1862-townsend-manual-dates", "shares error and wording",
     "'Edward, Prince of Wales' with the ninth; 'Germans and Hungarians'", "documented"),
    ("sd2-1891-gays-circle", "sd2-1882-universal-self-instructor", "copies entries", "Same entries and error",
     "documented"),
    ("sd2-1892-atlas-chronology", "sd2-1882-universal-self-instructor", "copies entries",
     "'Barons' War ... Ninth Crusade, by Louis IX. and Edward, Prince of Wales'", "documented"),
    ("sd2-1854-willson-outlines", "sd2-1830-james-chivalry", "echoes sentence, renumbered",
     "'The fourth crusade ended without producing any benefit to Palestine' / 'THE fifth crusade had ended, as we have "
     "seen, without producing any other benefit to Palestine'", "inferred"),
    ("sd2-1854-willson-outlines", "Gibbon", "cites in footnotes", "'Gibbon, iv. 116-133'", "documented"),
    ("sd2-1857-chepmell-short-course", "Gibbon", "names in preface", "'the country which has produced Gibbon and "
                                                                     "Hallam'", "documented"),
    ("sd2-1894-smith-historical-geography", "Gibbon", "lists in reading list", "'On the Crusades generally, cf. "
                                                                              "Gibbon'", "documented"),
    ("sd2-1894-smith-historical-geography", "1874-george-w-cox", "lists in reading list",
     "'Cox's little manual in the Epochs of History'", "documented"),
    ("sd2-1897-desmond-mooted", "Cox", "names", "2 mentions in the text layer", "documented"),
    ("sd2-1917-webster-early-european", "Gibbon", "lists in bibliography", "'edited by J. B. Bury'", "documented"),
    ("sd2-1920-breasted-robinson", "Gibbon", "lists in additional reading", "'chaps. lviii-lix'", "documented"),
    ("sd2-1874-gilman-first-steps", "Proctor", "names", "1 mention in the text layer", "documented"),
    ("sd2-1887-cox-concise-england", "1874-george-w-cox", "same author", "Cox's own count", "documented"),
]
L.append_citations([dict(citing_work_id=a, cited=b, relation=c, evidence=d, confidence=e) for a, b, c, d, e in C])

R = [
    dict(reason_id="r34", year="1853", work="A History of All Nations", author="Samuel G. Goodrich", language="en",
         entry_id="sd2-1853-goodrich-all-nations", kind="alternative_reckoning", target="count of ten",
         expeditions_affected="all",
         phrase="Some writers make ten, namely, in 1096, 1110, '50, '90, '95, 1909, '17, '98, '40, '48.",
         verification="full_text", source="archive.org ahistoryallnati00goodgoog",
         notes="OCR; the dates read 1096, 1101?, 1147, 1189, 1195, 1202, 1217, 1228, 1240, 1248. Goodrich's own count "
               "is Gibbon's seven. Compare the Americana chronological table (sd2-1831-americana-chron-table)."),
    dict(reason_id="r35", year="1857", work="A Short Course of History", author="H. Le M. Chepmell", language="en",
         entry_id="sd2-1857-chepmell-short-course", kind="alternative_reckoning", target="scheme",
         expeditions_affected="H6;C;D;L1;L2",
         phrase="The Crusade of the Germans (or the Fourth Crusade) ... The Fourth (or Fifth) Crusade ... The Fifth "
                "(or Sixth) Crusade ... The Seventh (or Ninth) Crusade",
         verification="full_text", source="archive.org ashortcoursehis00chepgoog",
         notes="Gibbon's seven with the nine-count in parentheses."),
    dict(reason_id="r36", year="1894", work="Mediaeval Europe (814-1300)", author="Ephraim Emerton", language="en",
         entry_id="sd2-1894-emerton-mediaeval-europe", kind="inclusion_note", target="fifth",
         expeditions_affected="D;F",
         phrase="The phrase \"fifth crusade\" includes the long series of expeditions and negotiations that went on "
                "between the years 1217 and 1230.",
         verification="full_text", source="archive.org mediaevaleurope02emergoog",
         notes="Also 'the so-called sixth crusade' for Louis IX's two crusades."),
    dict(reason_id="r37", year="1896", work="Europe in the Middle Age", author="O. J. Thatcher and F. Schwill",
         language="en", entry_id="sd2-1896-thatcher-schwill", kind="statement_of_custom", target="fourth",
         expeditions_affected="C",
         phrase="The expedition which is called the fourth crusade (1202-1204) did not proceed against the "
                "Mohammedans",
         verification="full_text", source="archive.org europeinmiddlea01mcnegoog",
         notes="Follows an unnumbered account of Henry VI's crusade."),
    dict(reason_id="r38", year="1898", work="The Empire and the Papacy, 918-1273", author="T. F. Tout",
         language="en", entry_id="sd2-1898-tout-empire-papacy", kind="statement_of_custom", target="fifth",
         expeditions_affected="D", phrase="Started in 1217 for what is generally called the Fifth Crusade.",
         verification="full_text", source="archive.org empirepapacy00toutiala (1909 printing)", notes=""),
]
L.append_reasons(R)

B = "archive.org metadata and djvu text (browser)"
FTS = "archive.org full-text search (browser)"
LOG = [
    (B, "School texts batch: Tytler (3 printings), Keightley Outlines, Yonge, Freeman, White, Dickens vol. 1, "
        "Goodrich (2 titles), Willson, Worcester, Fredet, Anderson, West, Robinson, Breasted and Robinson, Webster, "
        "Thatcher and Schwill, Pinnock, Mangnall (2), Tout, Emerton, G. B. Adams, Ransome, Gilman, Ontario Public "
        "School History, Creighton primer, Toronto topical notes, Robertson vol. 6, Blyth", "1814-1920",
     "32 items", "32",
     "29 rows (see works.csv, census_frame d2_school_en); not usable: Dickens vol. 1 (ends before Edward), Pinnock "
     "(undated copy; 'the last crusade' = 1248), Creighton primer and Toronto notes (no crusades), Robertson vol. 6 "
     "(wrong volume)"),
    (FTS, "\"fourth crusade\" by decade, first 200 hits classified by context (Henry VI/Celestine vs "
          "Constantinople/Zara)", "1800-1949 by decade", "1800-2373 per decade", "2,767",
     "data/usage/archiveorg_d2_fourth_referent_by_decade.csv"),
    (FTS, "\"ninth crusade\", \"fifth crusade\", \"eighth crusade\" AND Edward by decade, hits classified by context",
     "1800-1949 by decade", "1-726 per decade", "about 2,600",
     "data/usage/archiveorg_d2_referents_by_decade.csv; sd2-1862-townsend-manual-dates; "
     "sd2-1882-universal-self-instructor; sd2-1892-atlas-chronology; sd2-1883-lupton-concise; "
     "sd2-1887-cox-concise-england; sd2-1920-parry-pilgrim; sd2-1935-outhwaite-unrolling"),
    (FTS, "\"ninth crusade\", \"fourth crusade\", \"sixth crusade\", \"eight crusades\", \"seven crusades\", \"nine "
          "crusades\", \"eighth crusade\" AND Edward: item counts by decade", "1800-1949 by decade", "see table",
     "0", "data/usage/archiveorg_d2_phrases_by_decade.csv; the AND-with-OR queries for the Fourth and Fifth returned "
          "0 in every decade (syntax not supported)"),
    (B, "Works found by the ninth sweep: W. C. Taylor (London 1858, New York 1844), Chepmell, Townsend 1862, "
        "Johnston's Historical Atlas, Swinton (Halifax 1883), Boyce, Desmond, Gay's, Harbottle, G. A. Smith, G. W. "
        "Cox's Concise History, Lupton, Universal Self-Instructor, O. H. Parry, two 'New Columbia Encyclopedia' "
        "copies", "1844-1935", "17 items", "17",
     "15 rows; excluded: in.ernet.dli.2015.147441 and .121022, dated 1935 by DLI but The New Columbia "
     "Encyclopedia of 1975 (Library of Congress CIP data on the verso)"),
]
L.append_log(D, LOG)

L.set_frame_status({
    "S01": ("read", "sd2-1801-tytler-elements", "D2: New York 1819, 1837, Nares 1839 printings"),
    "S02": ("partial", "", "D2: Pinnock's Catechism of Modern History read (undated copy): 'the last crusade' = "
                          "Louis IX 1248; Pinnock's Goldsmith not reached"),
    "S03": ("read", "sd2-1814-mangnall-questions", "D2: 1814 and 1857"),
    "S04": ("read", "sd2-1830-keightley-outlines", ""),
    "S06": ("read", "sd2-1864-yonge-landmarks", ""),
    "S07": ("read", "sd2-1872-freeman-sketch", ""),
    "S10": ("read", "sd2-1898-tout-empire-papacy", "D2: The Empire and the Papacy; Edward the First not reached"),
    "S11": ("read", "sd2-1858-white-eighteen-centuries", "D2: Philadelphia 1859 printing"),
    "S15": ("read", "sd2-1853-goodrich-all-nations", "D2: History of All Nations 1853; Peter Parley's Universal "
                                                     "History 1874 ed. has only 'Last crusade begun 1248'"),
    "S16": ("read", "sd2-1854-willson-outlines", ""),
    "S17": ("read", "sd2-1843-worcester-elements", ""),
    "S21": ("read", "sd2-1842-fredet-modern-history", ""),
    "S27": ("read", "sd2-1870-anderson-manual", ""),
    "S29": ("read", "sd2-1915-west-modern-world", ""),
    "S30": ("read", "sd2-1903-robinson-western-europe", ""),
    "S31": ("read", "sd2-1920-breasted-robinson", ""),
    "S32": ("read", "sd2-1917-webster-early-european", ""),
    "S33": ("read", "sd2-1896-thatcher-schwill", ""),
    "S34": ("partial", "sd2-1883-swinton-canadian;sd2-1910-ontario-ps-history",
            "D2: Halifax 1883 Swinton and Toronto 1910 read; Creighton primer and Toronto topical notes have no "
            "crusades"),
    "S35": ("not_reached", "", "D2: only vol. 1 (to Henry III's reign) had a text layer"),
    "R14": ("read", "sd2-1862-townsend-manual-dates", "D2: 1862 and 1867"),
    "R33": ("not_reached", "", "D2: the two DLI copies dated 1935 are The New Columbia Encyclopedia (1975)"),
    "H18": ("read", "sd2-1894-emerton-mediaeval-europe", ""),
    "H19": ("read", "sd2-1894-adams-civilization", ""),
    "C06": ("not_reached", "", "D2: vols. 5 and 6 read were the wrong volumes"),
    "C02": ("not_reached", "", "D2: vol. 17 read was the wrong volume"),
    "P28": ("read", "", "D2: ten copies 1831-37 in the full-text search"),
})
L.add_frame_rows([
    dict(frame_id="S36", frame="d2_school_en", country="England", genre="School", author="W. C. Taylor",
         title="The Student's Manual of Modern History; A Manual of Ancient and Modern History (New York)",
         editions_targeted="1844 New York; 1847; 1858", existing_work_ids="sd2-1844-taylor-manual-us;"
                                                                         "sd2-1858-taylor-students-manual",
         status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="S37", frame="d2_school_en", country="England", genre="School", author="H. Le M. Chepmell",
         title="A Short Course of History", editions_targeted="1857", existing_work_ids="sd2-1857-chepmell-short-course",
         status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="S38", frame="d2_school_en", country="US", genre="School", author="Arthur Gilman",
         title="First Steps in General History", editions_targeted="1874", existing_work_ids="sd2-1874-gilman-first-steps",
         status="read", notes="added_during_reading"),
    dict(frame_id="S39", frame="d2_school_en", country="England", genre="School", author="W. B. Boyce",
         title="Introduction to the Study of History", editions_targeted="1884",
         existing_work_ids="sd2-1884-boyce-introduction", status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="S40", frame="d2_school_en", country="England", genre="School",
         author="W. M. Lupton; G. W. Cox; Cyril Ransome", title="Concise histories of England",
         editions_targeted="1883; 1887; 1888",
         existing_work_ids="sd2-1883-lupton-concise;sd2-1887-cox-concise-england;sd2-1888-ransome-short-history",
         status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="R37", frame="d2_reference_en", country="Scotland", genre="Reference",
         author="W. & A. K. Johnston", title="Johnston's Historical Atlas", editions_targeted="1880",
         existing_work_ids="sd2-1880-johnston-atlas", status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="R38", frame="d2_reference_en", country="US", genre="Reference",
         author="A. E. Berg; Gay Brothers; Ogle", title="Universal Self-Instructor; Gay's Circle of Knowledge; "
                                                     "atlas chronologies",
         editions_targeted="1882; 1891; 1892-1936",
         existing_work_ids="sd2-1882-universal-self-instructor;sd2-1891-gays-circle;sd2-1892-atlas-chronology",
         status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="R39", frame="d2_reference_en", country="England", genre="Reference", author="T. B. Harbottle",
         title="Dictionary of Battles", editions_targeted="1904", existing_work_ids="sd2-1904-harbottle-battles",
         status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="P33", frame="d2_popular_en", country="US", genre="Popular history",
         author="H. J. Desmond; O. H. Parry; L. Outhwaite",
         title="Mooted Questions; The Pilgrim in Jerusalem; Unrolling the Map", editions_targeted="1902; 1920; 1935",
         existing_work_ids="sd2-1897-desmond-mooted;sd2-1920-parry-pilgrim;sd2-1935-outhwaite-unrolling",
         status="read", notes="added_during_reading (ninth sweep)"),
    dict(frame_id="H23", frame="d2_scholarly_en", country="Scotland", genre="Scholarship", author="G. A. Smith",
         title="The Historical Geography of the Holy Land", editions_targeted="1894; 1897",
         existing_work_ids="sd2-1894-smith-historical-geography", status="read",
         notes="added_during_reading (ninth sweep)"),
])
print("block 2 written")
