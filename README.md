# Who Numbered the Crusades?

A digital humanities project on how the crusades acquired their numbers. It began as an article on the origin of the familiar one-to-eight sequence and grew into a survey of crusade numbering across languages, genres and countries, centered on the nineteenth and early twentieth centuries.

The answer so far is not a person but a convention. The modern eight first appears in Marie-Nicolas Bouillet's *Dictionnaire universel d'histoire et de géographie* (Paris: Hachette, 1842). Cesare Cantù adopted it by 1851, Victor Duruy's schoolbook carried it in 1861, and American schoolbooks took it up from 1885. Other national traditions kept other counts: German schoolbooks a seven with Frederick II as the fifth, British popular histories Henry VI's crusade as the fourth into the 1870s.

## What is here

| Folder | Contents |
|---|---|
| `data/` | The dataset: expeditions, works, the number each work gives each expedition, evidence, citations |
| `docs/` | Project plan, codebook, decisions log, research log, sub-project briefs |
| `notes/` | Research notes: one file per work or question, plus dated findings |
| `paper/` | Drafts of the article for *Digital Medievalist* |
| `site/` | Interactive visualizations, published with GitHub Pages |
| `scripts/` | Code that builds derived data and figures |
| `sources/` | Bibliography exports |

Start with `docs/PLAN.md`, `docs/CODEBOOK.md` and `docs/SEARCH_PROTOCOL.md`. Findings so far are in `notes/findings/`, newest first in `docs/RESEARCH_LOG.md`.

**Status (November 2026).** Work in progress. Most print rows rest on Google Books snippets or contents pages and are leads, not verified readings; each row records its verification level. The search protocol sets the standard for claims of priority.

## Rebuilding derived data

```
python3 scripts/derive_numberings.py
```

## License

Data, notes and text: [CC BY 4.0](LICENSE-DATA-TEXT.md). Code: [MIT](LICENSE).

## Citation

See `CITATION.cff`. Author: John Giebfried, University of Vienna.
