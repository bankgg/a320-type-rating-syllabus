# FUEL IMBALANCE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** HS-TXA..TXO, HS-TXP..TXU — The center tank lines differ: CTR TK PUMP 1 and 2 on HS-TXA..TXO, CTR TK L and R XFR on HS-TXP..TXU.

A fuel imbalance may be a fuel leak, so check the fuel first: compare FOB + FU with the FOB at departure, and do not apply this procedure if a leak is suspected. Otherwise open the crossfeed, stop the center tank feed and switch OFF the pumps on the lighter side. When balanced, restore the pumps and close the crossfeed.

## 1. What it is
- **Trigger:** QRH procedure with no ECAM alert. There is no requirement to correct an imbalance until the ECAM fuel advisory is displayed (difference between wing fuel quantities greater than 1 500 kg). [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-ABN-ADV P 6/6, PDF 2841]
- **Flight phase inhibition:** none [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-ABN-ADV P 6/6, PDF 2841]
- In exceptional conditions (i.e. fuel system failure), the maximum imbalance values may be exceeded without significant effect to the aircraft handling qualities. The aircraft remains fully controllable in all flight phases. [FCOM LIM-FUEL P 3/4, PDF 4722]
- The fuel check (FOB + FU against the FOB at departure) must also be performed each time a FUEL IMBALANCE procedure is necessary, before applying it. An abnormally negative value suggests a leak; an abnormally positive value, a fuel quantity overread. [FCOM PRO-NOR-SOP-15 P 2/4, PDF 4199]

## 2. Key limits
- **ECAM fuel advisory:** Wing difference > 1 500 kg [FCOM PRO-ABN-ABN-ADV P 6/6, PDF 2841]
- **Correct before the advisory:** No requirement [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-FUEL P 3/76, PDF 3608]
- **Leak suspected:** Do not apply; apply FUEL LEAK [QRH 21.05A, PDF 198]
- **Max imbalance, tank full:** 1 500 kg in flight and at landing [FCOM LIM-FUEL P 3/4, PDF 4722]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PM**
- “ADVISORY ON FUEL SYSTEM” [FCTM AOP-30-40 P 1/2, PDF 88; PDP Management of abnormal operations, PDF 421]
- FUEL MANAGEMENT …… CHECK [FCOM PRO-ABN-ABN-ADV P 6/6, PDF 2841]
**1.2 PF**
- Asks the PM to monitor the drifting parameter [FCTM AOP-30-40 P 1/2, PDF 88; PDP Management of abnormal operations, PDF 421]

### 2. Rule out a fuel leak
**2.1 PM**
- FOB …… CHECK [QRH 21.05A, PDF 198]
- Compare the FOB + FU with the FOB at departure [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-FUEL P 3/76, PDF 3608; FCOM PRO-NOR-SOP-15 P 2/4, PDF 4199]
- **If the difference is significant, or if the FOB + FU decreases** [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-FUEL P 3/76, PDF 3608]
  - Suspect a fuel leak: do not apply this procedure. Apply FUEL LEAK [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-FUEL P 3/76, PDF 3608; FCOM PRO-NOR-SOP-15 P 2/4, PDF 4199]

### 3. Order
**3.1 PF**
- “FUEL IMBALANCE PROCEDURE” [PDP Management of abnormal operations, PDF 427]
**3.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427; FCTM AOP-30-30 P 5/6, PDF 86]

### 4. Balance
**4.1 PM**
- FUEL X FEED …… ON [QRH 21.05A, PDF 198]
- **[HS-TXA..TXO]** CTR TK PUMP 1 …… OFF [QRH 21.05A, PDF 198]
- **[HS-TXA..TXO]** CTR TK PUMP 2 …… OFF [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** CTR TK L XFR …… OFF [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** CTR TK R XFR …… OFF [QRH 21.05A, PDF 198]
- **On lighter side** [QRH 21.05A, PDF 198]
  - FUEL PUMPS …… OFF [QRH 21.05A, PDF 198]

### 5. When fuel balanced
**5.1 PM**
- **[HS-TXA..TXO]** ALL FUEL PUMPS …… ON [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** FUEL PUMPS …… ON [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** CTR TK L XFR …… ON [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** CTR TK R XFR …… ON [QRH 21.05A, PDF 198]
- FUEL X FEED …… OFF [QRH 21.05A, PDF 198]
- “FUEL IMBALANCE PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### FUEL IMBALANCE (QRH 21.05A; FCOM PRO-ABN-FUEL P 2–3/76)
- FOB …… CHECK [QRH 21.05A, PDF 198]
- **CAUTION** A fuel imbalance may indicate a fuel leak. Do not apply this procedure, if a fuel leak is suspected. Refer to ABN-21 Fuel Leak [QRH 21.05A, PDF 198]
- FUEL X FEED …… ON [QRH 21.05A, PDF 198]
- **[HS-TXA..TXO]** CTR TK PUMP 1 …… OFF [QRH 21.05A, PDF 198]
- **[HS-TXA..TXO]** CTR TK PUMP 2 …… OFF [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** CTR TK L XFR …… OFF [QRH 21.05A, PDF 198]
- **[HS-TXP..TXU]** CTR TK R XFR …… OFF [QRH 21.05A, PDF 198]
- **On lighter side:** [QRH 21.05A, PDF 198]
  - FUEL PUMPS …… OFF [QRH 21.05A, PDF 198]
- **When fuel balanced:** [QRH 21.05A, PDF 198]
  - **[HS-TXA..TXO]** ALL FUEL PUMPS …… ON [QRH 21.05A, PDF 198]
  - **[HS-TXP..TXU]** FUEL PUMPS …… ON [QRH 21.05A, PDF 198]
  - **[HS-TXP..TXU]** CTR TK L XFR …… ON [QRH 21.05A, PDF 198]
  - **[HS-TXP..TXU]** CTR TK R XFR …… ON [QRH 21.05A, PDF 198]
  - FUEL X FEED …… OFF [QRH 21.05A, PDF 198]
- *There is no requirement to correct an imbalance, until the ECAM fuel advisory is displayed.* [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-FUEL P 3/76, PDF 3608]

## 6. QRH and reference tables
### Maximum fuel imbalance in flight and at landing 
Inner tanks, outer tanks balanced. The variation is linear between these values, and there is no limitation below 2 250 kg.

| Heavier tank fuel quantity | Maximum asymmetry |
|---|---|
| Full | 1 500 kg |
| 4 300 kg | 1 600 kg |
| 2 250 kg | 2 250 kg |
| Outer tanks | 690 kg, with the conditions in the FCOM |
[FCOM LIM-FUEL P 3/4, PDF 4722]

### Maximum fuel imbalance at takeoff 
Inner tanks, outer tanks balanced. The variation is linear between these values.

| Heavier tank fuel quantity | Maximum asymmetry |
|---|---|
| Full | 500 kg |
| 3 000 kg | 1 050 kg |
| 1 450 kg | 1 450 kg |
| Outer tanks (inner balanced) | 370 kg |
[FCOM LIM-FUEL P 3/4, PDF 4722]

## 7. FCTM technique
- For any message or alert related to the fuel leak, fuel quantity or fuel imbalance, the flight crew should consider a fuel leak as a possible cause. [FCTM PR-AEP-FUEL P 1/4, PDF 434]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| FUEL LEAK | A fuel imbalance may indicate a fuel leak. If a wing leak is suspected, the FUEL LEAK procedure says not to apply FUEL IMBALANCE. | See the FUEL LEAK brief | [QRH 21.05A, PDF 198; QRH 21.06A, PDF 199] |

## 9. HS-TX differences
| Topic | HS-TXA..TXO | HS-TXP..TXU | Ref |
|---|---|---|---|
| Center tank lines | CTR TK PUMP 1 and 2 OFF; ALL FUEL PUMPS ON when balanced | CTR TK L and R XFR OFF; FUEL PUMPS ON and CTR TK L and R XFR ON when balanced | [QRH 21.05A, PDF 198] |

## 10. Gaps and omissions
- The FCTM has no technique for this procedure beyond considering a fuel leak; the PDP has no module for it. The flow is the standard advisory and QRH sequence. [FCTM PR-AEP-FUEL P 1/4, PDF 434; PDP Management of abnormal operations, PDF 427]
- The outer tank limit (690 kg in flight and at landing) has conditions on the inner tank quantities; see FCOM LIM-FUEL. [FCOM LIM-FUEL P 3/4, PDF 4722]
- The manuals print a separate version for each HS-TX group. "From the manuals" merges them into one procedure, with a chip on the lines that differ, confirmed by the user. [FCOM PRO-ABN-FUEL P 2/76, PDF 3607; FCOM PRO-ABN-FUEL P 3/76, PDF 3608]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| QRH | 21.05 FUEL IMBALANCE | 21.05A | 198 | 18 FEB 26 |
| FCOM | PRO-ABN-FUEL — [QRH] FUEL IMBALANCE | P 2–3/76 | 3607–3608 | 26 MAY 26 |
| FCOM | PRO-ABN-ABN-ADV; PRO-NOR-SOP-15; LIM-FUEL | P 6/6; P 2/4; P 3/4 | 2841, 4199, 4722 | 18 FEB 26 |
| FCTM | AOP-30-40 advisory; PR-AEP-FUEL | P 1/2; P 1/4 | 88, 434 | 24 NOV 25 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
