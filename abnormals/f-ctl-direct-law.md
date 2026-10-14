# F/CTL DIRECT LAW — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (the HS-TO version is not used).

An amber caution: the flight controls are in direct law. Sidestick deflection moves the surfaces directly, there is no automatic trim (USE MAN PITCH TRIM on the PFD) and no protection. Overspeed and stall warnings remain. Keep below 320 kt / M .77, trim manually, use small inputs at high speed, prefer manual thrust and avoid large thrust changes. Land in CONF 3 at VREF + 10 kt.

## 1. What it is
- **Trigger:** This alert triggers when direct law is active. Inhibited in flight phases 4, 5, 7 and 8. [FCOM PRO-ABN-F_CTL P 18/132, PDF 3491]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-F_CTL P 18/132, PDF 3491]
- The pitch direct law is a direct stick-to-elevator relationship. Maximum elevator deflection is a compromise between controllability with a forward CG and a not-too-sensitive control with an aft CG. [FCOM DSC-27-20-20 P 17/20, PDF 1628]
- The roll direct law uses only the ailerons and spoilers 4 and 5 to limit roll rate (spoiler 3 replaces a failed spoiler 4; all roll spoilers if the ailerons have failed). [FCOM DSC-27-20-20 P 17/20, PDF 1628]
- Both pitch trim wheels give mechanical control of the THS and have priority over electrical control. A pilot action on the pitch trim wheel disconnects the autopilot. [FCOM DSC-27-20-30 P 2/22, PDF 1633]
- The abnormal attitude law also shows F/CTL DIRECT LAW on the ECAM and USE MAN PITCH TRIM on the PFDs. [FCOM DSC-27-20-20 P 18/20, PDF 1629]

## 2. Key limits
- **MAX SPEED:** 320 KT / M .77 [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- **Pitch trim:** MAN PITCH TRIM — USE [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- **FOR LDG:** FLAPS LVR 3 [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- **APPR SPD:** VREF + 10 KT [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- PFD: amber USE MAN PITCH TRIM below the FMA; amber X instead of the green protection symbols [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492; FCOM DSC-27-20-20 P 1/20, PDF 1612; PDP Reconfiguration laws, PDF 515]
**1.2 PM**
- “F/CTL DIRECT LAW” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-F_CTL P 18/132, PDF 3491; PDP Management of abnormal operations, PDF 424]
- Confirm on the F/CTL SD page and the PFD before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- With GPWS alerts, protections are lost: respect the stall warning when applying the GPWS procedure [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- MAX SPEED …… 320/.77 [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
**2.2 PF**
- Keep below 320 kt / M .77 (high speed protection lost) [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
**2.3 PM**
- MAN PITCH TRIM …… USE [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
**2.4 PF**
- Trim manually with the pitch trim wheel — automatic trim is inoperative [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492; FCOM DSC-27-20-30 P 2/22, PDF 1633]
**2.5 PM**
- MANEUVER WITH CARE …… — [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- USE SPD BRK WITH CARE …… — [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
**2.6 PF**
- Small control inputs at high speed (controls are powerful); manual thrust recommended; avoid large thrust changes [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- At high Mach, use speed brakes with care to avoid strong nose-up changes [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]

### 3. STATUS
**3.1 PM**
- “CLEAR FLIGHT CONTROL ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR FLIGHT CONTROL” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

### 4. Approach and landing
**4.1 PF**
- Brief: CONF 3 landing at VREF + 10 kt, manual pitch trim through configuration and thrust changes, landing distance with the LDG DIST PROC [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
**4.2 PM**
- FOR LDG …… FLAPS LVR 3 [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- MAN PITCH TRIM …… USE [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
**4.3 PF**
- Re-trim after each speed, configuration or thrust change; retract speedbrakes gently [FCTM AOP-10-30-20 P 1/2, PDF 62; FCOM DSC-27-20-20 P 17/20, PDF 1628]
- **If go-around** [FCTM AOP-10-30-20 P 1/2, PDF 62]
  - TOGA gives a large pitch-up moment: apply nose-down trim to avoid excessive pitch-up or a transient stall warning [FCTM AOP-10-30-20 P 1/2, PDF 62]

## 4. Procedure
### F/CTL DIRECT LAW (FCOM PRO-ABN-F_CTL (HS-TX))
- *The PFD displays USE MAN PITCH TRIM.* [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- *In the case of GPWS (EGPWS) alerts, since protections are lost, respect stall warning when applying the GPWS (EGPWS) procedure.* [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- MAX SPEED …… 320/.77 — Speed is limited, due to the loss of high-speed protection. Do not exceed M 0.77, so as not to degrade handling qualities. [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- MAN PITCH TRIM …… USE — Automatic trim is inoperative in direct law. [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- MANEUVER WITH CARE …… — — Use small control inputs at high speed, since in direct law the controls are powerful. Use of manual thrust is recommended. Avoid large thrust changes. [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- USE SPD BRK WITH CARE …… — — At high Mach numbers, use speed brakes with care to avoid too strong nose up changes. [FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]

## 5. STATUS
**Limitations**
- MAX SPEED …… 320/.77 [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- MANEUVER WITH CARE [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- USE SPD BRK WITH CARE [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
**Information**
- DIRECT LAW [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
**APPR PROC**
- FOR LDG …… FLAPS LVR 3 — Replaced by "FOR LDG : FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- GPWS LDG FLAP 3 …… ON — Displayed when flaps are in CONF 3. [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- MAN PITCH TRIM …… USE [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
**INOP SYS**
- F/CTL PROT [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]
- STEEP APPR [FCOM PRO-ABN-F_CTL P 20/132, PDF 3493]

## 6. QRH and reference tables
### Direct law — handling 
FCOM DSC-27 direct law.

| Axis | In direct law |
|---|---|
| Pitch | Direct stick-to-elevator; max elevator deflection varies with CG; no automatic trim |
| Roll | Direct stick-to-surface; about 30°/s clean, 25°/s with slats extended |
| Yaw | Mechanical (rudder pedals); yaw damping and turn coordination lost |
| Protections | None; α floor inoperative; overspeed and stall warnings available |
[FCOM DSC-27-20-20 P 17/20, PDF 1628]

## 7. FCTM technique
- Direct law: be careful with large thrust changes or sudden speedbrake movements, particularly with an aft CG. Retract speedbrakes gently to give time to re-trim. At go-around, TOGA thrust gives a large pitch-up moment — apply nose-down trim to avoid excessive pitch-up or a transient stall warning. [FCTM AOP-10-30-20 P 1/2, PDF 62]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| F/CTL ALTN LAW | Alternate law reverts to direct law at landing gear extension. | MAX SPEED 320 KT; FOR LDG FLAP LVR 3, VREF + 10 KT | [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- Conflict on yaw in direct law: FCOM DSC-27 says yaw damping and turn coordination are lost (mechanical yaw); the PDP slide says "Turn coordination reduced". FCOM is followed. [FCOM DSC-27-20-20 P 17/20, PDF 1628; PDP Reconfiguration laws, PDF 515]
- The HS-TO version (FCOM P 21–24/132) is not used. [FCOM PRO-ABN-F_CTL P 18/132, PDF 3491]
- No PDP task-sharing module is specific to F/CTL DIRECT LAW; the flow uses the generic ECAM handling, the FCTM reconfiguration-law technique and the PDP law slides. [FCTM AOP-10-30-20 P 1/2, PDF 62; PDP Reconfiguration laws, PDF 515]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-F_CTL — F/CTL DIRECT LAW (HS-TX) | P 18–20/132 | 3491–3493 | 26 MAY 26 |
| FCOM | DSC-27-20-20 — direct law, abnormal attitude laws | P 1/20, 17–18/20 | 1612, 1628–1629 | 18 FEB 26 |
| FCOM | DSC-27-20-30 — pitch trim wheel | P 2/22 | 1633 | 18 FEB 26 |
| FCTM | AOP-10-30-20 — flying in reconfiguration laws | P 1/2 | 62 | 25 FEB 25 |
| PDP | Reconfiguration laws (EFTDN1RCFGLAW01) | Flight control laws, alternate, direct | 512–515 | OCT 2018 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS | 424–426 | JAN 2024 |
