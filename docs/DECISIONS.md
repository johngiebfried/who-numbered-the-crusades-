# Decisions log

Newest first. Each entry: date, decision, reason.

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
