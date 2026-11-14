import csv
D="/home/claude/work/task2/"
H=open("/home/claude/work/header_entries.txt").read().strip().split(",")
def row(**k):
    r={h:"" for h in H}; r.update(k); r.setdefault("checked_on","2026-11-13"); r["checked_on"]="2026-11-13"; return r
rows=[
row(entry_id="sb-1808-heeren-villers",work="Essai sur l'influence des croisades (tr. of Heeren's prize essay)",
 author_editor="A. H. L. Heeren; tr. Charles Villers",edition="French translation, 1st ed.",year_read="1808",
 place_publisher="Paris and Strasbourg: Treuttel et Würtz",volume="1 vol.",pages="narrative sections (chars 0-200,000 of OCR text; c. first quarter of volume)",
 language="fr",access="archive.org djvu text (OCR), read via fetch",url="https://archive.org/stream/essaisurlinflue00villgoog/essaisurlinflue00villgoog_djvu.txt",
 verification_level="full_text",title_page_checked="yes (OCR text: 'A PARIS, Chez Treuttel et Würtz ... 1808')",census_frame="strand_b_fr_1800_1842",
 enumerates="no",stated_count="",stated_phrase="",highest_ordinal="1",organized_by="narrative by theme",scheme_family="none",signature_match="no",
 differing_slots="fourth, fifth, sixth, seventh, eighth",
 quote="Une autre croisade, qui eut lieu peu d'années après, en 1203, amena un résultat d'une bien plus grande importance.",
 notes="Only 'la première croisade' is numbered. Later expeditions are 'une autre croisade', 'une nouvelle croisade' (Thibaut 1239; Louis IX to Tunis). Henry VI named ('céda aux prières de Célestin III') without a number. Only the first 200,000 of 781,204 characters were read (narrative survey); the later analytic chapters were not checked for ordinals. Prize essay genre (Institut 1808). Brief: read only if Schöll or Koch cites it; read here because it surfaced in a control search."),
row(entry_id="sb-1841-buchon-recherches",work="Recherches et matériaux pour servir à une histoire de la domination française aux XIIIe, XIVe et XVe siècles dans les provinces démembrées de l'empire grec à la suite de la quatrième croisade",
 author_editor="J.-A.-C. Buchon",edition="1st ed., première partie",year_read="1841 (OCR of roman numerals garbled; confirm)",
 place_publisher="Paris: Auguste Desrez",volume="1re partie",pages="title page; introduction",language="fr",access="archive.org djvu text (OCR), read via fetch",
 url="https://archive.org/stream/bub_gb_NIUPAAAAQAAJ/bub_gb_NIUPAAAAQAAJ_djvu.txt",verification_level="full_text",
 title_page_checked="yes (OCR text; year garbled)",census_frame="",enumerates="partial",C="4",highest_ordinal="4",organized_by="title and running text (scholarship)",
 scheme_family="",signature_match="no",differing_slots="fifth, sixth, seventh, eighth (not stated)",
 quote="... dans les provinces démembrées de l'empire grec à la suite de la quatrième croisade",
 notes="Out of the four Strand B genres (scholarly edition), but in Paris in the window. 1202-04 is 'la quatrième croisade' in the title itself and 'les pèlerins de la quatrième croisade' in the introduction. No fifth to eighth seen in the first 100,000 characters. A second archive.org copy is recherchesetmat00goog. Shows C 4 as a working label in Paris scholarship c. 1840-41, independent of the schoolbooks; says nothing about slots 5-8."),
row(entry_id="sb-1841-buchon-chroniques-etrangeres",work="Chroniques étrangères relatives aux expéditions françaises pendant le XIIIe siècle",
 author_editor="J.-A.-C. Buchon (ed. and tr.)",edition="1st ed.",year_read="c. 1840-41 (OCR 'M DCCC XL...' garbled)",
 place_publisher="Paris: Mairet; impr. Auguste Desrez",volume="1 vol.",pages="Notice (preface)",language="fr",access="archive.org djvu text (OCR), read via fetch",
 url="https://archive.org/stream/chroniquestrang00unkngoog/chroniquestrang00unkngoog_djvu.txt",verification_level="full_text",
 title_page_checked="yes (OCR text; year garbled)",census_frame="",enumerates="partial",C="4",highest_ordinal="4",organized_by="running text (scholarship)",
 scheme_family="",signature_match="no",differing_slots="fifth, sixth, seventh, eighth (not stated)",
 quote="l'histoire de cette quatrième croisade",
 notes="Same author and usage as sb-1841-buchon-recherches: 1202-04 called the fourth crusade. Only the first 100,000 of 3.6 million characters read. Matched a control search for 'sixième croisade' + 'Frédéric II' + 'cinquième croisade', so later pages may carry more ordinals: unread."),
row(entry_id="sb-1886-michaud-poujoulat-abrege",work="Histoire des croisades abrégée à l'usage de la jeunesse",
 author_editor="J.-F. Michaud and J.-J.-F. Poujoulat",edition="later printing of the abridgment first published 1838",year_read="1886",
 place_publisher="Tours: Alfred Mame et fils",volume="1 vol.",pages="Table (end of volume); preface",language="fr",access="archive.org djvu text (OCR), read via fetch",
 url="https://archive.org/stream/histoiredescrois00mich/histoiredescrois00mich_djvu.txt",verification_level="full_text",
 title_page_checked="yes (OCR text: 'TOURS ALFRED MAME ET FILS, ÉDITEURS M DCCC LXXXVI')",census_frame="",enumerates="yes",stated_count="8 (headings)",
 stated_phrase="Huitième croisade. — Seconde expédition de saint Louis.",H6="4",C="5",D="6",F="6",B="6",L1="7",L2="8",highest_ordinal="8",
 organized_by="numbered chapter headings",scheme_family="moreri_eight",signature_match="no",differing_slots="fourth, fifth, sixth",
 stemma_parent="Michaud, Histoire des croisades",parent_evidence="documented: abridgment of Michaud by Poujoulat (preface)",
 quote="Quatrième croisade. — Prédication de la croisade en Allemagne. [...] Cinquième croisade. — Prédication de la croisade par Foulque de Neuilly. (De 1202 à 1205.) [...] Commencement de la sixième croisade. — Expédition d'André II",
 notes="Table: ch. XXIV 'Commencement de la sixième croisade' (André II, 1215-17); XXVII 'Suite de la sixième croisade' (Frédéric II, 1228-29); XXVIII 'Fin de la sixième croisade' (Thibaut, 1238-40); XXIX 'Septième croisade' (Louis IX, 1244-53); XXXIII 'Huitième croisade' (dates printed '1208 à 1270', misprint). This 1886 printing is outside the window; it confirms that the 1838 abridgment's scheme (works.csv row 1838-michaud-poujoulat, paper_table) is Michaud's and was never re-slotted. 1838 title page not seen."),
row(entry_id="sb-1826-michaud-histoire-4e-ed",work="Histoire des croisades, 4e éd., t. III (1826) and t. IV (1827)",
 author_editor="J.-F. Michaud",edition="4th ed.",year_read="1826-27",place_publisher="Paris: Ponthieu; Levasseur",volume="t. III, t. IV",pages="title statements",
 language="fr",access="catalog transcription of title pages (Bibliothèques numériques de la Défense)",
 url="https://bibliotheques-numeriques.defense.gouv.fr/impression/document/50ca0864-6313-4179-9679-383e4c939336",verification_level="secondary",
 title_page_checked="no (catalog transcription only)",census_frame="",enumerates="partial",stated_count="",stated_phrase="contenant le récit de la 4e croisade, de la conquête de Constantinople par les Francs, et de la 6e croisade",
 H6="4",C="5",D="6",highest_ordinal="6",organized_by="volume title statements",scheme_family="moreri_eight",signature_match="no",differing_slots="fourth, fifth",
 quote="T. III, contenant le récit de la 4e croisade, de la conquête de Constantinople par les Francs, et de la 6e croisade",
 notes="t. IV (record e98631a5-9287-4450-ac0f-ee1f7ba5a423, 1827): 'fin de la sixième croisade et la première expédition de saint Louis'. The 4e croisade precedes the conquest of Constantinople and is therefore Henry VI's (Michaud's book order); 1202-04 is the unnamed fifth between. Catalog-level evidence: Michaud's scheme stands in the leading French authority through the 1820s. Outside the four Strand B genres; anchor for what schoolbooks would copy."),
]
with open(D+"entries.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=H); w.writeheader(); [w.writerow(r) for r in rows]

FH="work_id,author,title,first_year,editions_in_window,genre,publisher,source_of_listing,status".split(",")
F=[
("F01","Émile Lefranc","Histoire du moyen âge (476-1453), 'sur un plan tout-à-fait neuf'","1834","1834; 3e éd. 1838; 7e éd. 1841 (and 1843 outside)","précis (collège)","Lyon and Paris: Périsse frères","Europeana record (1841, 7e éd.); AbeBooks listings (1838 3e éd., 1843); works.csv","coded_previously (1834 contents snippet: H6 4, C 5, F 6, L2 8); 1838/1841 not_reached"),
("F02","David Lévi Alvarès","Nouveaux élémens d'histoire générale","1835","1835 and later eds (not enumerated)","précis / élémens","Paris (publisher not confirmed)","works.csv","coded_previously (snippet: D 5, L1 6, F excluded); not re-read"),
("F03","C.-O. Des Michels","Précis de l'histoire du moyen âge","before 1832","3e éd. 1832 (Colas); further eds to 1840s (recalled)","précis (collège)","Paris: L. Colas (with Hachette, recalled)","cageweb.be records (3e éd. 1832); recalled","not_reached"),
("F04","C.-O. Des Michels","Histoire générale du moyen âge","1827","t. I 1827; 2e éd. 1837 (2 vols)","history for collèges","Paris: L. Colas et L. Hachette","Défense catalog records","not_reached (both volumes stop before the crusades by their contents notes)"),
("F05","C.-O. Des Michels","Tableau chronologique de l'histoire du moyen âge","unknown (in window, recalled)","unknown","chronological table","Paris (publisher not confirmed)","Google Books record bEdCygAACAAJ","not_reached"),
("F06","Jules Michelet","Précis de l'histoire de France jusqu'à la Révolution française","1833","1833 and later","précis (collège)","Paris: Hachette","archive.org prcisdelhistoi00michuoft; DDB record","not_reached"),
("F07","Louis-Pierre Anquetil","Précis de l'histoire universelle (nouvelle édition revue et corrigée)","1797","1818 (Janet et Cotelle) and others","précis","Paris: Janet et Cotelle","archive.org cihm_48028 (t. 3, 1818)","not_reached (t. 3 read: Roman history; crusade volume not found)"),
("F08","C.-F.-X. Millot","Élémens d'histoire générale (reprints)","1772","reprints in window (recalled)","élémens","various","archive.org results; recalled","not_reached"),
("F09","J.-N. Loriquet","Histoire de France à l'usage de la jeunesse","1814","many eds 1816-42 (recalled)","abrégé (Catholic schools)","Lyon/Paris: Rusand (recalled)","recalled","not_reached"),
("F10","Le Ragois (continued)","Instruction sur l'histoire de France (par demandes et réponses)","1684","many eds in window (recalled)","question-and-answer","various","recalled","not_reached"),
("F11","Louis Gaultier, rev. Blignières, Demoyencourt et al.","Leçons de chronologie et d'histoire (t. V Histoire de France)","1836 (this rev.)","1836; reprints 1837-66","question-and-answer","Paris: J. Renouard","BnF cb304879822 (Gallica t. 2, t. 5)","not_reached (Gallica unreachable)"),
("F12","Mme de Saint-Ouen","Histoire de France (for children)","1827 (recalled)","many eds (recalled)","abrégé","Paris (recalled)","recalled","not_reached"),
("F13","J.-R. Lamé-Fleury","L'histoire de France racontée à la jeunesse / Histoire du moyen âge racontée à la jeunesse","1830s (recalled)","several","abrégé","Paris (recalled)","archive.org lhistoiredefranc00lame; recalled","not_reached"),
("F14","Victor Boreau","Histoire générale des temps du moyen âge, avec tableaux synoptiques","before 1846 (3e éd. 1846)","1st and 2nd eds date unknown","précis with synoptic tables","Paris","Google Books about page id ShQOxk7LRKgC (3e éd. 1846)","not_reached (contents: only 'Première croisade' heading)"),
("F15","François Valentin","Abrégé de l'histoire des croisades (1095-1291)","1841","1841 (10e éd. by 1863)","abrégé (Bibliothèque de la jeunesse chrétienne)","Tours: A. Mame","archive.org abrgdelhistoire00valegoog (1841); biblio.co.uk listing (10e éd. 1863)","not_reached (text URL not in search results)"),
("F16","J.-F. Michaud and J.-J.-F. Poujoulat","Histoire des croisades abrégée à l'usage de la jeunesse","1838","1838 (later Mame printings)","abrégé for youth","Paris / Tours: Mame","works.csv; archive.org histoiredescrois00mich (1886)","coded (1886 printing, contents: Michaud scheme); 1838 not seen"),
("F17","J.-F. Michaud","Histoire abrégée des croisades (for youth)","1839","1839","abrégé for youth","Paris","works.csv","coded_previously (snippet: L2 8); not re-read"),
("F18","M. S. F. Schöll","Cours d'histoire des états européens","1830","1830-34","history course","Paris: Gide; Berlin: Duncker et Humblot","task 1","coded_task1 (snippet: C 4, D 5, F 6, L1 7)"),
("F19","C.-G. Koch, rev. Schöll","Tableau des révolutions de l'Europe, nouvelle éd.","1814 (Schöll rev.; Gallica record)","1814; 1823","history / chronological tablets","Paris: Gide fils","task 1; Gallica records (t. 2, t. 3 of the 'nouvelle édition ... continuée' by 'l'auteur de l'Histoire des traités de paix')","coded_task1 for 1823 (English tr. only); 1814 French not_reached"),
("F20","C.-G. Koch","Tableau des révolutions de l'Europe (3 vols, with Tablettes chronologiques)","1807 (this ed.)","1807","history with chronological tablets","Paris: F. Schoell","Défense catalog; DDB/BSB; Google Books IcpNAAAAcAAJ (contents)","not_reached (MDZ needs approval; Google page views robots-blocked; Gallica t. III unreachable)"),
("F21","C.-G. Koch","Tableau des révolutions de l'Europe dans le moyen âge","1771","(pre-window)","history","Lausanne and Strasbourg: Bauer","archive.org tableaudesrvolu07kochgoog; Gallica bpt6k1158958 (T2)","not_reached (djvu text needs approval; Gallica unreachable)"),
("F22","E. Lefranc, G. Jeannin, J. Langlebert","Manuel du baccalauréat ès lettres","unknown (45e éd. 1875)","early eds not dated","baccalauréat manual","Paris: J. Delalain","BnF cb30735256k","not_reached (window membership unconfirmed)"),
("F23","Université de France","Programme / questions d'histoire pour le baccalauréat ès lettres","1840 (recalled)","1840","official programme","Paris","recalled","not_reached"),
("F24","Université de France","Programmes de l'enseignement historique des collèges royaux","1830s (recalled)","unknown","official programme","Paris: Hachette (recalled)","recalled","not_reached"),
("F25","Saint-Allais et al.","L'art de vérifier les dates, octavo reissue (depuis la naissance de N.-S.)","1818","1818-19","chronological table","Paris: rue de la Vrillière / Valade","archive.org lartdeverifier02sain (t. 2), lartdevrifierle10saingoog","not_reached for the crusade volumes (t. 2 read in part: no crusades)"),
("F26","A. Lesage (Las Cases)","Atlas historique, généalogique, chronologique et géographique","1803-08","reissues 1814-1826 (recalled)","atlas / chronological tables","Paris","euratlas.net; Défense records","not_reached"),
("F27","Philippe Le Bas","France: Annales historiques (L'Univers)","1840","1840-43","chronological annals","Paris: Firmin Didot frères","books2ebooks/BNU record","not_reached (candidate source of Le Bas 1842 table)"),
("F28","Philippe Le Bas","Allemagne (L'Univers)","1838 (recalled)","1838","national history with chronology","Paris: Firmin Didot frères","recalled","not_reached"),
("F29","A. H. L. Heeren, tr. Ch. Villers","Essai sur l'influence des croisades","1808","1808","prize essay","Paris and Strasbourg: Treuttel et Würtz","archive.org essaisurlinflue00villgoog","coded (enumerates: no)"),
("F30","M.-G.-A.-F. de Choiseul-Daillecourt","De l'influence des croisades sur l'état des peuples de l'Europe","1809","1809","prize essay","Paris: Tilliard","recalled","not_reached"),
("F31","Bureau des longitudes","Annuaire (Google Books volume dated 1802)","1802 (metadata)","annual","almanac with chronological table","Paris","Strand A note","not_reached (checked once; hit not reproduced)"),
]
with open(D+"frame.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(FH); [w.writerow(x) for x in F]

NR=[
("Koch, Tableau des révolutions de l'Europe","1771 (Bauer), archive.org tableaudesrvolu07kochgoog","djvu text link needs fetch approval (link appeared only on the details page); Gallica copy bpt6k1158958 unreachable","Highest: decides whether slots 4-7 are Koch's (1771) or Schöll's"),
("Koch, Tableau des révolutions de l'Europe","1807 (F. Schoell), t. 1 and t. III Tablettes chronologiques","MDZ bsb11690731 needs fetch approval; Google Books IcpNAAAAcAAJ page views, search and PDF robots-disallowed; Gallica bpt6k1042963h (T. III) server error","High: the Tablettes chronologiques would number the crusades in Koch's lifetime"),
("Koch-Schöll, Tableau, nouvelle édition","1814 (Gallica bpt6k9815643d t. 2; bpt6k9816855m t. 3)","Gallica unreachable from this session (client/server errors on every call)","High: earliest Schöll revision; t. 1 not yet located"),
("Lefranc, Histoire du moyen âge","1838 (3e éd.), 1841 (7e éd.)","No text-bearing copy reachable: Google Books text robots-blocked; archive.org has only the 1850 recast (bub_gb_2rB52UBtCuwC) and its text link needs approval","Highest of the schoolbooks: did slots 4-6 change between 1834 and 1841?"),
("Lefranc, Histoire du moyen âge (recast to 1378)","1850 (Lecoffre), archive.org bub_gb_2rB52UBtCuwC","djvu text link appeared only on details page (approval required)","Medium: shows whether Lefranc had switched to the modern slots by 1850"),
("Valentin, Abrégé de l'histoire des croisades (1095-1291)","1841 (Mame), archive.org abrgdelhistoire00valegoog","text URL not surfaced by any search; details page only","High: a crusade schoolbook of 1841 that must enumerate"),
("Des Michels, Précis de l'histoire du moyen âge","3e éd. 1832 and later","No digitized text found (archive.org prcisdelhistoi01mich PDF redirect needs approval; identity of that item unconfirmed)","High: the Université's standard précis; Hachette circle"),
("Le Bas, France: Annales historiques (L'Univers)","1840-43","Record only (BNU Strasbourg via books2ebooks)","High: most likely immediate source of the Le Bas 1842 table"),
("Gaultier rev., Leçons de chronologie et d'histoire, t. V","1836 (Renouard)","Gallica bpt6k6536490w unreachable","Medium: question-and-answer manual"),
("Michelet, Précis de l'histoire de France","1833 (Hachette)","archive.org prcisdelhistoi00michuoft; no text URL in search results","Medium: Hachette collège précis"),
("Lévi Alvarès, Nouveaux élémens d'histoire générale","1835 and later eds","No copy found by web search","Medium: re-read the 1835 snippet in full; check later eds for Frederick II"),
("L'art de vérifier les dates, octavo reissue","1818-19, volumes on Jerusalem kings and popes","Only t. 2 surfaced (calendars, pre-Christian chronology)","Medium"),
("Lesage (Las Cases), Atlas historique","1803-1826","Plates not reachable (euratlas index server error)","Medium: chronological table of the Middle Ages"),
("Choiseul-Daillecourt, De l'influence des croisades","1809","Not searched beyond recall","Low"),
("Université programmes and baccalauréat question lists","1830-42","No catalog route reachable (Emmanuelle not reachable; BnF catalogue searches return session-bound lists)","Highest for the protocol's hypothesis, but needs the author's library access"),
("Annuaire du Bureau des longitudes","'1802' Google Books volume","Checked once by web search; not reproduced","Low: probably metadata error"),
("Buchon, Chronique de la conquête de Constantinople ... Morée","1825 (Verdière), archive.org bub_gb_OlscpMdCp-0C","text URL not in search results","Medium: would show whether Buchon called 1202-04 the fourth crusade already in 1825"),
]
with open(D+"not_reached.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["work","editions","why_not_reached","priority_note"]); [w.writerow(x) for x in NR]
import collections
st=collections.Counter()
for x in F:
    s=x[8]
    st["coded_this_session" if s.startswith("coded (") else ("coded_task1_or_previous" if s.startswith("coded_") else "not_reached")]+=1
print(len(F),st)
