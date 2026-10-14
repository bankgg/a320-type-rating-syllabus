# NAV IR 1+2(1+3)(2+3) FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX.

An amber caution: two inertial references have failed. AP, FD and A/THR are lost, the flight controls revert to alternate law (protections lost) and one PFD loses attitude unless IR 3 can replace it. With IR 1+2 failed, set ATT HDG to CAPT 3: the captain keeps attitude and the F/O PFD has none. Land in CONF 3 at VREF + 10 kt; the law becomes DIRECT when the gear goes down.

## 1. What it is
- **Trigger:** This alert triggers when IR 1+2(1+3)(2+3) are failed. Inhibited in flight phases 4 and 8. [FCOM PRO-ABN-NAV P 89/124, PDF 3914]
- **Flight phase inhibition:** phases 4, 8 [FCOM PRO-ABN-NAV P 89/124, PDF 3914]
- Dual NAV IRS failures cause the loss of AP, FD and A/THR, and the flight controls revert to ALTN law. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- (3) in the table: after the faulty IR is set to OFF and ELAC 1 and 2 are reset. [FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 5/20, PDF 1616]
- There is no procedure for IRS 1 + 2 + 3 failure; the ECAM STATUS shows the approach procedure and INOP systems, and the standby instruments are the only attitude, altitude, speed and heading references. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- ATT HDG selector: CAPT 3 — IR 3 replaces IR 1; F/O 3 — IR 3 replaces IR 2. [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]
- IR FAULT light flashing: attitude and heading may be recovered in ATT mode. Steady: the IR is lost. [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]
- In ATT mode the IR gives only attitude and heading (heading entered on the MCDU, reset about every 10 min). Once an IR is set from NAV to ATT or OFF in flight, NAV mode is lost for the rest of the flight; it is recovered only on ground by a complete alignment. [FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101]

## 2. Key limits
- **MAX SPEED:** 320 KT [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- **IR 1+2 FAULT:** ATT HDG CAPT 3 [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
- **FOR LDG:** FLAP LVR 3 [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- **APPR SPD:** VREF + 10 KT [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- **Law:** ALTN (PROT LOST) · DIRECT at L/G DN [FCOM PRO-ABN-NAV P 91/124, PDF 3916]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- AP, FD and A/THR are lost and the flight controls revert to alternate law [FCTM PR-AEP-NAV P 1/20, PDF 478]
**1.2 PF**
- Fly manually with manual thrust; keep a safe flight path first [FCTM AOP-30-30 P 1/6, PDF 82; FCOM PRO-ABN-NAV P 91/124, PDF 3916]
**1.3 PM**
- “NAV IR 1+2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-NAV P 89/124, PDF 3914; PDP Management of abnormal operations, PDF 424]
- Announce the pair shown (1+2, 1+3 or 2+3) [FCOM PRO-ABN-NAV P 89/124, PDF 3914]
- Confirm on the overhead ADIRS panel (IR FAULT lights) and on the PFD/ND flags [FCTM AOP-30-30 P 2/6, PDF 83; FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101; FCOM DSC-34-NAV-20 P 8/10, PDF 2131]
**1.4 PF**
- **If attitude is lost on the PF's PFD** [FCTM AOP-30-30 P 1/6, PDF 82]
  - The FLY task is affected — the captain may re-allocate the PF role [FCTM AOP-30-30 P 1/6, PDF 82]
  - The pilot taking control announces "I have control" and presses the sidestick pb [FCTM AOP-10-30-20 P 1/2, PDF 62]
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- If ADR and IR of the same ADIRU fail together, do the ADR FAULT procedure first [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
- **If NAV IR 1+2 FAULT** [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - ATT HDG SWTG …… CAPT 3 [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - IR 3 (if available) on the CAPT side. Attitude information is lost on the F/O PFD [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
- **If NAV IR 1+3(2+3) FAULT** [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - ATT HDG SWTG …… NORM [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - Attitude information is lost on one side (CAPT or F/O) [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
**2.2 PM**
- “F/CTL ALTN LAW” [FCOM PRO-ABN-NAV P 90/124, PDF 3915; FCTM AOP-30-30 P 2/6, PDF 83]
- Associated procedure F/CTL ALTN LAW (PROT LOST): MAX SPEED 320 KT, maneuver with care — see the F/CTL ALTN LAW brief [FCOM PRO-ABN-NAV P 90/124, PDF 3915; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482]

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
- IR (AFFECTED) MODE SEL …… ATT [QRH 26.04A, PDF 243; FCOM PRO-ABN-NAV P 15/124, PDF 3840]
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

### 5. Approach and landing
**5.1 PF**
- Brief: CONF 3 landing, VREF + 10 kt, landing distance with the LDG DIST PROC; FLS limited to F-APP + RAW [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
**5.2 PM**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
**5.3 PF**
- **At landing gear extension** [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
  - Control reverts to DIRECT LAW in pitch and roll: USE MAN PITCH TRIM [FCOM PRO-ABN-NAV P 91/124, PDF 3916; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]

## 4. Procedure
### NAV IR 1+2(1+3)(2+3) FAULT (FCOM PRO-ABN-NAV)
- *In the case of a simultaneous ADR and IR (same ADIRU) failure, apply the ADR FAULT procedure prior to the IR FAULT procedure.* [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
- **If NAV IR 1+2 FAULT:** [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - ATT HDG SWTG …… CAPT 3 [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - *Set IR 3 (if available) on the CAPT side. Attitude information is lost on the FO PFD.* [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
- **If NAV IR 1+3(2+3) FAULT:** [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - ATT HDG SWTG …… NORM [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
  - *Attitude information is lost on one side (CAPT or FO).* [FCOM PRO-ABN-NAV P 90/124, PDF 3915]
- *ASSOCIATED PROCEDURES: F/CTL ALTN LAW (PROT LOST) — Refer to PRO-ABN-F_CTL F/CTL ALTN LAW* [FCOM PRO-ABN-NAV P 90/124, PDF 3915]

### [QRH] IR ALIGNMENT IN ATT MODE (QRH 26.04A (HS-TX version))
- IR (affected) MODE SEL …… ATT [QRH 26.04A, PDF 243]
- *KEEP SPEED, HEADING, AND FL CONSTANT FOR 30 s* [QRH 26.04A, PDF 243]
- FMS DATA page …… SELECT [QRH 26.04A, PDF 243]
- IRS MONITOR key …… PRESS [QRH 26.04A, PDF 243]
- [SET HDG key] A/C HDG …… ENTER [QRH 26.04A, PDF 243]
- *CROSSCHECK HEADING REGULARLY WITH STBY COMPASS AND UPDATE AS REQUIRED* [QRH 26.04A, PDF 243]

## 5. STATUS
**Limitations**
- MAX SPEED …… 320 KT [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
**Information**
- ALTN LAW : PROT LOST [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- WHEN L/G DN : DIRECT LAW — at landing gear extension, control reverts to direct law in pitch as well as in roll. [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- IR (AFFECTED) MAY BE AVAIL IN ATT — Refer to [QRH] IR ALIGNMENT IN ATT MODE [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- FLS LIMITED TO F–APP + RAW [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- If IR 1 fails, the TCAS may be inoperative (depending on the TCAS manufacturer). If IR 1 is available in ATT mode, the TCAS can be recovered by entering the aircraft magnetic heading into the CDU. [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG: FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- GPWS LDG FLAP 3 …… ON — Displayed when flaps are in CONF 3. [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
**INOP SYS**
- F/CTL PROT [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- IR 1+2(1+3)(2+3) [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- AP 1+2 [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- A/THR [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- YAW DAMPER 1 (if NAV IR 1+3 FAULT) [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- YAW DAMPER 2 (if NAV IR 2+3 FAULT) [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- GPWS TERR (if IR 1 fails) [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- TCAS [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- CAT 2 [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- GLS AUTOLAND [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- STEEP APPR [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- ROW/ROP [FCOM PRO-ABN-NAV P 91/124, PDF 3916]

## 6. QRH and reference tables
### Law reconfiguration — dual IR 
FCOM flight controls law reconfiguration table (NAV rows), same values for HS-TXA..TXF and HS-TXG..TXU.

| Failure | Pitch law | Protection | Roll | Yaw |
|---|---|---|---|---|
| 2 ADR or 2 IR (2nd self detected failed) | ALTN | REDUCED | DIRECT | ALTN |
| 2 IR (2nd not self detected failed) | DIRECT → ALTN (3) | NO → REDUCED (3) | DIRECT | MECH → ALTN (3) |
| 3 IR | DIRECT | NO | DIRECT | MECH |
[FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 5/20, PDF 1616]

## 7. FCTM technique
- The PF usually remains PF, unless the captain re-allocates tasks or a failure impacts the PF's FLY task (e.g. loss of attitude on the PF side). [FCTM AOP-30-30 P 1/6, PDF 82]
- To take control, the pilot clearly announces "I have control" and presses and holds the sidestick pb. [FCTM AOP-10-30-20 P 1/2, PDF 62]
- Reconfiguration law: at high altitude descend to increase the buffet margin (about 4 000 ft below REC MAX ALT); at high speed maneuver with care using small inputs. [FCTM AOP-10-30-20 P 1/2, PDF 62]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| F/CTL ALTN LAW (PROT LOST) | Associated procedure of the dual IR fault. | MAX SPEED 320 KT; MANEUVER WITH CARE (if displayed); Respect stall warnings with TAWS alerts | [FCOM PRO-ABN-NAV P 90/124, PDF 3915; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 10/132, PDF 3483] |
| F/CTL DIRECT LAW | Active once the landing gear is down. | MAN PITCH TRIM USE; MAX SPEED 320/.77; Maneuver and use speed brakes with care | [FCOM PRO-ABN-NAV P 91/124, PDF 3916; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492] |
| [QRH] IR ALIGNMENT IN ATT MODE | STATUS shows IR MAY BE AVAIL IN ATT; apply when the IR FAULT light flashes. | IR (affected) MODE SEL ATT (crosscheck first); Keep speed, heading and FL constant for 30 s; MCDU DATA → IRS MONITOR → SET HDG: enter A/C HDG; Crosscheck heading with STBY compass; update about every 10 min | [QRH 26.04A, PDF 243; FCOM PRO-ABN-NAV P 15/124, PDF 3840; FCOM DSC-34-NAV-10-20 P 2/6, PDF 2101] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- FD loss is stated by the FCTM; the FCOM STATUS INOP SYS lists AP 1+2 and A/THR but not FD. [FCTM PR-AEP-NAV P 1/20, PDF 478; FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- No IR-specific PDP module or callouts; the flow uses the generic ECAM handling. The F/CTL ALTN LAW callout is the ECAM title announced by the PM. [PDP Management of abnormal operations, PDF 424]
- GLS AUTOLAND, STEEP APPR, ROW/ROP and FLS items carry option marks (equipment-dependent). [FCOM PRO-ABN-NAV P 91/124, PDF 3916]
- The HS-TO version of IR ALIGNMENT IN ATT MODE (extra "On ground: T.O SURV pb OFF" line) is not used. [QRH 26.04A, PDF 243]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — NAV IR 1+2(1+3)(2+3) FAULT (HS-TX) | P 89–91/124 | 3914–3916 | 26 MAY 26 |
| QRH | 26.04 IR ALIGNMENT IN ATT MODE | 26.04A | 243 | 26 MAY 26 |
| FCTM | PR-AEP-NAV — ADR/IRS FAULT · AOP-10-30-20 reconfiguration laws | P 1/20 · P 1/2 | 478 · 62 | 26 MAY 26 |
| FCOM | DSC-27-20-20 — law reconfiguration table | P 3/20, P 5/20 | 1614, 1616 | 18 FEB 26 |
| FCOM | DSC-34-NAV-10-20 — ADIRS controls | P 2–3/6 | 2101–2102 | 18 FEB 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
