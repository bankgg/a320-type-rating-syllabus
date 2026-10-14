# Source map — where things live in `books/`

## The books
| Key | File | Title | Issue / effective | Pages |
|---|---|---|---|---|
| `fcom` | `A320FAM_FCOM_14JUL26_compressed.pdf` | THA A320/A321 Flight Crew Operating Manual | rev dates per page (latest 26 MAY 26); 14 JUL 26 edition | 4,891 |
| `fctm` | `A320FAM_FCTM_14JUL26.pdf` | THA A320/A321 Flight Crew Techniques Manual | issue 14-JUL-26, effective 07-SEP-26 | 507 |
| `qrh` | `A320FAM_QRH_14JUL26.pdf` | THA A320/A321 Quick Reference Handbook | 14 JUL 26 edition | 297 |
| `pdp` | `Airbus Tutorial PDP Jan 2024.pdf` | Airbus Tutorials (UPRT included) / Flow Patterns / Cockpit Panels — slide deck, generic A320/A330 | January 2024 | 685 |

All three are marked "UNCONTROLLED IF DOWNLOADED OR PRINTED" — say so in the plan footer.
Other manuals (MEL, AFM, OM-A) are **not** in `books/`; if a procedure points to one, list it as a gap rather than filling it in.

## Locators
- **PDP**: no page numbers; cite the tutorial module and PDF page: `PDP Engine failure after V1, PDF 500`. In JSON: `{"book": "PDP", "code": "Engine failure after V1", "page": "XFTDA10ENGFTO01", "pdf": 500}`.
- **FCOM / FCTM**: footer `THA A320/A321 FLEET  <CODE> P x/y` + revision date. Cite as `FCOM PRO-ABN-ELEC P 90/122 (PDF 3215)`.
- **QRH**: header page code such as `18.01A` (chapter 18, sheet 01, page A). Cite as `QRH 18.01A (PDF 152)`.
- PDF page numbers are 1-based physical pages — the numbers `manuals.py` prints and `Read … pages:` uses.

## Effectivity
Each documentary unit carries `Ident.:` and (usually) `Applicable to:`; continuation units inherit the last stated applicability.
- HS-TX fleet letters: A B C D E F G H J K L M N O P Q R S T U (no I). HS-TO fleet: A–L, N, O, Q.
- Common HS-TX splits seen in the books: **HS-TXA..TXO vs HS-TXP..TXU** (e.g. ELEC EMER CONFIG), **HS-TXA..TXF vs HS-TXG..TXU** (e.g. F/CTL ALTN LAW). Other splits occur; always trust the block's own list.
- Policy: KEEP `ALL` and any list containing an HS-TX registration; DROP lists with only HS-TO registrations.
- Aircraft allocation table: FCOM `PLP-AAT` (PDF 26–27).

## System → chapter correspondence
ECAM title prefix (e.g. `ELEC`, `HYD`, `ENG`) ≈ FCOM `PRO-ABN-<SYS>` section. `manuals.py find` resolves this from the FCOM PRO-ABN table of contents (PDF 2804–2821).

| PRO-ABN system | FCOM procedures (PDF) | FCTM technique (PDF) | FCOM DSC chapters | QRH chapter |
|---|---|---|---|---|
| A-ICE | 2848–2889 | — | DSC-30 | — |
| AIR | 2890–2971 | — | DSC-36, DSC-21 | ABN-11 AIR |
| APU / APUF | 2972–2977 | — | DSC-49 (+DSC-26 fire) | — |
| AUTO_FLT | 2978–3019 | PR-AEP-AUTOFLT (394–395) | DSC-22_10/_30/_40 | — |
| AVNCS | 3020–3021 | — | DSC-21 | — |
| BLEED | 3022–3023 | — | DSC-36 | — |
| BRAKES / NWS | 3024–3047 | PR-AEP-BRK (396–397) | DSC-32 | ABN-12 BRAKES |
| CAB_PR | 3048–3061 | PR-AEP-CAB_PR (398–399) | DSC-21 | ABN-13 CAB PR |
| C_B | 3062–3063 | — | DSC-24 | — |
| COM | 3064–3085 | — | DSC-23 | — |
| COND | 3086–3095 | — | DSC-21 | ABN-14 COND |
| CONFIG | 3096–3101 | — | DSC-31 | — |
| DATALINK | 3102–3105 | — | DSC-46, DSC-23 | — |
| DOOR | 3106–3121 | — | DSC-52 | ABN-15 DOOR |
| EIS | 3122–3125 | — | DSC-31 | ABN-17 EIS |
| ELEC | 3126–3247 | PR-AEP-ELEC (400–401) | DSC-24 | ABN-18 ELEC |
| ENG | 3248–3473 | PR-AEP-ENG (402–427) | DSC-70 (+DSC-26 fire) | ABN-19 ENG |
| F_CTL | 3474–3605 | PR-AEP-F_CTL (428–433) | DSC-27 | ABN-20 F/CTL |
| FUEL | 3606–3681 | PR-AEP-FUEL (434–437) | DSC-28 | ABN-21 FUEL |
| FWS | 3682–3689 | — | DSC-31 | — |
| HYD | 3690–3765 | PR-AEP-HYD (438–441) | DSC-29 | ABN-23 HYD |
| LG | 3766–3795 | PR-AEP-LG (442–445) | DSC-32 | ABN-24 L/G |
| MISC | 3796–3825 | PR-AEP-MISC (446–477) | (by topic) | ABN-25 MISC |
| NAV | 3826–3949 | PR-AEP-NAV (478–497) | DSC-34 | ABN-26 NAV |
| OVERSPEED | 3950–3951 | — | DSC-27 | — |
| RECORDER | 3952–3957 | — | DSC-31 | — |
| SMOKE | 3958–4007 | PR-AEP-SMOKE (498–507) | DSC-26, DSC-21 | ABN-27 SMOKE |
| SURV | 4008–4019 | — | DSC-34 | — |
| T-O | 4020–4029 | — | DSC-31 | — |
| VENT | 4030–4041 | — | DSC-21 | — |
| WHEEL | 4042–4045 | — | DSC-32 | ABN-28 WHEEL |
| W_A_ICE | 4046–4057 | — | DSC-30 | — |

Other QRH chapters: ABN-01 [ADV] ECAM advisory, ABN-02 [RESET] system reset (check it whenever the plan considers a reset), NP normal procedures, OPS operational data (fuel penalty factors, landing distance), OEB.

## PDP tutorial modules relevant to abnormal operations
| Module | PDF pages |
|---|---|
| Golden rules | 18–22 |
| Management of abnormal operations (detection, ECAM actions, SD, STATUS, QRH procedures, actions completed, descent preparation) | 420–435 |
| Use of summary (ELEC EMER CONFIG / dual HYD) | 436–442 |
| All engine flameout (+ relight sequences) | 443–450 |
| Dual FMGC failure (FMGC 1 failure, dual, NAV B/UP) | 451–482 |
| Emergency descent | 483–491 |
| Emergency evacuation | 492–493 |
| Engine failure after V1 (detection → ECAM → acceleration → continue ECAM → approach prep) | 494–504 |
| Engine failure in cruise | 505–511 |
| Reconfiguration laws | 512–515 |
| Crew incapacitation | 516–521 |
| Rejected takeoff (task sharing, flow pattern) | 524–533 |
| Smoke | 534–540 |
| Stall recovery | 541–556 |
| Unreliable speed indication (and UPRT) | 557–671 |
| Windshear | 672–686 |
`section pdp <words>` prints any module's range (normal-procedure modules too, e.g. takeoff 183–197, go-around 264–279).

## Always-relevant general sources
- FCTM AOP-20 (PDF 68–77) task sharing; FCTM AOP-30-10…60 (PDF 78–95) management of abnormal operations; FCTM AOP-40 (PDF 96–99) golden rules; FCTM PR-AEP-GEN (PDF 392) "ECAM/QRH handled as described in AOP-30-30".
- FCOM PRO-ABN-ABN-00 (PDF 2824–2835) procedure layout and callouts; PRO-ABN-ABN-MEM (2842–2843) memory items list; PRO-ABN-ABN-QRH (2844–2847) list of QRH procedures.
- FCOM DSC-31-15 flight phases (for flight phase inhibition numbers).
These are pre-extracted in `abnormal-operations.md`.
