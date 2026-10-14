# REMOVAL OF SMOKE / FUMES — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL (QRH 27.02, FCOM [QRH] procedure).

Used when dense smoke or fumes become the greatest threat. Keep the air flowing (CAB FANS OFF and PACK FLOW HI, unless there are fuel vapours), raise the landing elevation to 10 000 ft / MEA-MORA and start a descent to FL 100 / MEA-MORA. Then go back to the SMOKE / FUMES / AVNCS SMOKE procedure during the descent. At FL 100 the cabin is depressurised and RAM AIR is used. If smoke persists: max 200 kt, cockpit door open, and open the PM sliding window.

## 1. What it is
- **Trigger:** QRH procedure. Apply it if smoke/fumes become the greatest threat when applying the [QRH] SMOKE / FUMES / AVNCS SMOKE procedure — a boxed item that may be applied at any time of that procedure, but not before its immediate actions. [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985; FCTM PR-AEP-SMOKE P 8/10, PDF 505]
- **Flight phase inhibition:** none [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985; FCTM PR-AEP-SMOKE P 8/10, PDF 505]
- The most effective means of smoke/fumes removal is ram air: descend to FL 100 or MEA-MORA while the cabin altitude is raised to 10 000 ft or MEA-MORA. The higher cabin altitude also reduces, at least temporarily, the smoke/fumes concentration. [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- With fuel vapours, CAB FANS ON: recirculated air ventilates the air mixer bay and other fuselage areas, preventing fuel vapour accumulation and the risk of explosion; passenger health is not affected. [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- Without fuel vapours, CAB FANS OFF prevents smoke/fumes from entering the cockpit and cabin; PACK FLOW HI gives maximum airflow. Do not shut down the packs or reduce ventilation to smother the fire. Do not deploy oxygen masks if fire is suspected in the cabin. [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- In ELEC EMER CONFIG, APU MASTER ON closes the battery contactors for a maximum of 3 min, so the crew can manually control the outflow valve powered by the DC BAT BUS. [FCOM PRO-ABN-SMOKE P 29/50, PDF 3986]
- If there is smoke/fumes in the cockpit, open the cockpit window to evacuate it. Due to the increased noise level, pay particular attention to visual warnings. [FCOM PRO-ABN-SMOKE P 29/50, PDF 3986]

## 2. Key limits
- **LDG ELEV:** 10 000 FT / MEA-MORA [QRH 27.02A, PDF 249]
- **Descent:** FL 100 / MEA-MORA [QRH 27.02A, PDF 249]
- **RAM AIR:** Open when ΔP ≤ 1 PSI [FCOM PRO-ABN-SMOKE P 29/50, PDF 3986]
- **Window open:** MAX SPEED 200 kt [QRH 27.02B, PDF 250]

## 3. Flow (PF / PM)
### 1. Order
**1.1 PF**
- Smoke is dense and becomes the greatest threat [PDP Smoke, PDF 539; FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- “REMOVAL OF SMOKE / FUMES PROCEDURE” [PDP Smoke, PDF 539; PDP Management of abnormal operations, PDF 427]
**1.2 PM**
- REMOVAL OF SMOKE / FUMES …… APPLY [PDP Smoke, PDF 539]
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427; FCTM AOP-30-30 P 5/6, PDF 86]

### 2. First steps
**2.1 PM**
- EMER EXIT LIGHT …… ON [QRH 27.02A, PDF 249]
- **If fuel vapors** [QRH 27.02A, PDF 249]
  - CAB FANS …… ON [QRH 27.02A, PDF 249]
  - PACK 1 …… OFF [QRH 27.02A, PDF 249]
  - PACK 2 …… OFF [QRH 27.02A, PDF 249]
  - Recirculated air ventilates the mixer bay and fuselage, preventing fuel vapour accumulation [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- **If no fuel vapors** [QRH 27.02A, PDF 249]
  - CAB FANS …… OFF [QRH 27.02A, PDF 249]
  - PACK FLOW …… HI [QRH 27.02A, PDF 249]
  - Do not shut down the packs or reduce ventilation to smother the fire [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- LDG ELEV …… 10 000 FT / MEA-MORA [QRH 27.02A, PDF 249]
**2.2 PF**
- DESCENT TO FL 100 / MEA-MORA …… INITIATE [QRH 27.02A, PDF 249]
- Cabin depressurization starts when the descent is initiated [FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- ATC …… NOTIFY [QRH 27.02A, PDF 249; FCTM AOP-20 P 1–2/10, PDF 68]
**2.3 PM**
- SMOKE / FUMES / AVNCS SMOKE PROC …… CONTINUE [QRH 27.02A, PDF 249; PDP Smoke, PDF 539]
- Return to the SMOKE / FUMES / AVNCS SMOKE procedure for the remaining steps while descending; resume this procedure at FL 100 / MEA-MORA [PDP Smoke, PDF 539; FCTM PR-AEP-SMOKE P 8/10, PDF 505]

### 3. At FL 100 or MEA-MORA
**3.1 PM**
- **If in ELEC EMER CONFIG** [QRH 27.02A, PDF 249]
  - APU MASTER sw …… ON [QRH 27.02A, PDF 249]
  - Battery contactors close for a maximum of 3 min, so the outflow valve (DC BAT BUS) can be controlled manually [FCOM PRO-ABN-SMOKE P 29/50, PDF 3986]
- PACK 1 …… OFF [QRH 27.02A, PDF 249]
- PACK 2 …… OFF [QRH 27.02A, PDF 249]
- CABIN PRESS MODE SEL …… MAN [QRH 27.02A, PDF 249]
- MAN V/S CTL …… FULL UP [QRH 27.02A, PDF 249]
- The outflow valve must be fully open to prevent repressurization when the RAM AIR valve is open [QRH 27.02A, PDF 249]
- RAM AIR …… ON [QRH 27.02A, PDF 249]
- Possible when ΔP is 1 PSI or below; RAM AIR enables flying with both packs OFF [FCOM PRO-ABN-SMOKE P 29/50, PDF 3986]
- APU MASTER sw …… OFF [QRH 27.02A, PDF 249]

### 4. If smoke/fumes persist
**4.1 PF**
- MAX SPEED …… 200 kt [QRH 27.02B, PDF 250]
**4.2 PM**
- COCKPIT DOOR …… OPEN [QRH 27.02B, PDF 250]
- HEADSETS …… ON [QRH 27.02B, PDF 250]
- PM SLIDING WINDOW …… OPEN [QRH 27.02B, PDF 250]
- **When window open** [QRH 27.02B, PDF 250]
  - NON-AFFECTED PACK(s) …… ON [QRH 27.02B, PDF 250]
  - VISUAL WARNINGS (noisy CKPT) …… MONITOR [QRH 27.02B, PDF 250]
  - SMOKE / FUMES / AVNCS SMOKE PROC …… CONTINUE [QRH 27.02B, PDF 250]
- “REMOVAL OF SMOKE / FUMES PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### REMOVAL OF SMOKE / FUMES (QRH 27.02A–B)
- EMER EXIT LIGHT …… ON [QRH 27.02A, PDF 249]
- **If fuel vapors:** [QRH 27.02A, PDF 249]
  - CAB FANS …… ON [QRH 27.02A, PDF 249]
  - PACK 1 …… OFF [QRH 27.02A, PDF 249]
  - PACK 2 …… OFF [QRH 27.02A, PDF 249]
- **If no fuel vapors:** [QRH 27.02A, PDF 249]
  - CAB FANS …… OFF [QRH 27.02A, PDF 249]
  - PACK FLOW …… HI [QRH 27.02A, PDF 249]
- LDG ELEV …… 10 000 FT / MEA-MORA [QRH 27.02A, PDF 249]
- DESCENT TO FL 100 / MEA-MORA …… INITIATE [QRH 27.02A, PDF 249]
- ATC …… NOTIFY [QRH 27.02A, PDF 249]
- SMOKE / FUMES / AVNCS SMOKE PROC …… CONTINUE — Refer to ABN-27 Smoke / Fumes / AVNCS Smoke [QRH 27.02A, PDF 249]
- **At FL 100 or MEA-MORA:** [QRH 27.02A, PDF 249]
  - **If in ELEC EMER CONFIG:** [QRH 27.02A, PDF 249]
    - APU MASTER sw …… ON [QRH 27.02A, PDF 249]
  - PACK 1 …… OFF [QRH 27.02A, PDF 249]
  - PACK 2 …… OFF [QRH 27.02A, PDF 249]
  - CABIN PRESS MODE SEL …… MAN [QRH 27.02A, PDF 249]
  - MAN V/S CTL …… FULL UP [QRH 27.02A, PDF 249]
  - *The outflow valve must be fully open to prevent repressurization when the RAM AIR valve is open.* [QRH 27.02A, PDF 249]
  - RAM AIR …… ON [QRH 27.02A, PDF 249]
  - APU MASTER sw …… OFF [QRH 27.02A, PDF 249]
  - **If smoke/fumes persist:** [QRH 27.02B, PDF 250]
    - *MAX SPEED: 200 kt* [QRH 27.02B, PDF 250]
    - COCKPIT DOOR …… OPEN [QRH 27.02B, PDF 250]
    - HEADSETS …… ON [QRH 27.02B, PDF 250]
    - PM SLIDING WINDOW …… OPEN [QRH 27.02B, PDF 250]
    - **When window open:** [QRH 27.02B, PDF 250]
      - NON-AFFECTED PACK(s) …… ON [QRH 27.02B, PDF 250]
      - VISUAL WARNINGS (noisy CKPT) …… MONITOR [QRH 27.02B, PDF 250]
      - SMOKE / FUMES / AVNCS SMOKE PROC …… CONTINUE — Refer to ABN-27 Smoke / Fumes / AVNCS Smoke [QRH 27.02B, PDF 250]

## 7. FCTM technique
- The [QRH] SMOKE / FUMES / AVNCS SMOKE procedure: diversion anticipated (LAND ASAP), immediate actions, then — if the source is not immediately isolated — diversion and descent, origin identification and fighting. Boxed items (REMOVAL OF SMOKE / FUMES, ELEC EMER CONFIG, immediate landing) may be applied at any time, but not before the immediate actions. [FCTM PR-AEP-SMOKE P 3/10, PDF 500; FCTM PR-AEP-SMOKE P 8/10, PDF 505; PDP Smoke, PDF 538]
- Once the first steps of REMOVAL OF SMOKE / FUMES are applied, return to the SMOKE / FUMES / AVNCS SMOKE procedure for the steps for the suspected source while descending to FL 100; reaching FL 100, complete REMOVAL OF SMOKE / FUMES. [FCTM PR-AEP-SMOKE P 8/10, PDF 505; PDP Smoke, PDF 539]
- QRH procedures: read the notes before performing the action they relate to. [FCTM AOP-30-30 P 5/6, PDF 86]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] SMOKE / FUMES / AVNCS SMOKE | Parent procedure: REMOVAL OF SMOKE / FUMES is one of its boxed items. | LAND ASAP; immediate actions (crew protection, avoid further contamination, cabin crew communication); If source not immediately isolated: DIVERSION and DESCENT TO FL 100 / MEA-MORA INITIATE; Identify and fight: AIR COND, CAB EQPT, or AVNCS/ELECTRICAL (or source unknown and persisting) | [QRH 27.01D, PDF 247; FCTM PR-AEP-SMOKE P 3/10, PDF 500; PDP Smoke, PDF 537; PDP Smoke, PDF 538] |
| ELEC EMER CONFIG (as a smoke boxed item) | Dense smoke still the greatest threat, or all specific actions unsuccessful. | Shed as much electrical equipment as possible to isolate the source; Remain in ELEC EMER CONFIG until a late stage; restore generation a few minutes before landing | [FCTM PR-AEP-SMOKE P 8/10, PDF 505; PDP Smoke, PDF 540] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The parent [QRH] SMOKE / FUMES / AVNCS SMOKE procedure (two HS-TX FCOM variants, HS-TXA..TXO and HS-TXP..TXU) is summarised only, not reproduced. [QRH 27.01D, PDF 247; FCOM PRO-ABN-SMOKE P 28/50, PDF 3985]
- The PDP gives only the order callout ("REMOVAL OF SMOKE / FUMES PROCEDURE"); the split of the QRH lines between PF and PM is not given beyond read & do by the PM. The PF descent, ATC and speed items follow the FCTM task sharing. [PDP Smoke, PDF 539; FCTM AOP-20 P 1–2/10, PDF 68]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| QRH | 27.02 REMOVAL OF SMOKE / FUMES | 27.02A–B | 249–250 | 14 JUL 26 |
| FCOM | PRO-ABN-SMOKE — [QRH] REMOVAL OF SMOKE / FUMES | P 28–29/50 | 3985–3986 | 14 JUL 26 |
| FCTM | PR-AEP-SMOKE — smoke/fumes procedure, boxed items | P 1/10, 3/10, 8/10 | 498, 500, 505 | 24 NOV 25 |
| PDP | Smoke (XFTDA1SMOKE0001) | Immediate actions, procedure, removal of smoke | 537–540 | JAN 2024 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
