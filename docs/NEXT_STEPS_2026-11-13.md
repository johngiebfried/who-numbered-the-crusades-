# Next five research steps, for delegation

13 November 2026. Written at the decision point after Strand A (French and English) and the prior-literature check. Each brief below is meant to be handed whole to a fresh Opus or Sonnet session with no memory of earlier work. Give the agent this file plus `docs/SEARCH_PROTOCOL.md`, `docs/CODEBOOK.md` and `notes/findings/2026-11-strand-a.md`.

## Where the project stands

The total of eight is old: Moréri's dictionary had eight numbered crusades by 1689, with Henry VI's expedition (1195) fourth, 1202–04 fifth, and one long sixth (1213–44). Every French and English reference entry read from 1689 to 1838 keeps that scheme. The modern eight (1202–04 fourth, Damietta fifth, Frederick II sixth, Louis IX seventh and eighth) appears in two Paris reference works of 1842, Bouillet and Le Bas. Bouillet abridged an older entry and changed slots four to six without changing the total.

Three things are not established, and the five tasks go after them:

1. **Where the re-slotting was made.** The only evidence that it predates 1842 is Schöll (1830), read in fragments. (Tasks 1 and 2.)
2. **Whether the dictionary bracket holds.** Several reference works of 1836–42 are unread, and two bracket dates rest on catalog metadata. (Task 3.)
3. **How the scheme won, and where the eight came from outside France.** Larousse in 1869 still ignores Bouillet's scheme, and a German dictionary may state "eight" in 1704. (Tasks 4 and 5.)

## Order and assignment

| # | Task | Model | Size | Depends on |
|---|---|---|---|---|
| 1 | Schöll and Koch: the Franco-German hinge | Opus | small | none |
| 2 | French schoolbooks and programmes, 1816–42 | Opus | medium | read task 1's report first |
| 3 | Close the Strand A gaps and verify the bracket | Sonnet | small | none |
| 4 | Strand A in German, from Hübner (1704) | Sonnet | medium | none |
| 5 | French diffusion, 1842–1914 | Sonnet | medium | none |

Tasks 1, 3, 4 and 5 can run in parallel. Task 2 should start after task 1 reports, because task 1 decides whether the search looks for a German import or a French school invention. Every report comes back for review before its rows are merged or its claims enter the findings notes.

Opus gets the two tasks where the lead is ambiguous and the agent has to decide what a source is evidence of. Sonnet gets the three that apply a frozen codebook to a list that can be written down in advance.

## Rules for every task

**The signature.** A work has the modern eight only if all five hold: fourth = 1202–04; fifth = 1217–21 (Andrew of Hungary and/or Damietta); sixth = Frederick II, 1228–29, on its own; seventh = Louis IX, 1248–54; eighth = Tunis, 1270, and the last number. No number for Henry VI, the Barons' Crusade or Edward.

**Coding traps met so far.**
- A "fifth crusade, 1198, Innocent III" is 1202–04 under an early date. Code by the expedition described, not the year printed.
- A sixth that "began in 1228" may still contain Damietta, Richard of Cornwall and Gaza. Read to the end of the paragraph.
- Headings and running text can disagree inside one entry (*Penny Cyclopaedia*, 1837). Record both.
- "On compte huit croisades" states a total. It is not evidence for any slot. Fill `stated_count` and the slot columns separately.
- Date the edition read, from its title page. Never date the work, and never trust Google Books or archive.org metadata for a year.

**Evidence.** A row is `full_text` only if the agent read the enumeration passage itself. A search-result snippet is `snippet`. Every row carries a URL that opens the page, a quotation under 50 words in the original language, and `title_page_checked` yes or no. Works searched and found not to enumerate get a row too. Every search goes in `data/search_log.csv`, including the ones that find nothing.

**Access, as of 10 November.**
- archive.org: full OCR text downloads work (`_djvu.txt`). Best source.
- Google Books: full-view volumes can be read as text by adding `&output=text` to a page URL. The Books API is over quota; use the website.
- Gallica: search and OCR work, but requests are rate-limited after a handful. Pause between calls. Many pre-1800 scans have no text layer.
- HathiTrust: blocked by a bot check. Do not spend time on it.
- zeno.org and Wikisource: full transcriptions of several German and French reference works.
- If a source can only be reached as a page image with no text, record the URL and the page, mark it `image_only`, and list it for the author to read. Do not guess from a thumbnail.

**Claims.** No report says "first." It says "attested by [work, year]; absent in N works checked before it." Anything from the agent's own memory and not from a page it read is marked `recalled`.

**Deliverables, the same for all five.**
1. Rows in the task's CSV, using the `data/strand_a/entries.csv` columns.
2. Rows appended to `data/search_log.csv`.
3. A findings note, `notes/findings/2026-11-<task-slug>.md`, of two pages at most: result first, then evidence, then what was not reached.
4. A list of pages the author should read himself (the rows that would carry a published claim).

Work on a branch and open a pull request. Do not edit `docs/SEARCH_PROTOCOL.md` sections 2 or 6; propose amendments in the findings note.

---

## Task 1. Schöll and Koch: the Franco-German hinge

**Model: Opus. Size: small (four to six volumes).**

**Question.** Does Schöll's *Cours d'histoire des états européens* (1830) have the modern slots throughout, and did he take them from Koch?

**Why it matters.** Schöll is the only evidence that the re-slotting is older than 1842. He was read in fragments: 1202–04 is "quatrième croisade" (t. 6, p. 102), and t. 4 has "Cinquième et sixième croisades, 1217 et 1228," "Septième croisade, 1248," then "Deuxième croisade de S. Louis" with no number. Nobody has read the opening of his crusade chapter. German schoolbooks already counted 1202–04 fourth, and French books already ended on an eighth at Tunis. The working guess is that the modern eight is the French total with the German fourth, and that a Franco-German writer joined them.

**Read.**
- Schöll, *Cours d'histoire des états européens*, t. 3 and t. 4 (Paris: Gide; Berlin: Duncker et Humblot, 1830), chapter VI, "De la chevalerie, des croisades et du royaume de Jérusalem," from its first section. Google Books ids seen: `gmlHAAAAYAAJ` (t. 4), `BmtHAAAAYAAJ` (t. 6).
- Christophe-Guillaume Koch, *Tableau des révolutions de l'Europe*: the 1771 first edition, the 1807 edition, and Schöll's own revised edition (1823). That Schöll continued Koch is `recalled`; confirm it from a title page before using it.
- Heeren's prize essay on the consequences of the crusades in its French translation (c. 1808), only if Schöll or Koch cites it.

**Answer these.**
1. Does Schöll give Henry VI's expedition (1195–97) a number, name it without one, or omit it?
2. Does he state a total anywhere ("on compte … croisades")?
3. Does he number Tunis (1270) anywhere in the work, including tables and indexes?
4. Which authorities does he cite for the crusades?
5. What is Koch's count in each edition, and does it change between 1771, 1807 and 1823?

**Stop** when the five questions are answered or shown to be unanswerable from the scans available. Do not widen to other authors.

**Output.** `data/strand_b/entries.csv` rows for each edition read; findings note `2026-11-schoell-koch.md`. State plainly whether "the swap predates Bouillet" survives.

---

## Task 2. French schoolbooks and programmes, 1816–42

**Model: Opus. Size: medium (aim for 25 to 40 works coded).**

**Question.** In French books forced to enumerate, when do slots four to six change, and in what kind of book first?

**Why it matters.** This is Strand B of the protocol and the direct attack on the title question. The dictionaries did not make the change. Two Paris reference works report it in the same year, 1842, in unrelated wording, which points to a shared source in the school market. Bouillet was a headmaster (proviseur of the Collège royal de Bourbon) publishing with Hachette, "libraire de l'Université."

**Known points to build from.**
- Lefranc, *Histoire du moyen âge* (1834): Henry VI fourth, 1202–04 fifth, Frederick II sixth, Tunis eighth. Editions of 1838 and 1841 exist and their contents pages number an "huitième et dernière croisade." Whether slots four to six changed between editions is the single most useful check in this task.
- Lévi Alvarès, *Nouveaux élémens d'histoire générale* (1835): Damietta fifth, Louis IX sixth, and an explicit refusal to count Frederick II's voyage as a crusade.
- Michaud and Poujoulat's abridgment (1838) and Michaud's *Histoire abrégée* for the young (1839) keep Michaud's count (Henry VI fourth).
- Le Bas, *France: dictionnaire encyclopédique*, t. 6 (Didot, 1842): modern eight in a chronological table. Its source inside Didot's *L'Univers* series is unknown.
- Google Books matches "sixième croisade" with Frédéric in the *Annuaire du Bureau des longitudes* (1802) with no preview. Probably a false hit; check once and move on.

**Method.**
1. Build the frame before reading: list French works of 1816–42 in four genres from a catalog (BnF catalogue général, and the Emmanuelle database of French textbooks if reachable). The genres are collège *précis* and *abrégés* of medieval or French history; question-and-answer manuals and baccalauréat manuals; chronological tables and atlases (including the 1818–19 reissue of *L'art de vérifier les dates* and Lesage/Las Cases); official programmes and question lists of the Université.
2. Read the editions of Lefranc first, then authors with several editions in the window, then the rest by date.
3. Run the signature strings as a control: "sixième croisade" near "Frédéric" or "1228"; "quatrième croisade" near "Constantinople" or "1204"; "cinquième croisade" near "Damiette" or "André," all limited to 1816–42.

**Decision the agent must make and report.** For each work with the modern slots four to six, say whether it looks like a source, a copy, or independent, and on what evidence (shared wording, cited authority, publisher). Where the evidence cannot decide, say so.

**Stop** when the frame's listed works are each coded or marked unreachable, or at 40 coded works, whichever comes first. Report the frame size and the share reached.

**Output.** `data/strand_b/entries.csv`, `data/strand_b/frame.csv` (every work in the frame, read or not), findings note `2026-11-strand-b.md` ending in the protocol's claim template.

---

## Task 3. Close the Strand A gaps and verify the bracket

**Model: Sonnet. Size: small. A checklist; no interpretation needed.**

**Question.** Does the dictionary bracket (1838 to 1842) survive the unread entries, and do its dates survive a title-page check?

**Do each of these and report yes, no, or not reachable.**

1. *Encyclopédie des gens du monde*, t. 7 (Paris: Treuttel et Würtz, c. 1836), entry CROISADES. Twenty archive.org volumes were searched on 10 November and none was t. 7; try Google Books and Gallica. Code the scheme.
2. d'Harmonville, *Dictionnaire des dates* (1842–45), entry CROISADES. Code the scheme.
3. *Encyclopaedia Britannica*, 7th edition (1842), entry CRUSADES; then the 4th to 6th if quick. The 3rd and 8th have identical text.
4. Title pages: Courtin, *Encyclopédie moderne*, t. 7 (dated 1824 by Google only; id `o0FnAAAAcAAJ`); Furne's *Biographie universelle* (dated 1838 by Google only; id `G0yUbp4tTkAC`), including its volume number and the missing sections VI and VIII.
5. Furetière 1690 (Gallica `bpt6k8720514m`, view 397): confirm on the page image that "On compte 8. Croisades" is absent. The OCR is poor.
6. Le Bas, t. 6: one Michigan copy is cataloged 1841. Look for evidence of issue in installments before the 1842 title page.
7. Dezobry and Bachelet, first edition (1857): same scheme as the 1863 printing?
8. Trévoux 1704, 1721, 1732 and Moréri 1674–83: image-only scans. Attempt each once. If no text can be read, list the exact page for the author.
9. Rees's *Cyclopaedia*, vol. 10: find the issue date of the part containing CROISADE (the set is dated 1819; the part is earlier).

**Rider, separate file.** Compare English Wikipedia revision 349190657 (28 October 2001, "Crusades") word for word with Louis Bréhier, "Crusades," *Catholic Encyclopedia*, vol. 4 (1908), on New Advent. Report shared sentences and shared date ranges. The eight date ranges are known to match; the wording has never been compared.

**Stop** when the list is done. Do not add works to it.

**Output.** New rows appended to `data/strand_a/entries.csv`; rows moved out of `not_reached.csv`; a one-page note `2026-11-strand-a-gaps.md` with a table of the nine items; a half-page note on the Bréhier comparison.

---

## Task 4. Strand A in German, from Hübner (1704)

**Model: Sonnet. Size: medium (20 to 30 entries).**

**Question.** What do German reference works count, edition by edition, and is there a German dictionary eight in 1704?

**Why it matters.** Christoph Maier (in Weber, ed., *Crusade: The Uses of a Word*, 2024, p. 24 n. 39) reports that Johann Hübner's *Reales Staats- und Zeitungs-Lexicon* (1704) says "Man zehlet acht Croisaden," the first in the late eleventh century and the last in 1270. Not yet checked against the original. If it holds, the dictionary eight crossed into German within three years of Basnage's "On compte 8. Croisades" (1701). German encyclopedias of the 1830s–60s then count six and skip 1202–04, while German schoolbooks count seven. When and why German reference works dropped the eight is unknown, and the *Encyclopaedia Americana* and the *Penny Cyclopaedia* carried German counts into English.

**Read, in date order. One row per edition.**
- Hübner, *Reales Staats- und Zeitungs-Lexicon*: 1704, then two or three later editions to 1780. Which eight? Does the list match Furetière-Basnage, Trévoux or Moréri?
- Zedler, *Universal-Lexicon* (1730s), entries Creutz-Zug, Creutzfahrt, Croisade.
- Brockhaus, *Conversations-Lexikon*: every edition reachable from the first (1809–11) to the fourteenth (1890s), entry Kreuzzüge.
- Pierer, every edition reachable. Meyer, from the 1840s *Großes Conversations-Lexicon* to the sixth edition (1900s). Herder (1854–57). Ersch and Gruber, entry Kreuzzüge.
- Wetzer and Welte, *Kirchen-Lexikon*, both editions (Catholic), to test whether Catholic reference works differ.

zeno.org has full text for Brockhaus 1809, 1837 and 1911, Pierer 1857, Meyer 1905, Herder 1854 and others. Rows already in `data/works.csv` from the German pass (Damen 1834, Brockhaus 1837, Pierer 1857, Herder 1854, Brockhaus 1911) should be re-read and re-coded in the new columns, not copied.

**Search terms.** Kreuzzug, Kreuzzüge, Kreutzzug, Creutzzug, Creutzfahrt, Croisade; ordinals vierter to achter; "acht Kreuzzüge," "sieben Kreuzzüge," "sechs Kreuzzüge." Fraktur OCR confuses s and f, and k and t.

**Stop** at 30 coded entries or when the list is exhausted.

**Output.** `data/strand_a/entries_de.csv` (frame code `strand_a_de`), findings note `2026-11-strand-a-german.md` with a table by decade: which scheme each work has, and the edition in which each work changes.

---

## Task 5. French diffusion, 1842–1914

**Model: Sonnet. Size: medium (30 to 40 rows).**

**Question.** When does the modern eight become the majority scheme in French reference works and schoolbooks?

**Why it matters.** The project has assumed it was standard in France soon after Bouillet. Larousse's *Grand dictionnaire universel* (t. 5, 1869) contradicts that: it counts Andrew of Hungary's crusade fourth "plus généralement," Frederick II fifth, and the 1234–44 crusade sixth. The current *Dictionnaire de l'Académie* gives "la huitième et dernière croisade" as a stock example. Somewhere between 1869 and now the scheme won. The likeliest route is the school system: Victor Duruy's *Histoire du moyen âge* (Hachette, 1861) has the modern eight, and Duruy was minister of public instruction from 1863 to 1869.

**Read. One row per edition.**
- *Reference panel.* Bouillet at intervals (1842, 1857, 1869, 1878, 1893, 1908 or the nearest reachable); Dezobry and Bachelet (1857, 1869, 1888); Larousse (*Grand dictionnaire* 1869 and supplements, *Nouveau Larousse illustré* c. 1898–1904, *Petit Larousse* 1905 or 1906); *La grande encyclopédie* (c. 1891, entry Croisades, with its author's name); *Dictionnaire de la conversation*, second edition (1850s); *Dictionnaire de l'Académie*, 1835, 1878 and 1932–35, entry croisade (do the examples number any crusade?); Vapereau and Lalanne if they enumerate.
- *School series.* Duruy, *Histoire du moyen âge*, first edition and three later ones; Duruy's shorter school histories; the Lavisse primary-school course (1880s onward); Malet (1900s); two Catholic series of the same decades, to test whether confession matters.
- *Programmes.* The official secondary history programmes of 1852, 1865, 1880, 1890 and 1902: does any name or number a crusade? These dates are `recalled`; confirm each from the text found.

**Report.** A table by decade from the 1840s to the 1910s: rows read, how many have the modern eight, how many another scheme, how many do not enumerate. Name the first edition of each long-running work that has the modern eight, and any that changes scheme between editions. The corpus is a panel chosen in advance, so shares may be stated for the panel, and only for the panel.

**Stop** at 40 rows.

**Output.** `data/panel/entries_fr.csv` (frame codes `panel_1770_1930` and `school_series`), findings note `2026-11-french-diffusion.md`.

---

## Held for later

- Cantù's editions between 1844 and 1851, and the Italian chain.
- The route into English (Picot's reader of 1846, translations of Duruy, Myers's sources).
- The blind full-text sweep (Strand C) and the all-language encyclopedia panel.
- Reconciling the ledger, `strand_a/entries.csv` and `works.csv` into one table.
- Bibliographic databases not reachable by web search (International Medieval Bibliography, RI-OPAC, JSTOR), which the author should run himself before claiming priority in print.

## What comes back to the decision point

After tasks 1 and 3: is the origin claim "re-slotted in France between X and 1842," or "imported from the German fourth by way of Koch and Schöll"? That choice sets the frame of task 2 and the opening of the article. After tasks 4 and 5: can the article say when the scheme became standard anywhere, or only that it was attested?