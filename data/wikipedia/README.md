# Wikipedia numbering data

Sub-project data, version 0.3. Yearly samples retrieved 8 November 2026 from the MediaWiki API of the English, German, French, Italian, Spanish, Dutch, Greek, Arabic, Persian and Hebrew Wikipedias. Second pass 9 November 2026: pageviews (Wikimedia REST API), Wikidata, the German National Library (lobid.org GND), and titles and navboxes in Turkish, Russian, Portuguese, Swedish, Polish, Czech, Hungarian, Danish and Norwegian. Rebuild the derived tables with:

```
python3 scripts/build_wikipedia.py
python3 scripts/build_wikipedia_chart.py
```

Wikipedia text quoted in these files is licensed CC BY-SA; quotations are kept to short key phrases. Every row carries a revision ID, and `https://<lang>.wikipedia.org/w/index.php?oldid=<id>` opens the revision.

## Pages covered

| Language | Main article | Navigation box | Other |
|---|---|---|---|
| en | Crusades (titled "Crusade" until 2006) | Template:Campaignbox Crusades (2004–) | List of Crusades (2020–) |
| de | Kreuzzug | Vorlage:Navigationsleiste Kreuzzüge (2005–) | |
| fr | Croisade | Modèle:Palette Croisades (2013–) | Modèle:Croisades (2007–), coded as `navbox_2` |
| it | Crociata | Template:Campagnabox Crociate (2008–) | |
| es | Cruzadas | Plantilla:Campaña Cruzadas (2009–) | |
| nl | Kruistocht | Sjabloon:Navigatie kruistochten (2011–) | |
| el | Σταυροφορίες | Πρότυπο:Σταυροφορίες (2005–) | |
| ar | حملات صليبية | قالب:حملات صليبية (2004–) | |
| fa | جنگ‌های صلیبی | الگو:جنگ‌های صلیبی (2016–) | |
| he | מסעי הצלב | תבנית:מסעי הצלב (2009–) | |

Article codes follow `expeditions.csv` (E1 E2 E3 H6 C CH D F B L1 L2 E). Five codes are proposed additions for Wikipedia coverage: `PEO` People's Crusade, `C1101` Crusade of 1101, `ALX` Alexandria 1365, `NIC` Nicopolis 1396, `VAR` Varna 1443–44. Combined counts use the codebook's plus sign (`D+F`).

## Files

### yearly_counts.csv

One row per page per sample: the revision in force at 00:00 UTC on 1 July of each year from 2001 to 2026, plus a check on 8 November 2026. Years before a page existed are omitted (461 rows).

| Field | Meaning |
|---|---|
| `language`, `page`, `page_title` | Edition, page kind (`main_article`, `navbox`, `navbox_2`, `list_article`), current title |
| `sample_date` | 1 July of the year, or 2026-11-08 |
| `revision_id`, `revision_date`, `bytes` | The revision in force at the sample date |
| `highest_ordinal` | Highest crusade ordinal the page uses anywhere (title, label or running text). German rows give 7 for the German count |
| `count_family` | `nine`, `eight`, `german_seven`, `german_seven_bracketed` (German count with the modern count in brackets), or `partial` (no complete sequence on the page) |
| `stated_count` | Any explicit count the text states in that year (see count_statements.csv); empty if none |
| `numbering_shorthand` | The page's numbering in project notation (`C 4, D 5, ...`). Bracketed ordinals are the alternative count the page gives |
| `ninth_is` | Expedition holding the Ninth, if any |
| `unnumbered_linked` | Crusade articles the page links without a number |
| `barons_named` | 1 if the page names the 1239–41 crusade (by title, leader or "crusade" within 40 characters of "1239") |
| `linked_codes_raw`, `ordinals_in_text_raw` | Automatic output: each linked crusade article with the ordinal its link carries; every ordinal found in the text |
| `coding_source` | `links`, `links+text` (ordinals in text filled from the standard sequence) or `hand` |
| `verification` | `auto` or `hand` |
| `notes`, `url` | Notes on hand-coded rows; link to the revision |

### article_creation.csv

One row per article or template (182 rows): first revision, whether it began as a redirect or as junk, the first real article revision, the title at creation, and notes on moves. `first_article_utc` is the date to use for "when did this language get an article".

### title_moves.csv

Page moves that change a title (42 rows), with `kind`: `rename_numbering` (the move adds or removes a number), `rename_other`, `capitalization`, `numeral_form` (Greek Δ' to Δ΄). Vandal moves and history-maintenance moves are left out.

### ordinal_titles_2026.csv

What each ordinal title ("Fifth Crusade", "Fünfter Kreuzzug", "Δέκατη Σταυροφορία") is in each language on 8 November 2026: article, redirect (with target), short page or missing, with the expedition and first-revision date.

### key_edits.csv

Forty-three dated edits that changed a count, a title or Barons' Crusade coverage, with revision links where the edit is a content change. Transitions found by binary search were checked against the parent revision.

### count_statements.csv

Explicit statements of how many crusades there were ("gives us nine", "insgesamt sieben", "On compte habituellement neuf"), with the sample range in which each appears, a short key phrase and a gloss.

### alternative_number_statements.csv

Hand-curated from the yearly leads of the Fifth to Ninth articles: where an edition admits another number for the same expedition ("sometimes counted as the Seventh", "Nach anderer Rechnung"). One row per statement and sample range, with the first revision carrying it, the alternative in project codes, a key phrase and a gloss.

### pageviews_annual.csv, pageviews_annual_old_titles.csv, pageviews_by_language.csv

Human pageviews (agent=user, all access) per article and calendar year, July 2015 to October 2026. `months` counts the months with data; 2015 is July–December and 2026 January–October. Views of a title before a rename sit in `_old_titles` (French, Spanish, Greek); minor renames elsewhere are not merged. `pageviews_by_language.csv` totals 2016–25 per edition and gives 2025 views for the main article, the First to Ninth, the Barons' Crusade and Edward's crusade.

### wikidata_series.csv

The crusade items on Wikidata: QID, English label, the series ordinal on "part of" (P361, qualifier P1545), and "follows"/"followed by" (P155/P156) in project codes.

### gnd_headings.csv

German National Library subject headings for the numbered expeditions: preferred heading (dated) and the variant forms that carry numbers. Library of Congress headings are missing: id.loc.gov blocks automated access.

### ordinal_titles_new_languages.csv, navbox_new_languages.csv

For tr, ru, pt, sv, pl, cs, hu, da, no: every ordinal title from First to Tenth with its status in October 2026 (article, redirect, missing), redirect target, English equivalent and first revision; and the crusade navbox sampled yearly, as a list of linked project codes with ordinals.

### raw/

`snapshots_auto.csv` and `creation_auto.csv` (first seven languages) and the `_ar_fa_he` files (second pull) are the unedited outputs of the API; the build script reads them and applies the hand-coding.
