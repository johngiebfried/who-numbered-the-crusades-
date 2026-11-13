# Strand A gaps and the bracket check (task 3)

13 November 2026. Rows: `entries.csv` (4 new, all `strand_a_fr_en`). Shell had no internet; WebSearch and WebFetch only. No browser, so page images could not be viewed.

## Result

The 1838–42 bracket survives every item that could be reached, but two of the unread works (items 1 and 2) are still unread, so it is not closed. The one new reference work dated inside the window, Britannica 7th edition (1842), has the Moréri eight: fourth Henry VI 1195, fifth Innocent III 1198, sixth 1228 with Damietta, seventh Louis 1249, eighth 1270. The Britannica series 1771–1854 (1st to 8th) now has no modern eight. No title-page check succeeded.

## The nine items

| # | Item | Answer | Evidence |
|---|---|---|---|
| 1 | Gens du monde t. 7 (1836), CROISADES | Not reachable | Volume is catalogued (BSB Munich, Enc. 58 d-7, 800 pp.; urn:nbn:de:bvb:12-bsb10401033-5). The MDZ resolver returned a fetch-approval error, so not retried. Gallica surfaced t. 6.1 (CHR-COM) only, and that fetch failed. Scheme not coded. |
| 2 | d'Harmonville (1842–45), CROISADES | Not reachable | Three searches; no scan or snippet surfaced. Scheme not coded. |
| 3 | Britannica 7th (1842); 4th–6th | Yes | EB7 vol. 7, CRUSADES: "The fifth crusade was proclaimed by order of Pope Innocent III. in 1198." Moréri eight, no stated total. EB4 (1810), EB5 (1815), EB6 (1823), CROISADE: same scheme; stated total "eight different croisades were set on foot". Read on jimclifford.ca transcriptions; year from site metadata, not title pages. Site gives EB4–6 all as vol. 6 p. 762, which looks like a copied pagination. |
| 4 | Title pages, Courtin t. 7 and Furne | Not reachable | No Google Books URL for either id appeared in a result. A dealer listing (drouot.com) gives "Paris, au bureau de l'Encyclopédie, 1824" for the 26-volume set, which is not t. 7's title page. BnF and HathiTrust records that surfaced were other editions (Didot 1861–65; Desplaces 1843–65). Furne's volume number and sections VI and VIII still unread. |
| 5 | Furetière 1690 view 397 | Not reachable | Needs the page image. |
| 6 | Le Bas t. 6 installments | No evidence found | Catalog records (Europeana, DDB) date the 12-volume set 1840–45 and t. 7 as 1842. Nothing on livraisons or on t. 6 before its 1842 title page. Inconclusive, not a "no". |
| 7 | Dezobry 1857 vs 1863 | Not reachable | No scan of the first edition located. |
| 8 | Trévoux 1704/21/32; Moréri 1674–83 | Not reachable | One attempt each. ATILF's inventory of Trévoux copies has no scan links. Wikisource 1721 page returned url_not_found. No text read, so no exact page can be given; read CROISADE in the first letter-C volume. |
| 9 | Rees vol. 10 issue date | Yes (secondary) | Wikipedia's table of Rees's parts: vol. 10, Part 19, 2 May 1808, "first part of CROISADE"; Part 20, 2 July 1808. The archive.org page gives 1819 for the set. Wikipedia is a secondary source; the part title page or the publisher's list would be the primary check. The existing row `sa-1808-rees` can take year_read 1808 with that caveat. |

## What would move the bracket

Only items 1 and 2 (both Paris reference works of 1836–42) can still produce a modern eight before 1842. Item 1 is a catalogued, digitized volume; the author can open it at the BSB link above.

## Protocol note

Britannica transcriptions on jimclifford.ca are convenient but carry catalog years. Treat as `full_text`, title page unchecked, until a scan title page is seen.
