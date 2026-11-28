# Strand D2: English print, 1800–1945 (28 November 2026)

Interim report of the D2 pass set out in `notes/strand-d2-protocol.md` (startup prompt of 28 November). Browser session on archive.org (djvu text and full-text search), 11:51 to about 13:00 Vienna time, then a wrap-up pass in the evening. Branch `strand-d2-english`, blocks 1 to 6 (`scripts/d2_block1_2026_11_28.py` to `d2_block6_2026_11_28.py`, legacy attributes in `d2_block4_legacy_attrs_2026_11_28.py`, tables from `scripts/d2_analyses.py`).

## 1. What was done

The frame (`data/strand_d2/frame.csv`) grew from 143 to 160 targets: 97 read, 11 partial, 24 not reached, 27 still to read, 1 merged. `data/works.csv` now has 347 rows; 124 are new D2 rows (`sd2-`), and 132 rows in all carry the D2 pass. 184 English rows fall between 1788 and 1945. Each English row has a line in `data/strand_d2/attributes.csv` (184 rows): 140 coded from the text in this pass, 44 legacy rows derived from their slots and flagged "derived from slots; not re-read in D2". New reasons r29–r41, new citations, about 30 search-log rows dated 28 November.

Two counting passes stand beside the rows. The archive.org full-text search classified up to 200 "fourth crusade" items per decade by referent (`data/usage/archiveorg_d2_fourth_referent_by_decade.csv`). The "ninth crusade" search returned 470 items for 1800–1949; all were classified by context, the 219 the first pass could not place in a second pass on the full djvu text. The result is recorded by work in `data/strand_d2/ninth_crusade_hits_by_work.csv` (87 groups, 441 copies to 1945). A title census of archive.org items called "crusade(s)" or "crusaders", 1800–1945, is in `data/strand_d2/census_archiveorg_titles.csv` (72 works after merging copies and dropping fiction, music and modern uses; 36 read, 17 not read, 17 out of scope, 2 excluded).

No WorldCat. HathiTrust was not used (bot check). No lending copy was borrowed in this session, so none had to be returned; works available only as lending copies are listed under not reached. Works after 1930 were read for numbering and chapter titles only.

## 2. The answers in brief

**The Fourth.** English print never moved from Henry VI to 1202–04 as a body. The 1202–04 fourth is the majority in every decade of the full-text count, from Gibbon on. The Henry VI fourth was a counter-current carried by a few long-lived series: the Britannica (EB2–EB9, to the US reprints of 1902), Haydn's *Dictionary of Dates* (1866 to the 25th edition, 1910), Mills (1820) and the books that reused him, Robson's Michaud (1852 to New York 1900), Cox (1874 to 1901), Nelson's Collier (Edinburgh 1860, Toronto 1872), and the American Catholic school line (Fredet 1842, Kerney 1855). Its share of decided full-text items peaked in the 1810s (0.25) and the 1850s and 1870s (0.19) and fell below 0.10 after 1880 and to 0.03 or less after 1900. It ended by attrition, not by conversion: the series that carried it went out of print, except the Britannica, which switched once, with Barker's article in EB11 (1910–11). Of the three explanations, scholarship and schools did not move because they were already there; Barker removed the last major reference holdout, after the decline.

**Gibbon.** Citing Gibbon did not mean using his numbers. Of 42 rows that name him in the crusade chapter, preface or bibliography, 16 match him on every slot they share, 8 on some, 12 on none (6 have no slots). Most matches are on C 4 and D 5, which the modern eight shares. His distinctive L1 6 and L2 7 survive in a small group: Turner 1830, Stebbing 1830, Chepmell 1857, Mosheim in Reid's edition (1860), the Student's Gibbon (1868), Murray's separate printing of the crusade chapters (1869), Gilbert (Toronto 1882), and two books that do not cite him (Goodrich 1853, Tout 1898). Mills, Perry, Michaud's translator, EB9, Conder and the Historians' History cite or quote him and number otherwise. The editors' notes in the Bohn variorum and Bury's edition do not comment on the numbering.

**Edward and the Ninth.** "Ninth crusade" in English print to 1945 has at least six referents. The dominant one, from Russell's *Palestine* (Edinburgh, 1831) to the county atlases of 1936 and A. H. Newman's *Manual* (reprinted to 1937), is a ninth that holds Tunis and Edward together; EB9 (1875–89) was its strongest channel, and EB11 ended it there. An Edward-centered ninth, Edward's crusade called "the ninth" with nothing said of Tunis, is attested in Masonic degree lore (1857, 1872), a review in *The Academy* (1874), Lupton (1883), G. W. Cox's *Concise History of England* (1887), the EETS *Godeffroy of Boloyne* (1893), Parry (1920) and Outhwaite (1935). The modern split, Tunis the eighth and Edward alone the ninth, was not found before 1945.

## 3. The Fourth

### 3.1 The curve

Full-text items (archive.org year; up to 200 classified per decade; Gibbon's own text excluded):

| Decade | Items | C | H6 | both | unclear | H6 or both, share of decided |
|---|---|---|---|---|---|---|
| 1800s | 73 | 35 | 3 | 3 | 23 | 0.15 |
| 1810s | 79 | 41 | 10 | 4 | 12 | 0.25 |
| 1820s | 188 | 75 | 5 | 3 | 83 | 0.10 |
| 1830s | 295 | 93 | 1 | 2 | 100 | 0.03 |
| 1840s | 366 | 114 | 6 | 7 | 66 | 0.10 |
| 1850s | 617 | 105 | 8 | 17 | 59 | 0.19 |
| 1860s | 425 | 100 | 8 | 2 | 75 | 0.09 |
| 1870s | 756 | 102 | 21 | 3 | 74 | 0.19 |
| 1880s | 1,331 | 147 | 11 | 3 | 32 | 0.09 |
| 1890s | 1,458 | 121 | 7 | 0 | 68 | 0.05 |
| 1900s | 2,373 | 154 | 3 | 2 | 34 | 0.03 |
| 1910s | 2,355 | 152 | 0 | 3 | 39 | 0.02 |
| 1920s | 1,844 | 153 | 1 | 1 | 40 | 0.01 |
| 1930s | 1,644 | 135 | 1 | 6 | 58 | 0.05 |
| 1940s | 1,680 | 162 | 0 | 4 | 31 | 0.02 |

The coded rows (`data/strand_d2/fourth_pivot.csv`) tell the same story with a heavier H6 tail, because the frame deliberately includes the reference series. Among decided rows the H6 share is 0.33–0.56 from the 1830s to the 1860s, 0.25–0.33 from the 1870s to the 1890s, 0.50 in the 1900s (Robson's Michaud reprinted 1900, Cox 1901, Great Events 1904, the Historians' History 1904, Skinner's *Collegiate Course for Home Study* 1909), 0.25 in the 1910s (Haydn 1910, Parker 1915) and zero from the 1920s.

### 3.2 Switch dates by series

From `data/strand_d2/fourth_series.csv`:

| Series | Fourth | Switch |
|---|---|---|
| Encyclopaedia Britannica | H6 in EB3 (1797) to EB9 (1875–89; US reprints 1875, 1902) | C from EB11 (1910–11, Barker); EB14 (1929) C |
| Haydn, *Dictionary of Dates* | none numbered in 1844; H6 1866 (London), 1869 and 1883 (New York), 1898 (Toronto), 1910 (25th ed.) | never, to the last edition |
| Chambers's | none in *Information for the People* (1848) | C 4 from the *Encyclopaedia* (1868 vol. 3; Philadelphia 1871; 1901), Frederick-fifth seven throughout |
| Encyclopaedia Americana | 1830: German six (no fourth for 1202–04); chronological table C 5 | C 4 by 1918 (read 1922–24), Frederick-fifth seven |
| Appleton's | New American (1859) none | American Cyclopaedia (1873) C 4, Barons' sixth |
| Johnson's; New International | C 4 (1893–95; 1902) | — |
| Nuttall | "to the number of eight" (1900–07) | C 4, modern eight, 1923 and 1930 |
| Ploetz → Langer | C 4, Frederick-fifth seven (1883, 1905) | Langer 1940: C 4, modern eight |
| Michaud in Robson's English | H6 (1852 to New York 1900) | never |
| Mills and reuse | H6 (1820–44); Historians' History 1904–09 copies him | never |
| Procter | C 4 (1842, Philadelphia 1856) | — |
| Cox | H6 (1874 to the 12th ed., 1901) | never |
| Collier (Nelson) | H6 (1860; Toronto 1869, 1872) | never |
| Swinton | C 4 (New York 1874) | reversed: H6 in the Canadian revision (Halifax 1883), which copies EB9 |
| W. C. Taylor; Myers | C 4 (1844–80; 1885–1921) | — |
| Gibbon and abridgments | C 4 (1788; Student's Gibbon 1868; Murray 1869) | — |

Only two series changed their fourth: the Britannica, toward C, in 1910–11; and Swinton, toward H6, in 1883. Everything else kept its fourth for its whole life.

### 3.3 The three explanations

*Scholarship.* No move to explain. From Gibbon (1788) and Hallam (1818) through Procter (1842; r30, which rejects the Henry VI fourth in so many words), Pears (1885), Stubbs (1886), Archer (1888) and Archer and Kingsford (1894), Munro (1896), Stevenson (1907) and Barker, scholars wrote C 4. The exceptions are popular or semi-popular historians who followed Mills (Perry 1865, Cox 1874, Conder 1897). Riant was not checked in English.

*The school market.* Also already there. Tytler (Edinburgh, 1801) and Keightley (1830) in Britain and Willard (1835) and most American schoolbooks from the 1840s write C 4. The Henry VI fourth survived in schools only in particular lines: American Catholic texts (Fredet 1842, Kerney 1855), Nelson's Collier in Scotland and Canada, the Canadian Swinton (1883), Boyce (1884).

*Barker, 1911.* Barker ended the Henry VI fourth in the Britannica, the most-cited English reference work, and gave it the modern eight (r29, r31: his footnote echoes Procter's). The full-text share had already fallen to 0.05 in the 1890s. Haydn's last edition (1910) and Cox's last (1901) closed the other two main channels at about the same time. Barker canonized the outcome; he did not cause it.

## 4. Gibbon

`data/strand_d2/gibbon_table.csv` lists the 42 rows that name Gibbon in the crusade chapter, preface or bibliography (footnote 14, bibliography 8, named in the text 9, quoted 3, preface 1, and 7 rows with two of these).

The rows that match him fully mostly match only on C 4 and D 5 (Hallam, Willson, Pears, Paetow, Webster, CMH, Newhall, Coulton). The rows that carry his distinctive sixth and seventh are listed in section 2. Two have the full seven: Chepmell (1857), whose preface names Gibbon and whose contents give "The Sixth (or Eighth) Crusade ... The Seventh (or Ninth) Crusade" (r35), and the Student's Gibbon (1868), numerals I–VII, Edward inside the seventh. Mosheim in Reid's edition (1860) says Louis's first expedition "is reckoned the sixth crusade by all authorities" (r40); the corpus shows that only the Gibbon and Frederick-fifth counts did so.

Citing without following is the commoner case. Mills (1820) attacks Gibbon's coverage in his preface and numbers his own way. Perry (1865) cites Gibbon for 1202–04 and calls it the fifth. EB9 (1877) and Conder (1897, who lists "Gibbon's History of the Crusades", the separately printed chapters) list him and number otherwise. Nelson's encyclopedia (1917) lists him and has a Frederick-fifth seven, which agrees with his sixth and seventh but not his fifth. Robson's Michaud keeps Michaud's numbers under Gibbon footnotes.

The Student's Gibbon was a school channel: the Student's Hume (1859) sends readers to it, and Murray's 1869 printing of chapters 57–61 sold Gibbon's crusade narrative separately. The editions with editors' notes (Milman's, carried into Smith's and the Bohn variorum; Bury 1896–1906) have no note on the numbering; the Milman edition's crusade volume itself was not reached.

## 5. Edward and the Ninth

### 5.1 The ninth's referents

From `data/strand_d2/ninth_crusade_hits_by_work.csv` and the coded rows:

| Referent | First and last witness | Examples |
|---|---|---|
| Tunis and Edward together (L2+E) | Russell 1831 to the county-atlas chronology 1936 and Newman's *Manual* (reprints to 1937) | Wallen 1836, Milner 1847, Townsend 1862, Cox 1874, EB9 1875–89, Johnston 1880, the Self-Instructor 1882 and its chain, Lupton 1883 (Edward-led), Swinton (Halifax) 1883, Boyce 1884, Historians' History 1904–09 |
| Tunis (L2) | Rees c. 1808 to Parker 1915 | Chepmell 1857 ("Seventh (or Ninth)"), Hazlitt 1860 to 1915, a reading book of 1864, Johonnot 1887, Desmond 1902, Harbottle 1904, a wall chart of 1905 |
| Louis IX's first crusade (L1) | Mackay 1841 (reprints to 1932) | W. C. Taylor 1844–80 (London and New York; US question editions ask "Who led the ninth crusade?"), G. A. Smith 1894–1935, Blyth 1913, the *Daily Express Encyclopaedia* 1934 ("the Ninth Crusade by Joinville") |
| Thibaut (Barons') | Americana chronological table 1829–33 (reprints 1835–60) | Jenks's *Comprehensive Commentary* (1838, 1860); *Chicago Tribune* 1907 |
| Gregory X's projected crusade (1274) | Colquhoun 1851; Beazley 1890 | American Cyclopaedia 1873 ("sought to evoke a ninth") |
| Other | — | Gilbert 1886 ("all thoughts of a ninth Crusade", after 1272; the 1882 printing says "eighth"); Howells 1895–96 (the name put on 1202–04); Anderson 1944 (a ninth in 1344, a tenth in 1353) |
| Edward alone, Tunis not mentioned | Masonic lore 1857 to Outhwaite 1935 | *Indian Freemason's Friend* 1857 and Yarker 1872 ("after the ninth crusade, A.D. 1272"); *The Academy* 1874; G. W. Cox 1887; EETS *Godeffroy* 1893; Parry 1920 ("1270-1272. Ninth Crusade: Edward I of England", with Louis's first crusade the eighth) |

Metaphors take a growing share after 1860: the Palestine Exploration Fund as "The Ninth Crusade" (*The Builder*, *Athenaeum*, *Spectator*, December 1867); the Crimean War as "a sort of ninth Crusade" (*Protestant Episcopal Quarterly Review*, 1855); the Russo-Turkish War (*Christian Herald*, 1878); Du Bois's "this Ninth Crusade" of the Northern teachers (*Atlantic*, 1901; *The Souls of Black Folk*, 1903, and reprints), which presupposes eight medieval crusades ending with St. Louis; temperance, the NAACP (*The Crisis*), church fund-raising (1924); and a December 1917–1918 newspaper cluster that fits Allenby's capture of Jerusalem but was not read.

### 5.2 Rise and fall

Edward's crusade enters an English numbered count through the Tunis-and-Edward ninth: Russell (1831), then the English nine of Townsend (1862), Perry (1865), Cox (1874) and EB9. EB9 made it standard reference matter on both sides of the Atlantic, and the cheap chronologies (the Self-Instructor 1882, Gay's 1891, the county atlases 1892–1936) printed "Ninth Crusade, by Louis IX. and Edward, Prince of Wales" for half a century. Their shared error, "Prince of Wales", a title created in 1301, marks the chain.

The fall comes with EB11 (Barker names Edward's expedition and excludes it from the numbering, r29) and the modern eight in Wells (1920), EB14 (1929), Nuttall (1923) and Langer (1940, "the second of King Louis IX and Edward of England"). The Edward-centered ninth outlived the count that produced it, in English national histories and popular books (Lupton, Cox, Parry, Outhwaite): when English writers told Edward's story, the ninth became his. That usage, not a nine-crusade scheme, is the bridge to the later "Edward = ninth". The explicit modern split, Tunis the eighth and Edward the ninth in one count, was not found before 1945. This corrects the interim conclusions, which dated the Edward-alone ninth from Scott-Giles (1979): the Edward-alone ninth is a century older, the split is not.

## 6. Lines of conversation

The documented lines (copying of eight or more words, shared errors, or explicit citation; `data/citations.csv`, `data/strand_d2/conversation_edges.csv`):

*The English Henry VI nine.* Mills 1820 → Townsend 1862 → Perry 1865 → Cox 1874 → EB9 1877 → Swinton's Canadian revision 1883 (copies EB9) and Boyce 1884 (lists Cox) → Desmond 1902 → Historians' History 1904 (copies Mills's text). The ninth itself is Russell's (1831), not Mills's.

*The cheap-chronology chain.* Townsend 1862 → Universal Self-Instructor 1882 → Gay's 1891 → county atlases 1892–1936, marked by "Edward, Prince of Wales".

*Nine with Frederick seventh* (`nine_F7`). Rees c. 1808, Mary Milner 1847, Johnston's atlas 1880, Parker 1915.

*Ten.* Mackay 1841 (Louis and Edward the tenth), the Americana table, Goodrich's report "Some writers make ten" (r34).

*Frederick-fifth seven.* Earliest English witness Stebbing (Edinburgh, 1830); then the Penny Cyclopaedia 1837, Chambers's 1868–1901, Anderson 1870, Emerton (variant), Fisher 1885 (with Ploetz's translation, 1883–1905), Nelson's 1917, Alzog, the Americana from 1918 (r39).

*German six.* Americana 1830 → Collier's 1921 (copied); Kurtz (Edinburgh, 1864) with L2 7.

*Gibbon seven.* Goodrich, Chepmell, the Student's Gibbon, Tout, Gilbert (Toronto 1882).

*Moréri eight.* Haydn, Robson's Michaud, Bloss, Fredet, Boyd 1892, Collier.

*Barons' sixth.* Procter, Swinton 1874, American Cyclopaedia 1873, Adams 1883 (whose table names the alternatives, r41).

*Modern eight.* Greene (US, 1851), White (Edinburgh, 1858) and Beale (London, 1858) are the earliest English-language witnesses found; then Taylor's 1858 table, Gilman 1874 (Henry VI and 1202 under one fourth), Myers 1885, the Christian Brothers' compendium (Quebec 1875, French school line), Mombert 1894, Ludlow 1896, the Catholic Encyclopedia 1908, Barker 1911, Wells 1920, Nuttall 1923, EB14 1929, Langer 1940.

*Numbering only to the Fifth.* Oman (1898; read in the 1924 text), Myers's *General History* (1889; read 1906 and 1921), Previté-Orton (1916; and 1937), Paetow (1917, after Röhricht), CMH vol. 5 (1926). A British and American academic practice of the 1890s–1920s: number to the Fifth, then name by leader ("the Crusade of St. Louis").

Echoes without copying: Barker's 1911 footnote follows Procter's (r29, r31); Willson (1854) follows G. P. R. James and changes his fifth to the fourth.

The edge table: 81 edges among English rows; the citing work agrees with the cited on every shared slot in 33, partly in 19, disagrees in 13, shares no slot in 7, and 9 have no slots to compare.

## 7. National differences

*Scotland.* Edinburgh firms kept the older reference counts (EB to 1877 and its reprints to 1902; Johnston's nine; Nelson's Collier) but also issued the new ones early: Stebbing's Frederick-fifth (1830), White's modern eight (1858), Kurtz's German count (1864), Chambers's Frederick-fifth (1868). The Edinburgh Encyclopaedia (1830) numbers nothing.

*England.* London carried the Henry VI fourth in popular history (Mills, Robson's Michaud, Perry, Cox, Mackay, Haydn) and C 4 in scholarship (Hallam, Procter, Pears, Stubbs, Archer, Barker).

*United States.* C 4 dominates from the 1830s; the American reference works had C 4 by 1873, a generation before the Britannica. The Henry VI fourth survives in the Catholic school line, in reprints (Haydn, Robson's Michaud, Bloss), in Newman's Baptist *Manual* (1899) and in the Historians' History (1904). American reference works were the most varied: German six (Americana 1830, Collier's 1921), Barons' sixth (American Cyclopaedia, Johnson's), Frederick-fifth seven (New International 1902, Americana 1918), modern eight (Langer 1940).

*Canada.* Canadian printings lean to the Henry VI fourth when American ones had left it: Haydn (Toronto 1898), Collier (Toronto 1869, 1872), Swinton revised from EB9 (Halifax 1883). The Christian Brothers' compendium (Quebec 1875) has C 4 and Edward inside the eighth; Gilbert (Toronto 1882) has Gibbon's seventh; Ontario's authorized histories (1886, 1891, 1910, 1915) number nothing.

*Ireland.* Dublin printings of church and national history only: Reeve (1837, Henry VI fourth; the English Catholic line, from Fleury by inference), Newman's *Lectures on the Turks* (1854, no numbers), Lingard (Duffy, 1874, no numbers). No Irish school book (National Board readers, Christian Brothers' class-books) was found.

## 8. The 2022 paper, retested

*Crimean War.* A cluster of titles in 1852–56 (Robson's Michaud, Bloss, Busk, Rule, the Procter printings, Jacob) fits Crimean-era demand, and the war was called "a sort of ninth Crusade" in 1855. But these books carry older counts; the war explains reprinting, not a change in numbering.

*Mills's template.* Partly confirmed. Mills's Henry VI eight is the base of the English nine, and the Historians' History copies his text in 1904. The ninth itself is Russell's (1831), and Mills does not call his count nine.

*Mombert.* Not first: the modern eight is in Greene (1851), White and Beale (1858).

*Stevenson as the first to number only five.* Fails: Stevenson quote-marks numbers through the eighth (r32). Numbering only to the Fifth is attested before him in Oman (1898) and Myers (1889), and after him in Previté-Orton, Paetow and the CMH.

*Barker as canonizer.* Confirmed in the narrow sense: EB11 fixed the modern eight in the Britannica and ended its Henry VI fourth. Not in the wide sense: the modern eight was sixty years old in English, and American reference works kept other counts into the 1920s.

*Corrections to the paper's table.* Stebbing (both expeditions are fourth; the fifth is D+F). Perry is G. G. Perry, not "Walter C. Perry", and gives Edward his own unnumbered chapter, not E 9. Mackay's ten is confirmed. Adams's *Wars of the Cross* is coded from its tables (Barons' sixth) where the paper coded the narrative (Henry VI fourth); both readings are in the row.

## 9. Corrections made in this pass

- `1865-walter-c-perry`: author George Gresley Perry; F 6; nine_H6; the 1840-dated copy merged into it.
- `sd2-1830-stebbing-chivalry`: corrected from vol. 2 (H6+C 4, D+F 5, L1 6, L2 7).
- `sd-1841-mackay-delusions`: L1 9, L2 10, E 10; family `other`.
- `1923-ernest-barker`: E cleared (matches EB11); EB9 E 9 and Barker E conflicts resolved in `reconciliation/conflicts.csv`.
- `sd2-1853-bloss-heroines`: unsupported F cleared.
- Three Edinburgh imprints (Chambers's 1868 and 1901, Collier 1860) recoded to Scotland; Lingard (Dublin, Duffy) to Ireland.
- Excluded: the DLI "New Columbia Encyclopedia" copies dated 1935 (the 1975 edition) and a modern generated "Michaud abridged, 1839".
- `sd2-1883-lupton-concise`: the classifier's "metaphor" label replaced by the Edward reading.

## 10. Not reached

EB 1938 and 1944 (lending copies); the Milman edition's crusade volume; CMH vols. 4 and 6 (no usable text); the New Schaff-Herzog crusade volume; McClintock and Strong (copy lacks the headword); Encyclopaedia Perthensis (CROISADE article not located), Londinensis, Everyman's (vol. 4 has no text), Harmsworth (no copy found), Beeton, Brewer, Blair; Milner, Robertson and Gieseler church histories (wrong volumes); Knight; Dickens vol. 2; Ridpath; Abbott; Dutton (1877); Belloc (1937), King (1931), La Monte (1932), Lamb's *Iron Men and Saints* (lending copies); Irish National School and Christian Brothers' books. Of 23 encyclopedia volumes searched for an uppercase CRUSADES headword, the article was found and read in three (Edinburgh vol. 5; Nuttall 1923 and 1930); the misses (Johnson's 1876 and 1881, Chambers's 1888 and 1923, New International 1917, Americana 1904, Everyman's 1913–14) need a case-insensitive pass. About 80 "ninth crusade" items stay unclear (mostly periodicals) and 30 have no text layer; the December 1917 cluster is unverified.

## 11. Next steps

1. Decide whether the D2 attribute fields become `works.csv` columns (the author's call; they live in `data/strand_d2/attributes.csv` until then).
2. Case-insensitive headword pass on the eight encyclopedia volumes missed; read Johnson's 1876 and Chambers's 1888 and 1923 to close the reference series.
3. Read the December 1917 newspaper cluster for Allenby and the "ninth crusade".
4. Irish school books outside archive.org (needs another library; HathiTrust is blocked to the browser).
5. Hand-code the 22 rows in `data/numberings_unparsed.csv`.
6. Borrow and read EB 1938/1944 and Lamb's *Iron Men and Saints* (lending copies; to be returned the same session).

## Files

`data/strand_d2/`: `frame.csv`, `attributes.csv`, `fourth_by_decade.csv`, `fourth_pivot.csv`, `fourth_series.csv`, `gibbon_table.csv`, `edward_timeline.csv`, `edward_firsts.csv`, `conversation_edges.csv`, `national.csv`, `census_archiveorg_titles.csv`, `ninth_crusade_hits_by_work.csv`. `data/usage/archiveorg_d2_*.csv`. Scripts `scripts/d2_lib.py`, `scripts/d2_block1_2026_11_28.py` … `d2_block6_2026_11_28.py`, `scripts/d2_block4_legacy_attrs_2026_11_28.py`, `scripts/d2_analyses.py`.
