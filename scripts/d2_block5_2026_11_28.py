"""Strand D2, block 5 (28 November 2026): Ireland and Canada, the archive.org title census, and further
popular and scholarly works (Newman's Manual, Newhall, Coulton, Adams, Boyd, Gibbon's separately printed
crusade chapters). Same conventions as blocks 2-3. Writes data/strand_d2/census_archiveorg_titles.csv.
MIT License.
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


W = cur()
works = [
    # Ireland
    dict(work_id="sd2-1874-lingard-england", place_publisher="Dublin: James Duffy", tradition="Ireland",
         country="IE",
         notes=app("sd2-1874-lingard-england", "notes", "Imprint of the copy read: Dublin, J. Duffy, 1874.", W)),
    new("sd2-1854-newman-turks", label="J. H. Newman, Lectures on the History of the Turks",
        author="John Henry Newman", work="Lectures on the History of the Turks in its Relation to Christianity",
        year_label="1854", year_sort="1854", place_publisher="Dublin: James Duffy", tradition="Ireland",
        genre="Church and national history", census_frame="d2_church_en", enumerates="no", scheme_family="none",
        url=IA + "LecturesOnHistoryOfTheTurks", verification_level="full_text", title_page_checked="no",
        country="IE",
        notes="Lectures given in Liverpool, printed in Dublin while Newman was rector of the Catholic University. No "
              "crusade numbers; footnotes cite Gibbon ten times."),
    new("sd2-1837-reeve-church-dublin", label="Joseph Reeve, A Short View of the History of the Christian Church",
        author="Joseph Reeve", work="A Short View of the History of the Christian Church",
        year_label="1837 (Dublin printing)", year_sort="1837", place_publisher="Dublin: R. Grace",
        tradition="Ireland", genre="Church and national history", census_frame="d2_church_en",
        enumerates="partial", H6="4",
        quote="Pope Celestine announced to the Christian world a fourth crusade",
        url=IA + "historyofthechri00reevuoft", verification_level="full_text",
        title_page_checked="no (metadata: Dublin, R. Grace, 1837)", country="IE",
        notes="English Catholic church history (first published York, 1802-03), here in a Dublin printing. Section "
              "X: 'Last Crusades under St. Lewis, King of France'."),
    # Canada
    new("sd2-1872-collier-outlines-toronto", label="W. F. Collier, Outlines of General History (Toronto)",
        author="William Francis Collier", work="Outlines of General History (British-American Series of School "
                                               "Books)",
        year_label="1872", year_sort="1872", place_publisher="Toronto: James Campbell", tradition="Canada",
        genre="School", census_frame="d2_school_en", enumerates="yes", H6="4", C="5", F="6", L1="7", L2="8",
        scheme_family="moreri_eight", signature_match="no", stemma_parent="sd-1860-collier-great-events",
        parent_evidence="inferred: same author and count",
        quote="5. The soldiers of the Fifth Crusade never reached Jerusalem. Dandolo, Doge of Venice ... 6. Frederic "
              "II. of Germany headed the Sixth Crusade ... 7. The Seventh Crusade was led by Saint Louis IX.",
        url=IA + "outlinesofgenera00colluoft", verification_level="full_text", title_page_checked="no",
        country="CA",
        notes="The fourth ends with 'the ignominious flight of the Crusaders from the siege of Thoron' (1197). '8. "
              "Saint Louis went upon an Eighth Crusade to Africa ... Edward I. of England, then only Prince Edward, "
              "afterwards led his Crusaders to the Holy Land'. Also 1869 Campbell printing (outlinesofgener00coll)."),
    new("sd2-1882-gilbert-world-toronto", label="Frank Gilbert, The World, Historical and Actual (Toronto)",
        author="Frank Gilbert", work="The World, Historical and Actual", year_label="1882", year_sort="1882",
        place_publisher="Toronto: C. R. Parish", tradition="Canada", genre="Reference",
        census_frame="d2_reference_en", enumerates="partial", C="4", D="5", L2="7", E="7",
        quote="Fifth Crusade ... 1216-1220 ... Seventh Crusade ... 1270",
        url=IA + "cihm_28802", verification_level="full_text", title_page_checked="no (metadata: Toronto, C. R. "
                                                                                     "Parish, 1882)",
        country="CA",
        notes="Chronological tables; 'until the fourth Crusade (1203)'. The crusade of 1270-72: 'St. Louis began it, "
              "but he soon died, and the leadership fell upon Edward of England'. Gibbon's L2 7. An American author's "
              "subscription book in a Toronto printing."),
    new("sd2-1878-thompson-england-toronto", label="Edith Thompson, History of England (Toronto)",
        author="Edith Thompson", work="History of England (Freeman's Historical Course; Campbell's Educational "
                                      "Series)",
        year_label="1878", year_sort="1878", place_publisher="Toronto: James Campbell", tradition="Canada",
        genre="School", census_frame="d2_school_en", enumerates="no", scheme_family="none",
        url=IA + "n1006historyofen00thom", verification_level="full_text", title_page_checked="no", country="CA",
        notes="'Edward and Edmund set off upon what proved to be the last Crusade'."),
    new("sd2-1886-adam-robertson-toronto", label="Adam and Robertson, Public School History of England and Canada",
        author="G. Mercer Adam; W. J. Robertson", work="Public School History of England and Canada",
        year_label="1886", year_sort="1886", place_publisher="Toronto: Copp, Clark", tradition="Canada",
        genre="School", census_frame="d2_school_en", enumerates="no", scheme_family="none",
        url=IA + "publicscho86west00adam", verification_level="full_text", title_page_checked="no", country="CA",
        notes="Authorized Ontario text. No crusade numbers. The 1891 High School History of England (Buckley and "
              "Robertson; highschool91west00buck) and the Ontario High School History of England (Wrong, 1915; "
              "ontariohighschoo00wron) also have none."),
    # popular and scholarly
    dict(work_id="1899-a-h-newman", author="Albert Henry Newman", label="A. H. Newman, A Manual of Church History",
         work="A Manual of Church History, vol. 1", year_label="1899 (read 1900 printing)",
         place_publisher="Philadelphia: American Baptist Publication Society", H6="4", C="5", D="6", F="6", B="7",
         L1="8", L2="9", E="9", scheme_family="nine_H6", signature_match="no", verification_level="full_text",
         quote="(3) The Fourth Crusade (1196-1197) ... (4) The Fifth Crusade (1201-1204) ... (8) The Ninth Crusade "
               "(1259-1291) embraces several feeble expeditions",
         url=IA + "manualofchurchhi01newm", how_verified=TXT, access=TXT, title_page_checked="no", country="US",
         research_pass="review;strand_d2", checked_on=D,
         notes=app("1899-a-h-newman", "notes",
                   "[D2 2026-11-28] Read in the 1899 and 1900 printings (manualofchurchhi0001albe; "
                   "manualofchurchhi01newm): 'The Sixth Crusade (1216-1229)', with Frederick II; 'The Seventh Crusade "
                   "(1239-1242) was made up of a French and English expedition'; 'The Eighth Crusade (1248) was led by "
                   "Louis IX.'; the ninth covers 1259-1291, Tunis and Edward inside it. Confirms the paper's table.",
                   W)),
    new("sd2-1883-adams-wars-of-cross", label="W. H. Davenport Adams, The Wars of the Cross",
        author="William Henry Davenport Adams", work="The Wars of the Cross; or, The History of the Crusades",
        year_label="1883 (copy read; the paper dates it 1886)", year_sort="1883", place_publisher="London",
        tradition="Britain", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        C="4", D="5", B="6", L1="7", L2="8", E="8", scheme_family="barons_sixth", signature_match="no",
        quote="The Fifth (or Sixth) Crusade 1216-1220 ... The Sixth Crusade* 1240-1241 ... The Eighth Crusade. "
              "1270-1272",
        url=IA + "warscrossorhist00adamgoog", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="Slots from the chronological tables, which give alternatives in parentheses ('The Fifth (or Sixth) "
              "Crusade') and a footnote on the Barons' crusade (reasons r41). The narrative heads differ: 'Pope "
              "Celestine III. proclaimed the Fourth Crusade' over Henry VI's expedition and 'The Fifth Crusade' over "
              "1202-04 (the paper's table codes the narrative). The table's eighth includes Edward (Acre 1271). Quotes "
              "Gibbon."),
    new("sd2-1892-boyd-story", label="J. P. Boyd, Story of the Crusades", author="James P. Boyd",
        work="Story of the Crusades", year_label="1892", year_sort="1892", place_publisher="Philadelphia: P. W. "
                                                                                          "Ziegler",
        tradition="US", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        H6="4", C="5", D="6", L1="7", L2="8", E="8", scheme_family="moreri_eight", signature_match="no",
        quote="PART IV. FOURTH CRUSADE. Death of Saladin ... PART V. FIFTH CRUSADE. I. Siege of Constantinople",
        url=IA + "storyofcrusadesw00boyd", verification_level="full_text", title_page_checked="no", country="US",
        notes="Parts: IV Fourth (Henry VI; 'End of Fourth'), V Fifth (Constantinople), VI Sixth (famine, John of "
              "Brienne, the Children's Crusade), VII Seventh (Gaza 1244, Louis IX), VIII Eighth (Tunis; Prince Edward "
              "inside it). Subscription book. Michaud's count."),
    new("sd2-1869-gibbon-crusades-extract", label="Gibbon, The Crusades (separately printed chapters)",
        author="Edward Gibbon", work="The Crusades, A.D. 1095-1261 (chapters 57-61 of Decline and Fall)",
        year_label="1869", year_sort="1869", place_publisher="London: Alex. Murray and Son (Murray's Reprints)",
        tradition="Britain", genre="Popular history", census_frame="d2_popular_en", enumerates="yes",
        C="4", D="5", scheme_family="gibbon_seven", signature_match="no", stemma_parent="1788-edward-gibbon",
        parent_evidence="documented: reprint of the chapters",
        quote="The fourth crusade (A.D. 1203) was diverted from Syria to Constantinople",
        url=IA + "crusadesad00gibbgoog", verification_level="full_text",
        title_page_checked="yes (OCR: CRUSADES. A.D. 1095-1261. EDWARD GIBBON ... LONDON: ALEX: MURRAY AND SON ... "
                           "1869)",
        country="GB",
        notes="Gibbon's chapters printed as a crusade history, with Gibbon's numbering (running head 'THE FOURTH AND "
              "FIFTH CRUSADES'). The same text with Kaye's Siege of Rhodes and Scott's Essays on Chivalry "
              "(crusades00scotgoog, c. 1870). This is the 'Gibbon's History of the Crusades' of Conder's "
              "bibliography (1897)."),
    new("sd2-1927-newhall-crusades", label="R. A. Newhall, The Crusades (Berkshire Studies)",
        author="Richard A. Newhall", work="The Crusades (Berkshire Studies in European History)",
        year_label="1927", year_sort="1927", place_publisher="New York: Henry Holt", tradition="US",
        genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial", C="4",
        quote="The Fourth Crusade 61 Venice and the crusaders. Capture of Constantinople, the Latin Empire",
        url=IA + "in.ernet.dli.2015.186685", verification_level="full_text", title_page_checked="no",
        country="US",
        notes="Read in a DLI copy (the archive.org copy crusades0000newh is a lending copy). Contents number the "
              "Fourth only after the Third; 'The new and last crusade organized in 1270 by Louis IX'. Cites Gibbon, "
              "Munro, Barker, Bréhier, Stevenson. Read for numbering only."),
    new("sd2-1925-wright-geographical-lore", label="J. K. Wright, The Geographical Lore of the Time of the Crusades",
        author="John Kirtland Wright", work="The Geographical Lore of the Time of the Crusades",
        year_label="1925", year_sort="1925", place_publisher="New York: American Geographical Society",
        tradition="US", genre="Scholarship", census_frame="d2_scholarly_en", enumerates="partial", C="4", D="5",
        quote="Egypt was the objective of the Crusaders of the Fifth Crusade, who seized and held the city of Damietta "
              "from 1219 to 1221",
        url=IA + "geographicallore00wrig", verification_level="full_text", title_page_checked="no", country="US",
        notes="'a history of the Fourth Crusade by a participant' (Robert de Clari). Read for numbering only."),
    new("sd2-1930-coulton-crusades-commerce", label="G. G. Coulton, Crusades, Commerce and Adventure",
        author="G. G. Coulton", work="Crusades, Commerce and Adventure", year_label="1930", year_sort="1930",
        place_publisher="London: Thomas Nelson", tradition="Britain", genre="Popular history",
        census_frame="d2_popular_en", enumerates="partial", C="4", D="5",
        quote="THE FOURTH CRUSADE-I ... THE FIFTH TO THE EIGHTH CRUSADE ... Thus ended the Fifth Crusade (1221)",
        url=IA + "crusadescommerce0000ggco", verification_level="full_text", title_page_checked="no",
        country="GB",
        notes="Chapter titles 'The Princes' Crusade', 'The Second and Third Crusades', 'The Fourth Crusade' (three "
              "chapters), 'The Fifth to the Eighth Crusade': the modern eight by implication. Edward 'joined the "
              "Crusade only between the acceptation of the treaty (Nov. 1) and its final ratification' (inside "
              "the eighth). Read for numbering only."),
    new("sd2-1903-clinton-novels-list", label="Clinton, A Study of the Crusades through Historical Novels",
        author="[Clinton]", work="A Study of the Crusades through a Selected and Annotated List of Historical Novels",
        year_label="1903", year_sort="1903", place_publisher="", tradition="US", genre="Reference",
        census_frame="d2_reference_en", enumerates="partial", L1="7", L2="8", E="8",
        quote="Apparently no historical novels have been written on the fourth, fifth and sixth Crusades",
        url=IA + "studyofcrusadest00clin", verification_level="full_text", title_page_checked="no", country="US",
        notes="Library reading list. Edgar's Boy Crusaders under 'Seventh Crusade'; Yonge's The Prince and the Page, 'a "
              "story of the last crusade' (Prince Edward), under 'Eighth Crusade'."),
    new("sd2-1849-dansey-english-crusaders", label="J. Dansey, The English Crusaders", author="James Dansey",
        work="The English Crusaders", year_label="1849-50", year_sort="1849", place_publisher="London",
        tradition="Britain", genre="Popular history", census_frame="d2_popular_en", enumerates="no",
        scheme_family="none", url=IA + "englishcrusaders00dansuoft", verification_level="full_text",
        title_page_checked="no", country="GB", notes="Heraldic roll of English crusaders. No crusade numbers."),
    new("sd2-1869-hutton-heroes", label="Barbara Hutton, Heroes of the Crusades", author="Barbara Hutton",
        work="Heroes of the Crusades", year_label="1869", year_sort="1869", place_publisher="London: Griffith and "
                                                                                           "Farran",
        tradition="Britain", genre="Popular history (juvenile)", census_frame="d2_popular_en", enumerates="no",
        scheme_family="none", url=IA + "heroescrusades01huttgoog", verification_level="full_text",
        title_page_checked="no", country="GB",
        notes="Juvenile. Numbers only the first three crusades; later expeditions told by their heroes."),
    new("sd2-1921-stein-little-crusader", label="Evaleen Stein, Our Little Crusader Cousin of Long Ago",
        author="Evaleen Stein", work="Our Little Crusader Cousin of Long Ago", year_label="1921", year_sort="1921",
        place_publisher="Boston: L. C. Page", tradition="US", genre="Popular history (juvenile)",
        census_frame="d2_popular_en", enumerates="no", scheme_family="none", url=IA + "ourlittlecrusade00stei_0",
        verification_level="full_text", title_page_checked="no", country="US", notes="No crusade numbers."),
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
    attr("sd2-1874-lingard-england", country_pub="Ireland"),
    attr("sd2-1854-newman-turks", frame_id="C20", country_pub="Ireland", author_origin="England",
         fourth_identity="none", fifth_identity="none", gibbon_cited="footnote", gibbon_edition="unspecified",
         sources_named="Gibbon", numbers_follow="unclear;inferred"),
    attr("sd2-1837-reeve-church-dublin", frame_id="C21", country_pub="Ireland", author_origin="England",
         fourth_identity="H6", fifth_identity="none", edward_status="absent", gibbon_cited="none",
         numbers_follow="moreri;inferred", notes="Catholic; Fleury's and Maimbourg's Henry VI fourth (inferred)."),
    attr("sd2-1872-collier-outlines-toronto", frame_id="S05", country_pub="Canada", author_origin="Ireland",
         fourth_identity="H6", fifth_identity="C", edward_status="named_unnumbered", gibbon_cited="none",
         numbers_follow="moreri;inferred", notes="Collier was born in Dublin."),
    attr("sd2-1882-gilbert-world-toronto", frame_id="R41", country_pub="Canada", author_origin="US",
         fourth_identity="C", fifth_identity="D", edward_status="inside_last", gibbon_cited="named_in_text",
         gibbon_edition="unspecified", sources_named="Gibbon;Hallam;Guizot", numbers_follow="gibbon;inferred"),
    attr("sd2-1878-thompson-england-toronto", frame_id="S34", country_pub="Canada", author_origin="England",
         fourth_identity="none", fifth_identity="none", edward_status="last_unnumbered", gibbon_cited="none",
         numbers_follow="unclear;inferred"),
    attr("sd2-1886-adam-robertson-toronto", frame_id="S34", country_pub="Canada", author_origin="Canada",
         fourth_identity="none", fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
    attr("1899-a-h-newman", frame_id="C10", country_pub="US", author_origin="US", fourth_identity="H6",
         fifth_identity="C", edward_status="ninth_with_tunis", ninth_referent="tunis+edward", gibbon_cited="none",
         sources_named="Michaud;Milman;Kugler;Prutz;Lane-Poole;Cox;Raumer;Gieseler",
         numbers_follow="michaud_mills;inferred", notes="Ninth = 1259-1291, 'several feeble expeditions'."),
    attr("sd2-1883-adams-wars-of-cross", frame_id="P14", country_pub="England", author_origin="England",
         fourth_identity="both", fifth_identity="D", edward_status="inside_last", gibbon_cited="quoted",
         gibbon_edition="unspecified", sources_named="Gibbon", numbers_follow="own;documented",
         notes="Table and narrative disagree; the table names the alternatives."),
    attr("sd2-1892-boyd-story", frame_id="P34", country_pub="US", author_origin="US", fourth_identity="H6",
         fifth_identity="C", edward_status="inside_last", gibbon_cited="none", numbers_follow="michaud_mills;inferred",
         notes="Michaud's slots (moreri_eight)."),
    attr("sd2-1869-gibbon-crusades-extract", frame_id="H21", country_pub="England", author_origin="England",
         fourth_identity="C", fifth_identity="D", gibbon_cited="named_in_text", gibbon_edition="unspecified",
         sources_named="Gibbon", numbers_follow="gibbon;documented"),
    attr("sd2-1927-newhall-crusades", frame_id="H12", country_pub="US", author_origin="US", fourth_identity="C",
         fifth_identity="none", edward_status="last_unnumbered", gibbon_cited="named_in_text",
         gibbon_edition="unspecified", sources_named="Gibbon;Munro;Barker;Bréhier;Stevenson",
         numbers_follow="modern;inferred"),
    attr("sd2-1925-wright-geographical-lore", frame_id="H24", country_pub="US", author_origin="US",
         fourth_identity="C", fifth_identity="D", gibbon_cited="none", sources_named="Stubbs;Grousset",
         numbers_follow="modern;inferred", notes="Added during reading (census)."),
    attr("sd2-1930-coulton-crusades-commerce", frame_id="P35", country_pub="Scotland", author_origin="England",
         fourth_identity="C", fifth_identity="D", edward_status="inside_last", gibbon_cited="named_in_text",
         gibbon_edition="unspecified", sources_named="Gibbon;Lightfoot", numbers_follow="modern;inferred",
         notes="Added during reading (census). Nelson, Edinburgh firm; London imprint."),
    attr("sd2-1903-clinton-novels-list", frame_id="R40", country_pub="US", fourth_identity="none",
         fifth_identity="none", edward_status="inside_last", gibbon_cited="none", numbers_follow="modern;inferred",
         notes="Added during reading (census)."),
    attr("sd2-1849-dansey-english-crusaders", frame_id="P35", country_pub="England", fourth_identity="none",
         fifth_identity="none", gibbon_cited="none", sources_named="Keightley", numbers_follow="unclear;inferred",
         notes="Added during reading (census)."),
    attr("sd2-1869-hutton-heroes", frame_id="P30", country_pub="England", fourth_identity="none",
         fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
    attr("sd2-1921-stein-little-crusader", frame_id="P30", country_pub="US", author_origin="US",
         fourth_identity="none", fifth_identity="none", gibbon_cited="none", numbers_follow="unclear;inferred"),
]
L.upsert_attrs(A)

C = [
    ("sd2-1854-newman-turks", "Gibbon", "cites in footnote", "'* Gibbon.' (10 notes)", "documented"),
    ("sd2-1883-adams-wars-of-cross", "Gibbon", "quotes", "'the Temple, as Gibbon aptly calls it, of the Christian "
                                                        "world'", "documented"),
    ("sd2-1927-newhall-crusades", "Gibbon", "cites", "'The historian Gibbon has likened the Emperor Alexius to a Hindu "
                                                    "peasant'", "documented"),
    ("sd2-1927-newhall-crusades", "1911-ernest-barker", "bibliography", "Barker named", "documented"),
    ("sd2-1927-newhall-crusades", "1908-louis-brehier", "bibliography", "Bréhier named 3 times", "documented"),
    ("sd2-1869-gibbon-crusades-extract", "1788-edward-gibbon", "reprints", "chapters 57-61", "documented"),
    ("sd2-1897-conder-latin-kingdom", "sd2-1869-gibbon-crusades-extract", "bibliography",
     "'Gibbon's History of the Crusades' (a separate printing of the chapters; which one not stated)", "inferred"),
    ("sd2-1872-collier-outlines-toronto", "sd-1860-collier-great-events", "same author", "Same count", "inferred"),
]
L.append_citations([dict(citing_work_id=a, cited=b, relation=c, evidence=d, confidence=e) for a, b, c, d, e in C])

L.append_reasons([
    dict(reason_id="r41", year="1883", work="The Wars of the Cross", author="W. H. Davenport Adams", language="en",
         entry_id="sd2-1883-adams-wars-of-cross", kind="alternative_reckoning", target="sixth; fourth",
         expeditions_affected="B;H6",
         phrase="This is included in the Fifth Crusade by some authorities; and the Seventh Crusade is then known as "
                "the Sixth. Others reckon as the Fourth Crusade that which was undertaken by the Emperor Henry VI.",
         verification="full_text", source="archive.org warscrossorhist00adamgoog, chronological tables",
         notes="Footnote to 'The Sixth Crusade, 1240-1241' (Richard of Cornwall). The table also gives 'The Fifth (or "
               "Sixth) Crusade 1216-1220'."),
])

# census of archive.org titles with "crusade(s)" or "crusaders", 1800-1945
raw = """1800|1800|1|Kingdom|The crusaders, or, the siege of Acre (play)|crusadersorsiege0000king|other
1800|1800|1|Religious Tract Society|The Crusades|crusades00britgoog|narrative
1800|1800|1||The Crusades|crusades00londuoft|narrative
1820|1844|22|Mills|The History of the Crusades, for the Recovery and Possession of the Holy Land|historyofcrusade02milluoft|narrative
1820|1820|1|Rutebeuf|The Crusaders|nby_544595|other
1826|1833|5|Sismondi|History of the Crusades against the Albigenses|historyofcrusade00sism|other
1827|1827|1|Oakeley|The Influence of the Crusades upon the Arts and Literature of Europe|TheInfluenceOfTheCrusades|essay
1829|1830|6|Stebbing|The History of Chivalry and the Crusades|historychivalry00stebgoog|narrative
1831|1831|1|Vahram|Vahram's Chronicle of the Armenian Kingdom in Cilicia|vahramschronicle00vahrrich|sources
1834|1859|4|Keightley|The Crusaders; or, Scenes, Events, and Characters|crusadersorscen00keiggoog|narrative
1837|1930|9|Sybel|The History and Literature of the Crusades (tr. 1861)|historyliteratur00sybe|scholarship
1839|1839|1|Michaud|History of the Crusades, Abridged (modern generated translation)|history-of-the-crusades-abridged-j.-f.-michaud|excluded
1840|1840|1|Perry|History of the Crusades|historyofcrusade00perr|narrative
1848|1908|8|Giles; Joinville; Richard of Devizes|Chronicles of the Crusades|chroniclesofcrus00gile|sources
1848|1848|1|Lamping|Crusades in Africa|crusadesinafric|other
1849|1860|3|Sargent|Sketches of the Crusades|sketchescrusade01sarggoog|narrative
1849|1850|2|Dansey|The English Crusaders|englishcrusaders00dansuoft|narrative
1851|1851|6|Finlay|The History of Greece from its Conquest by the Crusaders|historyofgreecef00finl|scholarship
1852|1900|30|Michaud; tr. Robson|History of the Crusades|historycrusades00michgoog|narrative
1852|1853|5|Bloss|Heroines of the Crusades|heroinesofcrusad00blosiala|narrative
1853|1872|4|Browne|Yusef; or, The Journey of the Frangi (travel)|yuseforjourneyf00browgoog|other
1853|1853|1|Herbert|The Chevaliers of France|cavaliersengland53herbrich|other
1854|1889|6|Procter|History of the Crusades: Their Rise, Progress, and Results|historycrusades00procgoog|narrative
1854|1856|10|Busk|Mediaeval Popes, Emperors, Kings, and Crusaders|medivalpopesem01buskuoft|narrative
1854|1854|1|Rule|The Third Crusade|TheThirdCrusade|narrative
1859|1859|2|Ditson|The Crescent and French Crusaders|crescentandfren00distgoog|other
1860|1860|4|Edgar|The Crusades and the Crusaders|crusadesandcrus00edgagoog|narrative
1869|1869|2|Hutton|Heroes of the Crusades|heroescrusades01huttgoog|juvenile
1869|1870|3|Gibbon|The Crusades (chapters 57-61)|crusadesad00gibbgoog|narrative
1870|1898|7|Gray|The Children's Crusade|childrenscrusade0000geor|narrative
1870|1870|2|Forge|Richard the First and the Third Crusade (from the French)|richardfirstand00richgoog|juvenile
1870|1901|13|Cox|The Crusades (Epochs of History)|crusades01coxg|narrative
1876|1876|1|Procter|Fighting their Way; or, The History of the Crusades|fightingtheirwa00procgoog|narrative
1878|1890|3|Raumer|Der erste Kreuzzug: The First Crusade (reader)|dererstekreuzzu00raumgoog|other
1880|1889|3|Gibbon|Life and Letters of Edward Gibbon, with his History of the Crusades|lifelettersofedw00gibb|narrative
1881|1891|7|Michaud|The History of the Crusades (later printings)|historyofcrusade0003jose|narrative
1882|1882|1|Norton|The Crusaders|crusaders00nort|other
1883|1883|1|Adams|The Wars of the Cross; or, The History of the Crusades|warscrossorhist00adamgoog|narrative
1885|1886|7|Pears|The Fall of Constantinople, being the Story of the Fourth Crusade|fallofconstantin00pear|scholarship
1888|1912|6|Archer|The Crusade of Richard I, 1189-92|crusaderichardi00archgoog|sources
1890|1902|18|Archer and Kingsford|The Crusades: the Story of the Latin Kingdom of Jerusalem|crusadesstoryla00kinggoog|narrative
1892|1892|1|Boyd|Story of the Crusades|storyofcrusadesw00boyd|narrative
1894|1894|6|Mombert|A Short History of the Crusades|ashorthistorycr00mombgoog|narrative
1896|1914|10|Ludlow|The Age of the Crusades|agecrusades00ludlgoog|narrative
1896|1907|3|Munro|The Fourth Crusade (Translations and Reprints)|TheFourthCrusade|sources
1898|1906|5|Gray; Schwob; Pierne|The Children's Crusade|childrenscrusade00grayuoft|other
1898|1901|2|Bramhall|The Temporal Privileges of Crusaders|temporalprivileg00bram|scholarship
1901|1903|4|Munro|Urban and the Crusaders; Letters of the Crusaders; Essays on the Crusades|urbanandcrusade00munrgoog|sources
1903|1903|1|Clinton|A Study of the Crusades through Historical Novels|studyofcrusadest00clin|reference
1907|1907|12|Stevenson|The Crusaders in the East|crusadersineastb00stevuoft|scholarship
1908|1926|9|Villehardouin; Joinville; Marzials|Memoirs of the Crusades|memoircrusades00villuoft|sources
1913|1913|2|Blyth|Jerusalem and the Crusades|jerusalemcrusade00blyt|juvenile
1913|1914|5|Whale; Stephens|From the Crusades to the French Revolution|fromcrusadestofr00whaluoft|other
1921|1921|10|Krey|The First Crusade: The Accounts of Eye-witnesses and Participants|firstcrusadeacc00kreygoog|sources
1921|1921|1|Stein|Our Little Crusader Cousin of Long Ago|ourlittlecrusade00stei_0|juvenile
1925|1925|3|Wright|The Geographical Lore of the Time of the Crusades|geographicallore00wrig|scholarship
1925|1939|3|Barker|The Crusades|crusades0000unse_z2b9|narrative
1927|1927|2|Newhall|The Crusades|crusades0000newh|scholarship
1928|1928|3|Paetow (ed.)|The Crusades and Other Historical Essays presented to Dana C. Munro|crusadesotherhis0000loui|scholarship
1929|1929|2|Hitti|An Arab-Syrian Gentleman and Warrior in the Period of the Crusades|arabsyriangentle00usma|sources
1930|1945|30|Lamb|The Crusades: Iron Men and Saints; The Flame of Islam|crusadesironmens00lamb|narrative
1930|1930|1|Coulton|Crusades, Commerce and Adventure|crusadescommerce0000ggco|narrative
1932|1932|4|Gibb|The Damascus Chronicle of the Crusades|damascuschronicl00harg|sources
1934|1934|1|Atiya|The Crusade of Nicopolis|bwb_C0-ABV-933|scholarship
1935|1935|1|Munro|The Kingdom of the Crusaders|kingdomofcrusade0000unse_a2t5|scholarship
1937|1937|2|Belloc|The Crusade: The World's Debate|crusadeworldsdeb0000bell|narrative
1938|1938|3|Atiya|The Crusade in the Later Middle Ages|crusadeinlatermi0000aziz|scholarship
1939|1939|2||The Epic of the Crusades|epicofcrusades0000unse|narrative
1939|1939|1|Waters Taylor|The Eighth Crusade (Palestine 1917-20; Berlin propaganda imprint)|the_eighth_crusade|excluded
1939|1939|1|Siedschlag|English Participation in the Crusades 1150-1220|englishparticipa0000beat|scholarship
1941|1941|4|McGinty; Hubert and La Monte|Fulcher of Chartres; The Crusade of Richard Lion-Heart|chronicleoffirst0000fouc|sources
1943|1943|1|Halecki|The Crusade of Varna|crusadeofvarnadi0000hale|scholarship"""
works_now = cur()
urls = {}
for w in works_now.values():
    for part in (w["url"] + " " + w["notes"]).split():
        part = part.strip("();,.'")
        if part.startswith("https://archive.org/details/"):
            part = part.rsplit("/", 1)[-1]
        urls.setdefault(part, w["work_id"])
READ_BY_AUTHOR = {"Mills": "1820-charles-mills", "Stebbing": "sd2-1830-stebbing-chivalry",
                  "Keightley": "sd2-1834-keightley-crusaders", "Perry": "1865-walter-c-perry",
                  "Sargent": "sd2-1849-sargent-sketches", "Dansey": "sd2-1849-dansey-english-crusaders",
                  "Michaud; tr. Robson": "1852-michaud-trans-william-robson", "Bloss": "sd2-1853-bloss-heroines",
                  "Procter": "1842-george-proctor", "Edgar": "sd2-1860-edgar-crusaders",
                  "Hutton": "sd2-1869-hutton-heroes", "Gibbon": "sd2-1869-gibbon-crusades-extract",
                  "Cox": "1874-george-w-cox", "Adams": "sd2-1883-adams-wars-of-cross", "Pears": "1885-edwin-pears",
                  "Archer": "sd2-1888-archer-crusade-richard", "Archer and Kingsford": "1894-t-a-archer-c-l-kingsford",
                  "Boyd": "sd2-1892-boyd-story", "Mombert": "1894-j-i-mombert", "Ludlow": "1896-j-m-ludlow",
                  "Munro": "1896-dana-c-munro", "Clinton": "sd2-1903-clinton-novels-list",
                  "Stevenson": "1907-w-b-stevenson", "Blyth": "sd2-1913-blyth-jerusalem",
                  "Krey": "sd2-1921-krey-first-crusade", "Stein": "sd2-1921-stein-little-crusader",
                  "Wright": "sd2-1925-wright-geographical-lore", "Barker": "1923-ernest-barker",
                  "Newhall": "sd2-1927-newhall-crusades", "Lamb": "sd2-1930-lamb-flame-islam",
                  "Coulton": "sd2-1930-coulton-crusades-commerce", "Religious Tract Society": "sd2-1850-rts-crusades"}
out = []
for line in raw.splitlines():
    y0, y1, n, au, ti, ident, kind = line.split("|")
    wid = urls.get(ident) or READ_BY_AUTHOR.get(au, "")
    status = "read" if wid else ("excluded" if kind == "excluded" else (
        "out of scope" if kind in ("other", "sources") else "not read"))
    out.append(dict(first_year=y0, last_year=y1, copies=n, author=au, title=ti, identifier=ident, kind=kind,
                    status=status, work_id=wid))
with open(L.ROOT / "strand_d2" / "census_archiveorg_titles.csv", "w", newline="", encoding="utf-8") as f:
    wr = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n")
    wr.writeheader()
    wr.writerows(out)

B = "archive.org metadata and djvu text (browser)"
L.append_log(D, [
    ("archive.org advancedsearch (browser)", "title:(crusade OR crusades OR crusaders), texts, 1800-1945 (1,000 "
                                             "items, the cap); publisher:(Dublin) histories; Duffy, Gill, Catholic "
                                             "Book Society; Toronto, Montreal, Halifax, Quebec histories; Newman; "
                                             "Gibbon editions", "1800-1945", "1,000; 80 x 6", "1,480",
     "data/strand_d2/census_archiveorg_titles.csv (83 works after merging copies and excluding fiction, music and "
     "modern 'crusades'); Irish and Canadian identifiers"),
    (B, "Ireland and Canada batch: Newman's Turks (Dublin 1854), Reeve (Dublin 1837), J. B. Robertson lectures "
        "(Dublin 1864), Collier (Toronto 1872), Adam and Robertson (Toronto 1886), Buckley and Robertson (1891), "
        "Wrong (1915), Pinnock's Goldsmith (Montreal 1866), Cyclopaedia of history (Montreal 1859), Gilbert "
        "(Toronto 1882), Thompson (Toronto 1878), Ontario syllabus 1908, A. H. Newman 1899 and 1900",
     "1837-1915", "14 items", "14",
     "sd2-1854-newman-turks; sd2-1837-reeve-church-dublin; sd2-1872-collier-outlines-toronto; "
     "sd2-1882-gilbert-world-toronto; sd2-1878-thompson-england-toronto; sd2-1886-adam-robertson-toronto; "
     "1899-a-h-newman; no crusade numbers in the others"),
    (B, "Census batch: Busk vol. 1, Dansey, Hutton, Gibbon's chapters (Murray 1869; with Scott, c. 1870), Adams, "
        "Boyd, Clinton, Whale, Stein, Newhall (DLI), Wright, Waters Taylor 1939, Coulton", "1849-1939", "14 items",
     "14", "10 rows; Busk vol. 1 has no numbers (later volumes not read); Whale no numbers; Waters Taylor excluded "
           "(Berlin imprint; 'the Eighth Crusade' is Allenby's campaign)"),
])
L.set_frame_status({
    "P14": ("read", "sd2-1883-adams-wars-of-cross", "D2: The Wars of the Cross found (1883 copy)"),
    "P30": ("partial", "sd2-1869-hutton-heroes;sd2-1921-stein-little-crusader", ""),
    "C10": ("read", "", "D2: 1899 and 1900 printings"),
    "H12": ("read", "sd2-1927-newhall-crusades", "D2: DLI copy"),
    "H21": ("partial", "sd2-1869-gibbon-crusades-extract", "D2: Murray 1869 chapters"),
    "S05": ("read", "sd2-1872-collier-outlines-toronto", "D2: Toronto 1869 and 1872"),
    "S34": ("partial", "sd2-1878-thompson-england-toronto;sd2-1886-adam-robertson-toronto", ""),
    "S13": ("not_reached", "", "D2: no Irish National School reader with crusades found; Irish rows come from "
                               "Dublin printings of church and national histories"),
})
L.add_frame_rows([
    dict(frame_id="C20", frame="d2_church_en", country="Ireland", genre="Church and national history",
         author="J. H. Newman", title="Lectures on the History of the Turks", editions_targeted="Dublin 1854",
         existing_work_ids="sd2-1854-newman-turks", status="read", notes="added_during_reading"),
    dict(frame_id="C21", frame="d2_church_en", country="Ireland", genre="Church and national history",
         author="Joseph Reeve", title="A Short View of the History of the Christian Church",
         editions_targeted="Dublin 1837", existing_work_ids="sd2-1837-reeve-church-dublin", status="read",
         notes="added_during_reading"),
    dict(frame_id="P34", frame="d2_popular_en", country="US", genre="Popular history", author="J. P. Boyd",
         title="Story of the Crusades", editions_targeted="1892", existing_work_ids="sd2-1892-boyd-story",
         status="read", notes="added_during_reading (census)"),
    dict(frame_id="P35", frame="d2_popular_en", country="England", genre="Popular history",
         author="G. G. Coulton; J. Dansey", title="Crusades, Commerce and Adventure; The English Crusaders",
         editions_targeted="1930; 1849", existing_work_ids="sd2-1930-coulton-crusades-commerce;"
                                                         "sd2-1849-dansey-english-crusaders",
         status="read", notes="added_during_reading (census)"),
    dict(frame_id="H24", frame="d2_scholarly_en", country="US", genre="Scholarship", author="J. K. Wright",
         title="The Geographical Lore of the Time of the Crusades", editions_targeted="1925",
         existing_work_ids="sd2-1925-wright-geographical-lore", status="read", notes="added_during_reading (census)"),
    dict(frame_id="R41", frame="d2_reference_en", country="Canada", genre="Reference",
         author="Frank Gilbert", title="The World, Historical and Actual (Toronto printing)",
         editions_targeted="1882", existing_work_ids="sd2-1882-gilbert-world-toronto", status="read",
         notes="added_during_reading (Canadian printings)"),
    dict(frame_id="R40", frame="d2_reference_en", country="US", genre="Reference", author="[Clinton]",
         title="A Study of the Crusades through Historical Novels", editions_targeted="1903",
         existing_work_ids="sd2-1903-clinton-novels-list", status="read", notes="added_during_reading (census)"),
])
print("block 5 written;", len(out), "census rows")
