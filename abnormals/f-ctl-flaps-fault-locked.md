# F/CTL FLAPS FAULT/LOCKED — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX.

An amber caution: the flaps have stopped. First select the speed to stay below VFE. If the flaps are locked (wing tip brake on or alignment fault), hold the table MAX SPEED. If they are not locked, recycle the flaps lever once below VFE. If that fails, apply the QRH LANDING WITH SLATS OR FLAPS JAMMED, with approach speed from the table.

## 1. What it is
- **Trigger:** The FLAPS FAULT alert triggers when both flaps channels fail. The FLAPS LOCKED alert triggers when the flaps wing tip brakes activate. [FCOM PRO-ABN-F_CTL P 48/132, PDF 3521]
- **Flight phase inhibition:** phases 4, 5, 8 [FCOM PRO-ABN-F_CTL P 48/132, PDF 3521]
- Causes: dual flaps control unit (SFCC flaps channel) failure, dual hydraulic failure, a combination, a mechanical jam, or locking by wing tip brake activation. [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
- Consequences: the control laws may change, the selected speed must be used, an early stabilized approach should be preferred, approach attitudes change, approach speeds and landing distances increase, and the go-around procedure may have to be modified. [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
- For flight with SLATS or FLAPS extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]

## 2. Key limits
- **MAX SPEED:** Table: VFE of the next flap position (see tables) [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522; FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]
- **APPR SPD:** Table by slats/flaps position (see tables) [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]
- **AP:** May be used down to 500 ft AGL; monitor it [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522; FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- **FUEL penalty, flaps extended:** 80 % [QRH OPS.04C, PDF 275; QRH OPS.04E, PDF 277]

## 3. Flow (PF / PM)
### 1. Recognise · hold the speed
**1.1 PF**
- **Failure at takeoff** [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
  - During takeoff: pull the SPD/MACH knob to select the speed and stop the acceleration, to avoid exceeding VFE. The overspeed warning follows the actual slats/flaps position [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
- **Failure during the approach** [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
  - During the approach: pull the speed knob for selected speed to avoid further deceleration, and delay the approach to complete the ECAM procedure [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
**1.2 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PM**
- “F/CTL FLAPS FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-F_CTL P 48/132, PDF 3521; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.4 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- **If flaps locked** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - WING TIP BRK ON OR ALIGNMENT FAULT …… — [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - MAX SPEED …… REFER TO THE TABLE [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522; FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]
  - Limit speed to the VFE corresponding to the next flap position [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
- **If flaps not locked** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - **WHEN SPD BELOW VFE** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
    - Configuration change: the PF can stop the ECAM while the lever is moved [PDP Management of abnormal operations, PDF 430]
    - FLAPS LEVER …… RECYCLE [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
    - Return to the previous selection, then back to the desired position [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
- **If flaps extended** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - FUEL CONSUMPT INCRSD · FMS PRED UNRELIABLE …… — [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
- **If unsuccessful** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - Refer to [QRH] Landing with Slats or Flaps Jammed [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - The autopilot may be used down to 500 ft AGL. It is not tuned for abnormal configurations, so monitor its behavior [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]

### 3. STATUS
**3.1 PM**
- “CLEAR FLIGHT CONTROL ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR FLIGHT CONTROL” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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
**4.1 PF + PM**
- **After a failure at takeoff** [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
  - The landing distance available at the departure airport and the aircraft gross weight determine the next course of action [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
- Consider the fuel and the increased consumption on a diversion; FMS predictions are not valid. With slats/flaps extended, cruise altitude is limited to 20 000 ft [FCTM PR-AEP-F_CTL P 1/6, PDF 428; FCTM PR-AEP-F_CTL P 2/6, PDF 429]
**4.2 PF**
- Decide; inform ATC, cabin crew, passengers and airline operations as required [FCTM AOP-30-30 P 5/6, PDF 86; PDP Management of abnormal operations, PDF 428]

### 5. Approach preparation
**5.1 PF**
- “LANDING WITH SLATS OR FLAPS JAMMED PROCEDURE” [PDP Management of abnormal operations, PDF 427]
**5.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427]
**5.3 PM**
- The STATUS APPR PROC asks for it: S/F JAMMED PROC APPLY [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
**5.4 PF**
- Update the arrival briefing: tail strike awareness, go-around configuration, any deviation from standard callout, speeds after a missed approach, selected speed for acceleration at the acceleration altitude [FCTM PR-AEP-F_CTL P 2/6, PDF 429]

### 6. Approach
**6.1 PM**
- **If FLAPS ≤ 3** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS > 3** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - FLAPS …… KEEP CONF FULL [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS < 3** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - GPWS FLAP MODE …… OFF [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS ≥ 3** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- APPR SPD …… REFER TO THE TABLE [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
**6.2 PF**
- Fly the configuration steps of the QRH procedure with selected speed (see the LANDING WITH SLATS OR FLAPS JAMMED brief) [FCTM PR-AEP-F_CTL P 2/6, PDF 429; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- ENG 1 and ENG 2 APPR IDLE ONLY [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-F_CTL)
- **If flaps locked:** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - *WING TIP BRK ON OR ALIGNMENT FAULT* [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - MAX SPEED …… REFER TO F/CTL FLAPS/SLATS FAULT/LOCKED — Limit speed to the VFE corresponding to the next flap position. [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
- **If flaps not locked:** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - **WHEN SPD BELOW VFE:** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
    - FLAPS LEVER …… RECYCLE — Return to the previous selection, then back to the desired position. [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
- **If flaps extended:** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - *FUEL CONSUMPT INCRSD* [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - *FMS PRED UNRELIABLE* [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
- **If unsuccessful:** [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - *Refer to PRO-ABN-F_CTL [QRH] Landing with Slats or Flaps Jammed* [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]
  - *The autopilot may be used down to 500 ft AGL. As it is not tuned for abnormal configurations, its behavior can be less than optimum and must be monitored.* [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522]

## 5. STATUS
**Limitations**
- MAX SPEED …… REFER TO F/CTL FLAPS/SLATS FAULT/LOCKED [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- If flaps extended: FUEL CONSUMPT INCRSD [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
**Information**
- ENG 1 APPR IDLE ONLY [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- ENG 2 APPR IDLE ONLY [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- If flaps extended: FMS PRED UNRELIABLE — disregard FMS fuel predictions and refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
**APPR PROC**
- S/F JAMMED PROC …… APPLY — Refer to QRH/ABN-20 Landing with Slats or Flaps Jammed. [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS ≤ 3:** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG : FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS > 3:** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - FLAPS …… KEEP CONF FULL [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS < 3:** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - GPWS FLAP MODE …… OFF [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- **If FLAPS ≥ 3:** [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
  - GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- APPR SPD …… REFER TO F/CTL FLAPS/SLATS FAULT/LOCKED [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523]
**INOP SYS**
- FLAPS [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
- AP 1+2 (If both flap channels fault) [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
- A/THR (If both flap channels fault) [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
- CAT 2 (If both flap channels fault) [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
- GLS AUTOLAND [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
- STEEP APPR [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]
- FD 1+2 (If both flap channels fault) [FCOM PRO-ABN-F_CTL P 50/132, PDF 3523; FCOM PRO-ABN-F_CTL P 51/132, PDF 3524]

## 6. QRH and reference tables
### MAX SPEED 
Slats/flaps position displayed on the upper ECAM display.

| Slats \ Flaps | F = 0 | 0 < F ≤ 1 | 1 < F ≤ 2 | 2 < F ≤ 3 | F > 3 |
|---|---|---|---|---|---|
| S = 0 | NO LIMITATION | 215 kt | 200 kt | 185 kt | Not allowed (177 kt) |
| 0 < S < 1 | 230 kt | 215 kt | 200 kt | 185 kt | Not allowed (177 kt) |
| S = 1 | 230 kt | 215 kt | 200 kt | 185 kt | 177 kt |
| 1 < S ≤ 3 | 200 kt | 200 kt | 200 kt | 185 kt | 177 kt |
| S > 3 | 177 kt | 177 kt | 177 kt | 177 kt | 177 kt |
[FCOM PRO-ABN-F_CTL P 59/132, PDF 3532; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474; QRH 20.02C, PDF 189]

### APPR SPD 
Slats/flaps position displayed on the upper ECAM display.

| Slats \ Flaps | F = 0 | 0 < F < 1 | 1 ≤ F < 2 | 2 ≤ F < 3 | F = 3 | F > 3 |
|---|---|---|---|---|---|---|
| S = 0 | VREF +60 (Appr), VREF +50 (Touch Down) | VREF +45 | VREF +30 | VREF +25 | VREF +25 | Not allowed |
| 0 < S < 1 | VREF +45 | VREF +45 | VREF +30 | VREF +25 | VREF +25 | Not allowed |
| 1 ≤ S ≤ 3 | VREF +25 | VREF +25 | VREF +15 | VREF +10 | VREF +10 | VREF +10 |
| S > 3 | VREF +25 | VREF +25 | VREF +15 | VREF +10 | VREF +10 | VREF +5 |
[FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]

## 7. FCTM technique
- The detection on approach comes with the flap lever selection. With A/THR operating, the managed target becomes the next characteristic speed, so pull the knob for selected speed to avoid further deceleration. [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
- The AP may be used down to 500 ft AGL. It is not tuned for abnormal configurations: monitor it. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| LANDING WITH SLATS OR FLAPS JAMMED | If unsuccessful, and on the STATUS page: S/F JAMMED PROC APPLY | See the QRH brief | [FCOM PRO-ABN-F_CTL P 49/132, PDF 3522; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- F/CTL FLAPS FAULT/LOCKED is not in the QRH reset table. [QRH 02.02A, PDF 51]
- The PDP has no slide for this failure: the turns come from the FCTM AOP-30-30 sequence and PR-AEP-F_CTL. The FCTM says "the crew" pulls the knob; it is shown for the PF, who flies. [FCTM PR-AEP-F_CTL P 1/6, PDF 428; FCTM AOP-30-30 P 2/6, PDF 83]
- The ECAM calls the alert F/CTL FLAPS FAULT or F/CTL FLAPS LOCKED: announce the title shown. [FCOM PRO-ABN-F_CTL P 48/132, PDF 3521]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-F_CTL — F/CTL FLAPS FAULT/LOCKED (HS-TX); FLAPS/SLATS tables | P 48–51, 59/132 | 3521–3524, 3532 | 26 MAY 26 |
| FCTM | PR-AEP-F_CTL — abnormal slats/flaps configuration | P 1–2/6 | 428–429 | 26 MAY 26 |
| QRH | OPS.04 — fuel penalty factors | OPS.04C, E | 275, 277 | 14 JUL 26 |
