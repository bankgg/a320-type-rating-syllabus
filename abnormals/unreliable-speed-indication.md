# UNRELIABLE SPEED INDICATION · SEVERE TURBULENCE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Memory items · memory items**  
**Applicability:** HS-TXA..TXF, HS-TXG..TXU — Unreliable speed: one version for all HS-TX. Severe turbulence N1 table differs HS-TXA..TXF / HS-TXG..TXU.

If the safe conduct of the flight is affected, fly the memory pitch/thrust, then level off and stabilise using the QRH pitch/thrust tables while the PM identifies and isolates the faulty ADR. This brief also compares the QRH table with the Severe Turbulence table: unreliable speed gives pitch and thrust to fly without trusting speed, while severe turbulence keeps the AP on and sets a target speed/Mach with a reference N1.

## 1. What it is
- **Trigger:** ADR CHECK PROC APPLY on ECAM (e.g. NAV ADR DISAGREE), or crew suspicion: speed discrepancies, fluctuating IAS/altitude, abnormal pitch/thrust/speed correlation, abnormal AP/FD/A/THR behaviour, stall/overspeed warning contradicting IAS. [FCTM PR-AEP-NAV P 14/20, PDF 491; FCTM PR-AEP-NAV P 15/20, PDF 492]
- **Flight phase inhibition:** none [FCTM PR-AEP-NAV P 14/20, PDF 491; FCTM PR-AEP-NAV P 15/20, PDF 492]
- Most likely cause: obstruction of pitot and/or static probes; probes rarely clog identically, so the first sign is usually a discrepancy between CAPT PFD, F/O PFD and STBY. [FCTM PR-AEP-NAV P 2/20, PDF 479]
- Systems vote across three ADRs; two consistent but wrong ADRs can out-vote the correct one (e.g. two pitots blocked the same way). [FCTM PR-AEP-NAV P 2/20, PDF 479; FCTM PR-AEP-NAV P 3/20, PDF 480]
- Above FL 250 unreliable speed is mostly temporary (water/ice) and clears in minutes; at low altitude it is mostly permanent. [FCTM PR-AEP-NAV P 4/20, PDF 481]
- Erroneous barometric altitude affects FPV, V/S and the transponder — advise ATC. [FCTM PR-AEP-NAV P 4/20, PDF 481]

## 2. Key limits
- **Below THR RED ALT:** 15° / TOGA [FCOM PRO-ABN-NAV P 1/124, PDF 3826; QRH 26.02A, PDF 235]
- **THR RED ALT – FL 100:** 10° / CLB [FCOM PRO-ABN-NAV P 1/124, PDF 3826; QRH 26.02A, PDF 235]
- **Above FL 100:** 5° / CLB [FCOM PRO-ABN-NAV P 1/124, PDF 3826; QRH 26.02A, PDF 235]
- **Level-off pitch, clean:** 4° (≤ FL 250) · 3° (above) [QRH 26.02C, PDF 237]
- **Severe turbulence target:** 275 kt · M.76 at FL 330+ [QRH 25.08A–B, PDF 226; QRH 25.08B–C, PDF 227]

## 3. Flow (PF / PM)
### 1. Memory items (if safe flight is affected)
**1.1 PF + PM**
- “UNRELIABLE SPEED” [FCOM PRO-ABN-ABN-00 P 9/12, PDF 2832]
**1.2 PF**
- AP / A/THR / FD …… OFF [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- PITCH/THRUST …… 15°/TOGA · 10°/CLB · 5°/CLB [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- FLAPS …… MAINTAIN (CONF FULL → CONF 3) [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- SPEEDBRAKES …… CHECK RETRACTED [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- L/G …… UP [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- Once pitch/thrust are stable, go to the QRH without delay — memory values held too long can exceed speed limits [FCTM PR-AEP-NAV P 17/20, PDF 494]
**1.3 PM**
- Confirm discrepancies: STBY vs own PFD, own PFD vs PF PFD [FCTM PR-AEP-NAV P 15/20, PDF 492]
- Rely on the STALL warning (AOA-based) [FCTM PR-AEP-NAV P 15/20, PDF 492]

### 2. Level off (QRH procedure)
**2.1 PF**
- At or above MSA / circuit altitude: level off for troubleshooting [FCOM PRO-ABN-NAV P 1/124, PDF 3826; PDP Unreliable speed indication, PDF 557]
- AP …… OFF [PDP Unreliable speed indication, PDF 559; FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- “FDs OFF” [PDP Unreliable speed indication, PDF 559]
**2.2 PM**
- FDs …… OFF [PDP Unreliable speed indication, PDF 559]
**2.3 PF**
- A/THR …… OFF [PDP Unreliable speed indication, PDF 559; FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- SPEEDBRAKES …… CHECK RETRACTED [PDP Unreliable speed indication, PDF 559; FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- PITCH/THRUST …… APPLY [PDP Unreliable speed indication, PDF 559; QRH 26.02C, PDF 237]
**2.4 PM**
- PITCH/THRUST …… DETERMINE FROM QRH TABLE [PDP Unreliable speed indication, PDF 559; QRH 26.02C, PDF 237]
**2.5 PF**
- LEVEL OFF …… PERFORM [PDP Unreliable speed indication, PDF 559]
- Pitch above target → more thrust; below → less thrust. Altitude unreliable → GPS altitude (MCDU GPS MONITOR) [FCOM PRO-ABN-NAV P 1/124, PDF 3826; QRH 26.02C, PDF 237; PDP Unreliable speed indication, PDF 560]
- Below FL 250: reversible BUSS if installed [PDP Unreliable speed indication, PDF 559]
- **If needed and reliable (bird reliable if baro altitude reliable)** [PDP Unreliable speed indication, PDF 559]
  - “BIRD ON” [PDP Unreliable speed indication, PDF 559]
**2.6 PM**
- **After “BIRD ON”** [PDP Unreliable speed indication, PDF 559]
  - TRK/FPA (BIRD) …… SELECT [PDP Unreliable speed indication, PDF 559]
**2.7 PF + PM**
- “RESPECT STALL WARNING” [FCOM PRO-ABN-NAV P 2/124, PDF 3827; PDP Unreliable speed indication, PDF 559]

### 3. Flight path stabilised
**3.1 PF**
- AP / A/THR …… OFF [PDP Unreliable speed indication, PDF 561; FCOM PRO-ABN-NAV P 2/124, PDF 3827]
**3.2 PM**
- FDs …… OFF [PDP Unreliable speed indication, PDF 561]
**3.3 PF**
- SPEEDBRAKES …… CHECK RETRACTED [PDP Unreliable speed indication, PDF 561]
- FLIGHT PATH …… KEEP STABILIZED [PDP Unreliable speed indication, PDF 561; FCOM PRO-ABN-NAV P 2/124, PDF 3827]

### 4. Identify the faulty ADR
**4.1 PF**
- Advise ATC without delay (altitude may be wrong) [FCTM PR-AEP-NAV P 4/20, PDF 481]
**4.2 PM**
- PROBE/WINDOW HEAT …… ON [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- ALL SPEED INDICATIONS …… CROSSCHECK [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- ADR3 and STBY speed use the same probe [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- **At least one ADR confirmed reliable** [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - RELIABLE AIR DATA …… USE [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - UNRELIABLE ADR pb(s) …… OFF [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- **Cannot identify / all affected — above FL 250** [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - KEEP ONE ADR ON [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - TWO ADR pbs …… OFF [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - ATC/XPDR …… ALT RPTG OFF [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - Flight continuation: pitch/thrust tables [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- **Below FL 250, speed still unreliable** [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - ALL ADR pbs …… OFF [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - SPEED …… FLY THE GREEN (BUSS) [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
  - NAV ADR 1+2+3 FAULT ECAM …… APPLY [FCOM PRO-ABN-NAV P 3/124, PDF 3828]
- ADR pbs are switched off with the pb — not the rotary selector [FCTM PR-AEP-NAV P 2/20, PDF 479]

### 5. Continue the flight
**5.1 PF**
- Fly pitch/thrust by phase — climb, cruise, descent, approach — early stabilised approach [FCOM PRO-ABN-NAV P 4/124, PDF 3829; FCTM PR-AEP-NAV P 14/20, PDF 491]
**5.2 PM**
- Read the table for each phase; radome damage → +5 % N1, fuel flow +27 % [FCOM PRO-ABN-NAV P 4/124, PDF 3829; QRH 26.02E, PDF 239]

### 6. Compare: Severe turbulence (QRH 25.08)
**6.1 PF**
- SEAT BELTS …… ON [QRH 25.08A–B, PDF 226]
- KEEP AUTO PILOT ON; excessive thrust variations → disconnect A/THR [QRH 25.08A–B, PDF 226]
- Target 275 kt (FL 200–310) / M.76 (FL 330+), 250 kt at FL 150 and below [QRH 25.08A–B, PDF 226; QRH 25.08B–C, PDF 227]
- Consider descending to or below OPT FL for buffet margin [QRH 25.08A–B, PDF 226]
**6.2 PM**
- SPEED AND THRUST …… ADJUST (table N1 by FL / weight) [QRH 25.08A–B, PDF 226; QRH 25.08B–C, PDF 227]
- **For approach** [QRH 25.08A–B, PDF 226]
  - A/THR …… ON [QRH 25.08A–B, PDF 226]
  - USE MANAGED SPEED [QRH 25.08A–B, PDF 226]

## 4. Procedure
### [MEM] UNRELIABLE SPEED INDICATION — memory items (FCOM PRO-ABN-NAV / QRH 26.02)
- **If the safe conduct of the flight is impacted:** [FCOM PRO-ABN-NAV P 1/124, PDF 3826; QRH 26.02A, PDF 235]
  - AP …… OFF [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - A/THR …… OFF [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - FD …… OFF [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - *PITCH/THRUST:* [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
    - Below THRUST RED ALT …… 15° / TOGA [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
    - Above THRUST RED ALT and Below FL 100 …… 10° / CLB [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
    - Above THRUST RED ALT and Above FL 100 …… 5° / CLB [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - FLAPS (if CONF 0(1)(2)(3)) …… MAINTAIN CURRENT CONF [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - FLAPS (if CONF FULL) …… SELECT CONF 3 AND MAINTAIN [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - SPEEDBRAKES …… CHECK RETRACTED [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - L/G …… UP [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - *When at, or above MSA or Circuit Altitude: Level off for troubleshooting.* [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
- **To level off:** [FCOM PRO-ABN-NAV P 1/124, PDF 3826]
  - PITCH/THRUST TABLE …… APPLY [FCOM PRO-ABN-NAV P 1/124, PDF 3826; QRH 26.02C, PDF 237]
- **When flight path is stabilized:** [FCOM PRO-ABN-NAV P 2/124, PDF 3827]
  - FLIGHT PATH …… KEEP STABILIZED [FCOM PRO-ABN-NAV P 2/124, PDF 3827]
- *RESPECT STALL WARNING* [FCOM PRO-ABN-NAV P 2/124, PDF 3827]

### SEVERE TURBULENCE (QRH 25.08)
- SEAT BELTS …… ON [QRH 25.08A–B, PDF 226]
- SPEED AND THRUST …… ADJUST — Use the speed/Mach and N1 table. [QRH 25.08A–B, PDF 226]
- *KEEP AUTO PILOT ON* [QRH 25.08A–B, PDF 226]
- **If excessive thrust variations:** [QRH 25.08A–B, PDF 226]
  - A/THR …… DISCONNECT [QRH 25.08A–B, PDF 226]
- DESCENT TO OR BELOW OPT FL …… CONSIDER — Increases the margin to buffet. [QRH 25.08A–B, PDF 226]
- **For approach:** [QRH 25.08A–B, PDF 226]
  - A/THR …… ON [QRH 25.08A–B, PDF 226]
  - *USE MANAGED SPEED* [QRH 25.08A–B, PDF 226]

## 6. QRH and reference tables
### Unreliable speed — level flight, clean (thrust % N1, resultant speed) 
Pitch 4° at or below FL 250 · 3° above FL 250.

| FL | 80 t | 70 t | 60 t | 50 t |
|---|---|---|---|---|
| 100 | 64% (265 kt) | 60% (245 kt) | 56% (225 kt) | 52% (205 kt) |
| 200 | 72% (260 kt) | 68% (245 kt) | 66% (225 kt) | 60% (205 kt) |
| 300 | 78% (280 kt) | 76% (265 kt) | 74% (245 kt) | 70% (225 kt) |
| 350 | / | 80% (255 kt) | 76% (240 kt) | 74% (225 kt) |
| 400 | / | / | 82% (235 kt) | 78% (220 kt) |
[QRH 26.02C, PDF 237; QRH 26.02D, PDF 238]

### Severe turbulence — target speed and N1 (%) **[HS-TXG..TXU]** 
Selected weights shown; full table 44–76 t in QRH 25.08.

| FL | SPD / Mach | 52 t | 60 t | 68 t |
|---|---|---|---|---|
| 390 | .76 | 77.1 | — | — |
| 350 | .76 | 75.3 | 76.7 | 78.5 |
| 310 | 275 | 74.6 | 75.6 | 76.8 |
| 250 | 275 | 71.8 | 72.6 | 73.8 |
| 200 | 275 | 68.4 | 69.3 | 70.4 |
| 150 | 250 | 61.8 | 63.2 | 65.0 |
| 100 | 250 | 57.5 | 58.6 | 60.8 |
[QRH 25.08A–B, PDF 226]

### Severe turbulence — target speed and N1 (%) **[HS-TXA..TXF]** 
Selected weights shown; full table 44–76 t in QRH 25.08.

| FL | SPD / Mach | 52 t | 60 t | 68 t |
|---|---|---|---|---|
| 390 | 0.76 | 77.7 | — | — |
| 350 | 0.76 | 75.6 | 77.1 | 79.3 |
| 310 | 275 | 74.7 | 75.8 | 77.1 |
| 250 | 275 | 71.0 | 71.9 | 73.2 |
| 200 | 275 | 67.4 | 68.4 | 69.8 |
| 150 | 250 | 61.0 | 62.5 | 64.5 |
| 100 | 250 | 57.2 | 58.5 | 60.3 |
[QRH 25.08B–C, PDF 227]

## 7. FCTM technique
- Two objectives: fly the aircraft, then identify and isolate the affected ADR(s). [FCTM PR-AEP-NAV P 14/20, PDF 491]
- Apply the memory items when in doubt about flying safely in the short term with current parameters. [FCTM PR-AEP-NAV P 16/20, PDF 493]
- Rely on the STALL warning — it is AOA-based and not affected by erroneous airspeed. [FCTM PR-AEP-NAV P 15/20, PDF 492]
- Do not instinctively reject an outlier ADR: two or even three ADRs can give identical but erroneous data. [FCTM PR-AEP-NAV P 17–18/20, PDF 494]
- Change one parameter at a time (speed, altitude or configuration); GPS altitude is on the MCDU GPS MONITOR page. [FCTM PR-AEP-NAV P 17–18/20, PDF 494]
- Approach: early stabilised approach; configure wings level using back-up speeds (VMAX = VFE/VMO, VMIN = VSW). [FCTM PR-AEP-NAV P 14/20, PDF 491]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| NAV ADR 1+2+3 FAULT | All ADRs switched off below FL 250 | Apply the ECAM procedure | [FCOM PRO-ABN-NAV P 3/124, PDF 3828] |

## 9. HS-TX differences
| Topic | HS-TXA..TXF | HS-TXG..TXU | Ref |
|---|---|---|---|
| Severe turbulence N1 table | QRH 25.08B–C values (e.g. FL 350, 60 t: 77.1 %) | QRH 25.08A–B values (e.g. FL 350, 60 t: 76.7 %) | [QRH 25.08A–B, PDF 226; QRH 25.08B–C, PDF 227] |

## 10. Gaps and omissions
- Full pitch/thrust and severe-turbulence tables are abridged here; read the QRH tables for the actual weight. [QRH 26.02C, PDF 237; QRH 25.08A–B, PDF 226]
- HS-TO versions (A321 weights) omitted. [FCOM PRO-ABN-NAV P 5–8/124, PDF 3830]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — [MEM] UNRELIABLE SPEED INDICATION | P 1–4/124 | 3826–3829 | 26 MAY 26 |
| QRH | 26.02 UNRELIABLE SPEED INDICATION | 26.02A–E | 235–239 | 26 MAY 26 |
| QRH | 25.08 SEVERE TURBULENCE | 25.08A–C | 226–228 | 18 FEB 26 |
| FCTM | PR-AEP-NAV — unreliable airspeed | P 2–4, 14–16/20 | 479–481, 491–493 | 26 MAY 26 |
| PDP | Unreliable speed indication (XFTDA6UNRASPD01) | Memory item, level off, flight path stabilized | 557–561 | JUN 2023 |
