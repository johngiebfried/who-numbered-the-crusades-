#!/usr/bin/env python3
"""Build the Wikipedia sub-project tables from the raw API pulls.

Inputs (data/wikipedia/raw/):
  snapshots_auto.csv  revision in force on 1 July of each year (plus 8 Nov 2026)
                      for the main article, navbox(es) and list article in
                      seven languages, with link-based and text-based codes
                      produced in the browser by the extraction routine
                      described in notes/findings/2026-11-wikipedia-numbering.md
  creation_auto.csv   first revision of each article and template

Outputs (data/wikipedia/):
  yearly_counts.csv, article_creation.csv, title_moves.csv,
  ordinal_titles_2026.csv, key_edits.csv, count_statements.csv
  and site/data/wikipedia_timeline.json for the chart.

Run from the repository root:  python3 scripts/build_wikipedia.py
"""
import csv, json, os, re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "wikipedia", "raw")
OUT = os.path.join(ROOT, "data", "wikipedia")
SITE = os.path.join(ROOT, "site", "data")
os.makedirs(SITE, exist_ok=True)
RETRIEVED = "2026-11-08"

LANGS = ["en", "de", "fr", "it", "es", "nl", "el", "ar", "fa", "he"]
LANG_NAME = {"en": "English", "de": "German", "fr": "French", "it": "Italian",
             "es": "Spanish", "nl": "Dutch", "el": "Greek",
             "ar": "Arabic", "fa": "Persian", "he": "Hebrew"}
PAGE_TITLE = {
    ("en", "main_article"): "Crusades", ("en", "navbox"): "Template:Campaignbox Crusades",
    ("en", "list_article"): "List of Crusades",
    ("de", "main_article"): "Kreuzzug", ("de", "navbox"): "Vorlage:Navigationsleiste Kreuzzüge",
    ("fr", "main_article"): "Croisade", ("fr", "navbox"): "Modèle:Palette Croisades",
    ("fr", "navbox_2"): "Modèle:Croisades",
    ("it", "main_article"): "Crociata", ("it", "navbox"): "Template:Campagnabox Crociate",
    ("es", "main_article"): "Cruzadas", ("es", "navbox"): "Plantilla:Campaña Cruzadas",
    ("nl", "main_article"): "Kruistocht", ("nl", "navbox"): "Sjabloon:Navigatie kruistochten",
    ("el", "main_article"): "Σταυροφορίες", ("el", "navbox"): "Πρότυπο:Σταυροφορίες",
    ("ar", "main_article"): "حملات صليبية", ("ar", "navbox"): "قالب:حملات صليبية",
    ("fa", "main_article"): "جنگ‌های صلیبی", ("fa", "navbox"): "الگو:جنگ‌های صلیبی",
    ("he", "main_article"): "מסעי הצלב", ("he", "navbox"): "תבנית:מסעי הצלב",
}
# STATEMENTS must be defined before build_yearly runs; it is, as a module-level list below.
# Article codes. Codes already in expeditions.csv: E1 E2 E3 H6 C CH D F B L1 L2 E.
# Proposed additions (see codebook note): PEO, C1101, ALX, NIC, VAR.
CODE_ORDER = ["PEO", "E1", "C1101", "E2", "E3", "H6", "C", "CH", "D", "D+F", "F", "B",
              "L1", "L1+L2", "L2", "L2+E", "E", "ALX", "NIC", "VAR"]
STANDARD = {1: "E1", 2: "E2", 3: "E3", 4: "C", 5: "D", 6: "F", 7: "L1", 8: "L2", 9: "E"}


def url(lang, revid):
    return f"https://{lang}.wikipedia.org/w/index.php?oldid={revid}"


def parse_linked(s):
    """'E1:1 C1101 D+F:5' -> OrderedDict(code -> set of ordinals)"""
    out = OrderedDict()
    for tok in (s or "").split():
        if ":" in tok:
            code, ords = tok.split(":", 1)
            out[code] = set(int(x) for x in ords.split("/"))
        else:
            out[tok] = set()
    return out


def expand_ords(s):
    nums = set()
    for part in (s or "").split():
        if "-" in part:
            a, b = part.split("-")
            nums.update(range(int(a), int(b) + 1))
        else:
            nums.add(int(part))
    return nums


# ---------------------------------------------------------------------------
# Hand-coded snapshot readings. Key: (language, page, first_sample, last_sample).
# Each gives the shorthand in project notation, a family and a note.
# These override the automatic coding where link targets or prose mislead it.
# ---------------------------------------------------------------------------
HAND = [
    ("de", "main_article", "2002-07-01", "2003-07-01",
     "E1 1, E2 2, E3 3, C 4, D 5, F 6", "partial",
     "Zeitleiste lists '1. Kreuzzug' to '6. Kreuzzug' with dates: 5 = 1217-18 (Damietta), "
     "6 = 1228 (Frederick II). Link targets were numeric titles that later became redirects, "
     "so the automatic link coding is wrong for these years."),
    ("de", "main_article", "2004-07-01", "2006-07-01",
     "E1 1, E2 2, E3 3, C 4, D (5), F 5 (6), L1 6 (7), L2 7 (8)", "german_seven_bracketed",
     "Double count introduced 27 Mar 2004 (rev 938521): '(Fünfter) Kreuzzug' 1217-21, "
     "'Fünfter (Sechster) Kreuzzug' 1228-29, 'Sechster (Siebter)', 'Siebter (Achter)'. "
     "Bracketed count removed 2 Apr 2007 (rev 30022882)."),
    ("de", "main_article", "2007-07-01", "2026-11-08",
     "E1 1, E2 2, E3 3, C 4, D+F 5, L1 6, L2 7", "german_seven",
     "Zeitleiste groups 'Kreuzzug von Damiette' and 'Kreuzzug Friedrichs II.' under one "
     "'Fünfter Kreuzzug'. From 2011 Prince Edward's crusade is a sub-item of the Siebter, "
     "and the 1239-41 expeditions (Theobald, Richard of Cornwall) appear as unnumbered "
     "entries from 2009."),
    ("de", "navbox", "2005-07-01", "2007-07-01",
     "E1 1, E2 2, E3 3, C 4, D 5 ('gescheitert'), F 5 (6), L1 6 (7), L2 7 (8)", "german_seven_bracketed",
     "Damietta labeled 'Gescheiterter fünfter Kreuzzug'; Frederick II 'Fünfter (Sechster) "
     "Kreuzzug'; Louis IX 'Sechster (Siebter)' and 'Siebter (Achter)'."),
    ("de", "navbox", "2008-07-01", "2026-11-08",
     "E1 1, E2 2, E3 3, C 4, D 5, F 5 (6), L1 6 (7), L2 7 (8)", "german_seven_bracketed",
     "'Fünfter Kreuzzug (Kreuzzug von Damiette)' and 'Fünfter (Sechster) Kreuzzug (Kreuzzug "
     "Friedrichs II.)'; Louis IX bracketed as in 2005. Barons' and Prince Edward unnumbered "
     "from 2011. Still the current text."),
    ("en", "main_article", "2002-07-01", "2002-07-01",
     "E1 1, E2 2, E3 3, C 4, D 5, F 6, L1 7, L2 8", "eight",
     "Single article before the October 2002 split; bold headings First to Eighth with "
     "dates (Fifth 1217, Sixth 1228-29, Seventh 1249-52, Eighth 1270). No Ninth."),
    ("en", "main_article", "2005-07-01", "2012-07-01", None, "nine",
     "Text ordinals reach 10 only through a 'See also' link to 'Tenth Crusade', an article "
     "on a modern polemical use of the phrase (later retitled '(CounterPunch)' and deleted); "
     "excluded from the count."),
    ("es", "main_article", "2003-07-01", "2003-07-01", "", "eight",
     "No list; lead says 'Hubo ocho cruzadas, más una posible cruzada de los niños'."),
    ("ar", "main_article", "2007-07-01", "2007-07-01", "", "partial",
     "Sample falls in a vandalized state: an anonymous edit of 28 May 2007 replaced the article; Uwe a restored it on 18 Jul 2007. The restored text counts eight."),
    ("fa", "navbox", "2016-07-01", "2017-07-01",
     "E1 1, E2 2, E3 3, C 4, D 5, F 6, L1 7, L2 8, E 9", "nine",
     "The Ninth slot links the English 'Ninth Crusade' article ([[:en:Ninth Crusade|نهم]]), so the automatic coding missed it."),
    ("el", "main_article", "2005-07-01", "2005-07-01",
     "E1 1, E2 2, E3 3, C 4, D 5, F 6, L1 7", "partial",
     "First version (Mar 2005) was a bare list of links Α΄ to Ζ΄."),
]


def hand_for(lang, page, date):
    for h in HAND:
        if h[0] == lang and h[1] == page and h[2] <= date <= h[3]:
            return h
    return None


STATEMENTS = [
    # language, page, first_sample, last_sample, first_revision, numbers, key_phrase, translation
    ("en", "main_article", "2005-07-01", "2012-07-01", "4842086", "9",
     "A traditional numbering scheme for the crusades gives us nine", ""),
    ("en", "main_article", "2011-07-01", "2012-07-01", "", "7-9",
     "The numbering of crusades is problematical.",
     "Goes on: Eighth sometimes the Seventh if Fifth and Sixth are merged; Ninth sometimes part of the Eighth."),
    ("en", "main_article", "2013-07-01", "2015-07-01", "561812444", "7",
     "There were seven major Crusades against Muslim territories in the east", ""),
    ("en", "main_article", "2016-07-01", "2016-07-01", "", "7+",
     "The numbering of the Crusades is debated", "Some historians count seven major crusades."),
    ("en", "main_article", "2021-07-01", "2023-07-01", "1030727666", "8",
     "eight major numbered crusades and dozens of minor crusades", ""),
    ("en", "main_article", "2026-07-01", "2026-11-08", "", "defers",
     "The List of Crusades delineates the numbered Crusades", "Footnote; no count given in the article."),
    ("en", "list_article", "2021-07-01", "2026-11-08", "", "8 or 9",
     "the numbered Crusades (First through Eighth or Ninth)", ""),
    ("de", "main_article", "2005-07-01", "2006-07-01", "", "5/6",
     "fünften (bzw. nach anderer Zählung sechsten) Kreuzzugs",
     "Of Frederick II: 'the fifth (or by another count the sixth) crusade'."),
    ("de", "main_article", "2007-07-01", "2026-11-08", "30022882", "7",
     "insgesamt sieben Kreuzzüge (Orientkreuzzüge) als offizielle Kreuzzüge",
     "'Historians count seven crusades in all (crusades to the East) as official crusades.' "
     "Since 2009: 'Die Zählung ist in der Fachliteratur nicht ganz einheitlich' (the count is not uniform in the literature)."),
    ("fr", "main_article", "2020-07-01", "2024-07-01", "", "8",
     "les sept principales croisades ultérieures, de 1147 à 1291",
     "'the seven main later crusades, 1147-1291' (after the First)."),
    ("fr", "main_article", "2021-07-01", "2021-07-01", "", "8",
     "On compte habituellement huit croisades", "'Eight crusades are usually counted.'"),
    ("fr", "main_article", "2022-07-01", "2025-07-01", "188892738", "9",
     "On compte habituellement neuf croisades", "'Nine crusades are usually counted.' Earliest confirmed revision 15 Dec 2021."),
    ("fr", "main_article", "2025-07-01", "2025-07-01", "", "9",
     "les huit principales croisades ultérieures", "'the eight main later crusades' (after the First)."),
    ("fr", "main_article", "2026-07-01", "2026-11-08", "231718978", "8 (9)",
     "au nombre de huit principales en Orient",
     "Eight main crusades in the East, 'sometimes extended to nine' with Edward I's expedition."),
    ("es", "main_article", "2003-07-01", "2003-07-01", "", "8",
     "Hubo ocho cruzadas, más una posible cruzada de los niños", "'There were eight crusades, plus a possible children's crusade.'"),
    ("es", "main_article", "2006-07-01", "2020-07-01", "", "8",
     "Hubo ocho cruzadas desde el siglo XI", "'There were eight crusades from the eleventh century...'"),
    ("es", "main_article", "2021-07-01", "2026-11-08", "129019369", "9",
     "Entre 1096 y 1272, se llevaron a cabo nueve cruzadas", "'Between 1096 and 1272 nine crusades were carried out.' Section 'Las nueve cruzadas'."),
    ("he", "navbox", "2009-07-01", "2026-11-08", "6937057", "9",
     "תשעת המסעות הגדולים", "Group heading: 'the nine great crusades' (unchanged since the box was created in May 2009)."),
    ("el", "main_article", "2015-07-01", "2026-11-08", "5292022", "8/9",
     "καταλήγοντας σε μια Θ΄ Σταυροφορία",
     "Translated from the English 'numbering is problematical' passage: merging Fifth and Sixth makes Louis IX's second the Eighth; splitting it yields a Ninth."),
]


def build_yearly():
    rows = []
    for fn in ("snapshots_auto.csv", "snapshots_auto_ar_fa_he.csv"):
        rows += list(csv.DictReader(open(os.path.join(RAW, fn), encoding="utf-8")))
    out = []
    for r in rows:
        lang, page, d = r["language"], r["page"], r["sample_date"]
        linked = parse_linked(r["linked_codes"])
        text_ords = expand_ords(r["ordinals_in_text"])
        h = hand_for(lang, page, d)
        if lang == "en" and page == "main_article" and "2005" <= d[:4] <= "2012":
            text_ords.discard(10)
        highest = max(text_ords) if text_ords else 0
        # ordinal -> code from links, filled from the standard sequence for ordinals
        # present in the text but not linked (all languages except German)
        ord_map = {}
        for code, ords in linked.items():
            for n in ords:
                ord_map.setdefault(n, code)
        source = "links"
        if lang != "de":
            # a linked article with no parsed label takes its standard number when that slot is empty
            top = max([highest] + list(ord_map.keys()) or [0])
            for n in range(1, min(top, 9) + 1):
                if n not in ord_map and STANDARD[n] in linked:
                    ord_map[n] = STANDARD[n]
                    source = "links+text"
            for n in sorted(text_ords):
                if n not in ord_map and n in STANDARD:
                    ord_map[n] = STANDARD[n]
                    source = "links+text"
        shorthand = ", ".join(f"{ord_map[n]} {n}" for n in sorted(ord_map) if n <= 9)
        unnumbered = [c for c, o in linked.items() if not o and c not in ("D+F",)
                      and c not in ord_map.values()]
        # family
        covered = set(n for n in ord_map if n <= 9)
        if covered >= set(range(1, 10)) and highest >= 9:
            family = "nine"
        elif covered >= set(range(1, 9)) and highest == 8:
            family = "eight"
        else:
            family = "partial"
        note = ""
        verification = "auto"
        if h:
            if h[4] is not None:
                shorthand = h[4]
                source = "hand"
            family = h[5]
            note = h[6]
            verification = "hand"
        if lang == "de" and not h:
            family = "german_seven"
        holder9 = ord_map.get(9, "") if family == "nine" else ""
        if family == "nine" and highest < 9:
            highest = 9  # hand-coded nine whose Ninth is an interwiki link (fa navbox 2016)
        if family == "eight" and highest == 0:
            highest = 8  # statement only (es 2003)
        stated = "; ".join(st[5] for st in STATEMENTS
                           if st[0] == lang and st[1] == page and st[2] <= d <= st[3])
        out.append(OrderedDict([
            ("language", lang), ("page", page), ("page_title", PAGE_TITLE[(lang, page)]),
            ("sample_date", d), ("revision_id", r["revision_id"]), ("revision_date", r["revision_date"]),
            ("bytes", r["bytes"]), ("highest_ordinal", 7 if family.startswith("german") else highest),
            ("count_family", family), ("stated_count", stated), ("numbering_shorthand", shorthand),
            ("ninth_is", holder9), ("unnumbered_linked", " ".join(unnumbered)),
            ("barons_named", r["barons_named"]), ("linked_codes_raw", r["linked_codes"]),
            ("ordinals_in_text_raw", r["ordinals_in_text"]), ("coding_source", source),
            ("verification", verification), ("notes", note), ("url", url(lang, r["revision_id"])),
        ]))
    return out


def build_creation():
    rows = []
    for fn in ("creation_auto.csv", "creation_auto_ar_fa_he.csv"):
        rows += list(csv.DictReader(open(os.path.join(RAW, fn), encoding="utf-8")))
    # first substantive revision where the first revision is junk, vandalism or a request
    substantive = {
        ("F", "en"): ("2003-04-30T22:24:13Z", "65.94.51.84", "First revision ('pie', 3 bytes) was a test edit."),
        ("L1", "en"): ("2003-11-27T00:08:07Z", "Adam Bishop", "First revision (Oct 2003) was a paste of URLs."),
        ("E", "el"): ("2019-02-12T17:46:57Z", "NikosLikomitros", "First revision was vandalism, replaced eleven minutes later."),
        ("CH", "de"): ("2003-11-07T09:39:45Z", "Benedikt~dewiki", "First revision was a pupil's request for information."),
        ("MAIN", "es"): ("2002-12-11T19:46:05Z", "AstroNomo", "First revision was a question, not an article."),
    }
    title_at_creation = {
        ("MAIN", "en"): "Crusade", ("MAIN", "fr"): "Croisades",
        ("E", "en"): "Ninth Crusade", ("H6", "en"): "Henry's crusade", ("B", "fr"): "Croisade de 1239",
        ("D", "de"): "(Fünfter) Kreuzzug", ("F", "de"): "Fünfter Kreuzzug", ("E", "de"): "Achter Kreuzzug",
        ("C1101", "fr"): "Croisade de 1101", ("H6", "it"): "Crusade of 1197",
        ("PEO", "it"): "Crociata dei pezzenti", ("TPL", "en"): "Template:Crusade",
        ("TPL", "de"): "Vorlage:Kreuzzüge", ("TPL", "fr"): "Modèle:NavigationCroisades",
        ("TPL", "es"): "Plantilla:Campaña de Cruzadas", ("NIC", "de"): "Schlacht von Nikopolis",
        ("NIC", "el"): "Μάχη της Νικόπολης", ("CH", "fr"): "Croisade des enfants",
    }
    greek_apostrophe = {"E1", "E2", "E3", "C", "D", "F", "L1", "L2"}
    notes = {
        ("MAIN", "en"): "Earliest preserved revision. Pre-2002 history was imported in 2010 (User:Graham87/Import) and may be incomplete; the first comment ('Move pope Innocent III to Fourth Crusade') implies earlier text. Titled 'Crusade' until 16 Sep 2006.",
        ("E1", "en"): "Split out of 'Crusade' by Andre Engels on 17 Oct 2002, with Second, Third and Fourth.",
        ("E2", "en"): "Split out of 'Crusade' on 17 Oct 2002.",
        ("E3", "en"): "Split out of 'Crusade' on 17 Oct 2002.",
        ("C", "en"): "Split out of 'Crusade' on 17 Oct 2002.",
        ("L2", "en"): "Created 17 Oct 2002 as a redirect to 'Crusade'; article from 4 Sep 2003.",
        ("E", "en"): "Created as 'Ninth Crusade' (Adam Bishop, 'the last crusade'). Moved to 'Lord Edward's crusade' 17 Nov 2019 after a requested move; moved back and forth on 18 Sep 2020.",
        ("B", "en"): "No earlier page, redirect or deletion under this title. 'Crusade of 1239' redirect created the same day; added to the navbox, unnumbered, one minute later.",
        ("B", "de"): "Created as a redirect to 'Kreuzzug Theobalds IV. von Champagne' (itself a redirect, 2009, to a section of 'Theobald I. (Navarra)'); article two days later.",
        ("B", "es"): "Created 2014 as a redirect to an unrelated Albigensian Crusade article; article from June 2018.",
        ("B", "fr"): "Created as 'Croisade de 1239'; moved to 'Croisade des barons' 30 Jun 2016 ('nom utilisé').",
        ("B", "it"): "Title 'Crociata del 1239'; the article's lead calls it 'crociata dei baroni'.",
        ("D", "de"): "Created as '(Fünfter) Kreuzzug'; moved to 'Kreuzzug von Damiette' 22 Feb 2007.",
        ("F", "de"): "Created as 'Fünfter Kreuzzug'; moved to 'Kreuzzug Friedrichs II.' 22 Feb 2007 after a Qualitätssicherung discussion of 19 Feb 2007. 'Fünfter Kreuzzug' then became a disambiguation page, and since 30 Sep 2017 a short page saying both are counted together as the Fifth.",
        ("L1", "de"): "Title 'Sechster Kreuzzug' = Louis IX's first crusade (German count).",
        ("L2", "de"): "Title 'Siebter Kreuzzug' = Tunis (German count).",
        ("E", "de"): "Created as 'Achter Kreuzzug' 29 Sep 2010; moved next day by Herrgott: 'Zählung als Achter Kreuzzug in der Literatur unüblich (eher 7. oder 9.)'.",
        ("D", "it"): "Began as a redirect to 'Sesta crociata' for sixteen minutes.",
        ("H6", "en"): "Created as 'Henry's crusade'; renamed the same day.",
        ("CH", "es"): "History merged from 'Cruzada infantil' in Dec 2006; the title was briefly misused for the People's Crusade in 2005.",
        ("E", "el"): "Lead calls it 'Ένατο Σταυροφορία' and says it is sometimes grouped with the Eighth (machine-translation style).",
        ("TPL", "en"): "Created as 'Template:Crusade'; renamed 31 Jul 2006.",
        ("TPL", "de"): "Created as 'Vorlage:Kreuzzüge'; renamed 7 Aug 2006.",
        ("VAR", "en"): "Began as a redirect to 'Battle of Varna'.",
        ("C1101", "en"): "Began as a redirect to 'First Crusade'.",
        ("MAIN", "ar"): "Uwe a created the main article, navbox and most numbered articles in 2004-05. Titles were indefinite ('حملة صليبية أولى') until moves to the definite form between 2008 and 2018.",
        ("E", "ar"): "Created by an anonymous editor (79.173.197.170), who added the Ninth to the main article the same day. A separate article 'الحملة الصليبية العاشرة' (2009) treats a 'Tenth Crusade' as a metaphor for the US-led war on terror.",
        ("TPL", "ar"): "Counted eight until a Ninth was added on 4 Dec 2013 (Zaher.Kadour, rev 12091964).",
        ("D", "fa"): "Fifth to Ninth created by one editor (کامران اورفه) between 11 and 15 Mar 2016; the navbox two days into that run.",
        ("E", "fa"): "Moved to 'جنگ صلیبی ادوارد یکم' (Edward I's crusade) on 11 Feb 2020 and back the next day by the same editor (ImanFakhri), three months after the English rename.",
        ("TPL", "fa"): "The Ninth slot linked the English article until a Persian link replaced it (by mid-2018).",
        ("B", "he"): "Redirect from 2014; article from 28 Dec 2025, added to the navbox the same day.",
        ("E", "he"): "Hebrew had a Ninth Crusade article (2010) five years before an Eighth (2015).",
        ("TPL", "he"): "Created May 2009 with the heading 'תשעת המסעות הגדולים' (the nine great crusades), still current.",
        ("MAIN", "he"): "Organized by theme, not by numbered crusade; links First to Sixth only since 2013.",
    }
    out = []
    for r in rows:
        key = (r["article_code"], r["language"])
        sub = substantive.get(key)
        first_article = sub[0] if sub else r["first_non_redirect_utc"]
        first_article_user = sub[1] if sub else r["first_non_redirect_user"]
        began = "redirect" if r["began_as_redirect"] == "1" else ("junk" if sub else "article")
        tac = title_at_creation.get(key, "")
        if not tac and r["language"] == "el" and r["article_code"] in greek_apostrophe:
            tac = r["current_title"].replace("΄", "'")
        n = notes.get(key, "")
        if sub:
            n = (sub[2] + " " + n).strip()
        out.append(OrderedDict([
            ("article_code", r["article_code"]), ("language", r["language"]),
            ("current_title", r["current_title"]), ("title_at_creation", tac or r["current_title"]),
            ("page_id", r["page_id"]), ("first_revision_utc", r["first_revision_utc"]),
            ("first_revision_user", r["first_revision_user"]), ("first_revision_bytes", r["first_revision_bytes"]),
            ("began_as", began), ("first_article_utc", first_article),
            ("first_article_user", first_article_user), ("first_article_year", first_article[:4]),
            ("revisions_at_retrieval", r["revisions"]), ("retrieved", RETRIEVED), ("notes", n),
        ]))
    return out


MOVES = [
    # date, language, code, from, to, user, kind, reason (short; original language)
    ("2006-09-16", "en", "MAIN", "Crusade", "Crusades", "", "rename_other", "per RQM"),
    ("2021-02-26", "fr", "MAIN", "Croisades", "Croisade", "TED", "rename_other", "naming conventions (singular)"),
    ("2007-02-22", "de", "D", "(Fünfter) Kreuzzug", "Kreuzzug von Damiette", "Finanzer", "rename_numbering", "etwas im Bereich Fünfter Kreuzzug aufräumen"),
    ("2007-02-22", "de", "F", "Fünfter Kreuzzug", "Kreuzzug Friedrichs II.", "Frank Schulenburg", "rename_numbering", "siehe QS Geschichte vom 19. Februar 2007"),
    ("2010-09-30", "de", "E", "Achter Kreuzzug", "Kreuzzug des Prinzen Eduard", "Herrgott", "rename_numbering", "Zählung als Achter Kreuzzug in der Literatur unüblich (eher 7. oder 9.)"),
    ("2019-11-17", "en", "E", "Ninth Crusade", "Lord Edward's crusade", "DannyS712", "rename_numbering", "requested move (Srnec, 8 Nov 2019); no objections"),
    ("2020-09-18", "en", "E", "Lord Edward's crusade", "Ninth Crusade", "Johnbod", "rename_numbering", "restore old title; asks for a proper RM"),
    ("2020-09-18", "en", "E", "Ninth Crusade", "Lord Edward's crusade", "Srnec", "rename_numbering", "there was an RM"),
    ("2016-06-30", "fr", "B", "Croisade de 1239", "Croisade des barons", "Io Herodotus", "rename_other", "nom utilisé"),
    ("2007-09-13", "en", "H6", "Henry's crusade", "Crusade of 1197", "Adam Bishop", "rename_other", "better title"),
    ("2020-01-12", "it", "H6", "Crusade of 1197", "Crociata del 1197", "Enzo Encius", "rename_other", "translated title"),
    ("2010-10-07", "fr", "C1101", "Croisade de 1101", "Croisades de secours", "", "rename_other", "Titre plus pertinent"),
    ("2008-01-28", "it", "PEO", "Crociata dei pezzenti", "Crociata dei poveri", "", "rename_other", ""),
    ("2010-07-20", "fr", "CH", "Croisade des enfants", "Croisade des enfants (expédition)", "", "rename_other", "homonymie (via '(Moyen-Âge)')"),
    ("2025-04-23", "fr", "CH", "Croisade des enfants (expédition)", "Croisade des enfants", "Ælfgar", "rename_other", "primary topic"),
    ("2017-03-29", "de", "NIC", "Schlacht bei Nikopol (1396)", "Schlacht bei Nikopolis", "Hans-Jürgen Hübner", "rename_other", "in der Literatur deutlich gängiger"),
    ("2006-07-31", "en", "TPL", "Template:Crusade", "Template:Campaignbox Crusades", "", "rename_other", "Standard naming scheme"),
    ("2006-08-07", "de", "TPL", "Vorlage:Kreuzzüge", "Vorlage:Navigationsleiste Kreuzzüge", "", "rename_other", ""),
    ("2013-03-24", "fr", "TPL", "Modèle:NavigationCroisades", "Modèle:Palette Croisades", "Moumou82", "rename_other", "two moves the same day"),
    ("2014-06-29", "es", "TPL", "Plantilla:Campaña de Cruzadas", "Plantilla:Campaña Cruzadas", "Juan Mayordomo", "rename_other", ""),
    ("2020-02-11", "fa", "E", "جنگ صلیبی نهم", "جنگ صلیبی ادوارد یکم", "ImanFakhri", "rename_numbering", "اصلاح عنوان (title correction)"),
    ("2020-02-12", "fa", "E", "جنگ صلیبی ادوارد یکم", "جنگ صلیبی نهم", "ImanFakhri", "rename_numbering", "reverted the next day"),
    ("2012-02-18", "ar", "E", "حملة صليبية تاسعة", "الحملة الصليبية التاسعة", "", "rename_other", "indefinite to definite title; same pattern for First to Eighth, 2008-2018"),
    ("2025-01-23", "fa", "B", "جنگ صلیبی بارونی", "جنگ صلیبی بارون‌ها", "ImanFakhri", "rename_other", "اصلاح عنوان"),
    ("2022-10-19", "ar", "B", "الحملة البارونات الصليبية", "الحملة الصليبية البارونية", "", "rename_other", "تعديل الاسم"),
    ("2017-11-25", "es", "E1", "Primera Cruzada", "Primera cruzada", "Technopat", "capitalization", ""),
    ("2018-01-28", "es", "E3", "Tercera Cruzada", "Tercera cruzada", "Technopat", "capitalization", ""),
    ("2018-01-28", "es", "C", "Cuarta Cruzada", "Cuarta cruzada", "Technopat", "capitalization", ""),
    ("2018-01-28", "es", "D", "Quinta Cruzada", "Quinta cruzada", "Technopat", "capitalization", ""),
    ("2018-07-30", "es", "E2", "Segunda Cruzada", "Segunda cruzada", "Jarould", "capitalization", ""),
    ("2018-07-30", "es", "F", "Sexta Cruzada", "Sexta cruzada", "Jarould", "capitalization", ""),
    ("2018-07-30", "es", "L1", "Séptima Cruzada", "Séptima cruzada", "Jarould", "capitalization", ""),
    ("2018-07-30", "es", "L2", "Octava Cruzada", "Octava cruzada", "Jarould", "capitalization", ""),
    ("2018-07-30", "es", "E", "Novena Cruzada", "Novena cruzada", "Jarould", "capitalization", ""),
    ("2012-07-16", "el", "E1", "Α' Σταυροφορία", "Α΄ Σταυροφορία", "Chrysalifourfour", "numeral_form", "ορθή απόδοση ελληνικών αριθμητικών"),
    ("2012-07-17", "el", "E2", "Β' Σταυροφορία", "Β΄ Σταυροφορία", "Chrysalifourfour", "numeral_form", "ορθή γραφή ελληνικών αριθμητικών"),
    ("2012-07-28", "el", "E3", "Γ' Σταυροφορία", "Γ΄ Σταυροφορία", "Chrysalifourfour", "numeral_form", ""),
    ("2014-10-11", "el", "C", "Δ' Σταυροφορία", "Δ΄ Σταυροφορία", "FocalPoint", "numeral_form", "reversed and restored Aug 2024"),
    ("2012-07-18", "el", "D", "Ε' Σταυροφορία", "Ε΄ Σταυροφορία", "Chrysalifourfour", "numeral_form", ""),
    ("2012-07-28", "el", "F", "ΣΤ' Σταυροφορία", "ΣΤ΄ Σταυροφορία", "Ογκόλιθος", "numeral_form", ""),
    ("2012-07-28", "el", "L1", "Ζ' Σταυροφορία", "Ζ΄ Σταυροφορία", "Chrysalifourfour", "numeral_form", ""),
    ("2012-07-21", "el", "L2", "Η' Σταυροφορία", "Η΄ Σταυροφορία", "Chrysalifourfour", "numeral_form", ""),
]

ORDINAL_TITLES = [
    # language, ordinal, title, status_2026, target, expedition, first_revision, first_content_note
    ("en", 1, "First Crusade", "article", "", "E1", "2002-10-17", ""),
    ("en", 2, "Second Crusade", "article", "", "E2", "2002-10-17", ""),
    ("en", 3, "Third Crusade", "article", "", "E3", "2002-10-17", ""),
    ("en", 4, "Fourth Crusade", "article", "", "C", "2002-10-17", ""),
    ("en", 5, "Fifth Crusade", "article", "", "D", "2003-09-03", ""),
    ("en", 6, "Sixth Crusade", "article", "", "F", "2002-06-27", "first real text 2003-04-30"),
    ("en", 7, "Seventh Crusade", "article", "", "L1", "2003-10-02", "first real text 2003-11-27"),
    ("en", 8, "Eighth Crusade", "article", "", "L2", "2002-10-17", "redirect to 'Crusade' until 2003-09-04"),
    ("en", 9, "Ninth Crusade", "redirect", "Lord Edward's crusade", "E", "2004-05-04", "article title until 2019-11-17"),
    ("en", 10, "Tenth Crusade", "missing", "", "", "", "deleted 2015 and 2022; was about a modern polemical usage"),
    ("de", 1, "Erster Kreuzzug", "article", "", "E1", "2003-11-19", ""),
    ("de", 2, "Zweiter Kreuzzug", "article", "", "E2", "2004-01-29", ""),
    ("de", 3, "Dritter Kreuzzug", "article", "", "E3", "2003-08-31", ""),
    ("de", 4, "Vierter Kreuzzug", "article", "", "C", "2003-12-19", ""),
    ("de", 5, "Fünfter Kreuzzug", "short_page", "", "D+F", "2004-02-08", "Frederick II article 2004-07; disambiguation 2007-17; since 2017 says D and F are counted together"),
    ("de", 6, "Sechster Kreuzzug", "article", "", "L1", "2004-04-24", ""),
    ("de", 7, "Siebter Kreuzzug", "article", "", "L2", "2004-04-24", ""),
    ("de", 8, "Achter Kreuzzug", "redirect", "Siebter Kreuzzug", "L2", "2010-09-29", "was the Prince Edward article for one day; redirect to Tunis since 2010-10-01"),
    ("de", 9, "Neunter Kreuzzug", "redirect", "Kreuzzug des Prinzen Eduard", "E", "2010-09-30", ""),
    ("de", 10, "Zehnter Kreuzzug", "missing", "", "", "", ""),
    ("fr", 1, "Première croisade", "article", "", "E1", "2004-06-03", ""),
    ("fr", 2, "Deuxième croisade", "article", "", "E2", "2004-05-27", ""),
    ("fr", 3, "Troisième croisade", "article", "", "E3", "2004-05-27", ""),
    ("fr", 4, "Quatrième croisade", "article", "", "C", "2004-11-15", ""),
    ("fr", 5, "Cinquième croisade", "article", "", "D", "2004-11-28", ""),
    ("fr", 6, "Sixième croisade", "article", "", "F", "2004-11-24", ""),
    ("fr", 7, "Septième croisade", "article", "", "L1", "2004-11-29", ""),
    ("fr", 8, "Huitième croisade", "article", "", "L2", "2004-11-06", ""),
    ("fr", 9, "Neuvième croisade", "article", "", "E", "2004-12-03", ""),
    ("fr", 10, "Dixième croisade", "missing", "", "", "", ""),
    ("it", 1, "Prima crociata", "article", "", "E1", "2004-12-01", ""),
    ("it", 2, "Seconda crociata", "article", "", "E2", "2005-06-27", ""),
    ("it", 3, "Terza crociata", "article", "", "E3", "2005-12-29", ""),
    ("it", 4, "Quarta crociata", "article", "", "C", "2005-05-31", ""),
    ("it", 5, "Quinta crociata", "article", "", "D", "2006-03-13", "redirect to 'Sesta crociata' for sixteen minutes"),
    ("it", 6, "Sesta crociata", "article", "", "F", "2005-11-22", ""),
    ("it", 7, "Settima crociata", "article", "", "L1", "2006-12-29", ""),
    ("it", 8, "Ottava crociata", "article", "", "L2", "2007-03-20", ""),
    ("it", 9, "Nona crociata", "article", "", "E", "2005-12-29", ""),
    ("it", 10, "Decima crociata", "missing", "", "", "", ""),
    ("es", 1, "Primera cruzada", "article", "", "E1", "2004-04-05", ""),
    ("es", 2, "Segunda cruzada", "article", "", "E2", "2006-02-03", ""),
    ("es", 3, "Tercera cruzada", "article", "", "E3", "2006-02-05", ""),
    ("es", 4, "Cuarta cruzada", "article", "", "C", "2006-02-09", ""),
    ("es", 5, "Quinta cruzada", "article", "", "D", "2006-10-23", ""),
    ("es", 6, "Sexta cruzada", "article", "", "F", "2006-10-25", ""),
    ("es", 7, "Séptima cruzada", "article", "", "L1", "2006-11-14", ""),
    ("es", 8, "Octava cruzada", "article", "", "L2", "2006-12-07", ""),
    ("es", 9, "Novena cruzada", "article", "", "E", "2006-12-07", ""),
    ("es", 10, "Décima cruzada", "redirect", "Cruzada de Alejandría", "ALX", "2018-09-13", "Alexandria 1365 as a Tenth Crusade"),
    ("nl", 1, "Eerste Kruistocht", "article", "", "E1", "2004-03-08", ""),
    ("nl", 2, "Tweede Kruistocht", "article", "", "E2", "2003-07-19", ""),
    ("nl", 3, "Derde Kruistocht", "article", "", "E3", "2004-07-28", ""),
    ("nl", 4, "Vierde Kruistocht", "article", "", "C", "2004-07-28", ""),
    ("nl", 5, "Vijfde Kruistocht", "article", "", "D", "2005-04-09", ""),
    ("nl", 6, "Zesde Kruistocht", "article", "", "F", "2003-08-22", ""),
    ("nl", 7, "Zevende Kruistocht", "article", "", "L1", "2005-03-12", ""),
    ("nl", 8, "Achtste Kruistocht", "article", "", "L2", "2005-08-04", ""),
    ("nl", 9, "Negende Kruistocht", "article", "", "E", "2005-04-11", ""),
    ("nl", 10, "Tiende Kruistocht", "missing", "", "", "", ""),
    ("el", 1, "Α΄ Σταυροφορία", "article", "", "E1", "2005-05-25", "word form 'Πρώτη Σταυροφορία' a redirect since 2007-05-13"),
    ("el", 2, "Β΄ Σταυροφορία", "article", "", "E2", "2005-08-20", ""),
    ("el", 3, "Γ΄ Σταυροφορία", "article", "", "E3", "2005-09-08", ""),
    ("el", 4, "Δ΄ Σταυροφορία", "article", "", "C", "2006-05-07", ""),
    ("el", 5, "Ε΄ Σταυροφορία", "article", "", "D", "2006-11-21", ""),
    ("el", 6, "ΣΤ΄ Σταυροφορία", "article", "", "F", "2006-11-21", ""),
    ("el", 7, "Ζ΄ Σταυροφορία", "article", "", "L1", "2006-11-21", "word forms for 1-7 are redirects (2007); none for 8-10"),
    ("el", 8, "Η΄ Σταυροφορία", "article", "", "L2", "2007-07-23", ""),
    ("el", 9, "Θ΄ Σταυροφορία", "article", "", "E", "2019-02-12", "no Greek article on Edward's crusade before 2019"),
    ("el", 10, "Ι΄ Σταυροφορία", "missing", "", "", "", ""),
    ("ar", 1, "الحملة الصليبية الأولى", "article", "", "E1", "2006-01-11", ""),
    ("ar", 2, "الحملة الصليبية الثانية", "article", "", "E2", "2005-07-07", ""),
    ("ar", 3, "الحملة الصليبية الثالثة", "article", "", "E3", "2004-09-28", ""),
    ("ar", 4, "الحملة الصليبية الرابعة", "article", "", "C", "2004-09-29", ""),
    ("ar", 5, "الحملة الصليبية الخامسة", "article", "", "D", "2004-09-25", ""),
    ("ar", 6, "الحملة الصليبية السادسة", "article", "", "F", "2004-10-05", ""),
    ("ar", 7, "الحملة الصليبية السابعة", "article", "", "L1", "2004-09-28", ""),
    ("ar", 8, "الحملة الصليبية الثامنة", "article", "", "L2", "2005-09-25", ""),
    ("ar", 9, "الحملة الصليبية التاسعة", "article", "", "E", "2010-10-30", ""),
    ("fa", 1, "نخستین جنگ صلیبی", "article", "", "E1", "2013-05-27", "'جنگ صلیبی اول' redirects here"),
    ("fa", 2, "جنگ صلیبی دوم", "article", "", "E2", "2013-01-31", ""),
    ("fa", 3, "جنگ صلیبی سوم", "article", "", "E3", "2009-07-20", ""),
    ("fa", 4, "جنگ صلیبی چهارم", "article", "", "C", "2014-03-04", ""),
    ("fa", 5, "جنگ صلیبی پنجم", "article", "", "D", "2016-03-13", ""),
    ("fa", 6, "جنگ صلیبی ششم", "article", "", "F", "2016-03-12", ""),
    ("fa", 7, "جنگ صلیبی هفتم", "article", "", "L1", "2016-03-11", ""),
    ("fa", 8, "جنگ صلیبی هشتم", "article", "", "L2", "2016-03-13", ""),
    ("fa", 9, "جنگ صلیبی نهم", "article", "", "E", "2016-03-15", ""),
    ("he", 1, "מסע הצלב הראשון", "article", "", "E1", "2004-09-07", ""),
    ("he", 2, "מסע הצלב השני", "article", "", "E2", "2005-03-27", ""),
    ("he", 3, "מסע הצלב השלישי", "article", "", "E3", "2004-12-14", ""),
    ("he", 4, "מסע הצלב הרביעי", "article", "", "C", "2007-02-11", ""),
    ("he", 5, "מסע הצלב החמישי", "article", "", "D", "2008-02-29", ""),
    ("he", 6, "מסע הצלב השישי", "article", "", "F", "2009-04-24", ""),
    ("he", 7, "מסע הצלב השביעי", "article", "", "L1", "2008-05-28", ""),
    ("he", 8, "מסע הצלב השמיני", "article", "", "L2", "2015-11-16", ""),
    ("he", 9, "מסע הצלב התשיעי", "article", "", "E", "2010-02-11", ""),
    ("ar", 10, "الحملة الصليبية العاشرة", "redirect", "حملة صليبية عاشرة", "", "2011-05-04", "target is a 2009 article on the phrase as a metaphor for the war on terror"),
    ("fa", 10, "جنگ صلیبی دهم", "missing", "", "", "", ""),
    ("he", 10, "מסע הצלב העשירי", "missing", "", "", "", ""),
]

KEY_EDITS = [
    # date, language, page, revision_id, user, change
    ("2002-10-17", "en", "Crusade", "", "Andre Engels", "Splits First to Fourth Crusade out of the single 'Crusade' article; 'Eighth Crusade' created as a redirect. The article then counts eight."),
    ("2003-04-13", "en", "Crusade", "1093670", "Jeronimo", "First revision of the main article with a 'Ninth Crusade' heading (binary search between July 2002 and July 2003)."),
    ("2003-05-21", "nl", "Kruistocht", "44312", "Andre Engels", "Adds 'Achtste Kruistocht (1270)' and 'Negende Kruistocht (1271-1272)' sections, five weeks after the English article gained its Ninth. The same editor had split the English article in October 2002."),
    ("2004-03-27", "de", "Kreuzzug", "938521", "Hubert22", "Zeitleiste introduces the double count: '(Fünfter) Kreuzzug' for Damietta, 'Fünfter (Sechster)' for Frederick II, 'Sechster (Siebter)', 'Siebter (Achter)'."),
    ("2004-04-02", "en", "Template:Crusade", "", "Itai", "Navigation box created, First to Ninth."),
    ("2004-05-04", "en", "Ninth Crusade", "", "Adam Bishop", "Article 'Ninth Crusade' created ('the last crusade')."),
    ("2004-07-25", "en", "Crusade", "4842086", "Adam Bishop", "Adds 'A traditional numbering scheme for the crusades gives us nine'."),
    ("2005-05-05", "de", "Vorlage:Kreuzzüge", "", "Bender235", "German navbox created with the double count and Damietta as 'Gescheiterter fünfter Kreuzzug'."),
    ("2007-02-22", "de", "Fünfter Kreuzzug", "", "Frank Schulenburg; Finanzer", "Frederick II's article moved off 'Fünfter Kreuzzug'; Damietta's off '(Fünfter) Kreuzzug'. 'Fünfter Kreuzzug' becomes a disambiguation page."),
    ("2007-04-02", "de", "Kreuzzug", "30022882", "Rolz Reus", "Bracketed count removed ('Klammerzählweise rausgeholt'); adds 'insgesamt sieben Kreuzzüge ... als offizielle Kreuzzüge'. Damietta and Frederick II grouped under one Fifth."),
    ("2008-03-31", "en", "Talk:Ninth Crusade", "", "Secisek", "Talk page: proposes merging with the Eighth and asks what English source lists it as ninth."),
    ("2008-08-20", "fr", "Croisade de 1239", "", "Odejea", "First Wikipedia article on the Barons' Crusade in these seven languages."),
    ("2010-09-29", "de", "Diskussion:Kreuzzug des Prinzen Eduard", "", "Herrgott", "Proposes Damietta as Fifth, Frederick II Sixth, Louis IX Seventh and Eighth, Edward Ninth, calling it the 'englische' count; title moved to 'Kreuzzug des Prinzen Eduard' the next day."),
    ("2010-10-02", "de", "Kreuzzug der Barone", "", "Johnny47", "German article on the Barons' Crusade."),
    ("2013-05-01", "en", "Crusades", "553107724", "Ealdgyth", "First revision of the English main article to name the 1239 crusade (Theobald I of Navarre), as a follow-up to the Sixth."),
    ("2013-06-27", "en", "Crusades", "561812444", "Norfolkbigfish", "Lead now says 'seven major Crusades' while the body still numbers to nine."),
    ("2016-02-12", "en", "Barons' Crusade", "704652276", "Blue Danube", "English article on the Barons' Crusade created; added to the navbox, unnumbered, one minute later (rev 704652443)."),
    ("2016-06-30", "fr", "Croisade des barons", "", "Io Herodotus", "French article renamed from 'Croisade de 1239' to 'Croisade des barons'."),
    ("2017-09-30", "de", "Fünfter Kreuzzug", "", "Michileo", "Disambiguation turned into a short page: Damietta and Frederick II are counted together as the Fifth; another count makes them Fifth and Sixth."),
    ("2018-09-13", "es", "Décima cruzada", "", "", "Redirect 'Décima cruzada' to the Alexandrian Crusade of 1365."),
    ("2019-11-17", "en", "Ninth Crusade", "", "DannyS712", "Moved to 'Lord Edward's crusade' after Srnec's requested move of 8 Nov 2019 drew no objections."),
    ("2019-11-17", "en", "Template:Campaignbox Crusades", "926657250", "Srnec", "Navbox drops 'Ninth'; Lord Edward listed unnumbered. The English navbox counts eight from here."),
    ("2020-09-04", "es", "Cruzadas", "129019369", "Tintero21", "Spanish main article moves from eight to nine ('Las nueve cruzadas')."),
    ("2020-09-18", "en", "Lord Edward's crusade", "", "Johnbod; Srnec", "Moved back to 'Ninth Crusade' and returned the same day."),
    ("2020-12-09", "en", "List of Crusades", "", "Dr. Grampinator", "List article created (as 'List of Crusades to Europe and the Holy Land')."),
    ("2021-06-27", "en", "Crusades", "1030727666", "Dr. Grampinator", "Lead: 'eight major numbered crusades'."),
    ("2021-12-15", "fr", "Croisade", "188892738", "Sebleouf", "Earliest confirmed revision with 'On compte habituellement neuf croisades' (restores an earlier version by MarkHunt)."),
    ("2021-12-22", "en", "Crusades", "1061598911", "Dr. Grampinator", "Last 'Ninth Crusade' removed from the English main article."),
    ("2022-09-13", "it", "Crociata del 1239", "", "Fabio Daziano", "Italian article on the Barons' Crusade."),
    ("2023-09-15", "nl", "Baronnenkruistocht", "", "Xaviervd", "Dutch article on the Barons' Crusade."),
    ("2025-12-23", "fr", "Croisade", "231718978", "N0osphR", "Lead rewritten: eight main crusades, 'sometimes extended to nine' with Edward I."),
    ("2026-03-15", "el", "Σταυροφορία των Βαρόνων", "", "ArisMethymna", "Greek article on the Barons' Crusade."),
    ("2004-09-28", "ar", "قالب:حملات صليبية", "", "Uwe a", "Arabic navbox created with eight; Uwe a builds the main article and most numbered articles in 2004-05."),
    ("2009-05-12", "he", "תבנית:מסעי הצלב", "", "Ori", "Hebrew navbox created under the heading 'the nine great crusades'."),
    ("2009-08-16", "ar", "حملة صليبية عاشرة", "", "محمد أحمد عبد الفتاح", "Arabic article on 'the Tenth Crusade' as a metaphor for the US-led war on terror; still live."),
    ("2010-02-11", "he", "מסע הצלב התשיעי", "", "Infidel", "Hebrew Ninth Crusade article, five years before an Eighth."),
    ("2010-10-30", "ar", "حملات صليبية", "5949534", "79.173.197.170", "Arabic main article gains a Ninth the same day the same editor creates the Ninth Crusade article."),
    ("2013-12-04", "ar", "قالب:حملات صليبية", "12091964", "Zaher.Kadour", "Arabic navbox moves from eight to nine."),
    ("2016-03-13", "fa", "الگو:جنگ‌های صلیبی", "", "طاها", "Persian navbox created, its Ninth linked to the English article; Fifth to Ninth articles created 11-15 Mar 2016."),
    ("2019-03-12", "fa", "جنگ صلیبی بارونی", "", "ImanFakhri", "Persian article on the Barons' Crusade."),
    ("2019-07-13", "ar", "الحملة البارونات الصليبية", "", "Dall2611", "Arabic article on the Barons' Crusade."),
    ("2020-02-11", "fa", "جنگ صلیبی نهم", "", "ImanFakhri", "Persian Ninth renamed 'Edward I's crusade', following the English move, and restored the next day."),
    ("2025-12-28", "he", "מסע הצלב של הברונים", "", "שביל הזהב", "Hebrew article on the Barons' Crusade, after eleven years as a redirect."),
]


def write_csv(path, rows, header=None):
    with open(path, "w", newline="", encoding="utf-8") as f:
        if header is None:
            header = list(rows[0].keys())
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(list(r.values()) if isinstance(r, dict) else list(r))


def main():
    KEY_EDITS.sort(key=lambda k: k[0])
    yearly = build_yearly()
    write_csv(os.path.join(OUT, "yearly_counts.csv"), yearly)
    creation = build_creation()
    write_csv(os.path.join(OUT, "article_creation.csv"), creation)
    write_csv(os.path.join(OUT, "title_moves.csv"), MOVES,
              ["date", "language", "article_code", "from_title", "to_title", "user", "kind", "reason"])
    write_csv(os.path.join(OUT, "ordinal_titles_2026.csv"), ORDINAL_TITLES,
              ["language", "ordinal", "title", "status", "redirect_target", "expedition_id", "first_revision", "notes"])
    write_csv(os.path.join(OUT, "key_edits.csv"),
              [list(k) + [url(k[1], k[3]) if k[3] else ""] for k in KEY_EDITS],
              ["date", "language", "page", "revision_id", "user", "change", "url"])
    write_csv(os.path.join(OUT, "count_statements.csv"),
              [list(s) + [url(s[0], s[4]) if s[4] else ""] for s in STATEMENTS],
              ["language", "page", "first_sample", "last_sample", "first_revision_id", "count",
               "key_phrase", "gloss", "url"])

    # chart data
    lanes = []
    for lang in LANGS:
        for page in ("main_article", "list_article", "navbox", "navbox_2"):
            pts = [r for r in yearly if r["language"] == lang and r["page"] == page]
            if not pts:
                continue
            lanes.append({
                "language": lang, "language_name": LANG_NAME[lang], "page": page,
                "title": PAGE_TITLE[(lang, page)],
                "points": [{
                    "date": r["sample_date"], "family": r["count_family"], "highest": r["highest_ordinal"],
                    "shorthand": r["numbering_shorthand"], "barons": r["barons_named"] == "1",
                    "stated": r["stated_count"],
                    "revid": r["revision_id"], "url": r["url"], "note": r["notes"],
                } for r in pts]})
    barons = {c["language"]: c["first_article_utc"][:10] for c in creation if c["article_code"] == "B"}
    events = [{"date": k[0], "language": k[1], "page": k[2], "change": k[5]} for k in KEY_EDITS]
    statements = [{"language": s[0], "page": s[1], "from": s[2], "to": s[3], "count": s[5],
                   "phrase": s[6], "gloss": s[7]} for s in STATEMENTS]
    json.dump({"retrieved": RETRIEVED, "lanes": lanes, "barons_article": barons,
               "events": events, "statements": statements},
              open(os.path.join(SITE, "wikipedia_timeline.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("yearly", len(yearly), "creation", len(creation), "moves", len(MOVES),
          "ordinals", len(ORDINAL_TITLES), "edits", len(KEY_EDITS), "statements", len(STATEMENTS))


if __name__ == "__main__":
    main()
