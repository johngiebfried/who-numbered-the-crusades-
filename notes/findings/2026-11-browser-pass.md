# Browser pass: the five open items

13 November 2026. This pass reworks the five reads at the end of `2026-11-decision-point-2.md`, using the built-in browser: archive.org text, the DTA transcription, MDZ's full-text and IIIF search, and the page images at the Bibliothèque Diderot. The rows are in `data/strand_a/entries.csv`, `entries_de.csv`, `data/strand_b/entries.csv` and `data/panel/entries_fr.csv`, all checked 2026-11-13.

## Result

The slots of the modern eight were not invented in Paris around 1840. They are Koch's, and they are printed in his first edition of 1771. The French contribution was to add a numbered eighth at Tunis to Koch's "seventh and last." That step is attested in three Paris works of 1842, and the dictionary that reports it calls the result "l'usage le plus général."

## The five items

**1. Koch before 1823.** This is settled. Koch's *Tableau des révolutions de l'Europe* (Lausanne, and Strasbourg: Bauer, 1771; title page read in the OCR text), pp. 64–65, reads:

> "On en compte proprement sept ... La quatrième en 1202 ... La cinquième en 1217, par André, Roi d'Hongrie. La sixième en 1228, par l'Empereur Frédéric II. La septième enfin, en 1248, par Louis IX."

The fourth to seventh slots of the modern eight are therefore Koch's. They are not Schöll's, and they are 71 years older than Bouillet. The same seven reappears in the following works, each with "septième et dernière" and an unnumbered Tunis:

- Schöll's chronology in *Histoire de la littérature grecque profane*, t. 8 (1825).
- Saigey's *Précis de chronologie* (Hachette, 1834).
- Lamp's *Tables synchronistiques* (1839).

Saigey matters most, because the Koch seven was already in a Hachette school-market book eight years before Bouillet. The French text of the 1823 edition was not needed and was not read.

**2. Hübner 1704.** This is settled, and the answer is that there is nothing to identify. The DTA transcription of the whole entry says only:

> "Man zehlet acht Croiſaden, deren die erſte gegen das Ende des eilfften Jahr-hundert geſchehen. Die letzte aber trug ſich Anno 1270. zu, und verrichtete ſelbige Ludwig der Heilige."

There is no list, so the question of which eight Hübner meant has no answer. The row is `stated_only`, like Basnage 1701. Maier's quotation is accurate.

**3. *Encyclopédie des gens du monde*, t. 7 (1836).** This is settled, and the bracket does not move. The CROISADES entry is narrative and draws on Wilken, Michaud and Mills. Its highest numbered crusade is "la troisième croisade générale." OCR searches for the fourth to eighth ordinals find nothing in the entry.

**4. Lefranc.** Partly settled. The 3rd edition (Lyon and Paris: Périsse, 1837; the title page image was viewed; it is not 1838, as the frame had it) keeps the 1834 scheme in its table of contents:

- fourth: "Quatrième croisade (1195–1198)," that is, Henry VI;
- fifth: 1202–04;
- sixth: 1228–29;
- seventh: the 1248 crusade;
- eighth: "la huitième et dernière croisade" in 1270.

The 7th edition of 1841 is still unread. Google Books answered with a captcha, which was not attempted.

**5. Duruy 1861.** This is settled. The first edition (Paris: L. Hachette, 1861; title page read in the OCR text) has the modern eight: the fourth is 1201–04, the fifth is Andrew II's, the sixth is Frederick II's, and the "Septième et huitième croisades" are 1248 and 1270. One line reads "La première croisade fut bien différente des sept autres."

## Found on the way: a third 1842 witness and a statement of custom about the slots

The *Complément du Dictionnaire de l'Académie française* (Paris: Firmin Didot frères, 1842) gives the modern eight under CROISADE: fourth 1202–04, fifth Andrew 1217, sixth Frederick II 1227, seventh 1248, eighth Tunis 1270. It then adds:

> "Quelques historiens comptent pour la quatrième croisade l'expédition que les croisés entreprirent en 1197 ... Ces historiens admettent par conséquent huit croisades, sans compter celle de saint Louis contre Tunis. Nous avons suivi l'usage le plus général."

This is the first statement of custom found that concerns the slots and not merely the total. It names the Henry VI fourth as the minority practice in 1842.

The publisher is Didot, which also published Le Bas. The preface says the direction of the work was first entrusted to Narcisse Landois, "professeur au collège Bourbon," which is Bouillet's collège. So all three 1842 witnesses lead back to the same small Paris world of the Université, Hachette and Didot.

Two further hits are leads for task 2, read from OCR snippets only:

- Ruelle and Huillard-Bréholles, *Histoire générale du moyen-âge* (1842): "SIXIÈME CROISADE (1222–1229)" and "septième … huitième." This is probably another modern eight.
- Abel Hugo, *France historique et monumentale* (1839): Frederick II sixth, with Tunis as the "Neuvième croisade."

## Revised bracket (claim template)

> The modern eight is attested complete by 1842, in three Paris works: Bouillet (Hachette), Le Bas t. 6 (Didot), and the *Complément du Dictionnaire de l'Académie* (Didot), which calls it "l'usage le plus général." Its fourth to seventh slots are older: Koch, *Tableau des révolutions de l'Europe* (1771), counts exactly those four and ends at seven. The same seven is in Schöll (1825, 1830), Saigey (Hachette, 1834) and Lamp (1839). The French schoolbooks read from 1834 to 1837 (Lefranc 1834 and 1837; Lévi Alvarès 1835) and the reference works up to 1838 have other schemes. The step from Koch's seven to the modern eight, which is the addition of Tunis as a numbered eighth, falls between 1839 and 1842 in what has been read.

## Caveats

- The MDZ rows were read through OCR search hits, which give line-level context, and not from page images. They are coded `snippet`. Before citing the *Complément*, view MDZ canvas 335 of bsb10627876.
- Koch 1771 and Duruy 1861 were read from archive.org OCR. Their title pages were checked in OCR, not on the image.
- The MDZ full-text search reaches only BSB's holdings. It is a strong Strand C corpus for French books of 1800–45, but it is not a census.

## Next

1. View *Complément* canvas 335 and its title page.
2. Read Ruelle and Huillard-Bréholles 1842, slots four and five.
3. Read Abel Hugo 1839 in full (a nine).
4. Read Lefranc's 7th edition (1841).
5. Run the MDZ sweep for "septième et dernière croisade" and "huitième et dernière croisade" for 1771–1842, to find the first French book that adds Tunis to Koch's seven.
