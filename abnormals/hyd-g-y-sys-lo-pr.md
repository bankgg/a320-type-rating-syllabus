# HYD G+Y SYS LO PR — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items · QRH summary**  
**Applicability:** all HS-TX — One FCOM procedure for all HS-TX.

A red warning with red LAND ASAP: green and yellow hydraulics are lost. The FCTM says a MAYDAY should be declared, and the ECAM actions should be completed before the approach. No AP, alternate law with protections lost, no flaps and no stabilizer. The key point: stabilize at VAPP in CONF 3 before the gravity gear extension, because direct law then freezes the pitch trim reference and the manual trim is unusable. No reversers, no nosewheel steering, and braking on the yellow accumulator only.

## 1. What it is
- **Trigger:** This alert triggers when the green and yellow systems pressure ≤1 450 PSI (the alert resets if pressure ≥1 750 PSI). [FCOM PRO-ABN-HYD P 62/76, PDF 3751]
- **Flight phase inhibition:** phases 4, 5 [FCOM PRO-ABN-HYD P 62/76, PDF 3751]
- The stabilizer is lost. In alternate law, the auto trim function is provided through the elevators. At landing gear extension, switching to direct law, the auto trim is lost, and the mean elevator position at that time is memorized and becomes the reference for the centered sidestick position. [FCTM PR-AEP-HYD P 3/4, PDF 440]
- The PTU must be switched off without delay when required by the ECAM for reservoir low level, low air pressure (only if pressure fluctuates) or overheat, to avoid a PTU overheat that may lead to the loss of the second circuit. [FCTM PR-AEP-HYD P 1/4, PDF 438]
- Pitch: with HYD G+Y, alternate law has reduced protections; direct law applies in roll; yaw is mechanical. [FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 5/20, PDF 1616]

## 2. Key limits
- **MAX SPEED:** 320/0.77 [FCOM PRO-ABN-HYD P 64/76, PDF 3753; QRH 23.03A, PDF 212]
- **MAX FL:** 4000 FT below REC MAX FL [QRH 23.03A, PDF 212]
- **For landing:** FLAP LVR 3 · VREF + 25 KT · GPWS FLAP MODE OFF [FCOM PRO-ABN-HYD P 64/76, PDF 3753; FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- **L/G gravity extension:** When CONF 3 and VAPP [FCOM PRO-ABN-HYD P 64/76, PDF 3753; QRH 23.03A, PDF 212]
- **Braking:** BRK Y ACCU PR ONLY: 7 applications · MAX BRK PR 1 000 PSI [FCOM PRO-ABN-HYD P 64/76, PDF 3753; FCOM PRO-ABN-HYD P 65/76, PDF 3754; QRH 23.03A, PDF 212]
- **Go-around:** MAX PITCH 15 DEG · TOGA THEN MCT · no gear retraction [FCOM PRO-ABN-HYD P 64/76, PDF 3753; QRH 23.03A, PDF 212]

## 3. Flow (PF / PM)
### 1. Recognise · fly first
**1.1 PF**
- Fly the aircraft by hand: the AP is lost; the FD and A/THR remain [FCTM PR-AEP-HYD P 2/4, PDF 439]
- Maneuver with care to avoid high hydraulic demand on the remaining systems [FCTM PR-AEP-HYD P 2/4, PDF 439]
**1.2 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PM**
- “HYD G+Y SYS LO PR” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-HYD P 62/76, PDF 3751; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.4 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
**1.5 PF**
- Declare a MAYDAY to ATC [FCTM PR-AEP-HYD P 2/4, PDF 439]

### 2. ECAM actions
**2.1 PM**
- PTU …… OFF [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- AFFECTED PUMPS …… OFF [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- **If HYD Y ENG 2 PUMP LO PR** [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - YELLOW ELEC PUMP …… ON [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- MANEUVER WITH CARE …… — [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- **FOR GO-AROUND** [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - MAX PITCH 15 DEG …… — [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - THR LVR …… TOGA THEN MCT [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - Not displayed if one engine is inoperative [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- FUEL CONSUMPT INCRSD · FMS PRED UNRELIABLE …… — [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- F/CTL ALTN LAW (PROT LOST) …… Associated procedure [FCOM PRO-ABN-HYD P 63/76, PDF 3752; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482]
- **If yellow system recovered** [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - HYD G SYS LO PR …… Associated procedure [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- Secondary failures *F/CTL, *WHEEL: analyze each SD page and clear it [FCOM PRO-ABN-HYD P 63/76, PDF 3752; FCTM AOP-30-30 P 3/6, PDF 84]

### 3. STATUS
**3.1 PM**
- “CLEAR HYDRAULIC ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR HYDRAULIC” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

### 4. Assess and decide
**4.1 PM**
- After ECAM ACTIONS COMPLETE, refer to the HYD G + Y SYS LO PR summary: read the CRUISE section [FCTM AOP-30-60 P 2/4, PDF 93; PDP Use of summary, PDF 438; QRH 23.03A, PDF 212]
**4.2 PF + PM**
- Assess the situation; select a runway. Fuel: QRH OPS fuel penalty factors, since FMS predictions are unreliable. Landing performance: EFB application [FCTM AOP-30-60 P 2/4, PDF 93; PDP Use of summary, PDF 438; QRH 23.03A, PDF 212]
**4.3 PF**
- Decide; inform ATC, cabin crew, passengers and airline operations as required [FCTM AOP-30-30 P 5/6, PDF 86; PDP Management of abnormal operations, PDF 428]

### 5. Approach preparation and briefing
**5.1 PM**
- Review the STATUS page, then use the APPROACH, LANDING and GO-AROUND sections to prepare the approach and the FMS [FCTM AOP-30-60 P 2/4, PDF 93; PDP Use of summary, PDF 439; QRH 23.03A, PDF 212]
**5.2 PF**
- Brief with the APPROACH, LANDING and GO-AROUND sections, crosschecking STATUS [FCTM AOP-30-60 P 3/4, PDF 94; PDP Use of summary, PDF 441]
- Selected speed, gravity gear, flap lever, VAPP, an early stabilized approach, tail strike awareness (high pitch expected), braking and steering, go-around callout, configuration and speed [FCTM PR-AEP-HYD P 2/4, PDF 439]

### 6. Approach
**6.1 PM**
- **Before the approach: DUAL HYD LO PR** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - **If system lost by RSVR LO AIR PR** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
    - RELATED PUMP …… ON [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - **If system lost by RSVR OVHT** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
    - **IF GREEN OVHT OUT** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
      - GREEN ENG 1 PUMP …… ON [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
    - **IF YELLOW OVHT OUT** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
      - YELLOW ENG 2 PUMP …… ON [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
**6.2 PF**
- **For flaps extension** [QRH 23.03A, PDF 212]
  - SPD SEL …… VFE NEXT - 5 kt [QRH 23.03A, PDF 212]
- **When in CONF 3** [QRH 23.03A, PDF 212]
  - DECELERATE TO CALCULATED VAPP [QRH 23.03A, PDF 212]
- Stabilize at VAPP before L/G down, to be trimmed for approach [QRH 23.03A, PDF 212; FCTM PR-AEP-HYD P 3/4, PDF 440]
**6.3 PM**
- GPWS FLAP MODE …… OFF [FCOM PRO-ABN-HYD P 64/76, PDF 3753; QRH 23.03A, PDF 212]
- FOR LDG: FLAP LVR 3 [FCOM PRO-ABN-HYD P 64/76, PDF 3753; QRH 23.03A, PDF 212]
- **When CONF 3 and VAPP, if L/G is not downlocked** [FCOM PRO-ABN-HYD P 64/76, PDF 3753; QRH 23.03A, PDF 212]
  - GRVTY GEAR EXTN handcrank …… PULL AND TURN [QRH 23.03A, PDF 212]
  - Rotate the handle clockwise 3 turns until mechanical stop [QRH 23.03A, PDF 212]
  - L/G LEVER …… DOWN [QRH 23.03A, PDF 212]
  - GEAR DOWN …… CHECK [QRH 23.03A, PDF 212]
  - Disregard "USE MANUAL PITCH TRIM". MAN TRIM unusable [QRH 23.03A, PDF 212; FCTM PR-AEP-HYD P 3/4, PDF 440]
**6.4 PM**
- Before the final approach: check the STATUS page and that all APPR PROC have been completed [PDP Use of summary, PDF 442; FCTM AOP-30-60 P 4/4, PDF 95]

### 7. Landing
**7.1 PF**
- Flare: pitch authority reduced (no stabilizer), MAN TRIM unusable; only 1 spoiler per wing, direct law. When flaps are jammed close to zero, consider tailstrike clearance [QRH 23.03A, PDF 212]
- No reverser, no nosewheel steering. BRK Y ACCU PR ONLY (7 applications), MAX BRK PR 1 000 PSI [QRH 23.03A, PDF 212; FCOM PRO-ABN-HYD P 65/76, PDF 3754]

### 8. Go-around
**8.1 PF**
- MAX PITCH 15 DEG · THR LVR TOGA THEN MCT [QRH 23.03A, PDF 212]
**8.2 PF + PM**
- NO GEAR RETRACTION. Increased fuel consumption [QRH 23.03A, PDF 212; QRH 23.03B, PDF 213]
- **For circuit** [QRH 23.03B, PDF 213]
  - MAINTAIN SLATS/FLAPS CONFIGURATION; maintain speed close to VAPP (pitch trim unusable) [QRH 23.03B, PDF 213]
- **For diversion** [QRH 23.03B, PDF 213]
  - **If flaps jammed at zero** [QRH 23.03B, PDF 213]
    - SELECT CLEAN CONFIGURATION; maintain at least the higher of VAPP or VLS (pitch trim unusable) [QRH 23.03B, PDF 213]
  - **If flaps jammed above zero** [QRH 23.03B, PDF 213]
    - MAINTAIN SLATS/FLAPS CONFIGURATION; maintain speed close to VAPP (pitch trim unusable) [QRH 23.03B, PDF 213]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-HYD)
- **LAND ASAP (red)** [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- PTU …… OFF [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- AFFECTED PUMPS …… OFF [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- **If HYD Y ENG 2 PUMP LO PR** [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - YELLOW ELEC PUMP …… ON [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- *MANEUVER WITH CARE* [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- **FOR GO-AROUND** [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - *MAX PITCH 15 DEG* [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
  - THR LVR …… TOGA THEN MCT — This line is not displayed if one engine is inoperative. [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- *FUEL CONSUMPT INCRSD* [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- *FMS PRED UNRELIABLE* [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- *ASSOCIATED PROCEDURES: F/CTL ALTN LAW (PROT LOST). HYD G SYS LO PR, if yellow system recovered.* [FCOM PRO-ABN-HYD P 63/76, PDF 3752]
- *SECONDARY FAILURES: *F/CTL, *WHEEL* [FCOM PRO-ABN-HYD P 63/76, PDF 3752]

## 5. STATUS
**Limitations**
- MAX SPEED …… 320/0.77 [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- MAX BRK PR …… 1 000 PSI [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- MANEUVER WITH CARE [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- FOR GO-AROUND: MAX PITCH 15 DEG; THR LVR …… TOGA THEN MCT (not displayed if one engine is inoperative) [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
**Information**
- ALTN LAW: PROT LOST [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- WHEN L/G DN: DIRECT LAW — at landing gear extension, control reverts to direct law in pitch, as well as in roll [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- BRK Y ACCU PR ONLY — 7 full brake applications are available [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- FUEL CONSUMPT INCRSD [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- FMS PRED UNRELIABLE — disregard FMS fuel predictions and refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- SLATS SLOW [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- Following a yellow hydraulic system failure, the parking brake may be inoperative due to yellow accumulator low pressure. [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
**APPR PROC**
- *DUAL HYD LO PR* [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- **If system lost by RSVR LO AIR PR:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - RELATED PUMP …… ON [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- **If system lost by RSVR OVHT:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - **IF GREEN OVHT OUT:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
    - GREEN ENG 1 PUMP …… ON [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - **IF YELLOW OVHT OUT:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
    - YELLOW ENG 2 PUMP …… ON [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- **IF HYD NOT RECOVERED:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - S/F JAMMED PROC …… APPLY [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG: FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - GPWS FLAP MODE …… OFF [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
  - **If L/G is not downlocked:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
    - **WHEN CONF 3 AND VAPP:** [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
      - L/G GRVTY PROC …… APPLY — Being stabilized at VAPP, before selecting the gear down, enables the aircraft to be trimmed for approach. [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
      - **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- APPR SPD …… VREF + 25 KT — Approach speed must be increased, due to the loss of flaps. [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-HYD P 65/76, PDF 3754]
**INOP SYS**
- G+Y HYD [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- F/CTL PROT [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- STABILIZER [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- REVERSER 1+2 [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- SPLR 1+2+ 4+5 [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- FLAPS [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- LAF [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- YAW DAMPER [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- AP 1+2 [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- ANTI SKID [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- N/W STRG [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- NORM BRK [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- AUTO BRK [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- L/G RETRACT [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- CARGO DOOR (If HYD Y RSVR LO LVL) [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- CAT 2 [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- GLS AUTOLAND [FCOM PRO-ABN-HYD P 64/76, PDF 3753]
- STEEP APPR [FCOM PRO-ABN-HYD P 64/76, PDF 3753]

## 6. QRH and reference tables
### HYD G + Y SYS LO PR SUMMARY
**CRUISE**
- MAX SPD : 320/0.77 [QRH 23.03A, PDF 212]
- MAX FL : 4000FT BELOW REC MAX FL [QRH 23.03A, PDF 212]
- MANEUVER WITH CARE [QRH 23.03A, PDF 212]
- NO STABILIZER [QRH 23.03A, PDF 212]
- ALTN LAW: PROT LOST [QRH 23.03A, PDF 212]
- FUEL: Increased fuel consumption (Refer to OPS Use of Fuel Penalty Factor Tables) [QRH 23.03A, PDF 212]
- For Landing Performance assessment, use the performance application of the EFB. [QRH 23.03A, PDF 212]
**APPROACH**
- CAT 2 INOP [QRH 23.03A, PDF 212]
- SLATS SLOW / FLAPS JAMMED [QRH 23.03A, PDF 212]
- FOR LDG : FLAP LVR 3 [QRH 23.03A, PDF 212]
- GPWS FLAP MODE : OFF [QRH 23.03A, PDF 212]
- For Flaps extension: SPD SEL : VFE NEXT - 5 kt [QRH 23.03A, PDF 212]
- When in CONF 3: DECELERATE TO CALCULATED VAPP [QRH 23.03A, PDF 212]
- When in CONF 3 and VAPP: Stabilize at VAPP before L/G down, to be trimmed for approach. [QRH 23.03A, PDF 212]
- L/G gravity extension: GRVTY GEAR EXTN handcrank : PULL AND TURN (Rotate the handle clockwise 3 turns until mechanical stop); L/G LEVER : DOWN; GEAR DOWN : CHECK [QRH 23.03A, PDF 212]
- Disregard "USE MANUAL PITCH TRIM". MAN TRIM Unusable [QRH 23.03A, PDF 212]
**LANDING**
- FLARE: PITCH AUTHORITY REDUCED (No stabilizer). MAN TRIM Unusable. When Flaps jammed close to zero, consider tailstrike clearance. Only 1 spoiler per wing – Direct law [QRH 23.03A, PDF 212]
- SPOILERS: Only 1 per wing [QRH 23.03A, PDF 212]
- NO REVERSER [QRH 23.03A, PDF 212]
- BRAKING: BRK Y ACCU PR ONLY (7 applications) [QRH 23.03A, PDF 212]
- MAX BRK PR : 1 000 PSI [QRH 23.03A, PDF 212]
- NO NOSEWHEEL STEERING [QRH 23.03A, PDF 212]
**GO-AROUND**
- MAX PITCH 15 DEG [QRH 23.03A, PDF 212]
- THR LVR : TOGA THEN MCT [QRH 23.03A, PDF 212]
- NO GEAR RETRACTION [QRH 23.03A, PDF 212]
- FUEL: Increased fuel consumption (Refer to OPS Use of Fuel Penalty Factor Tables) [QRH 23.03B, PDF 213]
- For circuit: MAINTAIN SLATS/FLAPS CONFIGURATION; Maintain speed close to VAPP (due to pitch trim unusable) [QRH 23.03B, PDF 213]
- For diversion: If Flaps jammed at zero: SELECT CLEAN CONFIGURATION; Maintain at least the higher of VAPP or VLS (due to pitch trim unusable). If Flaps jammed above zero: MAINTAIN SLATS/FLAPS CONFIGURATION; Maintain speed close to VAPP (due to pitch trim unusable) [QRH 23.03B, PDF 213]
### Remaining systems 
FCTM table; the third column of the FCTM table (HYD B+Y) is left out.

| Phase | System | HYD G+B SYS LO PR | HYD G+Y SYS LO PR |
|---|---|---|---|
| Cruise | Autopilot | Inop | Inop |
| Cruise | Yaw damper | YD2 only | Inop |
| Cruise | Control law | ALTN LAW and DIRECT LAW when L/G DN | ALTN LAW and DIRECT LAW when L/G DN |
| Cruise | Stabilizer | Avail | Inop |
| Cruise | Spoilers | 2 SPLRS/wing | 1 SPLR/wing |
| Cruise | Elevator | R ELEV only | Avail |
| Cruise | Aileron | Inop | Avail |
| Landing | Slats/Flaps | FLAPS slow only | SLATS slow only |
| Landing | L/G extension | Gravity | Gravity |
| Landing | Braking | ALTN BRK only | Y ACCU PRESS only |
| Landing | Anti skid | Avail | Inop |
| Landing | Nose wheel steering | Avail | Inop |
| Landing | Reverse | REV 2 only | Inop |
| Go-around | L/G retraction | Inop | Inop |
[FCTM PR-AEP-HYD P 3/4, PDF 440; FCTM PR-AEP-HYD P 4/4, PDF 441]

## 7. FCTM technique
- A double hydraulic failure is an emergency, with red LAND ASAP displayed; a MAYDAY should be declared. Land as soon as possible, but complete the ECAM actions before the approach. [FCTM PR-AEP-HYD P 2/4, PDF 439]
- It is a "complex procedure": refer to the QRH summary when the ECAM procedure is complete. A clear reading of STATUS is essential to sequence the actions during the approach. [FCTM PR-AEP-HYD P 2/4, PDF 439]
- Wait for stabilization at VAPP before the gear extension, to ensure a proper centered sidestick position for approach and landing. If this is missed, the flare and pitch control in a go-around may be difficult. Disregard the PFD message USE MAN PITCH TRIM after gear extension. [FCTM PR-AEP-HYD P 3/4, PDF 440]
- High pitch during the approach should be expected: outline it in the arrival briefing for tail strike awareness, and monitor pitch attitude during the flare. [FCTM PR-AEP-HYD P 4/4, PDF 441]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| LANDING WITH SLATS OR FLAPS JAMMED | APPR PROC: S/F JAMMED PROC APPLY | SPD SEL VFE NEXT - 5 kt; AT VFE NEXT: SELECT FLAPS LEVER ONE STEP DOWN; See the QRH brief | [FCOM PRO-ABN-HYD P 64/76, PDF 3753; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474] |
| L/G GRAVITY EXTENSION | APPR PROC: L/G GRVTY PROC APPLY when CONF 3 and VAPP | See the QRH brief; the summary includes the lines | [FCOM PRO-ABN-HYD P 64/76, PDF 3753; FCOM PRO-ABN-LG P 7/30, PDF 3772] |
| F/CTL ALTN LAW | Associated procedure (PROT LOST) | See the ALTN LAW brief | [FCOM PRO-ABN-HYD P 63/76, PDF 3752; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482] |
| F/CTL DIRECT LAW | Control reverts to direct law at landing gear extension | See the DIRECT LAW brief | [FCOM PRO-ABN-HYD P 65/76, PDF 3754; FCOM PRO-ABN-F_CTL P 18/132, PDF 3491] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCTM and PDP give the sequence but no PF/PM slide for this failure: the turns come from the AOP-20 task sharing, FCTM AOP-30-60 and the QRH summary. The manuals do not say who turns the handcrank; the PM is shown from instructor practice. [FCTM AOP-20 P 1–2/10, PDF 68; FCTM AOP-30-60 P 1/4, PDF 92; PDP Use of summary, PDF 439]
- The MAYDAY wording is not given in the supplied manuals. [FCTM PR-AEP-HYD P 2/4, PDF 439]
- QRH fuel penalty factor for G+Y SYS LO PR is 0 % to 10 % for all HS-TX (stabilizer jammed, spoilers 1, 2, 4 and 5); the FMS predictions are unreliable. [QRH OPS.04C, PDF 275; QRH OPS.04D, PDF 276; QRH OPS.04E, PDF 277; QRH OPS.04F, PDF 278]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-HYD — HYD G+Y SYS LO PR (HS-TX) | P 62–65/76 | 3751–3754 | 26 MAY 26 |
| QRH | 23.03 — summary; OPS.04 — fuel penalty factors | 23.03A–B · OPS.04C–F | 212–213, 275–278 | 18 FEB 26, 14 JUL 26 |
| FCTM | PR-AEP-HYD · AOP-30-60 | P 1–4/4 · P 1–4/4 | 438–441, 92–95 | 26 MAY 26 |
| PDP | Use of summary (XFTDN1USESUMM01) | — | 436–442 |  |
| FCOM | DSC-27-20-20 — reconfiguration laws | P 3, 5/20 | 1614, 1616 | 18 FEB 26 |
