# Decisions log

Newest first. Each entry: date, decision, reason.

## 2026-11-28 (evening) — Strand D2, English print 1800–1945 (provisional, for the author to confirm)

- **D2 fields stay out of `works.csv`.** `fourth_identity`, `fifth_identity`, `edward_status`, `ninth_referent`, `gibbon_cited`, `gibbon_edition`, `gibbon_numbers`, `sources_named`, `numbers_follow`, `country_pub` and `author_origin` live in `data/strand_d2/attributes.csv`, keyed by `work_id`, as the startup prompt asked. Whether they become columns is the author's call.
- **New family `nine_B7`** (C 4, D 5, F 6, B 7, L1 8, L2 9): the cheap-chronology nine (Universal Self-Instructor 1882, Gay's 1891). Reason: neither `nine_H6` nor `nine_F7` fits a nine without Henry VI whose seventh is the Barons' crusade.
- **New reason kind `explanation`** (Barker 1911 r29, Procter r31), and `alternative_reckoning` used for works that print another count beside their own (Chepmell r35, Adams r41).
- **Derived attributes for 44 legacy English rows**, flagged in `notes`, so the D2 tables cover every English row; they are not a re-reading.
- **Rows found through the ninth sweep are coded for the ninth only.** Their other attributes stay blank and count as `unknown` in the Fourth tables. A ninth naming Louis IX's first crusade or Gregory X's projected crusade is `ninth_referent` = `other`.
- **Corrections.** `1865-walter-c-perry` is George Gresley Perry's book (the 1840-dated copy merged into it); Stebbing 1830 corrected from vol. 2; Mackay's ten coded L1 9, L2+E 10; the 1923 Barker reprint's E cleared as in EB11; the EB9 and Barker conflicts in `reconciliation/conflicts.csv` resolved; Bloss's unsupported F cleared; Edinburgh imprints that name London first recoded to Scotland; Lingard's Dublin printing to Ireland.
- **Exclusions.** The DLI "New Columbia Encyclopedia" copies dated 1935 (the 1975 edition, from its CIP data) and a modern generated "Michaud abridged, 1839".
- **Reprints.** A reprint gets its own row only if its text differs or it is the copy read for a country (Toronto, Halifax, New York and Philadelphia printings have rows; plain reprints are listed in `notes`).

## 2026-11-28 — Answer books (provisional, for the author to confirm)

- **New reasons kind `attribution`.** A statement naming the source of a count or division ("Nous avons adopté la division des croisades indiquée dans le Précis ... de M. Desmichels", Bouchitté 1836, `r28`). It is not a reason for the count, but it is the strongest evidence of transmission, so it belongs in the same table.
- **Implied ordinals are not coded.** Delavigne states only "cinquième et sixième" and "les deux dernières"; his rows carry D 5 and F 6, with the implied C 4, L1 7, L2 8 described in `notes`. D 5 with F 6 is diagnostic, so the family code `modern_eight` is given (partial-row rule).

## 2026-11-28 — Reconciliation (provisional, for the author to confirm)

- **`works.csv` is the single source for print rows.** The legacy table and the six strand and panel entry tables are merged into it (220 rows from 232) and frozen in `data/archive/2026-11-28-pre-reconciliation/`. New rows go into `works.csv` directly. Reason: rows sat in seven tables with duplicates across frames, and the dataset could not be cited.
- **Ids are kept, never reissued.** Merged rows keep the legacy `work_id` (or the first strand id); the others go in `alt_ids`. `data/reconciliation/id_map.csv` resolves every old id.
- **The slot columns are the record; the shorthand is display.** `numberings.csv` is derived from the slots. A cell may hold two ordinals (`5;6`) when a source splits an expedition.
- **Merge rule.** The best-verified source wins the slot vector; on a tie the strand row wins, but the other row's values fill its blanks. Disagreements go to `data/reconciliation/conflicts.csv`. One old ordinal did not carry over (EB9, Edward in the ninth), pending a reading.
- **No guessed metadata.** Genre and tradition are filled only where the frame decides them; 66 rows wait in `data/reconciliation/hand_coding.csv`.
- **The ledger stays hand-coded for now**, mapped to `work_id` by `data/reconciliation/ledger_map.csv`, until `works.csv` can record "named" and "excluded".

## 2026-11-28 — German snippet rows (provisional, for the author to confirm)

- **One book, two counts: one row per table.** When tables in the same work number the crusades differently, each table gets its own row in the strand table, cross-referenced in `notes`. First case: Stein's *Neuer Atlas der ganzen Erde* (1842), split into `sb-de-1842-streit-atlas` (German table, F 5) and `sb-de-1842-stein-atlas-universal` (universal table, F 4, L1 5). Reason: a row records one scheme; averaging two would invent a third.
- **Partial-row rule applied.** The German-table row's family code is cleared because F 5 alone is shared by `frederick_fifth_seven`, `german_six` and `larousse_eight`.
- **The universal table coded `other`.** A five-count with Frederick II fourth and Louis IX fifth and last has no code; one witness does not justify a new family. `other` is still missing from the codebook (see the 27 November housekeeping note).

## 2026-11-27 — Author's decisions on the gaps-pass proposals; the 1820–23 window

- **Bouillet thesis line held (author).** The line "first attested in Bouillet (1842)" stays until the author has read Desmichels 1823, pp. 63–66, himself. It is then replaced by the Desmichels claim.
- **`german_seven` renamed `frederick_fifth_seven` (author).** The scheme is named for its defining slot, as `nine_F7` is. `merged_fifth_seven` was rejected because it misdescribes the 1820 witness, where Andrew is unnumbered and Frederick alone is fifth. The rename covers every print table (17 rows) and the codebook. The Wikipedia `count_family` labels are unchanged. Done by `scripts/add_window_2026_11_27.py`.
- **`gibbon_seven` added (author).** C 4, D 5, L1 6, L2 7, with F unnumbered.
- **Both protocol amendments adopted for all strands (author).** A statement of custom dates a count, not slots. A stable page link plus a viewed title page counts as the page image. The author saves PDFs of the bracket rows himself.
- **Family codes for partial rows (proposed, for the author to confirm).** A code is given only when the numbered slots are diagnostic. L1 6 alone is not diagnostic (see the codebook).
- **Reading of the 1820–23 window (provisional).** No Université text found prescribes the modern eight. The 1820 programme counts seven, and the 1821 baccalauréat question on the crusades numbers none (as printed in 1826). The eight first appears in Desmichels's *Tableau chronologique*, registered on 21 December 1822. The status is probable, pending BnF G-31078 (the 1822 question pamphlet). Details are in `notes/findings/2026-11-window-1820-23.md`.
- **G-31078 re-weighted (follow-up, same day).** The règlement of 13 March 1821 (R.L.R. t. 7) orders a question table but prints none, so the June 1822 Brunot-Labbe *Questions* is treated as probably the first printing of the official table, not one witness among several. The BnF order stays with the author: per-page PDF (€0.70 a page excl. VAT) or full PDF (€45), or reading at Tolbiac. Nothing was ordered and no terms were accepted.

## 2026-11-23 — Gaps pass (provisional, for the author to confirm)

- **Working thesis revised.** The modern eight is first attested complete in Desmichels, *Tableau chronologique de l'histoire du moyen âge* (1823), a textbook for the Paris collèges royaux, not in Bouillet (1842). The 2026-11-08 thesis line ("first attested in Bouillet") is superseded. Reason: full-text read of pp. 63–66 with the title page viewed; the 1820 official programme by the same author still counts seven.
- **Family name `german_seven` under review.** The scheme (C 4, F 5, L1 6, L2 7) is attested in Paris in 1820, earlier than any German witness found (1834). Options: (a) keep the name as a label of later prevalence; (b) rename to `merged_fifth_seven` and record the D-and-F merger variant as a subtype. Recommended: (b), after the German block is page-verified. No rename done.
- **New family code proposed: `gibbon_seven`** (C 4, D 5, L1 6, L2 7, F unnumbered), already used for Gibbon 1788 in Strand D; now also the German Gibbon (1791), Herder (1792), Collin (1818).
- **New tables.** `data/reasons/reasons.csv` holds explicit justifications, one row per statement, with `kind` (statement_of_custom, correction, exclusion, inclusion_note, disclaimer, convenience, continuity, rejection, silent_inclusion, silent_exclusion). `data/usage/` holds corpus counts; they are a proxy, not evidence of any single author's scheme.
- **Census frames added.** `roots_1675_1771` (pre-Koch histories, in `data/strand_b/entries.csv`) and `strand_b_de_1780_1860` (German schoolbooks, in `data/strand_b/entries_de.csv`).
- **Quotations from modern copyrighted works** in `reasons.csv` are kept to short phrases.

## 2026-11-10 — Search protocol frozen; Strand A coding (provisional, for the author to confirm)

- **Protocol.** Fable's search protocol is frozen as `docs/SEARCH_PROTOCOL.md`. Sections 2 (signature) and 6 (evidence rules) do not change for Q1; amendments are dated at the end of the file.
- **Proposed amendment, statements of custom.** A phrase such as "on compte généralement huit croisades" dates the custom of a count, not of a slot assignment. Reason: Bouillet's "généralement" descends from Courtin's "communément" (1824), which described the Moréri eight.
- **Proposed amendment, page images.** Until scans can be downloaded to the repository, a stable page link plus a viewed title page counts for Strand A rows. The author decides whether bracket rows need saved PDFs.
- **Separate table.** Strand A rows live in `data/strand_a/entries.csv`, one row per edition read, with slot columns per expedition code. They are not merged into `works.csv` until the reconciliation step.
- **Scheme names.** The old dictionary eight is called the `moreri_eight` after its earliest witness. Codes in `docs/CODEBOOK.md`.

## 2026-11-10 — Repository

- **Public from the start.** The author chose to push to a public repository rather than keep it private until release (this reverses the 2026-11-08 setup decision).
- **Name.** Created as `who-numbered-the-crusades-` (trailing hyphen); to be renamed `who-numbered-the-crusades`. GitHub redirects the old URL.
- **Not committed.** The 2022 manuscript (`Who Numbered the Crusades (Giebfried).docx`) stays in the Claude project only, since the repository is public.

## 2026-11-08 — Wikipedia sub-project method (provisional, for the author to confirm)

- **Editions.** English, German, French, Italian, Spanish, Dutch, Greek for the first pass, matching tiers 1–2 of the main survey.
- **Sampling.** Revision in force at 00:00 UTC on 1 July each year, 2001–2026, plus the day of retrieval. Key transitions pinned to the exact edit by binary search and checked against the parent revision.
- **Pages.** Main crusade article, the navigation box(es), and the English "List of Crusades". Each is a separate lane; templates and articles are not reconciled.
- **Two measures.** `highest_ordinal` (any ordinal the page uses, asides included) and `stated_count` (explicit statements) are kept side by side, since pages often contradict themselves.
- **Codes.** Wikipedia tables use the expedition codes plus proposed PEO, C1101, ALX, NIC, VAR (not yet added to `expeditions.csv`).
- **Open.** Which page is authoritative when they disagree, and how to code asides ("sometimes counted as the Ninth"). Options in `notes/findings/2026-11-wikipedia-numbering.md`.

## 2026-11-08 — Setup

- **Title.** *Who Numbered the Crusades?*, the original article title, for project, repository and article.
- **Venue.** *Digital Medievalist* from the start. The method and data are part of the argument.
- **Outputs.** Article, open dataset with DOI, interactive site on GitHub Pages.
- **Licenses.** CC BY 4.0 for data and text; MIT for code.
- **Repository.** New GitHub repository `who-numbered-the-crusades`, private until the first public release. (Superseded 2026-11-10: public.)
- **Workspace.** A dedicated Claude project, "Who Numbered the Crusades?", and the local folder `~/Documents/Who Numbered the Crusades?` as the working clone.
- **Scope.** Beginning of crusading through Gibbon as a single-narrative prehistory. Gibbon to 1945 as the core survey, with national chains after Gibbon. After 1945, notes only: modern scholarship, popular histories, catalogs, schools. As many languages as can be reached, down to Sweden and Portugal.
- **Sub-project.** Wikipedia numbering, 2001 to the present, as a flagged separate task.
- **Data model.** Works, expeditions, numberings, evidence, citations. Translations get their own rows. Every number carries a verification level.
- **Article thesis (working).** The modern eight is a nineteenth-century reference-book and schoolbook convention first attested in Bouillet (1842), not Mombert's invention.
