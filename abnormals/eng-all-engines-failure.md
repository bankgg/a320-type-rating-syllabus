# ENG ALL ENGINES FAILURE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX: 280/0.77 optimum relight speed, windmill relight approaching or below FL 300.

All engines fail: the captain side keeps PFD 1 and the left-seat pilot flies, in alternate law with no AP, FD or A/THR. The PM runs a short ECAM (RAT and emergency generator, 280/0.77, APU, idle, FAC 1 reset, glide range), then goes straight to the QRH ALL ENG FAIL. If fuel remains and the engines are not damaged, try windmill relights on both engines, then starter-assisted relights below FL 200. If nothing relights, the QRH continues to a forced landing or ditching: those sections are under From the manuals, not in the flow.

## 1. What it is
- **Trigger:** All engines are failed in flight. [FCOM PRO-ABN-ENG P 37/226, PDF 3284]
- **Flight phase inhibition:** phases 1, 2, 3, 4, 8, 9, 10 [FCOM PRO-ABN-ENG P 37/226, PDF 3284]
- Thrust is lost so that level flight cannot be held. The alert may not trigger on a partial loss of thrust: the crew then decides between ALL ENG FAIL (time for a relight) and EMER LANDING (no time). [FCTM PR-AEP-ENG P 1/26, PDF 402; FCTM PR-AEP-ENG P 2/26, PDF 403]
- This alert inhibits ELEC EMER CONFIG. Its purpose is to secure RAT extension and emergency generator connection, then send the crew to the QRH. [FCOM PRO-ABN-ENG P 38/226, PDF 3285]
- All AC busbars are lost; the RAT supplies the emergency generator, which feeds AC ESS and DC ESS. Green and yellow hydraulics are lost; the RAT pressurizes blue. [FCTM PR-AEP-ENG P 2/26, PDF 403]
- Each APU start attempt takes about 3.5 min off the battery time; total battery time is more than 30 min. [FCTM PR-AEP-ENG P 2/26, PDF 403]
- The right aileron is lost and floats; the PF may use rudder trim to balance it instead of holding a stick input. It returns when the APU generator connects (ELAC 2). [FCTM PR-AEP-ENG P 2/26, PDF 403; FCTM PR-AEP-ENG P 3/26, PDF 404]
- Windmill relight is preferred: it works over a wide altitude range, tries all engines at once and does not depend on aircraft systems. [FCTM PR-AEP-ENG P 5/26, PDF 406]

## 2. Key limits
- **Optimum relight speed:** 280/0.77 [FCOM PRO-ABN-ENG P 38/226, PDF 3285; QRH 19.01A, PDF 162]
- **Windmill relight:** Approaching or below FL 300 [QRH 19.02A, PDF 164]
- **Starter-assisted relight:** Below FL 200 · APU bleed · green dot · one engine at a time [QRH 19.02A, PDF 164; FCTM PR-AEP-ENG P 7/26, PDF 408]
- **Glide:** 2 NM / 1000 FT at 280 kt · 2.5 NM / 1000 FT at green dot [QRH 19.01B, PDF 163; QRH 19.03A, PDF 167]
- **Minimum RAT speed:** 140 kt [FCOM PRO-ABN-ENG P 40/226, PDF 3287; QRH 19.04A, PDF 170; QRH 19.05B, PDF 172]
- **Max speed · max brake pressure:** 320/0.77 · 1000 PSI [FCOM PRO-ABN-ENG P 40/226, PDF 3287]

## 3. Flow (PF / PM)
### 1. Detection — fly first
**1.1 PF + PM**
- Golden rule 1: fly, navigate, communicate [FCTM PR-AEP-ENG P 5/26, PDF 406; PDP All engine flameout, PDF 443]
**1.2 PF**
- CM1 (left seat) is PF: only PFD 1 is available. Take over and establish a safe flight path [FCTM PR-AEP-ENG P 5/26, PDF 406]
- AP, FD and A/THR are lost; alternate law, protections lost. Remove the FD flag, consider FPV [FCTM PR-AEP-ENG P 5/26, PDF 406; PDP All engine flameout, PDF 443; PDP All engine flameout, PDF 444]
**1.3 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.4 PM**
- “ENG ALL ENGINES FAILURE” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-ENG P 38/226, PDF 3285; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.5 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- EMER ELEC PWR MAN ON PB …… PRESS [FCOM PRO-ABN-ENG P 38/226, PDF 3285; QRH 19.01A, PDF 162]
- OPT RELIGHT SPD …… 280/0.77 [FCOM PRO-ABN-ENG P 38/226, PDF 3285; QRH 19.01A, PDF 162]
**2.2 PF**
- Fly at or above the optimum relight speed: mandatory after a failure in climb or cruise, to prevent engine core lock [FCOM PRO-ABN-ENG P 38/226, PDF 3285; QRH 19.01A, PDF 162]
- In alternate law the overspeed protection is lost and the upper speed limits are reduced [FCTM PR-AEP-ENG P 5/26, PDF 406]
- **Speed indication failure (volcanic ash)** [FCOM PRO-ABN-ENG P 38/226, PDF 3285; QRH 19.01A, PDF 162]
  - Fly the pitch target from the QRH table [FCOM PRO-ABN-ENG P 38/226, PDF 3285; QRH 19.01A, PDF 162]
**2.3 PM**
- APU (BELOW FL 250) …… START [FCOM PRO-ABN-ENG P 39/226, PDF 3286; QRH 19.01A, PDF 162]
- THR LEVERS …… IDLE [FCOM PRO-ABN-ENG P 39/226, PDF 3286; QRH 19.01A, PDF 162]
**2.4 PF**
- Set the thrust levers to idle, after the PM confirms: no thrust surge at relight [FCTM PR-AEP-ENG P 5/26, PDF 406; FCTM AOP-30-20 P 1/2, PDF 80]
**2.5 PM**
- FAC 1 …… OFF THEN ON [FCOM PRO-ABN-ENG P 39/226, PDF 3286; QRH 19.01A, PDF 162]
- Recovers the characteristic speeds on the PFD and rudder trim [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- Read GLDG DIST: 2NM/1000FT [FCOM PRO-ABN-ENG P 39/226, PDF 3286; QRH 19.01B, PDF 163]
**2.6 PF**
- DIVERSION INITIATE: an accessible runway, or the best area for a forced landing or ditching [FCOM PRO-ABN-ENG P 39/226, PDF 3286; QRH 19.01B, PDF 163; FCTM PR-AEP-ENG P 5/26, PDF 406]
**2.7 PM**
- ALL ENG FAIL PROC …… APPLY [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- Go to the QRH ALL ENG FAIL at once and keep the ECAM procedure displayed [PDP All engine flameout, PDF 446; FCTM AOP-30-30 P 2/6, PDF 83]

### 3. QRH ALL ENG FAIL — notify, then check fuel
**3.1 PF**
- Emergency message on VHF 1 (MAYDAY) when time permits [FCTM PR-AEP-ENG P 6/26, PDF 407; PDP All engine flameout, PDF 444]
- PF communicates once the ECAM actions are started [FCTM AOP-20 P 1–2/10, PDF 68]
**3.2 PM**
- VHF1/HF1/ATC1 …… USE [FCOM PRO-ABN-ENG P 7/226, PDF 3254; QRH 19.01B, PDF 163]
- ATC …… NOTIFY [FCOM PRO-ABN-ENG P 7/226, PDF 3254; QRH 19.01B, PDF 163]
- CABIN CREW …… NOTIFY [FCOM PRO-ABN-ENG P 7/226, PDF 3254; QRH 19.01B, PDF 163]
- SIGNS …… ON [FCOM PRO-ABN-ENG P 7/226, PDF 3254; QRH 19.01B, PDF 163]
- CREW OXY MASK (FL > 100) …… USE [FCOM PRO-ABN-ENG P 7/226, PDF 3254; QRH 19.01B, PDF 163]
- FUEL QUANTITY …… CHECK [FCOM PRO-ABN-ENG P 7/226, PDF 3254; QRH 19.01B, PDF 163]
**3.3 PF + PM**
- Decide: can a relight be attempted? Fuel starvation is one of the most probable causes; engine damage or fuel starvation means no relight [FCTM PR-AEP-ENG P 6/26, PDF 407; FCTM PR-AEP-ENG P 7/26, PDF 408; QRH 19.01B, PDF 163]
- **Relight cannot be attempted** [QRH 19.01B, PDF 163]
  - Go to QRH 19.03A: green dot, then ditching or forced landing (see From the manuals) [QRH 19.01B, PDF 163; QRH 19.03A, PDF 167]

### 4. Fuel remains — windmill relight
**4.1 PM**
- ENG MODE sel …… IGN [FCOM PRO-ABN-ENG P 9/226, PDF 3256; QRH 19.02A, PDF 164]
- Indicate the ENG MASTER levers [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; QRH 19.02A, PDF 164]
**4.2 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**4.3 PM**
- **Approaching or below FL 300** [FCOM PRO-ABN-ENG P 9/226, PDF 3256; QRH 19.02A, PDF 164]
  - ALL ENG MASTERS …… OFF 30 S THEN ON [FCOM PRO-ABN-ENG P 9/226, PDF 3256; QRH 19.02A, PDF 164]
  - ENGs RELIGHT …… TRY REGULARLY [FCOM PRO-ABN-ENG P 9/226, PDF 3256; QRH 19.02A, PDF 164]
- Masters OFF, start the chrono; at 30 s masters ON; check N2 and EGT; at 1 min, if no relight, masters OFF; repeat [PDP All engine flameout, PDF 448; FCTM PR-AEP-ENG P 6/26, PDF 407]
- Both engines at the same time. The 30 s off ventilates the combustion chamber [FCTM PR-AEP-ENG P 6/26, PDF 407]
- APU (below FL 250) …… START [QRH 19.02A, PDF 164]
**4.4 PF**
- Hold the optimum relight speed for the windmill relight [FCOM PRO-ABN-ENG P 38/226, PDF 3285; FCTM PR-AEP-ENG P 5/26, PDF 406]

### 5. If one engine relights
**5.1 PF + PM**
- ENG ALL ENGINES FAILURE disappears and ENG 1(2) FAIL appears for the other engine: apply that ECAM procedure instead [FCTM PR-AEP-ENG P 9/26, PDF 410; FCOM PRO-ABN-ENG P 6/226, PDF 3253]
- After a successful start, use the restored engine as soon as possible [PDP All engine flameout, PDF 448; PDP All engine flameout, PDF 450]
- Normal electrical configuration returns, except AC ESS and DC ESS stay on the emergency generator; green, yellow and blue hydraulics return [FCTM PR-AEP-ENG P 9/26, PDF 410]
**5.2 PM**
- ENG 1(2) FAIL asks to consider the QRH ENG RELIGHT for the other engine; it may be stopped at any time if time or distance requires [FCTM PR-AEP-ENG P 9/26, PDF 410]

### 6. Windmill unsuccessful — starter-assisted relight
**6.1 PM**
- **APU available and windmill relight not successful, below FL 200** [FCOM PRO-ABN-ENG P 9/226, PDF 3256; QRH 19.02A, PDF 164]
  - ALL ENG MASTERS …… OFF [QRH 19.02A, PDF 164]
  - OPTIMUM SPEED: GREEN DOT (table) [QRH 19.02A, PDF 164]
**6.2 PF**
- Reduce to all-engines-inoperative green dot: displayed on PFD 1, also in the QRH table [FCTM PR-AEP-ENG P 6/26, PDF 407; QRH 19.02A, PDF 164]
**6.3 PM**
- WING ANTI ICE …… OFF [QRH 19.02A, PDF 164]
- APU BLEED …… ON [QRH 19.02A, PDF 164]
- ALL ENG MASTERS …… OFF [QRH 19.02A, PDF 164]
- ENG MASTER 1 or 2 …… ON [QRH 19.02A, PDF 164]
- ENG PARAMETERS (N2, EGT) …… MONITOR AT LEAST 30S [QRH 19.02A, PDF 164]
- One engine at a time: the APU cannot supply two. Do not abort while N2 and EGT keep increasing within limits [FCTM PR-AEP-ENG P 7/26, PDF 408]
- **If relight not successful** [QRH 19.02A, PDF 164; FCTM PR-AEP-ENG P 7/26, PDF 408]
  - ALL ENG MASTERS …… OFF [QRH 19.02A, PDF 164]
  - FOR SAME ENGINE RELIGHT …… WAIT 30S [QRH 19.02A, PDF 164]
  - ENGINE RELIGHT (one at a time) …… TRY REGULARLY [QRH 19.02A, PDF 164]
  - The opposite engine can be tried at once: it is already ventilated [FCTM PR-AEP-ENG P 7/26, PDF 408]

### 7. Below 10 000 ft AGL
**7.1 PF**
- SPEED BRAKES AVAILABLE. USE RUDDER WITH CARE: only the RAT powers hydraulics, so avoid large and rapid rudder inputs [QRH 19.02A, PDF 164; QRH 19.02B, PDF 165; FCTM PR-AEP-ENG P 3/26, PDF 404]
**7.2 PM**
- RAM AIR …… ON [QRH 19.02B, PDF 165; QRH 19.03A, PDF 167]
- BARO REF (if avail) …… SET [QRH 19.02B, PDF 165; QRH 19.03A, PDF 167]
- COMMERCIAL …… OFF [QRH 19.02B, PDF 165; QRH 19.03A, PDF 167]
- ELT (when conditions permit) …… ON [QRH 19.02B, PDF 165; QRH 19.03A, PDF 167]
- ENGs RELIGHT …… TRY REGULARLY [QRH 19.02B, PDF 165]
- Prepare cabin and cockpit [QRH 19.02B, PDF 165; QRH 19.03A, PDF 167]
**7.3 PF + PM**
- **If ditching or forced landing anticipated** [QRH 19.02B, PDF 165]
  - Go to QRH 19.04A (ditching) or 19.05B (forced landing): see From the manuals [QRH 19.02B, PDF 165; QRH 19.04A, PDF 170; QRH 19.05B, PDF 172]

### 8. No relight, time permits — clear ECAM → STATUS
**8.1 PF + PM**
- As long as no engine relights, keep to the QRH; clear the ECAM alerts and STATUS page only if there is sufficient time [FCOM PRO-ABN-ENG P 6/226, PDF 3253; FCOM PRO-ABN-ENG P 7/226, PDF 3254]
**8.2 PM**
- “CLEAR ENG ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**8.3 PF**
- “CLEAR ENG” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**8.4 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**8.5 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**8.6 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**8.7 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**8.8 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**8.9 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**8.10 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

## 4. Procedure
### ENG ALL ENGINES FAILURE — ECAM (FCOM PRO-ABN-ENG)
- **LAND ASAP (red)** [FCOM PRO-ABN-ENG P 38/226, PDF 3285]
- EMER ELEC PWR MAN ON PB …… PRESS — Enables RAT extension and emergency generator connection. [FCOM PRO-ABN-ENG P 38/226, PDF 3285]
- OPT RELIGHT SPD …… 280/0.77 — Speed indication failure (volcanic ash): pitch in the QRH. [FCOM PRO-ABN-ENG P 38/226, PDF 3285]
- *During high power operations (climb, cruise) it is mandatory to fly at or above the optimum relight speed, to prevent engine core lock.* [FCOM PRO-ABN-ENG P 38/226, PDF 3285]
- APU (BELOW FL 250) …… START [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- THR LEVERS …… IDLE [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- FAC 1 …… OFF THEN ON — Recovers characteristic speeds on the PFD and rudder trim. [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- *GLDG DIST: 2NM/1000FT* [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- DIVERSION …… INITIATE — An accessible runway, or the most appropriate area for a forced landing or ditching. [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- ALL ENG FAIL PROC …… APPLY [FCOM PRO-ABN-ENG P 39/226, PDF 3286]
- *Associated: F/CTL ALTN LAW (PROT LOST).* [FCOM PRO-ABN-ENG P 39/226, PDF 3286]

### ALL ENG FAIL — notify and decide (QRH 19.01)
- VHF1/HF1/ATC1 …… USE [QRH 19.01B, PDF 163]
- ATC …… NOTIFY [QRH 19.01B, PDF 163]
- CABIN CREW …… NOTIFY [QRH 19.01B, PDF 163]
- SIGNS …… ON [QRH 19.01B, PDF 163]
- CREW OXY MASK (FL > 100) …… USE [QRH 19.01B, PDF 163]
- FUEL QUANTITY …… CHECK [QRH 19.01B, PDF 163]
- **If engine relight can be attempted: QRH 19.02A** [QRH 19.01B, PDF 163]
- **If engine relight cannot be attempted: QRH 19.03A** [QRH 19.01B, PDF 163]

### ALL ENG FAIL — relight (QRH 19.02)
- **If engine relight can be attempted:** [QRH 19.02A, PDF 164]
  - ENG MODE sel …… IGN [QRH 19.02A, PDF 164]
  - **Approaching or below FL 300: Windmill Relight** [QRH 19.02A, PDF 164]
    - ALL ENG MASTERS …… OFF 30 S THEN ON [QRH 19.02A, PDF 164]
    - ENGs RELIGHT …… TRY REGULARLY [QRH 19.02A, PDF 164]
    - *Windmill relight attempts can be repeated until successful, or until the APU bleed is available.* [QRH 19.02A, PDF 164]
    - APU (below FL 250) …… START [QRH 19.02A, PDF 164]
    - **If APU available and windmill relight not successful: Starter Assisted Relight below FL 200** [QRH 19.02A, PDF 164]
      - ALL ENG MASTERS …… OFF [QRH 19.02A, PDF 164]
      - *OPTIMUM SPEED: GREEN DOT* [QRH 19.02A, PDF 164]
      - WING ANTI ICE …… OFF [QRH 19.02A, PDF 164]
      - APU BLEED …… ON [QRH 19.02A, PDF 164]
      - *ENGINE RELIGHT (one at a time)* [QRH 19.02A, PDF 164]
      - ALL ENG MASTERS …… OFF [QRH 19.02A, PDF 164]
      - ENG MASTER 1 or 2 …… ON [QRH 19.02A, PDF 164]
      - ENG PARAMETERS (N2, EGT) …… MONITOR AT LEAST 30S [QRH 19.02A, PDF 164]
      - **If relight not successful** [QRH 19.02A, PDF 164]
        - ALL ENG MASTERS …… OFF [QRH 19.02A, PDF 164]
        - FOR SAME ENGINE RELIGHT …… WAIT 30S [QRH 19.02A, PDF 164]
        - ENGINE RELIGHT (one at a time) …… TRY REGULARLY [QRH 19.02A, PDF 164]
  - *SPEED BRAKES AVAILABLE* [QRH 19.02A, PDF 164]
  - **When below 10 000 ft AGL:** [QRH 19.02B, PDF 165]
    - *PREPARE CABIN AND COCKPIT* [QRH 19.02B, PDF 165]
    - RAM AIR …… ON [QRH 19.02B, PDF 165]
    - BARO REF (if avail) …… SET [QRH 19.02B, PDF 165]
    - COMMERCIAL …… OFF [QRH 19.02B, PDF 165]
    - ELT (when conditions permit) …… ON [QRH 19.02B, PDF 165]
    - ENGs RELIGHT …… TRY REGULARLY [QRH 19.02B, PDF 165]
  - *USE RUDDER WITH CARE* [QRH 19.02B, PDF 165]
  - **If ditching anticipated: 19.04A · If forced landing anticipated: 19.05A** [QRH 19.02B, PDF 165]

### ALL ENG FAIL — no relight (QRH 19.03)
- **If engine relight cannot be attempted:** [QRH 19.03A, PDF 167]
  - *OPTIMUM SPEED: GREEN DOT* [QRH 19.03A, PDF 167]
  - *GLIDING DISTANCE : 2.5 NM / 1000 FT* [QRH 19.03A, PDF 167]
  - APU (below FL 250) …… START [QRH 19.03A, PDF 167]
  - WING ANTI ICE …… OFF [QRH 19.03A, PDF 167]
  - APU BLEED (below FL 200) …… ON [QRH 19.03A, PDF 167]
  - *SPEED BRAKES AVAILABLE* [QRH 19.03A, PDF 167]
  - **Below 10 000 ft AGL:** [QRH 19.03A, PDF 167]
    - *PREPARE CABIN AND COCKPIT* [QRH 19.03A, PDF 167]
    - RAM AIR …… ON [QRH 19.03A, PDF 167]
    - BARO REF (if avail) …… SET [QRH 19.03A, PDF 167]
    - COMMERCIAL …… OFF [QRH 19.03A, PDF 167]
    - ELT (when conditions permit) …… ON [QRH 19.03A, PDF 167]
  - *USE RUDDER WITH CARE* [QRH 19.03A, PDF 167]
  - **If ditching anticipated: 19.04A · If forced landing anticipated: 19.05A** [QRH 19.03B, PDF 168; QRH 19.03C, PDF 169]

### ALL ENG FAIL — ditching (QRH 19.04)
- **If ditching anticipated:** [QRH 19.04A, PDF 170]
  - *MIN RAT SPEED : 140 KT* [QRH 19.04A, PDF 170]
  - GPWS SYS …… OFF [QRH 19.04A, PDF 170]
  - GPWS TERR …… OFF [QRH 19.04A, PDF 170]
  - **At appropriate altitude (above 3 000 ft AGL), configure aircraft for ditching:** [QRH 19.04A, PDF 170]
    - FOR LDG …… FLAP LVR 2 — Only slats extend, and slowly. [QRH 19.04A, PDF 170]
    - *KEEP LANDING GEAR UP* [QRH 19.04A, PDF 170]
    - VAPP …… DETERMINE [QRH 19.04A, PDF 170]
  - **At 2 000 ft AGL:** [QRH 19.04A, PDF 170]
    - CABIN CREW …… NOTIFY FOR DITCHING [QRH 19.04A, PDF 170]
    - DITCHING pb …… ON — Ditch parallel to the swell. If that causes a strong crosswind, ditch into the wind. [QRH 19.04A, PDF 170]
  - **At 500 ft AGL:** [QRH 19.04A, PDF 170]
    - BRACE FOR IMPACT …… ORDER [QRH 19.04A, PDF 170]
    - *TOUCH DOWN AT MIN V/S · TARGET PITCH ATT 11°* [QRH 19.04A, PDF 170]
  - **At touchdown:** [QRH 19.04A, PDF 170]
    - ALL ENG MASTERS …… OFF [QRH 19.04A, PDF 170]
    - APU MASTER sw …… OFF [QRH 19.04A, PDF 170]
  - **After ditching:** [QRH 19.04A, PDF 170]
    - ATC (VHF 1) …… NOTIFY [QRH 19.04A, PDF 170]
    - ALL FIRE pb (ENGs & APU) …… PUSH [QRH 19.04A, PDF 170]
    - ALL AGENT (ENGs & APU) …… DISCH [QRH 19.04A, PDF 170]
    - EVACUATION …… INITIATE [QRH 19.04A, PDF 170]

### ALL ENG FAIL — forced landing (QRH 19.05)
- **If forced landing anticipated:** [QRH 19.05B, PDF 172]
  - *DESCENT SLOPE (CONF 2, L/G DOWN) : 1.6 NM / 1000 FT (600 FT/NM)* [QRH 19.05B, PDF 172]
  - *MIN RAT SPEED: 140 KT* [QRH 19.05B, PDF 172]
  - GPWS SYS …… OFF [QRH 19.05B, PDF 172]
  - GPWS TERR …… OFF [QRH 19.05B, PDF 172]
  - **At appropriate altitude (above 3 000 ft AGL), configure aircraft for landing:** [QRH 19.05B, PDF 172]
    - FOR LDG …… FLAP LVR 2 — Only slats extend, and slowly. [QRH 19.05B, PDF 172]
    - VAPP …… DETERMINE [QRH 19.05B, PDF 172]
    - **When in CONF 2 and VAPP:** [QRH 19.05B, PDF 172]
      - GRAVITY GEAR EXTN handcrank …… PULL AND TURN [QRH 19.05B, PDF 172]
      - *Flight controls revert to direct law at landing gear extension. MAN PITCH TRIM NOT AVAILABLE. Disregard the "USE MAN PITCH TRIM" message on the PFD.* [QRH 19.05B, PDF 172]
      - **When L/G downlocked:** [QRH 19.05B, PDF 172]
        - L/G lever …… DOWN [QRH 19.05B, PDF 172]
        - APPROACH SPEED …… ADJUST — To the VAPP above; it may be increased to reach the landing field or runway. [QRH 19.05B, PDF 172]
    - SPLRs …… ARM [QRH 19.05B, PDF 172]
    - *MAX BRK PR : 1 000 PSI* [QRH 19.05B, PDF 172]
  - **At 2 000 ft AGL:** [QRH 19.05B, PDF 172]
    - CABIN CREW …… NOTIFY FOR LANDING [QRH 19.05B, PDF 172]
  - **At 500 ft AGL:** [QRH 19.05B, PDF 172]
    - BRACE FOR IMPACT …… ORDER [QRH 19.05B, PDF 172]
  - **At touchdown:** [QRH 19.05B, PDF 172]
    - ALL ENG MASTERS …… OFF [QRH 19.05B, PDF 172]
    - APU MASTER SW …… OFF [QRH 19.05B, PDF 172]
    - *BRAKES ON ACCU ONLY* [QRH 19.05B, PDF 172]
  - **When aircraft stopped:** [QRH 19.05C, PDF 173]
    - PARKING BRK …… ON [QRH 19.05C, PDF 173]
    - ATC (VHF 1) …… NOTIFY [QRH 19.05C, PDF 173]
    - ALL FIRE pb (ENGs & APU) …… PUSH [QRH 19.05C, PDF 173]
    - ALL AGENT (ENGs & APU) …… DISCH [QRH 19.05C, PDF 173]
    - **If evacuation required:** [QRH 19.05C, PDF 173]
      - EVACUATION …… INITIATE [QRH 19.05C, PDF 173]
    - **If evacuation not required:** [QRH 19.05C, PDF 173]
      - CABIN CREW and PASSENGERS (PA) …… NOTIFY — Company wording: "REMAIN SEATED, RESUME NORMAL DUTIES". [QRH 19.05C, PDF 173]

## 5. STATUS
**Limitations**
- MIN RAT SPEED 140 KT [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- MAX SPEED 320/0.77 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- MAX BRK PR 1000 PSI [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- MANEUVER WITH CARE [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- FUEL GRVTY FEED [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- AVOID NEGATIVE G FACTOR [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
**Information**
- ALTN LAW: PROT LOST. WHEN L/G DN: DIRECT LAW (pitch and roll) [FCOM PRO-ABN-ENG P 40/226, PDF 3287; FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- BRK Y ACCU PR ONLY: 7 full brake applications [FCOM PRO-ABN-ENG P 40/226, PDF 3287; FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- SLATS SLOW [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- FLS LIMITED TO F-APP + RAW [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
**APPR PROC**
- FOR LDG …… FLAP LVR 2 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- **WHEN CONF 2 AND VAPP:** [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
  - L/G GRVTY EXTN …… AS RQRD — Being stabilized at VAPP before selecting the gear down lets the aircraft be trimmed for approach. [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
**INOP SYS**
- G+Y HYD [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- F/CTL PROT [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- STABILIZER [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- R AIL [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- REVERSER 1+2 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- ADR 2+3 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- IR 2+3 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- RA 1+2 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- SPLR 1+2+4+5 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- ELAC 2 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- SEC 2+3 [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- FLAPS [FCOM PRO-ABN-ENG P 40/226, PDF 3287]
- YAW DAMPER [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- A/CALL OUT [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- AP 1+2 [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- A/THR [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- FUEL PUMPS [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- ANTI SKID [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- N/W. STEER [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- CAT 2 [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- GLS AUTOLAND [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- L/G RETRACT [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- CAB PR 1+2 [FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- PACK 1+2 [FCOM PRO-ABN-ENG P 41/226, PDF 3288]

## 6. QRH and reference tables
### Pitch target if speed indications fail 
To hold the optimum relight speed.

| Gross weight | Pitch |
|---|---|
| At or below 50 000 kg | -2.5° |
| 60 000 kg | -1.5° |
| 70 000 kg | -0.5° |
[QRH 19.01A, PDF 162]

### Gliding distance, no wind 


| Speed | FL 200 | FL 300 | FL 400 |
|---|---|---|---|
| 280 kt: 2 NM / 1000 FT | 40 NM | 60 NM | 80 NM |
| Green dot: 2.5 NM / 1000 FT | 50 NM | 75 NM | 100 NM |
[QRH 19.01B, PDF 163; QRH 19.03A, PDF 167]

### Green dot speed with all engines inoperative (kt) 


| Weight (t) | ≤ FL 200 | FL 300 | FL 400 |
|---|---|---|---|
| 78 | 236 | 246 | 256 |
| 76 | 232 | 242 | 252 |
| 72 | 224 | 234 | 244 |
| 68 | 216 | 226 | 236 |
| 64 | 208 | 218 | 228 |
| 60 | 200 | 210 | 220 |
| 56 | 192 | 202 | 212 |
| 52 | 184 | 194 | 204 |
| 48 | 176 | 186 | 196 |
| 44 | 168 | 178 | 188 |
| 40 | 160 | 170 | 180 |
[QRH 19.02A, PDF 164; QRH 19.03A, PDF 167]

### VAPP for ditching or forced landing 


| Weight (t) | 40 | 50 | 60 | 70 | 80 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| VAPP (kt) | 150 | 150 | 163 | 173 | 183 | 193 | 198 |
[QRH 19.04A, PDF 170; QRH 19.05B, PDF 172]

## 7. FCTM technique
- The ECAM glide distance is an envelope value for a rough range estimate; the actual distance may differ. [FCTM PR-AEP-ENG P 5/26, PDF 406]
- Going faster than the optimum speed keeps relight conditions, but in alternate law there is no overspeed protection. [FCTM PR-AEP-ENG P 5/26, PDF 406]
- Prepare for a ditching or forced landing even if a runway can be reached, if no engine relights. [FCTM PR-AEP-ENG P 8/26, PDF 409]
- Forced landing: gear down by gravity even off a runway, to absorb energy. The brake accumulator allows a limited number of applications, and there is no anti-skid. [FCTM PR-AEP-ENG P 8/26, PDF 409; FCOM PRO-ABN-ENG P 41/226, PDF 3288]
- Ditching: DITCHING pb just before touchdown closes the valves under the aircraft; hold the pitch and keep the wings level until impact. [FCTM PR-AEP-ENG P 8/26, PDF 409]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG 1(2) FAIL | Appears for the remaining engine once one engine relights | See the ENG 1(2) FAIL brief | [FCTM PR-AEP-ENG P 9/26, PDF 410] |
| [QRH] ENG RELIGHT IN FLIGHT | Requested from ENG 1(2) FAIL for the remaining engine | See the ENG RELIGHT brief | [FCTM PR-AEP-ENG P 9/26, PDF 410] |
| F/CTL ALTN LAW (PROT LOST) | Associated procedure | See the F/CTL ALTN LAW brief | [FCOM PRO-ABN-ENG P 39/226, PDF 3286] |
| [QRH] EMER LANDING — ALL ENG FAILURE | Loss of thrust near the ground, not enough time for a relight | APU START, FLAPS LEVER 2, VAPP, gear per ditching or forced landing, BRACE FOR IMPACT, EMER EVAC PROC | [QRH C2, PDF 294; FCTM PR-AEP-MISC P 8/32, PDF 453; FCTM PR-AEP-MISC P 9/32, PDF 454] |
| EMER EVAC | After a ditching or forced landing | See the EMER EVAC brief | [QRH 19.04A, PDF 170; QRH 19.05C, PDF 173] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The title "ENG DUAL FAILURE - FUEL REMAINING" is not used in the supplied HS-TX manuals. They use ENG ALL ENGINES FAILURE (ECAM) and ALL ENG FAIL (QRH); the PDP shows a "FUEL REMAINING" title for the A330 only. Fuel remaining corresponds to the "relight can be attempted" branch here. [FCOM PRO-ABN-ENG P 37/226, PDF 3284; QRH 19.01A, PDF 162; PDP All engine flameout, PDF 446]
- No source gives PF/PM turns for the QRH part. The order follows the QRH lines, with the FCTM and PDP notes; the 30 s masters timing is from the PDP slide. [QRH 19.02A, PDF 164; PDP All engine flameout, PDF 448]
- The QRH lists CABIN CREW and PASSENGERS (PA) NOTIFY when no evacuation is needed; the company wording "REMAIN SEATED, RESUME NORMAL DUTIES" is noted on that line. [QRH 19.05C, PDF 173]
- The handling flow stops at relight and STATUS. The no-relight, ditching and forced landing sections of the QRH are given only as verbatim procedures, without PF/PM turns. [QRH 19.03A, PDF 167; QRH 19.04A, PDF 170; QRH 19.05B, PDF 172]
- HS-TO versions omitted (QRH 19.01A–B, 19.02B–19.03B and 19.05A blocks, FCOM P 41–43/226). The QRH points to 19.05A for a forced landing, but the HS-TX block starts on 19.05B. [QRH 19.02B, PDF 165; QRH 19.05B, PDF 172; FCOM PRO-ABN-ENG P 41/226, PDF 3288]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ENG — ENG ALL ENGINES FAILURE | P 37–41/226 | 3284–3288 | 26 MAY 26 |
| FCOM | PRO-ABN-ENG — [QRH] ALL ENG FAIL | P 6–9/226 | 3253–3256 | 26 MAY 26 |
| QRH | 19.01–19.05 ALL ENG FAIL | 19.01A–19.05C | 162–173 | 18 FEB 26 |
| QRH | C2 EMER LANDING | C2 | 294 | 22 MAR 17 |
| FCTM | PR-AEP-ENG — All engines failure | P 1–9/26 | 402–410 | 26 MAY 26 |
| FCTM | PR-AEP-MISC — EMER LANDING | P 8–9/32 | 453–454 | 26 MAY 26 |
| PDP | All engine flameout (XFTDA1ALENGFO01) | — | 443–450 | APR 2021 |
