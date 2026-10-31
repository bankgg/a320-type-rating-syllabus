# STALL RECOVERY — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Memory items · memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

Memory item for any stall indication. Reduce the angle of attack first: nose down pitch control and wings level. Only when the stall indications have stopped, increase thrust smoothly, check the speedbrakes retracted and recover the flight path smoothly. Minimizing the loss of altitude is secondary to regaining lift.

## 1. What it is
- **Trigger:** Any stall indication: aural warning, "STALL STALL" red message on the PFD, buffet, etc. [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCOM PRO-ABN-NAV P 123/124, PDF 3948]
- **Flight phase inhibition:** none [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCOM PRO-ABN-NAV P 123/124, PDF 3948]
- The stall is a condition where the angle of attack increases beyond a point such that the lift begins to decrease. Above AOAstall the airflow separates from the wing surface and the lift coefficient decreases. [FCTM PR-AEP-MISC P 23/32, PDF 468; FCTM PR-AEP-MISC P 24/32, PDF 469]
- The stall always occurs at the same angle of attack for a given configuration, Mach number and altitude. AOAstall depends on the aircraft configuration (slats, flaps, speed brakes), Mach and altitude, and wing contamination. [FCTM PR-AEP-MISC P 24/32, PDF 469; FCTM PR-AEP-MISC P 25/32, PDF 470]
- When the threshold is reached, permanent aural and visual alerts ("STALL, STALL" synthetic voice then cricket, "STALL STALL" red message on PFD) are triggered until a correct angle of attack is recovered. [FCOM PRO-ABN-NAV P 123/124, PDF 3948]
- Stall warnings give sufficient margin to alert the crew in advance of the actual stall, even with contaminated wings. Stall buffet is airframe vibration from the airflow separating when approaching AOAstall. [FCTM PR-AEP-MISC P 26/32, PDF 471]
- High altitude: buffeting increases due to the high Mach number, and both AOAstall and CL MAX decrease as Mach increases. For some Mach numbers the buffet may appear just before the stall warnings. [FCTM PR-AEP-MISC P 23/32, PDF 468; FCTM PR-AEP-MISC P 26/32, PDF 471]
- Near the maximum altitude, margins reach their required minimum. Icing conditions or turbulence could rapidly lead to a slowdown, a buffet onset, a stall condition and, subsequently, a high altitude upset. [PDP Unreliable speed indication (and UPRT), PDF 586]
- In alternate law the stall warnings are activated at an appropriate margin from the stall condition, the PFD speed scale shows a black/red barber pole below the stall warning, and the α floor protection is inoperative. In direct law, stall warnings are available as for alternate law. [FCOM DSC-27-20-20 P 12/20, PDF 1623; FCOM DSC-27-20-20 P 15/20, PDF 1626; FCOM DSC-27-20-20 P 17/20, PDF 1628]

## 2. Key limits
- **First action:** Nose down pitch control [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 26/32, PDF 471]
- **Bank:** Wings level [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- **Thrust:** Only when out of stall: increase smoothly as needed [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 26/32, PDF 471]
- **FLAPS 1:** Clean, below FL 200 and below VFE Next [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 27/32, PDF 472; PDP Unreliable speed indication (and UPRT), PDF 671]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF**
- Any stall indication: "STALL, STALL" synthetic voice then cricket, "STALL STALL" red message on the PFD, or buffet [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCOM PRO-ABN-NAV P 123/124, PDF 3948; FCTM PR-AEP-MISC P 26/32, PDF 471; PDP Stall recovery, PDF 542]
- “STALL, I have control” [FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833; PDP Stall recovery, PDF 543]

### 2. Reduce the angle of attack
**2.1 PF**
- NOSE DOWN PITCH CONTROL …… APPLY [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
- This will reduce angle of attack [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- **In the case of lack of pitch down authority** [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - Reducing thrust may be necessary [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 26/32, PDF 471; PDP Stall recovery, PDF 543]
- BANK …… WINGS LEVEL [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
- Simultaneously with the nose down order: wings level reduces the lift necessary for the flight and so the required angle of attack [FCTM PR-AEP-MISC P 26/32, PDF 471]

### 3. Increase energy
**3.1 PF**
- **When out of stall (no longer stall indications)** [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
  - THRUST …… INCREASE SMOOTHLY AS NEEDED [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
  - In the case of one engine inoperative, progressively compensate the thrust asymmetry with rudder [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - SPEEDBRAKES …… CHECK RETRACTED [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
  - FLIGHT PATH …… RECOVER SMOOTHLY [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
- **If a risk of ground contact exists, once clearly out of stall** [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - Establish smoothly a positive climb gradient [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- **If in clean configuration, below FL 200 and below VFE Next** [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 27/32, PDF 472; PDP Unreliable speed indication (and UPRT), PDF 671]
  - “FLAPS 1” [PDP Stall recovery, PDF 543]
**3.2 PM**
- FLAPS 1 …… SELECT [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]
- This increases the margin to the AOAstall [FCTM PR-AEP-MISC P 27/32, PDF 472; PDP Stall recovery, PDF 544]

## 4. Procedure
### [MEM] STALL RECOVERY (FCOM PRO-ABN-MISC P 2/30)
- *As soon as any stall indication (could be aural warning, "STALL STALL" red message on PFD, buffet, etc.) is recognized, apply the immediate actions:* [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- NOSE DOWN PITCH CONTROL …… APPLY [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- *This will reduce angle of attack* [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- *In the case of lack of pitch down authority, reducing thrust may be necessary.* [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- BANK …… WINGS LEVEL [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
- **When out of stall (no longer stall indications) :** [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - THRUST …… INCREASE SMOOTHLY AS NEEDED [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - *In the case of one engine inoperative, progressively compensate the thrust asymmetry with rudder.* [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - SPEEDBRAKES …… CHECK RETRACTED [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - FLIGHT PATH …… RECOVER SMOOTHLY [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - **If in clean configuration and below 20 000 ft :** [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
    - FLAPS 1 …… SELECT [FCOM PRO-ABN-MISC P 2/30, PDF 3797]
  - *If a risk of ground contact exists, once clearly out of stall (no longer stall indications), establish smoothly a positive climb gradient.* [FCOM PRO-ABN-MISC P 2/30, PDF 3797]

## 7. FCTM technique
- The immediate key action is to reduce the angle of attack with a nose down pitch order on the sidestick: this ensures an immediate aircraft response. [FCTM PR-AEP-MISC P 26/32, PDF 471]
- Minimizing the loss of altitude is secondary to reducing the angle of attack, as the first priority is to regain lift. [FCTM PR-AEP-MISC P 26/32, PDF 471]
- Immediate maximum thrust on stall recognition is not appropriate. Engine spool up makes the speed increase slow, so it does not reduce the angle of attack instantaneously, and the thrust increase from under wing mounted engines generates a pitch up that may prevent the reduction. [FCTM PR-AEP-MISC P 26/32, PDF 471]
- When stall indications have stopped and the aircraft has recovered sufficient energy, smoothly recover the initial flight path. [FCTM PR-AEP-MISC P 26/32, PDF 471]
- A stalled condition can exist in any attitude. Recover from the stall first, then apply the appropriate upset recovery technique. [FCTM PR-AEP-MISC P 29/32, PDF 474; PDP Unreliable speed indication (and UPRT), PDF 608; PDP Unreliable speed indication (and UPRT), PDF 667]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [MEM] STALL WARNING AT LIFTOFF | A separate memory item with different actions, for stall warnings triggered at liftoff. | THRUST: TOGA; At the same time: PITCH ATTITUDE 15°, BANK WINGS LEVEL; Callout: "STALL, TOGA 15°"; When a safe flight path and speed are achieved, consider warnings that are still active as spurious | [FCOM PRO-ABN-MISC P 3/30, PDF 3798; FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833; FCTM PR-AEP-MISC P 27/32, PDF 472] |
| UPSET PREVENTION AND RECOVERY | All upset recovery techniques assume the aircraft is not stalled. Once out of stall, apply the appropriate technique. | Nose high or nose low actions, as needed | [FCTM PR-AEP-MISC P 29/32, PDF 474; PDP Unreliable speed indication (and UPRT), PDF 608; PDP Unreliable speed indication (and UPRT), PDF 667] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FLAPS 1 condition differs between the sources: the FCOM says "If in clean configuration and below 20 000 ft", the FCTM says "below FL 200", and a PDP example says "if speed is still lower than VFE Next". The flow combines them as clean, below FL 200 and below VFE Next. Confirmed by the user. The verbatim FCOM procedure above is unchanged. [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 27/32, PDF 472; PDP Unreliable speed indication (and UPRT), PDF 671]
- The manuals describe no stick shaker. Their stall indications are the aural warning, the PFD message and buffet. Any training wording that mentions a stick shaker is left out of this brief. Confirmed by the user. [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCOM PRO-ABN-NAV P 123/124, PDF 3948]
- The manuals do not describe an "accelerated stall" by name. The nearest text is that a stalled condition can exist in any attitude. Linking such an exercise to this brief without further wording is confirmed by the user. [FCTM PR-AEP-MISC P 29/32, PDF 474]
- The FCOM gives the callout "STALL, I have control" without naming a pilot, and the manuals do not cover the PM noticing the stall first. The PDP slide shows the callout in the PF column, and this brief shows the PF. Confirmed by the user. The PF/PM split for FLAPS 1 also comes from the PDP slide. [FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833; PDP Stall recovery, PDF 543]
- This brief describes stall warnings in alternate and direct law only. Normal law, with its high angle-of-attack protection, is not covered. Confirmed by the user. [FCOM DSC-27-20-20 P 12/20, PDF 1623; FCOM DSC-27-20-20 P 15/20, PDF 1626; FCOM DSC-27-20-20 P 17/20, PDF 1628; FCOM DSC-27-20-10-20 P 9/14, PDF 1596]
- The manuals have no stall guidance specific to the landing configuration beyond the ground contact note, and FLAPS 1 applies only in clean configuration. Linking such an exercise to this brief is confirmed by the user. [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 27/32, PDF 472]
- The QRH has no stall recovery procedure, and the manuals give no other PM action for this procedure. [FCOM PRO-ABN-MISC P 2/30, PDF 3797; PDP Stall recovery, PDF 543]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-MISC — [MEM] STALL RECOVERY, [MEM] STALL WARNING AT LIFTOFF | P 2–3/30 | 3797–3798 | 18 FEB 26 |
| FCOM | PRO-ABN-ABN-00 — memory callouts | P 10/12 | 2833 | 26 MAY 26 |
| FCOM | PRO-ABN-NAV — STALL WARNING | P 123/124 | 3948 | 26 MAY 26 |
| FCOM | DSC-27-20-20 — alternate and direct law | P 12/20, 15/20, 17/20 | 1623, 1626, 1628 | 18 FEB 26 |
| FCOM | DSC-27-20-10-20 — high angle-of-attack protection | P 9/14 | 1596 | 18 FEB 26 |
| FCTM | PR-AEP-MISC — STALL RECOVERY | P 23–27/32 | 468–472 | 26 MAY 26 |
| FCTM | PR-AEP-MISC — UPSET PREVENTION AND RECOVERY | P 29/32 | 474 | 26 MAY 26 |
| PDP | Stall recovery (XFTDA4STALLRC01) | slides | 541–544 | OCT 2018 |
| PDP | Unreliable speed indication (and UPRT) (XFTDA6UNRASPD01) | slides | 586, 608, 667, 671 | OCT 2022 |
