# L/G GEAR NOT DOWNLOCKED — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Red warning · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL (ECAM, QRH and FCTM).

A red warning on approach: one gear did not lock down 30 s after the lever went down. Fly first (the approach may be discontinued). Then the PM recycles the gear (lever up, wait for uplock and doors closed, lever down). If it is still not locked after 120 s, do the QRH L/G GRAVITY EXTENSION. If that fails, do LANDING WITH ABNORMAL L/G. One green triangle on each gear is enough to confirm the gear is down.

## 1. What it is
- **Trigger:** One gear is not downlocked and L/G is selected down (landing gear sequence not completed after 30 s). [FCOM PRO-ABN-LG P 12/30, PDF 3777; FCOM PRO-ABN-LG P 13/30, PDF 3778]
- **Flight phase inhibition:** phases 3, 4, 5, 8 [FCOM PRO-ABN-LG P 12/30, PDF 3777; FCOM PRO-ABN-LG P 13/30, PDF 3778]
- Lever DOWN after gravity extension extinguishes the UNLK lights, avoids the L/G CTL message and minimises the risk of gear retraction on the ground. [FCOM PRO-ABN-LG P 7/30, PDF 3772]
- If both LGCIUs failed, ECAM gear indications are lost; the LDG GEAR panel lights stay if LGCIU 1 is powered. No three green arrows may mean the handcrank is not at its stop. [FCOM PRO-ABN-LG P 8/30, PDF 3773]
- Do not reset the free-fall system after a successful gravity extension (fluid loss, possible gear unlock); it may be reset on training flights. [FCOM PRO-ABN-LG P 8/30, PDF 3773]

## 2. Key limits
- **Warning:** gear sequence not complete after 30 s [FCOM PRO-ABN-LG P 13/30, PDF 3778]
- **Recycle (QRH):** up to 4 attempts, wait ≥ 60 s each [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- **Before gravity extension:** wait ≥ 120 s [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 13/30, PDF 3778]
- **Gravity handcrank:** 3 turns clockwise to the mechanical stop [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
- **Gear downlocked:** ≥ 1 green triangle per gear (WHEEL SD) [QRH 24.02A, PDF 216; FCTM PR-AEP-LG P 1/4, PDF 442]

## 3. Flow (PF / PM)
### 1. Recognise · fly first
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “L/G GEAR NOT DOWNLOCKED” [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- Check the WHEEL SD page and the LDG GEAR indicator: at least one green triangle on each gear plus the LDG GEAR DN memo means the gear is down and locked [FCTM PR-AEP-LG P 1/4, PDF 442; QRH 24.02A, PDF 216]
**1.3 PF**
- Maintain a safe flight path; discontinue the approach (go-around / level off) if needed before the ECAM [FCTM AOP-30-30 P 1/6, PDF 82; FCTM AOP-40 P 1/4, PDF 96]
- Configuration changes need both pilots: STOP ECAM … CONTINUE ECAM around them [PDP Management of abnormal operations, PDF 430; FCTM AOP-30-30 P 3/6, PDF 84]
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]

### 2. ECAM: recycle
**2.1 PM**
- L/G …… RECYCLE [FCOM PRO-ABN-LG P 13/30, PDF 3778]
- Lever UP → wait for uplock and doors closed (watch WHEEL SD) → lever DOWN [FCOM PRO-ABN-LG P 13/30, PDF 3778]
- The active LGCIU changes when the gear is recycled [FCOM PRO-ABN-LG P 13/30, PDF 3778]
**2.2 PF + PM**
- **If unsuccessful after 120 s** [FCOM PRO-ABN-LG P 13/30, PDF 3778]
  - L/G GRVTY PROC …… APPLY [FCOM PRO-ABN-LG P 13/30, PDF 3778]
  - Keep the ECAM displayed and do the QRH procedure [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 431]

### 3. QRH L/G GRAVITY EXTENSION
**3.1 PF**
- “L/G GRAVITY EXTENSION PROCEDURE” [PDP Management of abnormal operations, PDF 427; PDP Management of abnormal operations, PDF 431]
**3.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427]
- CAUTION: do not apply if at least one green triangle shows on each gear [QRH 24.02A, PDF 216]
- **L/G GEAR NOT DOWNLOCKED displayed and IF TIME PERMITS** [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
  - L/G lever …… UP [QRH 24.02A, PDF 216]
  - WAIT L/G UPLOCKED [QRH 24.02A, PDF 216]
  - L/G lever …… DOWN [QRH 24.02A, PDF 216]
  - WAIT AT LEAST 60 s [QRH 24.02A, PDF 216]
  - **If unsuccessful** [QRH 24.02A, PDF 216]
    - REPEAT UP TO THREE TIMES [QRH 24.02A, PDF 216]
    - **If unsuccessful after 4 attempts** [QRH 24.02A, PDF 216]
      - WAIT AT LEAST 120 s [QRH 24.02A, PDF 216]
      - GRAVITY GEAR EXTN handcrank …… PULL AND TURN [QRH 24.02A, PDF 216]
- **After GRAVITY GEAR EXTN handcrank PULL AND TURN (after 4 failed recycles, or in all other cases)** [QRH 24.02A, PDF 216]
  - Handcrank: 3 turns clockwise to the mechanical stop, even if resistance is felt [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 7/30, PDF 3772]
  - L/G lever …… DOWN [QRH 24.02A, PDF 216]
  - GEAR DOWN indications (if available) …… CHECK [QRH 24.02A, PDF 216]
  - L/G LGCIU 2 FAULT or BRAKES SYS 1(2) FAULT may trigger spuriously after a gravity extension [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
  - **If successful** [QRH 24.02A, PDF 216]
    - DO NOT RESET GRAVITY GEAR EXTN handcrank [QRH 24.02A, PDF 216; FCOM PRO-ABN-LG P 8/30, PDF 3773]
  - **If unsuccessful** [QRH 24.02A, PDF 216]
    - LDG WITH ABNORMAL L/G PROC …… APPLY [QRH 24.02A, PDF 216]
- “L/G GRAVITY EXTENSION PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

### 4. Continue ECAM · STATUS
**4.1 PM**
- “CLEAR L/G ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.2 PF**
- “CLEAR L/G” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- STATUS: L/G GRVTY EXTN; flight with gear down increases fuel burn (QRH OPS fuel penalty) [FCOM PRO-ABN-LG P 13/30, PDF 3778]
**4.4 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]
**4.5 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]
**4.6 PF**
- Assess fuel with gear down, decide, inform ATC / cabin [PDP Management of abnormal operations, PDF 428; FCOM PRO-ABN-LG P 13/30, PDF 3778]

### 5. Warning disappears during the procedure
**5.1 PF + PM**
- If the warning disappears during the procedure it is no longer applicable and the procedure can be stopped [FCTM AOP-30-30 P 4/6, PDF 85]
- Confirm three gear down and locked (green triangles, LDG GEAR DN memo) before the next approach [FCTM PR-AEP-LG P 1/4, PDF 442]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-LG)
- *This warning appears if the landing gear sequence is not completed after 30 s.* [FCOM PRO-ABN-LG P 13/30, PDF 3778]
- L/G …… RECYCLE — Lever up; wait for uplock and doors closed (monitor WHEEL SD); lever down. The active LGCIU changes. [FCOM PRO-ABN-LG P 13/30, PDF 3778]
- **IF UNSUCCESSFUL AFTER 120 s:** [FCOM PRO-ABN-LG P 13/30, PDF 3778]
  - L/G GRVTY PROC …… APPLY — Rotate the handle clockwise about 3 turns until reaching the mechanical stop. [FCOM PRO-ABN-LG P 13/30, PDF 3778]
  - **CAUTION** For flight with L/G extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-LG P 13/30, PDF 3778]

### [QRH] L/G GRAVITY EXTENSION (QRH 24.02A / FCOM PRO-ABN-LG)
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

## 5. STATUS
**Limitations**
- For flight with L/G extended, fuel consumption is increased (QRH/OPS Fuel Penalty Factors/ECAM Alert Table). [FCOM PRO-ABN-LG P 13/30, PDF 3778]
**Information**
- If gravity extension unsuccessful, refer to [QRH] Landing with Abnormal L/G. [FCOM PRO-ABN-LG P 13/30, PDF 3778]
**APPR PROC**
- L/G …… GRVTY EXTN [FCOM PRO-ABN-LG P 13/30, PDF 3778]

## 7. FCTM technique
- Check the WHEEL SD page and the LDG GEAR DN memo before any gravity extension or abnormal-gear landing: one green triangle on each gear is enough. [FCTM PR-AEP-LG P 1/4, PDF 442]
- Landing with abnormal gear: land on any available gear rather than none; reduce weight; no ground spoilers or autobrake with a main gear abnormal; anti-skid off. [FCTM PR-AEP-LG P 1/4, PDF 442]
- ENG masters OFF: nose gear abnormal — before nose impact; one main — at touchdown; both mains — in the flare. Fire pbs pushed when the aircraft has stopped. [FCTM PR-AEP-LG P 2/4, PDF 443]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] LANDING WITH ABNORMAL L/G | Gravity extension unsuccessful | Cabin crew, ATC NOTIFY; consider fuel reduction; LDG DIST up to +70 %; For approach: GPWS SYS OFF, handcrank back to normal, no autobrake, A/SKID & N/W STRG OFF, MAX BRAKE PR 1 000 PSI; At 500 ft AGL: BRACE FOR IMPACT ORDER; no reverse; ENG masters OFF per gear case; stopped: PARK BRK ON, all FIRE pb PUSH, AGENTS DISCH, evacuation as required | [QRH 24.01A, PDF 214; QRH 24.01B, PDF 215] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The ECAM says apply gravity extension if unsuccessful after 120 s; the QRH first allows up to 4 recycles (60 s each) if time permits, then 120 s. They are consistent — the QRH is the detailed version. [FCOM PRO-ABN-LG P 13/30, PDF 3778; QRH 24.02A, PDF 216]
- No PDP module and no FCTM text covers this warning or who turns the gravity handcrank; PF/PM split follows the general AOP-20/AOP-30 rules. [FCTM AOP-20 P 1–2/10, PDF 68; FCTM PR-AEP-LG P 1/4, PDF 442]
- Discontinued approach technique is outside this brief (recovery manoeuvre). [FCTM AOP-30-30 P 1/6, PDF 82]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-LG — L/G GEAR NOT DOWNLOCKED; [QRH] L/G GRAVITY EXTENSION | P 7–8, 12–13/30 | 3772–3773, 3777–3778 | 26 MAY 26 |
| QRH | 24 — Landing with abnormal L/G; L/G gravity extension | 24.01A–24.02B | 214–217 | 26 MAY 26 |
| FCTM | PR-AEP-LG — Landing with abnormal L/G | P 1–2/4 | 442–443 | 26 MAY 26 |
