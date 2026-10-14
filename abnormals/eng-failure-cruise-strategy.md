# ENGINE FAILURE IN CRUISE · drift-down strategy — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Technique · no memory items**  
**Applicability:** all HS-TX — FCTM technique and Airbus PDP tutorial; applies to all HS-TX.

After an engine failure at cruise level the aircraft cannot hold its altitude. The PF sets MCT with A/THR off, sets a heading and determines the engine-out recovery altitude, then drifts down at M.78/300 kt (standard strategy) to the EO LRC ceiling, never below green dot. After an engine fire, the fire drill is done first and without delay.

## 1. What it is
- **Trigger:** Engine failure or engine shutdown (including after an engine fire) at cruise level. [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 506]
- **Flight phase inhibition:** none [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 506]
- Three strategies exist: standard, obstacle and fixed speed. Unless a specific procedure was set at dispatch (ETOPS, mountainous areas), the standard strategy is used. [FCTM PR-AEP-ENG P 15/26, PDF 416]

## 2. Key limits
- **Thrust:** MCT · A/THR off [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 506]
- **Standard strategy:** M.78 / 300 kt [FCTM PR-AEP-ENG P 15/26, PDF 416]
- **Minimum speed:** Green dot [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 506]

## 3. Flow (PF / PM)
### 1. Drift down (standard strategy)
**1.1 PF + PM**
- After an engine fire, the fire drill comes first and without delay; the PF flies the strategy around it. No obstacle constraint → standard strategy [FCTM PR-AEP-ENG P 18/26, PDF 419; PDP Engine failure in cruise, PDF 507; FCTM PR-AEP-ENG P 15/26, PDF 416]
**1.2 PF**
- ALL THRUST LEVERS …… MCT [PDP Engine failure in cruise, PDF 506; FCTM PR-AEP-ENG P 15/26, PDF 416]
- A/THR …… OFF [PDP Engine failure in cruise, PDF 506; FCTM PR-AEP-ENG P 15/26, PDF 416]
- A/THR off so thrust is not reduced when selecting speed or OPEN DES; MCT is frozen [PDP Engine failure in cruise, PDF 506; FCTM PR-AEP-ENG P 15/26, PDF 416]
- Never decelerate below green dot; at high levels and weights do not delay the descent [PDP Engine failure in cruise, PDF 506; FCTM PR-AEP-ENG P 15/26, PDF 416]
- **If the failure occurs below the EO LRC ceiling** [PDP Engine failure in cruise, PDF 511]
  - Keep A/THR on [PDP Engine failure in cruise, PDF 511]
**1.3 PF + PM**
- STRATEGY …… DETERMINE [PDP Engine failure in cruise, PDF 506; PDP Engine failure in cruise, PDF 507]
**1.4 PM**
- ATC …… NOTIFY [PDP Engine failure in cruise, PDF 506]
- After an engine fire this is already done in the ECAM actions [FCOM PRO-ABN-ENG P 91/226, PDF 3338]
**1.5 PF**
- HDG …… SET AS APPROPRIATE AND PULL [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
- ENGINE OUT RECOVERY ALTITUDE …… DETERMINE [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
- MCDU PROG page REC MAX = EO LRC ceiling; do not press EO CLR [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 16/26, PDF 417; PDP Engine failure in cruise, PDF 507]
- **When ready for descent** [PDP Engine failure in cruise, PDF 508]
  - M.78 / 300 KT …… SET AND PULL [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
  - EO LRC CEILING ALTITUDE …… SET AND PULL [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
  - OPEN DES; with A/THR off the elevator holds the target speed. Managed speed would target green dot [FCTM PR-AEP-ENG P 15/26, PDF 416; PDP Engine failure in cruise, PDF 508]
- **When V/S < 500 ft/min in descent** [PDP Engine failure in cruise, PDF 510]
  - V/S − 500 FT/MIN …… SET AND PULL [PDP Engine failure in cruise, PDF 510; FCTM PR-AEP-ENG P 16/26, PDF 417]
  - A/THR …… ON [PDP Engine failure in cruise, PDF 510; FCTM PR-AEP-ENG P 16/26, PDF 417]
- **When reaching the EO LRC ceiling (ALT CRZ)** [PDP Engine failure in cruise, PDF 510]
  - SPEED …… MANAGE [PDP Engine failure in cruise, PDF 510]

## 4. Procedure
### Engine failure in cruise — standard strategy (FCTM PR-AEP-ENG / PDP)
- ALL THRUST LEVERS …… MCT [PDP Engine failure in cruise, PDF 506; FCTM PR-AEP-ENG P 15/26, PDF 416]
- A/THR …… OFF [PDP Engine failure in cruise, PDF 506; FCTM PR-AEP-ENG P 15/26, PDF 416]
- **If the failure occurs below the EO LRC ceiling:** [PDP Engine failure in cruise, PDF 511]
  - *Keep A/THR on* [PDP Engine failure in cruise, PDF 511]
- STRATEGY …… DETERMINE [PDP Engine failure in cruise, PDF 506; PDP Engine failure in cruise, PDF 507]
- ATC …… NOTIFY [PDP Engine failure in cruise, PDF 506]
- HDG …… SET AS APPROPRIATE AND PULL [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
- ENGINE OUT RECOVERY ALTITUDE …… DETERMINE [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
- **When ready for descent:** [PDP Engine failure in cruise, PDF 508]
  - M.78 / 300 KT …… SET AND PULL [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
  - EO LRC CEILING ALTITUDE …… SET AND PULL [PDP Engine failure in cruise, PDF 508; FCTM PR-AEP-ENG P 15/26, PDF 416]
- **When V/S < 500 ft/min in descent:** [PDP Engine failure in cruise, PDF 510]
  - V/S − 500 FT/MIN …… SET AND PULL [PDP Engine failure in cruise, PDF 510; FCTM PR-AEP-ENG P 16/26, PDF 417]
  - A/THR …… ON [PDP Engine failure in cruise, PDF 510; FCTM PR-AEP-ENG P 16/26, PDF 417]
- **When reaching the EO LRC ceiling (ALT CRZ):** [PDP Engine failure in cruise, PDF 510]
  - SPEED …… MANAGE [PDP Engine failure in cruise, PDF 510]

## 7. FCTM technique
- Engine failure in cruise: unless a dispatch procedure exists, use the standard strategy, M 0.78/300 kt to the REC MAX EO (LRC engine-out ceiling). Obstacle strategy: green dot to the drift-down ceiling, then standard when clear. [FCTM PR-AEP-ENG P 15/26, PDF 416; FCTM PR-AEP-ENG P 16/26, PDF 417]
- Do not hurry the ECAM actions in cruise — complete the drill correctly. [FCTM PR-AEP-ENG P 15/26, PDF 416]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG 1(2) FIRE (IN FLIGHT) | When the engine failure is a fire | Fire drill first, without delay | [FCOM PRO-ABN-ENG P 91/226, PDF 3338] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No source puts the fire drill and the cruise strategy in one sequence. The fire procedure is applied without delay (FCTM), while the cruise flow sets MCT and A/THR off first and starts ECAM “when appropriate” (PDP). The brief keeps the fire drill first. [FCTM PR-AEP-ENG P 18/26, PDF 419; PDP Engine failure in cruise, PDF 508]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCTM | PR-AEP-ENG — Engine failure during cruise | P 15–16/26 | 416–417 | 26 MAY 26 |
| PDP | Engine failure in cruise (EFTDA1ENGFCRZ01) | — | 505–511 | JAN 2024 |
