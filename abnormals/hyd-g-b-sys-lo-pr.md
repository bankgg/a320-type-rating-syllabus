# HYD G+B SYS LO PR — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items · QRH summary**  
**Applicability:** HS-TXA..TXF, HS-TXG..TXU — One FCOM procedure for all HS-TX. Only the QRH fuel penalty factor differs (see HS-TX differences).

A red warning with red LAND ASAP: green and blue hydraulics are lost. The FCTM says a MAYDAY should be declared, and the ECAM actions should be completed before the approach. No AP, alternate law with protections lost, no slats and no ailerons, only the right elevator. It is a hand-flown approach with selected speed and A/THR off, flap lever 3, and a gravity gear extension at 200 kt, which gives direct law. Use the QRH summary after the ECAM.

## 1. What it is
- **Trigger:** This alert triggers when the green and blue systems pressure ≤1 450 PSI (the alert resets if pressure ≥1 750 PSI). [FCOM PRO-ABN-HYD P 50/76, PDF 3739]
- **Flight phase inhibition:** phases 4, 5 [FCOM PRO-ABN-HYD P 50/76, PDF 3739]
- Dual hydraulic failures bring loss of the AP, flight control law degradation, landing in an abnormal configuration, extensive ECAM procedures and significant considerations for approach and landing. [FCTM PR-AEP-HYD P 1/4, PDF 438]
- Pitch: with HYD G+B, alternate law has no protections; direct law applies in roll. [FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 5/20, PDF 1616]
- The RAT can be extended at any time with the RAT MAN ON pushbutton. [FCOM DSC-29-20 P 3/10, PDF 1754]

## 2. Key limits
- **MAX SPEED:** 320/0.77 [FCOM PRO-ABN-HYD P 52/76, PDF 3741; QRH 23.02A, PDF 210]
- **MAX FL:** 4000 FT below REC MAX FL [QRH 23.02A, PDF 210]
- **MIN RAT SPD:** 140 KT, if the RAT is out and HYD B ELEC PUMP LO PR [FCOM PRO-ABN-HYD P 51/76, PDF 3740; FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- **For landing:** FLAP LVR 3 · VREF + 25 KT · GPWS LDG FLAP 3 ON [FCOM PRO-ABN-HYD P 52/76, PDF 3741; FCOM PRO-ABN-HYD P 53/76, PDF 3742]
- **L/G gravity extension:** When SPD 200 KT [FCOM PRO-ABN-HYD P 53/76, PDF 3742; QRH 23.02A, PDF 210]
- **Go-around:** MAX PITCH 15 DEG · TOGA THEN MCT · no gear retraction [FCOM PRO-ABN-HYD P 52/76, PDF 3741; QRH 23.02B, PDF 211]

## 3. Flow (PF / PM)
### 1. Recognise · fly first
**1.1 PF**
- Fly the aircraft by hand: the AP is lost; the FD and A/THR remain [FCTM PR-AEP-HYD P 2/4, PDF 439]
- Maneuver with care to avoid high hydraulic demand on the remaining systems [FCTM PR-AEP-HYD P 2/4, PDF 439]
**1.2 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PM**
- “HYD G+B SYS LO PR” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-HYD P 50/76, PDF 3739; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.4 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
**1.5 PF**
- Declare a MAYDAY to ATC [FCTM PR-AEP-HYD P 2/4, PDF 439]

### 2. ECAM actions
**2.1 PM**
- **If HYD B ELEC PUMP LO PR** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - **If the RAT is not out** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
    - RAT …… MAN ON [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - **If the RAT is out** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
    - MIN RAT SPD …… 140 KT [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- AFFECTED PUMPS: the BLUE ELEC PUMP pb is guarded — crosscheck it first [FCOM DSC-29-20 P 1/10, PDF 1752; FCTM AOP-30-20 P 1/2, PDF 80]
**2.2 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCOM DSC-29-20 P 1/10, PDF 1752]
**2.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.4 PM**
- AFFECTED PUMPS …… OFF [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- MANEUVER WITH CARE …… — [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- **FOR GO-AROUND** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - MAX PITCH 15 DEG …… — [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - THR LVR …… TOGA THEN MCT [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - Not displayed if one engine is inoperative [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- FUEL CONSUMPT INCRSD · FMS PRED UNRELIABLE …… — [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- F/CTL ALTN LAW (PROT LOST) …… Associated procedure [FCOM PRO-ABN-HYD P 51/76, PDF 3740; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482]
- **If blue system recovered** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - HYD G SYS LO PR …… Associated procedure [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- Secondary failures *WHEEL, *F/CTL: analyze each SD page and clear it [FCOM PRO-ABN-HYD P 51/76, PDF 3740; FCTM AOP-30-30 P 3/6, PDF 84]

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
- After ECAM ACTIONS COMPLETE, refer to the HYD G + B SYS LO PR summary: read the CRUISE section [FCTM AOP-30-60 P 2/4, PDF 93; PDP Use of summary, PDF 438; QRH 23.02A, PDF 210]
**4.2 PF + PM**
- Assess the situation; select a runway. Fuel: QRH OPS fuel penalty factors, since FMS predictions are unreliable. Landing performance: EFB application [FCTM AOP-30-60 P 2/4, PDF 93; PDP Use of summary, PDF 438; QRH 23.02A, PDF 210]
**4.3 PF**
- Decide; inform ATC, cabin crew, passengers and airline operations as required [FCTM AOP-30-30 P 5/6, PDF 86; PDP Management of abnormal operations, PDF 428]

### 5. Approach preparation and briefing
**5.1 PM**
- Review the STATUS page, then use the APPROACH, LANDING and GO-AROUND sections to prepare the approach and the FMS [FCTM AOP-30-60 P 2/4, PDF 93; PDP Use of summary, PDF 439; QRH 23.02A, PDF 210]
**5.2 PF**
- Brief with the APPROACH, LANDING and GO-AROUND sections, crosschecking STATUS [FCTM AOP-30-60 P 3/4, PDF 94; PDP Use of summary, PDF 441]
- Selected speed, gravity gear, flap lever, VAPP, an early stabilized approach, tail strike awareness, braking and steering, go-around callout, configuration and speed [FCTM PR-AEP-HYD P 2/4, PDF 439]

### 6. Approach
**6.1 PM**
- **Before the approach: DUAL HYD LO PR** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - **If system lost by RSVR LO AIR PR** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
    - RELATED PUMPS …… ON [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - **If system lost by RSVR OVHT** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
    - **IF BLUE OVHT OUT** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
      - BLUE ELEC PUMP …… AUTO [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
    - **IF GREEN OVHT OUT** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
      - GREEN ENG 1 PUMP …… ON [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
**6.2 PF**
- A/THR …… OFF [FCOM PRO-ABN-HYD P 52/76, PDF 3741; QRH 23.02A, PDF 210]
- Select the target speed on the FCU: the A/THR may not satisfactorily maintain speed [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- **For flaps extension** [QRH 23.02A, PDF 210]
  - SPD SEL …… VFE NEXT - 5 kt [QRH 23.02A, PDF 210]
**6.3 PM**
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-HYD P 53/76, PDF 3742; QRH 23.02A, PDF 210]
- FOR LDG: FLAP LVR 3 [FCOM PRO-ABN-HYD P 52/76, PDF 3741; QRH 23.02A, PDF 210]
- **When SPD 200 KT, if L/G is not downlocked** [FCOM PRO-ABN-HYD P 53/76, PDF 3742; QRH 23.02A, PDF 210]
  - GRVTY GEAR EXTN handcrank …… PULL AND TURN [QRH 23.02A, PDF 210]
  - Rotate the handle clockwise 3 turns until mechanical stop [QRH 23.02A, PDF 210]
  - L/G LEVER …… DOWN [QRH 23.02A, PDF 210]
  - GEAR DOWN …… CHECK [QRH 23.02A, PDF 210]
**6.4 PF**
- **When L/G down** [QRH 23.02A, PDF 210]
  - USE MAN PITCH TRIM: control is in direct law [QRH 23.02A, PDF 210; FCOM PRO-ABN-HYD P 53/76, PDF 3742]
- **When in landing CONF and in final approach** [QRH 23.02B, PDF 211]
  - DECELERATE TO CALCULATED VAPP [QRH 23.02B, PDF 211]
**6.5 PM**
- Before the final approach: check the STATUS page and that all APPR PROC have been completed [PDP Use of summary, PDF 442; FCTM AOP-30-60 P 4/4, PDF 95]

### 7. Landing
**7.1 PF**
- Flare: only one elevator and two spoilers per wing, no ailerons; slightly sluggish in direct law [QRH 23.02B, PDF 211]
- Reverser: only N°2. Spoilers: only 2 per wing. Braking: ALTERNATE [QRH 23.02B, PDF 211]

### 8. Go-around
**8.1 PF**
- MAX PITCH 15 DEG · THR LVR TOGA THEN MCT [QRH 23.02B, PDF 211]
**8.2 PF + PM**
- NO GEAR RETRACTION. Increased fuel consumption [QRH 23.02B, PDF 211]
- **For circuit** [QRH 23.02B, PDF 211]
  - MAINTAIN SLATS/FLAPS CONFIGURATION; recommended speed MAX SPD - 10 kt [QRH 23.02B, PDF 211]
- **For diversion** [QRH 23.02B, PDF 211]
  - SELECT CLEAN CONFIGURATION [QRH 23.02B, PDF 211]
  - Slats jammed at zero: normal operating speeds. Slats jammed above zero: recommended speed MAX SPD - 10 kt [QRH 23.02B, PDF 211]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-HYD)
- *If the green hydraulic system is lost due to low level, the HYD PTU FAULT alert may appear, and requests the flight crew to switch the PTU off.* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- **LAND ASAP (red)** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- **If HYD B ELEC PUMP LO PR:** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - **If the RAT is not out:** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
    - RAT …… MAN ON [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - **If the RAT is out:** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
    - MIN RAT SPD …… 140 KT [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- AFFECTED PUMPS …… OFF [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- *MANEUVER WITH CARE* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- **FOR GO-AROUND** [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - *MAX PITCH 15 DEG* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
  - THR LVR …… TOGA THEN MCT — This line is not displayed if one engine is inoperative. [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- *FUEL CONSUMPT INCRSD* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- *FMS PRED UNRELIABLE* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- *ASSOCIATED PROCEDURES: F/CTL ALTN LAW (PROT LOST). HYD G SYS LO PR, if blue system recovered.* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]
- *SECONDARY FAILURES: *WHEEL, *F/CTL* [FCOM PRO-ABN-HYD P 51/76, PDF 3740]

## 5. STATUS
**Limitations**
- MIN RAT SPD …… 140 KT — displayed if the RAT is out and in the case of HYD B ELEC PUMP LO PR [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- MAX SPEED …… 320/0.77 [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- MANEUVER WITH CARE [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- SPD BRK …… DO NOT USE [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- FOR GO-AROUND: MAX PITCH 15 DEG; THR LVR …… TOGA THEN MCT (not displayed if one engine is inoperative) [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- FUEL CONSUMPT INCRSD [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
**Information**
- ALTN LAW: PROT LOST [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
- WHEN L/G DN: DIRECT LAW — at landing gear extension, control reverts to direct law in pitch, as well as in roll [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
- FMS PRED UNRELIABLE — disregard FMS fuel predictions and refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table [FCOM PRO-ABN-HYD P 53/76, PDF 3742; FCOM PRO-ABN-HYD P 54/76, PDF 3743]
- FLAPS SLOW [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
**APPR PROC**
- *DUAL HYD LO PR* [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- **If system lost by RSVR LO AIR PR:** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - RELATED PUMPS …… ON [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- **If system lost by RSVR OVHT:** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - **IF BLUE OVHT OUT:** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
    - BLUE ELEC PUMP …… AUTO [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - **IF GREEN OVHT OUT:** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
    - GREEN ENG 1 PUMP …… ON [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- **IF HYD NOT RECOVERED:** [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - S/F JAMMED PROC …… APPLY [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - A/THR …… OFF — Select the target speed on the FCU. Due to the loss of slats and some flight control surfaces, the A/THR may not satisfactorily maintain speed. [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG: FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
  - GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
  - **If L/G is not downlocked:** [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
    - **WHEN SPD 200 KT (displayed when slats are retracted):** [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
      - L/G GRVTY PROC …… APPLY — Extend the landing gear at 200 kt to revert sooner in direct law. This provides, below 200 kt, a better pitch control than in alternate law with one elevator lost and all slats lost. [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
      - **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
- APPR SPD …… VREF + 25 KT — Approach speed must be increased due to the loss of ailerons and slats. [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-HYD P 53/76, PDF 3742]
**INOP SYS**
- G+B HYD [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- F/CTL PROT [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- L ELEV [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- L+R AIL [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- SPLR 1+3+5 [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- SLATS [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- AP 1+2 [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- AUTO BRK [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- NORM BRK [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- L/G RETRACT [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- REVERSER 1 [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- EMER GEN (If HYD B RSVR LO LVL) [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- G ENG 1 PUMP [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- B ELEC PUMP [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- YAW DAMPER 1 [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- CAT 2 [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- GLS AUTOLAND [FCOM PRO-ABN-HYD P 52/76, PDF 3741]
- STEEP APPR [FCOM PRO-ABN-HYD P 52/76, PDF 3741]

## 6. QRH and reference tables
### HYD G + B SYS LO PR SUMMARY
**CRUISE**
- SPD BRK : DO NOT USE [QRH 23.02A, PDF 210]
- MAX SPD : 320/0.77 [QRH 23.02A, PDF 210]
- MAX FL : 4000FT BELOW REC MAX FL [QRH 23.02A, PDF 210]
- MANEUVER WITH CARE [QRH 23.02A, PDF 210]
- ALTN LAW: PROT LOST [QRH 23.02A, PDF 210]
- FUEL: Increased fuel consumption (Refer to OPS Use of Fuel Penalty Factor Tables) [QRH 23.02A, PDF 210]
- For Landing Performance assessment, use the performance application of the EFB. [QRH 23.02A, PDF 210]
**APPROACH**
- CAT 2 INOP [QRH 23.02A, PDF 210]
- SLATS JAMMED/FLAPS SLOW [QRH 23.02A, PDF 210]
- ATHR : OFF [QRH 23.02A, PDF 210]
- FOR LDG : FLAP LVR 3 [QRH 23.02A, PDF 210]
- GPWS LDG FLAP 3 : ON [QRH 23.02A, PDF 210]
- For Flaps extension: SPD SEL : VFE NEXT - 5 kt [QRH 23.02A, PDF 210]
- When SPD 200 kt: L/G gravity extension: GRVTY GEAR EXTN handcrank : PULL AND TURN (Rotate the handle clockwise 3 turns until mechanical stop); L/G LEVER : DOWN; GEAR DOWN : CHECK [QRH 23.02A, PDF 210]
- When L/G down: USE MAN PITCH TRIM [QRH 23.02A, PDF 210]
- When in landing CONF and in final approach: DECELERATE TO CALCULATED VAPP [QRH 23.02B, PDF 211]
**LANDING**
- FLARE: Only one ELEV and two spoilers per wing. No ailerons. A/C slightly sluggish – Direct law [QRH 23.02B, PDF 211]
- SPOILERS: Only 2 per wing [QRH 23.02B, PDF 211]
- REVERSER: Only N°2 [QRH 23.02B, PDF 211]
- BRAKING: ALTERNATE [QRH 23.02B, PDF 211]
**GO-AROUND**
- MAX PITCH 15 DEG [QRH 23.02B, PDF 211]
- THR LVR : TOGA THEN MCT [QRH 23.02B, PDF 211]
- NO GEAR RETRACTION [QRH 23.02B, PDF 211]
- FUEL: Increased fuel consumption (Refer to OPS Use of Fuel Penalty Factor Tables) [QRH 23.02B, PDF 211]
- For circuit: MAINTAIN SLATS/FLAPS CONFIGURATION; Recommended speed: MAX SPD - 10 kt [QRH 23.02B, PDF 211]
- For diversion: SELECT CLEAN CONFIGURATION. If Slats jammed at zero: Normal operating speeds. If Slats jammed above zero: Recommended speed: MAX SPD - 10 kt [QRH 23.02B, PDF 211]
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
- The PF is very busy flying and communicating in alternate law. Handling may differ because some control surfaces are lost, so maneuver with care. [FCTM PR-AEP-HYD P 2/4, PDF 439]
- The G+B approach extends the gear at 200 kt: below 200 kt direct law gives better pitch control than alternate law with one elevator and all slats lost. [FCOM PRO-ABN-HYD P 53/76, PDF 3742]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| LANDING WITH SLATS OR FLAPS JAMMED | APPR PROC: S/F JAMMED PROC APPLY | SPD SEL VFE NEXT - 5 kt; AT VFE NEXT: SELECT FLAPS LEVER ONE STEP DOWN; See the QRH brief | [FCOM PRO-ABN-HYD P 52/76, PDF 3741; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474] |
| L/G GRAVITY EXTENSION | APPR PROC: L/G GRVTY PROC APPLY at 200 kt | See the QRH brief; the summary includes the lines | [FCOM PRO-ABN-HYD P 53/76, PDF 3742; FCOM PRO-ABN-LG P 7/30, PDF 3772] |
| F/CTL ALTN LAW | Associated procedure (PROT LOST) | See the ALTN LAW brief | [FCOM PRO-ABN-HYD P 51/76, PDF 3740; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482] |
| F/CTL DIRECT LAW | Control reverts to direct law at landing gear extension | See the DIRECT LAW brief | [FCOM PRO-ABN-HYD P 53/76, PDF 3742; FCOM PRO-ABN-F_CTL P 18/132, PDF 3491] |

## 9. HS-TX differences
| Topic | HS-TXA..TXF | HS-TXG..TXU | Ref |
|---|---|---|---|
| QRH fuel penalty factor, G+B SYS LO PR (L+R AIL, SPLR 1+3+5, L ELEV, RAT extended) | 10 % to 15 % | 15 % to 20 % | [QRH OPS.04E, PDF 277; QRH OPS.04C, PDF 275] |

## 10. Gaps and omissions
- The FCTM and PDP give the sequence but no PF/PM slide for this failure: the turns come from the AOP-20 task sharing, FCTM AOP-30-60 and the QRH summary. The manuals do not say who turns the handcrank; the PM is shown from instructor practice. [FCTM AOP-20 P 1–2/10, PDF 68; FCTM AOP-30-60 P 1/4, PDF 92; PDP Use of summary, PDF 439]
- The DSC does not label the RAT MAN ON pushbutton as guarded, so no crosscheck is shown for it; the BLUE ELEC PUMP pb is labelled guarded. [FCOM DSC-29-20 P 3/10, PDF 1754; FCOM DSC-29-20 P 1/10, PDF 1752]
- The MAYDAY wording is not given in the supplied manuals. [FCTM PR-AEP-HYD P 2/4, PDF 439]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-HYD — HYD G+B SYS LO PR (HS-TX) | P 50–54/76 | 3739–3743 | 26 MAY 26 |
| QRH | 23.02 — summary; OPS.04 — fuel penalty factors | 23.02A–B · OPS.04C, E | 210–211, 275, 277 | 18 FEB 26, 14 JUL 26 |
| FCTM | PR-AEP-HYD · AOP-30-60 | P 1–4/4 · P 1–4/4 | 438–441, 92–95 | 26 MAY 26 |
| PDP | Use of summary (XFTDN1USESUMM01) | — | 436–442 |  |
| FCOM | DSC-29-20 · DSC-27-20-20 | P 1, 3/10 · P 3, 5/20 | 1752, 1754, 1614, 1616 | 18 FEB 26 |
