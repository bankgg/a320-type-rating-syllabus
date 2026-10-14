# ENG 1(2) START FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for HS-TXA..TXU (Ident PRO-ABN-ENG-AD-00017995.0002001).

A hot start shows as ENG 1(2) START FAULT with EGT OVERLIMIT: EGT goes above 635 °C during the start. In an automatic start on ground the FADEC aborts the start and dry-cranks the engine by itself; the crew waits for the dry crank to finish, sets the ENG MASTER to OFF and, after the starter cools, does a manual start or reports a no-start to maintenance.

## 1. What it is
- **Trigger:** Start fault due to no light up, engine stall, engine overtemperature, hung start, no N1 rotation, low start air pressure, or thrust lever not at idle. [FCOM PRO-ABN-ENG P 186/226, PDF 3433]
- **Flight phase inhibition:** phases 3, 4, 5, 6, 7, 8, 9 [FCOM PRO-ABN-ENG P 186/226, PDF 3433]
- During engine start the ENG EGT OVER LIMIT alert is inhibited; if EGT goes above 635 °C the ENG 1(2) START FAULT [EGT OVERLIMIT] alert triggers instead. [FCOM PRO-ABN-ENG P 127/226, PDF 3374]
- The FADEC detects hot start, hung start, stall, failed light-up, low start air pressure and thrust lever not at idle; on ground with N2 below 50 % it closes the HP valve and start valve, turns off ignition and runs a 30 s dry crank to remove fuel vapours. [FCOM DSC-70-80-40 P 2/8, PDF 2735]
- With residual EGT above 250 °C at start, an auto-crank function motors the engine until EGT is below 250 °C, with no crew message (very hot conditions or turn-arounds under 20 min). [FCOM DSC-70-80-40 P 2/8, PDF 2735]
- Alert partly inhibited: phase 3 for no light-up, stall, overtemperature, hung start or low air pressure; phase 6 for thrust lever not at idle; phase 9 for no N1 rotation; fully inhibited in phases 4, 5, 7 and 8. [FCOM PRO-ABN-ENG P 186/226, PDF 3433]

## 2. Key limits
- **EGT limit · starting:** 635 °C [FCOM LIM-ENG P 1/8, PDF 4702]
- **Pause between start cycles (ground):** 15 s [FCOM LIM-ENG P 3/8, PDF 4704]
- **Starter cooling:** 30 min after 3 failed cycles, 4 min continuous or 5 min cumulated crank [FCOM LIM-ENG P 3/8, PDF 4704]
- **Dry crank (to clear fuel vapours):** 30 s minimum [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402; FCOM PRO-ABN-ENG P 188/226, PDF 3435]
- **Manual start: ENG MASTER ON:** N2 ≥ 16 % (max motoring) and 30 s after MAN START ON [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
- **Manual start max cycle:** 2 min [FCOM LIM-ENG P 3/8, PDF 4704]

## 3. Flow (PF / PM)
### 1. Automatic start (normal SOP)
**1.1 PF**
- “ENGINE 1 START” [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]
- THRUST levers …… IDLE [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]
- ENG MODE selector …… IGN/START [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]
- ENG 1 MASTER lever …… ON [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]
- Master ON only after the amber crosses (except N1 and N2) and messages have gone [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]
**1.2 PF + PM**
- Watch the start: FF increases 30 s after master ON; EGT rises and N1 rises before 34 % N2 within 20 s of fuel on; igniters off at 43 % N2 [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]
- An impending hot or hung start may be recovered by the FADEC without ECAM: dual ignition and fuel off then on within 0.5 s — no need to shut down [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]

### 2. Detection
**2.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**2.2 PM**
- “ENG 1 START FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424; FCOM PRO-ABN-ENG P 187/226, PDF 3434]
- Confirm on the EWD and ENG SD page: EGT OVERLIMIT is the hot-start case (EGT above 635 °C during start) [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-ENG P 127/226, PDF 3374; FCOM PRO-ABN-ENG P 187/226, PDF 3434]
**2.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]

### 3. ECAM actions — on ground, auto start
**3.1 PF + PM**
- The FADEC has already shut off fuel and ignition and starts an automatic dry crank; ECAM shows AUTO CRANK IN PROGRESS [FCOM PRO-ABN-ENG P 187/226, PDF 3434; FCOM DSC-70-80-40 P 2/8, PDF 2735]
**3.2 PM**
- AUTO CRANK IN PROGRESS …… (wait) [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
- **When dry crank process is completed** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
  - ENG MASTER (AFFECTED) …… OFF [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
  - Setting the master OFF confirms the automatic start abort [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
- On ground the ENG MASTER crosscheck (CONFIRM?/CONFIRMED) is not required [PDP Management of abnormal operations, PDF 432]
**3.3 PM**
- “CLEAR ENG ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.4 PF**
- “CLEAR ENG” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.5 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 4. Decide
**4.1 PF**
- After the starter cools, either do a manual start or report the “no start condition” to maintenance [FCOM PRO-ABN-ENG P 187/226, PDF 3434; FCOM PRO-NOR-SUP-ENG P 1/18, PDF 4386]
- Manual start is recommended after a start aborted for stall, EGT overlimit, LO START AIR PRESS, no N1 rotation or hung start [FCOM PRO-NOR-SUP-ENG P 1/18, PDF 4386]
- Respect the starter limits: 15 s between cycles; 30 min cooling after 3 failed cycles [FCOM LIM-ENG P 3/8, PDF 4704]

### 5. Manual start (SUP) — next attempt
**5.1 PF + PM**
- Read the whole procedure first; then the PM reads and the PF acts on the controls [FCTM AOP-20 P 1/10, PDF 68]
**5.2 PF**
- THR LEVERS …… IDLE [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
- ENG MODE sel …… NORM THEN IGN/START [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
- **When all engine parameters (except N1 and N2) are available** [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - ENG MAN START pb-sw …… ON [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - START VALVE …… CHECK IN-LINE [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - N2 INCREASE …… CHECK [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - OIL PRESS INCREASE …… CHECK [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
- **When N2 reaches max motoring (16 % minimum) and 30 s after MAN START ON** [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
  - ENG MASTER …… ON [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
**5.3 PM**
- CHRONO …… START [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
- Times the light-up [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
- IGNITERS A AND B …… CHECK ON [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
- FUEL FLOW INCREASE …… CHECK [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]
**5.4 PF + PM**
- **20 s maximum after fuel flow increase** [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
  - EGT INCREASE …… CHECK [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
  - N1 INCREASE (before 34 % N2) …… CHECK [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
- **When N2 reaches 43 %** [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
  - IGNITERS A AND B (at 43 % N2) …… CHECK OFF [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
  - START VALVE (slightly above 43 % N2) …… CHECK CROSS LINE [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
  - MAIN / SECONDARY ENG PARAMETERS …… CHECK NORMAL [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
**5.5 PF**
- ENG MAN START pb-sw …… OFF [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
- ENG MODE sel …… NORM [FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393]
- **If a start malfunction is suspected or an engine ECAM alert triggers** [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - Before master ON: ENG MAN START pb-sw OFF [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - After master ON: ENG MASTER OFF, then ENG MAN START pb-sw OFF; consider a dry crank before another attempt [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]
  - “ECAM ACTIONS” [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-ENG)
- **ENG 1(2) IGNITION FAULT:** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
  - *The engine does not start within the 20 s (30 s in flight) that follow the ignition start.* [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
- **NO N1 ROTATION: or STALL or EGT OVERLIMIT or HUNG START:** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
  - **In flight:** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - ENG MASTER (AFFECTED) …… OFF — Wait 30 s before attempting a new start (to drain the engine). [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
  - **On ground (auto start):** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - *If the engine does not start or in case of detected stall, potential EGT overheat or hung start, the FADEC will immediately shut off fuel and turn off ignition. After any start attempt that is not successful, a dry crank automatically occurs. At the end of the dry crank sequence, the start valve is closed.* [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - *AUTO CRANK IN PROGRESS.* [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - **When dry crank process is completed:** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
      - ENG MASTER (AFFECTED) …… OFF — Confirms automatic start abort. After the starter cools, for any subsequent attempt the crew must perform a manual start, or must report the “no start condition” to maintenance. [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
      - *With engine above idle, if EGT limit is exceeded ECAM requires to set engine master lever at OFF.* [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
  - **On ground (manual start):** [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - ENG MASTER (AFFECTED) …… OFF [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - MAN START (AFFECTED) …… OFF [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - MODE SEL …… CRANK [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - MAN START (AFFECTED) …… ON [FCOM PRO-ABN-ENG P 187/226, PDF 3434]
    - *ECAM does not display the last two lines. Dry crank the engine for 30 s. The start valve automatically reopens when N2 is below 10 %. After the starter cools: manual start, or report the “no start condition” to maintenance.* [FCOM PRO-ABN-ENG P 188/226, PDF 3435]
- **LO START AIR PRESS:** [FCOM PRO-ABN-ENG P 188/226, PDF 3435]
  - BLEED AIR SUPPLY …… CHECK [FCOM PRO-ABN-ENG P 188/226, PDF 3435]
- **THR LEVER NOT AT IDLE:** [FCOM PRO-ABN-ENG P 188/226, PDF 3435]
  - THR LEVER …… IDLE [FCOM PRO-ABN-ENG P 188/226, PDF 3435]

### ENGINE VENTILATION (DRY CRANKING) (FCOM PRO-NOR-SUP-ENG)
- *On ground, after an unsuccessful manual start, or an unsuccessful automatic start not followed by an automatic dry crank.* [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
- **Before dry crank:** [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MASTER (affected engine) …… CHECK OFF [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MODE sel …… CHECK NORM [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MAN START pb-sw (affected engine) …… CHECK OFF [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
- **Dry crank:** [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MODE sel …… CRANK [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MAN START pb-sw (affected engine) …… ON [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - *To clear fuel vapors, a 30 seconds dry crank cycle is the minimum required.* [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
- **When the dry crank is completed:** [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MAN START pb-sw (affected engine) …… OFF [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]
  - ENG MODE sel …… NORM [FCOM PRO-NOR-SUP-ENG P 17/18, PDF 4402]

## 7. FCTM technique
- Engine-start supplementary procedures: read the entire procedure first, then the PM reads the actions and the PF acts on the controls. [FCTM AOP-20 P 1/10, PDF 68]
- Manual start is recommended after a start aborted for stall, EGT overlimit, LO START AIR PRESS, no N1 rotation or hung start, and when an abort is expected (hot or high airfields, reduced EGT margin, weak ground air, tailwind above 10 kt). [FCOM PRO-NOR-SUP-ENG P 1/18, PDF 4386]
- In hot weather (OAT ≥ 40 °C) with residual EGT above 100 °C, dry crank 2 min before a manual start; starting with residual EGT above 250 °C is not recommended. [FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| MANUAL ENGINE START (SUP) | Next start attempt after the auto start abort | THR LEVERS IDLE; MODE IGN/START, MAN START ON; ENG MASTER ON at N2 ≥ 16 % and 30 s; CHRONO, check light-up within 20 s; At 43 % N2: MAN START OFF, MODE NORM | [FCOM PRO-NOR-SUP-ENG P 6/18, PDF 4391; FCOM PRO-NOR-SUP-ENG P 7/18, PDF 4392; FCOM PRO-NOR-SUP-ENG P 8/18, PDF 4393] |
| [QRH] ENGINE TAILPIPE FIRE | Internal fire can occur at start; EGT does not decrease after master OFF, or ground crew reports it | ENG MASTER OFF; Do not press the ENG FIRE pb (FADEC power needed for motoring); Air bleed press established, BEACON ON; MODE CRANK, MAN START ON until fire stopped | [FCOM PRO-ABN-ENG P 29/226, PDF 3276; QRH 19.08A, PDF 179; FCTM PR-AEP-ENG P 21/26, PDF 422; FCTM PR-AEP-ENG P 22/26, PDF 423] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The HS-TX procedure has no separate HOT START heading (it exists only in the HS-TO variant, not used); a hot start appears as EGT OVERLIMIT. [FCOM PRO-ABN-ENG P 127/226, PDF 3374; FCOM PRO-ABN-ENG P 192/226, PDF 3439]
- No FCTM technique or PDP slide covers the start-fault handling itself; the PF/PM split for the ECAM part follows the general AOP-20/AOP-30-30 rules. [FCTM AOP-20 P 1–2/10, PDF 68; FCTM AOP-30-30 P 2/6, PDF 83]
- The SOP says “ENGINE 1 START” for engine 1; use the engine being started. [FCOM PRO-NOR-SOP-08 P 1/6, PDF 4136]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ENG — ENG 1(2) START FAULT | P 186–188/226 | 3433–3435 | 26 MAY 26 |
| FCOM | PRO-ABN-ENG — ENG N1/N2/EGT OVER LIMIT (note 2) | P 127/226 | 3374 | 26 MAY 26 |
| FCOM | PRO-NOR-SOP-08 — Automatic engine start | P 1–2/6 | 4136–4137 | 18 FEB 26 |
| FCOM | PRO-NOR-SUP-ENG — Manual start, dry cranking | P 1, 6–8, 17/18 | 4386, 4391–4393, 4402 | 26 MAY 26 |
| FCOM | LIM-ENG — EGT, starter | P 1, 3/8 | 4702, 4704 | 26 MAY 26 |
| FCOM | DSC-70-80-40 — Engine starting system | P 2/8 | 2735 | 18 FEB 26 |
| FCTM | AOP-20 — Supplementary procedures task sharing | P 1/10 | 68 | 26 MAY 26 |
| FCTM | PR-AEP-ENG — Engine tailpipe fire | P 21–22/26 | 422–423 | 26 MAY 26 |
