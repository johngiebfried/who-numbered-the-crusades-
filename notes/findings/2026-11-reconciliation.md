# Reconciliation: one master table

28 November 2026. The print data now live in one table, `data/works.csv`. It replaces the legacy `works.csv` and six entry tables built strand by strand since 10 November. Script: `scripts/reconcile_works.py`; numberings re-derived by `scripts/derive_numberings.py`. The conclusions audit asked for this twice (14 and 23 November).

## What was merged

| Input | Rows |
|---|---|
| legacy `works.csv` | 85 |
| `strand_a/entries.csv` | 40 |
| `strand_a/entries_de.csv` | 2 |
| `strand_b/entries.csv` | 33 |
| `strand_b/entries_de.csv` | 22 |
| `strand_d/entries_en.csv` | 34 |
| `panel/entries_fr.csv` | 16 |
| **Total in** | **232** |
| **`works.csv` out** | **220** |

Twelve input rows recorded editions already in another table and were merged into eleven rows: Bouillet 1842 (three records), Dezobry 1863, Larousse 1869, Gibbon 1788, EB9 1877, Bréhier 1908, Barker 1911, D. S. Schaff 1907, Duruy 1861 and its 1891 translation, and Saint-Allais 1816. Each merged row keeps the legacy `work_id` (or the first strand id) and lists the others in `alt_ids`. Every old id resolves through `data/reconciliation/id_map.csv`, so the strand ids cited in the findings notes, `reasons.csv` and the stemma links still work. The old tables are frozen in `data/archive/2026-11-28-pre-reconciliation/`.

The slot columns (`H6` to `E`) are now the record; `numberings.csv` (672 rows) is derived from them. Every ordinal in the old tables survives, with one deliberate exception listed below. A slot cell may now hold two ordinals (`5;6`), so Cantù 1842's split of the Damietta crusade, which the old derive script stored as two rows for D, is kept.

## Decisions made in the merge

1. **Best-verified source wins the slot vector.** On a tie the strand row wins, but a value the other row had is kept where the strand row is blank.
2. **Five legacy rows got slots from their own shorthand.** Their free text had never been parsed, but the ledger had parsed it: Fuller 1639 (L1 12, L2 13), Mills 1820 (B 7, L1 8), the Greek syllabus 1893 (C 4), Stevenson 1907 (C 4) and Setton 1962 (C 4, D 5). Each value was checked against the shorthand and noted in the row.
3. **Tradition and genre are filled only where the frame settles them.** Dictionaries and the reference panel are Reference, the school series School, French and German texts France and Germany. The rest is left blank: 66 rows, mostly strand B and the roots frame, listed in `data/reconciliation/hand_coding.csv`. I did not guess.

## Conflicts (data/reconciliation/conflicts.csv)

Eleven slot disagreements, in three rows. Two need a reading:

- **EB9 (1877), Edward.** The legacy row (from the 2022 paper's table) has Tunis and Edward together as the ninth. The strand D full-text read records "the ninth and last crusade" for Tunis and leaves Edward blank. The full text wins, so E is now blank. This is the one old ordinal that did not carry over. **Check whether Edward sits inside EB9's ninth.**
- **Barker, EB11 (1911), Edward.** Both reads are full text. The legacy row has Edward inside the eighth; the strand row does not record him. The value is kept, flagged. I tried to check it and could not: Wikisource needed an approval nobody was there to give, and the archive.org OCR of EB11 vol. 7 lacks the article.

The other nine are fills: EB9's middle slots from the full-text read replace the paper table's "H6 4 through L2+E 9", and D. S. Schaff's full CCEL read (C 4, D+F 5, L1 6, L2 7) wins over the strand D snippet (F 5).

## The ledger

`data/ledger/ledger_print.csv` (78 rows) is still hand-coded in `scripts/ledger_code_corpus.py`. All 78 rows now map to a `work_id` (`data/reconciliation/ledger_map.csv`). After the five shorthand fills, the ledger and `works.csv` disagree in one cell: EB9's Edward, above. Generating the ledger from `works.csv` would lose the ledger's `n` (named) and `x` (excluded) cells, which `works.csv` cannot yet express. That waits on the planned `status` values in the codebook.

## Still open

- `numberings_unparsed.csv`: 18 rows say they enumerate but have no slots, for example Pasquier's "Six", Kugler's "scheme of his own", Avendaño, and English Wikipedia's "one to eight". Several are totals only and need no slots.
- `hand_coding.csv`: genre for 66 rows, tradition for one.
- Bouillet 1847 and 1851 carry `modern_eight` without slots (snippets of the "On compte généralement huit croisades" sentence). The family code should be checked against a full read or cleared.

## How to work from now on

Edit `data/works.csv`, run `scripts/derive_numberings.py`, and keep logging searches in `data/search_log.csv`. Do not rerun `reconcile_works.py` once `works.csv` has been edited; it would overwrite the edits. The one-off session scripts that wrote to the old tables now fail if run, on purpose (`scripts/README.md`).
