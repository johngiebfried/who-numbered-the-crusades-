# Data

Since 28 November 2026, `works.csv` is the single source for print works: one row per edition read, from every strand and frame. Everything else that carries numbers is derived from it or mapped to it.

| Path | What | Edited by hand? |
|---|---|---|
| `works.csv` | Master table, one row per edition, translation or catalog read. Field list in `docs/CODEBOOK.md` | **Yes**: the only place to add or correct a row |
| `numberings.csv` | One row per work and expedition, from the slot columns | No: `scripts/derive_numberings.py` |
| `numberings_unparsed.csv` | Rows that say they enumerate but have no slots filled | No (the queue for hand-coding) |
| `expeditions.csv` | Expedition codes | Yes |
| `citations.csv` | Who cites whom | Yes |
| `reasons/reasons.csv` | Explicit reasons for a count; `entry_id` resolves through `reconciliation/id_map.csv` | Yes |
| `search_log.csv` | Every search, negative ones included | Yes (append) |
| `strand_a/not_reached*.csv`, `strand_b/not_reached.csv`, `panel/not_reached_fr.csv` | Works in a frame not yet read | Yes |
| `strand_b/frame.csv` | The strand B census frame (works listed, not read) | Yes |
| `strand_d2/` | English print 1800–1945: `frame.csv` (census frame), `attributes.csv` (D2 fields per English row), the analysis tables written by `scripts/d2_analyses.py`, and two hand-built records (`census_archiveorg_titles.csv`, `ninth_crusade_hits_by_work.csv`). Fields in `docs/CODEBOOK.md` | `frame.csv`, `attributes.csv` and the two records yes (by dated script); the analysis tables no |
| `reconciliation/` | `id_map.csv` (every old id to its `work_id`), `conflicts.csv`, `ledger_map.csv`, `hand_coding.csv` | No: `scripts/reconcile_works.py` |
| `archive/2026-11-28-pre-reconciliation/` | The legacy `works.csv`, its numberings, and the six strand and panel entry tables as they stood before the merge | Never |
| `ledger/` | Visualization tables (print corpus plus Wikipedia runs) | Built by scripts; see `ledger/README.md` |
| `wikipedia/` | Wikipedia sub-project; revisions, not editions, so kept apart | Built by scripts |
| `usage/`, `ngrams/` | Corpus counts; `usage/archiveorg_d2_*.csv` are the D2 full-text counts (phrases, the Fourth's referent, the ninth's referents by decade) | Built by scripts or in the browser session that logged them |

Ids: a row keeps the id it had before the merge. Where two or three rows recorded the same edition, the legacy `work_id` (or the first strand id) is the row's `work_id`, and the others are listed in `alt_ids`. Findings notes written before 28 November cite strand ids and the old table paths; both resolve through `reconciliation/id_map.csv` and the archive.

To read one strand as it used to look: `python3 scripts/export_frame.py --source strand_b/entries_de`.
