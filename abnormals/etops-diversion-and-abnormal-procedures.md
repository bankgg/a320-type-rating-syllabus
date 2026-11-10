# ETOPS · diversion and abnormal procedures — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`, plus the THAI OM-A. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Technique · no memory items**  
**Applicability:** all HS-TX — FCOM special operations, FCTM technique and Airbus PDP tutorial; applies to all HS-TX.

On an ETOPS flight, four technical criteria govern a re-routing or diversion: loss of NAT-HLA capability, diversion airports going below minima or becoming unsuitable, LAND ASAP failures, and failures whose increased fuel consumption exceeds the reserves. After an engine or IDG failure, start the APU and use its electrical channel. After an engine failure, the fixed speed strategy is the one recommended for ETOPS: M.78/320 kt at MCT, the approved one-engine-inoperative diversion speed.

## 1. What it is
- **Trigger:** A failure, or a diversion airport becoming unsuitable, on an ETOPS flight. These procedures apply in addition to the SOP and the ABNORMAL and EMERGENCY procedures. [FCOM PRO-SPO-40-50 P 1/4, PDF 4588; FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- **Flight phase inhibition:** none [FCOM PRO-SPO-40-50 P 1/4, PDF 4588; FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- When an engine failure occurs during cruise, three strategies apply: standard, obstacle and fixed speed. Unless a specific procedure has been established before dispatch (considering ETOPS or mountainous areas), the standard strategy is used. [FCTM PR-AEP-ENG P 15/26, PDF 416]
- The FCTM says the fixed speed strategy is recommended for ETOPS operation and refers to the FCOM diversion decision making section. The PDP gives "ETOPS constraint" and "Speed value as established before dispatch". [FCTM PR-AEP-ENG P 17/26, PDF 418; PDP Engine failure in cruise, PDF 507]
- The FCOM maximum diversion distance tables are computed for ISA, no wind, the optimum diversion level after an engine failure and a single engine diversion speed schedule, with the schedules MCT/VMO and MCT/320 kt. Obstacles are not considered to determine if a route is an ETOPS route. [FCOM PRO-SPO-40-60 P 1/4, PDF 4592; FCOM PRO-SPO-40-60 P 2/4, PDF 4593]

## 2. Key limits
- **Engine or IDG failure:** Start the APU · use the APU electrical channel [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- **Blue hydraulic low level, low pressure or overheat:** Start the APU to ensure the APU generator [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- **Fixed speed strategy:** M.78/320 kt at MCT (approved OEI diversion speed) [PDP Engine failure in cruise, PDF 507; FCTM PR-AEP-ENG P 17/26, PDF 418; FCOM PRO-SPO-40-60 P 1/4, PDF 4592; FCOM PRO-SPO-40-60 P 2/4, PDF 4593; OM-A 8.5.4.4]
- **Loss of air conditioning:** At FL 100 with RAM AIR opened: CAB FANS off [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]

## 3. Flow (PF / PM)
### 1. Assess
**1.1 PF + PM**
- First maintain a safe flight path; apply the ECAM or QRH procedure [FCTM AOP-30-30 P 1/6, PDF 82]
- Fly, navigate, communicate [FCTM AOP-20 P 1–2/10, PDF 68]

### 2. Engine failure: strategy
**2.1 PF + PM**
- STRATEGY …… DETERMINE [PDP Engine failure in cruise, PDF 506; PDP Engine failure in cruise, PDF 507]
**2.2 PF**
- **A specific procedure was established before dispatch for ETOPS** [FCTM PR-AEP-ENG P 15/26, PDF 416; FCTM PR-AEP-ENG P 17/26, PDF 418]
  - Fixed speed strategy: MCT, speed M.78/320 kt (approved OEI diversion speed) [PDP Engine failure in cruise, PDF 507; FCTM PR-AEP-ENG P 17/26, PDF 418; FCOM PRO-SPO-40-60 P 1/4, PDF 4592; FCOM PRO-SPO-40-60 P 2/4, PDF 4593; OM-A 8.5.4.4]
- The diversion FL depends on the weight at the critical point (70 000 kg: FL 180) [FCOM PRO-SPO-40-60 P 1/4, PDF 4592; FCOM PRO-SPO-40-60 P 2/4, PDF 4593]
- Unless a specific procedure has been established before dispatch, the standard strategy is used [FCTM PR-AEP-ENG P 15/26, PDF 416]
- See the drift-down brief for the thrust, heading and descent lines [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 506]

### 3. ETOPS actions
**3.1 PM**
- **Engine or IDG failure** [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - Start the APU and use the APU electrical channel [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- **Blue hydraulic circuit low level, low pressure or overheat** [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - Start the APU to ensure availability of the APU generator [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- **Loss of the air conditioning capability, at FL 100 with the RAM AIR opened** [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - CAB FANS …… OFF [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]

### 4. Diversion decision
**4.1 PF + PM**
- Assess the failure against the diversion criteria (see Procedure); consider LAND ASAP, fuel and weather [FCOM PRO-SPO-40-40 P 1/2, PDF 4586; PDP Management of abnormal operations, PDF 428]
- Decide [FCTM AOP-30-30 P 5/6, PDF 86; PDP Management of abnormal operations, PDF 428]
**4.2 PF**
- Inform ATC, cabin crew, passengers and airline operations as required [FCTM AOP-30-30 P 5/6, PDF 86; PDP Management of abnormal operations, PDF 428]

## 4. Procedure
### Diversion decision making (FCOM PRO-SPO-40-40)
- *The technical criteria governing a re-routing or diversion decision can be classified into four categories:* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Loss of NAT-HLA capability, before entering the NAT-HLA area (as applicable)* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Weather minima at diversion airport(s) going below the company/crew en-route minima, before reaching the ETOPS Entry Point, or diversion airport(s) becoming unsuitable for any reason* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Failure cases requiring a diversion to the nearest airport (cases leading to a LAND ASAP message on the ECAM and/or in the QRH)* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Failure cases resulting in increased fuel consumption, exceeding the available fuel reserves* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- **Electrical generation. If one IDG fails, a diversion is required in the case of:** [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Blue hydraulic circuit low level, low pressure or overheat* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *APU no start* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *APU or APU generator inoperative* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Second IDG failure* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- *Fuel system. Some failure cases may lead to fuel gravity feeding which implies flight at lower altitude or to some fuel being unusable. The flight crew's evaluation of the actual situation and the fuel remaining may lead to the decision that a diversion is required.* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- **Hydraulic system. If there is low level, low pressure or overheat on blue hydraulic circuit, a diversion is required in the case of:** [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *One IDG failure* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *APU no start* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *APU/APU GEN failure* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- **APU. If APU/APU GEN fails, a diversion is required in the case of:** [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *Blue hydraulic circuit low level, low pressure or overheat* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
  - *One IDG failure* [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]

### ETOPS abnormal and emergency procedures (FCOM PRO-SPO-40-50 (HS-TX))
- **ELECTRICAL EMERGENCY CONFIGURATION. Complete the ECAM procedure using the following:** [FCOM PRO-SPO-40-50 P 1/4, PDF 4588]
  - *AIR CONDITIONING: As cockpit and cabin temperature control is lost, it is recommended to open the cockpit door.* [FCOM PRO-SPO-40-50 P 1/4, PDF 4588]
  - *FUEL: As all fuel pumps are lost, the engines are fed by gravity. Refer to GRVTY FUEL FEEDING Procedure.* [FCOM PRO-SPO-40-50 P 1/4, PDF 4588]
  - *ENGINE ANTI-ICE: Engine anti-ice valves are permanently open, although the ECAM memo ENG A. ICE is not displayed on the ECAM (except if the ENG A. ICE pb is at ON).* [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - *WING ANTI-ICE: If only one ENG BLEED is available, PACK 1 must be switched OFF, to avoid having both packs and wing anti-ice supplied by a single bleed source.* [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
  - *ENGINE: As the engines are in degraded N1 mode, the power setting has to be done using tables.* [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- *BLUE HYDRAULIC CIRCUIT LOW LEVEL OR LOW PRESSURE OR OVERHEAT: Start the APU to ensure availability of the APU generator.* [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- *ENGINE OR IDG FAILURE: Start the APU and use the APU electrical channel.* [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]
- *LOSS OF AIR CONDITIONING: In the case of loss of the air conditioning capability (loss of both packs, loss of both bleeds without APU bleed etc.), when at FL 100 with the RAM AIR opened, the CAB FANS must be switched off.* [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]

## 7. FCTM technique
- The fixed speed section of the FCTM gives no speed, thrust or descent lines of its own. [FCTM PR-AEP-ENG P 17/26, PDF 418]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| Engine failure in cruise · drift-down strategy | The thrust, heading and descent lines for the standard and obstacle strategies. | All thrust levers MCT, A/THR OFF; Do not decelerate below green dot | [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 506] |
| Maximum diversion distance | Dispatch performance table; it differs between HS-TXA..TXF and HS-TXG..TXU. | See the FCOM table | [FCOM PRO-SPO-40-60 P 1/4, PDF 4592; FCOM PRO-SPO-40-60 P 2/4, PDF 4593] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCOM maximum diversion distance table gives the MCT/320 kt schedule with no Mach number and does not call it the fixed speed. The M.78/320 kt comes from the THAI OM-A table of approved diversion times, speeds and distances (A320-200: 70 t, 90 min, OEI 0.78/320, 628 nm, the same as the FCOM HS-TXG to HS-TXU figure). The OM-A is not in books/; confirmed by the user to cite it. Its note refers to the A320 OPSPEC for the aircraft-specific approval, which was not checked. [FCTM PR-AEP-ENG P 17/26, PDF 418; FCOM PRO-SPO-40-60 P 1/4, PDF 4592; FCOM PRO-SPO-40-60 P 2/4, PDF 4593; OM-A 8.5.4.4]
- This brief goes beyond the ECAM/QRH scope of the other briefs. Confirmed by the user: add it as a brief for the diversion row. [FCOM PRO-SPO-40-40 P 1/2, PDF 4586]
- No source names roles for these ETOPS lines. Confirmed by the user: the PM performs the APU start and the CAB FANS line. [FCOM PRO-SPO-40-50 P 2/4, PDF 4589; FCTM AOP-30-20 P 1/2, PDF 80]
- The HS-TO versions (FCOM PRO-SPO-40-50 P 2–4/4, PRO-SPO-40-60 P 3–4/4) are not used. [FCOM PRO-SPO-40-50 P 2/4, PDF 4589]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-SPO-40-40 — Diversion decision making | P 1/2 | 4586 | 15 FEB 23 |
| FCOM | PRO-SPO-40-50 — ETOPS procedures (HS-TX) | P 1–2/4 | 4588–4589 | 18 FEB 26 |
| FCOM | PRO-SPO-40-60 — Maximum diversion distance (HS-TX) | P 1–2/4 | 4592–4593 | 18 FEB 26 |
| OM-A | 8.5.4.4 — THAI's fleet approved diversion time, speeds and distances | 8.5.4.4 | — |  |
| FCTM | PR-AEP-ENG — Engine failure during cruise | P 15, 17/26 | 416, 418 | 26 MAY 26 |
| PDP | Engine failure in cruise (EFTDA1ENGFCRZ01) | Detection and initial actions | 506–507 | JAN 2024 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
