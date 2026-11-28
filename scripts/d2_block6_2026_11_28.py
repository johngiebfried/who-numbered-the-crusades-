"""Strand D2, block 6 (28 November 2026): the second pass over the 'ninth crusade' hits, Langer, the US and
British college textbooks that number only to the Fifth, Nuttall and the Edinburgh Encyclopaedia.
Same conventions as blocks 2-5. The work-level record of the ninth-crusade hits is
data/strand_d2/ninth_crusade_hits_by_work.csv (written by hand from the browser pass). MIT License.
"""
import d2_lib as L

D = "2026-11-28"
TXT = "archive.org djvu text via built-in browser"
IA = "https://archive.org/details/"
SNIP = "archive.org full-text search hit, context read in the djvu text (browser)"


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


def ninth(wid, label, author, work, year, place, tradition, genre, frame, slots, quote, ident, country, notes,
          level="snippet"):
    """A row found through the ninth-crusade sweep: only the ninth (and any slot stated beside it) is coded."""
    return new(wid, label=label, author=author, work=work, year_label=year, year_sort=year[:4],
               place_publisher=place, tradition=tradition, genre=genre, census_frame=frame, enumerates="partial",
               quote=quote, url=IA + ident, verification_level=level, title_page_checked="no", country=country,
               how_verified=SNIP, notes=notes, **slots)


W = cur()
works = [
    new("sd2-1940-langer-encyclopedia", label="W. L. Langer (ed.), An Encyclopedia of World History",
        author="William L. Langer (ed.)", work="An Encyclopedia of World History", year_label="1940",
        year_sort="1940", place_publisher="Boston: Houghton Mifflin; London: Harrap", tradition="US",
        genre="Reference", census_frame="d2_reference_en", enumerates="yes", C="4", D="5", F="6", L1="7",
        L2="8", E="8", stated_count="8", scheme_family="modern_eight", signature_match="no",
        stemma_parent="1883-carl-ploetz", parent_evidence="documented: Langer's work revised Ploetz's Epitome",
        quote="1218-1221. THE FIFTH CRUSADE ... 1228-1229. THE SIXTH CRUSADE, of the Emperor Frederick II ... "
              "1248-1254. THE SEVENTH CRUSADE ... 1270. THE EIGHTH CRUSADE",
        url=IA + "dli.ernet.15877", verification_level="full_text", title_page_checked="no", country="US",
        notes="Read in a DLI copy of the Harrap issue (encyclopediaofwo00lang has no text). The Barons' crusade "
              "(1239-41) is unnumbered; the eighth is 'the second of King Louis IX and Edward of England'. "
              "Langer's successor to Ploetz drops Ploetz's Frederick-fifth seven for the modern eight. Read for "
              "numbering only."),
    new("sd2-1885-fisher-outlines-universal", label="G. P. Fisher, Outlines of Universal History",
        author="George Park Fisher", work="Outlines of Universal History", year_label="1885", year_sort="1885",
        place_publisher="New York and Chicago: Ivison, Blakeman, Taylor", tradition="US", genre="School",
        census_frame="d2_school_en", enumerates="yes", C="4", F="5", L1="6", L2="7",
        scheme_family="frederick_fifth_seven", signature_match="no",
        quote="Fourth Crusade (1202-1204) ... Fifth Crusade (1228-1229) ... Sixth Crusade (1248-1254): Seventh "
              "Crusade (1270)",
        url=IA + "outlinesofuniver00fish_0", verification_level="full_text", title_page_checked="yes (OCR)",
        country="US",
        notes="College and high-school text by Yale's church historian. Same count as Ploetz's Epitome in "
              "Tillinghast's translation (1883); no citation of Ploetz checked."),
    new("sd2-1889-myers-general-history", label="P. V. N. Myers, A General History for Colleges and High Schools",
        author="Philip Van Ness Myers", work="A General History for Colleges and High Schools; General History",
        year_label="1889 (read 1906 and 1921 printings)", year_sort="1889",
        place_publisher="Boston: Ginn", tradition="US", genre="School", census_frame="d2_school_en",
        enumerates="partial", C="4", scheme_family="", signature_match="no",
        quote="448. The Fourth Crusade (1202-1204); Capture of Constantinople by the Latins",
        url=IA + "generalhistory00myer", verification_level="full_text", title_page_checked="yes (OCR)",
        country="US",
        notes="Read in the 1906 (generalhistoryfo0000myer) and 1921 (generalhistory00myer) printings. Numbers the "
              "first three, the Fourth, and 'the interval between the Fourth and the Fifth Crusade'; the later "
              "expeditions are not numbered. The 1921 printing calls Pears 'the best account' of the Fourth. "
              "Myers's longer Outlines of Mediaeval and Modern History has the modern eight (1885-p-v-n-myers)."),
    new("sd2-1916-previte-orton-outlines", label="C. W. Previté-Orton, Outlines of Medieval History",
        author="C. W. Previté-Orton", work="Outlines of Medieval History", year_label="1916", year_sort="1916",
        place_publisher="Cambridge: Cambridge University Press", tradition="Britain", genre="Scholarship",
        census_frame="d2_scholarly_en", enumerates="partial", C="4", D="5", scheme_family="",
        signature_match="no",
        quote="After the perversion of the Fourth Crusade ... designed the Fifth Crusade against Saphadin",
        url=IA + "in.ernet.dli.2015.79791", verification_level="full_text", title_page_checked="yes (OCR)",
        country="GB",
        notes="Numbers to the Fifth, then by leader: the Tunis expedition 'was the last Crusade'; 'The crusade, in "
              "which Edward had intended to take part, was the second led by St Louis'. His History of Europe "
              "1198-1378 (Methuen, 1937; dli.ernet.2260) has the same practice ('the Fifth Crusade, recovery of "
              "Jerusalem by Frederick II', 'St. Louis' first Crusade', 'St. Louis' second Crusade'): read for "
              "numbering only."),
    new("sd2-1898-oman-art-of-war", label="C. W. C. Oman, A History of the Art of War in the Middle Ages",
        author="C. W. C. Oman", work="A History of the Art of War in the Middle Ages",
        year_label="1898 (read in the 2nd ed., 1924)", year_sort="1898", place_publisher="London: Methuen",
        tradition="Britain", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial",
        C="4", D="5", scheme_family="", signature_match="no",
        quote="First Crusade ... Fourth Crusade, ii. 305-315; Fifth Crusade, i. 265-267; Crusade of St. Louis",
        url=IA + "historyofartofwa0000char_v0d0", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="Index of the 1924 edition (vol. 2) and text of vol. 1 (isbn_0416717608, a reprint of the 1924 text): "
              "'during the fifth Crusade' (Damietta, 1220); Louis's expeditions are 'Crusade of St. Louis'. The "
              "1898 first edition not read. The 1885 prize essay has no crusade numbers."),
    new("sd2-1923-nuttall-encyclopaedia", label="The Nuttall Encyclopaedia (1923 and 1930 printings)",
        author="[ed. G. Elgie Christ; first ed. P. Austin Nuttall]", work="The Nuttall Encyclopaedia",
        year_label="1923; 1930", year_sort="1923", place_publisher="London: Frederick Warne", tradition="Britain",
        genre="Reference", census_frame="d2_reference_en", enumerates="yes", C="4", L1="7", L2="8",
        stated_count="8", scheme_family="modern_eight", signature_match="no",
        stemma_parent="1907-nuttall-encyclopaedia", parent_evidence="documented: later printing",
        quote="to the number of eight ... The Fourth (1202-1204), under sanction of Pope Innocent III ... The Seventh "
              "(1248-1254) ... The Eighth (1270)",
        url=IA + "in.ernet.dli.2015.96577", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="DLI copies of 1923 and 1930 (in.ernet.dli.2015.59270). The fifth and sixth entries were not "
              "captured by the OCR search; the seventh and eighth fix the modern eight. The 1907 row has the same "
              "opening ('to the number of eight')."),
    new("sd2-1830-edinburgh-encyclopaedia", label="The Edinburgh Encyclopaedia (Brewster), CRUSADES",
        author="David Brewster (ed.)", work="The Edinburgh Encyclopaedia, vol. 5 (article CRUSADES)",
        year_label="1830 (London issue; first published 1808-30)", year_sort="1830",
        place_publisher="Edinburgh: Blackwood; London", tradition="Britain", genre="Reference",
        census_frame="d2_reference_en", enumerates="no", scheme_family="none",
        quote="Edward the First, who had himself engaged in the last crusade",
        url=IA + "edinburghencycl05encygoog", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="An essay on causes and effects; no crusade numbers in the article. The 1832 Philadelphia reprint was "
              "not checked."),
    new("sd2-1893-colvin-godeffroy", label="Godeffroy of Boloyne, ed. Mary Noyes Colvin (EETS)",
        author="Mary Noyes Colvin (ed.)", work="Godeffroy of Boloyne; or, The Siege and Conqueste of Jerusalem "
                                               "(Early English Text Society, Extra Series 64)",
        year_label="1893", year_sort="1893", place_publisher="London: Early English Text Society",
        tradition="Britain", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial", E="9",
        quote="A narration of the prowesses of Prince Edward, son of Henry III., and of the events of the Ninth "
              "Crusade",
        url=IA + "godeffroyofboloy00willrich", verification_level="snippet", title_page_checked="no",
        country="GB", how_verified=SNIP,
        notes="Editor's description of a manuscript's contents. An Edward-centred ninth in a scholarly edition."),
    new("sd2-1857-masonic-knights-east-west", label="Masonic degree history of the Knights of the East and West",
        author="[Masonic manuals; J. Yarker 1872]",
        work="The Indian Freemason's Friend (1857); J. Yarker, Notes on the Scientific and Religious Mysteries of "
             "Antiquity (1872)",
        year_label="1857; 1872", year_sort="1857", place_publisher="Calcutta; London", tradition="Britain",
        genre="Other", census_frame="d2_popular_en", enumerates="partial", E="9",
        quote="After the ninth crusade, A.D. 1272, the Institution of Knights of the East and West",
        url=IA + "dli.bengal.10689.14208", verification_level="snippet", title_page_checked="no", country="GB",
        how_verified=SNIP,
        notes="Degree lore: after 'the ninth crusade, A.D. 1272', 'King Edward I.' dubs the knights. Yarker's text: "
              "notesonscientif00junrgoog. A channel outside history-writing for a ninth dated by Edward's return."),
    ninth("sd2-1836-wallen-round-church", "W. Wallen, The Round Church at Little Maplestead", "William Wallen",
          "The History and Antiquities of the Round Church at Little Maplestead, Essex", "1836", "London",
          "Britain", "Church and national history", "d2_church_en", dict(L2="9", E="9"),
          "THE NINTH CRUSADE. CHAPTER VI. A.D. 1267. HENRY III.", "historyantiquiti00wall", "GB",
          "Hospitaller history; chapter VI is headed 'The Ninth Crusade' and opens in 1267 under Henry III. Louis "
          "is named in the chapter; the earlier chapters' numbers were not read."),
    ninth("sd2-1851-colquhoun-civil-law", "P. Colquhoun, A Summary of the Roman Civil Law",
          "Patrick MacChombaich de Colquhoun", "A Summary of the Roman Civil Law", "1851", "London", "Britain",
          "Other", "d2_popular_en", {}, "The ninth Crusade was determined on in the second Council at Lyons",
          "ASummaryOfTheRomanCivilLawV1", "GB",
          "The ninth is Gregory X's projected crusade of 1274 (Second Council of Lyons). Not coded to a slot."),
    ninth("sd2-1860-hazlitt-venetian-republic", "W. C. Hazlitt, History of the Venetian Republic",
          "W. Carew Hazlitt", "History of the Venetian Republic: her Rise, her Greatness, and her Civilization",
          "1860", "London: Smith, Elder", "Britain", "Popular history", "d2_popular_en", dict(L2="9"),
          "episode in the history of France, known as the Ninth Crusade", "historyvenetian01hazlgoog", "GB",
          "Under 1268, 'Venice helps Saint Louis'. Same phrase in the 1900 and 1915 editions (The Venetian "
          "Republic)."),
    ninth("sd2-1864-reading-book-evening-schools", "A Reading Book for Evening Schools", "[C. K.]",
          "A Reading Book for Evening Schools", "1864", "London", "Britain", "School", "d2_school_en",
          dict(L1="8", L2="9"), "Louis IX. of France, surnamed S. Louis, was one of the leaders in the eighth and "
                                "ninth Crusades", "areadingbookfor00unkngoog", "GB",
          "Editor's note to a reading passage on Louis's return from the eighth."),
    ninth("sd2-1887-johonnot-ten-great-events", "James Johonnot, Ten Great Events in History", "James Johonnot",
          "Ten Great Events in History", "1887", "New York: D. Appleton", "US", "School", "d2_school_en",
          dict(L2="9"), "THE NINTH CRUSADE. 70. Some eight years later the tidings that Antioch had",
          "tengreateventsin00joho", "US",
          "Appleton's Instructive Reading Books. The heading covers the fall of Antioch (1268) and Tunis; Edward not "
          "read."),
    ninth("sd2-1890-beazley-james-aragon", "C. R. Beazley, James the First of Aragon", "C. Raymond Beazley",
          "James the First of Aragon (Stanhope/Lothian essay)", "1890", "Oxford: Blackwell", "Britain",
          "Scholarship", "d2_scholarly_en", {}, "to preach a ninth crusade up and down his land, at the Council of "
                                                "Lyons", "jamesfirstofarag00beaz", "GB",
          "The ninth is the crusade projected at Lyons in 1274. Not coded to a slot."),
    ninth("sd2-1896-howells-impressions", "W. D. Howells, Impressions and Experiences", "W. D. Howells",
          "Impressions and Experiences", "1896", "New York: Harper", "US", "Other", "d2_popular_en", {},
          "the amusing aspects of the Ninth Crusade, which the Venetians so cannily turned aside",
          "impressionsandex00howerich", "US",
          "First printed in Harper's Weekly, 19 October 1895. The 'ninth' is the crusade of 1202-04: a slip or a "
          "joke, not a scheme. Not coded to a slot."),
    ninth("sd2-1905-chronological-chart", "A Chronological Chart of European History", "",
          "A Chronological Chart of European History", "1905", "", "US", "Reference", "d2_reference_en",
          dict(L2="9"), "Seventh Crusade. Eighth, Crusade. Ninth Crusade.", "cu31924031005402", "US",
          "Wall chart; 1248 beside the eighth and 1270 beside the ninth (nine-crusade count with Louis's two as "
          "eighth and ninth)."),
    ninth("sd2-1934-daily-express-encyclopaedia", "The Daily Express Encyclopaedia", "",
          "The Daily Express Encyclopaedia, vol. 4", "1934", "London: Daily Express", "Britain", "Reference",
          "d2_reference_en", dict(L1="9"), "the history of the Ninth Crusade by Joinville",
          "in.ernet.dli.2015.108581", "GB",
          "In the article on French literature: Joinville's crusade (1248-54) as the ninth, as in Mackay, W. C. "
          "Taylor, G. A. Smith and Blyth. The CRUSADES article itself was not located."),
    ninth("sd2-1944-anderson-biography-cathedral", "R. G. Anderson, The Biography of a Cathedral",
          "Robert Gordon Anderson", "The Biography of a Cathedral", "1944", "New York: Longmans", "US",
          "Popular history", "d2_popular_en", {}, "XIII. Ninth Crusade, 1344 ... XIV. Tenth Crusade, 1353",
          "in.ernet.dli.2015.78269", "US",
          "A long count running into the fourteenth century (Smyrna 1344). Read for the numbering only; earlier "
          "items of the list not read."),
]
L.upsert_works(works)

W = cur()
upd = [
    dict(work_id="1885-p-v-n-myers",
         notes=app("1885-p-v-n-myers", "notes",
                   "[D2 2026-11-28] 1897 printing (outlinesofmediva00myer): 'The Fifth Crusade (1216-1220)', 'The "
                   "Sixth Crusade (1227-1229), headed by Frederick II.', 'The Seventh Crusade (1249-1254)', 'The Eighth "
                   "Crusade (1270-1272)' with Louis and Prince Edward as 'the two principal leaders'; Henry VI's army "
                   "of 1195-98 in a footnote.", W)),
    dict(work_id="1883-carl-ploetz",
         notes=app("1883-carl-ploetz", "notes",
                   "[D2 2026-11-28] Revised printing 1905 (epitomeofancient04ploe) unchanged: 1202-1204 Fourth, "
                   "1228-1229 Fifth, 1248-1254 Sixth, 1270 Seventh.", W)),
    dict(work_id="sd2-1882-gilbert-world-toronto",
         notes=app("sd2-1882-gilbert-world-toronto", "notes",
                   "The 1886 printing (worldhistoricala00gilb) reads 'a ninth Crusade' where the Toronto 1882 "
                   "printing reads 'an eighth Crusade' (a projected crusade after 1272).", W)),
    dict(work_id="sd2-1883-lupton-concise",
         notes=app("sd2-1883-lupton-concise", "notes",
                   "The first classifier pass labeled this hit a metaphor; the context is Edward's crusade.", W)),
]
L.upsert_works(upd)

W = cur()


def attr(wid, **kw):
    kw["work_id"] = wid
    kw.setdefault("checked_on", D)
    if wid in W and "gibbon_numbers" not in kw:
        kw["gibbon_numbers"] = L.gibbon_numbers(W[wid])
    return kw


A = [
    attr("sd2-1940-langer-encyclopedia", frame_id="R32", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="D", edward_status="inside_last", gibbon_cited="unchecked", numbers_follow="modern;inferred",
         notes="Successor to Ploetz; drops Ploetz's count."),
    attr("sd2-1885-fisher-outlines-universal", frame_id="S26", country_pub="US", author_origin="US",
         fourth_identity="C", fifth_identity="F", edward_status="absent", gibbon_cited="unchecked",
         numbers_follow="german;inferred", notes="Ploetz's count (inferred)."),
    attr("sd2-1889-myers-general-history", frame_id="S25", country_pub="US", author_origin="US",
         fourth_identity="C", fifth_identity="D", edward_status="", gibbon_cited="unchecked",
         sources_named="Pears", numbers_follow="modern;inferred", notes="Numbers only through the Fifth."),
    attr("sd2-1916-previte-orton-outlines", frame_id="H20", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="last_unnumbered", gibbon_cited="unchecked",
         numbers_follow="modern;inferred", notes="Numbers only through the Fifth."),
    attr("sd2-1898-oman-art-of-war", frame_id="H16", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="", gibbon_cited="unchecked",
         numbers_follow="modern;inferred", notes="Numbers only through the Fifth (1924 text)."),
    attr("sd2-1923-nuttall-encyclopaedia", frame_id="R27", country_pub="England", fourth_identity="C",
         fifth_identity="", edward_status="", gibbon_cited="none", numbers_follow="modern;inferred"),
    attr("sd2-1830-edinburgh-encyclopaedia", frame_id="R03", country_pub="Scotland", fourth_identity="none",
         fifth_identity="none", edward_status="last_unnumbered", gibbon_cited="unchecked",
         numbers_follow="unclear;inferred"),
    attr("sd2-1893-colvin-godeffroy", frame_id="", country_pub="England", author_origin="US", fourth_identity="none",
         fifth_identity="none", edward_status="ninth_alone", ninth_referent="edward", gibbon_cited="unchecked",
         numbers_follow="unclear;inferred", notes="Edward-centred ninth; whether Louis's Tunis is separate is not "
                                                  "stated. Added during reading (ninth sweep)."),
    attr("sd2-1857-masonic-knights-east-west", frame_id="", country_pub="England", fourth_identity="none",
         fifth_identity="none", edward_status="ninth_alone", ninth_referent="edward", gibbon_cited="none",
         numbers_follow="unclear;inferred", notes="Masonic lore; ninth dated 1272 (Calcutta 1857; London 1872). Added during reading (ninth sweep)."),
    attr("sd2-1836-wallen-round-church", frame_id="", country_pub="England", fourth_identity="",
         fifth_identity="", edward_status="ninth_with_tunis", ninth_referent="tunis+edward",
         gibbon_cited="unchecked", numbers_follow="unclear;inferred", notes="Added during reading (ninth sweep)."),
    attr("sd2-1851-colquhoun-civil-law", frame_id="", country_pub="England", fourth_identity="none",
         fifth_identity="none", edward_status="absent", ninth_referent="other", gibbon_cited="unchecked",
         numbers_follow="unclear;inferred", notes="Ninth = Gregory X's projected crusade (1274)."),
    attr("sd2-1860-hazlitt-venetian-republic", frame_id="", country_pub="England", fourth_identity="",
         fifth_identity="", edward_status="", ninth_referent="tunis", gibbon_cited="unchecked",
         numbers_follow="unclear;inferred", notes="Added during reading (ninth sweep)."),
    attr("sd2-1864-reading-book-evening-schools", frame_id="", country_pub="England", fourth_identity="",
         fifth_identity="", edward_status="", ninth_referent="tunis", gibbon_cited="unchecked",
         numbers_follow="unclear;inferred", notes="Added during reading (ninth sweep)."),
    attr("sd2-1887-johonnot-ten-great-events", frame_id="", country_pub="US", author_origin="US",
         fourth_identity="", fifth_identity="", edward_status="", ninth_referent="tunis",
         gibbon_cited="unchecked", numbers_follow="unclear;inferred", notes="Added during reading (ninth sweep)."),
    attr("sd2-1890-beazley-james-aragon", frame_id="", country_pub="England", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="absent", ninth_referent="other",
         gibbon_cited="unchecked", numbers_follow="unclear;inferred", notes="Ninth = the crusade projected at Lyons."),
    attr("sd2-1896-howells-impressions", frame_id="", country_pub="US", author_origin="US", fourth_identity="none",
         fifth_identity="none", edward_status="absent", ninth_referent="other", gibbon_cited="none",
         numbers_follow="unclear;inferred", notes="'Ninth' applied to 1202-04."),
    attr("sd2-1905-chronological-chart", frame_id="", country_pub="US", fourth_identity="",
         fifth_identity="", edward_status="", ninth_referent="tunis", gibbon_cited="none",
         numbers_follow="unclear;inferred", notes="Added during reading (ninth sweep)."),
    attr("sd2-1934-daily-express-encyclopaedia", frame_id="", country_pub="England", fourth_identity="",
         fifth_identity="", edward_status="", ninth_referent="other",
         gibbon_cited="unchecked", numbers_follow="unclear;inferred", notes="Ninth = Joinville's crusade, Louis IX's first (1248)."),
    attr("sd2-1944-anderson-biography-cathedral", frame_id="", country_pub="US", author_origin="US",
         fourth_identity="", fifth_identity="", edward_status="", ninth_referent="other",
         gibbon_cited="unchecked", numbers_follow="own;inferred", notes="Ninth = 1344 (Smyrna)."),
]
L.upsert_attrs(A)

L.append_citations([
    dict(citing_work_id="sd2-1889-myers-general-history", cited="1885-edwin-pears", relation="bibliography",
         evidence="'Pears, E., The Fall of Constantinople (the best account'", confidence="documented"),
    dict(citing_work_id="sd2-1940-langer-encyclopedia", cited="1883-carl-ploetz", relation="revision of",
         evidence="Langer's Encyclopedia was prepared as the successor to Ploetz's Epitome", confidence="documented"),
])

B = "archive.org metadata and djvu text (browser)"
L.append_log(D, [
    ("archive.org full-text search (browser)", "\"ninth crusade\", second pass: the 202 hits the first pass left "
                                               "unclassified plus 17 further 1900s hits, context read in the djvu "
                                               "text", "1800-1949", "219", "219",
     "data/strand_d2/ninth_crusade_hits_by_work.csv (87 work groups, 441 copies to 1945); 12 new rows"),
    ("archive.org advancedsearch (browser)", "Edinburgh Encyclopaedia; Encyclopaedia Perthensis; Encyclopaedia "
                                             "Londinensis; Everyman's Encyclopaedia; Harmsworth; Nuttall; New "
                                             "International 1914-30; Johnson's; Americana 1903-12; Chambers's "
                                             "1886-1935; Langer; Ploetz; Myers; Fisher; Previté-Orton; Oman; Mee",
     "1806-1948", "15 queries, up to 40 each", "about 400",
     "candidate volumes for the CRUSADES headword; Harmsworth not found"),
    (B, "CRUSADES headword in 23 encyclopedia volumes (Edinburgh 1830 and 1832, Perthensis 1816, Londinensis "
        "1810, Everyman's 1913-14, Nuttall 1900/1923/1930, Americana 1904, New International 1917, Johnson's "
        "1876/1881, Chambers's 1888/1901/1923)", "1810-1930", "23 volumes", "23",
     "found in Edinburgh vol. 5 (no numbers) and Nuttall 1923/1930 (eight); the others did not match the "
     "uppercase-headword search (OCR, case or wrong volume), Everyman's vol. 4 has no text: not reached"),
    (B, "Single volumes: Langer 1940 (two copies), Myers 1897/1906/1921, Fisher 1885, Previté-Orton 1916 and "
        "1937, Oman 1885 and 1924, CMH vol. 6, Ploetz 1905", "1885-1940", "13 items", "13",
     "sd2-1940-langer-encyclopedia; sd2-1885-fisher-outlines-universal; sd2-1889-myers-general-history; "
     "sd2-1916-previte-orton-outlines; sd2-1898-oman-art-of-war; CMH vol. 6 copy has no usable text"),
])
L.set_frame_status({
    "R03": ("partial", "sd2-1830-edinburgh-encyclopaedia", "D2: vol. 5 (London issue 1830) read; no numbers"),
    "R02": ("not_reached", "", "D2: vol. 6 of the 1816 edition has CRUSADE 'See CROISADE'; the CROISADE article "
                               "was not located"),
    "R04": ("not_reached", "", "D2: vols. 5 and 6 (1810) checked; headword not located"),
    "R26": ("not_reached", "", "D2: 1913-14 vols. 3-4 checked; vol. 4 has no text layer"),
    "R25": ("not_reached", "", "D2: no archive.org copy found by title search"),
    "R27": ("read", "sd2-1923-nuttall-encyclopaedia", "D2: 1923 and 1930 printings"),
    "R32": ("read", "sd2-1940-langer-encyclopedia", "D2: Ploetz 1905 unchanged; Langer 1940 modern eight"),
    "S25": ("read", "sd2-1889-myers-general-history", "D2: Outlines 1897; General History 1906 and 1921"),
    "S26": ("read", "sd2-1885-fisher-outlines-universal", "D2: 1885"),
    "H16": ("read", "sd2-1898-oman-art-of-war", "D2: 1924 text"),
    "H20": ("read", "sd2-1916-previte-orton-outlines", "D2: 1916 and 1937"),
})
print("block 6 written")
