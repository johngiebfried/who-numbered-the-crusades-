# Schöll and Koch: the Franco-German hinge

Task 1 of NEXT_STEPS_2026-11-13. Agent run, 13 November 2026. Status: for review; nothing here is merged.

## Result

The swap predates Bouillet, and the case is stronger than it was, with one caveat that has to be cleared before print. Koch's *Tableau des révolutions de l'Europe*, in the Paris edition of 1823 that Schöll revised and continued, has 1202–04 fourth, Andrew of Hungary (1217) fifth, Frederick II sixth, and Louis IX's 1248 crusade "the seventh and last grand crusade." It has no number and no place for Henry VI, and it does not mention Tunis. The text adds that after Mansoura "there was no longer any talk about crusades to the East." The caveat: I read this in Crichton's English translation (London, 2nd ed., 1839), which says it was made "from the edition of 1823." I did not see the French.

So the modern slots four to seven are attested by Koch–Schöll 1823 (in translation), seven years before Schöll's *Cours* (1830) and nineteen before Bouillet and Le Bas (1842). Koch–Schöll is a seven, not an eight: Louis IX's first crusade is the last. That makes the working guess of the brief more exact. The modern eight looks like the Koch–Schöll seven with the French eighth at Tunis added on, not the French eight with a German fourth swapped in.

What I could not settle is whether Koch himself had this scheme (1771, 1807, 1813–14) or Schöll introduced it in 1823. Every pre-1823 Koch text was out of reach.

## Answers to the five questions

1. **Henry VI in Schöll.** Unanswered for the *Cours*: the opening of chapter VI in t. 3 was not reached. In Koch–Schöll 1823 (translation) Henry VI's expedition is absent from the crusade sequence; he appears only in the Sicilian succession.
2. **Stated total in Schöll.** Unanswered (t. 3 not reached). Koch–Schöll 1823 states no total in what survives the OCR. The word before "grand crusades succeeded to the first" is lost, so a numeral there cannot be excluded. "Seventh and last" closes the series.
3. **Tunis numbered in Schöll.** Not answerable from what was reached. The t. 4 contents list (Google about page) shows no "huitième"; the 10 November snippets give "Deuxième croisade de S. Louis" without a number. No index volume for t. 1–12 was found (t. 24 indexes t. 13–23 only). Koch–Schöll 1823 does not mention Tunis at all.
4. **Schöll's authorities.** Unanswered for the *Cours*. Koch–Schöll 1823 cites no authority in the crusade passage (no footnote; the translation names none of Heeren, Michaud, Wilken, Choiseul, Mailly, Maimbourg). Heeren was therefore not pursued.
5. **Koch's count by edition.** 1823 (Schöll's revision, in translation): seven, C 4, D 5, F 6, L1 7 ("last"). 1771, 1807 and 1813–14: not read. Whether the count changed between editions is open.

## Evidence

- Koch, *The Revolutions of Europe*, tr. [Andrew] Crichton, 2nd ed. (London: Whittaker, 1839), title page read as OCR text only. Translator's note: "In the edition of 1823, from which the present translation is made," the *Tableau* "has been continued by M. Schoell, down to the 20th November 1815." Narrative, Period IV, p. 43: "The fourth was undertaken (1202), at the pressing instigation of Innocent III … The fifth crusade (1217) was conducted by Andrew, King of [Hungary] … [Frede]ric II. undertook the sixth … The seventh and last grand crusade, was undertaken by Louis IX. King of France (1248)." OCR is badly garbled; the readings in square brackets are mine. Analytical table (refers to p. 43): 1198 fourth (Innocent III), 1217 fifth (Andrew), 1228 sixth (Frederick II), 1249 seventh (Louis IX, Damietta). <https://archive.org/stream/revolutionsofeur00kochuoft/revolutionsofeur00kochuoft_djvu.txt>
- That Schöll continued Koch, no longer only `recalled`: the title page of the American reprint of Crichton's translation (Middletown: Edwin Hunt, vol. 2, archive.org cihm_36724) reads "continued … by M. Schöll." The French 1823 title page was not seen.
- Catalog evidence only, not dated from title pages: Koch 1807 (3 vols) and 1813 (4 vols, "nouvelle éd. corrigée et augmentée") were published in Paris "chez F. Schoell"; 1814 by Gide fils; 1823 by Gide fils (Défense digital library records; a bookseller's listing for 1823). Schöll was Koch's publisher before he was his reviser.
- Schöll, *Cours*, t. 4 (Google id WLFupTgLH0MC, 1830 by metadata): contents list, "Croisade de Frédéric II 1228" p. 8, ch. VII "Influence des croisades" p. 33, and errata for t. III, p. 345. So chapter VI begins in t. 3 and ends in the first pages of t. 4.

## Not reached

Schöll t. 3 (no text-bearing scan found; Google page views are robots-blocked, Google Play failed, no Brussels reprint found); Schöll t. 6 at BSB/MDZ (needs fetch approval); Koch 1771 on archive.org and Koch–Schöll 1825 t. 3 (djvu text needs fetch approval); Koch 1807, 1813, 1814 and French 1823 (catalog records only); Crichton 1828 Edinburgh (needs fetch approval). See not_reached.csv.

## What this means for task 2

Search for the Koch–Schöll seven, not for a stray French re-slotting. The first job is a French Koch before 1823 (1771, 1807 or 1813), to tell Koch from Schöll. Then the question for French schoolbooks of 1823–42 becomes who added "huitième" at Tunis to Koch's "seventh and last." Lefranc (1834) does not follow Koch, so the Koch scheme had not swept the school market by then.

## Protocol amendments proposed

1. Add an `edition_language` note, or a `translation_of` column, so that a row read in translation (as here) is never coded as the original. A row coded through a translation should not stand as `full_text` evidence for the original edition until the original is seen.
2. In the codebook, record "near_modern" subtypes: `koch_seven` (C 4, D 5, F 6, L1 7 last, no Tunis) is a distinct scheme from `german_seven` (C 4, F 5, L1 6, L2 7) and should get its own family code.
