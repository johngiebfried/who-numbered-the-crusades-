# Codebook

Version 0.1, 8 November 2026. Wikipedia section added the same day.

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
