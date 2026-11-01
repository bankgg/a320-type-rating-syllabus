# ELEC IDG 1(2) OIL LO PR/OVHT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX (the HS-TO version is not used).

An amber caution: the IDG oil pressure is low or its oil is above 180 °C. Disconnect the IDG with its guarded pushbutton after a crosscheck, pressing until the GEN FAULT light comes on and for no more than 3 s. Only maintenance can reconnect it. If available, the APU may be started and the APU GEN used; on an ETOPS flight, start the APU and use its electrical channel. Landing capability drops to CAT 3 SINGLE.

## 1. What it is
- **Trigger:** ELEC IDG 1(2) OIL LO PR: the IDG oil pressure is low. ELEC IDG 1(2) OIL OVHT: the IDG outlet oil temperature rises above 180 °C. [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- **Flight phase inhibition:** phases 1, 4, 5, 7, 8, 10 [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- The IDG FAULT light comes on if the oil outlet overheats above 180 °C or the oil pressure is low; it goes off when the IDG is disconnected. [FCOM DSC-24-20 P 3/22, PDF 1466]
- Pressing the IDG pb-sw disconnects the IDG from its driveshaft, and only maintenance personnel can reconnect it. Disconnect only with the engine running or windmilling. An automatic thermal disconnection occurs at 200 °C. [FCOM DSC-24-20 P 3/22, PDF 1466]
- GEN 1 and 2 have priority over the APU generator. The APU generator can supply the entire network. [FCOM DSC-24-10-30-10 P 1/2, PDF 1446]
- In flight, the APU backs up the electrical system. APU starting is permitted throughout the normal flight envelope. [FCOM DSC-49-10-10 P 1/2, PDF 2570]

## 2. Key limits
- **IDG pb-sw:** Press until GEN FAULT light on · not more than 3 s [FCOM PRO-ABN-ELEC P 117/122, PDF 3242; FCOM DSC-24-20 P 3/22, PDF 1466]
- **Engine:** At or above idle to disconnect [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- **Oil overheat:** Above 180 °C · automatic disconnection at 200 °C [FCOM PRO-ABN-ELEC P 117/122, PDF 3242; FCOM DSC-24-20 P 3/22, PDF 1466]
- **Landing capability:** CAT 3 SINGLE ONLY [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “ELEC IDG 1(2) OIL OVHT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-ELEC P 117/122, PDF 3242; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- IDG (AFFECTED) …… OFF [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- Guarded pb-sw: point to it and ask confirmation [FCOM DSC-24-20 P 3/22, PDF 1466; FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
**2.2 PM**
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCOM DSC-24-20 P 3/22, PDF 1466; FCTM AOP-30-20 P 1/2, PDF 80]
**2.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**2.4 PM**
- Press the IDG pb-sw until the GEN FAULT light comes on, for no more than 3 s [FCOM PRO-ABN-ELEC P 117/122, PDF 3242; FCOM DSC-24-20 P 3/22, PDF 1466]
- The engine must be at or above idle: disconnection is inhibited when the engine is stopped or below idle [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- The IDG FAULT light goes off when the IDG is disconnected [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]

### 3. STATUS
**3.1 PM**
- “CLEAR ELEC ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR ELEC” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

### 4. APU
**4.1 PF**
- STATUS: if available, the APU may be started and the APU GEN used [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]
- **On an ETOPS flight** [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - Start the APU and use the APU electrical channel [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
**4.2 PM**
- APU MASTER SW pb-sw …… ON [FCOM PRO-NOR-SOP-04 P 5/14, PDF 4084]
- Wait at least 3 s [FCOM PRO-NOR-SOP-04 P 5/14, PDF 4084]
- APU START pb-sw …… ON [FCOM PRO-NOR-SOP-04 P 5/14, PDF 4084]
- Engine generators have priority over the APU generator, which can supply the entire network [FCOM DSC-24-10-30-10 P 1/2, PDF 1446]
- After three consecutive start attempts, wait 60 min [FCOM LIM-APU P 1/2, PDF 4690]

## 4. Procedure
### ELEC IDG 1(2) OIL LO PR/OVHT (FCOM PRO-ABN-ELEC (HS-TX))
- IDG (AFFECTED) …… OFF [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- *If the associated engine is running, the IDG must be disconnected from the engine at or above idle to prevent damage to the disconnect mechanism.* [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- *The IDG disconnection is inhibited, when the engine is stopped or below idle. Press the IDG pb-sw until the GEN FAULT light comes on. However, do not press for more than 3 s, to avoid damage to the disconnect solenoid. The IDG FAULT light goes off, when the IDG is disconnected.* [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]
- *When the IDG is disconnected before takeoff, the oil temperature of the affected IDG may reach a higher value than during normal operations, but without exceeding 150 °C.* [FCOM PRO-ABN-ELEC P 117/122, PDF 3242]

## 5. STATUS
**Limitations**
- CAT 3 SINGLE ONLY [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]
**Information**
- Note: If available, the APU may be started and the APU GEN used. [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]
**INOP SYS**
- MAIN GALLEY (only if APU GEN is not online) [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]
- GEN 1(2) [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]
- CAT 3 DUAL [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]

## 7. FCTM technique
- ETOPS flights, engine or IDG failure: start the APU and use the APU electrical channel. [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- ETOPS flights, one IDG failed: a diversion is required in the case of blue hydraulic circuit low level, low pressure or overheat, APU no start, APU or APU generator inoperative, or a second IDG failure. [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ELEC IDG 1(2) DISCONNECTED | Triggers when the IDG is disconnected. | Crew awareness; Same STATUS: APU may be started and APU GEN used; CAT 3 SINGLE ONLY | [FCOM PRO-ABN-ELEC P 115/122, PDF 3240] |
| IDG OIL TEMP advisory | ECAM advisory at IDG OIL TEMP ≥ 147 °C, before the overheat alert. | Reduce IDG load, if possible (GALLEY or GEN OFF); If required, restore when the temperature has dropped; Restrict generator use to a short time, if the temperature rises again excessively | [FCOM PRO-ABN-ABN-ADV P 1/6, PDF 2836; QRH 01.01A, PDF 46] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCTM ELEC chapter covers only the emergency electrical configuration, and no PDP module covers this alert; the flow is the standard ECAM sequence. [FCTM PR-AEP-ELEC P 1/2, PDF 400; PDP Management of abnormal operations, PDF 424]
- The QRH reset table has no entry for this alert, and the FCOM says only maintenance personnel can reconnect the IDG. [QRH 02.01A, PDF 50; FCOM DSC-24-20 P 3/22, PDF 1466]
- The manuals name no role for the APU start. Confirmed by the user: the PM. The APU switch lines come from the normal cockpit preparation SOP. [FCTM AOP-30-20 P 1/2, PDF 80; FCOM PRO-NOR-SOP-04 P 5/14, PDF 4084]
- The HS-TO version of this procedure (FCOM P 118–119/122) is not used. [FCOM PRO-ABN-ELEC P 118/122, PDF 3243]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ELEC — ELEC IDG 1(2) OIL LO PR/OVHT, ELEC IDG 1(2) DISCONNECTED (HS-TX) | P 115, 117–118/122 | 3240, 3242–3243 | 26 MAY 26 |
| FCOM | DSC-24 — IDG pb-sw, generator priority | DSC-24-20 P 3/22; DSC-24-10-30-10 P 1/2 | 1466, 1446 | 21 MAY 25, 22 MAR 16 |
| FCOM | PRO-SPO-40-40, 40-50 — ETOPS diversion, abnormal procedures | P 1/2; P 2/4 | 4586, 4589 | 15 FEB 23, 18 FEB 26 |
| FCOM | PRO-NOR-SOP-04; LIM-APU; DSC-49-10-10; PRO-ABN-ABN-ADV | P 5/14; P 1/2; P 1/2; P 1/6 | 4084, 4690, 2570, 2836 | 18 FEB 26 |
| QRH | 01.01 advisory; 02.01 system reset | 01.01A; 02.01A | 46, 50 | 18 FEB 26, 26 MAY 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
