# ENG 1(2) FAIL — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · amber LAND ASAP · no memory items**  
**Applicability:** all HS-TX — ENG 1(2) FAIL and ENG 1(2) SHUT DOWN: one version for all HS-TX.

An engine fails after V1 (or at go-around). Below 400 ft the PF only flies: rudder to centre the beta target, 12.5° then SRS, gear up. At 400 ft the PF orders ECAM ACTIONS until the engine is secured, then calls STOP ECAM to level off at EO acceleration altitude, clean up and set MCT at green dot. CONTINUE ECAM takes the PM to the STATUS page, where the PF stops the ECAM again for the after-takeoff flow and a relight decision.

## 1. What it is
- **Trigger:** Engine core speed below idle with the ENG MASTER lever ON and the ENG FIRE pb not pushed. [FCOM PRO-ABN-ENG P 84/226, PDF 3331]
- **Flight phase inhibition:** none [FCOM PRO-ABN-ENG P 84/226, PDF 3331]
- Flameout causes include fuel starvation, volcanic ash/sand, heavy rain/hail/icing, bird strike, engine stall, control malfunction. [FCTM PR-AEP-ENG P 9/26, PDF 410]
- Suspect damage with two or more of: EGT above red line, rotor speed mismatch or no rotation, vibration/buffet, abnormal oil pressure/temperature, hydraulic loss, repeated stalls. [FCTM PR-AEP-ENG P 9/26, PDF 410; FCTM PR-AEP-ENG P 10/26, PDF 411]
- Takeoff with an engine failure: the blue beta target replaces the sideslip index; lateral normal law gives some rudder, the pilot completes it to centre the target. [FCTM PR-AEP-ENG P 11/26, PDF 412]
- When an engine failure is detected the FMGS gives engine-out predictions and deletes pre-selected speeds. [FCTM PR-AEP-ENG P 14/26, PDF 415]

## 2. Key limits
- **Rotation:** ≈3°/s to 12.5° pitch [FCTM PR-AEP-ENG P 10/26, PDF 411]
- **Minimum speed:** V2 (SRS: V2 to V2 +15 kt) [FCTM PR-AEP-ENG P 11/26, PDF 412; FCTM PR-AEP-ENG P 14/26, PDF 415]
- **READ & DO from:** 400 ft AGL [FCTM AOP-30-30 P 1/6, PDF 82]
- **Relight wait:** 30 s after ENG FAIL [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
- **Takeoff thrust:** 10 min max [FCTM PR-AEP-ENG P 11/26, PDF 412]
- **Final takeoff segment:** Green dot · MCT [FCTM PR-AEP-ENG P 12/26, PDF 413]

## 3. Flow (PF / PM)
### 1. Detection (below 400 ft: fly only)
**1.1 PF + PM**
- “ENGINE FAILURE” [PDP Engine failure after V1, PDF 495]
- First pilot who detects calls it [PDP Engine failure after V1, PDF 495]
**1.2 PF**
- Continue the takeoff; rudder to keep the centreline; rotate ≈3°/s towards 12.5° [FCTM PR-AEP-ENG P 10/26, PDF 411; PDP Engine failure after V1, PDF 495]
- Gear up; consider TOGA (FLEX takeoff); then follow the FD bars (SRS) [PDP Engine failure after V1, PDF 495; FCTM PR-AEP-ENG P 11/26, PDF 412]
- Centre the beta target with rudder, then rudder trim; consider AP [PDP Engine failure after V1, PDF 495; PDP Engine failure after V1, PDF 498; FCTM PR-AEP-ENG P 11/26, PDF 412]
- Navigate: amber LAND ASAP — consider the EO SID for the takeoff runway [PDP Engine failure after V1, PDF 495]
**1.3 PM**
- No READ & DO actions before 400 ft AGL (except gear up) [PDP Engine failure after V1, PDF 495; PDP Engine failure after V1, PDF 496; FCTM AOP-30-30 P 1/6, PDF 82]
- ATC …… NOTIFY [PDP Engine failure after V1, PDF 495]

### 2. ECAM actions (≥ 400 ft) — secure the engine
**2.1 PM**
- “ENG 1(2) FAIL” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-ENG P 84/226, PDF 3331]
**2.2 PF**
- “ECAM ACTIONS” [PDP Engine failure after V1, PDF 499; PDP Management of abnormal operations, PDF 424; FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]
- Fly, navigate, communicate; delay acceleration only to secure the engine [FCTM AOP-20 P 1–2/10, PDF 68; PDP Engine failure after V1, PDF 501]
**2.3 PM**
- ENG MODE SEL …… IGN [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- **During initial climb** [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
  - L/G …… UP [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- THR LEVER (AFFECTED ENGINE) …… IDLE [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
**2.4 PF**
- **Thrust lever (affected)** [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
  - PF moves it to IDLE after PM confirms the lever [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.5 PM**
- **IF NO ENG RELIGHT AFTER 30 S · IF NO RELIGHT** [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
  - “ENGINE MASTER 1 OFF — CONFIRM?” [PDP Management of abnormal operations, PDF 432]
  - PF verifies and answers “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
  - ENG MASTER (affected engine) …… OFF [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
  - **IF DAMAGE** [FCOM PRO-ABN-ENG P 86/226, PDF 3333; PDP Engine failure after V1, PDF 499]
    - ENG FIRE P/B (AFFECTED ENGINE) …… PUSH [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
    - AGENT 1 (AFTER 10 SECONDS IN FLIGHT) …… DISCH [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
- Engine secured = ENG MASTER OFF (no damage) or AGENT 1 DISCH (damage) [PDP Engine failure after V1, PDF 501; FCTM PR-AEP-ENG P 12/26, PDF 413]
- No damage: finish the ECAM first; consider relight at the STATUS page [PDP Engine failure after V1, PDF 499]

### 3. Acceleration (STOP ECAM)
**3.1 PF**
- “STOP ECAM” [PDP Engine failure after V1, PDF 500]
- Engine secured, before EO ACC ALT — do not exceed the maximum EO ACC ALT [PDP Engine failure after V1, PDF 500; PDP Engine failure after V1, PDF 501; FCTM PR-AEP-ENG P 12/26, PDF 413]
**3.2 PM**
- ECAM ACTIONS …… STOP [PDP Engine failure after V1, PDF 500]
**3.3 PF**
- V/S knob …… PUSH TO LEVEL OFF [PDP Engine failure after V1, PDF 500; FCTM PR-AEP-ENG P 12/26, PDF 413]
- “ALT (or V/S 0)” [PDP Engine failure after V1, PDF 500]
**3.4 PM**
- “CHECKED” [PDP Engine failure after V1, PDF 500]
- Checks the FMA after level-off [PDP Engine failure after V1, PDF 500]
**3.5 PF**
- Clean up the aircraft: flaps retraction on schedule (F, S speeds) [PDP Engine failure after V1, PDF 500; PDP Engine failure after V1, PDF 494]
- **Speed trend reaches GREEN DOT** [PDP Engine failure after V1, PDF 500]
  - ALT knob-selector …… PULL (OP CLB) [PDP Engine failure after V1, PDF 500; FCTM PR-AEP-ENG P 12/26, PDF 413]
- **LVR MCT flashes on the FMA** [PDP Engine failure after V1, PDF 500]
  - THRUST LEVER …… MCT [PDP Engine failure after V1, PDF 500; FCTM PR-AEP-ENG P 12/26, PDF 413]
  - Already in FLX/MCT: move to CL, then back to MCT [PDP Engine failure after V1, PDF 502; FCTM PR-AEP-ENG P 12/26, PDF 413]
- “THRUST MCT, OPEN CLIMB, AUTO THRUST” [PDP Engine failure after V1, PDF 500]
**3.6 PM**
- “CHECKED” [PDP Engine failure after V1, PDF 500]
- Checks THR MCT · OP CLB · A/THR on the FMA [PDP Engine failure after V1, PDF 500]

### 4. Continue ECAM → STATUS
**4.1 PF**
- “CONTINUE ECAM” [PDP Engine failure after V1, PDF 503; PDP Management of abnormal operations, PDF 426]
- Fly the EOSID / SID / radar vectors per the departure briefing [FCTM PR-AEP-ENG P 13/26, PDF 414]
**4.2 PM**
- ECAM ACTIONS …… CONTINUE [PDP Engine failure after V1, PDF 503]
- ENG SHUT DOWN ECAM (see procedure) until the STATUS page [FCTM PR-AEP-ENG P 13/26, PDF 414; FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- “STATUS” [PDP Management of abnormal operations, PDF 426; FCTM AOP-30-30 P 3/6, PDF 84]

### 5. STATUS (STOP ECAM again)
**5.1 PF**
- “STOP ECAM” [PDP Management of abnormal operations, PDF 426; FCTM AOP-30-30 P 3/6, PDF 84]
**5.2 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**5.3 PF**
- Acceleration flow pattern / After Takeoff C/L; system resets per QRH [PDP Engine failure after V1, PDF 503; PDP Management of abnormal operations, PDF 426; FCTM AOP-30-30 P 4/6, PDF 85]
- **No damage** [PDP Engine failure after V1, PDF 503]
  - Consider ENG RELIGHT (QRH procedure) [PDP Engine failure after V1, PDF 503; FCOM PRO-ABN-ENG P 173/226, PDF 3420]
- “CONTINUE ECAM” [PDP Management of abnormal operations, PDF 426]
**5.4 PM**
- Read the whole STATUS page [PDP Management of abnormal operations, PDF 426; FCTM AOP-30-30 P 3/6, PDF 84]
- “REMOVE STATUS?” [PDP Management of abnormal operations, PDF 426]
**5.5 PF**
- “REMOVE STATUS” [PDP Management of abnormal operations, PDF 426; FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]
**5.6 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 6. Approach preparation
**6.1 PF**
- “YOU HAVE CONTROL?” [PDP Engine failure after V1, PDF 504]
**6.2 PM**
- “I HAVE CONTROL” [PDP Engine failure after V1, PDF 504]
**6.3 PF**
- FMS …… PREPARE [PDP Engine failure after V1, PDF 504]
- ARRIVAL BRIEFING …… PERFORM [PDP Engine failure after V1, PDF 504]
**6.4 PM**
- FMS PREPARATION …… CHECK [PDP Engine failure after V1, PDF 504]
- One engine out landing: late in the approach, on PF request, reset the rudder trim to zero [PDP Engine failure after V1, PDF 504]

### 7. Engine failure at go-around
**7.1 PF**
- TOGA, rudder promptly to centre the beta target [FCTM PR-AEP-ENG P 23/26, PDF 424]
- Flap 1 or more: follow SRS; no SRS → 12.5° pitch [FCTM PR-AEP-ENG P 23/26, PDF 424]
- Lateral mode GA TRK (or NAV) — consider terrain [FCTM PR-AEP-ENG P 24/26, PDF 425]
**7.2 PM**
- “ENG 1(2) FAIL” [FCTM AOP-30-30 P 2/6, PDF 83]
- ECAM actions on PF order, as above [FCTM AOP-30-30 P 3/6, PDF 84]
**7.3 PF**
- EO acceleration altitude: same sequence as after V1 (STOP ECAM, level off, accelerate, MCT, CONTINUE ECAM) [FCTM PR-AEP-ENG P 24/26, PDF 425; PDP Engine failure after V1, PDF 500]

## 4. Procedure
### ENG 1(2) FAIL — in flight (FCOM PRO-ABN-ENG)
- **LAND ASAP (amber)** [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- ENG MODE SEL …… IGN — Confirms the immediate relight attempt made by the FADEC. [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- **During initial climb:** [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
  - L/G …… UP [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- THR LEVER (AFFECTED ENGINE) …… IDLE [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- *GPWS alerts: reduce speed with care below VLS with flaps extended (at light weights VMCA may be reached before αMax).* [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
- **IF NO ENG RELIGHT AFTER 30 S:** [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
  - *The 30 s countdown starts when ENG 1(2) FAIL triggers.* [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
  - **IF NO RELIGHT:** [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
    - ENG MASTER (affected engine) …… OFF [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
    - **IF DAMAGE:** [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
      - ENG FIRE P/B (AFFECTED ENGINE) …… PUSH [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
      - AGENT 1 (AFTER 10 SECONDS IN FLIGHT) …… DISCH [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
      - *Associated: ENG 1(2) SHUT DOWN if damage or relight unsuccessful.* [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
    - **IF NO DAMAGE:** [FCOM PRO-ABN-ENG P 86/226, PDF 3333]
      - ENG (AFFECTED) RELIGHT …… CONSIDER — Apply [QRH] ENG RELIGHT IN FLIGHT. [FCOM PRO-ABN-ENG P 86/226, PDF 3333]

### ENG 1(2) SHUT DOWN (FCOM PRO-ABN-ENG)
- **LAND ASAP (amber)** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- **If wing anti-ice ON:** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - PACK (AFFECTED SIDE) …… OFF — If ELEC EMER CONFIG: PACK 1 OFF. [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - **If ENG FIRE pb not pushed:** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
    - X BLEED …… OPEN [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- ENG MODE SEL …… IGN [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- **During initial climb:** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - L/G …… UP [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- **IF NO FUEL LEAK:** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - IMBALANCE …… MONITOR [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- TCAS MODE SEL …… TA [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- **If REV unlocked · IF BUFFET:** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - MAX SPEED …… 240 KT [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
- **If ENG FIRE pb-sw pushed:** [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - X BLEED …… SHUT [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - WING ANTI ICE …… OFF [FCOM PRO-ABN-ENG P 170/226, PDF 3417]
  - *AVOID ICING CONDITIONS* [FCOM PRO-ABN-ENG P 170/226, PDF 3417]

## 5. STATUS
**Limitations**
- If ENG FIRE pb-sw pushed: AVOID ICING CONDITIONS [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- If REV unlocked: MAX SPEED 300/0.78 [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
**Information**
- IF NO ENG DAMAGE: CONSIDER ENG RELIGHT [FCOM PRO-ABN-ENG P 173/226, PDF 3420]
- CAT 3 SINGLE ONLY · ONE PACK ONLY IF WAI ON [FCOM PRO-ABN-ENG P 173/226, PDF 3420]
- APU may be started and APU GEN used; APU bleed not to be used if ENG 1 FIRE pb pushed. [FCOM PRO-ABN-ENG P 173/226, PDF 3420]
- If WING A/ICE off and ENG FIRE pb not pressed — IF PERF PERMITS: X BLEED OPEN (no obstacle constraint). [FCOM PRO-ABN-ENG P 173/226, PDF 3420]
**APPR PROC**
- **If REV unlocked (buffet): reverser-specific APPR PROC — see FCOM** [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
**INOP SYS**
- CAT 3 DUAL [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- ENG 1(2) BLEED [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- PACK 1(2) [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- MAIN GALLEY [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- GEN 1(2) [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- G ENG 1 PUMP or Y ENG 2 PUMP [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- WING A. ICE (if ENG FIRE pb pushed) [FCOM PRO-ABN-ENG P 172/226, PDF 3419]
- STEEP APPR [FCOM PRO-ABN-ENG P 172/226, PDF 3419]

## 7. FCTM technique
- Aircraft handling first: stabilise pitch, speed and path before the ECAM. [FCTM PR-AEP-ENG P 10/26, PDF 411]
- Failure above V2: keep the SRS attitude; minimum speed V2. [FCTM PR-AEP-ENG P 14/26, PDF 415]
- "Secure the engine" = ENG MASTER OFF (no damage), AGENT 1 DISCH (damage), fire out or AGENT 2 DISCH (fire). [FCTM PR-AEP-ENG P 12/26, PDF 413]
- With AP engaged the rudder trim is managed by the AP; release rudder pedal pressure. [FCTM PR-AEP-ENG P 11/26, PDF 412]
- Do not exceed the EO maximum acceleration altitude if acceleration is delayed. [FCTM PR-AEP-ENG P 12/26, PDF 413]
- In cruise: MCT, A/THR off, set heading, standard strategy M.78/300 kt, descend to EO recovery altitude, never below green dot. [FCTM PR-AEP-ENG P 15/26, PDF 416]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] ENG RELIGHT IN FLIGHT | No damage, relight considered | See the ENG RELIGHT brief | [FCOM PRO-ABN-ENG P 4–5/226, PDF 3251] |
| ONE ENGINE INOPERATIVE — GO-AROUND | Engine failure at go-around | TOGA + prompt rudder; SRS or 12.5°; GA TRK — terrain | [FCTM PR-AEP-ENG P 23/26, PDF 424; FCTM PR-AEP-ENG P 24/26, PDF 425] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- Thrust-malfunction and on-ground branches of ENG FAIL are not shown in the flow; this brief covers the in-flight case. [FCOM PRO-ABN-ENG P 85/226, PDF 3332]
- Callout wording differs slightly between sources: FCOM "ECAM ACTION" / "ECAM ACTIONS COMPLETE" vs PDP and FCTM "ECAM ACTIONS" / "ECAM ACTIONS COMPLETED". The PDP is a generic Airbus tutorial; FCOM wording is shown where both exist. [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 424; PDP Management of abnormal operations, PDF 426]
- HS-TO-only versions omitted (FCOM P 87–89 and P 174–183/226). [FCOM PRO-ABN-ENG P 87–89/226, PDF 3334]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ENG — ENG 1(2) FAIL | P 84–86/226 | 3331–3333 | 26 MAY 26 |
| FCOM | PRO-ABN-ENG — ENG 1(2) SHUT DOWN | P 169–173/226 | 3416–3420 | 26 MAY 26 |
| FCTM | PR-AEP-ENG — engine failure after V1, initial climb, cruise, OEI go-around | P 9–15, 23–24/26 | 410–416, 424–425 | 26 MAY 26 |
| PDP | Engine failure after V1 (XFTDA10ENGFTO01) | Detection → Approach preparation | 494–504 | JAN 2024 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, confirmation, STATUS | 424–432 | JAN 2024 |
| FCTM | AOP-20 · AOP-30 | — | 68–95 | 26 MAY 26 |
