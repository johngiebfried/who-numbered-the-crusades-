# Who Numbered the Crusades? Interim conclusions

28 November 2026. Status report on the project as of commit `86789f8` (branch `window-1820-23`, PR #5). It draws on the 2022 manuscript, every findings note in `notes/findings/` and the Claude project, the research and decisions logs, the earlier conversations in the project, and the data in `data/`. It replaces no earlier note; it is the place to start. Updated the evening of 28 November with the English pass, Strand D2 (`notes/findings/2026-11-strand-d2-english.md`, branch `strand-d2-english`, PR #6): sections 1, 2.2, 3.4, 4.2, 4.4, 6.1 (one note), 7.9, 7.13, 8.5, 8.7, 9.3, 9.4 and Appendix A. The counts in section 6 are otherwise those of the morning.

**Evidence grades used throughout.** **Firm**: read at full text, wording quoted, edition identified, and where it matters more than one witness. **Probable**: the reading is sound but one link is inference or one document is unread. **Provisional**: read only in OCR search hits or snippets, or from one witness whose title page is unchecked. **Open**: not researched, or researched without result. Every claim of priority below means "attested in," never "invented by."

---

## Contents

1. Summary
2. The state of research before this project
3. The starting point: the 2022 paper
4. The problem: what any numbering has to decide
5. How the database was built
6. Size and scope of the database
7. Interim conclusions
8. Points of uncertainty
9. Future expansion
10. Appendix A: the key witnesses in date order
11. Appendix B: where everything lives

---

## 1. Summary

The modern one-to-eight sequence of crusades (1202–04 fourth, Damietta fifth, Frederick II sixth, Louis IX seventh and eighth, nothing for Henry VI, the Barons' Crusade or Edward) is first attested complete in C.-O. Desmichels, *Tableau chronologique de l'histoire du moyen âge* (Paris: Louis Colas), a textbook for the new Middle Ages course of the Paris collèges royaux. It was registered in the *Bibliographie de la France* on 21 December 1822 with a title page dated 1823. Three years earlier the same author's official course outline of 1820 counted seven, with Frederick II fifth. No Université text read so far prescribes the eight: the baccalauréat question on the crusades asks for a "précis historique des croisades" and numbers none. The eight reached students through Desmichels's own books and the exam-preparation manuals that answered that question, one of which (Bouchitté et al., Hachette, 1836) names him as its source. Paris reference works reported the result in 1842 as "l'usage le plus général."

The eight was not made from nothing. Its total, eight crusades with Tunis "huitième et dernière," is a dictionary convention reaching back to Moréri (by 1689) and Basnage's Furetière (1701). Its fourth to seventh slots are printed in Christoph Wilhelm Koch's *Tableau des révolutions de l'Europe* (1771), which counts "proprement sept." Desmichels's scheme is Koch's seven plus the dictionaries' numbered eighth.

Outside France the eight was imported, late and unevenly. English carried at least five imported counts side by side, and combined their slots into two nines of its own, until Bréhier's *Catholic Encyclopedia* article (1908) and Barker's Britannica article (1911) fixed the French eight in English reference books. In English the 1202–04 fourth was always the majority; the Henry VI fourth was a counter-current in a few long-lived series that died out, and Barker ended it in the Britannica after its decline. German schoolbooks kept a Frederick-fifth seven from 1834 to at least 1860, and German Wikipedia still does; that seven is itself attested first in Paris, in Desmichels's 1820 outline. Wikipedia's first English article (2001) carries Bréhier's dates.

The 2022 paper's answer (Mombert, 1894, perhaps a "simultaneous creation" of English popular historians) fails by seventy-two years and by a country. Its central moral survives in a sharper form: the numbers were made by people who wrote for students and general readers, not by crusade historians, who received the numbers and then spent a century disowning them.

What could still change this: one unread pamphlet at the BnF (G-31078, the 1822 printing of the official exam questions), the reason Desmichels changed his own count between 1820 and 1822, and the fact that much of the evidence outside France and outside the bracket years is still snippet-level, and none of it has had a second coder.

---

## 2. The state of research before this project

### 2.1 Dedicated treatments

There was no study of crusade numbering as such before this project, and a multilingual sweep on 13 November 2026 found none published 2016–2026 in thirteen languages (`findings-2026-11-prior-literature-check.md`). The literature that exists is short and in front matter or appendices:

- **Giles Constable**, "The Historiography of the Crusades," in Laiou and Mottahedeh (eds.), *The Crusades from the Perspective of Byzantium and the Muslim World* (2001), with a section recycled as Appendix B, "The Numbering of the Crusades," in *Crusaders and Crusading in the Twelfth Century* (2008), pp. 353–56. Constable lists a few wildly different counts (among them Carion and Bullinger's twelve) and concludes that the numbers later scholars gave the crusades "deserve to be studied." That sentence is the call the 2022 paper set out to answer.
- **Alan V. Murray**, "The Crusades: Names and Numbers," front matter to *The Crusades: An Encyclopedia* (ABC-CLIO, 2006). Murray says the numbers were first allocated in the eighteenth century and are inconsistent and misleading. The 2022 paper did not cite him.
- **Christopher Tyerman**, *The Debate on the Crusades* (2011), and his work on the word itself: "crusade" is rare in English before the eighteenth century and is settled only by Hume and Gibbon. That is the history of the word, not of the numbers, but it bounds when numbering in English could begin.

### 2.2 The complaint tradition

Scholars have complained about the numbers for as long as the modern eight has existed in English:

- **W. B. Stevenson**, *The Crusaders in the East* (Cambridge, 1907), p. 3: the crusades "have been numbered as if they were a series, well-defined and easily counted," eight bands chosen "on no clear principle." He then put the numbers he used, through the eighth, in quotation marks (Strand D2; the earlier reading that he stopped after the fifth was wrong).
- **Louis Bréhier**, "Crusades," *Catholic Encyclopedia*, vol. 4 (New York, 1908): "It has been customary to describe the Crusades as eight in number … This division is arbitrary."
- **Hans Eberhard Mayer**, *Geschichte der Kreuzzüge* (1965): the numbering "lacks all consistency" (as rendered in the English translation).
- Further disowning phrases collected in `data/reasons/reasons.csv` run from the *New International Encyclopaedia* (1902, "unanimous consent" only for the first four) to Laiou and Mottahedeh (2001, the numbering "differs widely").

The field's working convention since at least Runciman (vol. 3, 1954) is to number only the First to Fifth and to name the rest by leader, place or date. The paper describes that convention; the project has confirmed it as a specialists' habit and dated it in English to the 1890s (section 7.13).

### 2.3 Claims in circulation

Before this project the origin of the numbers was answered, when it was answered at all, by assertion:

- Janet L. Nelson, reviewing Tyerman in the *London Review of Books* 29/23 (2007): the French scholars were the ones "who numbered the crusades." Closer to right than anything else in print, but unsupported, and it points at scholars rather than schoolbooks.
- English Wikipedia's "Crusades" article said until 15 October 2019 that the nine-crusade count was a convention "used in 1820 by historian Charles Mills." The claim was deleted as possible original research during a Good Article review. Its sister article, "Historiography of the Crusades," still credits Mills with nine and Étienne Pasquier with the first numbering (six).
- A GEI teaching handout by Meyer-Hamme (2022) asserts that German historiography usually counts seven crusades and British only three.
- Popular items (a Medieval World blog post c. 2018; an r/AskHistorians thread of 2019) note the inconsistency and repeat Constable and Stevenson.

### 2.4 Adjacent work

- Reception studies of the crusades in nineteenth-century Britain: Elizabeth Siberry on Victorian readers and lending libraries; Mike Horswell, *The Rise and Fall of British Crusader Medievalism* (2018). Both explain why English popular histories multiplied, not where their numbers came from.
- Textbook and memory studies that record national counts without asking their origin: Hinz and Meyer-Hamme (eds.), *Controversial Histories: Current Views on the Crusades* (2020); Kurt and Turan, "The Crusades in history textbooks taught in England, France, Germany and Italy" (*Turkish History Education Journal*, 2026); earlier GEI dossiers.
- Lexicography of the word: B. Weber (ed.), *Crusade: The Uses of a Word* (Routledge, 2024, open access). Rosa Cetro's chapter on French dictionaries says nothing about counts and was dropped from the prior literature. Two other chapters supplied leads: Christoph T. Maier's footnote on Hübner's 1704 lexicon ("Man zehlet acht Croisaden"), and Caroline Salagnac's note that the current *Dictionnaire de l'Académie française* gives "La huitième et dernière croisade" as its example.

### 2.5 What nobody had done

Nobody had collected the counts themselves across genres and languages, dated them by edition, or followed them through the books that copy each other. Every earlier treatment looked at crusade histories, the one genre that turns out not to have made the numbers. Reference works, chronological tables, school courses, exam manuals and their translations, which did make them, had not been read for this question. Searches of the International Medieval Bibliography, RI-OPAC and JSTOR full text have still not been run (section 8.6).

---

## 3. The starting point: the 2022 paper

### 3.1 Origin and history

The question began in graduate school. The paper, "Who Numbered the Crusades?" (John Giebfried, University of Vienna), was drafted around 2018 (its Wikipedia citation is dated 28 January 2018), submitted to *Crusades*, and rejected in 2022. The manuscript stays in the Claude project and is not committed to the public repository.

### 3.2 Its method and corpus

The paper surveyed English-language histories of the crusades, found through a university library and then archive.org by searching for books with "Crusade" in the title. It set them beside the canonical continental historians (Maimbourg, Voltaire, Michaud, Michelet, Wilken, Sybel, Prutz, Kugler, Grousset) and summarized the English chain in a table of twenty-five works from Gibbon (1788) to the *Catholic Encyclopedia* (dated there 1917), coding each work's numbers for Henry VI's crusade through Edward's. It did not read reference works systematically, school courses, exam manuals, or anything outside English for the period after Michaud.

### 3.3 Its argument

1. Constable is the fullest treatment, and his call to study the numbers has not been taken up.
2. The modern numbering embodies the traditionalist definition of crusade (Jerusalem as goal) and survives into the pluralist era as a relic.
3. Early modern authors barely number: Fuller has thirteen unnumbered expeditions; Maimbourg numbers only Henry VI's crusade as the fourth; Voltaire, Hume and Robertson number only the first one or two.
4. Gibbon (1788) is the first extended numbering: 1202–04 fourth, Damietta fifth, Louis IX sixth and seventh.
5. Michaud numbers Henry VI fourth, and his school abridgment runs to eight with a composite sixth.
6. German academic historians (Wilken, Sybel, Prutz) do not number; Kugler has his own scheme.
7. Modern numbering arose in nineteenth-century England and America, in a flood of popular histories by clerics and "gentleman historians," triggered in part by the Crimean War.
8. Charles Mills (1820) made the template: a history told as a countdown of numbered crusades.
9. The Fourth was fixed as 1202–04 by the late nineteenth-century scholarly debate on 1204 (Riant, Klimke, Pears, Norden, Munro).
10. Nobody separates Edward's crusade as a Ninth before recent unfootnoted popular books; the origin of "Ninth Crusade" is unknown.
11. Jacob Isidor Mombert, *A Short History of the Crusades* (New York, 1894), is the earliest work with the modern one-to-eight sequence. Since none of his sources has it, and Ludlow (1896) and Barker (1911) do not cite him, the sequence was probably a "simultaneous creation."
12. A "golden age" of the eight ran from Mombert to Runciman; Barker's Britannica article (1911) did most to enshrine it.
13. Popular authors, not academics, shaped the numbering.
14. Stevenson (1907) was the first to use the now-standard academic practice of numbering only five; the five keep their numbers because they were collaborative ventures with no single leader to name them after.

### 3.4 What the review found

The fact-check of 8 November 2026 (`findings-2026-11-review.md`) and the conclusions audit of 14 November (`conclusions-audit-2026-11.md`, section 2) scored twenty-two of the paper's claims: **4 stand, 9 stand in part or with correction, 7 fail, 2 untested.** The failures are the paper's answer to its title (Mombert), its geography (England), its mechanism (popular histories), and its chronology (1894). Later sessions moved three verdicts further:

- **Claim 11 (Mombert first).** The complete scheme is attested seventy-two years earlier, in Paris (Desmichels, registered December 1822).
- **Claims 7 and 13 (English popular histories).** English made no count from scratch: it imported five and combined their slots into two nines; the modern eight entered English in 1851 as a translated French schoolbook. The "popular" moral survives only if "popular" means school and reference books, not narrative histories.
- **Claim 10 (Edward as Ninth).** Edward's crusade alone as "the ninth" is attested from Masonic lore (1857), English national histories (G. W. Cox 1887), the EETS *Godeffroy* (1893) and Parry (1920), then Scott-Giles (1979) and Toropov (2002); the commoner English ninth holds Tunis and Edward together (Russell 1831 to the county atlases of 1936). The modern split, Tunis eighth and Edward ninth, was not found before 1945 (Strand D2).

What stands from the paper: its table, where checked; Stevenson as the first complaint; the observation that popular narrative histories are the least standardized genre of all; Barker's article as the canonizing English text; the shape of the moral. The paper's observation that none of Mombert, Ludlow and Barker cites a source with the scheme is correct and becomes evidence: the scheme lived in books gentleman historians did not cite.

The second review also produced a fourteen-item errata list for anything reused from the paper (`findings-2026-11-second-review.md`, section 3): Fuller's *Historie of the Holy Warre* is 1639, not 1631, and he held no Cambridge chair; Mills's first edition is 1820; Gibbon's crusade chapters are in vol. 6; the *Catholic Encyclopedia* article is Bréhier's of 1908; Michelet's *Les Croisades* (1880) is a posthumous extract from 1833; Proctor (Procter) died in 1842, so the Crimean War preface of 1854 is the publisher's; Barker as Smail's supervisor is unconfirmed; and others.

---

## 4. The problem: what any numbering has to decide

### 4.1 What the canonical list assumes

The numbered crusades are a list of Holy Land expeditions in the traditionalist sense: aimed at Jerusalem or at the powers that held it. The Wendish, Albigensian, Baltic and Iberian crusades never received numbers in the main series, and Spain's Reconquista stays outside it in every Spanish book read (Las Navas falls unnumbered between the Fourth and the Fifth). "Holy Land" is loose even inside the list: the Fourth went to Constantinople, the Fifth and Seventh to Egypt, the Eighth to Tunis. Many Levantine expeditions are left out. In English Wikipedia's crusade box today, the unnumbered Holy Land expeditions (eleven) outnumber the numbered ones (eight).

### 4.2 The contested slots

Every count in the corpus has to answer the same handful of questions. The answers distinguish the schemes.

| Question | Options attested | Where the dispute is visible |
|---|---|---|
| **Is Henry VI's expedition (1195–97) the fourth?** | Yes: Maimbourg (1686), Moréri and the dictionary tradition to 1838, Michaud, Mills, Lefranc (1834, 1837), Saint-Allais (1816), British popular histories into the 1870s, Haydn's *Dictionary of Dates* to 1910. No: Koch (1771), Gibbon (1788), the modern eight. | The *Complément du Dictionnaire de l'Académie* (1842) names the Henry VI fourth as the minority practice and follows "l'usage le plus général." The last Henry VI fourth found in print is 1915. |
| **Is 1202–04 counted at all?** | Usually fourth or fifth. German encyclopedias of the 1830s–60s skip it (Pierer: "gewöhnlich gar nicht gerechnet"); so does the universal table of Stein's school atlas (1842). | Its status as "the Fourth" was settled first and most widely of the disputed slots. |
| **What is the fifth: Andrew of Hungary and Damietta (1217–21), or Frederick II (1228–29)?** | Damietta fifth: Koch, Gibbon, the modern eight. Frederick fifth: the 1820 Paris programme, German schoolbooks 1834–60, Chambers's, the Americana to 1953, Schaff (1907–67), German Wikipedia. Merged into one fifth ("1217–1229"): several German schoolbooks, Powell (1986) as an argument. | The modern eight's discriminating slot. The paper's second "primary problem." |
| **Is Frederick II counted on his own?** | Sixth on his own: Koch, the modern eight. Inside a long sixth (1213–44) with Damietta and the Barons: Moréri. Unnumbered: Gibbon. Refused as no crusade: Lévi Alvarès (1835). Seventh: Michaud, Rees (c. 1808). | Wikipedia's German editors made Damietta and Frederick one Fifth in 2007; Polish Wikipedia leaves Frederick out. |
| **Is the Barons' Crusade (1239–41) numbered?** | Sixth: Proctor (printed 1854), the *American Cyclopaedia* (1873), Swinton (1874), Larousse (1869, as Gregory IX's crusade). Seventh: Mills. Folded into another number: Moréri, Bréhier (1908, "1239 under the sixth"). Unnumbered: the modern eight. | English Wikipedia had no article on it until 2016; no edition has ever numbered it. |
| **Are Louis IX's two crusades seventh and eighth, or sixth and seventh?** | Seventh and eighth: Moréri, the modern eight. Sixth and seventh: Gibbon, the German seven. Seventh "and last" (Tunis unnumbered): Koch, Schöll, Saigey, Lamp. | Tunis as "huitième et dernière" is the French dictionary tradition's contribution to the modern eight. |
| **Is Edward (1271–72) part of the eighth, or a ninth?** | Inside the last: Mills ("the Last Crusade"), Myers (1885), Langer (1940). Named and excluded: Barker (1911). A ninth for Tunis, with or without Edward: Rees (c. 1808), Russell (1831, "Louis IX. and Edward I."), Perry (1865), Milner (1847), Cox (1874), EB9 (1877), the county atlases to 1936. Edward alone as the ninth: Masonic lore (1857), G. W. Cox (1887), the EETS *Godeffroy* (1893), Parry (1920), Outhwaite (1935), Scott-Giles (1979), Toropov (2002), English Wikipedia 2003–19. | English Wikipedia renamed "Ninth Crusade" to "Lord Edward's crusade" on 17 November 2019. |
| **How many in all?** | Six (Pasquier; German encyclopedias), seven (Koch, Gibbon, German schoolbooks, German Wikipedia), eight (Moréri, the modern eight, Larousse's own eight), nine (Rees, Mills, Michaud's English followers, Cox, Wikipedia 2003–19), more (Fuller's thirteen voyages; Carion and Bullinger's twelve). | A stated total is not a scheme: "On compte huit croisades" described the Moréri eight for 140 years before it described the modern one. |
| **What comes before and after?** | The People's Crusade and the Crusade of 1101 (Orderic Vitalis calls the 1107 expedition the "third"); the Children's Crusade (Schneller's sixth, 1810); Alexandria 1365 (Spanish Wikipedia's "Décima cruzada"); Nicopolis ("the last crusade"); the Hussite crusades (numbered four in Czech). | Wikipedia numbers the Swedish crusades First to Third while refusing numbers to the Levant's unnumbered expeditions. |

### 4.3 Count, label, name

A number can do three different jobs, and the project codes them apart:

- a **count** ("on compte huit croisades"), recorded as `stated_count`;
- a **slot**, the ordinal a source gives a particular expedition, recorded in the slot columns;
- a **name** ("the Fourth Crusade" as a proper name), visible when Arabic Wikipedia moved its titles from the indefinite to the definite form because the number had become "a proper name that cannot be indefinite."

The dictionary formula "on compte huit" survived from Basnage (1701) through Courtin's "communément" (1824) to Bouillet's "généralement" (1842) while the slots under it changed. Reading the formula as testimony for the slots was the mistake that made Bouillet look like an origin.

### 4.4 The rival schemes

The codebook names fifteen scheme families. The ones that matter:

| Family | Slots | First witness found | Last witness found |
|---|---|---|---|
| `moreri_eight` | H6 4, C 5, D+F(+B) 6, L1 7, L2 8 | Moréri, by 1689 | Haydn, 1910 (Henry VI fourth to 1915) |
| Koch's seven (not a separate code; coded `near_modern`) | C 4, D 5, F 6, L1 7 "et dernière" | Koch, 1771 | Lamp, 1839 |
| `gibbon_seven` | C 4, D 5, L1 6, L2 7; F unnumbered | Gibbon, 1788 | Tout, 1898 |
| `nine_F7` | H6 4, C 5, D 6, F 7, L1 8, L2 9 | Rees, c. 1808 | Parker, 1915 |
| `nine_H6` | H6 4, C 5, D+F 6, B 7, L1 8, L2(+E) 9 | Perry, 1865 (the ninth itself: Russell, 1831) | Historians' History, 1904–09 |
| `nine_B7` | C 4, D 5, F 6, B 7, L1 8, L2 9 | Universal Self-Instructor, 1882 | Gay's, 1891 (the chronology chain to 1936) |
| `frederick_fifth_seven` | C 4, F 5, L1 6, L2 7 | Desmichels and Trognon's Paris programme, 1820 | Americana 1953; Schaff reprint 1967; German Wikipedia today |
| `modern_eight` | C 4, D 5, F 6, L1 7, L2 8 | Desmichels, registered Dec. 1822 | current |
| `german_six` | D 4, F 5, L1 6 (C not counted) | Encyclopaedia Americana 1830 (from Brockhaus) | Schaefer's memorization tables, 1851–54 |
| `barons_sixth` | C 4, D 5, B 6, L1 7, L2 8 | Proctor (1842) | Adams, 1883 (variant: Johnson's, 1893–99) |
| `larousse_eight` | D 4, F 5, B 6, L1 7, L2 8 | Larousse, 1869 | — |

`german_seven` was renamed `frederick_fifth_seven` on 27 November 2026 because the scheme is attested in Paris fourteen years before any German witness.

---

## 5. How the database was built

### 5.1 Sequence of work

| Date (2026) | Session | What it produced |
|---|---|---|
| 8 Nov | Fact-check of the 2022 paper; citation, German, four-language and origin passes (Google Books snippets mostly) | A review document with a "Numbering corpus" of 85 works; the Mombert answer dead; Bouillet 1842 as the earliest modern eight then found |
| 8 Nov | Repository and project set up | Public GitHub repository, codebook, plan, decisions and research logs; 85 works migrated as dataset v0.1 |
| 8–9 Nov | Wikipedia sub-project | Ten language editions sampled yearly 2001–26, nine more for titles and navigation boxes, 22 for the scope of the crusade box; pageviews, Wikidata, GND, talk archives; the ledger and two visualizations; merged as PR #1 |
| 9 Nov | Second review | "Eight" is an eighteenth-century dictionary total; Bréhier is the bridge to Wikipedia; errata; Murray (2006) found |
| 10 Nov | Search protocol frozen; Strand A | The signature, evidence rules, census frames; 34 reference entries 1689–1869 read; the Moréri eight and Bouillet's two-slot change identified (PR #2) |
| 13 Nov | Delegated tasks (sub-agents) and decision point | Koch–Schöll lead; many `not_reached` rows (the agents could not open constructed URLs) |
| 13 Nov | Prior-literature check | No dedicated study 2016–26 in thirteen languages |
| 13 Nov | Browser pass | Koch 1771 settles the slots; Hübner 1704 is a bare total; the *Complément* (1842) "usage le plus général"; Duruy 1861 French text has the eight |
| 14 Nov | Strand D (English) and conclusions audit | English had five imported counts; Greene 1851 is Rendu translated; Henry VI fourth ends c. 1915; the 22-claim scorecard |
| 23 Nov | Gaps pass | Desmichels 1820 (seven) and 1823 (eight); the reasons table; usage counts; German schoolbooks; Edward as Ninth before 2003 (PR #4) |
| 27 Nov | The 1820–23 window and verification | The 1820 outline is an official programme; the exam question numbers nothing; registration 21 Dec 1822; Marchand's *Textes officiels* and the *Recueil de lois*; German block page-verified (PR #5) |
| 28 Nov | German snippet rows; reconciliation; answer books | Six German full sevens; one master table (`data/works.csv`); Bouchitté 1836 cites Desmichels |

### 5.2 Design principles

**Two questions, two designs** (`docs/SEARCH_PROTOCOL.md`, frozen 10 November). Q1 asks for the earliest complete modern eight. A priority search can never prove a first, so the answer is a bracket: the earliest attestation, and behind it a documented census of works in which the scheme is absent. Q2 asks how the scheme became the default, which needs rates inside defined populations and documented transmission, not more early instances.

**A frozen signature.** A work has the modern eight only if the fourth is 1202–04, the fifth 1217–21, the sixth Frederick II on his own, the seventh Louis IX 1248–54 and the eighth Tunis as the last number, with no number for Henry VI, the Barons or Edward. Fourth = 1204 together with sixth = Frederick II separates it from every rival.

**Census frames, not string searches.** Searching for ordinals finds only books that number. The frames are closed lists read whether or not a book numbers: Strand A (every edition of the general dictionaries, French and English, 1689–1870, plus German), Strand B (French works of 1800–42 in genres forced to enumerate: chronological tables, question-and-answer books, *précis*, exam manuals, official programmes), the roots frame (1675–1771), the German schoolbook frame (1780–1860), Strand D (English), the reference panel (1770–1930) and the school series. Strand C, a blind full-text sweep as a control, is not done.

**Evidence rules.** Reference works are revised silently, so the edition read is dated, never the work. `stated_count` is recorded apart from slots. A statement of custom dates a count, never a slot assignment (amendment adopted 27 November). A row counts toward the bracket only at full text, with the edition identified from the title page; a stable page link plus a viewed title page counts as the page image. `verification_level` rises from snippet to full text only after the page has been read. Every search is logged, negative results included. Translations are separate rows.

**Coding.** Slot columns for the eight expeditions that carry the dispute (H6, C, D, F, B, L1, L2, E), `scheme_family`, `signature_match`, `stemma_parent` with the evidence for the link (shared wording, or inferred), quotation in the original language, verification level, title-page status, census frame. A family code is given to a partial row only when its numbered slots are diagnostic. Since 28 November all print rows live in one table, `data/works.csv`, and the numbering rows are derived from the slot columns.

**Roles and disclosure.** The corpus was found, read and coded by Claude in long browser sessions, with the author deciding every coding and scope question and reading the bracket pages himself before any claim is retired or adopted. Earlier recollections are marked `recalled`. Some quotations from the first agent run passed through a summarizer and are flagged. No second coder has checked any row. A *Digital Medievalist* methods section will have to say all of this.

### 5.3 Sources and access

Reading was done in the built-in browser, because the workspace's shell reaches only GitHub: archive.org full text and djvu text, Gallica (SRU, ContentSearch, ALTO), the Google Books text layer and page images, MDZ (full-text search, hOCR, IIIF), the DTA, Persée, Wikisource, the BnF and SUDOC catalogs, and the MediaWiki API. Blocked or limited: HathiTrust (bot check, not attempted), Google Books captchas on some days, the Library of Congress subject headings (bot check), the Wikisource and other hosts when nobody was present to approve access, the CCFr's federated search, and WorldCat (terms not accepted on the author's behalf). Archive.org lending copies were borrowed through the author's account and returned. Nothing is saved as a scan in the repository; every row carries a stable URL.

---

## 6. Size and scope of the database

### 6.1 Print works (`data/works.csv`)

**224 rows**, one per edition, translation or catalog read. 148 were read under the protocol (strands A, B, D and the panel) and 76 are legacy rows from the November review that no later strand re-read. (After Strand D2 that evening: 347 rows, 124 of them new English rows; 184 English rows of 1788–1945 carry D2 attributes in `data/strand_d2/attributes.csv`.)

| Measure | Count |
|---|---|
| Date range | Orderic Vitalis (12th c.) to the Atlas school handout (2026) |
| Before 1700 | 9 |
| 1700–1799 | 29 |
| 1800–1849 | 86 |
| 1850–1899 | 63 |
| 1900–1949 | 21 |
| 1950 to the present | 15 |
| No sortable year | 1 |
| French | 85 |
| English | 76 |
| German | 36 |
| Italian 9, Spanish 8, Greek 3, Dutch 3, Latin or Latin/German 4 | 27 |
| Reference works | 70 |
| School texts | 45 |
| Other genres (scholarship, popular and universal history, translations, chronologies, syllabi, catalogs) | 44 |
| Genre not yet coded | 65 |

**Verification.** 126 full text, 71 snippet, 19 contents page, 3 from the paper's table, 3 secondary, 2 unverified. Among the 148 protocol rows: 100 full text, 45 snippet. Title pages have been checked, by image or OCR text, for 40 rows; 184 rows have no title-page check.

**Scheme families** (protocol rows; legacy rows carry slots but no family code): modern eight 32, Moréri eight 31 (plus 3 variants), Frederick-fifth seven 16 (plus 1 variant), no ordinals beyond the first 15, near-modern 7, stated total only 5, Gibbon seven 4, nine with Frederick seventh 4, German six 3, other 3, nine with Henry VI 2, Larousse eight 1, Barons-sixth variant 1. Twenty-nine rows have all five signature slots of the modern eight filled; the earliest eight of them are dated 1823, 1824, 1827, 1834, 1835, 1836, 1842 and 1842.

**Census frames.** Strand A French and English 40, Strand A German 2, roots 1675–1771 6, Strand B France 1800–42 27, German schoolbooks 1780–1860 22, Strand D English 12, reference panel 20, school series 18; 80 rows found outside any frame.

### 6.2 Derived and companion tables

| Table | Rows | What |
|---|---|---|
| `numberings.csv` | 682 | One row per work, expedition and ordinal, derived from the slots |
| `numberings_unparsed.csv` | 18 | Rows that enumerate but have no slots yet |
| `search_log.csv` | 281 | Every search since 10 November, negative ones included |
| `reasons/reasons.csv` | 28 | Explicit statements of why a count is used, disowned, or where it came from, 1701–2001 |
| `citations.csv` | 16 | Documented and inferred citation edges |
| `not_reached` tables (Strand A, A German, B, panel) | 79 | Works in a frame not yet read, with the reason |
| `strand_b/frame.csv` | 31 | The Strand B census frame |
| `usage/archiveorg_ordinal_counts_en.csv` | decades 1840s–2010s | Archive.org document counts for each English ordinal phrase |
| `reconciliation/` | — | Id crosswalk (232 old ids), 11 slot conflicts, ledger map (78/78), hand-coding queue (66) |
| `ledger/ledger.csv` | 115 | The visualization ledger: 78 print works and 37 Wikipedia runs |

### 6.3 Wikipedia (`data/wikipedia/`)

Ten editions sampled on 1 July of every year 2001–2026 (English, German, French, Italian, Spanish, Dutch, Greek, Arabic, Persian, Hebrew): 461 page-year observations, 182 article-creation records, 42 title moves, 43 pinned key edits (each checked against its parent revision), 19 explicit count statements, ordinal titles in nineteen languages, pageviews 2015–26, Wikidata series, GND headings, and the membership of the crusade box in twenty-two languages. Built from the MediaWiki API; reproducible.

### 6.4 Outputs so far

Thirteen findings notes and four Wikipedia notes; the Crusade Numbering Ledger and the scroll story "Nine, then eight: How Wikipedia Numbered the Crusades" (in `site/`); a popular-essay outline. Five pull requests: #1 (Wikipedia) merged; #2–#5 open and stacked (Strand A → delegated tasks → gaps pass → the 1820–23 window, reconciliation and answer books).

---

## 7. Interim conclusions

Ordered from the earliest layer to the latest. Each carries its grade.

### 7.1 Numbering crusades is early modern and was loose for two centuries. **Firm** for the pattern; several individual witnesses provisional.

Expeditions were counted long before the modern eight, and the counts disagreed about almost everything except the first three. Orderic Vitalis already calls the 1107 expedition a "third." Carion and Bullinger count twelve (the Third as three); Pasquier six; Fuller (1639) thirteen numbered "voyages" without the word crusade; Maimbourg (1675–76, 1686) makes Henry VI's expedition "cette quatrième Croisade"; G. C. Müller (1709) five. Eighteenth-century counts outside the dictionaries are independent of each other: Lenfant (1724) puts Henry VI fifth and runs to an eighth; Velly (1755) counts only French expeditions and makes Louis IX's first the fifth; Fleury's index (1758) puts Damietta sixth; Lenglet du Fresnoy numbers nothing. The Enlightenment historians (Voltaire, Hume, Robertson) number only the first one or two, as the paper said. The *Encyclopédie* (1754) numbers nothing.

### 7.2 "Eight crusades" is a dictionary total, fixed by 1701, with Tunis as the last. **Firm.**

Moréri's *Grand dictionnaire historique* has eight numbered sections, ending "Huitième & dernière Croisade," by its 1689 edition (the 1674, 1681 and 1683 editions show no numbered crusades by OCR search; negative provisional). Basnage's revision of Furetière (1701) supplies the formula "On compte 8. Croisades." Hübner's German lexicon (1704) has "Man zehlet acht Croisaden," with no list. Trévoux condenses Moréri's sections under Furetière's formula; Chambers (1728) translates Trévoux; Britannica's first edition (1771) keeps the total and drops the list; its second to eighth editions (1778–1854) keep the Moréri slots. Saint-Allais (1816), Courtin's *Encyclopédie moderne* (1824, "On compte communément huit croisades"), the *Dictionnaire de la conversation* (1835) and Furne's *Biographie universelle* (1838) all have the Moréri eight or a variant. Every French and English reference entry from 1689 to 1838 that numbers all eight uses this one scheme: Henry VI fourth, 1202–04 fifth, a long sixth from 1213 to 1244 (Damietta, Frederick II and the Barons together), Louis IX seventh and eighth.

Before 1838 "eight" was therefore a stable answer to "how many" and an unstable answer to "which."

### 7.3 The fourth to seventh slots are Koch's, printed in 1771. **Firm** for the text; **provisional** for Koch's own source.

Christoph Wilhelm Koch's *Tableau des révolutions de l'Europe* (Lausanne and Strasbourg, 1771), pp. 64–65: "On en compte proprement sept … La quatrième en 1202 … La cinquième en 1217, par André, Roi d'Hongrie. La sixième en 1228, par l'Empereur Frédéric II. La septième enfin, en 1248, par Louis IX." No Henry VI, no numbered Tunis. "Proprement" reads as a correction of the Moréri eight: it drops Henry VI, separates Damietta from Frederick II, and stops at Louis IX's first crusade. The same seven runs through Schöll's revision of Koch (1823, read in Crichton's English translation of 1839) and Schöll's own works (1825, 1830), Saigey's *Précis de chronologie* (Hachette, 1834) and Lamp's *Tables synchronistiques* (1839), each ending "septième et dernière." Gibbon (1788) independently has the 1202 fourth and Damietta fifth, but no Frederick II; he is a witness to the fourth, not its source. What Koch himself read is unknown.

### 7.4 The complete modern eight is first attested in Desmichels's *Tableau chronologique*, registered 21 December 1822. **Firm** for the text and date; **probable** for priority.

C.-O. Desmichels (1793–1866), professor of history at the collège royal Henri-IV, *Tableau chronologique de l'histoire du moyen âge* (Paris: Louis Colas), pp. 63–66: 1202–04 fourth, Andrew of Hungary and John of Brienne fifth, Frederick II sixth, Louis IX seventh, Tunis "huitième et dernière." Title page viewed; full-text read. The *Bibliographie de la France* registered the book in N° 51, Saturday 21 December 1822, as no. 5716; the 1823 on the title page is a post-date, and Larousse's "Paris, 1822" is the registration year, not a separate printing. The title page carries no "autorisé par le conseil royal" line. The *Revue encyclopédique* (1823) reviewed it as the volume that "complète" a Colas series of tables that the Université "a commandées." No document read gives Desmichels's reason for his slots.

The scheme is Koch's seven with the dictionary tradition's numbered Tunis on top. Whether Desmichels took the slots from Koch is inference: they match exactly, Koch circulated in Paris editions (1807; Schöll's revision of 1823), but the book has no preface and names no source.

Priority is graded probable because one official text from the same months is unread (section 8.1) and because priority searches can only bracket.

### 7.5 The same author counted seven three years earlier, in the official course outline. **Firm.**

The *Tableau sommaire du cours d'histoire générale* (Paris: Colas, 1820; Gallica bpt6k65448935), headed "Commission d'instruction publique" and written by Desmichels and Auguste Trognon (professors at Henri-IV and Louis-le-Grand), was registered in April 1820 (*Bibliographie de la France* no. 1350) together with the companion programmes for French and ancient history (nos. 1351–52), all in-4 from Colas. The circular of 4 July 1820 sent these cahiers to the rectors and hoped the programmes would be developed into "livres élémentaires." Chapter XIV, "De l'Orient et des croisades," numbers the 1202 crusade fourth, Frederick II fifth, Louis IX sixth and seventh, and names Andrew II's expedition without a number. It is the earliest witness found anywhere to the Frederick-fifth seven.

Between 1820 and late 1822, therefore, one Paris teacher changed his own official count: he numbered Andrew's expedition fifth, moved Frederick II to sixth, and turned Louis IX's crusades into the seventh and eighth.

### 7.6 The Université's own texts did not number the crusades. **Firm** for the texts read; **probable** overall.

- The statute of 4 September 1821 split the course: troisième took "l'histoire du Moyen Âge" (art. 172) and seconde "l'histoire moderne proprement dite" (art. 176). That split is why Desmichels wrote a separate medieval table and why the second edition of the 1820 outline (October 1822, "autorisé par le conseil royal") was retitled for "histoire moderne." No copy of that second edition has been found.
- The règlement of 13 March 1821 (read in the *Recueil de lois et règlemens*, t. 7) ordered a table of baccalauréat questions in three series, history and geography the second, drawn by numbered balls (art. 6). It does not print the table.
- The table itself, as printed by Hubert in 1826 (p. 16, page image viewed), makes the Middle Ages its own section. Question 14 asks for "État de l'empire d'Orient et de l'Asie à la fin du XIe siècle. — Précis historique des croisades. — Résultats généraux des guerres saintes …" with no ordinals.
- The texts of 1818–26 printed in Marchand's *Textes officiels* (INRP, 2000), read page by page, do not number the crusades. Marchand found only the Roman programme cahier and missed the general-history one that this project reads on Gallica; he does not mention Desmichels.

The examination asked for the crusades; it did not number them.

### 7.7 The eight spread through the exam-preparation market, and one manual names Desmichels. **Firm.**

The answer books to question 14 decide whether a candidate learned a number. Six have been read:

| Book | Year | Numbering |
|---|---|---|
| *Manuel complet des aspirans au baccalauréat* (Delalain) | 1824 | Desmichels's list, headings copied word for word |
| Ponelle, *Nouveau manuel complet* | 1826 | None in the answer; "quatrième croisade" in passing |
| Delavigne, *Manuel complet* | 1829 | "Les cinquième et sixième croisades" for 1217–1228, "les deux dernières" for Louis IX |
| Ponelle, *Manuel complet* (Mansut fils) | 1829 | As in 1826 |
| Delavigne, *Manuel complet* | 1835 | As in 1829, naming Andrew of Hungary for the fifth and Frederick for the sixth |
| Bouchitté, Charma, Saigey and Lesieur, *Manuel des aspirants* (Hachette) | 1836 | The full eight under numbered headings to "8e et dernière croisade," with a footnote: "Nous avons adopté la division des croisades indiquée dans le Précis d'histoire du moyen-âge de M. Desmichels." |

Four of six use the modern slots, two number nothing, none uses an older count. Bouchitté's footnote (second pagination, p. 158, page image viewed) is the first explicit attribution of the modern eight to a source found anywhere in the project. Desmichels's own *Précis de l'histoire du moyen âge* carried the eight from 1827 through a fourth edition co-published by Colas and Hachette (1834) and a Brussels edition (1835).

### 7.8 Paris reference works reported the eight in 1842; they did not make it. **Firm.**

Ansart and Rendu's *Cours d'histoire et de géographie* for the écoles normales primaires, written "d'après le Programme arrêté … par le Conseil Royal," has the eight in its second edition (1841–42), and Ansart's *Nouvelles Tablettes chronologiques* (1842) prints it in full (both read at snippet level so far). In 1842 three Paris reference works print it: Bouillet's *Dictionnaire universel d'histoire et de géographie* (Hachette), vol. 6 of Le Bas's *France: dictionnaire encyclopédique* (Didot), and the *Complément du Dictionnaire de l'Académie française* (Didot), which adds that "quelques historiens" count Henry VI's expedition fourth and concludes "Nous avons suivi l'usage le plus général." That is the first statement of custom about the slots rather than the total. Bouillet's entry is an abridgment of Courtin (1824) through Furne (1838) with two changes: he drops Courtin's fourth (Henry VI) and splits Courtin's sixth into a fifth (Damietta) and a sixth (Frederick II). His "généralement" is Courtin's "communément," which had described the Moréri eight.

The French chain runs: Koch (1771) and the dictionary tradition → Desmichels (1820 seven, 1822 eight) → exam manuals (1824–36) and Desmichels's *Précis* (1827–35) → normal-school courses (1840–42) → reference works (1842). After 1842 the eight is found in Duruy (Hachette, 1861; "La première croisade fut bien différente des sept autres"), Dezobry and Bachelet (1863), the *Grande encyclopédie* (1890s) and the *Petit Larousse* (1906). Larousse's *Grand dictionnaire* (1869) is the exception: its own eight gives the fourth to Andrew II "plus généralement," Frederick II the fifth and Gregory IX's crusade the sixth. Five of six enumerating panel rows 1842–1906 have the modern eight; the panel is not closed, so no share can be stated.

One flagged pattern: Bouchitté's manual (1836), the fourth edition of Desmichels's *Précis* (1834), Saigey's Koch-type chronology (1834), Bouillet's dictionary (1842) and Duruy's *Histoire du moyen âge* (1861) are all Hachette books. The modern eight was in Hachette's school list by 1834–36, and the *Complément*'s first director was a professor at Bouillet's collège. The route from the textbooks to Bouillet is short, but it is not documented.

### 7.9 English imported five counts and combined them into two nines of its own. **Firm** for the pattern (Strand D2 full-text pass); individual rows mixed.

Until about 1910 English books carried, side by side:
- the **Moréri eight** from the French dictionaries (Chambers 1728; Britannica 1st–8th eds. to 1854; Haydn's *Dictionary of Dates* to 1910; W. F. Collier's Nelson school text c. 1860, copied into an American home-study course in 1909);
- the **Michaud/Mills line** (Mills 1820, with Henry VI fourth and "the Last Crusade" for Tunis and Edward, an eight; then the nine of Townsend 1862, Perry 1865, Cox 1874 and the Britannica 9th ed. 1877, whose ninth holds Tunis and Edward and is first attested in Russell's *Palestine*, 1831; Mackay 1841 counts ten; Milner 1847 has Rees's nine with Frederick seventh);
- **Gibbon's seven** (Chepmell 1857, the Student's Gibbon 1868, Gilbert's *The World* 1882, Tout 1898);
- the **German counts**: the six of Brockhaus (Americana 1830, Collier's 1921) and the Frederick-fifth seven, first in English in Stebbing (Edinburgh, 1830), then the Penny Cyclopaedia 1837, Chambers's 1868–1926, Ploetz in translation 1883–1905 and Fisher 1885, the Americana from 1918, Schaff 1907–67;
- the **modern eight**, entering through French schoolbooks in translation.

The earliest English modern eight found is Greene's *History and Geography of the Middle Ages* (New York: Appleton, 1851), whose preface says it is taken from "a popular French work" with the sanction of the University; the text is Ambroise Rendu's part of Ansart and Rendu, translated ("The fifth and sixth crusades began in Germany"). The earliest British ones are Beale's *Student's Textbook* (London, 1858) and James White's *Eighteen Christian Centuries* (Edinburgh, 1858), sources unknown. Tainsh (1875), Gazeau (1878, a French Catholic textbook in translation), Steele (1883), Myers (1885, noting that counting Henry VI makes nine), the 1891 translation of Duruy, Mombert (1894) and Ludlow (1896) follow.

Schools led and reference works lagged. American and British school texts had the eight from the 1850s; the major encyclopedias kept older schemes until Bréhier's *Catholic Encyclopedia* article (1908) and Barker's Britannica article (1911, reprinted to 1962). The *New International Encyclopaedia* (1917) still says only "the first four Crusades" carry numbers "by unanimous consent." The last Henry VI fourth found in English is an anti-Catholic tract of 1915; the German-derived seven outlasted it by half a century (Americana to 1953; Schaff's reprints to 1967).

**Strand D2 (evening of 28 November)** read 184 English rows of 1788–1945 at full text or derived them from their slots, with full-text counts beside them. What it adds:

- *The Fourth did not move; its rival died out.* In archive.org full text the 1202–04 fourth is the large majority in every decade; the Henry VI share of decided items peaks at 0.25 (1810s) and 0.19 (1850s, 1870s) and is 0.05 or less from the 1890s. The Henry VI fourth lived in a few series (Britannica 2nd–9th eds. and US reprints to 1902; Haydn 1866–1910; Mills and the Historians' History 1904–09; Robson's Michaud to 1900; Cox to 1901; Nelson's Collier; American Catholic schoolbooks). Only two series changed their fourth: the Britannica toward 1202–04 with Barker (1910–11), and Swinton toward Henry VI in his Canadian revision (1883), copied from EB9. Scholars (Hallam, Procter, Pears, Stubbs, Archer, Munro) and most schoolbooks wrote 1202–04 throughout. Barker canonized the outcome; he did not cause it.
- *Gibbon was cited, not followed.* Of 42 rows that name him where it counts, 16 agree on every shared slot, mostly C 4 and D 5, which the modern eight shares. His sixth and seventh survive in a handful (Chepmell, the Student's Gibbon, Murray's 1869 printing of the chapters, Gilbert, Turner, Mosheim in Reid's edition).
- *The Ninth had six referents before 1945*: Tunis with Edward (Russell 1831 to county atlases of 1936 and Newman's *Manual* to 1937), Tunis alone, Louis IX's first crusade (Mackay, W. C. Taylor, G. A. Smith, Blyth, the *Daily Express Encyclopaedia* 1934), Thibaut (the Americana table), Gregory X's projected crusade of 1274, and Edward alone. The Edward-alone ninth is attested from Masonic lore (1857, 1872), Lupton (1883), G. W. Cox's *Concise History of England* (1887), the EETS *Godeffroy* (1893) and Parry (1920): English writers telling Edward's story kept the ninth after the count that produced it had gone. The modern split (Tunis eighth, Edward ninth) was not found before 1945.
- *National differences.* American reference works had the 1202–04 fourth by 1873, a generation before the Britannica; Canadian printings (Haydn, Collier, Swinton revised) kept the Henry VI fourth longest; Edinburgh firms printed both the old reference counts and three of the new ones early.

### 7.10 Germany kept a Frederick-fifth seven, which is not German in origin. **Firm** for the German schoolbooks; **probable** for the origin.

German usage of 1756–1830 is Moréri-type (Broughton's translation 1756, Beck 1790, Pütter 1795, Becker 1804–19, Schneller 1810–41) or Gibbon-type (the German Gibbon 1791, Herder 1792, Collin 1818). German encyclopedias of the 1830s–60s count six and skip 1202–04 (Brockhaus 1837, Pierer 1857). The Frederick-fifth seven appears in German schoolbooks from 1834 and is now read at full text in six of them: Fiedler (1834), the Catholic *Handbuch … für Schule und Haus* (1835, merged fifth), Haas (1844), Beitelrock (1853), Dietsch (1854), Kurts (1860, sixth from split OCR). Uschold (1839) and Weber (1847–49) stop at five with Frederick fifth. Stein's school atlas (1842, 1849) carries two counts at once: Frederick fifth in its German table, and in its universal table a five-count with Frederick fourth and Louis IX's 1248 crusade "fünfter u. letzter."

The same seven stands in the Paris programme of 1820, fourteen years before any German witness. The working hypothesis is a Gibbon-derived school seven that circulated in both countries. German academic historians named rather than numbered (Wilken, Raumer, Sybel); the German National Library keeps both counts as variants of dated headings; German Wikipedia states "insgesamt sieben Kreuzzüge" and calls the one-to-eight or one-to-nine sequence the count of "französischen und englischen Literatur."

A pattern, flagged as inference: in Haas and Beitelrock the full seven appears only in the chronological table; the narrative numbers the second and third and stops. In France too the course table numbered and the exam question did not. The numbers lived in tables.

### 7.11 The other national chains: Italy, Spain, Greece, the Low Countries. **Provisional** (snippet-level, from the first review).

Cantù's *Storia universale* first edition (1842–44) has its own eight (Andrew's 1217 expedition fifth, Damietta sixth) and is re-split to Bouillet's list by 1851; the French translation of 1854 pairs the fifth and sixth in one chapter. Michaud was translated and reprinted in Italy to 1941; Italian school texts take the eight in the 1890s. In Spain the Reconquista stays outside the series; Avendaño (1846) has an eight; Mellado's adaptation of Bouillet (1846) carries the Paris list. Greek writers call 1204 "Τετάρτη Σταυροφορία" from Koromelas (1845), and the 1893 teacher-college syllabus pairs it with the fall of medieval Hellenism. Dutch books split: northern schoolbooks the German seven, French-derived and Catholic books the French eight.

### 7.12 Almost nobody gave a reason before 1900; after 1900 the scheme was disowned while it was used. **Firm.**

Of 28 explicit statements collected, those before 1900 report custom ("on compte," "they reckon," "communément," "généralement," "l'usage le plus général") or argue about single slots: Lévi Alvarès refusing Frederick II's voyage as a crusade (1835), Pierer on 1202–04 as "usually not counted" (1857), Larousse giving Andrew the fourth "plus généralement" (1869), Myers noting a ninth (1885). Desmichels's change of 1820–22, the moment that matters most, has no comment at all. After 1900 the statements turn against the whole scheme: "unanimous consent" for only the first four (1902), "arbitrary" (Bréhier 1908), "conventionally … their distinctness cannot be maintained" (Chambers's 1926), "for the sake of convenience" (1935), "lacks all consistency" (Mayer 1965), "conventional for the movement was essentially continuous" (Chambers's 1966), "not particularly helpful" (Russell 2000). The one pre-1900 statement of source is Bouchitté's attribution to Desmichels (1836).

### 7.13 Specialists stopped at five; general usage did not. **Probable.**

The stop after the Fifth is a specialists' habit, older than the paper thought: Oman (1898), Myers's *General History* (1889), Previté-Orton (1916; also 1937), Paetow (1917) and the *Cambridge Medieval History* (1926) number to the Fifth and then name by leader (Strand D2). It is visible later in descriptive chapter titles (Setton's *History*, vol. 2, 1962: "The Crusade of Frederick II," "The Crusades of Louis IX") and in Mayer's verdict. In general print there is no fall: in archive.org document counts, "Sixth Crusade" per "Fifth Crusade" drifts from 0.88 in the 1840s to 0.56 in the 2010s, while "Seventh Crusade" per "Fifth" rises from 0.32 to 0.81. The paper's "consensus since Runciman" holds for monographs and is the wrong description of usage at large.

### 7.14 Wikipedia inherited Bréhier's French eight and then went to nine and back. **Firm.**

The oldest surviving English "Crusades" article (28 October 2001, unsourced) lists eight with Bréhier's dates, including the odd ones (1095–1101, 1188–92, 1249–52). Three weeks later the *New Schaff-Herzog* article was pasted beside it, so for four and a half months Frederick II was the Sixth at the top of the page and the Fifth at the bottom. A Ninth (Edward) appears in April 2003 and the editions converged on nine between 2003 and 2012, faster and more uniformly than any printed tradition; English renamed its Ninth on 17 November 2019 and dropped the last "Ninth" from the main article in December 2021. German Wikipedia kept the seven with the modern count in brackets; Polish counts seven by omitting Frederick II; Arabic's navigation box counted eight until December 2013, and Arabic turned its numbers into proper names. Neither English nor German Wikipedia has ever numbered Henry VI's crusade, 1101 or the People's Crusade, and no edition numbers the Barons' Crusade. The "Ninth Crusade" redirect still drew a third of the traffic to Edward's article in 2025. No edit spike followed 11 September 2001; the 9/11 era shows only in the "Tenth Crusade" pages (English 2005–10, deleted; Arabic 2009–, the war on terror as crusade).

### 7.15 The answer to the title, as it now stands

The crusades were numbered by dictionary compilers who fixed a total of eight around 1700, by a Strasbourg professor's textbook that fixed the fourth to seventh slots in 1771, and by a Paris history teacher who revised his own official count of 1820 when he wrote for the Université's new Middle Ages course in 1822. The numbers reached students through his textbooks and the exam manuals that copied and cited them, reached Paris reference works by 1842, and reached English through translated French schoolbooks from 1851 and through Bréhier and Barker after 1908. Crusade historians received the numbers and did not make them. (The author has put this sentence on hold until he has read Desmichels 1823, pp. 63–66, himself.)

---

## 8. Points of uncertainty

### 8.1 Could the Université have prescribed the eight after all?

The one unread document that could move the answer is *Questions sur l'histoire ancienne, l'histoire romaine, l'histoire du moyen âge, l'histoire moderne* (Paris: Brunot-Labbe, "libraire de l'Université"; registered 15 June 1822, again 28 December 1822; BnF G-31078, 44 p.; an 1823 printing, 16-G-434, 48 p.). Since the règlement of March 1821 orders the question table but does not print it, this pamphlet is probably the table's first printing. If its question 14 numbers the crusades, the switch belongs to the Université and not to Desmichels. It is not digitized. BnF reproduction: per-page PDF €0.70 a page excl. VAT (3–4 weeks), full PDF €45 excl. VAT (5–7 weeks), or reading at Tolbiac. Not ordered.

The second edition of the 1820 outline, *Tableau sommaire pour servir à l'enseignement de l'histoire moderne* (Colas, October 1822, "autorisé par le conseil royal"), would show whether the authorized revision kept any Middle Ages and which count it used. It is in none of the BnF, SUDOC, BVB, K10plus, SWB, Jisc or BNE catalogs. WorldCat and a manual CCFr search have not been run.

### 8.2 Why did Desmichels change his count?

Nothing read explains it. Candidate explanations, none tested: the 1821 split of the course into a separate Middle Ages year, which gave him a whole book for what had been one chapter; reading Koch in Schöll's 1823 revision or the 1807 Paris edition; the dictionary habit of a numbered eighth at Tunis. Which edition of the *Précis* Bouchitté used is also unknown.

### 8.3 The roots

- Koch's own source is unknown. The Strasbourg and German compendia of 1700–70 are unsearched.
- The Moréri negative for 1674–83 rests on OCR search of poor scans; the eight's entry into Moréri between 1683 and 1689 is provisional.
- Maimbourg's numbers above the fourth are not confirmed (poor OCR).
- Rees's *Cyclopaedia* nine with Frederick seventh: the issue date of the CROISADE part (c. 1808) rests on a secondary source.
- Hübner (1704) and Basnage (1701) are bare totals; "which eight" cannot be answered from them.

### 8.4 Gaps inside the French chain

- Lefranc's 7th edition (1841) is unread; his 1834 and 1837 editions keep Henry VI fourth.
- Ruelle and Huillard-Bréholles (1842) and Abel Hugo (1839, a nine with Frederick sixth) are snippet-level.
- The first edition of Ansart and Rendu (1840–41, BnF G-18709) is not digitized.
- Whether Bouillet drew on Hachette's own school list is untested.
- Larousse's later editions and the date he switched are unread.
- Duruy's role in schools after 1861 is not traced.

### 8.5 Verification and coding

- 71 rows are snippet-level, among them the whole Italian, Spanish, Greek and Dutch evidence and many legacy rows. 184 of 224 rows have no title-page check.
- No second coder has checked any row; the protocol requires one on the bracket rows and a 10% sample of the panel.
- Some quotations from the 13 November agent run passed through a summarizer (the *Petit Larousse* "quote" is a paraphrase of noisy OCR); the *Grande encyclopédie* year is recalled.
- The two Edward conflicts are resolved (Strand D2): EB9 (1877) puts Edward in the ninth with Tunis; Barker (1911; the 1923 book reprints the article) names Edward's expedition and excludes it from the numbering (`r29`). See `data/reconciliation/conflicts.csv`.
- Kurts's sixth (1860) rests on OCR broken across columns.
- Several rows are coded from translations (Koch via Crichton 1839; Duruy 1891) and are not evidence for the original's numbering.
- 65 rows have no genre code and 22 enumerating rows have no slots (four of them Strand D2 rows whose ninth names no slot).
- Legacy rows carry slots but no family code, so family counts in section 6 cover only protocol rows.

### 8.6 What the corpus can and cannot support

The early review rows came from string searches, which find only books that number. Shares and words such as "dominant" or "standard" are not supported anywhere outside the closed frames, and the reference panel is not yet closed. Strand C, the blind full-text control sweep, has not been run, so the protocol's stopping rule for the priority question is not met. The International Medieval Bibliography, RI-OPAC and JSTOR have not been searched for prior literature, and a 2019 paper on the Crusade of 1101 that discusses numbering in passing is unidentified.

### 8.7 Smaller open points

- Whether Saigey of Bouchitté's team is the J.-F. Saigey of the Koch-type *Traité de métrologie* (1834).
- The source of the Stein atlas's five-count.
- The Crimean War as a trigger for English reprinting: tested in Strand D2. A cluster of English crusade titles falls in 1852–56 and the war was called "a sort of ninth Crusade" in 1855, but the books reprinted carry older counts. It explains reprinting, not numbering, and cannot explain the origin (Bouillet is 1842, the war 1853–56).
- Barker as Smail's doctoral supervisor: unconfirmed.
- Wikipedia coding: whether navigation boxes or main articles are authoritative, and whether asides ("sometimes counted as the Ninth") count. Both await the author's decision. The Library of Congress subject headings are unread, and the deleted English "Tenth Crusade" text cannot be checked without an administrator.

---

## 9. Future expansion

### 9.1 Steps only the author can take

1. Read Desmichels 1823, pp. 63–66 (Google Books ZcweZNLzfukC), and the other bracket pages listed in `notes/findings/2026-11-window-1820-23.md`. The Bouillet line in the thesis is replaced only after this.
2. Order or read BnF G-31078 and check question 14 for ordinals.
3. Search WorldCat and the CCFr by hand for the 1822 *Tableau sommaire*, then ask the Bibliothèque Diderot (Lyon) or the Musée national de l'Éducation (Rouen).
4. Save PDFs of the bracket rows (Loriquet 1815, Caillot 1818, the 1820 programme, Desmichels 1823, the 1824 *Manuel*).
5. Run IMB, RI-OPAC and JSTOR before claiming priority in print.
6. Decide the provisional items in `docs/DECISIONS.md`: `works.csv` as single source and its merge rule; one row per table when a book has two counts; the `attribution` reasons kind; implied ordinals not coded; family codes for partial rows; the Wikipedia coding questions; the publication plan.
7. Merge the stacked pull requests #2–#5.

### 9.2 Research still needed for the title question

- The Université programmes and question lists of 1826–42, and the later answer books (Bouchitté 1838 onward and others after 1836).
- Which edition of Desmichels's *Précis* Bouchitté followed.
- Koch's sources in the Strasbourg and German compendia of 1700–70.
- German school histories of 1800–33, for a Frederick-fifth before 1820.
- Strand C, the blind sweep: the signature strings across Gallica, Google Books, HathiTrust, archive.org and MDZ for 1750–1845 in four languages, until two independent corpora return nothing earlier.

### 9.3 Diffusion (Q2)

- **France 1842–1914** (gap C5): close the reference panel (Larousse editions, the *Grande encyclopédie*, Bouillet's later editions), and read the long school series edition by edition (Duruy, Lefranc, Desmichels's *Précis*).
- **The Hachette hypothesis**: test whether Bouillet took the eight from his publisher's school list.
- **Germany**: Strand A German (Brockhaus, Pierer, Meyer, Ersch-Gruber) at full text; a systematic schoolbook frame from GEI-Digital; the Catholic-before-Protestant prediction by confession.
- **Italy**: Cantù's Turin editions of 1847–51 to date his switch.
- **English**: Beale's and White's sources; the Strand D2 leftovers (reference volumes missed by the headword search, the December 1917 "ninth crusade" cluster, Irish school books, EB 1938/1944 lending copies; `notes/findings/2026-11-strand-d2-english.md`, sections 10–11); Chambers's 1950s and the Americana after 1953; LCSH by hand.
- **The fall**: Runciman vol. 3, Setton vol. 2, Grousset and Mayer read directly; current French usage, where Balard and Richard still number to eight.
- **Tier 3 and 4 languages** (Portuguese, Scandinavian, Polish, Czech, Hungarian, Russian, Catalan, Latin school texts; then Romanian, Croatian and Serbian, Ottoman Turkish and Arabic) as a check on whether the western numbers were adopted wholesale, as Wikipedia suggests.
- **Text reuse**: detection across the collected entries, to replace inferred stemma links with documented ones.

### 9.4 Data

- `status` values for named, unnumbered, explicitly excluded and aside, so the ledger can be generated from `works.csv` rather than hand-coded.
- `evidence.csv` with quotation, page, URL and verification for every numbering.
- Genre for 65 rows and slots for 22 (the two Edward conflicts were resolved in Strand D2).
- A second coder on the bracket rows and a 10% panel sample.
- A versioned data release with a DOI on Zenodo; the repository renamed to drop its trailing hyphen.

### 9.5 Outputs

- **The article for *Digital Medievalist*.** The audit of 14 November recommended leading with the print study and treating Wikipedia as a companion, reversing the second review's recommendation of 9 November to publish the Wikipedia study first. The author has not yet decided. With the 1820–23 window closed as far as the online record allows, the print study now has a firm core: the Moréri total, Koch's slots, Desmichels's two counts, the exam manuals and Bouchitté's attribution, the 1842 reporting, and the English import route.
- **The popular essay.** Its outline (9 November) builds to Bouillet as the reveal; the reveal is now Desmichels and the exam manual that names him.
- **The site.** The timeline of counts and the slot-drift chart carry the argument; the citation network now has its first documented edge into the modern eight (Bouchitté → Desmichels); the Wikipedia scroll story is built.

---

## 10. Appendix A: the key witnesses in date order

| Year | Work | What it shows | Grade |
|---|---|---|---|
| 12th c. | Orderic Vitalis | 1107 expedition the "third" | secondary |
| 1639 | Fuller, *Historie of the Holy Warre* | Thirteen numbered voyages, no "crusade" | full text |
| 1686 | Maimbourg, *Histoire des croisades*, pt. 2 | Henry VI "cette quatrième Croisade" | snippet |
| 1689 | Moréri, *Grand dictionnaire* | Eight numbered sections, "Huitième & dernière" | full text |
| 1701 | Basnage's Furetière | "On compte 8. Croisades" | full text |
| 1704 | Hübner, *Reales … Lexicon* | "Man zehlet acht Croiſaden"; no list | full text |
| 1728 | Chambers, *Cyclopaedia* | Trévoux's list in English | full text |
| 1771 | Koch, *Tableau des révolutions* | "On en compte proprement sept": the modern fourth to seventh | full text (OCR title page) |
| 1771 | Britannica 1st ed. | "They reckon eight croisades"; no list | full text |
| 1788 | Gibbon, ch. LIX | 1202 fourth, Damietta fifth, Louis sixth and seventh, Frederick unnumbered | full text |
| c. 1808 | Rees, *Cyclopaedia* | A nine with Frederick seventh | full text |
| 1820 | Mills, *History of the Crusades* | Henry VI fourth; Barons seventh; "the Last Crusade" | contents |
| 1820 | Desmichels and Trognon, *Tableau sommaire* | Official programme; Frederick-fifth seven | full text |
| 1821 | Règlement of 13 March; statute of 4 Sept. | Exam question table ordered; Middle Ages a separate year | full text |
| 21 Dec. 1822 | Desmichels, *Tableau chronologique* (dated 1823) | **Modern eight complete** | full text, title page viewed |
| 1824 | *Manuel complet des aspirans* (Delalain) | Desmichels's list copied | full text |
| 1824 | Courtin, *Encyclopédie moderne* | Moréri eight, "On compte communément huit croisades" | full text |
| 1826 | Hubert, exam question table | Q. 14 "Précis historique des croisades," no numbers | full text, image |
| 1827–35 | Desmichels, *Précis* (Colas; Colas and Hachette 1834; Brussels) | Modern eight | full text / snippet |
| 1829, 1835 | Delavigne, *Manuel complet* | Fifth and sixth for 1217–28; "les deux dernières" | full text |
| 1834 | Fiedler, *Tafeln* | First German Frederick-fifth seven found | full text |
| 1834, 1837 | Lefranc, *Histoire du moyen âge* | Henry VI fourth, eight | snippet / contents |
| 1835 | Lévi Alvarès | Seven; Frederick II refused as a crusade | snippet |
| 1836 | Bouchitté et al., *Manuel des aspirants* (Hachette) | Modern eight; footnote naming Desmichels | full text, image |
| 1838 | Furne, *Biographie universelle* | Moréri eight (last dictionary witness) | full text |
| 1841–42 | Ansart and Rendu, *Cours* (2nd ed.) | Modern eight, written to the official programme | snippet |
| 1842 | Bouillet; Le Bas; *Complément de l'Académie* | Modern eight in reference works; "l'usage le plus général" | full text, title pages |
| 1851 | Greene, *History and Geography of the Middle Ages* | First English modern eight (Rendu translated) | full text |
| 1851 | Cantù, *Storia universale* | Re-split to Bouillet's list | snippet |
| 1831 | Russell, *Palestine* (Edinburgh) | First ninth found: Tunis and Edward together | full text |
| 1857 | Masonic degree history (*Indian Freemason's Friend*) | Edward's crusade alone "the ninth crusade, A.D. 1272" | snippet |
| 1858 | Beale, *Student's Textbook*; White, *Eighteen Christian Centuries* (Edinburgh) | First British modern eights | full text |
| 1861 | Duruy, *Histoire du moyen âge* (Hachette) | Modern eight | full text |
| 1869 | Larousse, *Grand dictionnaire* | Its own eight (Andrew fourth) | full text |
| 1877 | Britannica 9th ed. (Cox) | Nine with Henry VI | full text |
| 1885 | Myers, *Outlines* | Modern eight; Henry VI would make nine | full text |
| 1893 | EETS *Godeffroy of Boloyne* (ed. Colvin) | "the prowesses of Prince Edward ... and of the events of the Ninth Crusade" | snippet |
| 1894 | Mombert, *A Short History* | The 2022 paper's answer | contents |
| 1898 | Oman, *Art of War* | Numbers only to the Fifth (read in the 1924 text) | full text |
| 1907 | Stevenson | The first complaint; numbers in quotation marks | contents |
| 1908 | Bréhier, *Catholic Encyclopedia* | Modern eight, "arbitrary"; source of Wikipedia's dates | full text |
| 1910 | Haydn's *Dictionary of Dates*, 25th ed. | Last edition; Henry VI fourth to the end | full text |
| 1911 | Barker, Britannica 11th ed. | Modern eight in English reference, to 1962; ends the Britannica's Henry VI fourth | full text |
| 1915 | Parker, *Bloody Trail of Romanism* | Last Henry VI fourth found | full text |
| 1920 | Parry, *The Pilgrim in Jerusalem* | "Ninth Crusade: Edward I of England" in a chronology | full text |
| 1940 | Langer, *Encyclopedia of World History* | Modern eight replaces Ploetz's seven | full text |
| 1953 | Encyclopedia Americana | German seven still printed | full text |
| 1965 | Mayer | "Lacks all consistency" | reasons table |
| 1979 | Scott-Giles, *The Wimsey Family* | Edward alone as "the Ninth Crusade" | snippet |
| 2001 | English Wikipedia, first surviving version | Bréhier's eight | API |
| 2019 | English Wikipedia | "Ninth Crusade" renamed | API |

## 11. Appendix B: where everything lives

| Item | Path |
|---|---|
| Master table and derived tables | `data/works.csv`, `data/numberings.csv`, `data/README.md` |
| Search log, reasons, citations | `data/search_log.csv`, `data/reasons/reasons.csv`, `data/citations.csv` |
| Frames and not-reached lists | `data/strand_a/`, `data/strand_b/`, `data/panel/` |
| Reconciliation reports | `data/reconciliation/` |
| Pre-merge tables | `data/archive/2026-11-28-pre-reconciliation/` |
| Wikipedia data | `data/wikipedia/` |
| Protocol, codebook, plan, logs | `docs/SEARCH_PROTOCOL.md`, `docs/CODEBOOK.md`, `docs/PLAN.md`, `docs/RESEARCH_LOG.md`, `docs/DECISIONS.md` |
| Findings notes | `notes/findings/` (review, second review, Strand A, decision point, browser pass, Strand D, conclusions audit, gaps pass, 1820–23 window, German snippet rows, reconciliation, answer books; four Wikipedia notes) |
| Visualizations | `site/` (ledger, Wikipedia timeline, scroll story) |
| The 2022 manuscript | Claude project only, not in the repository |
