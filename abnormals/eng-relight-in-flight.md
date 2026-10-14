# ENG RELIGHT IN FLIGHT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** all HS-TX — Same procedure for all HS-TX.

A QRH (paper) procedure for restarting an engine that failed without damage. Check the relight envelope, set the failed engine to IDLE/IGN with crossbleed open, then ENG MASTER ON and watch N2/EGT — there is no automatic start abort in flight.

## 1. What it is
- **Trigger:** QRH procedure, considered from ENG 1(2) FAIL (no damage) or STATUS "CONSIDER ENG RELIGHT". [FCOM PRO-ABN-ENG P 4/226, PDF 3251; QRH 19.06B, PDF 175]
- **Flight phase inhibition:** none [FCOM PRO-ABN-ENG P 4/226, PDF 3251; QRH 19.06B, PDF 175]
- The relight can be a windmilling start or a starter-assisted relight using bleed from the other engine. [FCTM PR-AEP-ENG P 9/26, PDF 410]
- Unlike a ground auto start, the crew must act on an abnormal start. [FCOM PRO-ABN-ENG P 5/226, PDF 3252]

## 2. Key limits
- **Light-up:** within 30 s of fuel flow [FCOM PRO-ABN-ENG P 5/226, PDF 3252; QRH 19.06C, PDF 176]
- **Failed attempt:** N2 < 50 % within 70 s [QRH 19.06B, PDF 175]
- **Before retry:** wait 30 s (drain) [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- **Windmill relight:** ≥ 270 kt [QRH 19.06B, PDF 175]

## 3. Flow (PF / PM)
### 1. Decide
**1.1 PF**
- Only with no engine damage, no fire shutdown and no risk of fire [FCOM PRO-ABN-ENG P 4/226, PDF 3251]
- Choose relight type from the envelope (starter-assisted / windmill) [QRH 19.06B, PDF 175]
**1.2 PM**
- Open QRH ENG RELIGHT — IN FLIGHT (keep the ECAM displayed) [QRH 19.06B, PDF 175; FCTM AOP-30-30 P 2/6, PDF 83]
- From ENG 1(2) FAIL: recommended at the STATUS page once all ECAM actions are done [PDP Engine failure after V1, PDF 499]

### 2. Order the QRH procedure
**2.1 PF**
- “ENG RELIGHT PROCEDURE” [PDP Management of abnormal operations, PDF 427]
- PF orders “(name) PROCEDURE”, then flies and communicates [PDP Management of abnormal operations, PDF 427]
**2.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427]

### 3. Set up
**3.1 PM**
- ENG MASTER (affected engine) …… OFF [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- THR LEVER (affected engine) …… Check IDLE [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
**3.2 PF**
- Thrust lever of the affected engine: confirm IDLE [FCOM PRO-ABN-ENG P 5/226, PDF 3252; FCTM AOP-30-20 P 1/2, PDF 80]
**3.3 PM**
- ENG MODE sel …… IGN [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- X BLEED …… OPEN [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- WING ANTI ICE (for starter assist) …… OFF [FCOM PRO-ABN-ENG P 5/226, PDF 3252]

### 4. Start
**4.1 PM**
- ENG MASTER (affected engine) …… ON [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- ENG PARAMETERS (N2, EGT) …… MONITOR [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- Light-up within 30 s after fuel flow increases — AUTOMATIC START ABORT NOT AVAIL [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
**4.2 PF**
- Unsure of the relight? Move the thrust lever forward and check the response [FCOM PRO-ABN-ENG P 5/226, PDF 3252]

### 5. Result
**5.1 PM**
- **When idle reached (ENG AVAIL)** [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - ENG MODE sel …… NORM [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - TCAS MODE sel …… TA/RA [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - X BLEED …… AUTO [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - Affected SYS …… RESTORE [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- **If no relight** [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - ENG MASTER (affected engine) …… OFF [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - Wait 30 s before a new start (drain) [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- “ENG RELIGHT PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### ENG RELIGHT — IN FLIGHT (FCOM PRO-ABN-ENG [QRH] / QRH 19.06)
- *No attempt if engine damage, if shut down for fire, or if a relight may cause fire.* [FCOM PRO-ABN-ENG P 4/226, PDF 3251]
- ENG MASTER (affected engine) …… OFF [FCOM PRO-ABN-ENG P 5/226, PDF 3252; QRH 19.06B, PDF 175]
- THR LEVER (affected engine) …… Check IDLE [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- ENG MODE sel …… IGN [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- X BLEED …… OPEN — Outside the windmilling envelope the FADEC opens the starter valve. [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- WING ANTI ICE (for starter assist) …… OFF [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- ENG MASTER (affected engine) …… ON [FCOM PRO-ABN-ENG P 5/226, PDF 3252; QRH 19.06C, PDF 176]
- ENG PARAMETERS (N2, EGT) …… MONITOR [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- *AUTOMATIC START ABORT NOT AVAIL* [FCOM PRO-ABN-ENG P 5/226, PDF 3252; QRH 19.06C, PDF 176]
- **When idle reached (ENG AVAIL):** [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - ENG MODE sel …… NORM [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - TCAS MODE sel …… TA/RA [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - X BLEED …… AUTO [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - Affected SYS …… RESTORE [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
- **If no relight:** [FCOM PRO-ABN-ENG P 5/226, PDF 3252]
  - ENG MASTER (affected engine) …… OFF — Wait 30 s before attempting a new start. [FCOM PRO-ABN-ENG P 5/226, PDF 3252; QRH 19.06B, PDF 175]
  - *If N2 does not increase above 50 % within 70 s, consider the relight unsuccessful; consider a windmill relight at minimum 270 kt.* [QRH 19.06B, PDF 175]

## 6. QRH and reference tables
### Engine relight envelope (QRH 19.06B) 
Read the chart in the QRH; zones summarised.

| Zone | Relight type |
|---|---|
| 1 | Starter-assisted relight (N2 ≤ 18 %), lower speeds |
| 2 | Windmill quick relight if N2 > 18 % |
| 3 | Stabilised windmill relight, higher speeds up to MMO |
[QRH 19.06B, PDF 175]

## 7. FCTM technique
- The crew may stop the relight procedure at any time if the situation requires (time, distance to fly). [FCTM PR-AEP-ENG P 9/26, PDF 410]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG 1(2) FAIL | Calls for ENG RELIGHT CONSIDER if no damage | See the ENG 1(2) FAIL brief | [FCOM PRO-ABN-ENG P 86/226, PDF 3333] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- Envelope boundaries are graphical — use the QRH chart; values are not transcribed. [QRH 19.06B, PDF 175]
- HS-TO version omitted (FCOM P 1–3/226, QRH 19.06A). [FCOM PRO-ABN-ENG P 1/226, PDF 3248]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ENG — [QRH] ENG RELIGHT IN FLIGHT | P 4–5/226 | 3251–3252 | 26 MAY 26 |
| QRH | 19.06 ENG RELIGHT | 19.06B–C | 175–176 | 18 FEB 26 |
| FCTM | PR-AEP-ENG | P 9/26 | 410 | 26 MAY 26 |
| PDP | Management of abnormal operations — QRH procedures (XFTDN6ECAM00001) | QRH procedures | 427 | JAN 2024 |
