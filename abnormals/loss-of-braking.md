# LOSS OF BRAKING — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Memory items · memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

Memory items for no braking on the ground. Set maximum reverse, release the pedals, then have the PM switch A/SKID & N/W STRG OFF so the ABCU gives alternate braking. Only then press the pedals again, with brake pressure limited to 1 000 PSI. If there is still no braking, use short successive parking brake applications. Nosewheel steering and antiskid are lost, so steer with the rudder and differential braking.

## 1. What it is
- **Trigger:** No perceived effect on the deceleration when applying manual braking, after the PF took over the autobrake (if used), during a RTO, the landing roll or taxi. [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 1/2, PDF 396]
- **Flight phase inhibition:** none [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 1/2, PDF 396]
- The procedure lets the crew manually activate alternate braking without antiskid when the normal braking mode has failed and the automatic switch to alternate braking has also failed. If that fails too, it asks for the parking brake. [FCTM PR-AEP-BRK P 1/2, PDF 396]
- It results in the loss of nosewheel steering and of the antiskid function. [FCTM PR-AEP-BRK P 1/2, PDF 396]
- In alternate braking without antiskid, autobrake and antiskid are inoperative. Brake pressure is limited to 1 000 PSI automatically, to limit the risk of wheel locking and tire burst. [FCOM DSC-32-30-10 P 6/8, PDF 2047]

## 2. Key limits
- **MAX BRK PR:** 1 000 PSI [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
- **REV:** MAX; may be kept to full stop if needed [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
- **Below 70 kt:** Idle reverse once the aircraft can stop on the runway [FCTM PR-AEP-BRK P 1/2, PDF 396]
- **Accumulator:** At least 7 full brake applications [FCOM DSC-32-30-10 P 6/8, PDF 2047]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF**
- Take over the autobrake (if used) and apply manual braking [FCTM PR-AEP-BRK P 1/2, PDF 396; FCTM PR-AEP-MISC P 21/32, PDF 466]
- Apply this procedure only if no effect is felt on the deceleration. On a wet or contaminated runway the felt deceleration may be lower and antiskid cycling can be felt: an undue application can affect landing performance [FCTM PR-AEP-BRK P 1/2, PDF 396]
- “LOSS OF BRAKING” [FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833]

### 2. Memory items
**2.1 PF**
- REV …… MAX [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
- BRAKE PEDALS …… RELEASE [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
- Release before the PM selects A/SKID off: this avoids brutal braking application [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
- “A/SKID OFF” [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
**2.2 PM**
- A/SKID & N/W STRG …… OFF [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
- Braking transfers from the BSCU to the ABCU: alternate braking mode [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
**2.3 PF**
- BRAKE PEDALS …… PRESS [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
- Only after the PM has set the switch OFF [FCTM PR-AEP-BRK P 2/2, PDF 397]
- MAX BRK PR …… 1000 PSI [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
- Monitor brake pressure on the BRAKES PRESS indicator [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
- Directional control: rudder at high speed, then differential braking (if recovered) [FCTM PR-AEP-BRK P 1/2, PDF 396]

### 3. If still no braking
**3.1 PF**
- PARK BRAKE …… USE [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
- Short successive parking brake applications. Delay until low speed if possible, to reduce the risk of tire burst and lateral control difficulties [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024; FCTM PR-AEP-BRK P 2/2, PDF 397]
- Brake onset asymmetry may be felt at each application [FCTM PR-AEP-BRK P 2/2, PDF 397]

## 4. Procedure
### [MEM] LOSS OF BRAKING (FCOM PRO-ABN-BRAKES P 1/22)
- **If no braking:** [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - REV …… MAX [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - *If needed, the flight crew may keep maximum reverse thrust until full aircraft stop.* [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - BRAKE PEDALS …… RELEASE [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - *When the flight crew sets the A/SKID & N/W STRG sw to OFF, the control of the braking system is transferred from the BSCU to the ABCU, and the alternate braking mode is activated. Consequently the PF should release the brake pedals before the PM selects the A/SKID off. This action avoids brutal braking application.* [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - A/SKID OFF …… ORDER [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - *The PF orders the PM to set the A/SKID & N/W STRG sw to OFF.* [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - A/SKID & N/W STRG …… OFF [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - BRAKE PEDALS …… PRESS [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - MAX BRK PR …… 1000 PSI [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - *The ABCU automatically limits the brake pressure to 1 000 PSI. Monitor brake pressure on the BRAKES PRESS indicator.* [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
  - **If still no braking:** [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
    - PARK BRAKE …… USE [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
    - *Use short successive parking brake applications to stop the aircraft.* [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]

## 7. FCTM technique
- Sequence the switch to alternate braking in three steps. The PF should: 1. Release the brake pedals. 2. Request the PM to set the A/SKID & N/W STRG sw to OFF. 3. Press the brake pedals, only after the PM has set the sw to OFF. [FCTM PR-AEP-BRK P 1/2, PDF 396; FCTM PR-AEP-BRK P 2/2, PDF 397]
- Full reverse may be used to a complete stop if needed. Below 70 kt, when the crew considers that the aircraft can stop on the runway, set idle reverse. Unless required by an emergency, avoid high reverse thrust at low speed, to avoid engine stall and excessive EGT. [FCTM PR-AEP-BRK P 1/2, PDF 396]
- When reverse is reduced from REV MAX to REV IDLE, be prepared to perceive a change in the felt deceleration. [FCTM PR-AEP-BRK P 1/2, PDF 396]
- During a RTO: if normal braking is inoperative, immediately apply the LOSS OF BRAKING memory items. [FCTM PR-AEP-MISC P 21/32, PDF 466]

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCOM gives the callout "LOSS OF BRAKING" and PARK BRAKE USE without naming a pilot. The brief shows the PF for both, confirmed by the user. [FCOM PRO-ABN-ABN-00 P 10/12, PDF 2833; FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]
- The PDP has no module for this procedure. [FCOM PRO-ABN-BRAKES P 1/22, PDF 3024]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-BRAKES — [MEM] LOSS OF BRAKING | P 1/22 | 3024 | 18 FEB 26 |
| FCTM | PR-AEP-BRK — LOSS OF BRAKING; PR-AEP-MISC — RTO | P 1–2/2; P 21/32 | 396–397, 466 | 26 MAY 26 |
| FCOM | DSC-32-30-10 — braking modes; PRO-ABN-ABN-00 — memory callouts | P 6/8; P 10/12 | 2047, 2833 | 26 MAY 26 |
