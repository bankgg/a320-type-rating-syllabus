# SMOKE AFT CARGO SMOKE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (the HS-TO version is not used).

A red warning with red LAND ASAP. Smoke is detected in the aft cargo hold, which is built to contain a fire, so the smoke is not felt in the cockpit; only the SMOKE light on the CARGO SMOKE panel confirms it. Close the aft isolation valve if it did not close by itself, cabin fans OFF, discharge AGENT 1 (guarded pb, crosscheck first) and AGENT 2 after 60 min, and divert. Expect the warning to stay after discharge. On the ground, the passengers disembark before any cargo door is opened.

## 1. What it is
- **Trigger:** This alert triggers when smoke in the AFT cargo compartment is detected. Inhibited in flight phases 4, 5, 7 and 8. [FCOM PRO-ABN-SMOKE P 31/50, PDF 3988]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-SMOKE P 31/50, PDF 3988]
- The cargo compartments are designed to be air-tight and fireproof to contain a fire, and the cargo ventilation prevents cargo smoke from reaching the cockpit/cabin. The crew can only confirm the alert with the SMOKE light on the CARGO SMOKE panel. [FCTM PR-AEP-SMOKE P 9/10, PDF 506]
- The aft compartment has four smoke detectors on two loops. The warning needs both detectors of a cavity (or one, if the other is inoperative). The isolation valves close and the extraction fan stops automatically. [FCOM DSC-26-50-10 P 3/8, PDF 1546]
- The DISCH pb fires the squibs of the fire bottles: bottle 1 discharges in about 60 s; a flow metering system controls bottle 2 for at least 135 min. BTL 1(2) light amber when empty. [FCOM DSC-26-50-10 P 5/8, PDF 1548]
- The DISCH sw is guarded. The DISCH AGENT 2 light comes on amber 60 min after AGENT 1 and goes off when the AGENT 2 squib is ignited. [FCOM DSC-26-50-20 P 3/4, PDF 1554]

## 2. Key limits
- **LAND ASAP:** Red — nearest airport with a safe landing [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCTM AOP-30-10 P 2/2, PDF 79]
- **AGENT 1:** DISCH (bottle 1 empties in about 60 s) [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCOM DSC-26-50-10 P 5/8, PDF 1548]
- **AGENT 2:** DISCH after 60 min [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCOM PRO-ABN-SMOKE P 38/50, PDF 3995; FCOM DSC-26-50-20 P 3/4, PDF 1554]
- **Cargo doors:** Not opened before PAX DISEMBARK [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCTM PR-AEP-SMOKE P 9/10, PDF 506]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “SMOKE AFT CARGO SMOKE” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-SMOKE P 31/50, PDF 3988; PDP Management of abnormal operations, PDF 424]
- Confirm with the AFT SMOKE light on the CARGO SMOKE panel — cargo smoke is not perceptible from the cockpit or cabin [FCTM PR-AEP-SMOKE P 9/10, PDF 506; FCTM AOP-30-30 P 2/6, PDF 83]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
- LAND ASAP (red): land as soon as possible at the nearest airport where a safe landing can be made — anticipate the diversion [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCTM AOP-30-10 P 2/2, PDF 79; FCTM PR-AEP-SMOKE P 1/10, PDF 498]

### 2. ECAM actions (in flight)
**2.1 PM**
- AFT ISOL VALVE …… OFF [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- If the AFT ISOL VALVE is not automatically closed [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCOM DSC-26-50-10 P 3/8, PDF 1546]
- CAB FANS …… OFF [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
**2.2 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
- Guarded DISCH sw: point to it and ask confirmation [FCOM DSC-26-50-20 P 3/4, PDF 1554; FCTM AOP-30-20 P 1/2, PDF 80]
**2.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
**2.4 PM**
- Press the AFT DISCH pb (AGENT 1) — the amber DISCH light comes on within 60 s when the bottle is fully discharged [FCOM DSC-26-50-20 P 3/4, PDF 1554; FCOM DSC-26-50-10 P 5/8, PDF 1548]
- **AFT 60MIN** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - The DISCH AGENT 2 light comes on amber 60 min after AGENT 1; the SMOKE DISCH AGENT 2 alert triggers at 60 min if the cargo smoke alert is no longer displayed [FCOM DSC-26-50-20 P 3/4, PDF 1554; FCOM PRO-ABN-SMOKE P 38/50, PDF 3995]
- Expect the SMOKE AFT CARGO SMOKE alert to remain after agent discharge, even if the smoke source is extinguished. Gases from the smoke source still remain, and smoke detectors are also sensitive to the extinguishing agent. [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCTM PR-AEP-SMOKE P 9/10, PDF 506]
- **WHEN ON GROUND BEFORE OPEN CRG DOORS** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]

### 3. STATUS
**3.1 PM**
- “CLEAR SMOKE ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR SMOKE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

### 4. Diversion
**4.1 PF**
- Inform ATC, cabin crew and passengers; divert to the nearest suitable airport [PDP Management of abnormal operations, PDF 428; FCTM AOP-30-10 P 2/2, PDF 79]
- Cargo temperature is unreliable once the isolation valves are closed (no cargo ventilation) [FCTM PR-AEP-SMOKE P 9/10, PDF 506]

### 5. On ground
**5.1 PF**
- Order the ground crew not to open the door of the affected cargo compartment until the passengers have disembarked and fire services are present [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989; FCTM PR-AEP-SMOKE P 9/10, PDF 506]
**5.2 PM**
- **If the alert appears on ground with AFT CRG CLOSED** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - Ensure the cargo door is closed before discharging [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - **AFT 60MIN** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - **BEFORE OPEN CRG DOORS** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- **If the alert appears on ground with the cargo door open** [FCTM PR-AEP-SMOKE P 9/10, PDF 506]
  - Do not initiate an AGENT DISCHARGE; ask the ground crew to investigate and eliminate the smoke source [FCTM PR-AEP-SMOKE P 9/10, PDF 506]

## 4. Procedure
### SMOKE AFT CARGO SMOKE (FCOM PRO-ABN-SMOKE (HS-TX))
- **LAND ASAP (red)** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- AFT ISOL VALVE …… OFF — If AFT ISOL VALVE is not automatically closed. [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- CAB FANS …… OFF [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- **On ground:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - **IF AFT CRG CLOSED:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - *Order the ground crew not to open the door of the affected cargo compartment, unless the passengers have disembarked and fire services are present. Also ensure that the cargo door is closed before discharging the extinguishing agent.* [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - **AFT 60MIN:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
      - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
      - *Expect the SMOKE AFT CARGO SMOKE alert to remain after agent discharge, even if the smoke source is extinguished. Gases from the smoke source still remain, and smoke detectors are also sensitive to the extinguishing agent.* [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - **BEFORE OPEN CRG DOORS:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
      - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- **In flight:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - **AFT 60MIN:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - *Expect the SMOKE AFT CARGO SMOKE alert to remain after agent discharge, even if the smoke source is extinguished. Gases from the smoke source still remain, and smoke detectors are also sensitive to the extinguishing agent.* [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
  - **WHEN ON GROUND BEFORE OPEN CRG DOORS:** [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
    - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- *On ground, the warning may be triggered due to a high level of humidity or insecticide spraying. If the smoke is not visually confirmed and the warning is no more displayed: deactivate the smoke detection system (SDCU C/Bs), reset the cargo ventilation system (AIR COND/AFT CARGO/VENT/CTL & MONG C/B), and at cargo doors closure reactivate SDCU 1 and 2.* [FCOM PRO-ABN-SMOKE P 33/50, PDF 3990]

### SMOKE DISCH AGENT 2 (FCOM PRO-ABN-SMOKE (HS-TX))
- *This alert triggers 60 minutes after discharging the first extinguisher bottle in case the SMOKE FWD(AFT) CARGO SMOKE alerts are not triggered.* [FCOM PRO-ABN-SMOKE P 38/50, PDF 3995]
- AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 38/50, PDF 3995]

## 5. STATUS
**Information**
- In flight: WHEN ON GROUND BEFORE OPEN CRG DOORS: PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 33/50, PDF 3990]
- On ground: BEFORE OPEN CRG DOORS: PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 33/50, PDF 3990]
**INOP SYS**
- L+R CAB FAN [FCOM PRO-ABN-SMOKE P 33/50, PDF 3990]
- AFT CRG VENT [FCOM PRO-ABN-SMOKE P 33/50, PDF 3990]
- AFT CRG HEAT [FCOM PRO-ABN-SMOKE P 33/50, PDF 3990]

## 7. FCTM technique
- An immediate diversion should be considered as soon as smoke/fumes are detected. If the source is not immediately obvious, accessible and extinguishable, divert without delay. [FCTM PR-AEP-SMOKE P 1/10, PDF 498]
- Guarded controls are crosschecked by both pilots before acting in flight. [FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
- If smoke/fumes become perceptible in the cockpit or cabin, or any doubt exists about the smoke origin, apply the [QRH] SMOKE / FUMES / AVNCS SMOKE procedure. [FCTM PR-AEP-SMOKE P 1/10, PDF 498; PDP Smoke, PDF 535]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] SMOKE / FUMES / AVNCS SMOKE | If any doubt exists about the smoke origin, or smoke/fumes are perceptible. | LAND ASAP; immediate actions; Diversion and descent to FL 100 / MEA-MORA if the source is not isolated; Boxed items at any time: REMOVAL OF SMOKE / FUMES, ELEC EMER CONFIG, immediate landing | [FCTM PR-AEP-SMOKE P 3/10, PDF 500; PDP Smoke, PDF 535; PDP Smoke, PDF 538] |
| SMOKE DISCH AGENT 2 | Reminder 60 min after AGENT 1 when the cargo smoke alert has stopped. | AGENT 2 DISCH | [FCOM PRO-ABN-SMOKE P 38/50, PDF 3995] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- "AFT/BULK CRG SMOKE" is not an HS-TX alert title; the THA FCOM gives SMOKE AFT CARGO SMOKE for all HS-TX. [FCOM PRO-ABN-SMOKE P 31/50, PDF 3988]
- The procedure does not call for an evacuation; it requires PAX DISEMBARK before opening the cargo doors. [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- FCOM note 1 (recovering aft cargo ventilation for livestock) applies only to aircraft with the AFT cargo ventilation option and is not used here. [FCOM PRO-ABN-SMOKE P 32/50, PDF 3989]
- No PDP module covers cargo smoke; the flow uses the generic ECAM handling. [PDP Management of abnormal operations, PDF 424]
- The HS-TO version (FCOM P 34–36/50) is not used. [FCOM PRO-ABN-SMOKE P 31/50, PDF 3988]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-SMOKE — SMOKE AFT CARGO SMOKE, SMOKE DISCH AGENT 2 (HS-TX) | P 31–33/50, 38/50 | 3988–3990, 3995 | 14 JUL 26 |
| FCTM | PR-AEP-SMOKE — introduction, cargo smoke | P 1/10, 9/10 | 498, 506 | 24 NOV 25 |
| FCOM | DSC-26-50 — cargo smoke detection, extinguishing, panel | DSC-26-50-10 P 3/8, 5/8; DSC-26-50-20 P 3/4 | 1546, 1548, 1554 | 18 FEB 26 |
| PDP | Smoke (XFTDA1SMOKE0001) | SMOKE ECAM alerts | 535 | JAN 2024 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
