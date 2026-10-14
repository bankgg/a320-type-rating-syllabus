# NAV ADR 1(2)(3) FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (the HS-TO version is not used).

An amber caution: one air data reference has failed, so one side loses speed and altitude data. Switch AIR DATA to CAPT 3 (ADR 1) or F/O 3 (ADR 2) and turn the failed ADR pb OFF; for ADR 2 also check the baro reference. Approach capability drops to CAT 3 SINGLE.

## 1. What it is
- **Trigger:** This alert triggers when the ADR 1(2)(3) is failed. Inhibited in flight phases 1, 3, 4, 5, 7, 8 and 10 — NAV ADR 1(2) FAULT is not inhibited in phases 3, 5 and 7; NAV ADR 3 FAULT is not inhibited in phase 3 while the ADR 3 is in use. [FCOM PRO-ABN-NAV P 21/124, PDF 3846]
- **Flight phase inhibition:** phases 1, 3, 4, 5, 7, 8, 10 [FCOM PRO-ABN-NAV P 21/124, PDF 3846]
- Each ADIRS has two parts (ADR and IRS) that may fail independently. A single NAV ADR FAULT only requires action on the switching panel as indicated by the ECAM. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- AIR DATA selector: NORM — ADIRU 1 to the captain side, ADIRU 2 to the F/O side. CAPT 3 — ADR 3 replaces ADR 1. F/O 3 — ADR 3 replaces ADR 2. [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]
- ADR pb-sw FAULT light: ADR failed (NAV ADR FAULT alert). Pressing it turns the ADR off and the FAULT light goes off. [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]

## 2. Key limits
- **ADR 1 FAULT:** AIR DATA CAPT 3 · ADR 1 OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **ADR 2 FAULT:** AIR DATA F/O 3 · ADR 2 OFF · BARO REF CHECK [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **ADR 3 FAULT:** ADR 3 OFF · AIR DATA NORM if ADR 3 in use [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **Approach capability:** CAT 3 SINGLE ONLY [FCOM PRO-ABN-NAV P 22/124, PDF 3847]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “NAV ADR 1 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-NAV P 21/124, PDF 3846; PDP Management of abnormal operations, PDF 424]
- Announce the ADR shown (1, 2 or 3) [FCOM PRO-ABN-NAV P 21/124, PDF 3846]
- Confirm on the overhead ADIRS panel: ADR FAULT light on [FCTM AOP-30-30 P 2/6, PDF 83; FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- If ADR and IR of the same ADIRU fail together, do this ADR procedure before the IR procedure [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **NAV ADR 1 FAULT** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - AIR DATA SWTG …… CAPT 3 [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - Point to the ADR 1 pb, announce system – control – action, then press it [FCTM AOP-30-20 P 1/2, PDF 80]
  - ADR 1 P/B …… OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **NAV ADR 2 FAULT** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - AIR DATA SWTG …… F/O 3 [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - Point to the ADR 2 pb, announce system – control – action, then press it [FCTM AOP-30-20 P 1/2, PDF 80]
  - ADR 2 P/B …… OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - BARO REF …… CHECK [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - Both baro reference channels are now driven by the same FCU channel [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **NAV ADR 3 FAULT** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - ADR 3 P/B …… OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - **If ADR 3 in use** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
    - AIR DATA SWTG …… NORM [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **If the GPWS TERR FAULT and GPWS SYS FAULT lights come on (ADR 1)** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - Switch off the GPWS TERR pb-sw and the GPWS SYS pb-sw [FCOM PRO-ABN-NAV P 22/124, PDF 3847]

### 3. STATUS
**3.1 PM**
- “CLEAR NAV ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR NAV” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

## 4. Procedure
### NAV ADR 1(2)(3) FAULT (FCOM PRO-ABN-NAV (HS-TX))
- *In case of simultaneous failure of ADR and IR (same ADIRU), apply ADR FAULT procedure before IR FAULT procedure.* [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **NAV ADR 1 FAULT:** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - AIR DATA SWTG …… CAPT 3 — Select ADR 3 to captain side. [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - ADR 1 P/B …… OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - *The GPWS TERR FAULT and GPWS SYS FAULT lights come on (enhanced/predictive GPWS functions inhibited). If this occurs, switch off the GPWS TERR pb-sw and the GPWS SYS pb-sw.* [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **NAV ADR 2 FAULT:** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - AIR DATA SWTG …… F/O 3 — Select ADR 3 to first officer side. [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - ADR 2 P/B …… OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - BARO REF …… CHECK — If ADR 2 fails, both baro reference channels are driven by the same FCU channel. Consequently the baro reference displays must be checked. [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- **NAV ADR 3 FAULT:** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - ADR 3 P/B …… OFF [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
  - **If ADR 3 in use:** [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
    - AIR DATA SWTG …… NORM [FCOM PRO-ABN-NAV P 22/124, PDF 3847]

## 5. STATUS
**Information**
- CAT 3 SINGLE ONLY [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
**INOP SYS**
- ADR 1(2)(3) [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- CAT 3 DUAL [FCOM PRO-ABN-NAV P 22/124, PDF 3847]
- GPWS (in case of ADR 1 FAULT only) [FCOM PRO-ABN-NAV P 22/124, PDF 3847]

## 7. FCTM technique
- Overhead actions: the PM points to the control and announces system – control – action, then checks the result. [FCTM AOP-30-20 P 1/2, PDF 80]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| NAV IR 1(2)(3) FAULT | If the IR of the same ADIRU has also failed, apply it after this ADR procedure. | ATT HDG SWTG to the side of the failed IR; ATC/XPDR to the other system | [FCOM PRO-ABN-NAV P 22/124, PDF 3847; FCOM PRO-ABN-NAV P 88/124, PDF 3913] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No ADR-specific FCTM technique beyond the ADR/IRS FAULT paragraph, and no PDP module; the flow uses the generic ECAM handling. No callout is given for the switching itself. [FCTM PR-AEP-NAV P 1/20, PDF 478; PDP Management of abnormal operations, PDF 424]
- The HS-TO version of the procedure (FCOM P 23–25/124) is not used. [FCOM PRO-ABN-NAV P 22/124, PDF 3847]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — NAV ADR 1(2)(3) FAULT (HS-TX) | P 21–22/124 | 3846–3847 | 26 MAY 26 |
| FCTM | PR-AEP-NAV — ADR/IRS FAULT | P 1/20 | 478 | 26 MAY 26 |
| FCOM | DSC-34-NAV-10-20 — ADIRS controls | P 3/6 | 2102 | 18 FEB 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
