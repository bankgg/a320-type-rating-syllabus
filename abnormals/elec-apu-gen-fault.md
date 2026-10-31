# ELEC APU GEN FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX.

The APU generator has tripped or its line contactor is open. Cycle the APU GEN pb-sw OFF then ON, and leave it OFF if that does not work. The MAIN GALLEY is shown inoperative only when one generator is operating.

## 1. What it is
- **Trigger:** The protection trip is initiated by the associated GCU, or the line contactor is open with APU GEN pb-sw set to ON. [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]
- APU GEN pb-sw OFF de-energizes the generator field, opens the line contactor and resets the fault circuit. [FCOM DSC-24-20 P 4/22, PDF 1467]
- The APU GEN FAULT light is inhibited when APU speed is too low, or when the APU GEN line contactor opens after EXT PWR or an engine generator takes over. [FCOM DSC-24-20 P 4/22, PDF 1467]

## 2. Key limits
- **APU GEN:** OFF THEN ON; OFF if unsuccessful [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]

## 3. Flow (PF / PM)
### 1. Detection and ECAM actions
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “ELEC APU GEN FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-ELEC P 27/122, PDF 3152; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
**1.4 PM**
- APU GEN …… OFF THEN ON [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]
- **IF UNSUCCESSFUL** [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]
  - APU GEN …… OFF [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]

### 2. STATUS
**2.1 PM**
- “CLEAR ELEC ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**2.2 PF**
- “CLEAR ELEC” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**2.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**2.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

## 4. Procedure
### ELEC APU GEN FAULT (FCOM PRO-ABN-ELEC P 27/122)
- APU GEN …… OFF THEN ON [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]
- **IF UNSUCCESSFUL:** [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]
  - APU GEN …… OFF [FCOM PRO-ABN-ELEC P 27/122, PDF 3152]

## 5. STATUS
**INOP SYS**
- MAIN GALLEY (when only one GEN operating) [FCOM PRO-ABN-ELEC P 28/122, PDF 3153]
- APU GEN [FCOM PRO-ABN-ELEC P 28/122, PDF 3153]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| APU AUTO (EMER) SHUT DOWN | A different alert: the APU itself has stopped, not only its generator. | See the APU AUTO (EMER) SHUT DOWN brief | [FCOM PRO-ABN-APU P 1/4, PDF 2972] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- HS-TO-only version of this procedure is excluded. [FCOM PRO-ABN-ELEC P 28/122, PDF 3153]
- The FCTM and the PDP have no technique specific to this alert, and the QRH reset table does not list it; the OFF THEN ON line is the procedure's own. The flow is the standard ECAM sequence. [FCOM PRO-ABN-ELEC P 27/122, PDF 3152; FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ELEC — ELEC APU GEN FAULT | P 27–28/122 | 3152–3153 | 26 MAY 26 |
| FCOM | DSC-24-20 — electrical controls | P 4/22 | 1467 | 21 MAY 25 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
