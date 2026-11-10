# Research log

Newest first. Findings in detail go in `notes/findings/`.

## 2026-11-10 — Strand A: the dictionary stemma, French and English

Protocol step 1 done: signature and evidence rules frozen in `docs/SEARCH_PROTOCOL.md`, new fields in `docs/CODEBOOK.md`. Step 2 done for French and English (`notes/findings/2026-11-strand-a.md`, project copy `claude/findings-2026-11-strand-a.md`; data in `data/strand_a/` and `data/search_log.csv`; 34 entries, 25 at full text).

1. **The Moréri eight.** Every French and English reference entry of 1689–1838 that numbers all eight uses Moréri's scheme: Henry VI fourth (1195), 1202–04 fifth (dated 1198), a sixth from 1213 to 1244, Louis IX seventh and eighth. Basnage's Furetière (1701) adds the formula "On compte 8. Croisades"; Trévoux condenses Moréri's sections under it; Chambers (1728) translates Trévoux; Britannica keeps it in the 2nd, 3rd and 8th editions (1778, 1797, 1854); Courtin's *Encyclopédie moderne* (1824) recasts it by pontificate ("On compte communément huit croisades"); Furne's *Biographie universelle* (1838) abridges Courtin. The *Encyclopédie* (1754) numbers nothing.
2. **Bouillet reported the swap; he did not make it.** His 1842 entry (title page checked) abridges Courtin/Furne and changes two things: it drops Celestine III/Henry VI and splits Honorius III/Gregory IX into a fifth and a sixth. "Généralement" is Courtin's "communément", which described the old eight. Le Bas's *France: dictionnaire encyclopédique*, t. 6 (Didot, 1842, title page checked) has the modern eight in a different text. Outside the frame, Schöll's *Cours d'histoire des états européens* (1830) already numbers 1202–04 fourth, 1217 fifth, 1228 sixth, 1248 seventh.
3. **Other branches.** Rees's *Cyclopaedia* (vol. 10, c. 1808) counts nine with Frederick II seventh, before Mills. The *Encyclopaedia Americana* (1830) carries the German six from Brockhaus. The *Penny Cyclopaedia* (1837) has a German-type seven. Larousse (1869) has a third eight: Andrew II fourth "plus généralement", Frederick II fifth, Barons' sixth.
4. **Diffusion leads.** Bouillet's text reused in Picot's English school reader (1846), de Bormans's Belgian tables (1853) and a Brussels adaptation (1852–53).

## 2026-11-10 — Repository created and first commit

GitHub repository created (public) and the project's work committed: skeleton and v0.1 dataset (85 works), docs, the search protocol (`docs/SEARCH_PROTOCOL.md`), the essay outline (`paper/essay-outline.md`), and all findings notes (November review, second review, four Wikipedia notes).

Not yet in the repository: `data/wikipedia/`, `data/ledger/`, the ledger and scroll-story pages in `site/`, and the scripts that built them. Those were produced in earlier sessions whose working files did not reach the local folder or the project. The Wikipedia tables can be regenerated through the MediaWiki API ("the extraction reruns in a few minutes"); the scroll story exists as a Claude dashboard (https://claude.ai/artifact/NHzfxkeMeY3BocN1EEZZi8).

## 2026-11-09 (late) — Second review and search protocol

Second-round fact-check and strategy (`notes/findings/2026-11-second-review.md`): "eight" is an eighteenth-century dictionary total (EB1 1771; Saint-Allais 1816), so the question becomes who dropped Henry VI and seated Frederick II inside an existing eight, c. 1816–42; Bréhier's *Catholic Encyclopedia* list (1908) matches the oldest English Wikipedia version; prior literature to cite (Murray 2006, Cetro); errata in the 2022 paper. Search protocol for the origin and diffusion questions (`docs/SEARCH_PROTOCOL.md`).

## 2026-11-09 (evening) — Scope of the side boxes, and the final scroll story

1. **What counts as a crusade, English and German** (`notes/findings/2026-11-wikipedia-scope.md`). English box 12 links (2004) → 107 (April 2025) → 64; Reconquista in four times; early modern wars six times; Holy Land section today 19 entries, 8 numbered. German 16 → 22, one chronological line. No title, redirect, lead or alias in either language ever numbers 1197, 1101, People's, Children's or a late crusade.
2. **Twenty-two languages** (`notes/findings/2026-11-wikipedia-scope-languages.md`; matrix `data/wikipedia/scope/box_membership_matrix.tsv`, not yet committed). Spanish is not the Reconquista edition, Catalan is; Danish began as a Baltic box, Finnish removed the crusades to Finland; Arabic and Persian include Europe's internal crusades; Czech numbers four crusades against the Hussites; editions often leave out their own (Polish, Russian, Hungarian, Portuguese, Finnish). English is the exporter.
3. **The 2001 article and 9/11** (`notes/findings/2026-11-wikipedia-2001-and-911.md`). Oldest surviving version 28 October 2001 (Alan Millar): eight crusades, no sources, a crusade/jihad "symmetry" paragraph. 19 November 2001 the pasted Schaff-Herzog text added the German seven to the same page until April 2002. No edit spike after 9/11; 9/11 never named in July samples 2002–12. It shows up in the Tenth (English 2005–10, Arabic 2009–, Spanish → Alexandria).
4. **Final scroll story: "Nine, then eight: How Wikipedia Numbered the Crusades"** (Claude dashboard, https://claude.ai/artifact/NHzfxkeMeY3BocN1EEZZi8; standalone copy planned for `site/wikipedia-story/standalone.html`). Opening (2001 facsimile, two counts, 9/11, edits, 2004 box), Act I numbers (counts by language, rename, pageviews), Act II the English box (link counts, contested entries, Holy Land section), Act III 22 languages (grid by kind, tours, absences), Coda the Tenth. Five public-domain Commons images.

## 2026-11-09 (later) — Visualizations: the ledger and the scroll story

Built the two pieces chosen from the three visualization schemes (ledger first, scroll story on top; the transmission network is on hold until the citation data can carry it).

1. **One table under both.** `data/ledger/ledger.csv`: 78 print works and catalogs hand-coded from the Claude Doc's "Numbering corpus" tab into expedition columns (H6 to E), plus 37 runs of Wikipedia navigation boxes in 15 languages. Cell codes: number, `n` named, `x` not counted, `(7)` variant; the same number in adjacent columns = counted as one. Built by `scripts/ledger_code_corpus.py` and `scripts/build_ledger.py` (not yet committed).
2. **Crusade Numbering Ledger** (Claude dashboard): every source by every expedition, colored against the modern list, filters by tradition, click a row for its note. Earliest full modern list: Bouillet (1842).
3. **The Life of a Number** (Claude dashboard, scroll story): four chapters on a sticky timeline, one lane per tradition: the Ninth, Damietta and Frederick II as rival Fifths, the Barons' Crusade, and how many crusades.
4. Standalone copies planned for GitHub Pages in `site/ledger.html` and `site/story.html`.
5. **Mills (1820), from the corpus row:** Henry VI 4, 1202–04 5, Damietta and Frederick 6, Barons' 7, Louis IX 8, Tunis and Edward "the Last Crusade". Nine expeditions, the ninth named, not numbered. Consistent with the deleted Wikipedia claim that the nine was "used in 1820 by Charles Mills", but the number nine itself is not in the row as recorded.

## 2026-11-09 — Wikipedia, second pass

Pageviews, article leads, Wikidata, GND, talk archives, and nine more languages (findings note section "Second pass").

1. **Readership.** English is 52% of views across the ten editions (2016–25), Spanish 14, German 9, French 8. The "Ninth Crusade" redirect still drew a third of traffic to Edward's crusade in 2025. "Most-read reference" is untestable; "read millions of times a year" is safe.
2. **Leads.** English Eighth said "sometimes counted as the Seventh" 2005–22; Greek translated it the year English dropped it. German leads since 2011 call the one-to-nine count that of "französische und englische Literatur".
3. **New languages.** Nine in pt (complete 2005), cs, tr, ru. Polish counts seven by omitting Frederick II. Swedish stops at the Third, Hungarian at the Fifth. No Tenth anywhere.
4. **Wikidata.** Ordinals only First to Sixth; follows/followed-by chain Sixth → Barons' (2015) → Seventh, then nothing. Edward's label still "Ninth Crusade".
5. **Talk archives.** English "Crusades" credited the nine to Charles Mills (1820) until the GA review deleted it, 15 October 2019. German QS 19 February 2007 cited Mayer, Setton, LexMA, Riley-Smith (1999).
6. **GND** keeps German and English numbers together as variants of dated headings. **LoC** blocked by a bot check; not attempted further.

## 2026-11-08 (evening) — Wikipedia: Arabic, Persian, Hebrew

1. **Arabic** counted eight 2004–10 (navbox until 4 December 2013, the last box in the set to move to nine). Titles moved from indefinite to definite ("اسم علم", proper name). Live article on a "Tenth Crusade" (2009) as a metaphor for the war on terror.
2. **Persian** Fifth to Ninth created 11–15 March 2016 by one editor; navbox's Ninth linked to English. Ninth renamed "Edward I's crusade" 11 February 2020, after the English rename, and restored the next day.
3. **Hebrew** navbox heads its list "the nine great crusades" (2009–); main article thematic, links First to Sixth only. Ninth article (2010) before Eighth (2015). Barons' article 28 December 2025.
4. None of the three has its own count; all follow the western scheme.

## 2026-11-08 — Wikipedia sub-project, first pass

Pulled the MediaWiki histories of the main crusade article, navigation boxes and seventeen crusade articles in English, German, French, Italian, Spanish, Dutch and Greek (`notes/findings/2026-11-wikipedia-numbering.md`).

1. **Barons' Crusade.** English article created 12 February 2016, no earlier page or redirect; first named in the English main article 1 May 2013. French 2008, German 2010, Spanish 2018, Italian 2022, Dutch 2023, Greek 2026. Never numbered.
2. **Nine, then eight, in English.** Ninth in the main article from 13 April 2003; "Ninth Crusade" article 2004–19; renamed "Lord Edward's crusade" 17 November 2019 and dropped from the navbox the same day; out of the main article December 2021.
3. **German seven.** Double count 2004–07 ("Fünfter (Sechster) Kreuzzug"); since April 2007 "insgesamt sieben … offizielle Kreuzzüge", Damietta and Frederick II one Fifth; navbox still brackets the modern count. 2010 talk page calls one-to-nine the "englische" count.
4. **Transmission.** Dutch Ninth added 21 May 2003 by Andre Engels, who had split the English article in October 2002. Greek numbering passage translated from English.
5. **Spanish Tenth.** "Décima cruzada" redirects to Alexandria 1365 (2018).

Checks: 13 pinned transitions verified against parent revisions; 6 random cells re-extracted.

## 2026-11-08 — Setup and the November review

Work done in one long session before the project existed (see `notes/findings/2026-11-review.md`):

1. **Fact-check of the 2022 submission.** The Mombert (1894) origin fails; Duruy (1861) and Myers (1885) have the modern eight; numbering is early modern (Fuller 1639, Maimbourg 1675–76). No 1894–1951 "golden age" in Ngram data.
2. **Citation pass.** Myers cites Michaud as a principal authority and Gibbon as a lesser one. The pre-1885 American eight runs through Mills and Proctor.
3. **German pass.** German encyclopedias count six (1830s–60s), schoolbooks seven with Frederick II fifth. Röhricht's Fifth is Damietta, as in Gibbon. GND uses dated headings.
4. **Four-language pass.** Italian, Spanish, Greek, Dutch. Greek writers call 1204 the Fourth Crusade from at least 1845. Dutch splits: northern schoolbooks follow the German seven, French-derived and Catholic books the French eight. The Reconquista never enters the series.
5. **Origin check.** Bouillet (Hachette, 1842) is the earliest modern eight found. Cantù's first edition (1842–44) has a different eight and switched to Bouillet's list by 1851. Lefranc (1834) and Lévi Alvarès (1835) show French school counts still unsettled.

Setup: repository skeleton, licenses, codebook, plan, 85 works migrated into `data/works.csv`, 235 derived numbering rows, 15 citation edges.

## Next

- [ ] Rename the repository to drop the trailing hyphen
- [ ] Regenerate and commit `data/wikipedia/`, `data/ledger/`, their scripts, and standalone `site/` pages
- [x] Dictionary chain at full text (search protocol, Strand A), French and English: 34 entries, `data/strand_a/` (10 November)
- [ ] Strand A gaps: Trévoux 1704, 1721, 1732 page images; Moréri 1674–94; *Encyclopédie des gens du monde* t. 7 (1836); d'Harmonville (1842); EB4–7; title pages for Courtin 1824 and Furne 1838; Furetière 1690 page image
- [ ] Strand A, German: Brockhaus, Pierer, Meyer, Ersch-Gruber
- [ ] Compare Wikipedia rev 349190657 with Bréhier (1908) word for word
- [ ] Read Murray (2006) and Cetro; rewrite the paper's opening claim
- [ ] Strand B, in this order: Schöll, *Cours d'histoire des états européens* t. 3 (1830); Le Bas's source in *L'Univers*; Lefranc 1838 and 1841; Université programmes and baccalauréat lists 1830–42; *Annuaire du Bureau des longitudes* (1802)
- [ ] Cantù editions 1844–51: which one switched
- [ ] Avendaño (1846): contents of the fourth to sixth
- [ ] How the eight reached English: translations of Bouillet, Cantù, Duruy; British school texts 1850–1900 (lead: Picot, *Historical Narrations in French*, 1846, reuses Bouillet's paragraph)
- [ ] Charles Mills, *History of the Crusades* (1820): does he call his count nine anywhere?
- [ ] Hand-code the 18 rows in `data/numberings_unparsed.csv`
- [ ] Build `data/evidence.csv` from the review doc's quotations
- [ ] Split the grouped Dutch row into separate works
- [ ] Reconcile the ledger and `data/strand_a/entries.csv` with `data/works.csv` / `numberings.csv` (make `works.csv` the single source)
- [ ] EB9 and Newman: record the middle cells of their nine
- [ ] Wikipedia: decide the two coding questions (options in the findings note)
- [ ] LCSH headings for the crusades, by hand
- [ ] Add codes PEO, C1101, ALX, NIC, VAR to `expeditions.csv` if approved
