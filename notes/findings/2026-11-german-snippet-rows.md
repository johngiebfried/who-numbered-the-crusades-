# The German snippet rows, verified

28 November 2026. Browser session, archive.org djvu text (BSB/MDZ scans; one Kraków and one Warsaw scan for the atlas). It finishes direction B for the German schoolbook block: the five rows coded `frederick_fifth_seven` on 23 November from search highlights alone. Script: `scripts/verify_german_snippets_2026_11_28.py` (5 rows updated, 1 row added, 5 search-log rows).

## Result

Four of the five are full Frederick-fifth sevens (C 4, F 5, L1 6, L2 7) at full text: Haas 1844, Beitelrock 1853, Dietsch 1854 and Kurts 1860. Beitelrock's family code, which rested on "der sechste Kreuzzug unter Ludwig IX." alone, is confirmed rather than cleared. The fifth row, Stein's *Neuer Atlas der ganzen Erde* (Leipzig: Hinrichs, 1842, the row filed under Streit), is not a seven at all. Its two tables count differently, and the row is split.

| Row | Read in | Slots | Note |
|---|---|---|---|
| Haas, *Populäre Kirchengeschichte* (1844) | 11287230bsb, Zeittafel pp. 348–350 | C 4, F 5, L1 6, L2 7 | "1270. Siebenter und letzter Kreuzzug." Narrative numbers only the second and third; Andrew (1217) unnumbered |
| Beitelrock, *Grundriß* (2nd ed., Dillingen, 1853) | 10031114bsb, Zeittafel | C 4, F 5, L1 6, L2 7 | "1228 Friedrich II. erlangt auf dem fünft. Kreuzzuge … Jerusalem." Narrative (pp. 194–197) numbers only the second and third |
| Dietsch, *Grundriß*, Theil 2 (Leipzig: Teubner, 1854) | 10031690bsb, §§ 79–86 and Zeittafel | C 4, F 5, L1 6, L2 7 | "§ 85. Der fünfte Kreuzzug 1227–29. Friedrich II." Damietta narrated unnumbered. Section headings and table agree |
| Kurts, *Geschichtstabellen* (Leipzig: Weigel, 1860) | 10348116bsb, synchronistic tables | C 4, F 5, L1 6, L2 7 | Andrew II's "erfolgloser Kreuzzug" unnumbered. The sixth is read from OCR broken across columns and needs the page image |
| Stein atlas (1842), German table | jbc.bj.uj.edu.pl.NDIGKART022297 | F 5 only | Family code **cleared**: F 5 alone is shared with `german_six` and `larousse_eight` |
| Stein atlas (1842), universal table (new row) | same | F 4, L1 5 "u. letzter" | Coded `other` |

## The atlas

The *Neuer Atlas der ganzen Erde* is Stein's school atlas, with maps by Streit and others; the 1847 and 1854 title pages credit its historical tables to K. Th. Wagner. Its universal-history table runs: "1096. Erster Kreuzzug … 1147. Zweiter … 1189. Dritter … 1228. Vierter Kreuzzug. Erneuerung des Königr. Jerusalem (— 1244) … 1248. Fünfter u. letzter Kreuzzug nach Ägypten (— 1250). Ludwig IX." The 1202–04 expedition appears only in the Italian table, as the capture of Constantinople by the crusaders, without a number. Tunis appears in the French table as "Kreuzzug gegen Tunis," also unnumbered. The German table of the same atlas has "1228. Fünfter Kreuzzug — 1229. Friedrich II. im Banne." The 1852 printing (Warsaw copy; universal table dated Leipzig 1849) has the same wording, so the conflict survived from the 1842 printing to the 1849 table.

The five-count is a Holy-Land-and-Egypt count: it numbers the expeditions that fought the Muslims and leaves out the one that took Constantinople. I have not seen this scheme elsewhere in the project's tables. **Firm** for the wording (two printings), **open** for its source.

## What this does to the German argument

The narrowed claim of 27 November stands and gets stronger. German school texts of 1834–60 fixed Frederick II as fifth, and the full seven is now read at full text in six of them: Fiedler 1834, the *Handbuch* 1835 (merged form), Haas 1844, Beitelrock 1853, Dietsch 1854 and Kurts 1860. Uschold 1839 and Weber 1847–49 stop at five. The atlas shows that a single school book could carry two counts at once.

**A pattern (inference, flagged).** In Haas and Beitelrock the full seven appears only in the chronological table; the narrative numbers the second and third and stops. Dietsch numbers in both, but in section headings, which are a table in prose. This parallels the French case of 27 November, where the course table numbered and the examination question did not. The numbers lived in the tables. If that holds across the strand, `organized_by` deserves a value that separates table from narrative within one book, and the census should code the two separately.

## Not done

- Kurts's sixth on the page image (MDZ 10348116).
- Haas's title page and confession; the 1846 edition.
- The source of the atlas's five-count: Wagner's own tables, or an earlier edition of the atlas (it was in its 24th edition by 1847).
