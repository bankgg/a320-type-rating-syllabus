# FWS SDAC 1 + 2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

Both system data acquisition concentrators are lost, so some amber cautions will not appear. Red warnings, engine and fuel parameters and slat/flap positions stay on the upper ECAM. Watch the overhead panel for local fault lights; only the ENG, FUEL, F/CTL and WHEEL (gear position) SD pages remain.

## 1. What it is
- **Trigger:** Both SDAC 1 and SDAC 2 have failed. [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-FWS P 6/8, PDF 3687]

## 2. Key limits
- **Lost:** some amber cautions [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
- **SD pages left:** ENG · FUEL · F/CTL · WHEEL [FCOM PRO-ABN-FWS P 6/8, PDF 3687]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PM**
- “SDAC 1 + 2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-FWS P 6/8, PDF 3687]
**1.2 PF**
- “ECAM ACTION” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]

### 2. Procedure
**2.1 PM**
- MONITOR OVERHEAD PANEL …… — [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
- ECAM ENG FUEL F/CTL WHEEL (L/G POS IND) SYS PAGES AVAIL [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
**2.2 PF**
- Red warnings, ENG/FUEL parameters and slat/flap position remain on the upper ECAM [FCOM PRO-ABN-FWS P 6/8, PDF 3687]

### 3. STATUS
**3.1 PM**
- “CLEAR FWS ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR FWS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**3.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- INOP SYS: SDAC 1 + 2 [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-FWS)
- MONITOR OVERHEAD PANEL …… — — Some amber cautions are lost. [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
- *All red warnings, engine and fuel parameters, and slat/flap positions are available on ECAM upper DU.* [FCOM PRO-ABN-FWS P 6/8, PDF 3687]
- *ECAM ENG FUEL F/CTL WHEEL (L/G POS IND) SYS PAGES AVAIL.* [FCOM PRO-ABN-FWS P 6/8, PDF 3687]

## 5. STATUS
**INOP SYS**
- SDAC 1 + 2 [FCOM PRO-ABN-FWS P 6/8, PDF 3687]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| FWS FWC 1 + 2 FAULT | Related FWS failure | See the FWC brief | [FCOM PRO-ABN-FWS P 3/8, PDF 3684] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No SDAC entry in the QRH system reset table and no FCTM technique for this alert in the supplied manuals; the syllabus "reset" is not described in books/. [FCOM PRO-ABN-FWS P 6/8, PDF 3687; QRH 02.01A, PDF 50]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-FWS — FWS SDAC 1 + 2 FAULT | P 6/8 | 3687 | 26 MAY 26 |
