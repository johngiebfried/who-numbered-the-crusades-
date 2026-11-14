# Strand D: the crusade count in English, Britain and the US, 1788–1924

14 November 2026. This pass was done by browser. It has three parts: a backward chain from Wikipedia, a reference panel, and school books and translations. The new rows are in `data/strand_d/entries_en.csv` (19 rows, with `country` and `channel` columns). They supplement the older English rows in `data/works.csv`: Mills, Proctor, Cox, Swinton, Myers, Perry, Mombert, Ludlow, Schaff and the Duruy translation.

## Result

English had no count of its own. Until about 1910 it carried at least five imported counts side by side:
- the Moréri eight, from the French dictionaries;
- the German seven, from Brockhaus;
- the Michaud/Mills nine;
- Gibbon's seven;
- the modern eight.

The modern eight came in through French schoolbooks in translation and through a few school authors. It did not come through the reference books. Every major English-language encyclopedia read stayed with an older scheme until Bréhier (1908) and Barker's article in Britannica's 11th edition (1911). The *New International Encyclopaedia* (New York, 1917) says outright that "the first four Crusades are the only ones to which the same numbers are assigned by unanimous consent."

## The backward chain

The chain runs: Wikipedia 2001 ← Bréhier, *Catholic Encyclopedia* (New York, 1908) ← French scholarship. Bréhier writes: "It has been customary to describe the Crusades as eight in number … This division is arbitrary."

Britannica, in parallel:

| Edition | Count |
|---|---|
| 1st–8th (1771–1854) | Moréri eight |
| 9th (1877, Cox) | Nine: Henry VI fourth, Richard of Cornwall seventh, "the ninth and last crusade" |
| 11th (1911, Barker) | Modern eight: "So ended the Eighth Crusade" |

Barker's notes rest on German scholarship: Röhricht, Kugler, Prutz.

Gibbon (1788) has "the seven crusades": 1202–04 fourth, Damietta fifth, Louis IX sixth and seventh, and Frederick II unnumbered. He is a British witness to the 1202 fourth, seventeen years after Koch, but he is not its source.

## The panel: reference works, by country

| Country | Work and date | Count |
|---|---|---|
| Britain | *Chambers's Encyclopaedia*, 1868 and 1901 | German seven: Frederick II fifth, Louis IX sixth and seventh |
| Britain | Haydn's *Dictionary of Dates*, 1878 and 25th ed. 1910 | Moréri eight: "IV. 1195, by emperor Henry VI" |
| Britain | Britannica 9th ed., 1877 | Nine |
| Britain | Britannica 11th ed., 1911 | Modern eight |
| US | *Encyclopaedia Americana*, 1830 and 1838 | German six |
| US | *Encyclopedia Americana*, 1918–24 | German seven: "What is more usually called the Fifth Crusade was led by Frederick II" |
| US | *American Cyclopaedia*, 1873 | Barons sixth |
| US | *Johnson's Universal Cyclopaedia*, 1890s | Another eight: Frederick fifth, Thibaut sixth, Damietta unnumbered |
| US | *New International*, 1902 and 1917 | German seven, with the "unanimous consent" sentence |
| US | Bréhier, *Catholic Encyclopedia*, 1908 | Modern eight |

## School books and translations: the route the modern eight took

| Date | Work | Count | Channel |
|---|---|---|---|
| 1835 | Willard (US) | "a fourth crusade" only | — |
| 1841 | Mackay (GB) | Michaud/Mills nines | — |
| 1847 | Milner (GB) | Michaud/Mills nines; "THE NINE CRUSADES," noting that Gibbon counts differently | — |
| 1855 | Kerney (Baltimore, Catholic) | Moréri eight | — |
| **1851** | **Greene, *History and Geography of the Middle Ages* (New York: Appleton)** | **Modern eight** | Preface: "chiefly taken from a popular French work which has … received the sanction of the University." The earliest English modern eight found. |
| **1858** | **Beale, *Student's Textbook* (London: Bell and Daldy)** | **Modern eight** (Barons folded into the sixth) | The earliest British one found. Source unknown. |
| 1875 | Tainsh, *Improved Manual* | Modern eight | Duruy's wording translated |
| 1878 | Gazeau (New York: Catholic Publication Society) | Modern eight | A French Catholic textbook in translation, with exam questions |
| 1883 | Steele (Barnes, New York) | Modern eight; outline heading "The Eight Crusades" | — |
| 1885 on | Myers (Ginn) | Modern eight, with a nine noted in passing | — |
| 1891 | Duruy (Holt), in translation | Modern eight | — |
| 1890s | Mombert, Ludlow | Modern eight | — |

The German seven also came into English through translated German manuals: Weber (1853), Ploetz (1883), Schaff (1907).

## What it means

1. **In English the modern eight is a translation phenomenon.** Its first carriers are French Université schoolbooks in English: Greene in 1851, then Tainsh, Gazeau and Duruy. That ties the English story to Strand B. Identifying Greene's French source would put another dated French schoolbook from before 1850 into the Strand B frame.
2. **Schools led and reference works lagged.** American school texts had the eight by the 1850s–80s. American encyclopedias were still printing German or Barons-type counts in 1924. In Britain, Beale had the eight in 1858, while Chambers's, Haydn and Britannica 9th ran other schemes until 1910–11.
3. **Two canonizing moments, both around 1908–1911.** Bréhier for the US and Catholic channel, and Barker in Britannica's 11th edition for Britain. Wikipedia's 2001 article descends from Bréhier.
4. **Confession is not decisive.** The Catholic Kerney (1855) kept the Moréri eight. The Catholic Gazeau (1878) has the modern eight because it is translated from French.

## Not reached, and next steps

- **HathiTrust** full-text search was blocked by its bot check, which was not attempted. **Google Books** was captcha-limited.
- **Greene's French source.** Identify it: archive.org's alternate copy id (`historyandgeogr00rendgoog`) points to Rendu. Then date its first edition with the modern slots.
- **Beale's source**, through her preface and the Cheltenham connection.
- **Britain between 1858 and 1911.** Mangnall, Tytler, Keightley, Freeman, Oman, Collier (coded "eight Crusades" but not read in detail), and Yonge.
- **Chambers's 1923–27 and the Americana after 1924**, to date when each switched.
- **US newspapers** (Chronicling America) as a check on the textbooks. "Crusade" is very noisy in the temperance era, so phrase pairs would be needed.
- **Verification.** All rows rest on archive.org OCR. Title pages were checked in OCR where marked. The auto-coding by nearby keywords was checked by hand for every row listed above.

## Follow-up reads (14 November, later)

**Greene's source is identified, and it reaches back into Strand B.** Greene's 1851 text is Ambroise Rendu's *Histoire du moyen âge*. This is part 2 of Ansart and Rendu, *Cours d'histoire et de géographie, rédigé spécialement pour l'usage des écoles normales primaires… d'après le Programme arrêté… par le Conseil Royal de l'Instruction Publique* (Paris: H. Delloye; 1st ed. 1840–41; 2nd ed. 1841–42). The wording matches:

| Rendu (2nd ed.) | Greene (1851) |
|---|---|
| "La cinquième et la sixième croisade prirent naissance en Allemagne" | "The fifth and sixth crusades began in Germany" |

Rendu's text cross-refers "V. quatrième croisade, 42" (the Latin empire) and "Voyez la huitième croisade, 43" (Tunis). Ansart's *Nouvelles Tablettes chronologiques* (1842) has the full modern eight: "Quatrième croisade… Baudouin… Sixième… Frédéric II… Septième… saint Louis… Huitième et dernière croisade."

So the modern eight is in an official-programme schoolbook for teacher-training colleges by 1841–42 at the latest, and probably in the 1840–41 first edition. That edition's part 2 is not digitized; it is at the BnF under shelfmark G-18709. This is the strongest candidate yet for the French origin, and it fits the protocol's hypothesis that the swap entered through the Université programmes.

**Beale's source** remains unknown. She writes: "to quote authorities would have been inconsistent with my plan."

**British school texts, 1859–1899:**
- Mangnall (1859) does not number.
- Yonge, *Landmarks: Middle Ages* (1864), has modern slots four to seven.
- Collier (1872) says "There were eight Crusades," but its count is the old dictionary eight with Damietta dropped.
- Freeman (1873) numbers only to the fourth.
- Tout, *Empire and the Papacy* (2nd ed. 1899), is Gibbon's seven: Louis IX sixth and seventh, Frederick II unnumbered.

British usage was therefore split three ways until Barker in 1911: Gibbon in the universities, Moréri/Mills in the popular books, and the modern eight in a few school authors (Beale, Yonge).

**Switch dates.** *Chambers's* still had the German seven in the 1908 printing. The 1950s–60s *Chambers's* and the 1932 and 1953 *Americana* are lending-only on archive.org and were not reached, so both switch dates remain open.

## The last Henry VI fourth (search of 1900–1960)

**Method.** Full-text search of archive.org for 1900–1960, for "fourth crusade" together with Henry VI, Celestine or 1195. About 1,500 results were scanned. Only those where the terms fall within 250 characters of each other in a highlighted passage were kept (64). Each of those was then read.

**Result.** The Henry VI fourth survives into the 1910s in four places, then disappears from the corpus.

| Date | Work | Count |
|---|---|---|
| 1901 | Cox, *The Crusades*, 12th ed. (Longmans) | The nine |
| 1909 | *Collegiate Course for Home Study* (US), following W. F. Collier's Nelson text | "THE FOURTH CRUSADE. (1195–1197.) The emperor Henry VI…" |
| 1910 | Haydn's *Dictionary of Dates*, 25th ed. | Moréri eight |
| 1915 | Billy Parker, *The Bloody Trail of Romanism* (US anti-Catholic tract) | Michaud/Mills nine, citing both |

In addition:
- The Michaud translations were still being reprinted in 1900.
- *The Great Events by Famous Historians* (1904) is internally split: its introduction has the modern slots, while a headnote keeps "The Fourth Crusade (1196–1197)."

After about 1915, every hit in the corpus treats Henry VI only as background to the 1202–04 Fourth Crusade, for example Previté-Orton (1937) and La Monte (1949).

**Caveats.**
- Dates come from archive.org metadata, and Indian DLI reprints are unreliable. A "History of the British Empire" dated 1919 carries Collier's chronology ("The Fourth Crusade 1195–97") but is probably a 19th-century Nelson book.
- Lending-only volumes could not be read.
