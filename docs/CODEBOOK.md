# Codebook

Version 0.5, 28 November 2026 (evening): `nine_B7` added; the Strand D2 tables (`data/strand_d2/`) and their attribute fields described; reason kinds listed, with `attribution` and `explanation`; country code `CA`. Version 0.4, 28 November 2026: the strand tables merged into `works.csv`, which is now the single source (section "works.csv" rewritten); slot cells may hold two ordinals; `other` and `barons_sixth_variant` listed. Version 0.3, 27 November 2026: `german_seven` renamed `frederick_fifth_seven`, `gibbon_seven` added. Version 0.2 of 10 November (fields for the search protocol); version 0.1 of 8 November, with the Wikipedia section added the same day.

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

The master table since 28 November 2026: one row per edition, translation or catalog read, from every strand, panel and frame. It replaced the legacy `works.csv` (85 rows) and six entry tables (`strand_a/entries.csv`, `strand_a/entries_de.csv`, `strand_b/entries.csv`, `strand_b/entries_de.csv`, `strand_d/entries_en.csv`, `panel/entries_fr.csv`), which are frozen in `data/archive/2026-11-28-pre-reconciliation/`. Built once by `scripts/reconcile_works.py`; edited by hand from then on.

| Field | Meaning |
|---|---|
| `work_id` | Stable id. Legacy rows keep `year-slug`; strand rows keep their entry id (`sa-`, `sa-de-`, `sb-`, `sb-de-`, `sr-`, `sd-`, `pn-fr-`, `ss-fr-`). New rows: the prefix of the frame they belong to, or `year-slug` if none. Never reused |
| `alt_ids` | Ids of rows merged into this one (same edition recorded twice), separated by `;` |
| `source_tables` | Which pre-merge tables the row came from (`works`, `strand_a/entries`, ...); `;`-separated |
| `label` | Short display title |
| `author` | As on the title page; translators and editors noted |
| `work` | Full title as read |
| `edition`, `place_publisher`, `volume`, `pages`, `headword` | Bibliographic detail of the edition read |
| `year_label` | Date as it should be shown, ranges and edition notes included |
| `year_sort` | Single year for sorting: first year of the edition read |
| `language` | Language of the text read, spelled out (French, German, English, ...) |
| `tradition` | Country or school of transmission (France, Germany, Britain, US, Germany (in English), Wikipedia, ...) |
| `genre` | Universal history, School, Reference, Popular history, Scholarship, Church history, Chronology, Syllabus, Catalog, ... |
| `census_frame` | Frame(s) the row belongs to (below); `;`-separated; blank for rows found outside any frame |
| `enumerates`, `stated_count`, `stated_phrase` | As in "Fields added 10 November 2026" below |
| `numbering_shorthand` | Display text in the key notation below, generated from the slot columns for every row read under the protocol; legacy rows keep their original free text |
| `H6`, `C`, `D`, `F`, `B`, `L1`, `L2`, `E` | The ordinal the source gives each expedition. **These columns are the record**; `numberings.csv` is derived from them. Blank = no number recorded. Two expeditions with the same ordinal were counted as one. A cell holds two ordinals separated by `;` when the source splits the expedition (Cantù 1842, `D` = `5;6`: Andrew II's 1217 expedition fifth, Damietta sixth) |
| `highest_ordinal` | Highest ordinal anywhere in the slots |
| `organized_by`, `scheme_family`, `signature_match`, `differing_slots` | As below |
| `stemma_parent`, `parent_evidence` | Strand A stemma; ids resolve through `alt_ids` |
| `quote` | Original language, under 50 words |
| `how_verified` | Edition and place the numbers were read |
| `access`, `url` | How and where it was read |
| `verification_level` | `full_text`, `contents`, `snippet`, `paper_table`, `secondary`, `unverified` |
| `title_page_checked` | `yes`, `by OCR`, `half-title`, `no`, ... |
| `research_pass` | Which pass added the row (review, citation, german, four-language, origin, strand_a, strand_b, strand_d, panel) |
| `country`, `channel` | Strand D: country of publication; channel of transmission into English |
| `notes` | Free text. Merged rows prefix each source's note with its table, e.g. `[works]` |
| `checked_on` | Date of the last read |

**Merged rows.** Eleven editions were recorded in more than one table (Bouillet 1842 in three). The slot vector comes from the best-verified source. On a tie the strand row wins, but a value the other source had and the winner left blank is kept, because a blank in a strand row can mean "not recorded". Every disagreement is in `data/reconciliation/conflicts.csv`.

**Ledger.** `data/ledger/ledger_print.csv` is still hand-coded in `scripts/ledger_code_corpus.py`, with a richer cell vocabulary (`n` named, `x` excluded, `(7)` aside). `data/reconciliation/ledger_map.csv` maps each of its 78 rows to a `work_id` and lists slot disagreements. Generating the ledger from `works.csv` waits on the planned `status` values below.

### Shorthand notation

Expedition code followed by the ordinal: `C 4, D 5, F 6, L1 7, L2 8`. A plus sign means two expeditions counted as one: `D+F 5`. Quotations follow in double quotes. Anything else is free text and goes to hand-coding.

An ordinal in parentheses is an alternative count the same source gives: German Wikipedia's navbox is `F 5 (6), L1 6 (7), L2 7 (8)`.

## numberings.csv

Derived by `scripts/derive_numberings.py` from the slot columns of `works.csv` (since 28 November 2026; before that, from the shorthand). One row per work, expedition and ordinal.

| Field | Meaning |
|---|---|
| `work_id` | From works.csv |
| `expedition_id` | From expeditions.csv |
| `ordinal` | Number given |
| `shared_with` | Other expeditions counted under the same number |
| `source` | `works.csv` (the slot columns). The old values `derived` and `manual` are in the archived copy |

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

`count_family`: `nine`, `eight`, `german_seven`, `german_seven_bracketed`, `partial`. Here `german_seven` labels German Wikipedia's count (Damietta and Frederick II one fifth); the print family of the same shape is `frederick_fifth_seven`.

## Fields added 10 November 2026 (search protocol, step 1)

Added to `works.csv` and used in every new table. Existing rows get them as they are re-checked.

| Field | Meaning |
|---|---|
| `enumerates` | `yes` (numbers the crusades), `no` (names or narrates only), `partial` (one or two ordinals in passing) |
| `stated_count` | The total the text states ("on compte huit", "seven times"), recorded apart from slot assignments. Blank if none. "8 (sections)" when the total is only implied by numbered headings |
| `census_frame` | The closed frame the row belongs to: `strand_a_fr_en`, `strand_a_de`, `roots_1675_1771`, `strand_b_fr_1800_1842`, `strand_b_de_1780_1860`, `strand_c_sweep`, `strand_d_en`, `panel_1770_1930`, `school_series`. Blank if found outside any frame |
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
| `nine_B7` | C 4, D 5, F 6, B 7, L1 8, L2 9 (the modern eight with the Barons' crusade seventh) | Universal Self-Instructor 1882, Gay's 1891 |
| `barons_sixth` | C 4, D 5, B 6, L1 7, L2 8 | Proctor, American Cyclopaedia |
| `larousse_eight` | D 4, F 5, B 6, L1 7, L2 8 (C unnumbered) | Larousse 1869 |
| `german_six` | D 4, F 5, L1 6 | Brockhaus 1837, Americana 1830 |
| `gibbon_seven` | C 4, D 5, L1 6, L2 7 (F unnumbered) | Gibbon 1788, German Gibbon 1791, Herder 1792, Collin 1818 |
| `frederick_fifth_seven` | C 4, F 5, L1 6, L2 7; Andrew/Damietta named but unnumbered, or merged into the fifth (D+F 5) | Paris programme 1820, Fiedler 1834 (base form); *Handbuch für Schule und Haus* 1835 (merged form) |
| `frederick_fifth_seven_variant` | Frederick-fifth seven with other merges | Penny Cyclopaedia 1837 |
| `barons_sixth_variant` | Barons'-sixth count with other merges | Johnson's Universal Cyclopaedia 1893–99 |
| `other` | A scheme with no code; say what it is in `notes` | Stein atlas 1842 universal table (F 4, L1 5 "letzter"); Schneller 1810; Cammerer 1828 |
| `stated_only` | a total, no slots | Basnage's Furetière 1701, EB1 1771 |
| `none` | no ordinals beyond the first | Encyclopédie 1754, Haydn 1844 |

`frederick_fifth_seven` was `german_seven` until 27 November 2026. It was renamed because the scheme is attested in the official Paris programme of 1820, fourteen years before the earliest German witness found (Fiedler 1834). It is named for its defining slot, as `nine_F7` is. The Wikipedia `count_family` labels `german_seven` and `german_seven_bracketed` are unchanged: they name the count German Wikipedia uses, not the print family.

A row that stops short of the full scheme takes a family code only when its numbered slots are diagnostic. F 5 with C 4 places a row in `frederick_fifth_seven` (Weber 1847–49, which stops at five). L1 6 alone does not, because `gibbon_seven` and `frederick_fifth_seven` share it.

## Strand A tables (data/strand_a/)

(Until 28 November 2026 each strand had its own entry table with the fields below; those rows are now in `works.csv`, and the fields carried over unchanged. The description is kept for the archived copies.)

`entries.csv`: one row per edition read of a dictionary or encyclopedia entry. Fields: `entry_id` (`sa-<year>-<slug>`), bibliographic fields, `headword`, `access` (how it was read), `url`, `verification_level`, `title_page_checked`, the fields above, one column per expedition code (`H6`, `C`, `D`, `F`, `B`, `L1`, `L2`, `E`) holding the ordinal, `highest_ordinal`, `organized_by` (dates, pontificates, numbered sections, chronological table, leaders), `stemma_parent`, `parent_evidence` (documented by shared wording, or inferred), `quote` (original language, under 50 words), `notes`, `checked_on`. Two expeditions with the same ordinal were counted as one.

`not_reached.csv`: works and editions in the frame not yet read, with the reason.

`data/search_log.csv`: one row per search (date, corpus, query, date filter, hits, hits examined, works added, searcher). Negative searches stay in.

## Strand D2 tables (data/strand_d2/)

English print 1800–1945. Protocol: `notes/strand-d2-protocol.md` (with its amendments). The new fields live here, not in `works.csv`, until the author decides otherwise.

`frame.csv`: the census frame. `frame_id` (R reference, S school, P popular, H scholarly, C church and national), `frame`, `country`, `genre`, `author`, `title`, `editions_targeted`, `existing_work_ids`, `status` (`to_read`, `read`, `partial`, `not_reached`, `merged`), `notes` (`added_during_reading` for targets found while reading).

`attributes.csv`: one row per English row of `works.csv`, keyed by `work_id`.

| Field | Values |
|---|---|
| `frame_id` | The frame target the row answers; blank if found outside the frame |
| `country_pub` | England, Scotland, Ireland, US, Canada (place of the imprint read) |
| `author_origin` | The author's country, where known |
| `fourth_identity` | `H6`, `C`, `both`, `none`, `other`; blank if not read (protocol rule 2) |
| `fifth_identity` | `C`, `D`, `D+F`, `F`, `none`, `other`; blank if not read |
| `edward_status` | `absent`, `named_unnumbered`, `inside_last`, `ninth_with_tunis`, `ninth_alone`, `other_number`, `last_unnumbered`; blank if not read (protocol rule 3) |
| `ninth_referent` | `tunis`, `tunis+edward`, `edward`, `other` (say what in `notes`), blank |
| `gibbon_cited` | `none`, `footnote`, `bibliography`, `named_in_text`, `quoted`, `preface`, combinations joined by `;`, `unchecked` (protocol rule 5) |
| `gibbon_edition` | The edition cited, or `unspecified` |
| `gibbon_numbers` | Computed: `all`, `some` or `none` of the row's C, D, L1, L2 slots agree with Gibbon's (C 4, D 5, L1 6, L2 7); blank if the row has none of them |
| `sources_named` | Modern authorities named, `;`-separated (protocol rule 6) |
| `numbers_follow` | `moreri`, `michaud_mills`, `gibbon`, `german`, `french_school`, `modern`, `own`, `unclear`, then `;documented` or `;inferred` |
| `checked_on`, `notes` | Date; "derived from slots; not re-read in D2" marks the 44 derived legacy rows |

Derived tables, written by `scripts/d2_analyses.py` (do not edit): `fourth_by_decade.csv`, `fourth_pivot.csv` (decade by genre, with the H6 share of decided rows), `fourth_series.csv` (edition by edition for the main series), `gibbon_table.csv`, `edward_timeline.csv`, `edward_firsts.csv`, `conversation_edges.csv` (`numbers_vs_cited`: `agrees`, `partly agrees`, `disagrees`, `no shared slot`), `national.csv`.

Hand-built records: `census_archiveorg_titles.csv` (archive.org items titled crusade(s)/crusaders, 1800–1945, merged by work: `first_year`, `last_year`, `copies`, `author`, `title`, `identifier`, `kind`, `status`, `work_id`) and `ninth_crusade_hits_by_work.csv` (every "ninth crusade" item to 1945 grouped by work: `referent` = `L2+E`, `L2`, `L1`, `E`, `B`, `G10` (Gregory X's projected crusade), `post-1272`, `other`, `list`, `metaphor`, `modern`, `mixed`, `unclear`; `basis` = `context` (read around the phrase) or `classifier`).

`country`: `CA` (Canada) added 28 November 2026 beside `GB`, `US`, `IE` and the others.

## reasons/reasons.csv: kind

`statement_of_custom`, `correction`, `exclusion`, `inclusion_note`, `disclaimer`, `convenience`, `continuity`, `rejection`, `silent_inclusion`, `silent_exclusion`, `alternative_reckoning` (a work names another count beside its own: Chepmell 1857, Adams 1883), `attribution` (names the source of a count: Bouchitté 1836), `explanation` (explains why a count runs as it does: Barker 1911, Procter).

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
