# APU FIRE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

Red warning with red LAND ASAP. Push the APU FIRE pb after both pilots confirm it, discharge the agent after 10 s, and switch the APU MASTER SW OFF. Do not attempt to restart the APU. Pushing the APU FIRE pb also triggers APU EMER SHUT DOWN.

## 1. What it is
- **Trigger:** Fire detected by both loops, or by one loop when the other loop is faulty, or a rupture in both loops within 5 s. [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- **Flight phase inhibition:** none [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- The APU has one fire extinguisher bottle with two electrically-operated squibs. The flight crew controls the discharge from the FIRE panel in the cockpit. [FCOM DSC-26-20-10 P 2/2, PDF 1531]
- The APU AGENT pb becomes active when the flight crew releases the APU FIRE pb-sw. [FCOM DSC-26-20-20 P 3/6, PDF 1534]
- When an APU fire is detected on the ground, the APU automatically shuts down and the bottle discharges automatically, 3 s after the fire warning appears. The red APU FIRE light on the external power panel and an external horn also come on. [FCOM DSC-26-20-10 P 2/2, PDF 1531; FCOM DSC-26-20-20 P 5/6, PDF 1536]

## 2. Key limits
- **Agent:** After 10 s [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- **Landing:** LAND ASAP (red) [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- **APU restart:** Do not attempt [FCOM PRO-ABN-APUF P 1/2, PDF 2976]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “APU FIRE” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-APUF P 1/2, PDF 2976; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
- Red LAND ASAP: land at the nearest airport at which a safe landing can be made [FCOM PRO-ABN-APUF P 1/2, PDF 2976; FCTM AOP-30-10 P 2/2, PDF 79]

### 2. Fire procedure
**2.1 PM**
- Read the ECAM line and point to the APU FIRE pb (guarded control) [FCOM PRO-ABN-APUF P 1/2, PDF 2976; FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.2 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.3 PM**
- APU FIRE P/B …… PUSH [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- APU LP valve closes, the aural warning stops, and the pb-sw stays on as long as a fire is detected [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- AGENT AFTER 10 S …… DISCH [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- The ECAM counts down automatically. The delay lets the airflow decrease, which makes the agent more effective [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- MASTER SW …… OFF [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- Do not attempt to restart the APU [FCOM PRO-ABN-APUF P 1/2, PDF 2976]

### 3. STATUS
**3.1 PM**
- “CLEAR APU ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR APU” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

## 4. Procedure
### APU FIRE (FCOM PRO-ABN-APUF P 1/2)
- **LAND ASAP (red)** [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- APU FIRE P/B …… PUSH [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- *APU LP valve closes. Aural warning stops. APU FIRE pb-sw remains on, as long as a fire is detected.* [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- AGENT AFTER 10 S …… DISCH [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- *The 10 s delay allows the airflow to decrease, which increases the effect of the agent. Automatic countdown on the ECAM.* [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- MASTER SW …… OFF [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- *Do not attempt to restart the APU.* [FCOM PRO-ABN-APUF P 1/2, PDF 2976]

## 5. STATUS
**INOP SYS**
- APU [FCOM PRO-ABN-APUF P 2/2, PDF 2977]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| APU AUTO (EMER) SHUT DOWN | Triggers when the APU FIRE pb is pushed or an APU fire on ground is detected. | MASTER SW: OFF; Do not attempt a restart after a fire | [FCOM PRO-ABN-APU P 1/4, PDF 2972; FCOM PRO-ABN-APUF P 1/2, PDF 2976] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCOM gives no further action if the APU FIRE pb-sw stays on after the agent is discharged. [FCOM PRO-ABN-APUF P 1/2, PDF 2976]
- The FCTM and the PDP have no technique specific to this warning; the flow is the standard ECAM sequence with the crosscheck for guarded controls. [FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-APUF — APU FIRE | P 1–2/2 | 2976–2977 | 22 MAR 17 |
| FCOM | DSC-26-20 — engines and APU fire protection | P 2/2; P 3/6, 5/6 | 1531, 1534, 1536 | 17 AUG 22 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
