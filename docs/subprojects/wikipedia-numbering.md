# Sub-project: crusade numbering in Wikipedia, 2001 to the present

Status: first pass done, 8 November 2026; second pass and scope study 9 November. Findings in `notes/findings/2026-11-wikipedia-numbering.md`, `2026-11-wikipedia-scope.md`, `2026-11-wikipedia-scope-languages.md` and `2026-11-wikipedia-2001-and-911.md`. Data tables (`data/wikipedia/`) and the site pages are not yet in the repository; see the research log.

## Question

How have Wikipedia's articles, lists and navigation templates numbered the crusades over a quarter century, and how did those choices change? Wikipedia is read millions of times a year for these articles (the stronger claim, "most-read crusade reference," is untestable), so its count is the modern descendant of the nineteenth-century dictionaries this project studies.

## Known lead (resolved)

The author recalled that English Wikipedia had no article on the Barons' Crusade (1239–41) as late as the early 2010s. Confirmed and later than remembered: the English article was created on 12 February 2016, with no earlier page, redirect or deletion under the title. The main "Crusades" article first named the expedition on 1 May 2013. French (2008) and German (2010) had articles first; Spanish 2018, Italian 2022, Dutch 2023, Greek 2026. No edition numbers it.

## Results of the first pass

- German Wikipedia aside, the editions converged on nine between 2003 and 2012. English had the first Ninth (13 April 2003); Dutch followed on 21 May 2003, added by the editor who had split the English article.
- English has since retreated to eight: "Ninth Crusade" renamed "Lord Edward's crusade" on 17 November 2019, navigation box renumbered the same day, last Ninth out of the main article in December 2021.
- German Wikipedia keeps the nineteenth-century German schoolbook seven (Damietta and Frederick II as one Fifth, Louis IX Sixth and Seventh), with the modern count in brackets in its navigation box since 2005. A German editor in 2010 called the one-to-nine sequence the "englische" count.
- Spanish alone has a Tenth: "Décima cruzada" redirects to the Alexandria crusade of 1365 (since 2018).
- Pages often state one count and use another; the data keeps both.

## Method (as run)

1. **Article creation dates.** First revision, first non-redirect revision and title at creation for 17 articles and the templates in seven languages (`article_creation.csv`).
2. **Count over time.** Revision in force on 1 July each year, 2001–2026, for the main article, navigation box(es) and the English list article (`yearly_counts.csv`), coded in project notation; explicit counts in `count_statements.csv`.
3. **Renames and redirects.** Page moves from revision histories (`title_moves.csv`); ordinal titles First to Tenth in each language as of November 2026 (`ordinal_titles_2026.csv`).
4. **Other languages.** German, French, Italian, Spanish, Dutch and Greek done alongside English; Arabic, Persian, Hebrew and nine more added later.
5. **Key edits.** Thirty-two dated edits, transitions pinned by binary search and checked against parent revisions (`key_edits.csv`).

## Questions to settle

Options and trade-offs are in the findings note. The data keeps both measures, so either choice works without recoding.

- Which to treat as authoritative when templates and articles disagree.
- How to code a number in a lead sentence ("sometimes called the Ninth") against a number in a title.
