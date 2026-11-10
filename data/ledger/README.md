# Crusade numbering ledger

One table that puts the print corpus and Wikipedia side by side, built 9 November 2026 for the ledger page and the scroll story ("The Life of a Number").

```
python3 scripts/ledger_code_corpus.py   # writes ledger_print.csv from the hand-coding in the script
python3 scripts/build_ledger.py         # adds Wikipedia navigation-box runs, writes ledger.csv
```

## ledger.csv

One row per source. Print rows are the 78 works and catalogs of the numbering corpus (the Claude Doc "Numbering corpus" tab, rev 5), hand-coded; Orderic Vitalis and the two Wikipedia rows of that tab are left out (Wikipedia comes from `data/wikipedia/`). Wikipedia rows are the crusade navigation box in 15 languages, sampled 1 July each year (`yearly_counts.csv`, `navbox_new_languages.csv`) and collapsed into runs with unchanged numbering. Polish 2014 (only Alexandria linked) is skipped as anomalous.

| Field | Meaning |
|---|---|
| `id` | Slug of source and year label |
| `source`, `year_label`, `year_sort`, `year_end` | As displayed; `year_end` is the last sample of a Wikipedia run |
| `language`, `tradition`, `tradition_label` | Language of the text; tradition = where the count comes from (a translation of Ploetz is DE) |
| `kind` | `print`, `catalog`, `wikipedia` |
| `stated_count` | Total the source states, if any |
| `H6` … `E` | Number given to each expedition (codebook codes) |
| `note` | Short gloss |

Cell values: a number; two adjacent expeditions with the same number are counted as one; `n` discussed or linked without a number; `x` explicitly not counted; `5/6` both numbers given; `(7)` variant or aside only; `5 (6)` number with a bracketed alternative (German Wikipedia). Blank means the source as checked gives no number, not that it is silent. EB9 and Newman record only the ends of their nine.

## ninth_views.csv

Human pageviews per year, 2016–25, of English "Ninth Crusade" (article until 17 November 2019, then a redirect) and "Lord Edward's crusade". From `data/wikipedia/pageviews_annual.csv`.
