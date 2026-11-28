# Scripts

## Current

| Script | Does |
|---|---|
| `reconcile_works.py` | Builds `data/works.csv` from the frozen inputs in `data/archive/2026-11-28-pre-reconciliation/`, with the crosswalk and reports in `data/reconciliation/`. Rerunnable, but rerunning it **overwrites every edit made to `works.csv` since 28 November 2026**. Do not rerun once `works.csv` has been edited by hand |
| `derive_numberings.py` | Writes `data/numberings.csv` and `data/numberings_unparsed.csv` from the slot columns of `works.csv`. Run after any edit to `works.csv` |
| `export_frame.py` | Prints a filtered view of `works.csv` (by census frame, source table or language) |
| `build_ledger.py`, `ledger_code_corpus.py` | Build the ledger visualization tables (`data/ledger/`). The ledger is still hand-coded in `ledger_code_corpus.py`; `data/reconciliation/ledger_map.csv` maps its rows to `work_id` |
| `build_wikipedia.py`, `build_wikipedia_chart.py` | Wikipedia sub-project |

## Historical (do not rerun)

These wrote to the per-strand tables that the reconciliation retired. The tables now live only in `data/archive/2026-11-28-pre-reconciliation/`, so the scripts fail if run. They are kept as the record of what each session changed.

- `build_strand_a.py` (10 Nov): rebuilt strand A and the search log from scratch
- `add_gaps_2026_11_23.py`, `add_window_2026_11_27.py`, `add_followup_2026_11_27.py`, `verify_german_snippets_2026_11_28.py`

From 28 November 2026 a session that adds or corrects rows edits `data/works.csv` directly (or with a dated script that edits `works.csv`), then runs `derive_numberings.py`, and still logs every search in `data/search_log.csv`.
