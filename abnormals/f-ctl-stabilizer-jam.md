# F/CTL STABILIZER JAM — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — ECAM procedure for all HS-TX; QRH procedure for ALL.

The stabilizer no longer moves electrically. Two versions: the amber ECAM with alternate law, or no ECAM with normal law, where the QRH procedure applies. Check the pitch trim wheel first. If it works, trim to keep the elevators at neutral on the F/CTL SD page. If not, the landing is FLAP LVR 3 and the gear goes down only in CONF 3 at VAPP, because direct law then removes the autotrim.

## 1. What it is
- **Trigger:** This alert triggers when there is a loss of the electrical control of the stabilizer (with or without jamming of the stabilizer). The ELACs may not detect a jam when the pitch trim wheel is jammed: no ECAM warning, normal law remains, and the [QRH] STABILIZER JAM applies. [FCOM PRO-ABN-F_CTL P 124/132, PDF 3597; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- **Flight phase inhibition:** phases 4, 5 [FCOM PRO-ABN-F_CTL P 124/132, PDF 3597; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- The ECAM alert triggers on a loss of electrical control of the stabilizer. Pitch reverts to alternate law, and the autotrim remains available with the elevators commanded by the SEC. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- Depending on the type of failure, the MAN PITCH TRIM may still be available. [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598; FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- With the THS jammed with the alert F/CTL STABILIZER JAM: pitch alternate law with reduced protections, roll direct, yaw alternate. [FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 4/20, PDF 1615]

## 2. Key limits
- **MAX SPEED:** 320 KT [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- **For landing:** FLAP LVR 3 · GPWS LDG FLAP 3 ON · VREF + 10 KT [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- **If MAN TRIM not available:** L/G DN only when CONF 3 and VAPP [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599; FCTM PR-AEP-F_CTL P 4/6, PDF 431]
- **Go-around:** MAX PITCH 15 DEG · TOGA THEN MCT [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598; FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- **CONF FULL (QRH, no MAN PITCH TRIM):** Do not select, to keep the handling qualities [FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]

## 3. Flow (PF / PM)
### 1. ECAM: recognise
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “F/CTL STABILIZER JAM” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-F_CTL P 124/132, PDF 3597; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
**1.4 PF**
- Pitch law reverts to alternate law; the autotrim remains, with the elevators commanded by the SEC [FCTM PR-AEP-F_CTL P 2/6, PDF 429; FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]

### 2. ECAM actions
**2.1 PM**
- MAN PITCH TRIM …… CHECK [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
**2.2 PF**
- Check the pitch trim wheel [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- The force needed on the PITCH TRIM wheel may be higher than during pre-takeoff manual setting [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- **IF MAN TRIM AVAIL** [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - TRIM FOR NEUTRAL ELEV …… — [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - Use the pitch trim wheel to keep the elevators at the zero position on the F/CTL SD page: this gives maximum elevator authority [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598; FCTM PR-AEP-F_CTL P 2/6, PDF 429; FCTM PR-AEP-F_CTL P 3/6, PDF 430]
  - Elevators UP: trim nose UP. Elevators DOWN: trim nose DOWN [FCTM PR-AEP-F_CTL P 3/6, PDF 430]
**2.3 PM**
- MANEUVER WITH CARE …… — [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- **FOR GO-AROUND** [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - MAX PITCH 15 DEG …… — [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - THR LVR …… TOGA THEN MCT [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - Not displayed if one engine is inoperative [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- F/CTL ALTN LAW (PROT LOST) …… Associated procedure [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482]

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
**4.1 PM**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- **Flaps in CONF 3** [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
  - GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
**4.2 PF**
- **IF MAN TRIM NOT AVAIL** [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
  - **WHEN CONF 3 AND VAPP** [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
    - L/G …… DN [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
    - Landing gear extension is delayed, to delay the switching to direct law. It ensures the aircraft is correctly trimmed for the final approach [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599; FCTM PR-AEP-F_CTL P 4/6, PDF 431; FCTM PR-AEP-F_CTL P 5/6, PDF 432]
- **IF MAN TRIM AVAIL** [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - Keep trimming for neutral elevator [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598; FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- WHEN L/G DN: DIRECT LAW, in pitch and in roll. The autotrim with the elevators is lost in direct law [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599; FCTM PR-AEP-F_CTL P 5/6, PDF 432]

### 5. No ECAM: QRH STABILIZER JAM
**5.1 PF**
- **The stabilizer is jammed with no ECAM warning** [FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
  - “STABILIZER JAM PROCEDURE” [PDP Management of abnormal operations, PDF 427]
  - Normal law remains active [FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
**5.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427]
- AP …… OFF [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- MAN PITCH TRIM …… CHECK [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
**5.3 PF**
- Check the pitch trim wheel [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- The pitch trim wheel may not be fully jammed; the force needed may be higher than pre-takeoff manual setting [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- **If MAN PITCH TRIM available** [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
  - TRIM FOR NEUTRAL ELEV: keep the elevator at the zero position on the F/CTL SD page [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
**5.4 PM**
- **If MAN PITCH TRIM not available** [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
  - FOR LDG …… FLAP LVR 3 [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
  - Do not select CONF FULL, in order not to degrade the handling qualities [FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
  - GPWS LDG FLAP 3 …… ON [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- CAT 1 ONLY [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- “STABILIZER JAM PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### F/CTL STABILIZER JAM — ECAM procedure (FCOM PRO-ABN-F_CTL)
- MAN PITCH TRIM …… CHECK — The force needed on the PITCH TRIM wheel may be higher than during pre-takeoff manual setting. [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- **IF MAN TRIM AVAIL:** [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - *TRIM FOR NEUTRAL ELEV* [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - *If manual pitch trim is available, trim to maintain the elevator at the zero position (indications on F/CTL SD page).* [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- *MANEUVER WITH CARE* [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- **FOR GO-AROUND:** [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - *MAX PITCH 15 DEG* [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
  - THR LVR …… TOGA THEN MCT — This line is not displayed if one engine is inoperative. [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]
- *ASSOCIATED PROCEDURES: F/CTL ALTN LAW (PROT LOST)* [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598]

### [QRH] STABILIZER JAM — no ECAM (QRH 20.04A / FCOM PRO-ABN-F_CTL)
- *The ELACs may not detect a stabilizer jam when the pitch trim wheel is jammed. The flight control normal law remains active in this case and there is no ECAM warning. Apply the following procedure.* [FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]
- AP …… OFF [QRH 20.04A, PDF 192]
- MAN PITCH TRIM …… CHECK — The pitch trim wheel may not be fully jammed, the force needed may be higher than pre-takeoff manual setting. [QRH 20.04A, PDF 192]
- **If MAN PITCH TRIM available:** [QRH 20.04A, PDF 192]
  - *TRIM FOR NEUTRAL ELEV* [QRH 20.04A, PDF 192]
  - *If manual pitch trim is available, trim to maintain the elevator at the zero position (indications on F/CTL SD page).* [QRH 20.04A, PDF 192]
- **If MAN PITCH TRIM not available:** [QRH 20.04A, PDF 192]
  - FOR LDG …… FLAP LVR 3 — Do not select CONF FULL, in order not to degrade the handling qualities. [QRH 20.04A, PDF 192]
  - GPWS LDG FLAP 3 …… ON [QRH 20.04A, PDF 192]
- *CAT 1 ONLY* [QRH 20.04A, PDF 192]

## 5. STATUS
**Limitations**
- MAX SPEED …… 320 KT [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- MANEUVER WITH CARE [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- FOR GO-AROUND: MAX PITCH 15 DEG; THR LVR …… TOGA THEN MCT (not displayed if one engine is inoperative) [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
**Information**
- ALTN LAW: PROT LOST [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- WHEN L/G DN: DIRECT LAW — at landing gear extension, control reverts to direct law in pitch, as well as in roll [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG : FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- GPWS LDG FLAP 3 …… ON — Will be displayed when flaps in CONF 3. [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- **IF MAN TRIM NOT AVAIL:** [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
  - **WHEN CONF 3 AND VAPP:** [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
    - L/G …… DN — Landing gear extension is delayed, in order to delay the switching to direct law. [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
**INOP SYS**
- F/CTL PROT [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- STABILIZER [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- ELAC PITCH [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- AP 1 + 2 [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- CAT 2 [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- GLS AUTOLAND [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- STEEP APPR [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]

## 7. FCTM technique
- Trimming for neutral elevator provides maximum authority to the elevators. Elevators in the UP position: move the wheel nose UP. Elevators in the DOWN position: move the wheel nose DOWN. Neutral is shown on the F/CTL SD page. [FCTM PR-AEP-F_CTL P 2/6, PDF 429; FCTM PR-AEP-F_CTL P 3/6, PDF 430; FCTM PR-AEP-F_CTL P 4/6, PDF 431]
- If manual trim is not available, extend the gear after CONF 3 and stabilization at VAPP. This ensures the aircraft is correctly trimmed for the final approach when control reverts to direct law, since the autotrim with the elevators is lost in direct law. [FCTM PR-AEP-F_CTL P 4/6, PDF 431; FCTM PR-AEP-F_CTL P 5/6, PDF 432]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| HYD G+Y SYS LO PR | The stabilizer is also lost in this failure: MAN TRIM is unusable and the same VAPP-before-gear rule applies | See the HYD G+Y brief | [FCTM PR-AEP-HYD P 3/4, PDF 440; QRH 23.03A, PDF 212] |
| F/CTL ALTN LAW | Associated procedure (PROT LOST) | See the ALTN LAW brief | [FCOM PRO-ABN-F_CTL P 125/132, PDF 3598; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482] |
| F/CTL DIRECT LAW | At landing gear extension | See the DIRECT LAW brief | [FCOM PRO-ABN-F_CTL P 126/132, PDF 3599; FCOM PRO-ABN-F_CTL P 18/132, PDF 3491] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The manuals say "the flight crew" uses the pitch trim wheel; the PF is shown from instructor practice. The PDP has no slide for this failure. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- The QRH procedure has no APPR SPD or gear extension line, so the VREF + 10 KT and the VAPP-before-gear rule are shown only for the ECAM case. The manuals do not state them for the no-ECAM case, where normal law remains. [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480; FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- The QRH says CAT 1 ONLY; the ECAM STATUS lists CAT 2 under INOP SYS. Each is quoted as written. [QRH 20.04A, PDF 192; FCOM PRO-ABN-F_CTL P 126/132, PDF 3599]
- No fuel penalty entry exists for F/CTL STABILIZER JAM in the QRH table. [QRH OPS.04C, PDF 275; QRH OPS.04E, PDF 277]
- F/CTL STABILIZER JAM is not in the QRH reset table. [QRH 02.02A, PDF 51]
- The syllabus says "stabilizer jam" and does not say which version the simulator presents; both are shown. [FCOM PRO-ABN-F_CTL P 124/132, PDF 3597; FCOM PRO-ABN-F_CTL P 7/132, PDF 3480]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-F_CTL — F/CTL STABILIZER JAM (HS-TX) | P 124–126/132 | 3597–3599 | 26 MAY 26 |
| FCOM | PRO-ABN-F_CTL — [QRH] STABILIZER JAM | P 7/132 | 3480 | 26 MAY 26 |
| QRH | 20.04 — STABILIZER JAM | 20.04A | 192 | 26 MAY 26 |
| FCTM | PR-AEP-F_CTL — stabilizer jam | P 2–5/6 | 429–432 | 26 MAY 26 |
| FCOM | DSC-27-20-20 — reconfiguration laws | P 3–4/20 | 1614–1615 | 18 FEB 26 |
| PDP | Management of abnormal operations | — | 427 |  |
