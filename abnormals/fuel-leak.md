# FUEL LEAK — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**QRH procedure · amber LAND ASAP · no memory items**  
**Applicability:** HS-TXA..TXO, HS-TXP..TXU — The center tank lines differ: CTR TK PUMP 1 and 2 on HS-TXA..TXO, CTR TK L and R XFR on HS-TXP..TXU.

When a leak is confirmed: amber LAND ASAP. If the leak is confirmed from an engine or pylon, shut that engine down and do not restart it. If not, keep the crossfeed closed, stop the center tank feed and watch the inner tanks. One tank depleting faster by at least 300 kg in less than 30 min: shut down that engine to tell an engine leak from a wing leak. Both depleting alike: suspect the center tank or APU feed line. Do not use the reversers for landing.

## 1. What it is
- **Trigger:** FOB + FU significantly less than FOB at engine start or decreasing; fuel spray seen from an engine, pylon or wingtip/sharklet; total fuel decreasing abnormally; a developing imbalance; a tank decreasing too fast; excessive fuel flow with low N1; fuel smell in the cabin; destination EFOB amber or "DEST EFOB BELOW MIN"; depending on the FWC standard, the FUEL F.USED/FOB DISAGREE alert. [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611; FCTM PR-AEP-FUEL P 4/4, PDF 437]
- **Flight phase inhibition:** none [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611; FCTM PR-AEP-FUEL P 4/4, PDF 437]
- A fuel leak may be detected if the FOB + FU is significantly less than the FOB at engine start or decreasing, a passenger observes fuel spray, the total fuel decreases at an abnormal rate, an imbalance develops, a tank decreases too fast, fuel flow is excessive with low N1, fuel is smelt in the cabin, or the destination EFOB turns amber or "DEST EFOB BELOW MIN" appears. [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611]
- **[HS-TXP..TXU]** On HS-TXP..TXU a tank overflowing (pipe rupture in a tank) is also listed as a way to detect a leak. [FCOM PRO-ABN-FUEL P 6/76, PDF 3611]
- APU OFF for a fuel smell in the cabin prevents additional fuel loss through the APU feeding line. [FCOM PRO-ABN-FUEL P 5/76, PDF 3610; FCOM PRO-ABN-FUEL P 7/76, PDF 3612]

## 2. Key limits
- **Landing:** LAND ASAP (amber) [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **Asymmetric depletion:** ≥ 300 kg in less than 30 min [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **Center tank feed restored:** Inner tank below 3 000 kg [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
- **Reversers:** Do not use for landing; not available for landing performance [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202; FCTM PR-AEP-FUEL P 3/4, PDF 436]
- **Fuel checks:** Each waypoint or at least every 30 min [FCTM PR-AEP-FUEL P 1/4, PDF 434]

## 3. Flow (PF / PM)
### 1. Detect
**1.1 PF + PM**
- Fuel checks at each waypoint or at least every 30 min; investigate any difference without delay [FCTM PR-AEP-FUEL P 1/4, PDF 434]
- If visibility permits, identify the leak source by a visual check from the cabin [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611]
- Consider a fuel leak for any message or alert on fuel quantity or imbalance [FCTM PR-AEP-FUEL P 1/4, PDF 434]
- Depending on the FWC standard, the FUEL F.USED/FOB DISAGREE alert may address both cases of fuel leak and fuel over read [FCTM PR-AEP-FUEL P 4/4, PDF 437]

### 2. Order
**2.1 PF**
- “FUEL LEAK PROCEDURE” [PDP Management of abnormal operations, PDF 427]
- PF flies, navigates and communicates. Amber LAND ASAP: consider landing at the nearest suitable airport [FCTM AOP-20 P 1–2/10, PDF 68; FCTM AOP-30-10 P 2/2, PDF 79; QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
**2.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427; FCTM AOP-30-30 P 5/6, PDF 86]

### 3. Leak from engine/pylon confirmed
**3.1 PF + PM**
- Confirmed by excessive fuel flow, low N1, or visual check [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
**3.2 PM**
- THR LEVER (affected engine) …… IDLE [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
**3.3 PF**
- Moves it to IDLE after the PM confirms the lever [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**3.4 PM**
- “ENGINE MASTER 1 OFF — CONFIRM?” [PDP Management of abnormal operations, PDF 432; QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
**3.5 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**3.6 PM**
- ENG MASTER (affected engine) …… OFF [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- FUEL X FEED …… AS RQRD [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- If the leak stops, the crossfeed can be opened to re-balance fuel or use fuel from both wings [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611]
- DO NOT RESTART AFFECTED ENGINE [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]

### 4. Leak not confirmed or not located
**4.1 PM**
- FUEL X FEED …… MAINTAIN CLOSED [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- Stops the leak from affecting both sides [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611]
- **[HS-TXA..TXO]** CTR TK PUMP 1 …… OFF [QRH 21.06A, PDF 199]
- **[HS-TXA..TXO]** CTR TK PUMP 2 …… OFF [QRH 21.06A, PDF 199]
- **[HS-TXP..TXU]** CTR TK L XFR …… OFF [QRH 21.06C, PDF 201]
- **[HS-TXP..TXU]** CTR TK R XFR …… OFF [QRH 21.06C, PDF 201]
- INNER TANK FUEL QUANTITIES …… MONITOR [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- Each engine is now fed by its own inner tank only: monitor the depletion rate of each [FCOM PRO-ABN-FUEL P 4/76, PDF 3609; FCOM PRO-ABN-FUEL P 6/76, PDF 3611; FCOM PRO-ABN-FUEL P 7/76, PDF 3612]

### 5. One inner tank depletes faster (≥ 300 kg in < 30 min)
**5.1 PM**
- THR LEVER (engine on leaking side) …… IDLE [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
**5.2 PF**
- Moves it to IDLE after the PM confirms the lever [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**5.3 PM**
- “ENGINE MASTER 1 OFF — CONFIRM?” [PDP Management of abnormal operations, PDF 432; QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
**5.4 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**5.5 PM**
- ENG MASTER (engine on leaking side) …… OFF [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **[HS-TXA..TXO]** CTR TK PUMP 1 …… ON [QRH 21.06A, PDF 199]
- **[HS-TXA..TXO]** CTR TK PUMP 2 …… ON [QRH 21.06A, PDF 199]
- FUEL LEAK …… MONITOR [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **If leak stops: ENGINE LEAK CONFIRMED** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - **[HS-TXP..TXU]** CTR TK L XFR …… ON [QRH 21.06C, PDF 201]
  - **[HS-TXP..TXU]** CTR TK R XFR …… ON [QRH 21.06C, PDF 201]
  - FUEL X FEED …… AS RQRD [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - DO NOT RESTART AFFECTED ENGINE [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **If leak continues (after engine shutdown): WING LEAK SUSPECTED** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - ENGINE RESTART …… CONSIDER [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - **[HS-TXP..TXU]** CTR TK XFR (non-leaking side) …… ON [QRH 21.06C, PDF 201]
  - Do not apply the FUEL IMBALANCE procedure. Approach and landing can be done, even with one full wing/one empty wing [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]

### 6. Both inner tanks deplete at a similar rate
**6.1 PM**
- LEAK FROM CENTER TANK OR APU FEEDING LINE SUSPECTED [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **If fuel smell in cabin** [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
  - APU …… OFF [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
- **When fuel quantity in one inner tank less than 3 000 kg (6 600 lb)** [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
  - **[HS-TXA..TXO]** CTR TK PUMP 1 …… ON [QRH 21.06A, PDF 199]
  - **[HS-TXA..TXO]** CTR TK PUMP 2 …… ON [QRH 21.06A, PDF 199]
  - **[HS-TXP..TXU]** CTR TK L XFR …… ON [QRH 21.06D, PDF 202]
  - **[HS-TXP..TXU]** CTR TK R XFR …… ON [QRH 21.06D, PDF 202]

### 7. For landing
**7.1 PF**
- DO NOT USE REVERSERS, even if they are available [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202; FCTM PR-AEP-FUEL P 3/4, PDF 436]
- Consider the thrust reversers not available when computing landing performance [FCTM PR-AEP-FUEL P 3/4, PDF 436]
**7.2 PM**
- “FUEL LEAK PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### FUEL LEAK (QRH 21.06A, 21.06C–D; FCOM PRO-ABN-FUEL P 4–7/76)
- **WHEN A LEAK IS CONFIRMED** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **LAND ASAP (amber)** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **Leak from engine/pylon confirmed by excessive fuel flow, low N1, or visual check:** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - THR LEVER (affected engine) …… IDLE [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - ENG MASTER (affected engine) …… OFF [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - FUEL X FEED …… AS RQRD [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - *DO NOT RESTART AFFECTED ENGINE* [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
- **Leak from engine/pylon not confirmed or leak not located:** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - FUEL X FEED …… MAINTAIN CLOSED [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - **[HS-TXA..TXO]** CTR TK PUMP 1 …… OFF [QRH 21.06A, PDF 199]
  - **[HS-TXA..TXO]** CTR TK PUMP 2 …… OFF [QRH 21.06A, PDF 199]
  - **[HS-TXP..TXU]** CTR TK L XFR …… OFF [QRH 21.06C, PDF 201]
  - **[HS-TXP..TXU]** CTR TK R XFR …… OFF [QRH 21.06C, PDF 201]
  - INNER TANK FUEL QUANTITIES …… MONITOR [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - **If one inner tank depletes faster than other by at least 300 kg (660 lb) in less than 30 min:** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - THR LEVER (engine on leaking side) …… IDLE [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - ENG MASTER (engine on leaking side) …… OFF [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - **[HS-TXA..TXO]** CTR TK PUMP 1 …… ON [QRH 21.06A, PDF 199]
    - **[HS-TXA..TXO]** CTR TK PUMP 2 …… ON [QRH 21.06A, PDF 199]
    - FUEL LEAK …… MONITOR [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - **If leak stops:** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
      - *ENGINE LEAK CONFIRMED* [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
      - **[HS-TXP..TXU]** CTR TK L XFR …… ON [QRH 21.06C, PDF 201]
      - **[HS-TXP..TXU]** CTR TK R XFR …… ON [QRH 21.06C, PDF 201]
      - FUEL X FEED …… AS RQRD [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
      - *DO NOT RESTART AFFECTED ENGINE* [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - **If leak continues (after engine shutdown):** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
      - *WING LEAK SUSPECTED* [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
      - ENGINE RESTART …… CONSIDER [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
      - **[HS-TXP..TXU]** CTR TK XFR (non-leaking side) …… ON [QRH 21.06C, PDF 201]
      - **CAUTION** Do not apply the FUEL IMBALANCE procedure. Approach and landing can be done, even with one full wing/one empty wing. [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
  - **If both inner tanks deplete at a similar rate:** [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - *LEAK FROM CENTER TANK OR APU FEEDING LINE SUSPECTED* [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]
    - **If fuel smell in cabin:** [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
      - APU …… OFF [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
    - **When fuel quantity in one inner tank less than 3 000 kg (6 600 lb):** [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]
      - **[HS-TXA..TXO]** CTR TK PUMP 1 …… ON [QRH 21.06A, PDF 199]
      - **[HS-TXA..TXO]** CTR TK PUMP 2 …… ON [QRH 21.06A, PDF 199]
      - **[HS-TXP..TXU]** CTR TK L XFR …… ON [QRH 21.06D, PDF 202]
      - **[HS-TXP..TXU]** CTR TK R XFR …… ON [QRH 21.06D, PDF 202]
- **For landing: DO NOT USE REVERSERS** [QRH 21.06A, PDF 199; QRH 21.06D, PDF 202]

## 6. QRH and reference tables
### Indications and probable source 
FCTM table of indications and observations.

| Indications and observations | Symmetry | Probable source |
|---|---|---|
| Fuel spray from an engine/pylon. For one engine side only: excessive fuel flow or significant N1 decrease. One wing tank decreases abnormally fast. | Asymmetric | Engine |
| Fuel spray from the wing. One wing decreases abnormally fast. | Asymmetric & symmetric | Hole in a tank |
| Sudden overflow in one of the tanks. | Asymmetric & symmetric | Hole in a pipe |
| Developing imbalance. Burnt fuel smell in the cabin. Abnormal decrease of total fuel. [FOB + FU] < BLOCK. FOB differs from the flight plan at a waypoint. Destination EFOB decreasing or amber. | Asymmetric & symmetric | Engine, hole in a tank, hole in a pipe, APU |
[FCTM PR-AEP-FUEL P 1/4, PDF 434; FCTM PR-AEP-FUEL P 2/4, PDF 435]

## 7. FCTM technique
- If the leak is confirmed from the engine or pylon, the engine is shut down to stop the leak and to prevent a fire hazard from fuel leaking onto hot engine surfaces. [FCTM PR-AEP-FUEL P 2/4, PDF 435]
- If it is not confirmed, each tank is isolated so each wing tank feeds its own engine. If one wing tank decreases faster, its engine is shut down to confirm whether the leak is from the wing tank or the engine. [FCTM PR-AEP-FUEL P 2/4, PDF 435]
- The 300 kg threshold allows for fuel system accuracy. A leak rate that is constant or increasing below it indicates a permanent asymmetric leak developing over time, and should be considered a leak from a wing or an engine. [FCTM PR-AEP-FUEL P 2/4, PDF 435]
- If both wing tanks decrease symmetrically and the center tank quantity decreases, the leak comes from the center tank or the APU feed line. [FCTM PR-AEP-FUEL P 2/4, PDF 435]
- Do not use the reversers at landing even if available: their airflow blows leaking fuel toward the engine air inlet or the brakes, which may overheat the engine or start a fire, or reduce brake performance or start a fire on hot brakes. [FCTM PR-AEP-FUEL P 3/4, PDF 436]
- If the crew detects a fuel leak before the ECAM alert is triggered, the crew can activate the QRH FUEL LEAK procedure. [FCTM PR-AEP-FUEL P 1/4, PDF 434]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG 1(2) SHUT DOWN | The QRH does not name it here. Apply it after the engine shutdown in this procedure, as confirmed by the user. | See the ENG 1(2) FAIL brief, which holds this procedure | [FCOM PRO-ABN-ENG P 169/226, PDF 3416] |
| FUEL IMBALANCE | A fuel imbalance may indicate a leak; do not apply FUEL IMBALANCE if a leak is suspected. | See the FUEL IMBALANCE brief | [QRH 21.05A, PDF 198] |
| ENG RELIGHT IN FLIGHT | ENGINE RESTART: CONSIDER if the leak continues after the engine shutdown (wing leak suspected). | See the ENG RELIGHT IN FLIGHT brief | [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201] |
| FUEL OVERREAD | The opposite indication: FOB + FU significantly more than the FOB at engine start, or increasing. | Apply the QRH FUEL OVERREAD procedure | [FCTM PR-AEP-FUEL P 4/4, PDF 437] |

## 9. HS-TX differences
| Topic | HS-TXA..TXO | HS-TXP..TXU | Ref |
|---|---|---|---|
| Center tank lines | CTR TK PUMP 1 and 2 | CTR TK L and R XFR | [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201] |
| After shutdown of the engine on the leaking side | CTR TK PUMP 1 and 2 ON immediately | CTR TK L and R XFR ON if the leak stops; CTR TK XFR (non-leaking side) ON if it continues | [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201] |

## 10. Gaps and omissions
- The QRH does not say which ECAM procedure follows the engine shutdown. The brief points to ENG 1(2) SHUT DOWN under Related procedures, confirmed by the user. HS-TO-only versions (QRH 21.06B, FCOM ENG 1(2) FUEL LEAK P 103/226) are excluded. [QRH 21.06A, PDF 199; QRH 21.06B, PDF 200; FCOM PRO-ABN-ENG P 103/226, PDF 3350]
- The FCTM mentions a FUEL F.USED/FOB DISAGREE alert "depending on the FWC standard". The HS-TX FCOM procedures do not list it. The brief shows it as a possible trigger, confirmed by the user. [FCTM PR-AEP-FUEL P 4/4, PDF 437]
- "ENGINE MASTER 1 OFF" is the PDP example of the crosscheck wording: apply it to the engine concerned. The PDP has no fuel module; the flow is the standard QRH sequence. [PDP Management of abnormal operations, PDF 432; PDP Management of abnormal operations, PDF 427]
- The manuals print a separate version for each HS-TX group. "From the manuals" merges them into one procedure, with a chip on the lines that differ, confirmed by the user. [QRH 21.06A, PDF 199; QRH 21.06C, PDF 201]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| QRH | 21.06 FUEL LEAK | 21.06A, 21.06C–D | 199, 201–202 | 18 FEB 26 |
| FCOM | PRO-ABN-FUEL — [QRH] FUEL LEAK | P 4–7/76 | 3609–3612 | 26 MAY 26 |
| FCTM | PR-AEP-FUEL — fuel leak, troubleshooting, overread | P 1–4/4 | 434–437 | 24 NOV 25 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
| FCOM | PRO-ABN-ENG — ENG 1(2) SHUT DOWN | P 169–173/226 | 3416–3420 | 26 MAY 26 |
