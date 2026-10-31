# NAV ADR 1+2+3 FAULT · BUSS — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Red warning · no memory items**  
**Applicability:** HS-TXA..TXO, HS-TXP..TXU — ECAM procedure and STATUS: one version for all HS-TX. QRH ALL ADR OFF differs: HS-TXA..TXO also lose both FMS.

Below FL 250, if the speed stays unreliable, the crew turns off all three ADRs. Both PFDs then show the Backup Speed Scale (BUSS) based on angle of attack and the backup altitude scale, GPS altitude. Fly the green band with pitch and thrust. The BUSS cannot be switched back. Do not use speed brakes, and control the cabin pressure manually.

## 1. What it is
- **Trigger:** The three ADRs are failed. Also triggers when the crew turns off all ADRs below FL 250 because speed stays unreliable. [FCOM PRO-ABN-NAV P 38/124, PDF 3863; FCTM PR-AEP-NAV P 20/20, PDF 497]
- **Flight phase inhibition:** phases 1, 4, 8, 10 [FCOM PRO-ABN-NAV P 38/124, PDF 3863; FCTM PR-AEP-NAV P 20/20, PDF 497]
- When activated, the BUSS replaces the normal speed and GPS altitude replaces the barometric altitude scale, on both PFDs, once the crew turns off all ADRs. [FCOM DSC-34-NAV-10-30-10 P 1/4, PDF 2106]
- The BUSS comes from the angle of attack and depends on the slat/flap configuration. [FCOM DSC-34-NAV-10-30-10 P 1/4, PDF 2106]
- Backup altitude scale: current GPS altitude with two amber dashes over the last two digits, a GPS ALT flag, and no vertical speed indication. [FCOM DSC-34-NAV-10-30-10 P 3/4, PDF 2108; PDP Unreliable speed indication, PDF 563]
- Speed brakes change the speed-to-AOA relationship, so the BUSS may then give erroneous data. [FCTM PR-AEP-NAV P 19/20, PDF 496]

## 2. Key limits
- **Use the BUSS:** Below FL 250 [FCOM PRO-ABN-NAV P 3/124, PDF 3828; FCTM PR-AEP-NAV P 18/20, PDF 495]
- **Speed:** FLY THE GREEN [FCOM PRO-ABN-NAV P 39/124, PDF 3864; QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **Speed brakes:** DO NOT USE [FCOM PRO-ABN-NAV P 40/124, PDF 3865; FCTM PR-AEP-NAV P 19/20, PDF 496]
- **Landing configuration:** FLAP LVR 3 · gravity gear extension at FLAP 2 [FCOM PRO-ABN-NAV P 11/124, PDF 3836; FCOM PRO-ABN-NAV P 13/124, PDF 3838; QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **Approach speed:** BUSS target speed (green triangle) [FCOM PRO-ABN-NAV P 11/124, PDF 3836; FCOM PRO-ABN-NAV P 14/124, PDF 3839; QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **Cabin V/S target:** Climb 500 ft/min · descent 300 ft/min [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]

## 3. Flow (PF / PM)
### 1. Turn off all ADRs (from Unreliable speed)
**1.1 PF + PM**
- Below FL 250, the affected ADR cannot be identified, or all speeds stay unreliable [FCOM PRO-ABN-NAV P 3/124, PDF 3828; FCTM PR-AEP-NAV P 18/20, PDF 495; PDP Unreliable speed indication, PDF 562]
**1.2 PM**
- ALL ADR pbs …… OFF [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- Use the pushbuttons, not the rotary selector. The BUSS activation is not reversible [FCTM PR-AEP-NAV P 2/20, PDF 479; FCOM DSC-34-NAV-10-30-10 P 1/4, PDF 2106]

### 2. ECAM actions
**2.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**2.2 PM**
- “NAV ADR 1+2+3 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-NAV P 39/124, PDF 3864; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**2.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 3. ECAM procedure
**3.1 PF**
- AP+FD …… OFF [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- A/THR …… OFF [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- AP/FD and A/THR must stay disconnected while the BUSS is active; alternate law [FCTM PR-AEP-NAV P 19/20, PDF 496]
**3.2 PM**
- PROBE/WINDOW HEAT …… ON [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- ADR 1+2+3 P/B …… OFF [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- GPWS TERR FAULT and GPWS SYS FAULT lights can come on: the crew should then switch off the GPWS TERR and GPWS SYS pb-sw [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
**3.3 PF**
- SPD …… FLY THE GREEN [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- Adjust pitch and thrust to fly the green area. The STALL WARNING remains operative [FCTM PR-AEP-NAV P 19/20, PDF 496; FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- **The BUSS does not react to longitudinal stick input** [FCOM PRO-ABN-NAV P 39/124, PDF 3864; FCTM PR-AEP-NAV P 19/20, PDF 496]
  - Disregard it and use the pitch/thrust tables [FCOM PRO-ABN-NAV P 39/124, PDF 3864; FCTM PR-AEP-NAV P 19/20, PDF 496; PDP Unreliable speed indication, PDF 563]
**3.4 PM**
- STBY INST …… MAY BE UNREL [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- ADR 3 and the standby speed use the same probes [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- ALL ADR OFF PROC …… APPLY [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- Keep the ECAM displayed and apply the QRH procedure [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 431]

### 4. QRH ALL ADR OFF
**4.1 PF**
- SPEED …… FLY THE GREEN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- For flaps retraction, fly the top of the green area [FCOM PRO-ABN-NAV P 11/124, PDF 3836; FCOM PRO-ABN-NAV P 13/124, PDF 3838]
**4.2 PM**
- **[HS-TXA..TXO]** **WHEN ALL ADR OFF BOTH FMS LOST** [FCOM PRO-ABN-NAV P 13/124, PDF 3838; QRH 26.01B, PDF 233]
  - BACK UP NAV …… USE [FCOM PRO-ABN-NAV P 13/124, PDF 3838; QRH 26.01B, PDF 233]
  - NAV B/UP prompt on the MCDU MENU page. USE RMP FOR NAVAID TUNING [FCOM PRO-ABN-NAV P 13/124, PDF 3838; QRH 26.01B, PDF 233]
- PFD ALTITUDE: GPS [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- TCAS & ATC ALT RPTG INOP [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- CABIN PRESS MODE SEL …… MAN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- MAN V/S CTL …… AS RQRD [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- LDG DIST PROC …… APPLY [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]

### 5. Continue ECAM → STATUS
**5.1 PM**
- “CLEAR NAV ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**5.2 PF**
- “CLEAR NAV” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**5.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**5.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 6. Approach
**6.1 PF**
- SPEED …… FLY THE GREEN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- Early stabilized approach. Change configuration wings level; before extending the next flap setting, fly the bottom of the green band [FCTM PR-AEP-NAV P 20/20, PDF 497; FCOM PRO-ABN-NAV P 11/124, PDF 3836; FCOM PRO-ABN-NAV P 13/124, PDF 3838]
- APPR SPEED: fly the BUSS target speed, the green triangle shows VAPP [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233; PDP Unreliable speed indication, PDF 563]
**6.2 PM**
- FOR LDG …… FLAP LVR 3 [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- GPWS LDG FLAP 3 …… ON [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **When FLAP 2** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - LDG GEAR GRVTY EXTN handcrank …… PULL AND TURN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **When L/G downlocked** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - L/G lever …… DOWN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - GEAR DOWN indications …… CHECK [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - L/G DOORS REMAIN OPEN. Direct law in pitch and roll at gear extension [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233; FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- **During final approach** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - MAN V/S CTL …… FULL UP [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- Before door opening: CHECK ΔP ZERO [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]

## 4. Procedure
### NAV ADR 1+2+3 FAULT — ECAM (FCOM PRO-ABN-NAV)
- *In case of a simultaneous ADR and IR (same ADIRU) failure, apply the ADR FAULT procedure prior to the IR FAULT procedure.* [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- AP+FD …… OFF [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- A/THR …… OFF [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- PROBE/WINDOW HEAT …… ON [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- ADR 1+2+3 P/B …… OFF [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- *The STALL WARNING remains operative.* [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- SPD …… FLY THE GREEN [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- *If the BUSS does not react to longitudinal stick input when flying the green area of the speed scale, the flight crew must disregard the BUSS and use pitch/thrust table.* [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- STBY INST …… MAY BE UNREL — ADR3 and STBY speeds use the data of the same probes. [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- ALL ADR OFF PROC …… APPLY [FCOM PRO-ABN-NAV P 39/124, PDF 3864]
- *Associated: F/CTL ALTN LAW (PROT LOST).* [FCOM PRO-ABN-NAV P 39/124, PDF 3864]

### ALL ADR OFF — QRH (QRH 26.01)
- SPEED …… FLY THE GREEN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- *If the BUSS does not react to longitudinal stick input when flying the green area of the speed scale, the flight crew must disregard the BUSS and use pitch/thrust tables.* [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **[HS-TXA..TXO]** **WHEN ALL ADR OFF BOTH FMS LOST** [QRH 26.01B, PDF 233]
  - **[HS-TXA..TXO]** BACK UP NAV …… USE [QRH 26.01B, PDF 233]
  - **[HS-TXA..TXO]** *USE RMP FOR NAVAID TUNING* [QRH 26.01B, PDF 233]
- *PFD ALTITUDE: GPS* [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- *TCAS & ATC ALT RPTG INOP* [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- CABIN PRESS MODE SEL …… MAN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- MAN V/S CTL …… AS RQRD — Target CAB PRESS V/S: climb 500 ft/min, descent 300 ft/min. [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- LDG DIST PROC …… APPLY [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- **For approach:** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - SPEED …… FLY THE GREEN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - FOR LDG …… FLAP LVR 3 [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - GPWS LDG FLAP 3 …… ON [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - *APPR SPEED: BUSS TARGET SPEED. During approach, BUSS TARGET SPEED (green triangle) indicates VAPP.* [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - **When FLAP 2:** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
    - LDG GEAR GRVTY EXTN handcrank …… PULL AND TURN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - **When L/G downlocked:** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
    - L/G lever …… DOWN [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
    - GEAR DOWN indications …… CHECK [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
    - *L/G DOORS REMAIN OPEN* [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
    - **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to OPS Fuel Penalty Factors/ECAM Alert Table. [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
  - **During final approach:** [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
    - MAN V/S CTL …… FULL UP [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]
- *Before door opening: CHECK ΔP ZERO* [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]

## 5. STATUS
**Limitations**
- MANEUVER WITH CARE [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- SPD BRK DO NOT USE [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- STBY INST MAY BE UNREL [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
**Information**
- ALTN LAW: PROT LOST. WHEN L/G DN: DIRECT LAW (pitch and roll) [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- LDG …… GRVTY EXTN [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
**INOP SYS**
- REAC W/S DET [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- PRED W/S DET [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- F/CTL PROT [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- ADR 1+2+3 [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- STEEP APPR [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- RUD TRV LIM [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- AP 1+2 [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- A/THR [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- CAB PR 1+2 [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- GPWS [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- GPWS TERR [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- ATC/XPDR 1 [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- ATC/XPDR 2 [FCOM PRO-ABN-NAV P 40/124, PDF 3865]
- ROW/ROP [FCOM PRO-ABN-NAV P 40/124, PDF 3865]

## 6. QRH and reference tables
### Backup Speed Scale (BUSS) 
Top to bottom on the PFD.

| Band | Meaning |
|---|---|
| Red FAST | Excessive speed, decreasing the margin to the maximum structural speed |
| Amber FAST | Excessive speed, keeping an appropriate margin to the maximum structural speed |
| Green | Safe speed range |
| Green triangle | Optimum target speed; in approach, the approach target speed |
| Yellow line | Current speed |
| Amber SLOW | Too low, keeping an appropriate margin to the stall speed |
| Red SLOW | Too low, reducing the margin to the stall speed |
[FCOM DSC-34-NAV-10-30-10 P 2/4, PDF 2107; FCOM DSC-34-NAV-10-30-10 P 3/4, PDF 2108]

### Cabin altitude target 
With manual cabin pressure control.

| Aircraft cruise FL | CAB ALT target (ft) |
|---|---|
| 410 | 8000 |
| 350 | 7000 |
| 300 | 5500 |
| 250 | 3000 |
| <200 | 0 |
[QRH 26.01A, PDF 232; QRH 26.01B, PDF 233]

## 7. FCTM technique
- Before retracting the next flap setting fly the upper part of the green band; before extending it, the lower part. This limits excursions into the amber zones. [FCTM PR-AEP-NAV P 20/20, PDF 497]
- Any longitudinal stick input changes the AOA, so the BUSS must move. If it does not, disregard it. [FCTM PR-AEP-NAV P 19/20, PDF 496]
- While the BUSS is active: cabin pressure controlled manually, HUD not used if installed, FPV available on one or both PFDs depending on the ADIRS standard. [FCTM PR-AEP-NAV P 19/20, PDF 496]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| UNRELIABLE SPEED INDICATION | Leads here below FL 250 when speed stays unreliable | See the Unreliable speed brief | [FCOM PRO-ABN-NAV P 3/124, PDF 3828; FCTM PR-AEP-NAV P 18/20, PDF 495] |
| F/CTL ALTN LAW (PROT LOST) | Associated procedure | See the F/CTL ALTN LAW brief | [FCOM PRO-ABN-NAV P 39/124, PDF 3864] |
| F/CTL DIRECT LAW | Control reverts to direct law at gear extension | See the F/CTL DIRECT LAW brief | [FCOM PRO-ABN-NAV P 40/124, PDF 3865] |

## 9. HS-TX differences
| Topic | HS-TXA..TXO | HS-TXP..TXU | Ref |
|---|---|---|---|
| FMS after all ADRs off | WHEN ALL ADR OFF BOTH FMS LOST · BACK UP NAV USE · USE RMP FOR NAVAID TUNING | No such lines in the QRH ALL ADR OFF | [QRH 26.01A, PDF 232; QRH 26.01B, PDF 233; FCOM PRO-ABN-NAV P 11/124, PDF 3836; FCOM PRO-ABN-NAV P 13/124, PDF 3838] |

## 10. Gaps and omissions
- "BAS" is not an abbreviation in the supplied manuals: the FCOM says Backup Altitude Scale and the PDP says Back-Up Altitude Scale. [FCOM DSC-34-NAV-10-30-10 P 3/4, PDF 2108; PDP Unreliable speed indication, PDF 562]
- PDP mentions a "reversible BUSS (if installed)". The FCOM states activation is not reversible for all HS-TX; the reversible modification is listed for HS-TO only. This brief follows the FCOM. [FCOM DSC-34-NAV-10-30-10 P 1/4, PDF 2106; FCOM PLP-LOM P 25/58, PDF 52; PDP Unreliable speed indication, PDF 562]
- The flow order and PF/PM split of the QRH part are arranged from the QRH lines and AOP-30-30; no PDP slide gives the turns. [QRH 26.01A, PDF 232; FCTM AOP-30-30 P 2/6, PDF 83]
- HS-TO versions omitted (FCOM P 41–42/124, QRH 26.01C). [FCOM PRO-ABN-NAV P 40/124, PDF 3865]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — NAV ADR 1+2+3 FAULT | P 38–40/124 | 3863–3865 | 26 MAY 26 |
| FCOM | PRO-ABN-NAV — [QRH] ALL ADR OFF | P 11–14/124 | 3836–3839 | 26 MAY 26 |
| FCOM | DSC-34-NAV-10-30-10 — Backup Speed/Altitude Scale | P 1–3/4 | 2106–2108 | 21 MAY 25 |
| QRH | 26.01 ALL ADR OFF | 26.01A–B | 232–233 | 26 MAY 26 |
| FCTM | PR-AEP-NAV — Backup Speed Scale | P 18–20/20 | 495–497 | 26 MAY 26 |
| PDP | Unreliable speed indication (XFTDA6UNRASPD01) | — | 562–563 | JUN 2023 |
