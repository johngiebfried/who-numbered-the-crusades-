# Decision point after the five delegated tasks

13 November 2026. Combines the reports of tasks 1–5 in `docs/NEXT_STEPS_2026-11-13.md`. Task notes: `2026-11-schoell-koch.md`, `2026-11-strand-b.md`, `2026-11-strand-a-gaps.md`, `2026-11-brehier-wikipedia.md`, `2026-11-strand-a-german.md`, `2026-11-french-diffusion.md`. The pages the author should read himself are in `notes/read_lists/`.

## Access in this run

The agents were limited to URLs returned by their own searches. Constructed URLs (Google Books `&output=text`, archive.org `_djvu.txt`, Gallica `f` numbers, MDZ) needed approval, and nobody was present to give it. Gallica failed outright and zeno.org looped. Coverage is far below the earlier Strand A pass, and the many `not_reached` rows reflect access, not absence.

## Answers to the decision-point questions

**Origin: "re-slotted in France" or "imported by way of Koch and Schöll"?** The Koch–Schöll route is now the leading hypothesis, but it is not confirmed.

- Koch's *Tableau des révolutions de l'Europe*, in Schöll's revised Paris edition of 1823, numbers 1202–04 fourth, Andrew of Hungary fifth, Frederick II sixth, and Louis IX 1248 "seventh and last." It has no Henry VI and no Tunis. This was read only in Crichton's English translation (1839), which says it was made "from the edition of 1823."
- Schöll's *Cours* (1830) has the same slots four to seven.
- No French book before 1842 numbering Tunis eighth on top of these slots was found.
- Buchon (c. 1840–41) calls 1202–04 "la quatrième croisade."
- Michaud–Poujoulat and Lefranc 1834 keep Henry VI fourth.

The working formula is that the modern eight is the Koch–Schöll seven plus a numbered Tunis. Two checks are still open: whether Koch's 1771, 1807 and 1813–14 texts already have the slots, and where Tunis was first numbered.

**Does the dictionary bracket (1838–42) hold?** It holds on everything reached. Britannica's 4th to 7th editions (1810–42) have the Moréri eight. Two works could still move the bracket: *Encyclopédie des gens du monde* t. 7 (1836; BSB urn:nbn:de:bvb:12-bsb10401033-5) and d'Harmonville. The title pages of Courtin and Furne are still unchecked.

**German.** Hübner 1704 "Man zehlet acht Croisaden," ending with Louis IX in 1270, is confirmed only through Maier's footnote, and only the total and the endpoints are known. No German reference entry from 1709 to 1911 was read.

**Diffusion.** In the reference panel, five of six enumerating rows from 1842 to 1906 have the modern eight. The exception is Larousse 1869. Larousse changes scheme between 1869 and the *Petit Larousse* of 1906. Duruy's modern eight is attested only in the 1891 English translation of his 12th edition. The French text of 1861 has not been read, and nothing yet shows the eight entering schools through Duruy. No share can be stated, because the panel is not closed.

## Review flags (main session, before merge)

- `sb-1839-koch-schoell-crichton` is coded from a translation, and its `year_read` is the translation's year. Do not cite it as French evidence for 1823.
- `ss-fr-1891-duruy-moyen-age-en` is also a translation, coded `modern_eight`. It is not evidence for Duruy's French numbering.
- `pn-fr-1842-bouillet`, `pn-fr-1863-dezobry` and `pn-fr-1869-larousse-gdu` were carried over from Strand A without re-reading. They duplicate Strand A rows in a different frame.
- `sa-de-1704-huebner` has `signature_match` = `unknown`, which is not a codebook value. It is level `secondary`, and its quotation passed through a PDF summarizer: check it against Maier, p. 24, n. 39.
- The task 5 quotations passed through WebFetch's summarizer. The Petit Larousse "quote" is a paraphrase of noisy OCR. The *Grande encyclopédie* year (1892) is recalled.
- The task 2 frame is partly from the agent's recollection (`recalled`), because the BnF and Emmanuelle catalogs were not queryable.
- `sa-1808-rees`: task 3 found Part 19, 2 May 1808, "first part of CROISADE", from a secondary source (Wikipedia's parts table). The row was not changed.

## Proposed codebook and protocol amendments (author to decide)

- A new family code `koch_seven` (C 4, D 5, F 6, L1 7 and last), distinct from `german_seven` (C 4, F 5, L1 6, L2 7).
- A flag for rows coded from a translation.
- `signature_match` value `unknown`, for stated-only rows.
- Allow the agents to fetch exact URLs already recorded in the repository, or pre-approve archive.org, Google Books, Gallica, MDZ, DTA and zeno.org.

## Cheapest next reads for the author

1. Hübner 1704, cols. 321–323 (DTA): which eight it is.
2. *Gens du monde* t. 7 (MDZ): CROISADES.
3. The French text of Koch 1823 and Koch 1771/1807: whether the slots are Koch's.
4. Lefranc 1838 and 1841: slots four to six.
5. Duruy, *Histoire du moyen âge*, 1861: the French numbering.
