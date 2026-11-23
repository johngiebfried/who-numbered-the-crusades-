# Gaps pass: the ten gaps in the conclusions audit

23 November 2026. One session, browser only (Google Books text layer, Gallica SRU/ContentSearch/ALTO, archive.org full-text search and djvu text). New rows: 15 in `data/strand_b/entries.csv` (8 French schoolbook rows, 6 pre-Koch "roots" rows, 1 contents-only row), 20 in the new `data/strand_b/entries_de.csv`, 1 in `data/strand_a/entries_de.csv`, 4 in `data/strand_d/entries_en.csv`. New tables: `data/reasons/reasons.csv` (27 explicit justifications), `data/usage/archiveorg_ordinal_counts_en.csv` (decade counts). Search log rows dated 2026-11-23.

## Result

The modern eight has a birthplace and nearly a birthday. In 1820 the official course outline for history in the Paris collèges, the *Tableau sommaire du cours d'histoire générale* issued under the Commission d'instruction publique and written by Desmichels and Trognon, numbers seven: the 1202 crusade fourth, Andrew II's expedition of 1217 named but not numbered, Frederick II fifth, Louis IX sixth and seventh. In 1823 Desmichels's *Tableau chronologique de l'histoire du moyen âge*, written "pour servir à l'étude et à l'enseignement ... dans les collèges de l'Université," numbers eight: 1202–04 fourth, Andrew and John of Brienne fifth, Frederick II sixth, Louis IX seventh, Tunis "huitième et dernière." Same author, same publisher (Louis Colas), same classroom, three years apart. No comment accompanies the change. A baccalauréat cram manual by "professeurs de l'Académie de Paris" (Delalain, 1824) copies Desmichels's headings word for word a year later, and his *Précis* carries the scheme through 1827 and into a Hachette co-edition by 1834. Bouillet (1842) inherits it; he did not make it.

The answer to the title question is therefore no longer "Paris reference works, 1842" but "a Paris history teacher writing for the new Université course, 1820–23." Koch's 1771 slots for four to seven survive inside it, and the Moréri tradition's "huitième et dernière" for Tunis supplies the eighth.

## Gap by gap

**A1. The merger moment. Closed, to within a three-year window.**

| Year | Work | Scheme | Row |
|---|---|---|---|
| 1815 | Loriquet, *Histoire ecclésiastique par demandes et par réponses*, 3e éd. | Moréri type: Henry VI fourth (to 1197), 1202 fifth, Damietta sixth (1219), Louis seventh and eighth; Frederick unnumbered | `sb-1815-loriquet-hist-eccl-3e` |
| 1818 | Caillot, *Tableau des croisades* | Moréri type (Celestine III's fourth; "huitième et dernière") | `sb-1818-caillot-tableau-croisades` (snippet) |
| 1820 | Desmichels and Trognon, *Tableau sommaire du cours d'histoire générale* (Commission d'instruction publique) | the seven the project calls `german_seven` | `sb-1820-desmichels-trognon-tableau-sommaire` |
| 1823 | Desmichels, *Tableau chronologique de l'histoire du moyen âge* | modern eight, complete | `sb-1823-desmichels-tableau-chronologique` |
| 1824 | *Manuel complet des aspirans au baccalauréat ès-lettres* | modern eight, copied from 1823 | `sb-1824-manuel-aspirans-bac` |
| 1827–35 | Desmichels, *Précis de l'histoire du moyen âge* (1827; 4e éd. Colas and Hachette 1834; Brussels 1835) | modern eight | three rows |

Title page of the 1823 book viewed. The verso of the half-title lists the Colas series it belongs to: chronological tables for ancient history (Poirson and Caix), Roman history (du Rozoir), modern history (Trognon and Desmichels), synchronic tables (Boismilon), and a forthcoming modern table by Ragon, all "professeurs aux collèges royaux." Voss (*Das Mittelalter im historischen Denken Frankreichs*, 1972, p. 92, snippet) calls Desmichels's 1823 *Tableau* the first of the French school textbooks on the Middle Ages. Larousse (1870) and a 1910 Var genealogy give "Paris, 1822," so a printing dated 1822 may exist; the copy read is dated 1823.

What is still inference: that Desmichels took slots four to six from Koch. The 1823 slots match Koch's exactly, and Koch's *Tableau* circulated in Paris editions (1807; Schöll's revision, 1823), but Desmichels names no source and the book has no preface. Also inference: that the 1820 seven came from Gibbon (see C6).

**A2. The two roots. Narrowed.**

- Maimbourg's *Histoire des croisades*, second part (1686), opens in 1195 with "cette quatrième Croisade." Henry VI is fourth in Maimbourg, as the 2022 paper said. Gallica OCR is too poor to confirm his higher numbers.
- OCR search of Moréri's 1674, 1681 and 1683 editions and the 1689 *Supplément* finds no numbered crusades. This supports Strand A's finding that the eight enters Moréri after Maimbourg, but the negative is provisional.
- Moréri's eight reached English and German reference books intact: Broughton's *Historical Dictionary of All Religions* (London 1742; German translation 1756, read at full text) has Henry VI fourth, the 1202–04 contingent fifth, Damietta and Frederick II fused as a sixth "begun 1228," Louis IX seventh. Hoff (1787) copies Broughton's sentence.
- Other pre-Koch counts are independent of Moréri: Lenfant (1724) numbers Henry VI fifth and runs to an eighth; Velly (1755) counts only French expeditions and makes Louis IX's first the fifth; Fleury's index (1758) puts Damietta sixth. Lenglet du Fresnoy's *Tablettes* number nothing.
- What Koch corrected is now clear in outline. His "On en compte proprement sept" (1771) answers the Moréri eight: it drops Henry VI, splits Damietta from Frederick II, and stops at Louis IX's first. Which book Koch read is still not known; Strasbourg's German compendia remain unsearched.

**B3. Reasons table. Built.** `data/reasons/reasons.csv`, 27 rows, 1701–2001. Three findings:

1. Before 1900 almost nobody gives a reason. Authors report custom ("on compte," "they reckon," "généralement," "l'usage le plus général") or change the slots silently. Desmichels's switch of 1820–23, the moment that matters most, has no comment at all.
2. The few pre-1900 arguments are about single slots: Lévi Alvarès (1835) refuses to count Frederick II's voyage; Pierer (1857) says the 1202–04 expedition is "usually not counted at all"; Larousse (1869) gives Andrew's expedition the fourth "plus généralement"; Myers (1885) notes that counting Henry VI makes nine.
3. After 1900 the reasons turn against the whole scheme, in a steady sequence of phrases: "unanimous consent" for only the first four (1902), "arbitrary" (Bréhier 1908), "conventionally ... their distinctness cannot be maintained" (Chambers's 1926), "for the sake of convenience" (1935), "arbitrary—a conventional highlighting" (McSorley 1946), "customary" (Pernoud 1960), "lacks all consistency" (Mayer 1965), "conventional for the movement was essentially continuous" (Chambers's 1966), "not particularly helpful" (Russell 2000), "differs widely" (Laiou and Mottahedeh 2001). The scheme was being disowned for a century while it was being used.

**B4. The fall. Partly answered, and the premise needs revising.** Two kinds of evidence:

- Explicit disowning (B3 above) begins in reference works in 1902–08, not in monographs, and reaches the field's standard survey with Mayer (1965).
- A crude usage proxy: archive.org full-text document counts per decade for each English ordinal phrase (`data/usage/archiveorg_ordinal_counts_en.csv`). "Sixth Crusade" per "Fifth Crusade" drifts down from 0.88 (1840s) to 0.56 (2010s). "Seventh Crusade" per "Fifth Crusade" rises from 0.32 to 0.81. "Crusade of Frederick II" never exceeds a fifth of "Sixth Crusade."

So in general print there is no fall at five. The sixth weakens slowly; the seventh gets stronger. The stop at five is a habit of specialists, visible in descriptive chapter titles (Setton's *History*, vol. 2, 1962: "The Crusade of Frederick II," "The Crusades of Louis IX"; not re-read this pass) and in Mayer's verdict. The essay should say "specialists stopped numbering after the Fifth" and cite the disowning sequence, not claim that usage at large stopped.

**C5. France 1842–1914. Not worked this pass.** The 1823 result moves the French question back twenty years and makes 1842–1914 a diffusion question, not an origin question.

**C6. Germany and the German seven. Narrowed, with a surprise.**

German usage 1756–1830 is Moréri type or Gibbon type, not the German seven:

- Moréri type (Henry VI fourth or 1202 fifth): Broughton trans. (1756), Beck (1790), the 1790 *Abriß der Kirchengeschichte*, Pütter (1795), Becker's *Weltgeschichte für die Jugend* (1804–19, Louis IX seventh), Schneller (1810–41, whose sixth is the Children's Crusade).
- Gibbon type (1202 fourth, Andrew fifth, Frederick unnumbered, Louis sixth and seventh): the German Gibbon (1791, 1805–06), Herder's *Ideen* (1792), Collin's Vienna *Jahrbücher* (1818).

The German seven (Frederick II fifth, Louis IX sixth and seventh) first appears in German schoolbooks found here in 1834 (Fiedler), then the *Handbuch der allgemeinen Weltgeschichte für Schule und Haus* (1835, 1838, 1845), Uschold (1839), Streit (1842), Haas (1844), Weber's *Lehrbuch* (1849), Dietsch (1854), Kurts (1860). Several merge Andrew and Frederick into one fifth ("1217–1229"). A third German habit counts Louis IX fifth (Stüve 1833; Schaefer's memorization tables 1851–54).

The surprise is the date. The German seven is attested in the 1820 Paris programme fourteen years before any German witness found. Its shape is Gibbon's seven with the fifth slot moved from Andrew to Frederick, or with the two merged. A working hypothesis: the "German seven" is a Gibbon-derived school seven that circulated in both countries, not a German invention. The family name `german_seven` should be reconsidered (see DECISIONS).

All German schoolbook rows are snippets from full-text search highlights. None is page-verified.

**C7. Cantù. Still open.** Confirmed only that the 1842 *Storia universale*, vol. 11, heads a chapter "Sesta Crociata" under Honorius III (Damietta sixth), and that the French translation of 1854 ("soigneusement remaniée par l'auteur") pairs "Cinquième et sixième croisade" in one chapter. Which Turin edition switched, and why, needs the 1847–51 volumes.

**D8. Edward alone as "Ninth" before 2003. Answered: yes, twice.** C. W. Scott-Giles, *The Wimsey Family* (1979): the mice in the arms date from "the Ninth Crusade, when Gerald de Wimsey accompanied Prince Edward." Brandon Toropov, *The Complete Idiot's Guide to the Popes and the Papacy* (2002): "The Ninth Crusade (1271–1272) was led by Prince Edward of England." Earlier English ninths are Tunis or Tunis plus Edward: Russell (1831, "Ninth Crusade—Louis IX. and Edward I."), Perry (1840), Milner (1847). So Edward-alone-as-Ninth existed in popular print before Wikipedia, but late and thin. Search limit: archive.org full text only; 880 hits, 100 examined.

**D9. Verification. Partial.** Title pages viewed or read this pass: Desmichels 1823 (image), the 1820 *Tableau sommaire* (ALTO text). Full-text reads: Desmichels 1823 pp. 63–66, the 1824 *Manuel* pp. 67–68, Loriquet 1815 pp. 70–72, Broughton 1756. The German block is snippet-level and is the next verification job.

**D10. Bibliographic databases.** For the author (IMB, RI-OPAC, JSTOR); not attempted.

## What changes in the conclusions

Replace the claim template in `2026-11-browser-pass.md` with:

> The modern eight is first attested complete in C.-O. Desmichels, *Tableau chronologique de l'histoire du moyen âge* (Paris: Colas, 1823), a textbook for the history course of the Paris collèges royaux. Three years earlier, the course's official outline, by Desmichels and Trognon, still counted seven, with Frederick II fifth. The fourth to seventh slots of the 1823 scheme are Koch's (1771); the numbered eighth at Tunis comes from the French tradition descending from Moréri. The scheme was copied into baccalauréat manuals by 1824, co-published by Hachette by 1834, and reported as general usage by Bouillet and the *Complément* of the Académie dictionary in 1842.

## Next

1. Find the 1821–22 Université history programme or question lists, and any 1822 printing of the *Tableau chronologique*. This decides whether the switch was the programme's or Desmichels's.
2. Page-verify the German block, starting with Fiedler 1834, the 1835 *Handbuch*, and Weber 1849.
3. Search German school histories 1800–1833 for a Frederick-fifth earlier than 1820.
4. Cantù's Turin editions 1847–51 (C7).
5. Setton vol. 2 and Runciman vol. 3 chapter titles, read directly (B4).
