# SMOKE FWD CARGO SMOKE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (the HS-TO version is not used).

A red warning with red LAND ASAP. Smoke is detected in the forward cargo hold, which is built to contain a fire, so the smoke is not felt in the cockpit; only the SMOKE light on the CARGO SMOKE panel confirms it. Cabin fans OFF, discharge AGENT 1 (guarded pb, crosscheck first) and AGENT 2 after 60 min, and divert. Expect the warning to stay after discharge. On the ground, the passengers disembark before any cargo door is opened.

## 1. What it is
- **Trigger:** This alert triggers when smoke in the FWD cargo compartment is detected. Inhibited in flight phases 4, 5, 7 and 8. [FCOM PRO-ABN-SMOKE P 39/50, PDF 3996]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-SMOKE P 39/50, PDF 3996]
- The cargo compartments are designed to be air-tight and fireproof to contain a fire, and the cargo ventilation prevents cargo smoke from reaching the cockpit/cabin. The crew can only confirm the alert with the SMOKE light on the CARGO SMOKE panel. [FCTM PR-AEP-SMOKE P 9/10, PDF 506]
- The forward compartment has two smoke detectors on two loops. The warning needs both detectors of a cavity (or one, if the other is inoperative). [FCOM DSC-26-50-10 P 3/8, PDF 1546]
- The DISCH pb fires the squibs of the fire bottles: bottle 1 discharges in about 60 s; a flow metering system controls bottle 2 for at least 135 min. BTL 1(2) light amber when empty. [FCOM DSC-26-50-10 P 5/8, PDF 1548]
- The DISCH sw is guarded. The DISCH AGENT 2 light comes on amber 60 min after AGENT 1 and goes off when the AGENT 2 squib is ignited. [FCOM DSC-26-50-20 P 3/4, PDF 1554]

## 2. Key limits
- **LAND ASAP:** Red — nearest airport with a safe landing [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCTM AOP-30-10 P 2/2, PDF 79]
- **AGENT 1:** DISCH (bottle 1 empties in about 60 s) [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCOM DSC-26-50-10 P 5/8, PDF 1548]
- **AGENT 2:** DISCH after 60 min [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCOM PRO-ABN-SMOKE P 38/50, PDF 3995; FCOM DSC-26-50-20 P 3/4, PDF 1554]
- **Cargo doors:** Not opened before PAX DISEMBARK [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCTM PR-AEP-SMOKE P 9/10, PDF 506]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “SMOKE FWD CARGO SMOKE” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-SMOKE P 39/50, PDF 3996; PDP Management of abnormal operations, PDF 424]
- Confirm with the FWD SMOKE light on the CARGO SMOKE panel — cargo smoke is not perceptible from the cockpit or cabin [FCTM PR-AEP-SMOKE P 9/10, PDF 506; FCTM AOP-30-30 P 2/6, PDF 83]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
- LAND ASAP (red): land as soon as possible at the nearest airport where a safe landing can be made — anticipate the diversion [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCTM AOP-30-10 P 2/2, PDF 79; FCTM PR-AEP-SMOKE P 1/10, PDF 498]

### 2. ECAM actions (in flight)
**2.1 PM**
- CAB FANS …… OFF [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
**2.2 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
- Guarded DISCH sw: point to it and ask confirmation [FCOM DSC-26-50-20 P 3/4, PDF 1554; FCTM AOP-30-20 P 1/2, PDF 80]
**2.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
**2.4 PM**
- Press the FWD DISCH pb (AGENT 1) — the amber DISCH light comes on within 60 s when the bottle is fully discharged [FCOM DSC-26-50-20 P 3/4, PDF 1554; FCOM DSC-26-50-10 P 5/8, PDF 1548]
- **AFT 60MIN** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - The DISCH AGENT 2 light comes on amber 60 min after AGENT 1; the SMOKE DISCH AGENT 2 alert triggers at 60 min if the cargo smoke alert is no longer displayed [FCOM DSC-26-50-20 P 3/4, PDF 1554; FCOM PRO-ABN-SMOKE P 38/50, PDF 3995]
- Expect the SMOKE FWD CARGO SMOKE alert to remain after agent discharge, even if the smoke source is extinguished. Gases from the smoke source still remain, and smoke detectors are also sensitive to the extinguishing agent. [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCTM PR-AEP-SMOKE P 9/10, PDF 506]
- **WHEN ON GROUND BEFORE OPEN CRG DOORS** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]

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

### 5. On ground
**5.1 PF**
- Order the ground crew not to open the door of the affected cargo compartment until the passengers have disembarked and fire services are present [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCTM PR-AEP-SMOKE P 9/10, PDF 506]
**5.2 PM**
- **If the alert appears on ground with FWD CRG CLOSED** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - Ensure the cargo door is closed before discharging [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - **AFT 60MIN** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - **BEFORE OPEN CRG DOORS** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- **If the alert appears on ground with the cargo door open** [FCTM PR-AEP-SMOKE P 9/10, PDF 506]
  - Do not initiate an AGENT DISCHARGE; ask the ground crew to investigate and eliminate the smoke source [FCTM PR-AEP-SMOKE P 9/10, PDF 506]

## 4. Procedure
### SMOKE FWD CARGO SMOKE (FCOM PRO-ABN-SMOKE (HS-TX))
- **LAND ASAP (red)** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- FWD ISOL VALVE …… OFF — If FWD ISOL VALVE is not automatically closed. [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- *FWD ISOL VALVE is an "if installed" item: the If Installed table lists it as not installed (see Gaps).* [FCOM GEN P 26/78, PDF 119]
- CAB FANS …… OFF [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- **On ground:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - **IF FWD CRG CLOSED:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - *Order the ground crew not to open the door of the affected cargo compartment, unless the passengers have disembarked and fire services are present. Also ensure that the FWD Cargo Door is closed before discharging the extinguishing agent.* [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - **AFT 60MIN:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
      - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
      - *Expect the SMOKE FWD CARGO SMOKE alert to remain after agent discharge, even if the smoke source is extinguished. Gases from the smoke source still remain, and smoke detectors are also sensitive to the extinguishing agent.* [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - **BEFORE OPEN CRG DOORS:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
      - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- **In flight:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - AGENT 1 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - **AFT 60MIN:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - *Expect the SMOKE FWD CARGO SMOKE alert to remain after agent discharge, even if the smoke source is extinguished. Gases from the smoke source still remain, and smoke detectors are also sensitive to the extinguishing agent.* [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
  - **WHEN ON GROUND BEFORE OPEN CRG DOORS:** [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
    - PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997]
- *On ground, the warning may be triggered due to a high level of humidity or insecticide spraying. If the smoke is not visually confirmed and the warning is no more displayed: deactivate the smoke detection system (SDCU C/Bs), reset the cargo ventilation system (AIR COND/AFT CARGO/VENT/CTL & MONG C/B), and at cargo doors closure reactivate SDCU 1 and 2.* [FCOM PRO-ABN-SMOKE P 41/50, PDF 3998]

### SMOKE DISCH AGENT 2 (FCOM PRO-ABN-SMOKE (HS-TX))
- *This alert triggers 60 minutes after discharging the first extinguisher bottle in case the SMOKE FWD(AFT) CARGO SMOKE alerts are not triggered.* [FCOM PRO-ABN-SMOKE P 38/50, PDF 3995]
- AGENT 2 …… DISCH [FCOM PRO-ABN-SMOKE P 38/50, PDF 3995]

## 5. STATUS
**Information**
- In flight: WHEN ON GROUND BEFORE OPEN CRG DOORS: PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 41/50, PDF 3998]
- On ground: BEFORE OPEN CRG DOORS: PAX …… DISEMBARK [FCOM PRO-ABN-SMOKE P 41/50, PDF 3998]
**INOP SYS**
- FWD CRG VENT [FCOM PRO-ABN-SMOKE P 41/50, PDF 3998]
- FWD CRG HEAT [FCOM PRO-ABN-SMOKE P 41/50, PDF 3998]

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
- The FCOM procedure prints the line FWD ISOL VALVE OFF, marked "if installed". The If Installed table (GEN P 26/78) lists FWD Cargo Ventilation and the FWD ISOL Valve as not installed, while GEN P 14/78 lists the general "Cargo ventilation system / Cargo isolation valves" as installed. Confirmed by the user: the flow leaves the line out; the procedure section keeps it verbatim. [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCOM GEN P 26/78, PDF 119; FCOM GEN P 14/78, PDF 107]
- STATUS prints FWD CRG VENT and FWD CRG HEAT, also "if installed"; the same table lists them as not installed. They are kept verbatim. [FCOM PRO-ABN-SMOKE P 41/50, PDF 3998; FCOM GEN P 26/78, PDF 119]
- The FCOM notes on recovering FWD cargo ventilation for livestock apply only to aircraft with FWD Cargo Ventilation and are not used here. [FCOM PRO-ABN-SMOKE P 40/50, PDF 3997; FCOM PRO-ABN-SMOKE P 41/50, PDF 3998]
- No PDP module covers cargo smoke; the flow uses the generic ECAM handling. [PDP Management of abnormal operations, PDF 424]
- The HS-TO version (FCOM P 42–43/50) is not used. [FCOM PRO-ABN-SMOKE P 39/50, PDF 3996]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-SMOKE — SMOKE FWD CARGO SMOKE, SMOKE DISCH AGENT 2 (HS-TX) | P 39–41/50, 38/50 | 3996–3998, 3995 | 14 JUL 26 |
| FCTM | PR-AEP-SMOKE — introduction, cargo smoke | P 1/10, 9/10 | 498, 506 | 24 NOV 25 |
| FCOM | DSC-26-50 — cargo smoke detection, extinguishing, panel | DSC-26-50-10 P 3/8, 5/8; DSC-26-50-20 P 3/4 | 1546, 1548, 1554 | 18 FEB 26 |
| FCOM | GEN — If Installed table | P 14/78, 23/78, 26/78 | 107, 116, 119 | 14 JUL 26 |
| PDP | Smoke (XFTDA1SMOKE0001) | SMOKE ECAM alerts | 535 | JAN 2024 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
