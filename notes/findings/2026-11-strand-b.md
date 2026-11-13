# Strand B: French schoolbooks and programmes, 1816–42

Task 2 of NEXT_STEPS_2026-11-13. Agent run, 13 November 2026. Status: for review; nothing here is merged. Data: `entries.csv` (5 rows), `frame.csv` (31 works), `not_reached.csv` (17), `search_log.csv` (65 searches), `read_list.md`.

## Result

This run did not move the bracket. No French schoolbook, programme or chronological table of 1816–42 was read with the modern slots four to six, and none was read that joins Koch's slots to a numbered eighth at Tunis. The frame has 31 works. Seven are coded at any level (23 percent): two in this session, five from task 1 or earlier passes, all of those at snippet, contents or translation level. Twenty-four are not reached. That is far short of the brief's 25 to 40, and the reason is access, not scarcity: Gallica refused every call, Google Books text, search and PDF are robots-blocked, MDZ and archive.org text links need fetch approval unless a search returns them directly, and general web search does not index 1816–42 book text. The signature-string controls returned modern web pages only.

What the run did establish:

1. **The Michaud scheme held in the youth abridgment.** The Michaud–Poujoulat *Histoire des croisades abrégée à l'usage de la jeunesse* (Mame printing of 1886, table read) has "Quatrième croisade" for the German expedition, "Cinquième croisade" for 1202–05, one sixth running from Andrew II through Frederick II to Thibaut, Louis IX seventh and eighth. The 1838 abridgment was never re-slotted, so the Catholic youth market that used it kept Henry VI fourth for decades. Michaud's own 4th edition (1826–27) carries the same scheme in its volume titles ("le récit de la 4e croisade, de la conquête de Constantinople par les Francs, et de la 6e croisade"), from catalog transcription only.
2. **Paris scholarship called 1202–04 "the fourth crusade" by 1840–41, outside the school market.** Buchon's *Recherches et matériaux ... à la suite de la quatrième croisade* (Desrez, 1841 by an OCR-garbled title page) puts the label in its title, and his *Chroniques étrangères* (c. 1840–41) uses "cette quatrième croisade." Neither says anything about slots five to eight. This is the German fourth in French learned usage, independent of Koch in wording.
3. **Heeren's prize essay in French (Villers, 1808) numbers nothing past the first** in its narrative survey. It cannot be Koch's or Schöll's source for the slots.

## Source, copy or independent

Only four French works with modern slots four to six are on record, and none is new:

- **Koch–Schöll, *Tableau*, 1823** (task 1, English translation): the earliest witness and the candidate source. Whether the slots are Koch's (1771/1807) or Schöll's (1814/1823) is undecided; every pre-1823 French text was out of reach again.
- **Schöll, *Cours*, 1830**: a copy, by the same reviser, with the same slots four to seven. Inferred; wording not compared.
- **Bouillet, 1842**: independent in wording (his text is Courtin's, abridged; Strand A). The slots could be Koch–Schöll's seven plus Tunis, but no shared wording or cited authority links them. Cannot decide.
- **Le Bas, 1842**: independent in wording (a chronological table, Didot). Le Bas was a Germanist (`recalled`), which makes a German or Koch–Schöll route plausible but not shown. His own *Annales historiques* (1840–43) is the obvious place to look and was not reached. Cannot decide.

## Does the Koch-import hypothesis hold?

It survives, unconfirmed. Before 1842 the only French texts with the modern fourth to sixth are by Koch and Schöll; the schoolbooks read (Lefranc 1834, Lévi Alvarès 1835, the Michaud abridgments of 1838 and 1839) follow other schemes. Buchon's usage shows the German fourth had entered Paris scholarship by 1840–41 without the rest. The step that makes the eight, adding Tunis as a numbered eighth to Koch's "seventh and last," is still unwitnessed before Bouillet and Le Bas. A French re-slotting inside the school market is not excluded either, because the books that would test it (Lefranc 1838/1841, Des Michels, Valentin 1841, the 1840 baccalauréat list) were not read.

## Claim template (protocol section 4)

"The modern eight is attested complete by Bouillet's *Dictionnaire universel* and Le Bas's *France: dictionnaire encyclopédique*, t. 6 (Paris, 1842). In a census of 31 French works of 1800–1842 in the forcing genres, 7 have been coded and none has it. The nearest predecessors are Koch–Schöll, *Tableau des révolutions de l'Europe* (1823, read in translation) and Schöll, *Cours* (1830), which differ in the eighth (no Tunis), and Lefranc, *Histoire du moyen âge* (1834), which differs in the fourth and fifth. The change falls between 1834 (school market) or 1830 (Schöll) and 1842." With 24 of 31 frame works unread, this is a bracket on paper, not a census result.

## Not reached (see not_reached.csv)

Koch 1771, 1807 and 1814 (decisive for Koch versus Schöll); Lefranc 1838 and 1841; Valentin 1841; Des Michels's *Précis*; Le Bas's *Annales historiques*; the Université programmes and the 1840 baccalauréat question list; Gaultier rev. 1836; Michelet's *Précis* 1833. The frame itself was built from catalog records the searches turned up (BnF, Défense, Europeana, cageweb, Google Books about pages, AbeBooks) plus `recalled` titles. No textbook catalog (Emmanuelle, BnF subject search) could be queried, so the frame is incomplete as well as unread.

## Proposed protocol amendments

1. **Access rule for Strand B.** Strand B cannot be run through web search and fetch alone. It needs Gallica full text (the 1814 and 1807 Koch volumes and Gaultier are all there) and Google Books text mode, or the author working in BnF or ÖNB. Record it as a precondition, not a search step.
2. **Frame provenance.** Add a `source_of_listing` value `recalled` to the frame file, and do not count recalled titles in the frame size used in the claim template until a catalog record confirms them.
3. **Partial C 4 witnesses.** Add a code for works that name only the fourth (Buchon 1840–41, Riant later): `partial_C4`. They date the spread of the German fourth separately from the eight.
4. **Later printings.** A later printing of a frame work (Michaud–Poujoulat 1886) may stand as `full_text` for the scheme of the abridgment, with `census_frame` left blank and the first edition flagged unread.
