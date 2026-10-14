# FMGC 1(2) FAULT · FMGC 1+2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** all HS-TX — QRH reset procedure: HS-TX version.

One FMGC failing leaves the other running everything (single mode): recover the AP on the other side, put both NDs on the same range and mode, and reset the failed FMGC from the QRH. Both FMGCs failing drops AP/FD and A/THR: try to re-engage them, otherwise fly manual thrust with FDs off and TRK/FPA, tune navaids on the RMPs, reset per QRH, and use MCDU BACK UP NAV.

## 1. What it is
- **Trigger:** Single or dual FMGC failure. Handled from the FCTM technique, the FMGS degraded modes and the QRH system reset table (AUTO FLT — BOTH MCDU LOCKED OR BLANK OR FMGC MALFUNCTION). [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; QRH 02.12A, PDF 65]
- **Flight phase inhibition:** none [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; QRH 02.12A, PDF 65]
- Single mode: the failed FMGC shows OPP FMGC IN PROCESS; its ND shows MAP NOT AVAIL / SET OFFSIDE RNG/MODE, or OFFSIDE FM CONTROL when ranges match. [FCOM DSC-22_10-30 P 4/6, PDF 319]
- If one FMGC fails, the remaining FMGC controls the radio receivers on both sides; if both fail, use the RMPs. [FCOM DSC-34-NAV-30-10 P 1/4, PDF 2134]
- BACK UP NAV gives flight planning, position from IRS/GPIRS, F-PLN on ND and sequencing — no AP/FD NAV mode. [FCOM DSC-22_10-30 P 5/6, PDF 320]

## 2. Key limits
- **C/B pull:** 10 s, then push [QRH 02.12A, PDF 65]
- **Re-engage AP/FD:** 1 min after PLEASE WAIT clears [QRH 02.12A, PDF 65]
- **Resets:** only per QRH table [QRH 02.01A, PDF 50; FCTM AOP-30-20 P 1/2, PDF 80]

## 3. Flow (PF / PM)
### 1. Single FMGC failure (demo FMGC 1 / FMGC 2)
**1.1 PF**
- Golden rules: fly, navigate, communicate; appropriate level of automation [PDP Dual FMGC failure, PDF 452]
- AP1 and FD1 lost (affected side) → engage AP2; A/THR stays [PDP Dual FMGC failure, PDF 453; FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]
- Do not use the MCDU until PLEASE WAIT clears [FCOM DSC-22_10-30 P 4/6, PDF 319]
**1.2 PM**
- Select the same range and mode on both NDs (SET OFFSIDE RNG/MODE → OFFSIDE FM CONTROL) [PDP Dual FMGC failure, PDF 454; FCOM DSC-22_10-30 P 4/6, PDF 319; FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]
- Failed-side MCDU reverts to MCDU MENU; exit by selecting any MCDU page (healthy FM in force) [PDP Dual FMGC failure, PDF 454]
- Both FDs now driven by the operative FMGC; any MCDU entry goes to it [FCOM DSC-22_10-30 P 4/6, PDF 319]

### 2. Reset the failed FMGC (QRH 02.12)
**2.1 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432]
- Before each C/B action: PM points to the C/B, PF answers “CONFIRMED” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.2 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
**2.3 PM**
- **If FMGC 1 is affected** [QRH 02.12A, PDF 65]
  - AP 2 pb …… ON [QRH 02.12A, PDF 65]
  - FD 1 pb …… OFF [QRH 02.12A, PDF 65]
  - C/B B02 (AUTO FLT / FMGC / 1) on 49VU …… PULL — wait 10 s — PUSH [QRH 02.12A, PDF 65]
- **If FMGC 2 is affected** [QRH 02.12A, PDF 65]
  - AP 1 pb …… ON [QRH 02.12A, PDF 65]
  - FD 2 pb …… OFF [QRH 02.12A, PDF 65]
  - C/B M17 (AUTO FLT / FMGC / 2) on 121VU …… PULL — wait 10 s — PUSH [QRH 02.12A, PDF 65]
**2.4 PF**
- Wait 1 min after PLEASE WAIT disappears before re-engaging FD/AP of the reset FMGC [QRH 02.12A, PDF 65]

### 3. Dual FMGC failure
**3.1 PF**
- FMGC auto-reset may occur; when the ECAM is confirmed apply ECAM/OEB actions and the abnormal task sharing [PDP Dual FMGC failure, PDF 456]
- AP/FD and A/THR disconnect — try to re-engage both [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]
- Not recovered: move thrust levers for manual thrust; FDs OFF; TRK/FPA (bird) [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]
**3.2 PM**
- Tune navaids on the RMPs [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; FCOM DSC-34-NAV-30-10 P 1/4, PDF 2134]
- Check the QRH system reset table, then reset per QRH 02.12 [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; QRH 02.12A, PDF 65]
- Not recovered: MCDU MENU → BACK UP NAV (simplified IRS/GPS navigation) [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; FCOM DSC-22_10-30 P 5/6, PDF 320]

## 4. Procedure
### AUTO FLT — BOTH MCDU LOCKED OR BLANK OR FMGC MALFUNCTION (in flight) (QRH 02.12)
- **If FMGC 1 is affected:** [QRH 02.12A, PDF 65]
  - AP 2 pb …… ON [QRH 02.12A, PDF 65]
  - FD 1 pb …… OFF [QRH 02.12A, PDF 65]
  - C/B B02 (AUTO FLT / FMGC / 1) — on 49VU …… PULL [QRH 02.12A, PDF 65]
  - *Wait 10 s* [QRH 02.12A, PDF 65]
  - C/B B02 (AUTO FLT / FMGC / 1) …… PUSH [QRH 02.12A, PDF 65]
  - **CAUTION** Wait 1 min after the PLEASE WAIT message disappears from the MCDU, before engaging or re-engaging the FD and the AP of reset FMGC. [QRH 02.12A, PDF 65]
- **If FMGC 2 is affected:** [QRH 02.12A, PDF 65]
  - AP 1 pb …… ON [QRH 02.12A, PDF 65]
  - FD 2 pb …… OFF [QRH 02.12A, PDF 65]
  - C/B M17 (AUTO FLT / FMGC / 2) — on 121VU …… PULL [QRH 02.12A, PDF 65]
  - *Wait 10 s* [QRH 02.12A, PDF 65]
  - C/B M17 (AUTO FLT / FMGC / 2) …… PUSH [QRH 02.12A, PDF 65]
  - **CAUTION** Wait 1 min after the PLEASE WAIT message disappears from the MCDU, before engaging or re-engaging the FD and the AP of reset FMGC. [QRH 02.12A, PDF 65]
- *If the FMGC reset is not successful, consider FMGC reset with engines not running.* [QRH 02.12B, PDF 66]

## 6. QRH and reference tables
### System reset — general
**In flight**
- Reset authorized only if an ECAM/OEB/FCOM/QRH procedure requests it, or the alert/malfunction is listed and authorized in the system reset table. [QRH 02.01A, PDF 50]
- Only one reset at a time unless the procedure says otherwise. [QRH 02.01A, PDF 50]
## 7. FCTM technique
- Single failure: recover flight-plan display on the affected ND by using the same range as the opposite ND; consider a reset per QRH. [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]
- Dual failure: if the FG part is still available, the AP may remain engaged and revert to HDG-V/S or TRK-FPA (FG standard dependent). [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No ECAM procedure titled FMGC 1(2) FAULT exists in the supplied FCOM; the brief uses FCTM, FCOM DSC and QRH reset content. [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; FCOM DSC-22_10-30 P 4/6, PDF 319]
- FCOM DSC-22_20-40-10 manual FMGC reset / resynchronisation not expanded here. [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCTM | PR-AEP-AUTOFLT — FMGC failure | P 1/2 | 394 | 23 AUG 23 |
| FCOM | DSC-22_10-30 — single mode, back up nav | P 4–5/6 | 319–320 | 30 JUL 24 |
| QRH | 02.01 System reset general · 02.12 FMGC malfunction | 02.01A, 02.12A–B | 50, 65–66 | 26 MAY 26 |
| PDP | Dual FMGC failure (EFTDA1DUALFM001) | FMGC 1 failure, dual FMGC failure | 451–456 | OCT 2018 |
