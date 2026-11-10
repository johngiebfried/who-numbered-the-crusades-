# Project plan

*Who Numbered the Crusades?* — John Giebfried, University of Vienna. Started 8 November 2026.

## 1. Goal

Explain how the crusades acquired numbers, and show it. The project produces three linked outputs from one dataset:

1. An article for *Digital Medievalist* that argues the case and presents the method and data.
2. An open, citable dataset of crusade numbering in printed works, archived with a DOI.
3. An interactive site that lets readers see how numbers shifted by date, language, genre and country.

*Digital Medievalist* is the target from the start, so the data model, method and visualizations are part of the argument, not an appendix to it.

## 2. Thesis as it stands

The paper's original answer (Mombert, 1894) fails. Numbering is early modern, and the modern one-to-eight sequence is a nineteenth-century convention of reference books and schoolbooks. The earliest modern eight found so far is Bouillet's Hachette dictionary of 1842, which looks like a synthesis of Gibbon's fourth and fifth with the sixth to eighth of French school counts such as Lefranc's (1834). Cantù re-split his own chapters to match it by 1851, Duruy carried it in 1861, and American schoolbooks took it up from 1885. Other countries kept other counts, each fixing a different point: Tunis as the eighth in France, Frederick II as the fifth in Germany, Henry VI's expedition as the fourth in British popular histories into the 1870s.

## 3. Scope

**Chronology.** Three zones.

- *Prehistory, single narrative: the first crusade through Gibbon (1788).* Orderic, Carion and Bullinger, Pasquier, Fuller, Maimbourg, Müller, Gibbon. Treated as one story, since the counts were few and passed between a small set of authors.
- *Core survey: Gibbon to 1945.* After Gibbon the story splits into national chains, and the dataset aims for breadth: every language and genre that can be reached.
- *Coda: after 1945.* Not surveyed systematically. Notes on modern scholarship (Setton, Runciman, Riley-Smith, Tyerman), modern popular histories, library subject headings, school materials, and the Wikipedia sub-project.

The 1945 end date is a survey boundary. In practice, full-text access thins out after about 1929 in the US and earlier for European works under copyright, so 1930–45 will rest more on snippets, catalogs and contents pages. Each row records how it was verified.

**Languages and countries.** As wide as possible, in tiers.

- Tier 1, core chains: English (Britain, US), French, German, Italian.
- Tier 2, already sampled: Spanish, Dutch and Flemish, Greek.
- Tier 3, to add: Portuguese, Swedish, Danish, Norwegian, Polish, Czech, Hungarian, Russian, Catalan, Latin school texts.
- Tier 4, if time allows: Romanian, Croatian and Serbian, Ottoman Turkish and Arabic (as a check on whether the western numbers were adopted).

**Genres.** Universal histories, school texts, reference works, popular crusade histories, scholarly histories and source editions, church histories, chronologies and syllabi, translations (coded separately from their originals).

## 4. Where things live

| Place | Role |
|---|---|
| GitHub repository `who-numbered-the-crusades` (public) | Canonical home: data, notes, drafts, code, site |
| Local folder `~/Documents/Who Numbered the Crusades?` | Working clone of the repository |
| Claude project "Who Numbered the Crusades?" | Plan, research log and decisions mirrored for any new conversation |
| Claude Docs | Drafts and memos for comment; finished text is committed to the repo |
| Zenodo | DOI for each data release |

Rule: anything a later conversation needs to know goes into the repo (`docs/RESEARCH_LOG.md`, `docs/DECISIONS.md`) and the project.

## 5. Data model

See `docs/CODEBOOK.md`. Five tables:

- `expeditions.csv`: the controlled list of expeditions (First through Edward, plus Henry VI, the Children's Crusade and Las Navas).
- `works.csv`: one row per work or edition, with language, country tradition, genre, a shorthand of its numbering, and how it was verified.
- `numberings.csv`: one row per work and expedition: the ordinal given, or named, unnumbered, merged. Derived from the shorthand by `scripts/derive_numberings.py`, overridden by hand-coded rows.
- `evidence.csv` (to build): the quotation, page, URL and verification level behind each numbering.
- `citations.csv`: who cites whom, marked documented, inferred or untested.

The 85 works in the November 2026 review corpus are migrated as version 0.1.

## 6. Visualizations

1. **Timeline of counts.** Each work as a dot by year, colored by count family (Michaud, Gibbon, German seven, French eight, modern eight, other). Shows the modern eight appearing in 1842 and spreading.
2. **Which expedition holds which number.** For each ordinal, the expedition filling it, by decade and language. The clearest picture of drift.
3. **Citation network.** Michaud, Gibbon, Bouillet, Cantù, Duruy, Myers and their readers, with edges marked by evidence strength.
4. **National comparison.** Small multiples by language, with each tradition's fixed point.
5. **Ngram panel.** "Fourth" to "Ninth Crusade" and their equivalents across languages.
6. **Work explorer.** Search and filter works; each shows its count, quotations and links.
7. **Wikipedia history** (sub-project, below).

Stack: a static site with Observable Plot or D3 reading the CSVs, published with GitHub Pages. Prototypes can be built as Claude artifacts first.

## 7. Phases

| Phase | Work | Output |
|---|---|---|
| 0. Setup | Repository, project, codebook, licenses, migration of the review corpus | v0.1 dataset |
| 1. Close the origin | Bouillet's source; the Cantù edition that switched; French texts 1834–42 | Origin section of the article |
| 2. Transmission to English | Translations or direct reading of Bouillet, Cantù, Duruy; British school texts 1850–1900; Ngram by language | English chain |
| 3. National chains, tier 1–2 | Fill French, German, Italian, Spanish, Dutch, Greek to 1945; GEI-Digital for German schoolbooks | Dataset v0.5 |
| 4. Visualization prototype | Views 1 and 2 first, since they carry the argument | Site draft |
| 5. Tier 3 languages | Portuguese, Scandinavian, Central and Eastern European | Dataset v0.8 |
| 6. Wikipedia sub-project | See below | Chart and short section |
| 7. Article | Draft from data and figures, in the author's voice | Submission to *Digital Medievalist* |
| 8. Release | Data release and DOI, site live, article submitted | v1.0 |

## 8. Sub-project: Wikipedia, 2001 to the present

Flagged as a separate research task: `docs/subprojects/wikipedia-numbering.md`. How English and other Wikipedias have numbered the crusades over a quarter century, when articles such as the Barons' Crusade were created, and how list articles and templates changed their counts.

## 9. Method notes

- Every number traces to a quotation and a verification level. Google Books snippets are evidence of a heading or a passage, not of a whole book's scheme.
- Translations are separate works with their own rows, since translators changed numbers.
- Metadata dates need checking against title pages. Example: Google Books dates Bouillet's Brussels edition to 1833.
- Absence of a number (naming by leader, as Wilken and Raumer did) is coded, not left blank.

## 10. Open questions

Kept current in `docs/RESEARCH_LOG.md`; the search design is `docs/SEARCH_PROTOCOL.md`. At setup: Bouillet's source and any earlier French text with his list; the Cantù edition between 1844 and 1851 that changed his count; Avendaño's full list (1846); how the eight reached English; Runciman vol. 3; Proctor's London text; Mailly (1780); Kugler, Prutz and Sybel; a systematic German schoolbook count.
