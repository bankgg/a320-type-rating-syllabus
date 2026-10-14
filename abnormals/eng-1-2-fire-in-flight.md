# ENG 1(2) FIRE (IN FLIGHT) — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

A red engine-fire warning in flight. Once the path is safe the crew applies the fire procedure without delay: idle, master off, fire pb, agent 1 after 10 s, and agent 2 if the fire is still there 30 s later. When the fire is out, ENG 1(2) SHUT DOWN follows; LAND ASAP. In cruise, the engine-out drift-down strategy is flown around the drill.

## 1. What it is
- **Trigger:** Fire detected by both loops, or by one loop with the other faulty, or both loops ruptured within 5 s. [FCOM PRO-ABN-ENG P 90/226, PDF 3337]
- **Flight phase inhibition:** none [FCOM PRO-ABN-ENG P 90/226, PDF 3337]
- Thrust and engine parameters can stay normal early in a fire — not a reason to delay the procedure. [FCTM PR-AEP-ENG P 18/26, PDF 419]
- Discharge agents while the alert and a local warning remain. The FIRE light stays on until the fire is out, even after agent 2. [FCTM PR-AEP-ENG P 18/26, PDF 419]

## 2. Key limits
- **AGENT 1:** after 10 s [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- **AGENT 2:** if fire after 30 s [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- **LAND ASAP:** red [FCOM PRO-ABN-ENG P 91/226, PDF 3338]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83]
**1.2 PF**
- Fly the aircraft; at takeoff wait until 400 ft unless the path is safe [FCTM AOP-30-30 P 1/6, PDF 82]
**1.3 PM**
- “ENG 1(2) FIRE” [FCTM AOP-30-30 P 2/6, PDF 83]
- Confirm with local warnings [FCTM PR-AEP-ENG P 18/26, PDF 419]

### 2. Fire procedure
**2.1 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 424]
**2.2 PM**
- THR LEVER (AFFECTED) …… IDLE [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
**2.3 PF**
- Thrust lever (affected): PF retards to IDLE after PM confirms the lever [FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432; FCOM PRO-ABN-ENG P 91/226, PDF 3338]
**2.4 PM**
- “ENGINE MASTER 1 OFF — CONFIRM?” [PDP Management of abnormal operations, PDF 432]
**2.5 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After checking each control the PM points to [PDP Management of abnormal operations, PDF 432]
**2.6 PM**
- ENG MASTER (AFFECTED) …… OFF [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- Reads the ECAM line and points to the affected FIRE pb (guarded control) [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432]
**2.7 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
**2.8 PM**
- ENG FIRE P/B (AFFECTED) …… PUSH [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- AGENT 1 AFTER 10 S …… DISCH [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- ATC …… NOTIFY [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- **IF FIRE AFTER 30 S** [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
  - AGENT 2 …… DISCH [FCOM PRO-ABN-ENG P 91/226, PDF 3338]

### 3. Fire out → ENG SHUT DOWN
**3.1 PF + PM**
- Fire light and alert go out when extinguished; the procedure can then stop and the remaining ECAM continues [FCTM PR-AEP-ENG P 18/26, PDF 419]
**3.2 PM**
- Continue with ENG 1(2) SHUT DOWN — do not restart the engine [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
**3.3 PF**
- Engine secured (fire out or AGENT 2 DISCH) before accelerating after takeoff [FCTM PR-AEP-ENG P 12/26, PDF 413]

### 4. STOP ECAM · STATUS
**4.1 PM**
- “CLEAR ENG ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.2 PF**
- “CLEAR ENG” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**4.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 5. Decide
**5.1 PF**
- Red LAND ASAP: nearest airport where a safe landing can be made [FCTM AOP-30-10 P 2/2, PDF 79; FCTM PR-AEP-ENG P 18/26, PDF 419]
- Inform ATC, cabin crew, passengers [FCTM AOP-30-30 P 5/6, PDF 86]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-ENG)
- **LAND ASAP (red)** [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- THR LEVER (AFFECTED) …… IDLE [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- ENG MASTER (AFFECTED) …… OFF — LP and HP valves close. [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- ENG FIRE P/B (AFFECTED) …… PUSH — Aural stops; light stays on until the fire is out; FADEC no longer supplied. [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- AGENT 1 AFTER 10 S …… DISCH — Delay lets N1 decrease; automatic countdown on ECAM. [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- ATC …… NOTIFY [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- **IF FIRE AFTER 30 S:** [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
  - AGENT 2 …… DISCH [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
- *Associated: ENG 1(2) SHUT DOWN — do not attempt to restart the engine.* [FCOM PRO-ABN-ENG P 91/226, PDF 3338]

## 7. FCTM technique
- If the alert and local warnings disappear after agent 1 (or 1+2), the fire procedure can be stopped and the remaining ECAM done as usual. [FCTM PR-AEP-ENG P 18/26, PDF 419]
- Consider LAND ASAP: land at the nearest airport where a safe landing can be performed. [FCTM PR-AEP-ENG P 18/26, PDF 419]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG 1(2) SHUT DOWN | Associated procedure | X BLEED SHUT, WING ANTI ICE OFF, avoid icing (fire pb pushed); TCAS TA; STATUS: CAT 3 SINGLE | [FCOM PRO-ABN-ENG P 170/226, PDF 3417; FCOM PRO-ABN-ENG P 172/226, PDF 3419] |
| ENGINE FAILURE IN CRUISE — drift-down strategy | Fire (or any engine failure) at cruise level | MCT, A/THR off; Standard strategy M.78/300 kt to the EO LRC ceiling; Never below green dot | [FCTM PR-AEP-ENG P 15/26, PDF 416; FCTM PR-AEP-ENG P 16/26, PDF 417] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- STATUS of the fire case is that of ENG 1(2) SHUT DOWN (see the ENG 1(2) FAIL brief). [FCOM PRO-ABN-ENG P 172/226, PDF 3419]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ENG — ENG 1(2) FIRE (IN FLIGHT) | P 90–91/226 | 3337–3338 | 26 MAY 26 |
| FCTM | PR-AEP-ENG — Engine fire | P 18/26 | 419 | 26 MAY 26 |
