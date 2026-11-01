# AIR PACK 1+2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX (the HS-TO version is not used).

An amber caution: neither pack is available. Switch both packs OFF and descend to FL 100 or MEA-MORA, whichever is higher. Below FL 100 with differential pressure under 1 PSI, switch RAM AIR ON (guarded, crosscheck first) and stay at or below FL 100/MEA-MORA. If the fault was due to an overheat, switch the affected pack back ON when the overheat clears.

## 1. What it is
- **Trigger:** Both ACSCs are failed. [FCOM PRO-ABN-AIR P 70/82, PDF 2959]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-AIR P 70/82, PDF 2959]
- Each controller has two lanes. If both lanes fail, the related pack is lost and the hot air pressure-regulating valve closes. [FCOM DSC-21-10-40 P 1/2, PDF 226]
- RAM AIR pb (guarded): the emergency ram air inlet opens. If Δp ≥ 1 PSI, the outflow valve control remains normal and no emergency ram air flows in. If Δp < 1 PSI, the outflow valve opens to about 50 % under automatic control, and ram air goes directly to the mixer unit. [FCOM DSC-21-10-50 P 3/16, PDF 230]

## 2. Key limits
- **Descent:** FL 100 or MEA-MORA, whichever is higher [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- **RAM AIR:** ON when DIFF PR < 1 PSI and FL below 100 [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- **MAX FL:** 100/MEA-MORA [FCOM PRO-ABN-AIR P 71/82, PDF 2960]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “AIR PACK 1+2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-AIR P 70/82, PDF 2959; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- PACK 1 …… OFF [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- PACK 2 …… OFF [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- The fault light goes off when the failure disappears [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- DESCENT TO FL 100/MEA-MORA [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
**2.2 PF**
- Descend to FL 100 or MEA-MORA, whichever is higher, and handle ATC, while the PM continues the ECAM [FCOM PRO-ABN-AIR P 71/82, PDF 2960; FCTM AOP-20 P 1–2/10, PDF 68]
**2.3 PM**
- **WHEN DIFF PR < 1 PSI AND FL BELOW 100** [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - RAM AIR …… ON [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - Guarded pb: point to it and ask confirmation [FCOM DSC-21-10-50 P 3/16, PDF 230; FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
**2.4 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCOM DSC-21-10-50 P 3/16, PDF 230; FCTM AOP-30-20 P 1/2, PDF 80]
**2.5 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.6 PM**
- Press the RAM AIR pb: the ON light comes on white [FCOM DSC-21-10-50 P 3/16, PDF 230]
- MAX FL …… 100/MEA-MORA [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- **If FAULT was due to an overheat** [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - Associated procedure AIR PACK 1(2) OVHT [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - **WHEN PACK OVHT OUT** [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
    - PACK (AFFECTED) …… ON [FCOM PRO-ABN-AIR P 71/82, PDF 2960]

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

### 4. ETOPS flight
**4.1 PM**
- **Loss of the air conditioning capability, at FL 100 with the RAM AIR opened** [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - CAB FANS …… OFF [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]

## 4. Procedure
### AIR PACK 1+2 FAULT (FCOM PRO-ABN-AIR (HS-TX))
- PACK 1 …… OFF [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- PACK 2 …… OFF [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- *The fault light goes off, when the failure disappears.* [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- *The rate at which the cabin altitude increases may be minimized by closing the FWD CARGO ISOL VALVE, if the cargo freight permits.* [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- *DESCENT TO FL 100/MEA-MORA. Descend to FL 100, or MEA-MORA, whichever is higher.* [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- **WHEN DIFF PR < 1 PSI AND FL BELOW 100:** [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - RAM AIR …… ON [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - MAX FL …… 100/MEA-MORA [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- **If FAULT was due to an overheat:** [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - *ASSOCIATED PROCEDURES: AIR PACK 1 (2) OVHT* [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
  - **WHEN PACK OVHT OUT:** [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
    - PACK (AFFECTED) …… ON [FCOM PRO-ABN-AIR P 71/82, PDF 2960]

## 5. STATUS
**Limitations**
- If packs not recovered: MAX FL ....... 100/MEA-MORA [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
**Information**
- If packs not recovered: CKPT AT FIXED TEMP; CAB AT FIXED TEMP [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- If FAULT was due to an overheat: WHEN PACK OVHT OUT: PACK (AFFECTED) ON [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
**INOP SYS**
- PACK 1 + 2 [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- COND CTL 1 [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- COND CTL 2 [FCOM PRO-ABN-AIR P 71/82, PDF 2960]
- FWD CRG HEAT [FCOM PRO-ABN-AIR P 71/82, PDF 2960]

## 7. FCTM technique
- ETOPS flights: in the case of loss of the air conditioning capability (loss of both packs, loss of both bleeds without APU bleed, etc.), when at FL 100 with the RAM AIR opened, the CAB FANS must be switched off. [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| AIR PACK 1(2) OVHT | Associated procedure if the fault was due to an overheat. | WHEN PACK OVHT OUT: PACK (AFFECTED) ON | [FCOM PRO-ABN-AIR P 71/82, PDF 2960; FCOM PRO-ABN-AIR P 76/82, PDF 2965] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCOM trigger names only both ACSCs failed, but the procedure also has the branch "If FAULT was due to an overheat". The manuals do not state that this alert follows an AIR L(R) WING LEAK with an AIR PACK 1(2) OVHT. Confirmed by the user: show it as the third step of that sequence. [FCOM PRO-ABN-AIR P 70/82, PDF 2959; FCOM PRO-ABN-AIR P 71/82, PDF 2960; FCOM PRO-ABN-AIR P 66/82, PDF 2955; FCOM PRO-ABN-AIR P 76/82, PDF 2965]
- The FCOM note on closing the FWD CARGO ISOL VALVE is left out of the flow: the If Installed table lists the FWD ISOL Valve as not installed, and likewise FWD Cargo Heating, although STATUS prints FWD CRG HEAT. [FCOM PRO-ABN-AIR P 71/82, PDF 2960; FCOM GEN P 26/78, PDF 119]
- The FCTM has no chapter for this alert and no PDP module covers it. Confirmed by the user: the PF flies the descent and the ECAM continues, with no STOP ECAM before STATUS. [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 430]
- The manuals name no role for the ETOPS CAB FANS line. Confirmed by the user: the PM. [FCOM PRO-SPO-40-50 P 2/4, PDF 4589; FCTM AOP-30-20 P 1/2, PDF 80]
- The HS-TO version of this procedure (FCOM P 72–74/82) is not used. [FCOM PRO-ABN-AIR P 72/82, PDF 2961]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-AIR — AIR PACK 1+2 FAULT (HS-TX) | P 70–71/82 | 2959–2960 | 26 MAY 26 |
| FCOM | DSC-21-10 — controllers, RAM AIR pb | DSC-21-10-40 P 1/2; DSC-21-10-50 P 3/16 | 226, 230 | 23 AUG 23, 18 FEB 26 |
| FCOM | PRO-SPO-40-50 — ETOPS loss of air conditioning | P 2/4 | 4589 | 18 FEB 26 |
| FCOM | GEN — If Installed table | P 26/78 | 119 | 14 JUL 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
