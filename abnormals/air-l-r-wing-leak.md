# AIR L(R) WING LEAK — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX (the HS-TO version is not used).

An amber caution: an overheat is detected near the hot air ducts in one wing. Switch the affected engine bleed OFF, shut the crossbleed and switch wing anti-ice OFF, so the crew must avoid icing conditions. For a left wing leak, also switch the APU bleed OFF if it has not closed. The STATUS lists the engine bleed, the pack on that side and wing anti-ice as inoperative.

## 1. What it is
- **Trigger:** Both BMCs are operative and detect a temperature above 124 °C for the L(R) wing, or one BMC is failed and the other detects a temperature above 124 °C for the L(R) wing. [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- Leak detection loops detect overheating near the hot air ducts. A wing has a double loop: a wing leak signal needs both loops, or one loop with the other inoperative. [FCOM DSC-36-10-50 P 1/4, PDF 2352]
- A wing leak signal closes the bleed valve on the related side, turns on the FAULT light on the AIR COND panel and closes the x-bleed valve (except during an engine start). For a left wing leak, it also closes the APU bleed valve if open (except during an engine start). [FCOM DSC-36-10-50 P 1/4, PDF 2352; FCOM DSC-36-10-30 P 1/2, PDF 2348]
- If one BMC fails, the other still issues the wing leak warning, but the associated FAULT light is lost and the associated bleed valve does not close automatically. [FCOM DSC-36-10-60 P 1/2, PDF 2356]

## 2. Key limits
- **Trigger:** Above 124 °C for the L(R) wing [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- **X BLEED:** SHUT [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- **If severe ice accretion:** MIN SPD VLS +10 / G DOT [FCOM PRO-ABN-AIR P 66/82, PDF 2955]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “AIR L(R) WING LEAK” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-AIR P 65/82, PDF 2954; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- ENG BLEED (AFFECTED) …… OFF [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- When the pb-sw is OFF, the FAULT light goes off when the overheat disappears [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- **If AIR L WING LEAK** [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
  - APU BLEED (IF NOT CLOSED) …… OFF [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- X BLEED …… SHUT [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- WING ANTI-ICE …… OFF [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- AVOID ICING CONDITIONS [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- Overhead actions: point to the panel and announce the system, the control and the action, then check the SD page [FCTM AOP-30-20 P 1/2, PDF 80]

### 3. STATUS
**3.1 PM**
- “CLEAR AIR ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR AIR” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

### 4. Flight continuation
**4.1 PF**
- Avoid icing conditions [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
- **If severe ice accretion** [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
  - MIN SPD …… VLS +10 / G DOT [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
  - Maneuver with care [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
  - LDG DIST PROC …… APPLY [FCOM PRO-ABN-AIR P 66/82, PDF 2955]

## 4. Procedure
### AIR L(R) WING LEAK (FCOM PRO-ABN-AIR (HS-TX))
- ENG BLEED (AFFECTED) …… OFF [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- *When the ENG BLEED pb-sw is ON, the FAULT light remains on. When the ENG BLEED pb-sw is OFF, the FAULT light goes off when the overheat disappears.* [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- **If AIR L WING LEAK:** [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
  - APU BLEED (IF NOT CLOSED) …… OFF [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- X BLEED …… SHUT [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- WING ANTI-ICE …… OFF [FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- *AVOID ICING CONDITIONS* [FCOM PRO-ABN-AIR P 65/82, PDF 2954]

## 5. STATUS
**Limitations**
- AVOID ICING CONDITIONS [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
**Information**
- IF SEVERE ICE ACCRETION: MIN SPD VLS +10 / G DOT; MANEUVER WITH CARE; LDG DIST PROC APPLY [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
**INOP SYS**
- WING A.ICE [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
- ENG 1(2) BLEED [FCOM PRO-ABN-AIR P 66/82, PDF 2955]
- PACK 1(2) [FCOM PRO-ABN-AIR P 66/82, PDF 2955]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| AIR ENG 1+2 BLEED FAULT (LEFT LEAK) | A separate procedure when both engine bleed supply systems are lost with a left wing leak or a pylon leak on side 1. | If unsuccessful: DES TO FL 100/MEA-MORA; See the FCOM procedure | [FCOM PRO-ABN-AIR P 30/82, PDF 2919; FCOM PRO-ABN-AIR P 31/82, PDF 2920] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCTM has no chapter for this alert and no PDP module covers it; the flow is the standard ECAM sequence. [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- The FCTM example of the overhead announcement is "AIR, XBLEED, CLOSE"; the ECAM line for this alert reads X BLEED SHUT. The flow does not quote an announcement for it. [FCTM AOP-30-20 P 1/2, PDF 80; FCOM PRO-ABN-AIR P 65/82, PDF 2954]
- The HS-TO version of this procedure (FCOM P 66–67/82) is not used. [FCOM PRO-ABN-AIR P 66/82, PDF 2955]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-AIR — AIR L(R) WING LEAK, AIR ENG 1+2 BLEED FAULT LEFT LEAK (HS-TX) | P 30–31, 65–66/82 | 2919–2920, 2954–2955 | 26 MAY 26 |
| FCOM | DSC-36-10 — leak detection, BMC failure, APU bleed | DSC-36-10-50 P 1/4; DSC-36-10-60 P 1/2; DSC-36-10-30 P 1/2 | 2352, 2356, 2348 | 18 FEB 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
