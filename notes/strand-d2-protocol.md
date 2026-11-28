# Strand D2 protocol: English-language print, 1800–1945

Frozen 28 November 2026, before reading. Changes go in the amendments list at the end, dated. The general rules of `docs/SEARCH_PROTOCOL.md` (signature, evidence rules) apply unchanged.

## 1. Questions

1. **Lines of conversation.** Which outside tradition does each English-language work's numbering follow, and what documents the link?
2. **The Fourth.** When, where and through which channels did English print move from Henry VI's expedition (1195–97) to the 1202–04 expedition as "the Fourth Crusade"?
3. **Gibbon and Edward.** How did these works use Gibbon, and did citing him go with his numbers? How did Edward's crusade (1271–72) rise and fall as "the Ninth"?

## 2. Frames

Listed in `data/strand_d2/frame.csv`, one row per work (series as one row, editions listed). Every listed work ends either read (a row in `data/works.csv` and in `data/strand_d2/attributes.csv`) or logged `not_reached` with the reason.

| Frame | `census_frame` value | Contents |
|---|---|---|
| Reference | `d2_reference_en` | General encyclopedias, dictionaries of dates, chronologies, religious encyclopedias, every edition reachable, 1800–1945 |
| School | `d2_school_en` | School and college texts of general, medieval, church and English history; long series by edition |
| Popular | `d2_popular_en` | Narrative histories of the crusades for general readers, juvenile and Sunday-school histories, anthologies, English translations of Michaud |
| Scholarly | `d2_scholarly_en` | Monographs, source collections, guides, the *Cambridge Medieval History*, Gibbon's annotated editions |
| Church and national | `d2_church_en` | Church histories (original and translated) and histories of England on Richard I and Edward I |

Countries: England (and Wales), Scotland, Ireland, US, Canada, coded from the imprint (`country_pub`). The author's origin is recorded when known and different (`author_origin`).

Edition policy: date the edition read. A reprint gets its own row when its text differs, or when it is the edition read for a country (a Dublin, Edinburgh, New York or Toronto printing). For long series, read the first edition reachable and the editions where the text changed; record which editions were read in `notes`.

## 3. Coding

Existing fields as in `docs/CODEBOOK.md` (slots, `stated_count`, `scheme_family`, `signature_match`, `stemma_parent`, `parent_evidence`, `verification_level`, `title_page_checked`). Strand fields in `data/strand_d2/attributes.csv`, one row per `work_id`:

- `country_pub`, `author_origin`: England, Scotland, Ireland, Wales, US, Canada.
- `fourth_identity`: `H6` (1195–97, Henry VI or Celestine III), `C` (1202–04), `both`, `none`, `other`.
- `fifth_identity`: `C`, `D` (Andrew and/or Damietta), `F`, `D+F`, `none`, `other`.
- `edward_status`: `absent`, `named_unnumbered`, `inside_last`, `ninth_with_tunis`, `ninth_alone`, `other_number`, `last_unnumbered`.
- `ninth_referent`: `tunis`, `tunis+edward`, `edward`, `other`, blank.
- `gibbon_cited`: `none`, `named_in_text`, `quoted`, `footnote`, `bibliography`, `preface`, `;`-separated; or `unchecked` when the crusade chapter was not read in full.
- `gibbon_edition`: Milman, Smith, Bury, Student's Gibbon, unspecified, blank.
- `gibbon_numbers`: `all`, `some`, `none` on C, D, L1, L2 against Gibbon (C 4, D 5, L1 6, L2 7), computed from the slots; blank if none of the four is numbered.
- `sources_named`: authorities named in the crusade chapter, preface or bibliography, `;`-separated.
- `numbers_follow`: `moreri`, `michaud_mills`, `gibbon`, `german`, `french_school`, `modern`, `own`, `unclear`, plus `documented` or `inferred`.

## 4. Classification rules

1. **Headings and lists outrank asides.** A work's slots come from its chapter headings, lists, tables or the sentence that enumerates. A passing ordinal that contradicts them ("what is sometimes called the fourth") is recorded in `notes` and does not fill a slot.
2. **Fourth.** `fourth_identity` = `H6` if the work calls the 1195–97 expedition (Celestine III, Henry VI, the "German crusade" of 1197) the fourth; `C` if it calls 1202–04 the fourth; `both` if it does each in different places, or puts both under one fourth; `none` if no fourth is numbered. A work that calls 1202–04 "the fifth" has `fourth_identity` = `H6` only if the fourth is identified as Henry VI's; otherwise `other`.
3. **Edward.** `inside_last`: Edward's expedition is told as part of the expedition that bears the last number, with no number of its own. `ninth_with_tunis`: a ninth covers Tunis and Edward together (or Tunis, with Edward told inside it). `ninth_alone`: Edward alone is called the ninth. `other_number`: Edward alone carries another number (Penny Cyclopaedia's "seventh and last"). `last_unnumbered`: "the last crusade" without a number. `named_unnumbered`: Edward's expedition is mentioned, no number attaches to it or to an expedition containing it. `ninth_referent` records what "ninth crusade" means wherever the phrase occurs.
4. **Copying.** Shared wording counts as copying when eight or more consecutive words match, or when an error is shared (a wrong date, a misattributed leader, the same misprint). Anything less is a scheme match and is coded `inferred`.
5. **Gibbon.** A citation counts only in the crusade chapter(s), the preface or the bibliography. The kind is coded from the context: a page or chapter reference is `footnote`; a list of authorities is `bibliography`; a sentence naming him is `named_in_text`; words in quotation marks attributed to him are `quoted`.
6. **Sources named.** Names of modern authorities only (Gibbon, Michaud, Mills, Wilken, Hallam, Robertson, Mosheim, Heeren, Sismondi, Voltaire, Hume, Fuller, Maimbourg, Milman, Guizot, Keightley, Stebbing, James, Mackay, Röhricht, Kugler, Sybel, Riant, Prutz, Pears, Stubbs, Lane-Poole, Archer, Cox, Munro, Barker, Bréhier, and so on). Medieval sources (William of Tyre, Joinville, Villehardouin) are recorded only in `notes`.
7. **Verification.** `full_text` only when the enumerating passage (or the crusade chapter) has been read in the text layer or on the page; `contents` when only the table of contents was read; `snippet` for search highlights. Title-page status is stated each time.
8. **Search procedure.** For each work: locate a full-text copy (archive.org, Google Books, Wikisource, Gutenberg, Canadiana, HathiTrust if reachable); extract every passage with an ordinal next to "crusade," every passage mentioning Henry VI or Celestine III with "crusade," every passage with Edward and Acre or Tunis, and every mention of Gibbon within 3,000 characters of "crusade"; read those passages; code. Searches are logged in `data/search_log.csv`.

## 5. Stopping rule

A frame is closed when every work in `frame.csv` is read or logged as `not_reached`. Works found during reading that belong to a frame are added to `frame.csv` with `added_during_reading` in `notes`.

## 6. Analyses (section 6 of the startup prompt)

The Fourth curve by decade, country and genre; the Gibbon table; the Edward and Ninth timeline; the conversation map from `data/citations.csv` and `numbers_follow`; national differences; a retest of the 2022 paper's English claims.

## Amendments
