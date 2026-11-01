# AIR PACK 1(2) OVHT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all aircraft.

An amber caution: the pack compressor outlet is above 260 °C. Switch the affected pack OFF; high flow is automatically selected on the remaining pack. When the overheat clears, the FAULT light goes off and the pack can be switched back ON.

## 1. What it is
- **Trigger:** The pack compressor outlet temperature rises above 260 °C. [FCOM PRO-ABN-AIR P 75/82, PDF 2964]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-AIR P 75/82, PDF 2964]
- The alert triggers when the pack compressor outlet temperature rises above 260 °C. [FCOM PRO-ABN-AIR P 75/82, PDF 2964]

## 2. Key limits
- **Trigger:** Compressor outlet above 260 °C [FCOM PRO-ABN-AIR P 75/82, PDF 2964]
- **PACK (AFFECTED):** OFF · ON when PACK OVHT OUT [FCOM PRO-ABN-AIR P 76/82, PDF 2965]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “AIR PACK 1(2) OVHT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-AIR P 75/82, PDF 2964; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- PACK (AFFECTED) …… OFF [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
- High flow is automatically selected on the remaining pack. The FAULT light goes off when the overheat disappears [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
- **WHEN PACK OVHT OUT** [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
  - PACK (AFFECTED) …… ON [FCOM PRO-ABN-AIR P 76/82, PDF 2965]

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

## 4. Procedure
### AIR PACK 1(2) OVHT (FCOM PRO-ABN-AIR)
- PACK (AFFECTED) …… OFF [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
- *High flow is automatically selected on the remaining pack. Fault light goes off, when the overheat disappears.* [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
- **WHEN PACK OVHT OUT:** [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
  - PACK (AFFECTED) …… ON [FCOM PRO-ABN-AIR P 76/82, PDF 2965]

## 5. STATUS
**Information**
- WHEN PACK OVHT OUT: PACK (AFFECTED) ON [FCOM PRO-ABN-AIR P 76/82, PDF 2965]
**INOP SYS**
- PACK 1(2) (if pack not recovered) [FCOM PRO-ABN-AIR P 76/82, PDF 2965]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| AIR PACK 1+2 FAULT | The double pack procedure. Its overheat branch returns to WHEN PACK OVHT OUT. | PACK 1, PACK 2 OFF; DESCENT TO FL 100/MEA-MORA; See the AIR PACK 1+2 FAULT brief | [FCOM PRO-ABN-AIR P 70/82, PDF 2959; FCOM PRO-ABN-AIR P 71/82, PDF 2960] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCTM has no chapter for this alert and no PDP module covers it; the flow is the standard ECAM sequence. [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-AIR — AIR PACK 1(2) OVHT, AIR PACK 1+2 FAULT (HS-TX) | P 70–71, 75–76/82 | 2959–2960, 2964–2965 | 26 MAY 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
