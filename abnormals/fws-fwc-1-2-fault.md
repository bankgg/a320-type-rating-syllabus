# FWS FWC 1 + 2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

Both flight warning computers are lost: no ECAM cautions or warnings, no aural warnings, no master lights, no altitude alert, STATUS, auto callouts or memos. ECAM system pages remain, so the crew checks the overhead panel and SD pages more often than usual. The procedure requests no reset, and the QRH reset table lists only a single FWC fault (FWS FWC 1(2) FAULT), so resetting FWC 1 + 2 is not authorized in flight.

## 1. What it is
- **Trigger:** Both FWC 1 and FWC 2 have failed, or communication between the FWC and the EIS is lost. [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- **Flight phase inhibition:** none [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- QRH system reset rule: in flight, a reset is authorized only if the ECAM/OEB/FCOM/QRH procedure requests it, or if the alert is listed and authorized in the system reset table; on ground, also if the affected system is NOT listed in the table. In all other cases: RESET NOT AUTHORIZED. Only one reset at a time. [QRH 02.01A, PDF 50]

## 2. Key limits
- **Lost:** ECAM warnings, aurals, MASTER lights [FCOM PRO-ABN-FWS P 4/8, PDF 3685]
- **Also lost:** ALTI ALERT · STATUS · A/CALL OUT · MEMO [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- **INOP:** CAT 2 [FCOM PRO-ABN-FWS P 4/8, PDF 3685]
- **Reset:** NOT AUTHORIZED in flight [QRH 02.01A, PDF 50; QRH 02.02D, PDF 54]

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

### 3. No reset
**3.1 PF + PM**
- Do not use the FWS FWC 1(2) FAULT reset (QRH 02.54A): it covers a single FWC only. FWC 1 + 2 is not in the system reset table and its procedure requests no reset → RESET NOT AUTHORIZED in flight. [QRH 02.01A, PDF 50; QRH 02.02D, PDF 54; QRH 02.54A, PDF 116; FCOM PRO-ABN-FWS P 3/8, PDF 3684]

## 4. Procedure
### ECAM procedure — FWC 1 + 2 FAULT (FCOM PRO-ABN-FWS)
- MONITOR SYS …… — [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- MONITOR OVERHEAD PANEL …… — [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- *NOT AVAIL: ECAM WARN · ALTI ALERT · STATUS · A/CALL OUT · MEMO* [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- *ECAM cautions and warnings, aural warnings, master caution and warning lights are lost. ECAM system pages are still available.* [FCOM PRO-ABN-FWS P 4/8, PDF 3685]

## 5. STATUS
**INOP SYS**
- CAT2 (other INOP SYS, FWC 1 + 2) [FCOM PRO-ABN-FWS P 4/8, PDF 3685]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| FWS SDAC 1 + 2 FAULT | Related FWS failure | See the SDAC brief | [FCOM PRO-ABN-FWS P 6/8, PDF 3687] |
| FWS FWC 1(2) FAULT (single FWC) | A different alert. Only this single-FWC fault is in the QRH system reset table; it does not apply to FWC 1 + 2. | If FWS FWC 1 FAULT: C/B F01 (FWS / FWC1 / SPLY) on 49VU PULL, wait 5 s, PUSH; If FWS FWC 2 FAULT: C/B Q07 (EIS / FWC2 / SPLY) on 121VU PULL, wait 5 s, PUSH; On ground, wait 50 s after pushing the C/Bs; STATUS: CAT 3 SINGLE ONLY | [QRH 02.02D, PDF 54; QRH 02.54A, PDF 116; FCOM PRO-ABN-FWS P 5/8, PDF 3686] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No FCTM technique for this alert in the supplied FCTM. [FCOM PRO-ABN-FWS P 3/8, PDF 3684]
- On ground, QRH 02.01A also authorizes a reset when the affected system is not listed in the reset table. The FWC is listed (as FWS FWC 1(2) FAULT), so the supplied manuals give no reset for FWC 1 + 2 on ground either. [QRH 02.01A, PDF 50; QRH 02.02D, PDF 54]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-FWS — FWC 1 + 2 FAULT, FWC 1(2) FAULT | P 3–5/8 | 3684–3686 | 26 MAY 26 |
| QRH | 02.01A System reset – general; 02.02D system reset table; 02.54A FWS FWC 1(2) FAULT (related, single FWC) | 02.01A, 02.02D, 02.54A | 50, 54, 116 | 26 MAY 26 |
