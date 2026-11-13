# Strand A in German, from Hübner (1704)

13 November 2026. Task 4. Data: `entries_de.csv` (1 row), `not_reached.csv` (9 works), `search_log.csv` (40 rows). Done by Claude, one session, no second coder.

## 1. Result

This pass did not reach the German reference texts, so it answers only half of the main question and none of the decade question.

**Hübner 1704: the count of eight is confirmed at secondary level only.** Maier (in Weber, ed., *Crusade: The Uses of a Word*, 2024, p. 24 n. 39) cites cols. 321-323, headword "Croisade," with a cross-reference "Creutz-Zug suche Croisade." I read the footnote in the open-access OAPEN PDF. It gives "Man zehlet acht Croisaden, deren die erste gegen das Ende des eilfften Jahr-hundert geschehen" and "Die letzte aber trug sich Anno 1270. zu, und verrichtete selbige Ludwig der Heilige." So Maier's report is accurate as a report: eight, first at the end of the eleventh century, last 1270 under Louis IX. Attested by Hübner 1704 (via Maier); absent in 0 other German works checked, because none was read.

**Which eight is unknown.** The endpoints fit both the Moréri eight (eighth = Louis IX, 1268/70) and the modern eight (Tunis, 1270). Only slots 4 to 6 discriminate, and the entry's middle was not read. I cannot say whether Hübner follows Basnage's Furetière (1701), Trévoux or Moréri. Neither the "Moréri eight" nor a German-original scheme is supported yet. Also unproven: that Hübner knew Basnage; the nearness of 1701 and 1704 is no evidence of descent.

**Edition where German reference works drop the eight:** not found. No German reference entry from 1709 to 1911 was read in this pass.

## 2. Decade table

| Decade | Works read | Scheme | Edition where it changes |
|---|---|---|---|
| 1700s | Hübner 1704 (secondary) | `stated_only` (8; last = 1270) | not known |
| 1710s to 1820s | none | not read | not known |
| 1830s | none read in this pass | works.csv has Damen 1834 and Brockhaus 1837 as `german_six` (D 4, F 5, L1 6); not re-read, not recoded | not known |
| 1850s | none read | works.csv has Pierer 1857 (D 4, F+B 5, L1+L2 6) and Herder 1854 (no numbers); not re-read | not known |
| 1900s-1910s | none read | works.csv has Brockhaus 1911 as `german_seven`; not re-read | not known |

The works.csv entries are the earlier pass's readings and are shown only to hold the places; they are not evidence of this pass. No new scheme code was needed.

## 3. What was tried and why it failed

- DTA's Hübner viewer needs JavaScript, so the fetch returns nothing. MDZ's resolver was refused (provenance), bavarikon returned an access-denied bot page, Münster and Halle PDFs sit behind bot checks. Wikisource pages (Hübner, Zedler, MKL1888, Brockhaus) return "url_not_found" through the fetch tool, and the Wikisource Hübner pages carry no scan links anyway.
- The only zeno.org page that surfaced in any search (Brockhaus 1837, Kreuzzüge) never loads: the server redirects https to http and the tool will not follow it. No other zeno page surfaced, so none could be fetched under the access rules. Search results return titles only, so no snippet-level rows were possible.
- Fetched and not relevant: Düsseldorf PDFs (Brockhaus 7th ed. front matter, Wilken, E. A. Schmidt's 1847 *Grundriß*), Meusel, Pock, Schiller. Schmidt 1847 numbers first to fifth crusades in section headings; it is a schoolbook outside this frame and I did not follow it.

## 4. Proposed protocol amendments

1. Allow fetching exact URLs that are recorded in the repository (works.csv, entries.csv), or list zeno.org/DTA/MDZ as approved hosts; otherwise German tasks cannot start.
2. Search results here carry no snippets, so "snippet" rows can only come from fetched pages. State this in section 6.
3. For Hübner, the cheapest fix is a person with a browser opening DTA at cols. 321-323 (see `read_list.md`); a ten-minute job that settles the main question.

## 5. Not reached

Everything in the brief's list except the Hübner footnote: Hübner primary and later editions, Zedler, Brockhaus 1809 to 1890s, Pierer, Meyer, Herder, Ersch-Gruber, Wetzer and Welte, and the re-reading of the five works.csv German rows. See `not_reached.csv`.
