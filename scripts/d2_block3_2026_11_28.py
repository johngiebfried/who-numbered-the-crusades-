"""Strand D2, block 3 (28 November 2026): reference editions (Haydn, Chambers's, Americana, Nelson's,
Collier's, Schaff), church and national histories, scholarly works, and corrections to rows from
blocks 1-2 (Stebbing vol. 2 found; Mackay's ten; Bloss's sixth). Same conventions as block 2. MIT License.
"""
import csv

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


def ref(wid, **kw):
    kw.setdefault("genre", "Reference")
    kw.setdefault("census_frame", "d2_reference_en")
    return new(wid, **kw)


def church(wid, **kw):
    kw.setdefault("genre", "Church and national history")
    kw.setdefault("census_frame", "d2_church_en")
    return new(wid, **kw)


def schol(wid, **kw):
    kw.setdefault("genre", "Scholarship")
    kw.setdefault("census_frame", "d2_scholarly_en")
    return new(wid, **kw)


W = cur()
HAYDN_Q = ("IV. 1195, by emperor Henry VI. ; successful till his death in 1197. V. Proclaimed by Innocent III., 1198. "
           "Baldwin, count of Flanders, attacked the Greeks, and took Constantinople in 1202")
works = [
    ref("sd2-1866-haydn-moxon", label="Haydn's Dictionary of Dates (London, 1866)", author="Joseph Haydn; Benjamin "
                                                                                            "Vincent (ed.)",
        work="Haydn's Dictionary of Dates", year_label="1866", year_sort="1866",
        place_publisher="London: E. Moxon", headword="CRUSADES", tradition="Britain", enumerates="yes",
        H6="4", C="5", F="6", B="6", L1="7", L2="8", E="8", stated_phrase="VIII. And last, in 1270",
        scheme_family="moreri_eight_variant", signature_match="no", quote=HAYDN_Q,
        url=IA + "haydnsdictionary00haydrich", verification_level="full_text",
        title_page_checked="no (metadata: London, E. Moxon and Co., 1866)", country="GB",
        notes="Roman-numeral list I-VIII. 'VI. In 1228, by emperor Frederick II. ... In 1240, Richard, earl of "
              "Cornwall'; Andrew II and Damietta absent. 'VIII. And last, in 1270, by the same prince ... Other princes "
              "followed him, among others prince Edward, afterwards our Edward I.' The entry cites the Recueil "
              "(1844-60), so it postdates the 1844 edition (sa-1844-haydn, no list). The EASTERN EMPIRE entry has "
              "'The fourth crusade begins 1202'."),
    ref("sd2-1869-haydn-harper", label="Haydn's Dictionary of Dates (New York, 1869)",
        author="Joseph Haydn; Benjamin Vincent (ed.)", work="Haydn's Dictionary of Dates", year_label="1869",
        year_sort="1869", place_publisher="New York: Harper & Brothers", headword="CRUSADES", tradition="US",
        enumerates="yes", H6="4", C="5", F="6", B="6", L1="7", L2="8", E="8",
        scheme_family="moreri_eight_variant", signature_match="no", quote=HAYDN_Q,
        stemma_parent="sd2-1866-haydn-moxon", parent_evidence="documented: same entry",
        url=IA + "haydnsdictionary03hayd", verification_level="full_text",
        title_page_checked="no (metadata: New York, Harper & Brothers, 1869)", country="US",
        notes="US printing, same entry as London 1866."),
    ref("sd2-1883-haydn-harper", label="Haydn's Dictionary of Dates (New York, 1883)",
        author="Joseph Haydn; Benjamin Vincent (ed.)", work="Haydn's Dictionary of Dates", year_label="1883",
        year_sort="1883", place_publisher="New York: Harper & Brothers", headword="CRUSADES", tradition="US",
        enumerates="yes", H6="4", C="5", D="6", F="6", B="6", L1="7", L2="8", E="8",
        scheme_family="moreri_eight", signature_match="no",
        quote="VI. In 1216. In 1229, emperor Frederick II. obtained possession of Jerusalem on a truce for ten years. "
              "In 1240, Richard, earl of Cornwall, arrived at Palestine",
        stemma_parent="sd2-1866-haydn-moxon", parent_evidence="documented: same entry, revised",
        url=IA + "haydnsdictionary02hayd", verification_level="full_text",
        title_page_checked="no (metadata: New York, Harper & Brothers, 1883)", country="US",
        notes="The sixth now opens 'In 1216', taking in the Damietta crusade; Constantinople's capture redated 1203. "
              "Same entry in the 1889 and 1892 Putnam printings (haydnsdictionary04hayd; haydnsdictionary09hayd) and "
              "the 25th edition of 1910 (sd-1910-haydn-dates-25)."),
    ref("sd2-1898-haydn-toronto", label="Haydn's Dictionary of Dates (Toronto, 1898)",
        author="Joseph Haydn; Benjamin Vincent (ed.)", work="Haydn's Dictionary of Dates", year_label="1898",
        year_sort="1898", place_publisher="Toronto: Publisher's Syndicate", headword="CRUSADES", tradition="Canada",
        enumerates="yes", H6="4", C="5", D="6", F="6", B="6", L1="7", L2="8", E="8",
        scheme_family="moreri_eight", signature_match="no",
        quote="IV. 1195, by emperor Henry VI.: death in 1197. V. Proclaimed by Innocent III., 1198",
        stemma_parent="sd2-1883-haydn-harper", parent_evidence="documented: same entry",
        url=IA + "haydnsdictionary00hayd_1", verification_level="full_text",
        title_page_checked="no (metadata: Toronto, Publisher's Syndicate, 1898)", country="CA",
        notes="Canadian printing; the edition read for Canada."),
    ref("sd2-1871-chambers-lippincott", label="Chambers's Encyclopaedia (Philadelphia, 1871)",
        author="", work="Chambers's Encyclopaedia, vol. 3", year_label="1871", year_sort="1871",
        place_publisher="Philadelphia: J. B. Lippincott", volume="vol. 3", headword="CRUSADES", tradition="US",
        enumerates="yes", C="4", F="5", L1="6", L2="7", scheme_family="frederick_fifth_seven",
        signature_match="no", stemma_parent="sd-1868-chambers-enc", parent_evidence="documented: same article",
        quote="Fourth Crusade. - Crusading unfortunately now became a constituent of the papal policy; and in 1203 a "
              "fourth expedition ... Fifth Crusade. - This was commanded by Frederick II.",
        url=IA + "chamberssencyclo03phil", verification_level="full_text",
        title_page_checked="no (metadata: Philadelphia, Lippincott, 1871)", country="US",
        notes="US printing, text as Edinburgh 1868. The 1878 printing (chamberssencyclo0003vari) adds the heads "
              "'Sixth Crusade.-In 1244, a new race of Turks burst into Syria' and 'Seventh Crusade.-This also was "
              "primarily undertaken by St Louis, but he having died at Tunis in 1270'."),
    ref("sd2-1917-nelsons-perpetual", label="Nelson's Perpetual Loose-Leaf Encyclopaedia, vol. 3",
        author="", work="Nelson's Perpetual Loose-Leaf Encyclopaedia", year_label="1917", year_sort="1917",
        place_publisher="New York: Thomas Nelson & Sons", volume="vol. 3", headword="CRUSADES", tradition="US",
        enumerates="yes", C="4", F="5", L1="6", L2="7", E="7", scheme_family="frederick_fifth_seven",
        signature_match="no",
        quote="The Fourth Crusade is known as a pseudo-crusade, for the crusaders never reached the Holy Land at all "
              "... The leader of the Fifth Crusade (1228-9), the Emperor Frederick II.",
        url=IA + "nelsonsperpetual03finl", verification_level="full_text", title_page_checked="no", country="US",
        notes="'the sixth crusade was undertaken (1248-54) by (St.) Louis IX.'; 'in 1270, Louis organized the seventh "
              "crusade ... This crusade, in which Edward of England (afterwards Edward I.) took part, was the last "
              "effort'. Bibliography: Gibbon's Decline and Fall, Milman, Cox (Epochs), Archer, Röhricht, Stevenson. "
              "Nelson's is an Edinburgh firm; this is the New York loose-leaf edition."),
    ref("sd2-1921-colliers-new", label="Collier's New Encyclopedia, vol. 3", author="",
        work="Collier's New Encyclopedia", year_label="1921", year_sort="1921",
        place_publisher="New York: P. F. Collier", volume="vol. 3", headword="CRUSADE", tradition="US",
        enumerates="yes", D="4", F="5", L1="6", scheme_family="german_six", signature_match="no",
        stemma_parent="sa-1830-americana",
        parent_evidence="documented: 'The fourth crusade was conducted by the king of Hungary, Andrew II., in 1217' "
                        "(Americana 1830, with 'by sea'), thirteen consecutive words",
        quote="4, The fourth crusade was conducted by the King of Hungary, Andrew II., in 1217. 5. The fifth (1228) "
              "was conducted by Frederick II. ... 6. The sixth, a. d. 1248, by Saint Louis",
        url=IA + "colliersnewencyc03newy", verification_level="full_text",
        title_page_checked="no (metadata: New York, P. F. Collier, 1921)", country="US", channel="Americana 1830",
        notes="A numbered list of 'the principal crusades for the conquest of Palestine', one to six, with the "
              "second dated 1142. The German six of the 1830 Americana, ninety years on; 1202-04 is not counted."),
    ref("sd2-1882-schaff-religious-encyclopedia", label="Schaff (ed.), A Religious Encyclopaedia, vol. 1",
        author="Philip Schaff (ed.)", work="A Religious Encyclopaedia (Schaff-Herzog)", year_label="1882",
        year_sort="1882", place_publisher="New York: Funk & Wagnalls", volume="vol. 1", headword="CRUSADES",
        tradition="US", enumerates="partial", C="4",
        quote="became sadly apparent when Innocent III. preached the fourth crusade (1203)",
        url=IA + "15203381.1309.emory.edu", verification_level="full_text", title_page_checked="no",
        country="US",
        notes="Only the Fourth numbered in the passages found ('In 1198 he was charged by Innocent III. with preaching "
              "the fourth crusade', of Fulk of Neuilly). Names Fuller, Kugler, Röhricht, Sybel, Stubbs, Wilken, "
              "Michaud, Mills, Maimbourg, Keightley."),
    ref("sd2-1848-chambers-information", label="Chambers's Information for the People", author="W. and R. Chambers",
        work="Chambers's Information for the People", year_label="1848", year_sort="1848",
        place_publisher="Edinburgh: W. and R. Chambers", tradition="Britain", enumerates="no", scheme_family="none",
        url=IA + "chamberssinform00goog", verification_level="full_text", title_page_checked="no", country="GB",
        notes="No crusade numbers in the text layer (27 mentions of 'crusad')."),
    church("sd2-1860-mosheim-reid", label="Mosheim's Institutes, tr. Murdock, ed. Reid",
           author="J. L. von Mosheim; tr. James Murdock; ed. James Seaton Reid",
           work="Institutes of Ecclesiastical History, Ancient and Modern",
           year_label="1860 printing (Reid's edition 1848)", year_sort="1860", place_publisher="London: W. Tegg",
           tradition="Britain", enumerates="partial", L1="6",
           quote="This is reckoned the sixth crusade by all authorities - R.",
           url=IA + "mosheimsinstitut00mosh", verification_level="full_text",
           title_page_checked="no (metadata: London, W. Tegg, 1860)", country="GB",
           notes="Editor's footnote signed 'R.' in the section on Louis IX's crusades; its anchor (the crusade of "
                 "1248-54 or of 1270) is unclear in the OCR, and the sixth fits Gibbon's count only for 1248. "
                 "Footnotes: 'The English reader may consult Gibbon's Decline and Fall, chap. lviii. lix.'; 'Milman in "
                 "his edition of Gibbon remarks'."),
    church("sd2-1872-neander-torrey", label="Neander, General History of the Christian Religion and Church, tr. "
                                          "Torrey, vol. 4",
           author="August Neander; tr. Joseph Torrey", work="General History of the Christian Religion and Church",
           year_label="1872 printing", year_sort="1872", place_publisher="Boston", tradition="US", enumerates="no",
           scheme_family="none", url=IA + "generalhistoryof187204nean", verification_level="full_text",
           title_page_checked="no", country="US",
           notes="No crusade numbers. Gregory X elected while 'at Ptolemais on a crusade under prince Edward of "
                 "England'."),
    church("sd2-1853-hardwick-middle-age", label="Charles Hardwick, A History of the Christian Church: Middle Age",
           author="Charles Hardwick", work="A History of the Christian Church: Middle Age",
           year_label="1853 (read 1877 printing)", year_sort="1853", place_publisher="Cambridge: Macmillan",
           tradition="Britain", enumerates="no", scheme_family="none", url=IA + "historyofchristi1853hard",
           verification_level="full_text", title_page_checked="no", country="GB",
           notes="No crusade numbers. Footnotes: 'Wilken, Gesch. der Kreuzzüge, Michaud, Hist. des Croisades, and "
                 "Gibbon, ch. lviii'; 'Gibbon, v. 283 sq., ed. Milman'."),
    church("sd2-1864-kurtz-history", label="J. H. Kurtz, History of the Christian Church (Edinburgh)",
           author="J. H. Kurtz", work="History of the Christian Church (English translation)",
           year_label="1864", year_sort="1864", place_publisher="Edinburgh: T. & T. Clark", tradition="Britain",
           enumerates="yes", D="4", F="5", L1="6", L2="7", scheme_family="other", signature_match="no",
           quote="1217. Fourth Crusade. Andrew II. of Hungary ... 1228. Fifth Crusade (Fred. II.) ... Sixth Crusade "
                 "(Louis IX.) ... 1270. Seventh Crusade (Louis IX.)",
           url=IA + "historyofchristi02kurt", verification_level="full_text",
           title_page_checked="no (metadata: Edinburgh, T. & T. Clark, 1864)", country="GB",
           channel="German church history (translation)",
           notes="Chronological table. The German six (D 4, F 5, L1 6) with Tunis added as seventh; 1202-04 not "
                 "counted. A translation: evidence for the English reader, not for Kurtz's German text."),
    church("sd2-1887-fisher-church", label="G. P. Fisher, History of the Christian Church",
           author="George Park Fisher", work="History of the Christian Church", year_label="1887", year_sort="1887",
           place_publisher="New York: Scribner", tradition="US", enumerates="partial", F="5",
           quote="Frederick's Fifth crusade, 1228-1229", url=IA + "historyofchrist00fish",
           verification_level="full_text", title_page_checked="no", country="US",
           notes="Marginal head. Only the fifth found numbered."),
    church("sd2-1912-alzog-manual", label="J. B. Alzog, Manual of Universal Church History (tr.)",
           author="J. B. Alzog; tr. F. J. Pabisch and T. S. Byrne", work="History of the Church (Manual of Universal "
                                                                         "Church History)",
           year_label="1912 printing (translation first published Cincinnati 1874-78)", year_sort="1912",
           place_publisher="New York", tradition="US", enumerates="yes", F="5", L1="6", L2="7",
           scheme_family="frederick_fifth_seven", signature_match="no",
           quote="1228. Frederic, notwithstanding that he was excommunicated, undertakes the fifth Crusade ... 1248. St. "
                 "Louis undertakes the sixth Crusade against Egypt ... St. Louis undertakes the seventh and last "
                 "Crusade against Tunis",
           url=IA + "historyofchurch02alzo", verification_level="full_text", title_page_checked="no", country="US",
           channel="German Catholic church history (translation)",
           notes="Chronological summary. Translation of a German Catholic manual for US seminaries."),
    church("sd2-1874-lingard-england", label="John Lingard, A History of England (vols. 2-3)",
           author="John Lingard", work="A History of England", year_label="1874 printing (first ed. 1819-30)",
           year_sort="1874", place_publisher="London", tradition="Britain", enumerates="no", scheme_family="none",
           url=IA + "historyofengland02ling_0", verification_level="full_text", title_page_checked="no",
           country="GB",
           notes="No crusade numbers in vols. 2-3 (Richard I to Edward I). Louis IX 'reassumed the cross; and Edward "
                 "immediately resolved to share with that accomplished monarch the danger and the merit of the new "
                 "crusade'. Catholic historian."),
    church("sd2-1854-hume-england", label="David Hume, The History of England, vol. 2 (1854 printing)",
           author="David Hume", work="The History of England", year_label="1854 printing", year_sort="1854",
           place_publisher="", tradition="Britain", enumerates="no", scheme_family="none",
           url=IA + "humeshistoryofen0002davi", verification_level="full_text", title_page_checked="no",
           country="GB", notes="No crusade numbers in the Plantagenet volume."),
    church("sd2-1859-students-hume", label="The Student's Hume", author="David Hume; abridged (Murray's Student's "
                                                                         "Manuals)",
           work="The Student's Hume: A History of England", year_label="1859", year_sort="1859",
           place_publisher="London: John Murray", tradition="Britain", genre="School", census_frame="d2_school_en",
           enumerates="no", scheme_family="none", url=IA + "studentshume00unkngoog", verification_level="full_text",
           title_page_checked="no", country="GB",
           notes="'§ 20. Prince Edward's Crusade' (unnumbered). Footnote: 'The history of the Crusades is narrated in "
                 "the Student's Gibbon, p. 545, seq.'"),
    church("sd2-1874-green-short-history", label="J. R. Green, A Short History of the English People",
           author="John Richard Green", work="A Short History of the English People",
           year_label="1874 (read 1893 printing)", year_sort="1874", place_publisher="London: Macmillan",
           tradition="Britain", enumerates="no", scheme_family="none", url=IA + "ashorthistoryen19greegoog",
           verification_level="full_text", title_page_checked="no", country="GB",
           notes="Annals: '1270 Edward goes on Crusade'. No numbers."),
    church("sd2-1893-tout-edward-first", label="T. F. Tout, Edward the First", author="T. F. Tout",
           work="Edward the First (Twelve English Statesmen)", year_label="1893", year_sort="1893",
           place_publisher="London: Macmillan", tradition="Britain", enumerates="no", scheme_family="none",
           url=IA + "edwardfirst00toutiala", verification_level="full_text", title_page_checked="no", country="GB",
           notes="'CHAPTER III Edward as a Crusader - 1268-1272'. No numbers."),
    schol("sd2-1921-krey-first-crusade", label="A. C. Krey, The First Crusade", author="August C. Krey",
          work="The First Crusade: The Accounts of Eye-Witnesses and Participants", year_label="1921",
          year_sort="1921", place_publisher="Princeton: Princeton University Press", tradition="US",
          enumerates="no", scheme_family="none", url=IA + "firstcrusadeacc00kreygoog",
          verification_level="full_text", title_page_checked="no", country="US",
          notes="Only the First. Gibbon cited: 'Gibbon: Decline and Fall of the Roman Empire, Chapters LVIII-LXI'."),
    schol("sd2-1917-paetow-guide", label="L. J. Paetow, A Guide to the Study of Medieval History",
          author="Louis John Paetow", work="A Guide to the Study of Medieval History", year_label="1917",
          year_sort="1917", place_publisher="Berkeley: University of California Press", tradition="US",
          enumerates="partial", C="4", D="5",
          quote="Fifth crusade. R. RÖHRICHT, Studien zur Geschichte des fünften Kreuzzuges, Innsbruck, 1891. Frederick "
                "II and the crusades.",
          url=IA + "guidetostudyofme00paetiala", verification_level="full_text", title_page_checked="no",
          country="US",
          notes="Bibliography heads: Munro's '\"The fourth crusade\"' (Translations and Reprints III.1), Villehardouin's "
                "'Chronicle of the fourth crusade', 'Fifth crusade' (Röhricht's title), then 'Frederick II and the "
                "crusades' by name. Numbers stop at five; later expeditions are named. Gibbon listed in the Fred de Fau "
                "reprint (1906) and Bury's edition."),
    schol("sd2-1926-cmh-v5", label="The Cambridge Medieval History, vol. 5", author="J. R. Tanner, C. W. "
                                                                                    "Previté-Orton, Z. N. Brooke "
                                                                                    "(eds.)",
          work="The Cambridge Medieval History, vol. 5", year_label="1926", year_sort="1926",
          place_publisher="Cambridge: Cambridge University Press; New York: Macmillan", tradition="Britain",
          enumerates="partial", C="4", D="5",
          quote="1219 The Fifth Crusade. (5 Nov.) The Crusaders capture Damietta",
          url=IA + "BuryJBTheCambridgeMedievalHistoryVol51926", verification_level="full_text",
          title_page_checked="yes (OCR: THE CAMBRIDGE MEDIEVAL HISTORY VOLUME V)", country="GB",
          notes="Chronological table and text: 'had not the Fourth Crusade been diverted to the conquest of "
                "Constantinople'; Henry VI's crusade unnumbered; 'the last great Crusade under Louis IX of France and "
                "Edward of England' (1270-72, unnumbered). Read for numbering only."),
    schol("sd2-1905-thatcher-mcneal", label="Thatcher and McNeal, A Source Book for Mediaeval History",
          author="O. J. Thatcher; E. H. McNeal", work="A Source Book for Mediaeval History", year_label="1905",
          year_sort="1905", place_publisher="New York: Scribner", tradition="US", enumerates="no",
          scheme_family="none", url=IA + "sourcebookformed00thatuoft", verification_level="full_text",
          title_page_checked="no", country="US", notes="No crusade numbers."),
    schol("sd2-1888-archer-crusade-richard", label="T. A. Archer, The Crusade of Richard I",
          author="T. A. Archer", work="The Crusade of Richard I, 1189-92 (English History by Contemporary Writers)",
          year_label="1888 (read 1912 printing)", year_sort="1888", place_publisher="London: David Nutt",
          tradition="Britain", enumerates="partial", C="4",
          quote="Villehardouin tells us how he took part in the fourth crusade, was one of the envoys to the Venetians",
          url=IA + "CrusadeOfRichardI", verification_level="full_text", title_page_checked="no", country="GB",
          notes="Only the Fourth numbered. Draws on Stubbs (24 mentions)."),
    new("sd2-1920-wells-outline", label="H. G. Wells, The Outline of History", author="H. G. Wells",
        work="The Outline of History", year_label="1920", year_sort="1920", place_publisher="New York: Macmillan",
        tradition="Britain", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        C="4", D="5", F="6", L1="7", scheme_family="modern_eight", signature_match="near_modern",
        quote="The Sixth Crusade (1229) was a crusade bordering upon absurdity. The Emperor Frederick II",
        url=IA + "cu31924028328759", verification_level="full_text", title_page_checked="no", country="GB",
        notes="'The bulk of the Fourth Crusade never reached the Holy Land at all. It started from Venice (1202)'; 'a "
              "Fifth Crusade. This crusade aimed at the conquest of Egypt'; 'the Seventh Crusade, the Crusade of St. "
              "Louis'. No eighth found. US printing of the London work (1919-20)."),
    new("sd2-1921-van-loon-story", label="H. W. Van Loon, The Story of Mankind", author="Hendrik Willem Van Loon",
        work="The Story of Mankind", year_label="1921 (read DLI copy)", year_sort="1921",
        place_publisher="New York: Boni and Liveright", tradition="US", genre="Popular history",
        census_frame="d2_popular_en", enumerates="no", scheme_family="none", url=IA + "in.ernet.dli.2015.462857",
        verification_level="full_text", title_page_checked="no", country="US", notes="No crusade numbers."),
    new("sd2-1850-rts-crusades", label="The Crusades (Religious Tract Society)", author="[Religious Tract Society]",
        work="The Crusades", year_label="n.d. (archive.org '[180-]'; RTS imprint)", year_sort="1850",
        place_publisher="London: Religious Tract Society", tradition="Britain", genre="Popular history (juvenile)",
        census_frame="d2_popular_en", enumerates="yes", H6="4", C="5", D="6", B="7", L1="8",
        stated_phrase="The last Crusade", scheme_family="", signature_match="no",
        quote="Fourth Crusade. - Saladin did not long survive his treaty with Richard ... The author of the Sixth "
              "Crusade was Innocent III. It was started in the year 1215",
        url=IA + "crusades00britgoog", verification_level="full_text",
        title_page_checked="no (date not legible; year_sort 1850 is an estimate)", country="GB", channel="Mills",
        notes="Heads: 'Fourth Crusade' (Celestine III, Germany alone), 'The Fifth Crusade' (the Latin conquest of "
              "Constantinople its 'unlooked-for result'), Sixth (1215, Innocent III), 'The Seventh Crusade.-"
              "Notwithstanding the treaty of Frederick', 'The Eighth Crusade.-The peace of Richard, earl of Cornwall, "
              "was soon terminated', 'The last Crusade', in which 'Prince Edward signalized his name'. Mills's slots. "
              "Contradiction in the text: 'It was in the Sixth Crusade that Richard, earl of Cornwall, distinguished "
              "himself'. Footnotes cite Gibbon (12-volume edition) and quote him."),
    new("sd2-1875-christian-brothers-compendium",
        label="Christian Brothers, Compendiums of General History (Quebec)", author="Brothers of the Christian "
                                                                                   "Schools (B. C. S.)",
        work="Compendiums of General History, the History of Canada, and the Other British North American Provinces",
        year_label="1875", year_sort="1875", place_publisher="Quebec: C. Darveau", tradition="Canada",
        genre="School", census_frame="d2_school_en", enumerates="partial", C="4", L2="8", E="8",
        quote="Edward I, after having taken part in the eighth Crusade, hearing of the death of his father, 1272, "
              "hastened back to England",
        url=IA + "cihm_00977", verification_level="full_text",
        title_page_checked="yes (OCR: By B. C. S. Approved by the Council of Public Instruction. QUEBEC: C. DARVEAU)",
        country="CA", channel="French Christian Brothers' textbooks (inferred)",
        notes="Review questions: 'By whom was the fourth Crusade preached? ... Why did the crusaders march on "
              "Constantinople?'; 'What was the last Crusade? Against what country did he set out? How did St. Louis "
              "die?'. English-language Catholic school text from Quebec."),
    # corrections
    dict(work_id="sd2-1830-stebbing-chivalry", enumerates="yes", H6="4", C="4", D="5", F="5", L1="6", L2="7",
         scheme_family="frederick_fifth_seven", signature_match="no", url=IA + "dli.ministry.14023",
         quote="CHAPTER VII. THE FOURTH CRUSADE AND ITS INGLORIOUS TERMINATION ... CHAPTER VIII. DEPARTURE OF THE "
               "FOURTH CRUSADE.-ALLIANCE WITH THE VENETIANS.-SIEGE AND CAPTURE OF ZARA",
         title_page_checked="yes (OCR: IN TWO VOLUMES. EDINBURGH: PRINTED FOR CONSTABLE AND CO.)",
         notes="[D2 2026-11-28, second pass] Vol. 2 read (dli.ministry.14023; also historychivalry00stebgoog and "
               "03stebgoog; historychivalry02stebgoog is a second copy of vol. 1). Ch. VII: the Germans 'began the war "
               "of the Fourth Crusade' (1197); ch. VIII: 'Departure of the Fourth Crusade' for 1202-04: both called "
               "fourth. Ch. X: 'Conquest of Damietta.-Frederic II. and the Fifth Crusade'; ch. XI: 'Louis IX. and the "
               "Sixth and Seventh Crusades'. The paper's table has C 4, D 5, L1 6, L2 7. Footnotes '* Gibbon.' in vol. "
               "1."),
    dict(work_id="sd-1841-mackay-delusions", L1="9", L2="10", E="10", scheme_family="other", signature_match="no",
         stated_phrase="Tenth Crusade, by Louis IX. and Prince Edward of England", checked_on=D,
         research_pass="strand_d;strand_d2",
         notes=app("sd-1841-mackay-delusions", "notes",
                   "[D2 2026-11-28] Index of the copy read (a modern facsimile reprint of the 1852 edition; archive.org "
                   "dates it 1841): 'Fourth Crusade, undertaken by the German ...'; 'Seventh Crusade:-Undertaken by "
                   "Frederick II.'; 'Eighth Crusade, commenced in France ... Richard earl of Cornwall'; 'Ninth Crusade, "
                   "began by Louis IX. ... Damietta taken'; 'Tenth Crusade, by Louis IX. and Prince Edward of England'. "
                   "A count of ten: nine_F7 with the Barons' crusade as eighth. The text: 'Thus ended the eighth "
                   "Crusade, the most beneficial of all'; Edward 'set sail for England; and thus ended the last "
                   "Crusade'. Reprinted to the 1930s (archive.org copies 1852-1932). Whether the 1841 first edition "
                   "has the same count is not checked.", W)),
    dict(work_id="sd2-1853-bloss-heroines", F="",
         notes=app("sd2-1853-bloss-heroines", "notes",
                   "[second pass] F cleared: Violante (Yolande) as 'Heroine of the Sixth Crusade' does not show where "
                   "Frederick II's crusade falls; she was John of Brienne's daughter as well as Frederick's wife. The "
                   "paper's table also leaves Frederick blank.", W)),
    dict(work_id="sd-1924-americana",
         notes=app("sd-1924-americana", "notes",
                   "[D2 2026-11-28] Same text in the 1922 printing (encyclopediaamer08unse), vol. 8.", W)),
    dict(work_id="sd-1868-chambers-enc",
         notes=app("sd-1868-chambers-enc", "notes",
                   "[D2 2026-11-28] Same article in the Philadelphia 1871 (sd2-1871-chambers-lippincott) and 1878 "
                   "printings.", W)),
    dict(work_id="1894-t-a-archer-c-l-kingsford",
         notes=app("1894-t-a-archer-c-l-kingsford", "notes",
                   "US printing 1895 under the title The Story of the Crusades (storycrusades00wattgoog): same contents.",
                   W)),
    dict(work_id="sa-1837-penny",
         notes=app("sa-1837-penny", "notes",
                   "[D2 2026-11-28] Confirmed in pennycyclopaedi12unkngoog (vol. 8): 'Seventh Crusade,-England was the "
                   "pioneer of the seventh and last crusade. While Louis was still in Tunis, Edward ... prepared a new "
                   "crusade'.", W)),
]
L.upsert_works(works, clear_slots=[("sd2-1853-bloss-heroines", "F")])

W = cur()


def attr(wid, **kw):
    kw["work_id"] = wid
    kw.setdefault("checked_on", D)
    if wid in W and "gibbon_numbers" not in kw:
        kw["gibbon_numbers"] = L.gibbon_numbers(W[wid])
    return kw


A = [
    attr("sd2-1866-haydn-moxon", frame_id="R13", country_pub="England", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="inside_last", gibbon_cited="none",
         numbers_follow="moreri;inferred", notes="CRUSADES entry H6 4; EASTERN EMPIRE entry C 4."),
    attr("sd2-1869-haydn-harper", frame_id="R13", country_pub="US", author_origin="England", fourth_identity="H6",
         fifth_identity="C", edward_status="inside_last", gibbon_cited="none", numbers_follow="moreri;inferred"),
    attr("sd2-1883-haydn-harper", frame_id="R13", country_pub="US", author_origin="England", fourth_identity="H6",
         fifth_identity="C", edward_status="inside_last", gibbon_cited="none", numbers_follow="moreri;inferred"),
    attr("sd2-1898-haydn-toronto", frame_id="R13", country_pub="Canada", author_origin="England",
         fourth_identity="H6", fifth_identity="C", edward_status="inside_last", gibbon_cited="none",
         numbers_follow="moreri;inferred"),
    attr("sd2-1871-chambers-lippincott", frame_id="R12", country_pub="US", author_origin="Scotland",
         fourth_identity="C", fifth_identity="F", gibbon_cited="none", numbers_follow="german;documented",
         notes="Chambers's was built on Brockhaus."),
    attr("sd2-1917-nelsons-perpetual", frame_id="R24", country_pub="US", author_origin="Scotland",
         fourth_identity="C", fifth_identity="F", edward_status="inside_last", gibbon_cited="bibliography",
         gibbon_edition="unspecified", sources_named="Gibbon;Milman;Cox;Archer;Röhricht;Stevenson",
         numbers_follow="german;inferred", notes="Cites Gibbon and Cox; follows neither."),
    attr("sd2-1921-colliers-new", frame_id="R23", country_pub="US", fourth_identity="other", fifth_identity="F",
         edward_status="absent", gibbon_cited="none", numbers_follow="german;documented",
         notes="Copies the 1830 Americana."),
    attr("sd2-1882-schaff-religious-encyclopedia", frame_id="R29", country_pub="US", author_origin="Switzerland",
         fourth_identity="C", fifth_identity="none", gibbon_cited="none",
         sources_named="Fuller;Kugler;Röhricht;Sybel;Stubbs;Wilken;Michaud;Mills;Maimbourg;Keightley",
         numbers_follow="unclear;inferred"),
    attr("sd2-1848-chambers-information", frame_id="R11", country_pub="Scotland", fourth_identity="none",
         fifth_identity="none", gibbon_cited="none", sources_named="Hallam;Robertson;Sismondi",
         numbers_follow="unclear;inferred"),
    attr("sd2-1860-mosheim-reid", frame_id="C01", country_pub="England", author_origin="Germany",
         fourth_identity="none", fifth_identity="none", gibbon_cited="footnote", gibbon_edition="Milman",
         sources_named="Gibbon;Milman;Bower", numbers_follow="gibbon;inferred",
         notes="Editor's note: 'reckoned the sixth crusade by all authorities' (r40)."),
    attr("sd2-1872-neander-torrey", frame_id="C03", country_pub="US", author_origin="Germany",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         sources_named="Wilken", numbers_follow="unclear;inferred"),
    attr("sd2-1853-hardwick-middle-age", frame_id="C07", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", gibbon_cited="footnote", gibbon_edition="Milman",
         sources_named="Wilken;Michaud;Gibbon;Neander;Robertson", numbers_follow="unclear;inferred",
         notes="Cites Gibbon (Milman's edition), uses no numbers."),
    attr("sd2-1864-kurtz-history", frame_id="C05", country_pub="Scotland", author_origin="Germany",
         fourth_identity="other", fifth_identity="F", gibbon_cited="none", numbers_follow="german;documented",
         notes="Translation."),
    attr("sd2-1887-fisher-church", frame_id="C09", country_pub="US", author_origin="US", fourth_identity="none",
         fifth_identity="F", gibbon_cited="none", numbers_follow="german;inferred"),
    attr("sd2-1912-alzog-manual", frame_id="C12", country_pub="US", author_origin="Germany",
         fourth_identity="none", fifth_identity="F", edward_status="absent", gibbon_cited="none",
         sources_named="Michaud;Wilken;Raumer;Schlosser;Neander;Gieseler", numbers_follow="german;documented",
         notes="Translation."),
    attr("sd2-1874-lingard-england", frame_id="C14", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred"),
    attr("sd2-1854-hume-england", frame_id="C16", country_pub="England", author_origin="Scotland",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred"),
    attr("sd2-1859-students-hume", frame_id="C16", country_pub="England", fourth_identity="none",
         fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="footnote",
         gibbon_edition="Student's Gibbon", sources_named="Student's Gibbon", numbers_follow="unclear;inferred",
         notes="Sends the reader to the Student's Gibbon for the crusades."),
    attr("sd2-1874-green-short-history", frame_id="C18", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred"),
    attr("sd2-1893-tout-edward-first", frame_id="C19", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred"),
    attr("sd2-1921-krey-first-crusade", frame_id="H11", country_pub="US", author_origin="US",
         fourth_identity="none", fifth_identity="none", gibbon_cited="footnote", gibbon_edition="unspecified",
         sources_named="Gibbon;Munro", numbers_follow="unclear;inferred"),
    attr("sd2-1917-paetow-guide", frame_id="H13", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="D", gibbon_cited="bibliography", gibbon_edition="Bury",
         sources_named="Röhricht;Munro;Villehardouin;Bury;Gibbon", numbers_follow="modern;documented",
         notes="Fourth and Fifth from Munro's and Röhricht's titles; the rest named."),
    attr("sd2-1926-cmh-v5", frame_id="H14", country_pub="England", fourth_identity="C", fifth_identity="D",
         edward_status="last_unnumbered", gibbon_cited="named_in_text", gibbon_edition="unspecified",
         numbers_follow="modern;inferred", notes="Numbers the Fourth and Fifth only."),
    attr("sd2-1905-thatcher-mcneal", frame_id="H17", country_pub="US", fourth_identity="none",
         fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
    attr("sd2-1888-archer-crusade-richard", frame_id="H08", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="none", gibbon_cited="none", sources_named="Stubbs;Stevenson;Conder",
         numbers_follow="unclear;inferred"),
    attr("sd2-1920-wells-outline", frame_id="P24", country_pub="US", author_origin="England", fourth_identity="C",
         fifth_identity="D", gibbon_cited="quoted", gibbon_edition="unspecified", sources_named="Gibbon",
         numbers_follow="modern;inferred", notes="Read in the New York printing."),
    attr("sd2-1921-van-loon-story", frame_id="P25", country_pub="US", author_origin="Netherlands",
         fourth_identity="none", fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
    attr("sd2-1850-rts-crusades", frame_id="P30", country_pub="England", fourth_identity="H6",
         fifth_identity="C", edward_status="last_unnumbered", gibbon_cited="footnote;quoted",
         gibbon_edition="unspecified", sources_named="Gibbon", numbers_follow="michaud_mills;inferred",
         notes="Mills's slots."),
    attr("sd2-1875-christian-brothers-compendium", frame_id="S14", country_pub="Canada", author_origin="Canada",
         fourth_identity="C", fifth_identity="none", edward_status="inside_last", gibbon_cited="none",
         numbers_follow="french_school;inferred"),
    attr("sd2-1830-stebbing-chivalry", frame_id="P02", fourth_identity="both", fifth_identity="D+F",
         edward_status="", gibbon_cited="footnote", numbers_follow="german;inferred",
         notes="Frederick-fifth seven (merged form) in Edinburgh, 1830; Henry VI's and the 1202 expedition both "
               "'the Fourth Crusade'."),
    attr("sd-1841-mackay-delusions", frame_id="P05", country_pub="England", author_origin="Scotland",
         fourth_identity="H6", fifth_identity="C", edward_status="other_number", ninth_referent="other",
         gibbon_cited="unchecked", numbers_follow="michaud_mills;inferred",
         notes="Ten: Louis IX's first crusade the ninth, Tunis with Edward the tenth."),
]
L.upsert_attrs(A)

C = [
    ("sd2-1921-colliers-new", "sa-1830-americana", "copies wording",
     "'The fourth crusade was conducted by the king of Hungary, Andrew II., in 1217'", "documented"),
    ("sd2-1917-nelsons-perpetual", "Gibbon", "bibliography", "'See Gibbon's Decline and Fall of the Roman Empire "
                                                             "(1776-88)'", "documented"),
    ("sd2-1917-nelsons-perpetual", "1874-george-w-cox", "bibliography", "Cox named 8 times near 'crusade'",
     "documented"),
    ("sd2-1860-mosheim-reid", "Gibbon", "cites in footnote", "'The English reader may consult Gibbon's Decline and "
                                                            "Fall, chap. lviii. lix.'", "documented"),
    ("sd2-1853-hardwick-middle-age", "Gibbon", "cites in footnote", "'Gibbon, ch. lviii'; 'Gibbon, v. 283 sq., ed. "
                                                                   "Milman'", "documented"),
    ("sd2-1853-hardwick-middle-age", "Michaud", "cites in footnote", "'Michaud, Hist. des Croisades'", "documented"),
    ("sd2-1853-hardwick-middle-age", "Wilken", "cites in footnote", "'Wilken, Gesch. der Kreuzzüge'", "documented"),
    ("sd2-1859-students-hume", "sd2-1868-students-gibbon", "same publisher or series",
     "'The history of the Crusades is narrated in the Student's Gibbon, p. 545, seq.'", "documented"),
    ("sd2-1917-paetow-guide", "Röhricht", "bibliography", "'Studien zur Geschichte des fünften Kreuzzuges, "
                                                          "Innsbruck, 1891' under 'Fifth crusade'", "documented"),
    ("sd2-1917-paetow-guide", "1896-dana-c-munro", "bibliography", "'vol. III, no. 1, \"The fourth crusade\"'",
     "documented"),
    ("sd2-1921-krey-first-crusade", "Gibbon", "cites in footnote", "'Decline and Fall ... Chapters LVIII-LXI'",
     "documented"),
    ("sd2-1850-rts-crusades", "Gibbon", "cites in footnote; quotes", "'Gibbon's Decline and Fall of the Roman "
                                                                    "Empire, vol. xi p. 131'", "documented"),
    ("sd2-1882-schaff-religious-encyclopedia", "Michaud", "bibliography", "named near 'crusade'", "documented"),
    ("sd2-1882-schaff-religious-encyclopedia", "Mills", "bibliography", "named near 'crusade'", "documented"),
    ("sd2-1882-schaff-religious-encyclopedia", "Kugler", "bibliography", "named near 'crusade'", "documented"),
    ("sd2-1926-cmh-v5", "Gibbon", "cites", "'Gibbon, on economic effects of the Crusades' (index)", "documented"),
    ("sd2-1883-haydn-harper", "sd2-1866-haydn-moxon", "same publisher or series", "Same entry, revised",
     "documented"),
]
L.append_citations([dict(citing_work_id=a, cited=b, relation=c, evidence=d, confidence=e) for a, b, c, d, e in C])

R = [
    dict(reason_id="r39", year="1918", work="Encyclopedia Americana, CRUSADES", author="", language="en",
         entry_id="sd-1924-americana", kind="statement_of_custom", target="fifth", expeditions_affected="D;F",
         phrase="This is sometimes spoken of as the Fifth Crusade. What is more usually called the Fifth Crusade was "
                "led by Frederick II of Germany",
         verification="full_text", source="archive.org encyclopediaamer08unse (1922 printing), vol. 8",
         notes="Of the Damietta crusade. Same sentence in 1924 and 1953 (sd-1953-americana)."),
    dict(reason_id="r40", year="1848", work="Mosheim, Institutes of Ecclesiastical History (Murdock tr.)",
         author="James Seaton Reid (editor's note)", language="en", entry_id="sd2-1860-mosheim-reid",
         kind="statement_of_custom", target="L1 or L2", expeditions_affected="L1",
         phrase="This is reckoned the sixth crusade by all authorities",
         verification="full_text", source="archive.org mosheimsinstitut00mosh (London: Tegg, 1860)",
         notes="Signed 'R.'; the anchor is unclear in the OCR (Louis IX's crusade of 1248 or of 1270)."),
]
L.append_reasons(R)

# conflicts resolved by reading
cpath = L.ROOT / "reconciliation" / "conflicts.csv"
with open(cpath, newline="", encoding="utf-8") as f:
    raw = f.read()
nl = "\r\n" if "\r\n" in raw else "\n"
rows = list(csv.reader(raw.splitlines()))
for r in rows[1:]:
    if r[0] == "1877-eb9-crusades" and r[1] == "E" and "resolved" not in r[-1]:
        r[-1] += "; resolved 2026-11-28 (D2): E 9, Edward inside the ninth (US reprint read)"
    if r[0] == "1911-ernest-barker" and r[1] == "E" and "resolved" not in r[-1]:
        r[-1] += "; resolved 2026-11-28 (D2): E cleared, Edward named and excluded from the numbering"
with open(cpath, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, lineterminator=nl).writerows(rows)

B = "archive.org metadata and djvu text (browser)"
LOG = [
    (B, "Reference editions: Haydn 1866, 1867, 1869, 1875, 1878, 1883, 1889, 1892, 1898, 1906; Chambers's 1860, "
        "1871, 1878, 1880 (Library of Universal Knowledge), 1925; Americana 1903, 1922, 1932", "1860-1932",
     "18 items", "18",
     "sd2-1866-haydn-moxon; sd2-1869-haydn-harper; sd2-1883-haydn-harper; sd2-1898-haydn-toronto; "
     "sd2-1871-chambers-lippincott; not usable: Haydn 1867 and 1906 copies (other titles), Library of Universal "
     "Knowledge vol. 3 and Chambers's 1925 vol. 4 (CRUSADES not in volume), Americana 1903 (wrong volume), 1932 "
     "(no text layer)"),
    (B, "Reference, church, national, scholarly and popular batch: Penny vol. 8, Pantologia vol. 4, Popular "
        "Encyclopedia vol. 4, Information for the People, Collier's 1921, Nelson's 1917, Schaff 1882, McClintock "
        "vol. 2, Mosheim (Reid), Neander vol. 4, Gieseler, Kurtz, Hardwick, Fisher, Alzog, Lingard vols. 2-3, Hume "
        "vol. 2, Student's Hume, Knight, Green, Tout's Edward the First, Krey, Paetow, CMH vol. 5, Thatcher and "
        "McNeal, Archer 1888, Archer and Kingsford (US), Wells, Van Loon, Abbott, RTS Crusades, Christian Brothers "
        "(Quebec), Irish primer, Mackay", "1833-1926", "36 items", "36",
     "28 rows or updates; not usable: Pantologia vol. 4 and Popular Encyclopedia vol. 4 (CRUSADE not in volume), "
     "McClintock vol. 2 (no CRUSADES headword), Gieseler and Knight (wrong volumes), Abbott (no text layer), Irish "
     "primer (no crusades)"),
    ("archive.org advancedsearch (browser)", "identifier searches for 54 reference, church, national, scholarly, "
                                             "popular, Irish and Canadian titles", "1800-1945", "54 queries", "54",
     "identifiers; none found for Beeton, Brewer, Blair, Dutton; La Monte search matched other authors"),
    (B, "Stebbing, History of Chivalry and the Crusades: all copies (historychivalry00/01/02/03stebgoog, "
        "dli.ministry.14023)", "1829-1830", "5 items", "5",
     "sd2-1830-stebbing-chivalry corrected; 02stebgoog duplicates vol. 1"),
]
L.append_log(D, LOG)

L.set_frame_status({
    "R09": ("read", "", "D2: vol. 8 confirms the 1837 row"),
    "R11": ("read", "sd2-1848-chambers-information", ""),
    "R12": ("read", "sd2-1871-chambers-lippincott", "D2: 1871 Philadelphia and 1878; 1925 vol. 4 lacks the article"),
    "R13": ("read", "sd2-1866-haydn-moxon;sd2-1869-haydn-harper;sd2-1883-haydn-harper;sd2-1898-haydn-toronto",
            "D2: list first seen 1866; D added to the sixth by 1883; H6 fourth to 1910"),
    "R08": ("read", "", "D2: 1829-33 table; 1922 printing confirms 1918/1924"),
    "R23": ("read", "sd2-1921-colliers-new", ""),
    "R24": ("read", "sd2-1917-nelsons-perpetual", ""),
    "R29": ("partial", "sd2-1882-schaff-religious-encyclopedia", "D2: 1882 vol. 1; New Schaff-Herzog vol. with "
                                                                 "CRUSADES not located"),
    "R30": ("not_reached", "", "D2: vol. 2 copy lacks the CRUSADES headword"),
    "R05": ("not_reached", "", "D2: vol. 4 copy is not the volume with CRUSADE"),
    "R10": ("not_reached", "", "D2: vol. 4 pt. 1 is not the volume with CRUSADES"),
    "R16": ("not_reached", "", "D2: no archive.org copy found by title search"),
    "R17": ("not_reached", "", "D2: no archive.org copy found by title search"),
    "R15": ("not_reached", "", "D2: no archive.org copy found by title search"),
    "C01": ("read", "sd2-1860-mosheim-reid", ""),
    "C03": ("read", "sd2-1872-neander-torrey", "D2: vol. 4"),
    "C04": ("not_reached", "", "D2: copy found is the wrong volume"),
    "C05": ("read", "sd2-1864-kurtz-history", ""),
    "C07": ("read", "sd2-1853-hardwick-middle-age", ""),
    "C09": ("read", "sd2-1887-fisher-church", ""),
    "C12": ("read", "sd2-1912-alzog-manual", ""),
    "C13": ("not_reached", "", "D2: only French editions found"),
    "C14": ("read", "sd2-1874-lingard-england", ""),
    "C16": ("read", "sd2-1854-hume-england;sd2-1859-students-hume", ""),
    "C17": ("not_reached", "", "D2: copy found is the wrong volume"),
    "C18": ("read", "sd2-1874-green-short-history", ""),
    "C19": ("read", "sd2-1893-tout-edward-first", ""),
    "H08": ("read", "sd2-1888-archer-crusade-richard", ""),
    "H11": ("read", "sd2-1921-krey-first-crusade", ""),
    "H12": ("not_reached", "", "D2: Newhall 1927 is a lending copy; not borrowed this session"),
    "H13": ("read", "sd2-1917-paetow-guide", ""),
    "H14": ("partial", "sd2-1926-cmh-v5", "D2: vol. 5 read; vols. 4 and 6 not located"),
    "H15": ("not_reached", "", "D2: title search found no copy"),
    "H16": ("not_reached", "", "D2: not searched this session"),
    "H17": ("read", "sd2-1905-thatcher-mcneal", ""),
    "H20": ("not_reached", "", "D2: only later works found"),
    "H22": ("not_reached", "", "D2: lending copy; not borrowed"),
    "P02": ("read", "", "D2 second pass: vol. 2 found and read"),
    "P05": ("read", "", "D2: ten-count from the index"),
    "P13": ("not_reached", "", "D2: no archive.org copy found"),
    "P24": ("read", "sd2-1920-wells-outline", ""),
    "P25": ("read", "sd2-1921-van-loon-story", ""),
    "P30": ("partial", "sd2-1850-rts-crusades", "D2: RTS The Crusades read; SPCK and ASSU titles not found"),
    "P31": ("not_reached", "", "D2: Abbott's Richard I has no usable text layer"),
    "S13": ("not_reached", "", "D2: no Irish National School reader with crusades found"),
    "S14": ("partial", "sd2-1875-christian-brothers-compendium", "D2: Quebec 1875 compendium; Irish class-books "
                                                                 "not found"),
})
print("block 3 written")
