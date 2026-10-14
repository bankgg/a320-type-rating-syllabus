# CAB PR EXCESS CAB ALT · EMER DESCENT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Memory items · memory items**  
**Applicability:** HS-TXA..TXF, HS-TXG..TXU — The ECAM, memory items and QRH are the same for every HS-TX (Applicable to ALL). Only OEB 61 differs: it applies to HS-TXA..TXF.

A red warning that the cabin altitude is too high. Above FL 160 the crew first does the EMER DESCENT memory items: oxygen masks, signs, descent with AP and A/THR, speed brakes. Then they do the ECAM read-and-do. Without structural damage they descend at maximum speed to FL 100 or MEA/MORA. Below FL 160 they apply the ECAM and start a normal descent.

## 1. What it is
- **Trigger:** Climb or descent: cabin altitude above the higher of 9 550 ft or airfield pressure altitude + 1 000 ft. Cruise: cabin altitude above 9 550 ft. [FCOM PRO-ABN-CAB_PR P 2/14, PDF 3049]
- **Flight phase inhibition:** phases 1, 2, 3, 4, 5, 7, 8, 9, 10 [FCOM PRO-ABN-CAB_PR P 2/14, PDF 3049]
- Depressurization is identified by excessive and uncontrollable cabin altitude and rate of climb, the CAB PR EXCESS CAB ALT alert, or all cabin oxygen masks dropping (independent pressure switch). [FCTM PR-AEP-MISC P 3/32, PDF 448]
- At idle, high speed and speed brakes out, the descent rate is about 7 000 ft/min: FL 390 to FL 100 takes about 4 min and 40 NM. [FCTM PR-AEP-MISC P 3/32, PDF 448]
- Suspect structural damage after a loud bang or a high cabin V/S. [FCTM PR-AEP-MISC P 3/32, PDF 448; PDP Emergency descent, PDF 488]
- **[HS-TXA..TXF]** OEB 61 root cause: the active CPC can show a wrong but normal-looking cabin altitude; the standby CPC triggers the alert. The crew may wrongly disregard the alert or delay the descent. [QRH 61.02A, PDF 291]

## 2. Key limits
- **Alert (cruise):** CAB ALT > 9 550 ft [FCOM PRO-ABN-CAB_PR P 2/14, PDF 3049]
- **Crew oxygen masks:** above FL 100 [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
- **Memory items first:** above FL 160 [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050; FCTM PR-AEP-CAB_PR P 1/2, PDF 398]
- **PAX OXY MASKS MAN ON:** CAB ALT > 14 000 ft [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- **MAX FL:** 100 / MEA-MORA [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- **Rate below FL 100:** ≈ 1 000 ft/min (except approach) [FCTM PR-AEP-MISC P 4/32, PDF 449; PDP Emergency descent, PDF 490]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- Confirm on the CAB PRESS SD page: cabin altitude and V/S excessive and uncontrollable [FCTM PR-AEP-MISC P 3/32, PDF 448; PDP Emergency descent, PDF 483]
**1.2 PF + PM**
- **[HS-TXA..TXF]** Apply the ECAM even if the SD page does not confirm it: an internal CPC failure can show a false normal cabin altitude [QRH 61.01A, PDF 290; QRH 61.02A, PDF 291]
**1.3 PF**
- “EMERGENCY DESCENT” [PDP Emergency descent, PDF 484; FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833]

### 2. Protect (memory items)
**2.1 PF + PM**
- CREW OXY MASK …… USE [PDP Emergency descent, PDF 484; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- COMMUNICATION …… ESTABLISH [PDP Emergency descent, PDF 484]
- Interphone on (INT/RAD to INT); avoid continuous interphone use [PDP Emergency descent, PDF 484; PDP Emergency descent, PDF 491; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
**2.2 PM**
- ALL SIGNS …… ON [PDP Emergency descent, PDF 484; PDP Emergency descent, PDF 491; FCOM PRO-ABN-MISC P 1/30, PDF 3796]

### 3. Initiate descent (memory items)
**3.1 PF**
- EMER DESCENT …… INITIATE [PDP Emergency descent, PDF 485; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- ALT knob TURN then PULL (pull first and it will not descend) [PDP Emergency descent, PDF 485]
- HDG knob TURN off the airway then PULL [PDP Emergency descent, PDF 485]
- SPEED knob PULL [PDP Emergency descent, PDF 485]
- AP and A/THR highly recommended for the descent [FCTM PR-AEP-MISC P 3/32, PDF 448]
- “THRUST IDLE, OPEN DESCENT, HEADING, ALT BLUE” [PDP Emergency descent, PDF 485]
**3.2 PM**
- “CHECKED” [PDP Emergency descent, PDF 485]
- PM watches the FMA to make sure the PF set up the descent correctly [FCTM PR-AEP-MISC P 3/32, PDF 448]
**3.3 PF**
- **If A/THR is not active** [PDP Emergency descent, PDF 485; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
  - THR LEVERS …… IDLE [PDP Emergency descent, PDF 485; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- **When the aircraft is correctly established in descent** [PDP Emergency descent, PDF 485]
  - SPEED BRK LEVER …… FULL [PDP Emergency descent, PDF 485; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
  - Make sure the aircraft is descending first; watch VLS — AoA protection can retract the speed brakes and disconnect the AP [PDP Emergency descent, PDF 485; FCTM PR-AEP-MISC P 3/32, PDF 448; FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]

### 4. ECAM read & do (descent established)
**4.1 PF + PM**
- Read & do starts when the memory items are done and the aircraft is established in descent; the first ECAM lines recall the memory items [PDP Emergency descent, PDF 487; FCTM PR-AEP-CAB_PR P 1/2, PDF 398]
**4.2 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- SPEED …… MAX / APPROPRIATE [PDP Emergency descent, PDF 486; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- No structural damage: set MMO/VMO. If damage suspected: SPD/MACH pb to SPEED and reduce speed; use speed brakes with care [PDP Emergency descent, PDF 488; FCTM PR-AEP-MISC P 3/32, PDF 448]
- CONSIDER …… L/G EXTENSION [PDP Emergency descent, PDF 486; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
**4.3 PM**
- ENG MODE SEL …… IGN [PDP Emergency descent, PDF 486; FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
**4.4 PF**
- ATC …… NOTIFY [PDP Emergency descent, PDF 486; FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
- Nature of the emergency and intentions; CPDLC if voice is poor [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
**4.5 PF + PM**
- “EMERGENCY DESCENT” [PDP Emergency descent, PDF 486; PDP Emergency descent, PDF 489]
- PA to the cabin (EMER DESCENT (PA) … ANNOUNCE) [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
**4.6 PM**
- ATC XPDR …… 7700 [PDP Emergency descent, PDF 486; FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
**4.7 PF + PM**
- CREW OXYGEN MASK DILUTION …… NORM [PDP Emergency descent, PDF 486; FCOM PRO-ABN-MISC P 1/30, PDF 3796]
- Diluter to N saves oxygen; at 100 % it may not last the whole descent [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050; FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
**4.8 PF**
- MAX FL …… 100 or MEA – MORA [PDP Emergency descent, PDF 486; FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
- ND MORA is the highest within 40 NM (shown with CSTR and range ≥ 40 NM) [FCTM PR-AEP-MISC P 3/32, PDF 448; PDP Emergency descent, PDF 486]
**4.9 PM**
- **If CAB ALT above 14 000 ft** [PDP Emergency descent, PDF 486; FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
  - OXYGEN PAX MASK MAN ON …… PRESS [PDP Emergency descent, PDF 486; FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
- Press it earlier if it is obvious the cabin will pass 14 000 ft [FCTM PR-AEP-MISC P 4/32, PDF 449]
- **When descent is established, if time permits** [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
  - CAB PRESS SD: outflow valve closed? If not and ΔP positive, select the other CPC; still open → MODE SEL MAN and V/S CTL per table [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
**4.10 PM**
- “CLEAR CAB PR ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.11 PF**
- “CLEAR CAB PR” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.12 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.13 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.14 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**4.15 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.16 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- STATUS: MAX FL 100/MEA-MORA [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.17 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.18 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 5. Reaching FL 100 / MEA or MORA
**5.1 PF**
- **When ALT* engages** [PDP Emergency descent, PDF 490]
  - SPEED BRAKES …… RETRACT [PDP Emergency descent, PDF 490]
  - SPEED …… MANAGE [PDP Emergency descent, PDF 490]
**5.2 PF + PM**
- TCAS stays TA/RA; collision avoidance has priority over the descent [FCTM PR-AEP-MISC P 4/32, PDF 449]
- **Once oxygen masks are removed** [PDP Emergency descent, PDF 490]
  - MASK STOWAGE BOX …… CLOSE [PDP Emergency descent, PDF 490; FCTM PR-AEP-MISC P 4/32, PDF 449]
  - PRESS TO TEST AND RESET pb …… PRESS [PDP Emergency descent, PDF 490; FCTM PR-AEP-MISC P 4/32, PDF 449]
- Notify the cabin crew at a safe flight level and when cabin oxygen is no longer needed [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Emergency descent, PDF 490]
**5.3 PF**
- Assess and decide: fuel at low level, diversion; inform ATC, cabin, company [PDP Management of abnormal operations, PDF 428; FCTM AOP-30-30 P 5/6, PDF 86]

## 4. Procedure
### [MEM] EMER DESCENT (FCOM PRO-ABN-MISC / QRH 25.02A)
- CREW OXY MASKS …… USE [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
- SIGNS …… ON [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
- EMER DESCENT …… INITIATE [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
- **If A/THR not active:** [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - THR LEVERS …… IDLE [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
- SPD BRK …… FULL [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
- **When descent established:** [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - SPEED …… MAX/APPROPRIATE [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - *If structural damage suspected: MANEUVER WITH CARE* [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - *CONSIDER L/G EXTENSION* [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - ENG MODE SEL …… IGN [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - ATC …… NOTIFY [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - EMER DESCENT (PA) …… ANNOUNCE [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - ATC XPDR 7700 …… CONSIDER [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - CREW OXY MASKS DILUTION …… NORM [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - *MAX FL: 100/MEA-MORA* [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
  - **If CAB ALT above 14 000 ft:** [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
    - OXYGEN PAX MASK MAN ON …… PRESS [FCOM PRO-ABN-MISC P 1/30, PDF 3796; QRH 25.02A, PDF 219]
- *Notify the cabin crew, when the aircraft reaches a safe flight level, and when cabin oxygen is no more necessary.* [FCOM PRO-ABN-MISC P 2/30, PDF 3797]

### CAB PR EXCESS CAB ALT — ECAM procedure (FCOM PRO-ABN-CAB_PR)
- **If above FL 100:** [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
  - CREW OXY MASKS …… USE [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
  - **If below FL 160:** [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - DESCENT …… INITIATE [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - CABIN CREW …… ADVISE [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - MAX FL …… 100/MEA-MORA [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
  - **If above FL 160:** [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - SIGNS …… ON [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - *EMER DESCENT:* [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - DESCENT …… INITIATE [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - **If A/THR is not active:** [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
      - THR LEVERS …… IDLE [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - SPD BRK …… FULL — Significantly increases VLS; let speed increase before using speed brakes to avoid AP disconnection and speed-brake retraction by AoA protection. [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - SPD …… MAX/APPROPRIATE — If structural damage is suspected, use the flight controls with care and reduce speed; with L/G extended, reduce to VLO/VLE. [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - ENG MODE SEL …… IGN [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - ATC …… NOTIFY [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - EMER DESCENT (PA) …… ANNOUNCE [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - XPDR 7700 …… CONSIDER — Squawk 7700 unless otherwise specified by ATC. [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]
    - *To save oxygen, set the oxygen diluter selector to N position. With the oxygen diluter left to 100 %, oxygen quantity may not be sufficient for the entire descent profile.* [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050; FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
    - MAX FL …… 100/MEA-MORA [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
- **IF CAB ALT > 14 000 FT:** [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
  - PAX OXY MASKS …… MAN ON — Confirms that the passenger oxygen masks are released. [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]
- *When descent is established, and if time permits, check that the OUTFLOW VALVES are closed on the CAB PRESS SD page. If they are not closed and ΔP is positive, select the other CPC. If the OUTFLOW VALVE is still not closing, set the cabin pressure MODE SEL pb to MAN and adjust the V/S CTL sw, according to the table.* [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]

### OEB 61 — CAB PR EXCESS CAB ALT (QRH 61.01A)
- **[HS-TXA..TXF]** *Apply the CAB PR EXCESS CAB ALT ECAM procedure, even if not confirmed on the CAB PRESS SD page.* [QRH 61.01A, PDF 290]

## 5. STATUS
**Limitations**
- MAX FL 100/MEA-MORA [FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]

## 6. QRH and reference tables
### Manual cabin pressure targets 
TGT V/S: CLIMB 500 ft/min, DESC 300 ft/min (if MODE SEL MAN is needed).

| A/C FL | CAB ALT TGT |
|---|---|
| 390 | 8 000 |
| 350 | 7 000 |
| 300 | 5 500 |
| 250 | 3 000 |
| < 200 | 0 |
[FCOM PRO-ABN-CAB_PR P 4/14, PDF 3051]

## 7. FCTM technique
- Above FL 160: EMER DESCENT memory items first, then the ECAM. Below FL 160: ECAM procedure and a normal descent. [FCTM PR-AEP-CAB_PR P 1/2, PDF 398]
- Two steps: memory items (PM monitors the FMA), then read & do (PF adjusts the settings). [FCTM PR-AEP-MISC P 3/32, PDF 448]
- At high levels, extend speed brakes while monitoring VLS so AoA protection does not retract them or disconnect the AP. [FCTM PR-AEP-MISC P 3/32, PDF 448]
- Structural damage suspected: SPEED/MACH pb to SPEED to stop the IAS increasing or to reduce speed; use speed brakes carefully. [FCTM PR-AEP-MISC P 3/32, PDF 448; PDP Emergency descent, PDF 488]
- Below FL 100 limit the descent rate to about 1 000 ft/min (PDP adds 500 ft/min for passenger comfort), except on approach. [FCTM PR-AEP-MISC P 4/32, PDF 449; PDP Emergency descent, PDF 490]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| CAB PR SYS 1+2 FAULT | Both CPCs failed — a common lead-in to the excess cabin altitude | MODE SEL MAN; MAN V/S CTL AS RQRD; keep aircraft altitude at or above cabin altitude; Final approach: V/S CTL FULL UP; ΔP zero before opening doors | [FCOM PRO-ABN-CAB_PR P 12/14, PDF 3059; FCOM PRO-ABN-CAB_PR P 13/14, PDF 3060] |

## 9. HS-TX differences
| Topic | HS-TXA..TXF | HS-TXG..TXU | Ref |
|---|---|---|---|
| OEB 61 (CAB PR EXCESS CAB ALT) | Applies: do the ECAM even if the CAB PRESS SD page looks normal | Not applicable | [QRH 61.01A, PDF 290] |

## 10. Gaps and omissions
- The ECAM has no explicit LAND ASAP for this alert; the diversion decision follows the general assess/decide step. [FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050; PDP Management of abnormal operations, PDF 428]
- Callout wording comes from the PDP; the FCOM memory-item callout is “EMERGENCY DESCENT”. [FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833; PDP Emergency descent, PDF 484]
- The PDP says the EMER DESCENT (PA) line may not show on the ECAM on some aircraft; it is in the HS-TX FCOM procedure. [PDP Emergency descent, PDF 489; FCOM PRO-ABN-CAB_PR P 3/14, PDF 3050]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-CAB_PR — CAB PR EXCESS CAB ALT; CAB PR SYS 1+2 FAULT | P 2–4, 12–13/14 | 3049–3051, 3059–3060 | 24 NOV 25 |
| FCOM | PRO-ABN-MISC — [MEM] EMER DESCENT | P 1–2/30 | 3796–3797 | 18 FEB 26 |
| QRH | 25 — EMER DESCENT; 61 — OEB CAB PR EXCESS CAB ALT | 25.02A, 61.01A–61.02A | 219, 290–291 | 18 FEB 26 / 25 APR 24 |
| FCTM | PR-AEP-CAB_PR; PR-AEP-MISC — EMER DESCENT | P 1/2; P 3–4/32 | 398; 448–449 | 21 FEB 24 / 26 MAY 26 |
| PDP | Emergency descent (XFTDA7EMERDES01) | — | 483–491 | JAN 2024 |
