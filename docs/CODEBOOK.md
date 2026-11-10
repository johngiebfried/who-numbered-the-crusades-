# Codebook

Version 0.2, 10 November 2026. Version 0.1 of 8 November, with the Wikipedia section added the same day; fields for the search protocol added 10 November.

## expeditions.csv

| Field | Meaning |
|---|---|
| `expedition_id` | Short code used everywhere else: E1, E2, E3, H6, C, CH, NAV, D, F, B, L1, L2, E |
| `label` | Plain name |
| `start`, `end` | Years |
| `leader_or_target` | For disambiguation |
| `modern_number` | Number in the modern one-to-eight sequence, if any |
| `notes` | Known splits and alternative counts |

Add new expeditions only when a work numbers them (for example the 1101 expeditions, or Peter I of Cyprus's attack on Alexandria in 1365).

Proposed additions from the Wikipedia sub-project (not yet added): `PEO` People's Crusade (1096), `C1101` Crusade of 1101, `ALX` Alexandria (1365; Spanish Wikipedia's "Décima cruzada"), `NIC` Nicopolis (1396), `VAR` Varna (1443–44). Only ALX is numbered anywhere so far.

## works.csv

One row per work, edition or translation that a number is taken from.

| Field | Meaning |
|---|---|
| `work_id` | `year_sort` plus a slug of the author or title. Never reused. |
| `label` | Short title for display |
| `author` | As on the title page; translators noted in `label` |
| `year_label` | Date as it should be shown, including ranges and editions |
| `year_sort` | Single year for sorting: first year of publication of the edition checked |
| `language` | Language of the text checked |
| `tradition` | Country or school of transmission (France, Germany, Germany (in English), Wikipedia...) |
| `genre` | Universal history, School, Reference, Popular history, Scholarship, Church history, Chronology, Syllabus, Catalog, Translation variants |
| `numbering_shorthand` | Counts in the key notation below |
| `how_verified` | Edition and place the number was read |
| `verification_level` | `full_text`, `contents`, `snippet`, `secondary`, `paper_table`, `unverified` |
| `research_pass` | Which pass added the row: review, citation, german, four-language, origin... |
| `notes` | Free text |

### Shorthand notation

Expedition code followed by the ordinal: `C 4, D 5, F 6, L1 7, L2 8`. A plus sign means two expeditions counted as one: `D+F 5`. Quotations follow in double quotes. Anything else is free text and goes to hand-coding.

An ordinal in parentheses is an alternative count the same source gives: German Wikipedia's navbox is `F 5 (6), L1 6 (7), L2 7 (8)`.

## numberings.csv

Derived by `scripts/derive_numberings.py`. One row per work and expedition.

| Field | Meaning |
|---|---|
| `work_id` | From works.csv |
| `expedition_id` | From expeditions.csv |
| `ordinal` | Number given |
| `shared_with` | Other expeditions counted under the same number |
| `source` | `derived` from shorthand or `manual` from numberings_manual.csv |

Planned additions: `status` values `named` and `unnumbered` for expeditions a work discusses without a number, and `explicitly_excluded` (as Lévi Alvarès excludes Frederick II, or Pierer the 1202–04 expedition). The Wikipedia pass suggests a fourth, `aside`, for a number given only in passing ("sometimes counted as the Ninth") or in brackets; pending the author's decision.

## evidence.csv (to build)

`work_id`, `expedition_id` (optional), `quote` (original language, under 50 words), `translation`, `page`, `url`, `edition_checked`, `verification_level`, `checked_by`, `checked_on`.

## citations.csv

`citing_work_id`, `cited` (work_id or author name), `relation`, `evidence`, `confidence` (`documented`, `inferred`, `untested`).

## Wikipedia tables (data/wikipedia/)

Separate from works.csv: a Wikipedia page is a moving text, so its rows are revisions, not editions. Full field lists in `data/wikipedia/README.md` (not yet committed; see the research log).

| File | One row per |
|---|---|
| `yearly_counts.csv` | page and 1 July sample (revision in force), with `highest_ordinal`, `count_family`, `stated_count`, `numbering_shorthand`, `barons_named`, revision link |
| `article_creation.csv` | article or template: first revision, first real article revision, title at creation |
| `title_moves.csv` | page move, with `kind` (`rename_numbering`, `rename_other`, `capitalization`, `numeral_form`) |
| `ordinal_titles_2026.csv` | ordinal title in each language and what it is now |
| `key_edits.csv` | dated edit that changed a count, title or coverage |
| `count_statements.csv` | explicit count stated in the text, with sample range |

`count_family`: `nine`, `eight`, `german_seven`, `german_seven_bracketed`, `partial`.

## Fields added 10 November 2026 (search protocol, step 1)

Added to `works.csv` and used in every new table. Existing rows get them as they are re-checked.

| Field | Meaning |
|---|---|
| `enumerates` | `yes` (numbers the crusades), `no` (names or narrates only), `partial` (one or two ordinals in passing) |
| `stated_count` | The total the text states ("on compte huit", "seven times"), recorded apart from slot assignments. Blank if none. "8 (sections)" when the total is only implied by numbered headings |
| `census_frame` | The closed frame the row belongs to: `strand_a_fr_en`, `strand_a_de`, `strand_b_fr_1800_1842`, `strand_c_sweep`, `panel_1770_1930`, `school_series`. Blank if found outside any frame |
| `scheme_family` | One of the codes below |
| `signature_match` | `modern`, `near_modern` (three or four of the five signature slots right) or `no` |
| `differing_slots` | For anything but `modern`, the signature slots that differ (fourth, fifth, sixth, seventh, eighth) |

### Signature (frozen; protocol section 2)

Modern eight = fourth 1202–04; fifth 1217–21 (Andrew of Hungary and/or Damietta); sixth Frederick II 1228–29 counted on its own; seventh Louis IX 1248–54; eighth Tunis 1270 and the last number. No number for Henry VI, the Barons' Crusade or Edward. Fourth = 1204 together with sixth = Frederick II separates it from every rival.

### scheme_family codes

| Code | Slots | Example |
|---|---|---|
| `modern_eight` | C 4, D 5, F 6, L1 7, L2 8 | Bouillet 1842 |
| `near_modern` | three or four signature slots right | Schöll 1830 (eighth unnumbered) |
| `moreri_eight` | H6 4, C 5, D+F(+B) 6, L1 7, L2 8 | Moréri, Trévoux, Chambers, EB2–8, Courtin |
| `moreri_eight_variant` | Moréri slots with a different sixth | Saint-Allais 1816 (sixth = 1217) |
| `nine_F7` | H6 4, C 5, D 6, F 7, L1 8, L2 9 | Rees c. 1808 |
| `nine_H6` | Henry VI fourth, running to nine | Cox 1874, EB9 |
| `barons_sixth` | C 4, D 5, B 6, L1 7, L2 8 | Proctor, American Cyclopaedia |
| `larousse_eight` | D 4, F 5, B 6, L1 7, L2 8 (C unnumbered) | Larousse 1869 |
| `german_six` | D 4, F 5, L1 6 | Brockhaus 1837, Americana 1830 |
| `german_seven` | C 4, F 5, L1 6, L2 7 | Pütz, Weber, Ploetz |
| `german_seven_variant` | German seven with other merges | Penny Cyclopaedia 1837 |
| `stated_only` | a total, no slots | Basnage's Furetière 1701, EB1 1771 |
| `none` | no ordinals beyond the first | Encyclopédie 1754, Haydn 1844 |

## Strand A tables (data/strand_a/)

`entries.csv`: one row per edition read of a dictionary or encyclopedia entry. Fields: `entry_id` (`sa-<year>-<slug>`), bibliographic fields, `headword`, `access` (how it was read), `url`, `verification_level`, `title_page_checked`, the fields above, one column per expedition code (`H6`, `C`, `D`, `F`, `B`, `L1`, `L2`, `E`) holding the ordinal, `highest_ordinal`, `organized_by` (dates, pontificates, numbered sections, chronological table, leaders), `stemma_parent`, `parent_evidence` (documented by shared wording, or inferred), `quote` (original language, under 50 words), `notes`, `checked_on`. Two expeditions with the same ordinal were counted as one.

`not_reached.csv`: works and editions in the frame not yet read, with the reason.

`data/search_log.csv`: one row per search (date, corpus, query, date filter, hits, hits examined, works added, searcher). Negative searches stay in.

## Work note template (notes/works/<work_id>.md)

```
# <label>

- Edition checked:
- Link:
- Verification:

## Numbering
## Quotations
## Sources cited by the author
## Notes
```
