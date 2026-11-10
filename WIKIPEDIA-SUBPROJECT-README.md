# Wikipedia sub-project, first and second passes (8–9 November 2026)

Files in this archive use the repository's paths; copy them into the working clone.

- data/wikipedia/            fourteen tables, raw API pulls, README (data dictionary)
                             new on 9 Nov: pageviews (3 files), alternative_number_statements,
                             wikidata_series, gnd_headings, *_new_languages (2 files)
- scripts/build_wikipedia.py         rebuilds the tables from data/wikipedia/raw/
- scripts/build_wikipedia_chart.py   writes site/wikipedia-timeline.html
- site/wikipedia-timeline.html       the timeline chart (self-contained)
- site/data/wikipedia_timeline.json  chart data
- notes/findings/2026-11-wikipedia-numbering.md
- docs/subprojects/wikipedia-numbering.md   (replaces the brief)

Also updated, in the Claude project only (copy into docs/ when committing):
RESEARCH_LOG.md (entries for 8 and 9 November), DECISIONS.md (provisional
Wikipedia method), CODEBOOK.md (proposed codes, Wikipedia tables, `aside` status).

Added 9 November (visualizations):
- data/ledger/                ledger.csv (print corpus + Wikipedia runs), ninth_views.csv, README
- scripts/ledger_code_corpus.py, scripts/build_ledger.py
- site/ledger.html, site/story.html, site/dash-shim.js   standalone copies of the two Claude dashboards
