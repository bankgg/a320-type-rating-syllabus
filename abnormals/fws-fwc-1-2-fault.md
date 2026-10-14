# FWS FWC 1 + 2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

Both flight warning computers are lost: no ECAM cautions or warnings, no aural warnings, no master lights, no altitude alert, STATUS, auto callouts or memos. ECAM system pages remain, so the crew checks the overhead panel and SD pages more often than usual. A single FWC fault can be reset from the QRH.

## 1. What it is
- **Trigger:** Both FWC 1 and FWC 2 have failed, or communication between the FWC and the EIS is lost. [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- **Flight phase inhibition:** none [FCOM PRO-ABN-FWS P 3/8, PDF 3684]

## 2. Key limits
- **Lost:** ECAM warnings, aurals, MASTER lights [FCOM PRO-ABN-FWS P 4/8, PDF 3685]
- **Also lost:** ALTI ALERT · STATUS · A/CALL OUT · MEMO [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- **INOP:** CAT 2 [FCOM PRO-ABN-FWS P 4/8, PDF 3685]
- **FWC reset (single):** C/B 5 s [QRH 02.54A, PDF 116]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PM**
- “FWC 1 + 2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-FWS P 3/8, PDF 3684]
**1.2 PF**
- “ECAM ACTION” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]

### 2. Procedure
**2.1 PM**
- MONITOR SYS …… — [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- MONITOR OVERHEAD PANEL …… — [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- Check panels for local warnings and SD pages regularly — more often than usual [FCOM PRO-ABN-FWS P 4/8, PDF 3685]
**2.2 PF**
- No altitude alert and no auto callouts: crosscheck altitudes and call heights [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- Check the general status of systems for DES/APPR preparation [FCOM PRO-ABN-FWS P 4/8, PDF 3685]

### 3. Single FWC fault — reset (QRH 02.54)
**3.1 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432]
- PM points to the C/B; PF answers “CONFIRMED” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**3.2 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
**3.3 PM**
- **If FWS FWC 1 FAULT** [QRH 02.54A, PDF 116]
  - C/B F01 (FWS / FWC1 / SPLY) on 49VU …… PULL — wait 5 s — PUSH [QRH 02.54A, PDF 116]
- **If FWS FWC 2 FAULT** [QRH 02.54A, PDF 116]
  - C/B Q07 (EIS / FWC2 / SPLY) on 121VU …… PULL — wait 5 s — PUSH [QRH 02.54A, PDF 116]

## 4. Procedure
### ECAM procedure — FWC 1 + 2 FAULT (FCOM PRO-ABN-FWS)
- MONITOR SYS …… — [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- MONITOR OVERHEAD PANEL …… — [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- *NOT AVAIL: ECAM WARN · ALTI ALERT · STATUS · A/CALL OUT · MEMO* [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- *ECAM cautions and warnings, aural warnings, master caution and warning lights are lost. ECAM system pages are still available.* [FCOM PRO-ABN-FWS P 4/8, PDF 3685]

### FWS FWC 1(2) FAULT reset (QRH 02.54)
- **If FWS FWC 1 FAULT:** [QRH 02.54A, PDF 116]
  - C/B F01 (FWS / FWC1 / SPLY) — on 49VU …… PULL [QRH 02.54A, PDF 116]
  - *Wait 5 s* [QRH 02.54A, PDF 116]
  - C/B F01 (FWS / FWC1 / SPLY) …… PUSH [QRH 02.54A, PDF 116]
- **If FWS FWC 2 FAULT:** [QRH 02.54A, PDF 116]
  - C/B Q07 (EIS / FWC2 / SPLY) — on 121VU …… PULL [QRH 02.54A, PDF 116]
  - *Wait 5 s* [QRH 02.54A, PDF 116]
  - C/B Q07 (EIS / FWC2 / SPLY) …… PUSH [QRH 02.54A, PDF 116]
- *On ground, wait 50 s after pushing the C/Bs.* [QRH 02.54A, PDF 116]

## 5. STATUS
**Information**
- Single FWC fault: CAT 3 SINGLE ONLY (INOP SYS: CAT 3 DUAL, FWC 1(2)) [FCOM PRO-ABN-FWS P 5/8, PDF 3686]
**INOP SYS**
- CAT2 (other INOP SYS, FWC 1 + 2) [FCOM PRO-ABN-FWS P 4/8, PDF 3685]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| FWS SDAC 1 + 2 FAULT | Related FWS failure | See the SDAC brief | [FCOM PRO-ABN-FWS P 6/8, PDF 3687] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The QRH reset table covers FWC 1(2) FAULT (single); no reset is listed for FWC 1 + 2. [QRH 02.54A, PDF 116]
- No FCTM technique for this alert in the supplied FCTM. [FCOM PRO-ABN-FWS P 3/8, PDF 3684]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-FWS — FWC 1 + 2 FAULT, FWC 1(2) FAULT | P 3–5/8 | 3684–3686 | 26 MAY 26 |
| QRH | 02.54 FWS FWC 1(2) FAULT | 02.54A | 116 | 26 MAY 26 |
