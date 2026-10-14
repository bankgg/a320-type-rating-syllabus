# ENG 1(2) FIRE (ON GROUND) · RTO — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Red warning · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

An engine fire warning below V1: the Captain calls STOP and rejects the takeoff. Once stopped, the crew secures the aircraft, discharges both agents and — if the fire is not extinguished — goes to the QRH EMER EVAC procedure.

## 1. What it is
- **Trigger:** Fire detected by both loops, or by one loop with the other faulty, or both loops ruptured within 5 s. [FCOM PRO-ABN-ENG P 92/226, PDF 3339]
- **Flight phase inhibition:** none [FCOM PRO-ABN-ENG P 92/226, PDF 3339]
- ECAM inhibits non-essential alerts from 80 kt to 1 500 ft (or 2 min after lift-off): any alert in this period is significant. [FCTM PR-AEP-MISC P 18/32, PDF 463]
- Above 100 kt and below V1 the Captain is go-minded; a fire alert or severe damage is one of the few reasons to reject. [FCTM PR-AEP-MISC P 19/32, PDF 464]

## 2. Key limits
- **Reject above 100 kt:** fire alert is a reason [FCTM PR-AEP-MISC P 19/32, PDF 464]
- **Decision:** before V1 [FCTM PR-AEP-MISC P 19/32, PDF 464]
- **Reverse:** full, reduce passing 70 kt if runway allows [FCTM PR-AEP-MISC P 20/32, PDF 465]
- **Agents:** 1 + 2 together [FCOM PRO-ABN-ENG P 93/226, PDF 3340]

## 3. Flow (PF / PM)
### 1. Rejected takeoff (Captain decision)
**1.1 PF**
- “STOP!” [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 19/32, PDF 464; FCOM PRO-ABN-ABN-00 P 10–11/12, PDF 2833]
- The Captain is now PF — no “I have control” [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 19/32, PDF 464]
- ALL THRUST LEVERS …… IDLE [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
- REVERSE THRUST …… MAX AVAIL [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
- Simultaneously; A/BRK MAX decelerating → keep off the pedals, otherwise full manual braking [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 21/32, PDF 466]
- Below 72 kt: no ground spoilers, no autobrake — manual braking, NWS and differential braking [PDP Rejected takeoff, PDF 525; FCTM PR-AEP-MISC P 21/32, PDF 466]
**1.2 PM**
- REVERSERS / DECELERATION …… CHECK [PDP Rejected takeoff, PDF 527]
- “REVERSE GREEN” [PDP Rejected takeoff, PDF 527; FCOM PRO-ABN-ABN-00 P 10–11/12, PDF 2833]
- “DECEL” [PDP Rejected takeoff, PDF 527; FCOM PRO-ABN-ABN-00 P 10–11/12, PDF 2833]
- ANY AUDIO …… CANCEL [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]

### 2. Aircraft stopped
**2.1 PF**
- Consider positioning to keep the fire away from the fuselage [FCTM PR-AEP-MISC P 20/32, PDF 465]
- REVERSERS …… STOWED [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
- PARKING BRAKE …… ON [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
**2.2 PM**
- “THA ___, STOPPING” [PDP Rejected takeoff, PDF 527]
- Notify ATC [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
**2.3 PF**
- “CABIN CREW, AT YOUR STATIONS” [PDP Rejected takeoff, PDF 527; PDP Rejected takeoff, PDF 529]
- PA — alerts the cabin crew [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
**2.4 PM**
- EMERGENCY EVACUATION PROC (QRH) …… LOCATE [PDP Rejected takeoff, PDF 527; FCTM PR-AEP-MISC P 20/32, PDF 465]
**2.5 PF**
- “ECAM ACTIONS” [PDP Rejected takeoff, PDF 527; PDP Rejected takeoff, PDF 529; FCTM PR-AEP-MISC P 20/32, PDF 465]
**2.6 PM**
- ECAM actions are not confirmed on ground [PDP Emergency evacuation, PDF 493]

### 3. Fire procedure
**3.1 PM**
- THR LEVERS …… IDLE [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
- **WHEN A/C IS STOPPED** [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - PARKING BRK …… ON [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - ATC (VHF 1) …… NOTIFY [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - CABIN CREW (PA) …… ALERT [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - ENG MASTER (AFFECTED) …… OFF [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - ENG FIRE P/B (AFFECTED) …… PUSH [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - AGENT 1+2 …… DISCH [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - EMER EVAC PROC …… APPLY [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
**3.2 PF**
- Stay on the runway until it is clear that no evacuation is needed [FCTM PR-AEP-MISC P 21/32, PDF 466]

### 4. Evacuation decision
**4.1 PF**
- CAPT decides; see the EMER EVAC brief [FCTM PR-AEP-MISC P 6–7/32, PDF 451]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-ENG)
- THR LEVERS …… IDLE — Full reverse may be used to stop the aircraft. [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
- **WHEN A/C IS STOPPED:** [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - PARKING BRK …… ON [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - ATC (VHF 1) …… NOTIFY — Only VHF 1 is available on batteries. [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - CABIN CREW (PA) …… ALERT [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - ENG MASTER (AFFECTED) …… OFF [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - ENG FIRE P/B (AFFECTED) …… PUSH [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - AGENT 1+2 …… DISCH [FCOM PRO-ABN-ENG P 93/226, PDF 3340]
  - EMER EVAC PROC …… APPLY [FCOM PRO-ABN-ENG P 93/226, PDF 3340]

### RTO task sharing (FCTM) (FCTM PR-AEP-MISC)
- CAPT · "STOP" …… ANNOUNCE [FCTM PR-AEP-MISC P 20/32, PDF 465]
- CAPT · THRUST LEVERS …… IDLE [FCTM PR-AEP-MISC P 20/32, PDF 465]
- CAPT · REVERSE THRUST …… MAX AVAIL. [FCTM PR-AEP-MISC P 20/32, PDF 465]
- F/O · REVERSERS …… CHECK/ANNOUNCE [FCTM PR-AEP-MISC P 20/32, PDF 465]
- F/O · DECELERATION …… CHECK/ANNOUNCE [FCTM PR-AEP-MISC P 20/32, PDF 465]
- F/O · AUTOBRAKE …… MONITOR [FCTM PR-AEP-MISC P 20/32, PDF 465]
- F/O · ANY AUDIO …… CANCEL [FCTM PR-AEP-MISC P 20/32, PDF 465]
- **Aircraft stopped:** [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - CAPT · REVERSERS …… STOWED [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - CAPT · PARKING BRAKE …… ON [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - CAPT · CABIN CREW …… ALERT [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - CAPT · ECAM ACTIONS …… ORDER [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - F/O · ATC …… NOTIFY [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - F/O · EMER EVAC Procedure (QRH) …… LOCATE [FCTM PR-AEP-MISC P 20/32, PDF 465]
  - F/O · ECAM ACTIONS …… PERFORM [FCTM PR-AEP-MISC P 20/32, PDF 465]

## 7. FCTM technique
- The Captain keeps a hand on the thrust levers until V1, whether PF or PM. [FCTM PR-AEP-MISC P 19/32, PDF 464]
- "STOP" both confirms the decision and states the Captain has control — the only handover without "I have control". [FCTM PR-AEP-MISC P 19/32, PDF 464]
- Rejected before 72 kt or autobrake inoperative: reduce thrust and apply full pedal braking until stopped. [FCTM PR-AEP-MISC P 21/32, PDF 466]
- After an A/BRK MAX stop, disarm ground spoilers before taxiing; do not vacate until it is clear no evacuation is needed. [FCTM PR-AEP-MISC P 21/32, PDF 466]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] EMER EVAC | Fire not extinguishable | See the EMER EVAC brief | [FCOM PRO-ABN-MISC P 16/30, PDF 3811] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- Company (THAI) phraseology is used instead of the generic Airbus wording: PA “CABIN CREW, AT YOUR STATIONS” (PDP: “ATTENTION! CREW AT STATIONS”) and ATC call sign “THA ___” (PDP: “AIRBUS ___”). [PDP Rejected takeoff, PDF 527]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ENG — ENG 1(2) FIRE (ON GROUND) | P 92–93/226 | 3339–3340 | 26 MAY 26 |
| FCTM | PR-AEP-MISC — Rejected takeoff | P 18–21/32 | 463–466 | 26 MAY 26 |
| FCOM | PRO-ABN-ABN-00 — malfunction before V1 callouts | P 10–11/12 | 2833–2834 | 26 MAY 26 |
| PDP | Rejected takeoff (XFTDA6REJECTO01) | Task sharing, flow pattern | 524–529 | JUL 2021 |
