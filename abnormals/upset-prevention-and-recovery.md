# UPSET PREVENTION AND RECOVERY — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Technique · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL (FCTM technique).

A technique, with no ECAM or QRH procedure. The first pilot to see the divergence calls "NOSE HIGH" or "NOSE LOW". Assess the energy, confirm the attitude on the PFD and recover from any stall first. Then use the nose high or nose low actions as needed and recover the level flight at a sufficient airspeed.

## 1. What it is
- **Trigger:** An upset condition exists any time an aircraft diverges from what the flight crew is intending to do. [FCTM PR-AEP-MISC P 28/32, PDF 473]
- **Flight phase inhibition:** none [FCTM PR-AEP-MISC P 28/32, PDF 473]
- An upset is an undesired aircraft state characterized by unintentional divergences from parameters normally experienced during operations. It may involve pitch and/or bank angle divergences and may lead to inappropriate airspeeds for the conditions. [FCTM PR-AEP-MISC P 28/32, PDF 473]
- Prevention relies on effective monitoring of the environment, the aircraft energy state, the flight path and the technical state (flight control laws, system failures). All flight crew members are responsible for it. [FCTM PR-AEP-MISC P 28/32, PDF 473]
- When the abnormal attitude law engages: pitch alternate law with no protection (no load factor limitation), roll direct law, yaw mechanical law. Autotrim is not available, so USE MAN PITCH TRIM is displayed on the PFDs, and F/CTL DIRECT LAW is displayed on the ECAM. [FCOM DSC-27-20-20 P 18/20, PDF 1629]
- Back within the normal flight envelope, these conditions remain for the remainder of the flight: pitch alternate law without reduced protection, roll direct law, yaw alternate law, and F/CTL ALTN LAW on the ECAM. [FCOM DSC-27-20-20 P 18/20, PDF 1629]

## 2. Key limits
- **Callout:** NOSE HIGH or NOSE LOW [FCTM PR-AEP-MISC P 29/32, PDF 474]
- **Primary reference:** PFD [FCTM PR-AEP-MISC P 29/32, PDF 474; PDP Unreliable speed indication (and UPRT), PDF 608]
- **Nose high: bank:** Must not exceed 60° [FCTM PR-AEP-MISC P 31/32, PDF 476]
- **Nose low: roll:** Shortest direction to wings level [FCTM PR-AEP-MISC P 31/32, PDF 476]

## 3. Flow (PF / PM)
### 1. Recognise and confirm
**1.1 PF + PM**
- **First pilot to observe the divergence** [FCTM PR-AEP-MISC P 29/32, PDF 474]
  - “NOSE HIGH” [FCTM PR-AEP-MISC P 29/32, PDF 474; PDP Unreliable speed indication (and UPRT), PDF 611]
  - “NOSE LOW” [FCTM PR-AEP-MISC P 29/32, PDF 474; PDP Unreliable speed indication (and UPRT), PDF 625]
- Assess the energy: airspeed, altitude, attitude, load factor, thrust setting, position of drag and high-lift devices, and the rate of change of those conditions [FCTM PR-AEP-MISC P 29/32, PDF 474]
- Determine the pitch and bank angle on the PFD, and communicate with the other crew member [FCTM PR-AEP-MISC P 29/32, PDF 474]
- Confirm the attitude: nose low, normally airspeed increasing, altitude decreasing, VSI descent; nose high, normally airspeed decreasing, altitude increasing, VSI climb [FCTM PR-AEP-MISC P 29/32, PDF 474]
- Check other attitude sources: standby attitude indications, the PM instruments, references outside the cockpit when possible [FCTM PR-AEP-MISC P 30/32, PDF 475]
- **If stalled (stall buffet and/or stall aural alert)** [FCTM PR-AEP-MISC P 29/32, PDF 474]
  - Apply the stall recovery procedure first [FCTM PR-AEP-MISC P 29/32, PDF 474; PDP Unreliable speed indication (and UPRT), PDF 608]
- To avoid dual inputs, know at all times who has control. If the PM wants to act on the sidestick: announce "I have control", then press and maintain the sidestick pushbutton [FCTM PR-AEP-MISC P 29/32, PDF 474; FCTM AOP-10-30-20 P 1/2, PDF 62]

### 2. Nose high
**2.1 PF**
- Takeover and disconnect AP and A/THR [FCTM PR-AEP-MISC P 30/32, PDF 475; PDP Unreliable speed indication (and UPRT), PDF 612]
- If the AP and A/THR responses enable to stop the flight path divergence, the flight crew may keep them engaged [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 613]
- Apply nose down pitch order: as much as required to obtain a nose down pitch rate [FCTM PR-AEP-MISC P 30/32, PDF 475; FCTM PR-AEP-MISC P 31/32, PDF 476]
- **In the case of lack of pitch down authority** [FCTM PR-AEP-MISC P 31/32, PDF 476]
  - Use incremental inputs on the trim (nose down) to improve the effectiveness of the elevator control [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 615]
  - Excessive use of pitch trim may make the upset situation worse or may result in high structural loads [FCTM PR-AEP-MISC P 30/32, PDF 475; PDP Unreliable speed indication (and UPRT), PDF 615]
- Adjust the thrust: select up to maximum thrust available while ensuring adequate pitch control [FCTM PR-AEP-MISC P 30/32, PDF 475; FCTM PR-AEP-MISC P 31/32, PDF 476]
- Increasing thrust may reduce the effectiveness of nose-down pitch control. It may be necessary to limit or reduce thrust to the point where control of the pitch is achieved [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 617]
- Adjust the roll not to exceed 60 degrees [FCTM PR-AEP-MISC P 30/32, PDF 475; FCTM PR-AEP-MISC P 31/32, PDF 476]
- **If all normal pitch control techniques are unsuccessful** [FCTM PR-AEP-MISC P 31/32, PDF 476]
  - Keep the current bank angle or bank the aircraft to enable the nose to drop toward the horizon [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 619]
  - The least bank possible to start the nose down, never exceeding approximately 60°. If already greater than 60°, reduce it to less than 60° [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 619]
- Recover the level flight [FCTM PR-AEP-MISC P 30/32, PDF 475]
- At a sufficient airspeed while avoiding a stall due to premature recovery at low speed, or excessive g-loading at high speed [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 621]
**2.2 PM**
- Monitor the airspeed and the attitude throughout the recovery [FCTM PR-AEP-MISC P 30/32, PDF 475]
- Announce the flight path divergence if the recovery maneuver is not efficient [FCTM PR-AEP-MISC P 30/32, PDF 475]

### 3. Nose low
**3.1 PF**
- Takeover and disconnect AP and A/THR [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 626]
- If the AP and A/THR responses enable to stop the flight path divergence, the flight crew may keep them engaged [FCTM PR-AEP-MISC P 32/32, PDF 477; PDP Unreliable speed indication (and UPRT), PDF 627]
- **If required** [FCTM PR-AEP-MISC P 31/32, PDF 476]
  - Recover from stall [FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 628]
  - Even in a nose low situation, the aircraft may be stalled and it would be necessary to recover from a stall first [FCTM PR-AEP-MISC P 32/32, PDF 477; PDP Unreliable speed indication (and UPRT), PDF 629]
- Excessive use of pitch trim may make the upset situation worse or may result in high structural loads [FCTM PR-AEP-MISC P 31/32, PDF 476]
- Adjust the roll in the shortest direction to wings level [FCTM PR-AEP-MISC P 31/32, PDF 476]
- A nose low with high angle of bank requires prompt action, because the decreasing altitude is rapidly being exchanged for an increasing airspeed. It may be necessary to reduce the g-loading to improve roll effectiveness. The bank angle indicator shows the shortest direction [FCTM PR-AEP-MISC P 32/32, PDF 477; PDP Unreliable speed indication (and UPRT), PDF 631]
- Adjust the thrust and the drag: reduce the thrust and/or use the speedbrakes to control the speed [FCTM PR-AEP-MISC P 31/32, PDF 476; FCTM PR-AEP-MISC P 32/32, PDF 477]
- Recover the level flight [FCTM PR-AEP-MISC P 31/32, PDF 476]
- At a sufficient airspeed while avoiding a stall due to premature recovery at low speed, or excessive g-loading at high speed [FCTM PR-AEP-MISC P 32/32, PDF 477; PDP Unreliable speed indication (and UPRT), PDF 635]
**3.2 PM**
- Monitor the airspeed and the attitude throughout the recovery [FCTM PR-AEP-MISC P 30/32, PDF 475]
- Announce the flight path divergence if the recovery maneuver is not efficient [FCTM PR-AEP-MISC P 30/32, PDF 475]

## 4. Procedure
### Nose High Actions (FCTM PR-AEP-MISC P 30/32)
- *Recognize and confirm the situation* [FCTM PR-AEP-MISC P 30/32, PDF 475]
- *Takeover and disconnect AP and A/THR* [FCTM PR-AEP-MISC P 30/32, PDF 475]
- *Apply nose down pitch order* [FCTM PR-AEP-MISC P 30/32, PDF 475]
- *Excessive use of pitch trim may make the upset situation worse or may result in high structural loads.* [FCTM PR-AEP-MISC P 30/32, PDF 475]
- *Adjust the thrust* [FCTM PR-AEP-MISC P 30/32, PDF 475]
- *Adjust the roll not to exceed 60 degrees* [FCTM PR-AEP-MISC P 30/32, PDF 475]
- *Recover the level flight* [FCTM PR-AEP-MISC P 30/32, PDF 475]

### Nose Low Actions (FCTM PR-AEP-MISC P 31/32)
- *Recognize and confirm the situation* [FCTM PR-AEP-MISC P 31/32, PDF 476]
- *Takeover and disconnect AP and A/THR* [FCTM PR-AEP-MISC P 31/32, PDF 476]
- *Recover from stall if required* [FCTM PR-AEP-MISC P 31/32, PDF 476]
- *Excessive use of pitch trim may make the upset situation worse or may result in high structural loads.* [FCTM PR-AEP-MISC P 31/32, PDF 476]
- *Adjust the roll in the shortest direction to wings level* [FCTM PR-AEP-MISC P 31/32, PDF 476]
- *Adjust the thrust and the drag* [FCTM PR-AEP-MISC P 31/32, PDF 476]
- *Recover the level flight* [FCTM PR-AEP-MISC P 31/32, PDF 476]

## 6. QRH and reference tables
### Abnormal attitude law 
The law engages when one of these values is reached.

| Parameter | Value |
|---|---|
| Bank angle | Above 125° |
| Pitch attitude, if at least 2 ADC are valid and consistent | Above 50° nose up or below 30° nose down |
| Pitch attitude, in all other cases | Above 40° nose up or below 20° nose down |
| Speed | Below 70 to 90 kt (depending on the aircraft pitch attitude), or above 440 kt |
| Mach | Above 0.91 |
| Angle of attack | Above 40° |
[FCOM DSC-27-20-20 P 18/20, PDF 1629]

## 7. FCTM technique
- The nose high and nose low techniques are a logical progression and are not necessarily procedural. The sequence is guidance only: a series of options to consider depending on the situation. The crew may apply these actions or part of them, mainly if the recovery is effective. [FCTM PR-AEP-MISC P 30/32, PDF 475; PDP Unreliable speed indication (and UPRT), PDF 608]
- Troubleshooting the cause of the upset is secondary to initiating the recovery, but the pilot must still recognize and confirm the situation first. [PDP Unreliable speed indication (and UPRT), PDF 611; FCTM PR-AEP-MISC P 29/32, PDF 474]
- All upset recovery techniques assume the aircraft is not stalled. When needed, recover from the stall first. [PDP Unreliable speed indication (and UPRT), PDF 608; FCTM PR-AEP-MISC P 29/32, PDF 474]
- The PFD is a primary reference for recovery. Even in extreme attitudes, some portion of the sky or ground indications is present on the pitch scale, and the bank indicator gives the aircraft bank. [FCTM PR-AEP-MISC P 29/32, PDF 474]
- Avoid exaggerated control inputs through reflex responses. Inputs must be smooth, positive and proportional to the amount and rate of pitch, roll or yaw experienced. [PDP Unreliable speed indication (and UPRT), PDF 608]
- Aggressive and opposite flight control inputs must not be applied: they can lead to loads higher than the limit and result in structural damage or failure. If you sense an over control, set the sidestick to the neutral position. [PDP Unreliable speed indication (and UPRT), PDF 574]
- The rudder should not be used to induce roll, or to counter roll induced by any type of turbulence. [PDP Unreliable speed indication (and UPRT), PDF 575]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [MEM] STALL RECOVERY | A stalled condition can exist in any attitude and takes priority over the upset actions. | NOSE DOWN PITCH CONTROL: APPLY; BANK: WINGS LEVEL; When out of stall: thrust, speedbrakes, flight path | [FCOM PRO-ABN-MISC P 2/30, PDF 3797; FCTM PR-AEP-MISC P 29/32, PDF 474] |
| LOW ENERGY | The "SPEED, SPEED, SPEED" aural alert (if installed) announces a low energy situation. See Gaps. | Increase the thrust and/or adjust the pitch depending on the situation, until the aural alert stops; Available in CONF 2, 3 and FULL; Inhibited when TOGA is selected, below 100 ft RA, above 2 000 ft RA, at alpha floor or a ground proximity warning system alert, in alternate or direct law, or if both radio altimeters fail | [FCTM PR-AEP-MISC P 12/32, PDF 457; FCOM DSC-22_40-30 P 4/4, PDF 1279; FCOM DSC-27-20-10-20 P 13/14, PDF 1600] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The manuals have no ECAM or QRH procedure for an upset. This brief uses the FCTM technique and the PDP slides. Including it as a brief is confirmed by the user. [FCTM PR-AEP-MISC P 30/32, PDF 475]
- The manuals do not describe inverted flight by name. The nearest text is the nose low technique and the abnormal attitude law above 125° of bank. Linking such an exercise to this brief without further wording is confirmed by the user. [FCTM PR-AEP-MISC P 31/32, PDF 476; FCTM PR-AEP-MISC P 32/32, PDF 477; FCOM DSC-27-20-20 P 18/20, PDF 1629]
- The FCTM says the PF applies the required actions but says "flight crew" for the pitch trim. The PF on the pitch trim wheel is instructor practice, not from the manuals. [FCTM PR-AEP-MISC P 30/32, PDF 475; FCTM PR-AEP-MISC P 31/32, PDF 476]
- The FCOM system description applies the low energy aural alert to ALL, but another FCOM page heads it "IF INSTALLED", the FCTM says "if available", and the IF INSTALLED table in FCOM GEN has no row for it. Whether HS-TX aircraft have it is unconfirmed. Keeping the Related entry on that basis is confirmed by the user. [FCOM DSC-22_40-30 P 4/4, PDF 1279; FCOM DSC-27-20-10-20 P 13/14, PDF 1600; FCTM PR-AEP-MISC P 12/32, PDF 457; FCOM GEN P 29/78, PDF 122]
- The manuals do not describe a nose high, low energy exercise by name. Linking such an exercise to this brief, which says to recover from any stall first, is confirmed by the user. [FCTM PR-AEP-MISC P 29/32, PDF 474; FCTM PR-AEP-MISC P 30/32, PDF 475]
- The manuals give no callout wording for the PM announcing an inefficient recovery, beyond "NOSE HIGH" and "NOSE LOW". [FCTM PR-AEP-MISC P 29/32, PDF 474; FCTM PR-AEP-MISC P 30/32, PDF 475]
- The PDP lists the takeover step as "(if required)" where the FCTM figure relies on its note (1); the meaning is the same. The FCTM figure also places the pitch trim note in the nose low actions, and the PDP nose low slides do not show it. This brief follows the FCTM. [FCTM PR-AEP-MISC P 30/32, PDF 475; FCTM PR-AEP-MISC P 31/32, PDF 476; PDP Unreliable speed indication (and UPRT), PDF 626]
- After recovery, the PDP slide shows yaw mechanical control, and the FCOM says the yaw alternate law is active. This brief follows the FCOM. [FCOM DSC-27-20-20 P 18/20, PDF 1629; PDP Unreliable speed indication (and UPRT), PDF 577]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCTM | PR-AEP-MISC — UPSET PREVENTION AND RECOVERY | P 28–32/32 | 473–477 | 26 MAY 26 |
| FCTM | PR-AEP-MISC — LOW ENERGY | P 12/32 | 457 | 26 MAY 26 |
| FCTM | AOP-10-30-20 — USE OF SIDESTICK | P 1/2 | 62 | 25 FEB 25 |
| FCOM | DSC-27-20-20 — ABNORMAL ATTITUDE LAWS | P 18/20 | 1629 | 18 FEB 26 |
| FCOM | DSC-22_40-30 — LOW - ENERGY AURAL ALERT | P 4/4 | 1279 | 18 FEB 26 |
| FCOM | DSC-27-20-10-20 — low energy aural alert | P 13/14 | 1600 | 18 FEB 26 |
| FCOM | GEN — IF INSTALLED TABLE | P 7–46/78 | 100–139 | 14 JUL 26 |
| FCOM | PRO-ABN-MISC — [MEM] STALL RECOVERY | P 2/30 | 3797 | 18 FEB 26 |
| PDP | Unreliable speed indication (and UPRT) (XFTDA6UNRASPD01) | slides | 574–577, 608–636 | OCT 2022 |
