# Search protocol: first modern eight, and how it spread

10 November 2026. Design for the two questions that answer the title. Candidate works named here are places to look, not findings; none has been checked unless the research log says so.

## 1. Two questions, two designs

- **Q1, priority.** Earliest work with the complete modern eight. A priority search can never prove a first. It can produce a bracket: the earliest attestation, and behind it a documented census in which the scheme is absent.
- **Q2, diffusion.** How that scheme became the default. This needs rates inside defined populations and documented transmission, not more early instances.

The premise of Q2 needs testing, not assuming. On the project's own evidence the eight was not a global standard in 1900: German schoolbooks kept seven, Cox and EB9 had nine. The claim to test is narrower: standard in French, Italian, Catholic and American reference and school books by c. 1900, and in British ones after EB11 (1911).

## 2. The signature (freeze before searching)

A work has the **modern eight** only if all of these hold:

| Slot | Must be | Rules out |
|---|---|---|
| Fourth | 1202–04, Constantinople | Maimbourg, Michaud, the old dictionary eight (Henry VI, 1195) |
| Fifth | 1217–21, Andrew of Hungary and/or Damietta | Mills, Michaud, the German seven |
| Sixth | Frederick II, 1228–29, counted on its own | Gibbon (unnumbered), German seven (fifth), Cantù's first edition, the American Barons' sixth |
| Seventh | Louis IX, 1248–54 | Gibbon and German counts (sixth) |
| Eighth | Tunis, 1270, and the last number | Nines; Gibbon and German counts (seventh) |

No number for Henry VI, the Barons' Crusade or Edward. The sixth slot is the discriminator: Fourth = 1204 together with Sixth = Frederick II separates the modern eight from every rival scheme in the corpus.

Code partial matches (three or four slots right) as `near_modern`, with the differing slot named. Record `stated_count` ("on compte huit") separately from slot assignments, as in the Wikipedia tables.

## 3. Search strings

Run each as phrase plus proximity term, with ordinals also as numerals (6e, VIe, 6., VI.) and period spellings (croisade/croizade, long s in eighteenth-century OCR, Kreutzzug, Fraktur misreads).

| Language | Sixth slot | Eighth slot | Stated count |
|---|---|---|---|
| French | "sixième croisade" + Frédéric / 1228 | "huitième croisade" + Tunis | "huit croisades", "on compte … croisades" |
| English | "sixth crusade" + Frederick / 1228 | "eighth crusade" + Tunis | "eight crusades" (also "croisades") |
| German | "sechster Kreuzzug" + Friedrich | "achter Kreuzzug" | "acht Kreuzzüge", "sieben Kreuzzüge" |
| Italian | "sesta crociata" + Federico | "ottava crociata" + Tunisi | "otto crociate" |
| Spanish | "sexta cruzada" + Federico | "octava cruzada" + Túnez | "ocho cruzadas" |

Negative control in each language: Fourth + Henry VI / 1195, to map the scheme being displaced.

## 4. Q1: three strands, in this order

**Strand A. Stemma of the reference entry (1690–1870).** Collect the "Croisade(s)" entry from every edition of every general dictionary and encyclopedia: Furetière, Trévoux, Moréri, Chambers, the *Encyclopédie* and *Encyclopédie méthodique*, Britannica 1–8, Feller, Chaudon and Delandine, *Encyclopédie moderne*, *Dictionnaire de la conversation*, *Encyclopédie des gens du monde*, Saint-Allais, Bouillet (every edition from 1842), Dezobry and Bachelet, Brockhaus, Pierer, Meyer, Ersch-Gruber. Transcribe the enumeration passage, collate, and draw the stemma. Entries copy each other, so the edition where the list changes is findable the way a scribal variant is. About 50–70 entries, all enumerable in advance. This tells you whether Bouillet wrote his list or inherited it.

**Strand B. Census of the French gap (1800–1842).** Every French work in a genre that is forced to enumerate:
- dictionaries and encyclopedias (from Strand A);
- chronological tables and historical atlases (*L'art de vérifier les dates* and its 1818–19 reissue, Lesage/Las Cases, synoptic tables);
- question-and-answer schoolbooks and *précis* for the collèges;
- baccalauréat manuals and the official programmes and question lists of the Université;
- prize essays on the crusades (Heeren, Choiseul-Daillecourt, c. 1808–09).

Build the frame from a catalog first, then check each work. Hypothesis: the Henry VI / Frederick II swap was made in a programme or exam list, and Bouillet, a school administrator writing for that market, reported it.

**Strand C. Blind full-text sweep, as a control.** The signature strings across Gallica, Google Books, HathiTrust, Internet Archive and MDZ, 1750–1845, in French, English, German and Italian. Purpose: catch an origin outside France or outside the forcing genres. Candidates outside France: Rotteck, Schlosser, Becker; Tytler, Mangnall, Keightley's *Outlines*, Worcester, Willard.

**Stopping rule.** Stop when (1) every work in the Strand A and B frames is coded, and (2) Strand C returns nothing earlier in two independent corpora.

**Claim template.** "The modern eight is attested complete by [work, year]. In a census of N French works of 1800–[year] that enumerate the crusades, none has it. The nearest predecessors are X (differs in the fourth) and Y (differs in the sixth). The change falls between [year of X/Y] and [year]."

## 5. Q2: diffusion

**5.1 Encyclopedia panel, 1770–1930 (the backbone).** Every edition of every major general encyclopedia in each language: a closed population, a census and not a sample. Adds to Strand A: Britannica 9–11, Chambers's, *Encyclopaedia Americana* (Lieber, built on Brockhaus), *New American* / *American Cyclopaedia*, Johnson's, Larousse, *Grande encyclopédie*, Pomba, Mellado (an adaptation of Bouillet), Montaner y Simón, Espasa, Winkler Prins, Nordisk familjebok, Salmonsen, Brockhaus-Efron, Orgelbrand, Otto, Pallas, the *Catholic Encyclopedia*, Schaff-Herzog, Wetzer and Welte. One row per edition. Output: for each language, the decade the modern eight becomes the scheme of the majority.

**5.2 School series.** Not a sample of titles: the long-running series, edition by edition (Duruy, Pütz, Weber, Ploetz, Cantù, Myers, Swinton, Fisher), weighted by number of editions. Frames: GEI-Digital for Germany, a French textbook catalog, a US schoolbook collection. Add official syllabi and exam lists for France, Prussia, the US and England.

**5.3 Transmission edges.** Translations coded as separate works (Bouillet into Spanish and Italian, Cantù into French, Spanish and German, Duruy and Ploetz into English); publisher links (Hachette); prefaces and bibliographies; text-reuse detection on the collected entries.

**5.4 Statements of custom.** A table of sentences that say what is usual: Bouillet "généralement," Pierer "gewöhnlich gar nicht gerechnet," Myers "the number increased to nine," Stevenson 1907, Bréhier 1908 "customary … arbitrary." These are direct testimony that a count had become the norm, and when.

**5.5 Mechanisms, each with a prediction.**
- *School market* (Hachette, state programmes): adoption follows programme dates; schoolbooks lead encyclopedias.
- *Catholic channel* (Cantù, Catholic schoolbooks, Bréhier): inside one country, Catholic books adopt before Protestant ones. Testable in German and Dutch schoolbooks by confession.
- *Scholarship pull* (Riant and the 1204 debate, Röhricht): the Fourth settles first everywhere, the Sixth to Eighth later.
- *American textbook market* (Myers, Ginn): US adoption precedes British.

**Definition of "standard."** In a given language: majority of the encyclopedia panel for two consecutive decades, plus at least one statement of custom, plus adoption in a syllabus or leading school series.

## 6. Evidence rules

- A row counts toward the bracket only at `full_text` with a saved page image, the edition identified from the title page, and the first edition checked where a later one was seen.
- Reference works are revised silently: date the edition read, never the work.
- Keep `data/search_log.csv`: date, corpus, query, date filter, hits, hits examined, works added, searcher. Negative results are data; every work in a frame gets a row, with `enumerates` yes/no and `scheme_family`.
- Second coder on the bracket rows and a 10% sample of the panel.
- Ngram: corroboration only, proper-name forms, never the basis of a date.

## 7. Order of work

1. Freeze sections 2 and 6. Add `stated_count`, `enumerates`, `census_frame` to the codebook.
2. Strand A (French and English entries first).
3. Strand B.
4. Strand C.
5. Encyclopedia panel.
6. School series, syllabi, translations.
7. Write Q1 as a bracket and Q2 as adoption curves with named edges.
