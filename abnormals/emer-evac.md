# EMER EVAC — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** all HS-TX — FCOM HS-TX version; QRH C2 applies to ALL.

A QRH procedure. The F/O runs the actions up to the decision point while the Captain decides. The decision to evacuate is irreversible once ordered; until then it can be deferred or cancelled.

## 1. What it is
- **Trigger:** Applied when considering an emergency evacuation, or when required by the ECAM (e.g. ENG FIRE on ground: EMER EVAC PROC APPLY). [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- **Flight phase inhibition:** none [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- Typical causes: uncontrollable fire, smoke/fumes — during taxi, after a rejected takeoff or after landing. [FCTM PR-AEP-MISC P 6/32, PDF 451]
- With engines stopped only the right dome light works; on batteries the crew seats must be moved mechanically. [FCTM PR-AEP-MISC P 6/32, PDF 451; FCTM PR-AEP-MISC P 7/32, PDF 452]

## 2. Key limits
- **ΔP:** zero (check only if MAN CAB PR used) [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- **Engine agent 2:** not available [FCOM PRO-ABN-MISC P 16/30, PDF 3811]

## 3. Flow (PF / PM)
### 1. Stop and alert (aircraft stopped)
**1.1 PF**
- “STOP” [FCTM PR-AEP-MISC P 6/32, PDF 451]
- After an RTO; otherwise the Captain calls "I HAVE CONTROL" [FCTM PR-AEP-MISC P 6/32, PDF 451]
- CAPT: aircraft stopped, parking brake ON [FCTM PR-AEP-MISC P 6/32, PDF 451]
- “CABIN CREW, AT YOUR STATIONS” [PDP Emergency evacuation, PDF 493]
- PA [PDP Emergency evacuation, PDF 493]
- “EMERGENCY EVACUATION PROCEDURE” [PDP Emergency evacuation, PDF 493; PDP Management of abnormal operations, PDF 427]
**1.2 PM**
- EMER EVAC PROC …… PERFORM [PDP Emergency evacuation, PDF 493]

### 2. QRH EMER EVAC (F/O reads and does)
**2.1 PM**
- AIRCRAFT / PARKING BRK …… STOP / ON [FCOM PRO-ABN-MISC P 16/30, PDF 3811; QRH C2, PDF 294]
- ATC (VHF1) …… NOTIFY [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- CABIN CREW (PA) …… ALERT [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ΔP (only if MAN CAB PR has been used) …… CHECK ZERO [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- **If ΔP not at zero** [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - CAB PR MODE SEL …… MAN [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - V/S CTL …… FULL UP [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ALL ENG MASTER …… OFF [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ALL FIRE pb (ENGs & APU) …… PUSH [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ALL AGENTS (ENGs & APU) …… AS RQRD [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- F/O may set ENG MASTERs OFF and push FIRE pbs without Captain confirmation [FCTM PR-AEP-MISC P 7/32, PDF 452]
**2.2 PF**
- CAPT builds the evacuation decision from the circumstances [FCTM PR-AEP-MISC P 6/32, PDF 451]

### 3. Decision (Captain)
**3.1 PF**
- **If evacuation not required** [FCOM PRO-ABN-MISC P 16/30, PDF 3811; PDP Emergency evacuation, PDF 493]
  - “REMAIN SEATED, RESUME NORMAL DUTIES” [PDP Emergency evacuation, PDF 493; FCOM PRO-ABN-ABN-00 P 9/12, PDF 2832]
  - PA; notify ATC [PDP Emergency evacuation, PDF 493; FCTM PR-AEP-MISC P 7/32, PDF 452]
- **If evacuation required** [FCOM PRO-ABN-MISC P 16/30, PDF 3811; PDP Emergency evacuation, PDF 493]
  - EVACUATION …… INITIATE [FCOM PRO-ABN-MISC P 16/30, PDF 3811; PDP Emergency evacuation, PDF 493]
  - “EVACUATE, EVACUATE” [PDP Emergency evacuation, PDF 493; FCOM PRO-ABN-ABN-00 P 9/12, PDF 2832]
  - EVAC COMMAND pb …… PRESS [PDP Emergency evacuation, PDF 493; FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - Advise ATC if required [FCTM PR-AEP-MISC P 7/32, PDF 452]
**3.2 PM**
- **If evacuation required** [PDP Emergency evacuation, PDF 493]
  - EMER EVAC PROC …… CONTINUE [PDP Emergency evacuation, PDF 493]
  - “EMERGENCY EVACUATION PROCEDURE COMPLETED” [PDP Emergency evacuation, PDF 493]
**3.3 PF + PM**
- Then the flight crew evacuates [PDP Emergency evacuation, PDF 493]

## 4. Procedure
### QRH procedure (FCOM PRO-ABN-MISC [QRH] / QRH C2)
- AIRCRAFT / PARKING BRK …… STOP / ON [FCOM PRO-ABN-MISC P 16/30, PDF 3811; QRH C2, PDF 294]
- ATC (VHF1) …… NOTIFY — Only VHF 1 is available on batteries. [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- CABIN CREW (PA) …… ALERT — Short announcement: evacuation may be required. [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ΔP (only if MAN CAB PR has been used) …… CHECK ZERO [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- **If ΔP not at zero:** [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - CAB PR MODE SEL …… MAN [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - V/S CTL …… FULL UP [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ALL ENG MASTER …… OFF [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ALL FIRE pb (ENGs & APU) …… PUSH [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- ALL AGENTS (ENGs & APU) …… AS RQRD — Engine agent 2 not available; agents required if ENG or APU FIRE displayed. [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- **If evacuation required:** [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - EVACUATION …… INITIATE — Announce the evacuation; press the EVAC COMMAND pb. [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
- **If evacuation not required:** [FCOM PRO-ABN-MISC P 16/30, PDF 3811]
  - CABIN CREW AND PASSENGERS (PA) …… NOTIFY [FCOM PRO-ABN-MISC P 16/30, PDF 3811]

## 7. FCTM technique
- "CABIN CREW (PA)…ALERT" tells the cabin the flight crew still controls the situation and prevents an unwanted cabin-initiated evacuation (done in the RTO flow). [FCTM PR-AEP-MISC P 7/32, PDF 452]
- ΔP check does not apply after an RTO: at least one automatic pressure system is required for departure. [FCTM PR-AEP-MISC P 7/32, PDF 452]
- "EVACUATION…INITIATE" = notify cabin crew, press EVAC COMMAND, advise ATC — preferably in this order. [FCTM PR-AEP-MISC P 7/32, PDF 452]
- Until the order is given the evacuation can be deferred or cancelled; once ordered it is irreversible. [FCTM PR-AEP-MISC P 7/32, PDF 452]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG 1(2) FIRE (ON GROUND) · RTO | Engine fire on ground not extinguished | AGENT 1+2 DISCH → EMER EVAC PROC APPLY | [FCOM PRO-ABN-ENG P 93/226, PDF 3340] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- Company (THAI) phraseology is used instead of the generic Airbus/FCOM wording: “CABIN CREW, AT YOUR STATIONS” (PDP/FCOM: “ATTENTION CREW AT STATIONS”) and “REMAIN SEATED, RESUME NORMAL DUTIES” (PDP/FCOM: “CABIN CREW and PASSENGERS REMAIN SEATED”). [FCOM PRO-ABN-ABN-00 P 9/12, PDF 2832]
- HS-TO version omitted (FCOM PRO-ABN-MISC P 15/30). [FCOM PRO-ABN-MISC P 15/30, PDF 3810]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-MISC — [QRH] EMER EVAC | P 16/30 | 3811 | 18 FEB 26 |
| QRH | C2 EMER EVAC | C2 | 294–295 | 22 MAR 17 |
| FCTM | PR-AEP-MISC — EMER EVAC | P 6–7/32 | 451–452 | 26 MAY 26 |
| PDP | Emergency evacuation (XFTDA1EMREVAC01) | CAPT / F/O task sharing | 492–493 | JAN 2024 |
