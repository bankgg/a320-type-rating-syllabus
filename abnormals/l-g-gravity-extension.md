# L/G GRAVITY EXTENSION — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** all HS-TX — QRH and FCOM blocks for ALL aircraft.

The gear free-falls when the handcrank is pulled and turned 3 turns clockwise to the mechanical stop. Then set the L/G lever DOWN and check the gear down indications. Do not apply it if at least one green triangle shows on each gear. After a successful extension do not reset the free-fall system; if it fails, apply LDG WITH ABNORMAL L/G.

## 1. What it is
- **Trigger:** A QRH procedure, requested by L/G GRVTY PROC on an ECAM STATUS page or after L/G GEAR NOT DOWNLOCKED. [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- **Flight phase inhibition:** none [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- Lever DOWN after gravity extension extinguishes the UNLK lights on the LDG GEAR indicator panel, avoids the L/G CTL message on the WHEEL SD page, and minimizes the risk of gear retraction on the ground if the free-fall system is reset. [FCOM PRO-ABN-LG P 7/30, PDF 3772]
- Do not reset the free-fall system: this avoids further fluid loss in a leak, or a possible gear unlock if a gear selector valve is jammed UP. It may be reset on training flights; if the green system is available the reset allows the doors to close. The crew should not reset it on the ground after the flight. [FCOM PRO-ABN-LG P 8/30, PDF 3773]
- The display may show the gear doors in the amber transit position, depending on speed. [FCOM PRO-ABN-LG P 8/30, PDF 3773]
- With both LGCIUs failed, the gear position indications on the ECAM are lost; the LDG GEAR lights remain if LGCIU 1 is electrically supplied. [FCOM PRO-ABN-LG P 8/30, PDF 3773]
- With gear and doors extended, fuel consumption is increased (QRH factor 145 % for all HS-TX). [QRH 24.02B, PDF 217; QRH OPS.04D, PDF 276; QRH OPS.04F, PDF 278]

## 2. Key limits
- **Handcrank:** 3 turns clockwise, to the mechanical stop, even if resistance is felt [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- **Do not apply if:** At least one green triangle on each gear on the WHEEL SD page [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- **After L/G GEAR NOT DOWNLOCKED, if time permits:** Up to 4 recycles: wait at least 60 s after each; then wait at least 120 s [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- **Fuel penalty, gear and doors open:** 145 % [QRH OPS.04D, PDF 276; QRH OPS.04F, PDF 278]

## 3. Flow (PF / PM)
### 1. Order
**1.1 PF**
- “L/G GRAVITY EXTENSION PROCEDURE” [PDP Management of abnormal operations, PDF 427]
**1.2 PF**
- When the ECAM asks for the procedure, keep the ECAM displayed and do the QRH procedure [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 431]
**1.3 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427]
- CAUTION: do not apply if at least one green triangle shows on each gear. Disregard any possible GPWS "TOO LOW GEAR" aural alert [QRH 24.02A, PDF 216; FCTM PR-AEP-LG P 1/4, PDF 442]

### 2. Recycle first, after L/G GEAR NOT DOWNLOCKED
**2.1 PM**
- **If L/G GEAR NOT DOWNLOCKED alert was displayed and IF TIME PERMITS** [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
  - L/G lever …… UP [QRH 24.02A, PDF 216]
  - WAIT L/G UPLOCKED [QRH 24.02A, PDF 216]
  - L/G lever …… DOWN [QRH 24.02A, PDF 216]
  - WAIT AT LEAST 60 s [QRH 24.02A, PDF 216]
  - **If unsuccessful** [QRH 24.02A, PDF 216]
    - REPEAT UP TO THREE TIMES [QRH 24.02A, PDF 216]
    - **If unsuccessful after 4 attempts** [QRH 24.02A, PDF 216]
      - WAIT AT LEAST 120 s [QRH 24.02A, PDF 216]
      - Continue with the handcrank [QRH 24.02A, PDF 216]

### 3. Gravity extension
**3.1 PM**
- GRAVITY GEAR EXTN handcrank …… PULL AND TURN [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- Rotate the handle clockwise 3 turns until reaching the mechanical stop, even if resistance is felt [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- L/G lever …… DOWN [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- Extinguishes the UNLK lights, avoids the L/G CTL message and minimizes the risk of retraction on the ground [FCOM PRO-ABN-LG P 7/30, PDF 3772]
- GEAR DOWN indications (if available) …… CHECK [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- Three green downlock arrows not lit may mean the handcrank did not reach the mechanical stop: check it is firmly against the stop [FCOM PRO-ABN-LG P 8/30, PDF 3773]
- L/G LGCIU 2 FAULT or BRAKES SYS 1(2) FAULT may trigger spuriously after a gravity extension [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
- **If successful** [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
  - DO NOT RESET GRAVITY GEAR EXTN handcrank [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
- **If unsuccessful** [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
  - LDG WITH ABNORMAL L/G PROC …… APPLY [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
- “L/G GRAVITY EXTENSION PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]
**3.2 PF**
- In a dual hydraulic failure, control reverts to direct law at gear extension (see the HYD briefs) [FCOM PRO-ABN-HYD P 53/76, PDF 3742; FCOM PRO-ABN-HYD P 65/76, PDF 3754]

## 4. Procedure
### L/G GRAVITY EXTENSION (QRH 24.02A / FCOM PRO-ABN-LG)
- **CAUTION** Do not apply this procedure if at least one green triangle is displayed on each landing gear on the WHEEL SD page. Disregard any possible GPWS "TOO LOW GEAR" aural alert. [QRH 24.02A, PDF 216]
- **If L/G GEAR NOT DOWNLOCKED alert was displayed and IF TIME PERMITS:** [QRH 24.02A, PDF 216]
  - L/G lever …… UP [QRH 24.02A, PDF 216]
  - *WAIT L/G UPLOCKED* [QRH 24.02A, PDF 216]
  - L/G lever …… DOWN [QRH 24.02A, PDF 216]
  - *WAIT AT LEAST 60 s* [QRH 24.02A, PDF 216]
  - **If unsuccessful:** [QRH 24.02A, PDF 216]
    - *REPEAT UP TO THREE TIMES* [QRH 24.02A, PDF 216]
    - **If unsuccessful after 4 attempts:** [QRH 24.02A, PDF 216]
      - *WAIT AT LEAST 120 s* [QRH 24.02A, PDF 216]
      - GRAVITY GEAR EXTN handcrank …… PULL AND TURN — Rotate the handle clockwise 3 turns until reaching the mechanical stop, even if resistance is felt. [QRH 24.02A, PDF 216]
      - L/G lever …… DOWN [QRH 24.02A, PDF 216]
      - GEAR DOWN indications (if available) …… CHECK [QRH 24.02A, PDF 216]
      - *The L/G LGCIU 2 FAULT or BRAKES SYS 1(2) FAULT alert may be spuriously triggered after a gravity extension.* [QRH 24.02A, PDF 216]
      - **If successful:** [QRH 24.02A, PDF 216]
        - *DO NOT RESET GRAVITY GEAR EXTN handcrank* [QRH 24.02A, PDF 216]
      - **If unsuccessful:** [QRH 24.02A, PDF 216]
        - LDG WITH ABNORMAL L/G PROC …… APPLY [QRH 24.02A, PDF 216]
      - **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to OPS Fuel Penalty Factors/ECAM Alert Table. [QRH 24.02A, PDF 216]
- **In all other cases:** [QRH 24.02A, PDF 216]
  - GRAVITY GEAR EXTN handcrank …… PULL AND TURN [QRH 24.02A, PDF 216]
  - L/G lever …… DOWN [QRH 24.02A, PDF 216]
  - GEAR DOWN indications (if available) …… CHECK [QRH 24.02A, PDF 216]
  - **If successful:** [QRH 24.02A, PDF 216]
    - *DO NOT RESET GRAVITY GEAR EXTN handcrank* [QRH 24.02A, PDF 216]
  - **If unsuccessful:** [QRH 24.02A, PDF 216]
    - LDG WITH ABNORMAL L/G PROC …… APPLY [QRH 24.02A, PDF 216]

## 7. FCTM technique
- Check for the green indications on the WHEEL SD page first: at least one green triangle on each gear, with the LDG GEAR DN memo, confirms the gear is downlocked. [FCTM PR-AEP-LG P 1/4, PDF 442]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| L/G GEAR NOT DOWNLOCKED | The ECAM that leads to the recycle branch | See the GEAR NOT DOWNLOCKED brief | [FCOM PRO-ABN-LG P 7/30, PDF 3772] |
| HYD G+B SYS LO PR | L/G GRVTY PROC when SPD 200 KT | See the HYD G+B brief | [FCOM PRO-ABN-HYD P 53/76, PDF 3742] |
| HYD G+Y SYS LO PR | L/G GRVTY PROC when CONF 3 and VAPP | See the HYD G+Y brief | [FCOM PRO-ABN-HYD P 64/76, PDF 3753] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- FCOM calls the do-not-reset line DO NOT RESET LDG GEAR GRVTY EXTN; the QRH calls it DO NOT RESET GRAVITY GEAR EXTN handcrank. The QRH wording is used. [FCOM PRO-ABN-LG P 8/30, PDF 3773; QRH 24.02A, PDF 216]
- The manuals do not say who turns the handcrank; the PM is shown from instructor practice. In the dual hydraulic summaries the lines are in the APPROACH section. [PDP Management of abnormal operations, PDF 427; QRH 23.02A, PDF 210; QRH 23.03A, PDF 212]
- The landing after an unsuccessful extension is [QRH] Landing with Abnormal L/G, which is not covered here. [QRH 24.02A, PDF 216]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| QRH | 24.02 — L/G gravity extension; OPS.04 — fuel penalty factors | 24.02A–B · OPS.04D, F | 216–217, 276, 278 | 26 MAY 26, 14 JUL 26 |
| FCOM | PRO-ABN-LG — [QRH] L/G GRAVITY EXTENSION | P 7–8/30 | 3772–3773 | 26 MAY 26 |
| FCTM | PR-AEP-LG | P 1/4 | 442 | 26 MAY 26 |
| PDP | Management of abnormal operations | — | 427, 431 |  |
