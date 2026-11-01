# HYD G RSVR LO LVL — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-11-01 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One procedure for all aircraft.

An amber caution: the green reservoir is low. Switch the PTU OFF without delay, because a PTU overheat may occur two minutes later and may lead to the loss of the second hydraulic circuit, then switch the green engine 1 pump OFF. The green system is lost. Plan a gravity gear extension, alternate braking and slow slats and flaps, apply the landing distance procedure and use the fuel penalty factor instead of the FMS predictions.

## 1. What it is
- **Trigger:** The fluid quantity is below 3.5 l (0.92 US Gal). Inhibited for the first 15 s of flight phase 5. [FCOM PRO-ABN-HYD P 17/76, PDF 3706]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-HYD P 17/76, PDF 3706]
- A pump driven by engine 1 pressurizes the green system. [FCOM DSC-29-10-20 P 1/6, PDF 1744]
- The bidirectional PTU comes into action automatically when the differential pressure between the green and yellow systems is greater than 500 PSI. Hydraulic fluid cannot be transferred from one system to another. [FCOM DSC-29-10-20 P 3/6, PDF 1746; FCTM PR-AEP-HYD P 1/4, PDF 438]
- Single hydraulic failures have very little effect on the handling of the aircraft but degrade the landing capability to CAT 3 SINGLE. [FCTM PR-AEP-HYD P 1/4, PDF 438]

## 2. Key limits
- **Trigger:** Fluid below 3.5 l (0.92 US Gal) [FCOM PRO-ABN-HYD P 17/76, PDF 3706]
- **PTU:** OFF without delay [FCOM PRO-ABN-HYD P 18/76, PDF 3707; FCTM PR-AEP-HYD P 1/4, PDF 438]
- **Landing gear:** L/G GRVTY PROC APPLY [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- **Braking:** ALTN Y BRK WITH A/SKID [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- **Landing capability:** CAT 3 SINGLE ONLY [FCOM PRO-ABN-HYD P 19/76, PDF 3708]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “HYD G RSVR LO LVL” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-HYD P 17/76, PDF 3706; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- PTU …… OFF [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
- Without delay: a PTU overheat may occur two minutes later and may lead to the loss of the second hydraulic circuit [FCTM PR-AEP-HYD P 1/4, PDF 438]
- GREEN ENG 1 PUMP …… OFF [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
- G ENG 1 PUMP LO PR [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
**2.2 PM**
- “CLEAR HYD ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**2.3 PF**
- “CLEAR HYD” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]

### 3. Associated procedure and SD pages
**3.1 PM**
- Associated procedure G SYS LO PR; FUEL CONSUMPT INCRSD; FMS PRED UNRELIABLE [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
**3.2 PF + PM**
- Analyze the SD pages for the secondary failures: WHEEL, F/CTL [FCOM PRO-ABN-HYD P 18/76, PDF 3707; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.3 PM**
- “CLEAR WHEEL ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.4 PF**
- “CLEAR WHEEL” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.5 PM**
- “CLEAR FLIGHT CONTROL ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 425]
**3.6 PF**
- “CLEAR FLIGHT CONTROL” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 425]

### 4. STATUS
**4.1 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.2 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.3 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**4.4 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.5 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.6 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.7 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 5. Approach and landing
**5.1 PF + PM**
- Disregard FMS fuel predictions; find the fuel penalty factor in QRH/OPS Fuel Penalty Factors/ECAM Alert Table [FCOM PRO-ABN-HYD P 19/76, PDF 3708; QRH OPS.04C, PDF 275; QRH OPS.04E, PDF 277]
- LDG DIST PROC: apply [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
**5.2 PF**
- SLATS/FLAPS SLOW [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- ALTN Y BRK WITH A/SKID; no autobrake or normal braking; reverser 1 inoperative [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
**5.3 PM**
- L/G GRVTY PROC …… APPLY [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- See the QRH L/G GRAVITY EXTENSION brief. Fuel consumption is increased for flight with L/G extended [FCOM PRO-ABN-HYD P 19/76, PDF 3708; QRH 24.02A, PDF 216]

## 4. Procedure
### HYD G RSVR LO LVL (FCOM PRO-ABN-HYD)
- PTU …… OFF [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
- GREEN ENG 1 PUMP …… OFF [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
- *G ENG 1 PUMP LO PR* [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
- *ASSOCIATED PROCEDURES: G SYS LO PR; FUEL CONSUMPT INCRSD; FMS PRED UNRELIABLE* [FCOM PRO-ABN-HYD P 18/76, PDF 3707]
- *SECONDARY FAILURES: *WHEEL; *F/CTL* [FCOM PRO-ABN-HYD P 18/76, PDF 3707]

## 5. STATUS
**Limitations**
- L/G GRVTY PROC ....... APPLY [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- LDG DIST PROC ....... APPLY [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
**Information**
- Refer to PRO-ABN-LG [QRH] L/G GRAVITY EXTENSION. CAUTION: For flight with L/G extended, fuel consumption is increased. Refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table. [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- FUEL CONSUMPT INCRSD: triggered when the failure (or combination of failures) affects the nominal aerodynamic characteristics of the aircraft. [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- FMS PRED UNRELIABLE: disregard FMS fuel predictions and refer to QRH/OPS Fuel Penalty Factors/ECAM Alert Table in order to find the applicable Fuel Penalty Factor. [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- ALTN Y BRK WITH A/SKID [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- SLATS/FLAPS SLOW [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- CAT 3 SINGLE ONLY [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
**INOP SYS**
- GREEN HYD [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- SPLR 1 + 5 [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- CAT 3 DUAL [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- AUTO BRK (in flight, or on ground with at least one engine running) [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- NORM BRK [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- L/G RETRACT [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- REVERSER 1 [FCOM PRO-ABN-HYD P 19/76, PDF 3708]
- YAW DAMPER 1 (in flight, or on ground with both engines running) [FCOM PRO-ABN-HYD P 19/76, PDF 3708]

## 7. FCTM technique
- In case of reservoir low level, the PTU must be switched OFF as required by ECAM to avoid a PTU overheat which may occur two minutes later. A PTU overheat may lead to the loss of the second hydraulic circuit. [FCTM PR-AEP-HYD P 1/4, PDF 438]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| L/G GRAVITY EXTENSION | STATUS: L/G GRVTY PROC APPLY. | See the L/G gravity extension brief | [FCOM PRO-ABN-HYD P 19/76, PDF 3708; QRH 24.02A, PDF 216] |
| Fuel Penalty Factors/ECAM Alert Table | FMS PRED UNRELIABLE and FUEL CONSUMPT INCRSD. The G SYS LO PR row depends on whether spoilers 1 and 5 are indicated extended. | Find the factor in the QRH table for the registration | [QRH OPS.04C, PDF 275; QRH OPS.04E, PDF 277] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No PDP module covers this alert; the flow is the standard ECAM sequence with the FCTM PTU recommendation. [PDP Management of abnormal operations, PDF 424; FCTM PR-AEP-HYD P 1/4, PDF 438]
- The QRH reset table has no entry for this alert. [QRH 02.01A, PDF 50]
- The manuals name no PF/PM split for the approach items here; the split follows the task sharing and the L/G gravity extension brief. [FCTM AOP-20 P 1–2/10, PDF 68; QRH 24.02A, PDF 216]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-HYD — HYD G RSVR LO LVL | P 17–19/76 | 3706–3708 | 26 MAY 26 |
| FCOM | DSC-29-10-20 — green pump, PTU | P 1/6, 3/6 | 1744, 1746 | 11 MAR 19 |
| FCTM | PR-AEP-HYD — hydraulic generation particularities | P 1/4 | 438 | 26 MAY 26 |
| QRH | 24.02 L/G gravity extension; OPS.04 fuel penalty factors; 02.01 system reset | 24.02A; OPS.04C, E; 02.01A | 216, 275, 277, 50 | 26 MAY 26, 14 JUL 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
