# NAV IR 1(2)(3) FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (Applicable to: ALL).

An amber caution: one inertial reference has failed, so one side loses attitude and heading (red ATT flag on the PFD, red HDG flag on the ND). The only ECAM action is on the pedestal switching panel: ATT HDG to CAPT 3 for IR 1, F/O 3 for IR 2, plus the transponder system. If the IR FAULT light flashes, the IR may give attitude again in ATT mode through the QRH IR ALIGNMENT IN ATT MODE procedure.

## 1. What it is
- **Trigger:** This alert triggers when the IR 1(2)(3) is failed. Inhibited in flight phases 3, 4, 5, 7 and 8 — not inhibited in phase 3 for NAV IR 1(2) FAULT, or for NAV IR 3 FAULT while the ADR 3 is in use. [FCOM PRO-ABN-NAV P 87/124, PDF 3912]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-NAV P 87/124, PDF 3912]
- Each ADIRS has two parts (ADR and IRS) that may fail independently. The IRS part may fail totally or may be available in ATT mode. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- A single NAV ADR FAULT or NAV IRS FAULT is a simple procedure: only action on the switching panel as indicated by the ECAM. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- ATT HDG selector: NORM — ADIRU 1 supplies PFD 1/ND 1, ADIRU 2 supplies PFD 2/ND 2. CAPT 3 — IR 3 replaces IR 1. F/O 3 — IR 3 replaces IR 2. [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]
- If ADIRU 2 fails, the ATT HDG selector has to be set to F/O 3 to maintain side 1 / side 2 segregation; ADIRU 3 is then supplied by GPS receiver 2. [FCOM DSC-34-NAV-15-10 P 3/4, PDF 2122]
- IR FAULT light flashing: attitude and heading may be recovered in ATT mode. Steady: the IR is lost. [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]
- In ATT mode the IR gives only attitude and heading (heading entered on the MCDU, reset about every 10 min). Once an IR is set from NAV to ATT or OFF in flight, NAV mode is lost for the rest of the flight; it is recovered only on ground by a complete alignment. [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]

## 2. Key limits
- **IR 1 FAULT:** ATT HDG CAPT 3 · XPDR SYS 2 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 2 FAULT:** ATT HDG F/O 3 · XPDR SYS 1 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **Approach capability:** CAT 3 SINGLE ONLY [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **ATT mode heading:** Reset about every 10 min [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- Affected side: red ATT flag on the PFD and red HDG flag on the ND. CHECK ATT appears if both PFDs differ by more than 5° in pitch or roll [FCOM DSC-34-NAV-20 P 8/10, PDF 2131; FCOM PRO-ABN-NAV P 15/124, PDF 3840; FCOM DSC-31-05-60 P 4/6, PDF 1819]
**1.2 PM**
- “NAV IR 1 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-NAV P 87/124, PDF 3912; PDP Management of abnormal operations, PDF 424]
- Announce the IR shown (1, 2 or 3) [FCOM PRO-ABN-NAV P 87/124, PDF 3912]
- Confirm on the overhead ADIRS panel: IR FAULT light (flashing: ATT mode may be available; steady: IR lost) [FCTM AOP-30-30 P 2/6, PDF 83; FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]
**1.3 PF**
- **If the failed IR feeds the PF's instruments** [FCTM AOP-30-30 P 1/6, PDF 82]
  - The FLY task is affected — the captain may re-allocate the PF role [FCTM AOP-30-30 P 1/6, PDF 82]
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- If ADR and IR of the same ADIRU fail together, do the ADR FAULT procedure first [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 1 FAULT** [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATT HDG SWTG …… CAPT 3 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATC/XPDR …… SYS 2 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 2 FAULT** [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATT HDG SWTG …… F/O 3 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATC/XPDR …… SYS 1 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 3 FAULT** [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATT HDG SWTG (IF IR 3 IN USE) …… NORM [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - This line is not displayed on the ECAM [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- Check attitude and heading are back on the affected PFD/ND (IR 3 now replaces the failed IR) [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]

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

### 4. IR in ATT mode (if available)
**4.1 PF**
- **If the IR FAULT light flashes (attitude and heading may be recovered in ATT mode)** [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101; PDP Management of abnormal operations, PDF 427]
  - “IR ALIGNMENT IN ATT MODE PROCEDURE” [PDP Management of abnormal operations, PDF 427; QRH 26.04A, PDF 243]
**4.2 PM**
- IR (affected) MODE SEL …… ATT [QRH 26.04A, PDF 243; FCOM PRO-ABN-NAV P 15/124, PDF 3840]
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**4.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- IR MODE selector: crosscheck before acting in flight [FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
**4.4 PM**
- Set the IR mode selector to ATT [QRH 26.04A, PDF 243]
**4.5 PF**
- KEEP SPEED, HEADING, AND FL CONSTANT FOR 30 s …… — [QRH 26.04A, PDF 243]
**4.6 PM**
- FMS DATA page …… SELECT [QRH 26.04A, PDF 243]
- IRS MONITOR key …… PRESS [QRH 26.04A, PDF 243]
- [SET HDG key] A/C HDG …… ENTER [QRH 26.04A, PDF 243]
- CROSSCHECK HEADING REGULARLY WITH STBY COMPASS AND UPDATE AS REQUIRED …… — [QRH 26.04A, PDF 243]
- In ATT mode the heading must be reset about every 10 min [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]
- “IR ALIGNMENT IN ATT MODE PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### NAV IR 1(2)(3) FAULT (FCOM PRO-ABN-NAV)
- *In case of a simultaneous ADR and IR (same ADIRU) failure, apply the ADR FAULT procedure before the IR FAULT procedure.* [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 1 FAULT:** [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATT HDG SWTG …… CAPT 3 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATC/XPDR …… SYS 2 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 2 FAULT:** [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATT HDG SWTG …… F/O 3 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATC/XPDR …… SYS 1 [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- **IR 3 FAULT:** [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - ATT HDG SWTG (IF IR 3 IN USE) …… NORM [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
  - *This line is not displayed on the ECAM.* [FCOM PRO-ABN-NAV P 88/124, PDF 3913]

### [QRH] IR ALIGNMENT IN ATT MODE (QRH 26.04A (HS-TX version))
- IR (affected) MODE SEL …… ATT [QRH 26.04A, PDF 243]
- *KEEP SPEED, HEADING, AND FL CONSTANT FOR 30 s* [QRH 26.04A, PDF 243]
- FMS DATA page …… SELECT [QRH 26.04A, PDF 243]
- IRS MONITOR key …… PRESS [QRH 26.04A, PDF 243]
- [SET HDG key] A/C HDG …… ENTER [QRH 26.04A, PDF 243]
- *CROSSCHECK HEADING REGULARLY WITH STBY COMPASS AND UPDATE AS REQUIRED* [QRH 26.04A, PDF 243]

## 5. STATUS
**Information**
- IR MAY BE AVAIL IN ATT — Refer to [QRH] IR ALIGNMENT IN ATT MODE [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- CAT 3 SINGLE ONLY [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
**INOP SYS**
- IR 1(2)(3) [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- CAT 3 DUAL [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- GPWS TERR (in case of an IR 1 fault) [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- ROW/ROP (in case of an IR 1 fault) [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- TCAS (in case of an IR 1 fault) — may be inoperative depending on the TCAS manufacturer. If IR 1 is available in ATT mode, the TCAS can be recovered by entering the aircraft magnetic heading into the CDU, as per IR ALIGNMENT IN ATT MODE. [FCOM PRO-ABN-NAV P 88/124, PDF 3913]

## 7. FCTM technique
- The PF usually remains PF for the entire flight, unless the captain re-allocates tasks or a failure impacts the PF's FLY task. [FCTM AOP-30-30 P 1/6, PDF 82]
- IR MODE selector actions are crosschecked by both pilots before acting in flight. [FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] IR ALIGNMENT IN ATT MODE | STATUS shows IR MAY BE AVAIL IN ATT; apply when the IR FAULT light flashes. | IR (affected) MODE SEL ATT (crosscheck first); Keep speed, heading and FL constant for 30 s; MCDU DATA → IRS MONITOR → SET HDG: enter A/C HDG; Crosscheck heading with STBY compass; update about every 10 min | [QRH 26.04A, PDF 243; FCOM PRO-ABN-NAV P 15/124, PDF 3840; FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101] |
| NAV ADR 1(2)(3) FAULT | If the ADR of the same ADIRU has also failed, apply the ADR FAULT procedure first. | AIR DATA SWTG to the side of the failed ADR (CAPT 3 / F/O 3); ADR (affected) P/B OFF | [FCOM PRO-ABN-NAV P 88/124, PDF 3913; FCOM PRO-ABN-NAV P 22/124, PDF 3847] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No IR-specific FCTM or PDP module exists; the flow uses the generic ECAM handling (FCTM AOP-30-30, PDP Management of abnormal operations). No callout is given for the ATT HDG switching itself. [FCTM PR-AEP-NAV P 1/20, PDF 478; PDP Management of abnormal operations, PDF 424]
- The alert is inhibited in flight phases 4, 5, 7 and 8 (and partly 3). The manuals give no separate crew procedure for an IR loss with no ECAM alert; detection then relies on the PFD/ND flags and the overhead FAULT light. [FCOM PRO-ABN-NAV P 87/124, PDF 3912; FCOM DSC-34-NAV-20 P 8/10, PDF 2131; FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]
- GPWS TERR, ROW/ROP and TCAS INOP lines are equipment-dependent (option marks and footnotes on the FCOM page). [FCOM PRO-ABN-NAV P 88/124, PDF 3913]
- The HS-TO version of IR ALIGNMENT IN ATT MODE (extra "On ground: T.O SURV pb OFF" line) is not used. [QRH 26.04A, PDF 243]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — NAV IR 1(2)(3) FAULT | P 87–88/124 | 3912–3913 | 26 MAY 26 |
| FCOM | PRO-ABN-NAV — [QRH] IR ALIGNMENT IN ATT MODE | P 15/124 | 3840 | 26 MAY 26 |
| QRH | 26.04 IR ALIGNMENT IN ATT MODE | 26.04A | 243 | 26 MAY 26 |
| FCTM | PR-AEP-NAV — ADR/IRS FAULT | P 1/20 | 478 | 26 MAY 26 |
| FCOM | DSC-34-NAV — ADIRS controls, GPS, PFD flags | DSC-34-NAV-10-20 P 2–3/6, 15-10 P 3/4, 20 P 8/10 | 2101–2102, 2122, 2131 | 18 FEB 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
