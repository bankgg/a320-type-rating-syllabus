# NAV RA 1 AND 2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all HS-TX (the HS-TO version is not used).

An amber caution with no action line, crew awareness only. The effects matter for the approach: no G/S capture with the APPR pb (LOC is available with the LOC pb), CAT 1 limits only, no auto callouts or RETARD, no GPWS, reactive windshear detection or SPEED SPEED SPEED. When the gear goes down the flight controls revert to DIRECT LAW, the AP disconnects and USE MAN PITCH TRIM appears. Land in CONF 3 at VREF + 10 kt.

## 1. What it is
- **Trigger:** This alert triggers when both RAs are failed (dual RA failure). Inhibited in flight phases 3, 4, 5 and 8. [FCOM PRO-ABN-NAV P 113/124, PDF 3938]
- **Flight phase inhibition:** phases 3, 4, 5, 8 [FCOM PRO-ABN-NAV P 113/124, PDF 3938]
- The radio altimeters feed the GPWS and the FWC (auto callouts), the AP and A/THR modes, and the flight control law switching. With both RAs failed, the flight control system uses the LGCIU inputs instead for mode switching. [FCTM PR-AEP-NAV P 20/20, PDF 497]
- Law reconfiguration table: 2 radio altimeters at L/G extension (or CONF 2 if both LGCIUs faulty) — pitch DIRECT, no protection, roll DIRECT, yaw ALTN. [FCOM DSC-27-20-20 P 3/20, PDF 1614; FCOM DSC-27-20-20 P 5/20, PDF 1616]

## 2. Key limits
- **Approach:** CAT 1 only · LOC pb (no G/S) [FCTM PR-AEP-NAV P 20/20, PDF 497; FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- **FOR LDG:** FLAP LVR 3 [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- **APPR SPD:** VREF + 10 KT [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- **Law at L/G DN:** DIRECT (AP off, man pitch trim) [FCOM PRO-ABN-NAV P 114/124, PDF 3939; FCTM PR-AEP-NAV P 20/20, PDF 497]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “NAV RA 1 AND 2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-NAV P 113/124, PDF 3938; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. Procedure
**2.1 PM**
- Crew awareness …… — [FCOM PRO-ABN-NAV P 113/124, PDF 3938]

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

### 4. Approach preparation
**4.1 PF**
- Brief the effects: ILS/FLS/GLS cannot be captured with the APPR pb; capture the localizer with the LOC pb; G/S modes are not available; CAT 1 limits only [FCTM PR-AEP-NAV P 20/20, PDF 497; FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- Brief: final phases flown on raw data — AP/FD behaviour may not be reliable close to the ground [FCTM PR-AEP-NAV P 20/20, PDF 497]
- Brief: no auto callouts and no RETARD call; GPWS and SPEED SPEED SPEED inoperative — increased awareness of energy and terrain [FCTM PR-AEP-NAV P 20/20, PDF 497; FCOM PRO-ABN-NAV P 114/124, PDF 3939]
**4.2 PM**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- APPR SPD …… VREF+10 KT [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-NAV P 114/124, PDF 3939]

### 5. Approach and landing
**5.1 PF**
- **At landing gear selection down** [FCTM PR-AEP-NAV P 20/20, PDF 497]
  - DIRECT LAW becomes active (LGCIU input replaces RA); the AP disconnects with the law reversion [FCTM PR-AEP-NAV P 20/20, PDF 497; FCOM PRO-ABN-NAV P 114/124, PDF 3939]
  - USE MAN PITCH TRIM is displayed: trim manually [FCTM PR-AEP-NAV P 20/20, PDF 497; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- After landing, ground law becomes active when the MLG is compressed and pitch attitude is below 2.5° [FCTM PR-AEP-NAV P 20/20, PDF 497]

## 4. Procedure
### NAV RA 1 AND 2 FAULT (DUAL RA FAILURE) (FCOM PRO-ABN-NAV (HS-TX))
- *Crew awareness.* [FCOM PRO-ABN-NAV P 113/124, PDF 3938]

## 5. STATUS
**Information**
- WHEN L/G DN : DIRECT LAW [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- Note 1: at landing gear extension, flight controls revert to direct law in both pitch and roll (Refer to PRO-ABN-F_CTL F/CTL DIRECT LAW). [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- Note 2: LOC*, LOC, F-LOC* and F-LOC modes are available via the LOC pb. G/S*, G/S, F-G/S* and F-G/S modes are not available. [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG: FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- APPR SPD …… VREF+10 KT [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
**INOP SYS**
- RA 1+2 [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- A/CALL OUT [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- GPWS [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- CAT 2 [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- GLS AUTOLAND [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- REAC W/S DET [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- TCAS [FCOM PRO-ABN-NAV P 114/124, PDF 3939]
- ROW/ROP [FCOM PRO-ABN-NAV P 114/124, PDF 3939]

## 7. FCTM technique
- Although the ECAM procedure is straightforward, the effects of the failure on the aircraft operation require consideration. [FCTM PR-AEP-NAV P 20/20, PDF 497]
- Fly the final phases of the approach on raw data, to avoid possible excessive roll rates if LOC is still engaged. [FCTM PR-AEP-NAV P 20/20, PDF 497]
- Direct law: be careful with large thrust changes or sudden speedbrake movements; at go-around, TOGA thrust gives a large pitch-up moment — apply nose-down trim. [FCTM AOP-10-30-20 P 1/2, PDF 62]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| F/CTL DIRECT LAW | Active from landing gear extension. | MAN PITCH TRIM USE; MAX SPEED 320/.77; Maneuver and use speed brakes with care | [FCOM PRO-ABN-NAV P 114/124, PDF 3939; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCOM procedure is titled NAV RA 1 AND 2 FAULT (DUAL RA FAILURE); the FCTM calls it dual radio altimeter failure. No PDP module covers it; the flow uses the generic ECAM handling. [FCOM PRO-ABN-NAV P 113/124, PDF 3938; FCTM PR-AEP-NAV P 20/20, PDF 497]
- The manuals give no standard callouts to replace the missing auto callouts; none are invented here. [FCTM PR-AEP-NAV P 20/20, PDF 497]
- The HS-TO version (FCOM P 115–116/124) is not used. [FCOM PRO-ABN-NAV P 113/124, PDF 3938]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-NAV — NAV RA 1 AND 2 FAULT (HS-TX) | P 113–114/124 | 3938–3939 | 26 MAY 26 |
| FCTM | PR-AEP-NAV — Dual radio altimeter failure | P 20/20 | 497 | 26 MAY 26 |
| FCTM | AOP-10-30-20 — flying in reconfiguration laws | P 1/2 | 62 | 25 FEB 25 |
| FCOM | DSC-27-20-20 — law reconfiguration table | P 3/20, P 5/20 | 1614, 1616 | 18 FEB 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
