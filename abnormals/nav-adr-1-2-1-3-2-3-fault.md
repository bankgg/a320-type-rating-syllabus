# NAV ADR 1+2(1+3)(2+3) FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (the HS-TO versions are not used).

An amber caution: two air data references have failed. Normal law is lost (alternate law, protections lost), AP, FD and A/THR are lost, and one side loses air data unless ADR 3 can replace it. With ADR 1+2 failed, set AIR DATA to CAPT 3, turn the failed ADRs OFF and select FLAPS 1 only below the VFE of CONF 1+F. With ADR 1+3 failed, the gear cannot retract and must be extended by gravity. Land in CONF 3 at VREF + 10 kt; the law becomes DIRECT when the gear goes down.

## 1. What it is
- **Trigger:** This alert triggers when two ADRs are failed. Inhibited in flight phases 1, 4, 8 and 10. [FCOM PRO-ABN-NAV P 26/124, PDF 3851]
- **Flight phase inhibition:** phases 1, 4, 8, 10 [FCOM PRO-ABN-NAV P 26/124, PDF 3851]
- Dual NAV ADR failures cause the loss of AP, FD and A/THR, and the flight controls revert to ALTN law. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- With a triple ADR failure, the NAV ADR 1+2+3 FAULT procedure has all three ADRs switched OFF, to replace the PFD speed scale and altitude by the BUSS and GPS altitude. [FCTM PR-AEP-NAV P 1/20, PDF 478]
- AIR DATA selector: CAPT 3 — ADR 3 replaces ADR 1; F/O 3 — ADR 3 replaces ADR 2. [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]

## 2. Key limits
- **MAX SPEED:** 320 KT [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- **ADR 1+2 · FLAPS 1:** Below VFE CONF 1+F (SFCC sets 1+F) [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- **ADR 1+3 · L/G:** No retraction · GRVTY EXTN [FCOM PRO-ABN-NAV P 27/124, PDF 3852; FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- **FOR LDG:** FLAP LVR 3 [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- **APPR SPD:** VREF + 10 KT [FCOM PRO-ABN-NAV P 29/124, PDF 3854]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- Normal law is lost: alternate law with all protections except maneuver protections lost. AP, FD and A/THR are lost [FCOM PRO-ABN-NAV P 27/124, PDF 3852; FCTM PR-AEP-NAV P 1/20, PDF 478]
**1.2 PF**
- Fly manually with manual thrust; keep a safe flight path first [FCTM AOP-30-30 P 1/6, PDF 82; FCOM PRO-ABN-NAV P 29/124, PDF 3854]
**1.3 PM**
- “NAV ADR 1+2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-NAV P 26/124, PDF 3851; PDP Management of abnormal operations, PDF 424]
- Announce the pair shown (1+2, 1+3 or 2+3) [FCOM PRO-ABN-NAV P 26/124, PDF 3851]
- Confirm on the overhead ADIRS panel (ADR FAULT lights) and the PFD speed/altitude flags [FCTM AOP-30-30 P 2/6, PDF 83; FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102; FCOM DSC-34-NAV-20 P 8/10, PDF 2131]
**1.4 PF**
- **If air data is lost on the PF's PFD** [FCTM AOP-30-30 P 1/6, PDF 82]
  - The FLY task is affected — the captain may re-allocate the PF role [FCTM AOP-30-30 P 1/6, PDF 82]
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- If ADR and IR of the same ADIRU fail together, do the ADR procedure before the IR procedure [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- **If NAV ADR 1+2 FAULT** [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - AIR DATA SWTG …… CAPT 3 [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ADR 3 (if available) to the captain side [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ADR (AFFECTED) P/B …… OFF [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - **If GPWS TERR FAULT and GPWS SYS FAULT lights come on** [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
    - GPWS TERR pb-sw and GPWS SYS pb-sw OFF [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - Before selecting FLAPS 1, check speed is below VFE of CONF 1+F: the SFCCs will set CONF 1+F instead of CONF 1 [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- **If NAV ADR 1+3(2+3) FAULT** [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - Air data information is lost on one PFD [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ADR 1+3: the landing gear safety valve is controlled closed — no L/G retraction; extension by gravity [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - AIR DATA SWTG …… NORM [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ATC/XPDR (IF ADR 1 FAILED) …… SYS 2 [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ATC/XPDR (IF ADR 2 FAILED) …… SYS 1 [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ADR (AFFECTED) P/B …… OFF [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - **If GPWS TERR FAULT and GPWS SYS FAULT lights come on (ADR 1+3)** [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
    - GPWS TERR pb-sw and GPWS SYS pb-sw OFF [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
  - **If NAV ADR 2+3 FAULT and ANTI ICE CAPT AOA** [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
    - AVOID ICING CONDITIONS …… — [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
**2.2 PM**
- “F/CTL ALTN LAW” [FCOM PRO-ABN-NAV P 27/124, PDF 3852; FCTM AOP-30-30 P 2/6, PDF 83]
- Associated procedure F/CTL ALTN LAW (PROT LOST): MAX SPEED 320 KT, maneuver with care — see the F/CTL ALTN LAW brief [FCOM PRO-ABN-NAV P 27/124, PDF 3852; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482]

### 3. STATUS
**3.1 PM**
- “CLEAR NAV ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR NAV” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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
- Brief: CONF 3 landing, VREF + 10 kt, landing distance with the LDG DIST PROC; FLS limited to F-APP + RAW [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
**4.2 PM**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- **If NAV ADR 1+3 FAULT** [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
  - L/G …… GRVTY EXTN [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
  - Refer to [QRH] L/G GRAVITY EXTENSION. With L/G extended, fuel consumption is increased [FCOM PRO-ABN-NAV P 29/124, PDF 3854; QRH 24.02A, PDF 216]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
**4.3 PF**
- **At landing gear extension** [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
  - Control reverts to DIRECT LAW in pitch and roll: USE MAN PITCH TRIM [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]

## 4. Procedure
### NAV ADR 1+2(1+3)(2+3) FAULT (FCOM PRO-ABN-NAV (HS-TX))
- *Flight control normal laws are lost. Pitch alternate law preserves the neutral static stability. All protections, except maneuver protections are lost.* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- *In the case of a simultaneous ADR and IR (same ADIRU) failure, apply the ADR FAULT procedure prior to the IR FAULT procedure.* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- **If NAV ADR 1+2 FAULT:** [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - AIR DATA SWTG …… CAPT 3 — Set ADR 3 (if available) to the captain's side. [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ADR (AFFECTED) P/B …… OFF [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - *The GPWS TERR FAULT and GPWS SYS FAULT lights illuminate (enhanced/predictive GPWS functions inhibited). If this occurs, switch off the GPWS TERR pb-sw and the GPWS SYS pb-sw.* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - *In the case of NAV ADR 1+2 FAULT, check speed is below VFE of CONF 1+F before selecting FLAPS 1. Because ADR 1+2 parameters are lost, the SFCCs will set CONF 1+F instead of CONF 1.* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - *ASSOCIATED PROCEDURES: F/CTL ALTN LAW (PROT LOST) — Refer to PRO-ABN-F_CTL F/CTL ALTN LAW* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- **If NAV ADR 1+3(2+3) FAULT:** [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - *Air data information is lost on one PFD.* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - *In the case of NAV ADR 1+3 FAULT, the landing gear safety valve is controlled closed: landing gear retraction is inoperative; landing gear extension must be performed by gravity.* [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - AIR DATA SWTG …… NORM [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ATC/XPDR (IF ADR 1 FAILED) …… SYS 2 [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ATC/XPDR (IF ADR 2 FAILED) …… SYS 1 [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - ADR (AFFECTED) P/B …… OFF [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
  - *In the case of NAV ADR 1+3 FAULT: The GPWS TERR FAULT and GPWS SYS FAULT lights illuminate (enhanced/predictive GPWS functions inhibited). If this occurs, switch off the GPWS TERR pb-sw and the GPWS SYS pb-sw.* [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
  - **If NAV ADR 2+3 FAULT and ANTI ICE CAPT AOA:** [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
    - AVOID ICING CONDITIONS …… — [FCOM PRO-ABN-NAV P 28/124, PDF 3853]
  - *ASSOCIATED PROCEDURES: F/CTL ALTN LAW (PROT LOST) — Refer to PRO-ABN-F_CTL F/CTL ALTN LAW* [FCOM PRO-ABN-NAV P 28/124, PDF 3853]

## 5. STATUS
**Limitations**
- MAX SPEED …… 320 KT [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
**Information**
- ALTN LAW : PROT LOST [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- WHEN L/G DN : DIRECT LAW — at L/G extension, control reverts to direct law in pitch and roll. [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- FLS LIMITED TO F–APP + RAW [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- In the case of NAV ADR 1+3 FAULT, the GPWS TERR FAULT and GPWS SYS FAULT lights come on; switch off the GPWS TERR pb-sw and the GPWS SYS pb-sw. [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG : FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- GPWS LDG FLAP 3 …… ON — Displayed when flaps are in CONF 3. [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- **If NAV ADR 1+3 FAULT:** [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
  - L/G …… GRVTY EXTN — Refer to [QRH] L/G GRAVITY EXTENSION. [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
  - **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-NAV P 29/124, PDF 3854]
**INOP SYS**
- F/CTL PROT [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- ADR 1+2(2+3)(1+3) [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- AP 1+2 [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- A/THR [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- ATC/XPDR 1 (if ADR 1 fails) [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- ATC/XPDR 2 (if ADR 2 fails) [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- RUD TRV LIM 1(2) (if NAV ADR 1+3 (2+3) FAULT) [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- GPWS (if ADR 1 fails) [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- CAT 2 [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- GLS AUTOLAND [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- STEEP APPR [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]
- ROW/ROP [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-NAV P 30/124, PDF 3855]

## 6. QRH and reference tables
### Law reconfiguration — dual ADR 
FCOM flight controls law reconfiguration table (NAV rows), same values for HS-TXA..TXF and HS-TXG..TXU.

| Failure | Pitch law | Protection | Roll | Yaw |
|---|---|---|---|---|
| 2 ADR or 2 IR (2nd self detected failed) | ALTN | REDUCED | DIRECT | ALTN |
| 2 ADR (2nd not self detected failed) | ALTN | NO (REDUCED if AOA disagree) | DIRECT | ALTN |
| 3 ADR | ALTN | NO | DIRECT | MECH |
[FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 5/20, PDF 1616]

## 7. FCTM technique
- Reconfiguration law: at high altitude descend to increase the buffet margin (about 4 000 ft below REC MAX ALT); at high speed maneuver with care using small inputs. [FCTM AOP-10-30-20 P 1/2, PDF 62]
- The PF usually remains PF, unless the captain re-allocates tasks or a failure impacts the PF's FLY task. [FCTM AOP-30-30 P 1/6, PDF 82]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| F/CTL ALTN LAW (PROT LOST) | Associated procedure of the dual ADR fault. | MAX SPEED 320 KT; MANEUVER WITH CARE (if displayed); Respect stall warnings with TAWS alerts | [FCOM PRO-ABN-NAV P 27/124, PDF 3852; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 10/132, PDF 3483] |
| F/CTL DIRECT LAW | Active once the landing gear is down. | MAN PITCH TRIM USE; MAX SPEED 320/.77; Maneuver and use speed brakes with care | [FCOM PRO-ABN-NAV P 29/124, PDF 3854; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492] |
| [QRH] L/G GRAVITY EXTENSION | NAV ADR 1+3 FAULT: the gear can only be extended by gravity. | Do not apply if at least one green triangle on each gear on the WHEEL SD page; GRAVITY GEAR EXTN handcrank PULL AND TURN (3 turns clockwise to the mechanical stop); L/G lever DOWN; GEAR DOWN indications CHECK; If successful: do not reset the handcrank; if unsuccessful: LDG WITH ABNORMAL L/G PROC APPLY | [QRH 24.02A, PDF 216] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- FD loss is stated by the FCTM; the FCOM STATUS INOP SYS lists AP 1+2 and A/THR but not FD. [FCTM PR-AEP-NAV P 1/20, PDF 478; FCOM PRO-ABN-NAV P 29/124, PDF 3854]
- VFE of CONF 1+F is in FCOM LIM-AG-SPD, not reproduced here. [FCOM PRO-ABN-NAV P 27/124, PDF 3852]
- No ADR-specific PDP module or callouts; the flow uses the generic ECAM handling. [PDP Management of abnormal operations, PDF 424]
- The HS-TO versions of the procedure (FCOM P 30–37/124) are not used. [FCOM PRO-ABN-NAV P 30/124, PDF 3855]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — NAV ADR 1+2(1+3)(2+3) FAULT (HS-TX) | P 26–30/124 | 3851–3855 | 26 MAY 26 |
| QRH | 24.02 L/G GRAVITY EXTENSION | 24.02A | 216 | 26 MAY 26 |
| FCTM | PR-AEP-NAV — ADR/IRS FAULT · AOP-10-30-20 reconfiguration laws | P 1/20 · P 1/2 | 478 · 62 | 26 MAY 26 |
| FCOM | DSC-27-20-20 — law reconfiguration table | P 3/20, P 5/20 | 1614, 1616 | 18 FEB 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
