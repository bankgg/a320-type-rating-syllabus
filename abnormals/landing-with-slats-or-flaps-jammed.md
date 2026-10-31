# LANDING WITH SLATS OR FLAPS JAMMED — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**QRH procedure · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX.

The approach configures in steps with selected speed: VFE NEXT - 5 kt, then one flaps lever step at VFE NEXT, repeated until the landing configuration. In landing configuration on final, decelerate to the calculated VAPP and keep selected speed; no AP below 500 ft AGL. Prepare the go-around speed from the MAX SPEED table before the approach.

## 1. What it is
- **Trigger:** A QRH procedure, requested by S/F JAMMED PROC APPLY on the STATUS page of a slats/flaps fault or a dual hydraulic failure. [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- **Flight phase inhibition:** none [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- The line SPD SEL VFE NEXT - 5 kt lets the crew configure for landing while controlling the speed safely. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- FMS predictions do not take slat or flap failures into account. Fuel consumption is increased, so the predictions are not valid. [FCTM PR-AEP-F_CTL P 1/6, PDF 428]
- QRH fuel penalty factor for all HS-TX: flaps extended 80 %, slats extended 60 %, slats and flaps extended 100 %. [QRH OPS.04C, PDF 275; QRH OPS.04E, PDF 277]

## 2. Key limits
- **Configure:** SPD SEL VFE NEXT - 5 kt; AT VFE NEXT: flaps lever one step down [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- **Final:** Keep selected speed: calculated VAPP [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- **AP:** DO NOT USE BELOW 500 ft AGL [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- **Go-around, circuit:** Recommended speed: MAX SPEED - 10 kt [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
- **Diversion with slats/flaps extended:** Cruise altitude limited to 20 000 ft [FCTM PR-AEP-F_CTL P 2/6, PDF 429]

## 3. Flow (PF / PM)
### 1. Order and prepare
**1.1 PF**
- “LANDING WITH SLATS OR FLAPS JAMMED PROCEDURE” [PDP Management of abnormal operations, PDF 427]
**1.2 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427]
**1.3 PM**
- LDG DIST PROC …… APPLY [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- Determine flap lever position for landing [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
**1.4 PF**
- Update the arrival briefing: tail strike awareness, go-around configuration, any deviation from standard callout, speeds after a missed approach, selected speed for acceleration at the acceleration altitude [FCTM PR-AEP-F_CTL P 2/6, PDF 429]

### 2. Configure · repeat until landing configuration
**2.1 PF**
- SPD SEL …… VFE NEXT - 5 kt [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- This may take you below the manoeuvring speed for the current configuration, which is acceptable above VLS. Preferably reduce speed and configure with wings level [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
**2.2 PF + PM**
- **AT VFE NEXT** [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
  - SELECT FLAPS LEVER ONE STEP DOWN [QRH 20.02B, PDF 188; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- OVERSPEED alert and VLS on the PFD are computed from the current flaps/slats position. VFE and VFE NEXT follow the FLAPS lever; if not displayed, use the placard speeds [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
**2.3 PF**
- **If VLS is greater than VFE NEXT (overweight landing case)** [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
  - The FLAPS lever can be set in the required next position while the speed is reduced to follow VLS reduction as surfaces extend. The VFE warning threshold should not be triggered [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
  - Disconnect the A/THR; it can be re-engaged when the landing configuration is established [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]

### 3. Final approach and landing
**3.1 PF**
- **When in landing CONF and in final approach** [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
  - DECELERATE TO CALCULATED VAPP [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
  - Use and keep the selected speed [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
  - DO NOT USE AP BELOW 500 ft AGL [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474]
- VAPP should be close to VLS + wind correction. If VAPP is lower than VLS, disconnect the A/THR above VLS when reducing to VAPP [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- An early stabilized approach should be preferred; approach attitudes change, so stay aware of tail strike [FCTM PR-AEP-F_CTL P 1/6, PDF 428; FCTM PR-AEP-F_CTL P 2/6, PDF 429]
**3.2 PM**
- “LANDING WITH SLATS OR FLAPS JAMMED PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

### 4. Go-around
**4.1 PF**
- Use selected speed: at the acceleration altitude, control the acceleration to the speed required for the configuration [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- MAX SPEED from the table. In a go-around with CONF FULL selected, the L/G GEAR NOT DOWN warning triggers at landing gear retraction [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
**4.2 PF + PM**
- **If SLATS jammed** [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
  - **For circuit** [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
    - MAINTAIN SLATS/FLAPS CONFIGURATION; recommended speed MAX SPEED - 10 kt [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
  - **For diversion** [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
    - SELECT FLAPS LEVER 0. Recommended speed for flaps retraction: between MAX SPEED - 10 kt and MAX SPEED. Recommended diversion speed: MAX SPEED - 10 kt. INCREASED FUEL CONSUMPTION [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
- **If FLAPS jammed** [QRH 20.02C, PDF 189; QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
  - **For circuit** [QRH 20.02C, PDF 189; QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
    - MAINTAIN SLATS/FLAPS CONFIGURATION; recommended speed MAX SPEED - 10 kt. If HYD G+Y SYS LO PR: MAINTAIN SPEED CLOSE TO VAPP [QRH 20.02C, PDF 189; QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
  - **For diversion, flaps jammed at 0** [QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
    - SELECT FLAPS LEVER 0. Recommended speed for slats retraction: between MAX SPEED - 10 kt and MAX SPEED. USE NORMAL OPERATING SPEEDS. If HYD G+Y SYS LO PR: MAINTAIN AT LEAST THE HIGHER OF VAPP OR VLS [QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
  - **For diversion, flaps jammed > 0** [QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475; FCOM PRO-ABN-F_CTL P 3/132, PDF 3476]
    - MAINTAIN SLAT/FLAP CONFIGURATION. Recommended speed for diversion: MAX SPEED - 10 kt. If HYD G+Y SYS LO PR: MAINTAIN SPEED CLOSE TO VAPP. INCREASED FUEL CONSUMPTION [QRH 20.02D, PDF 190; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475; FCOM PRO-ABN-F_CTL P 3/132, PDF 3476]

## 4. Procedure
### LANDING WITH SLATS OR FLAPS JAMMED (QRH 20.02B–D / FCOM PRO-ABN-F_CTL)
- LDG DIST PROC …… APPLY [QRH 20.02B, PDF 188]
- *Determine flap lever position for landing.* [QRH 20.02B, PDF 188]
- **Repeat the following until landing configuration is reached:** [QRH 20.02B, PDF 188]
  - SPD SEL …… VFE NEXT - 5 kt [QRH 20.02B, PDF 188]
  - *AT VFE NEXT: SELECT FLAPS LEVER ONE STEP DOWN* [QRH 20.02B, PDF 188]
  - *OVERSPEED alert, and VLS displayed on the PFD, are computed according to the current flaps/slats position.* [QRH 20.02C, PDF 189]
  - *VFE and VFE NEXT are displayed on the PFD according to the FLAPS lever position. If not displayed, use the placard speeds.* [QRH 20.02C, PDF 189]
  - *In some cases, the recommended speed for go-around requested by the procedure might be slightly above the VFE displayed on PFD as the VFE is linked to the S/F lever position. The OVERSPEED alert will not be triggered as it is taking into account the current slat/flap position.* [QRH 20.02C, PDF 189]
  - *If VLS is greater than VFE NEXT (overweight landing case), the FLAPS lever can be set in the required next position, while the speed is reduced to follow VLS reduction as surfaces extend. The VFE warning threshold should not be triggered. In this case, disconnect the A/THR. A/THR can be re-engaged when the landing configuration is established.* [QRH 20.02C, PDF 189]
- **When in landing CONF and in final approach:** [QRH 20.02C, PDF 189]
  - *DECELERATE TO CALCULATED VAPP* [QRH 20.02C, PDF 189]
  - *The flight crew must use and keep the selected speed.* [QRH 20.02C, PDF 189]
  - *DO NOT USE AP BELOW 500 ft AGL* [QRH 20.02C, PDF 189]
- **For Go-around: (MAX SPEED table)** [QRH 20.02C, PDF 189]
  - *In the case of go-around with CONF FULL selected, the L/G GEAR NOT DOWN warning is triggered at landing gear retraction.* [QRH 20.02C, PDF 189]
  - **If SLATS jammed:** [QRH 20.02C, PDF 189]
    - **For circuit:** [QRH 20.02C, PDF 189]
      - *MAINTAIN SLATS/FLAPS CONFIGURATION* [QRH 20.02C, PDF 189]
      - *Recommended speed: MAX SPEED - 10 kt* [QRH 20.02C, PDF 189]
    - **For diversion:** [QRH 20.02C, PDF 189]
      - *SELECT FLAPS LEVER 0* [QRH 20.02C, PDF 189]
      - *Recommended speed for flaps retraction: between MAX SPEED - 10 kt and MAX SPEED* [QRH 20.02C, PDF 189]
      - *Recommended speed for diversion: MAX SPEED - 10 kt* [QRH 20.02C, PDF 189]
      - *INCREASED FUEL CONSUMPTION* [QRH 20.02C, PDF 189]
  - **If FLAPS jammed:** [QRH 20.02C, PDF 189]
    - **For circuit:** [QRH 20.02C, PDF 189]
      - *MAINTAIN SLATS/FLAPS CONFIGURATION* [QRH 20.02C, PDF 189]
      - *Recommended speed: MAX SPEED - 10 kt* [QRH 20.02C, PDF 189]
      - **If HYD G+Y SYS LO PR:** [QRH 20.02D, PDF 190]
        - *MAINTAIN SPEED CLOSE TO VAPP* [QRH 20.02D, PDF 190]
    - **For diversion:** [QRH 20.02D, PDF 190]
      - **If FLAPS jammed at 0:** [QRH 20.02D, PDF 190]
        - *SELECT FLAPS LEVER 0* [QRH 20.02D, PDF 190]
        - *Recommended speed for slats retraction: between MAX SPEED - 10 kt and MAX SPEED* [QRH 20.02D, PDF 190]
        - *USE NORMAL OPERATING SPEEDS* [QRH 20.02D, PDF 190]
        - **If HYD G+Y SYS LO PR:** [QRH 20.02D, PDF 190]
          - *MAINTAIN AT LEAST THE HIGHER OF VAPP OR VLS* [QRH 20.02D, PDF 190]
      - **If FLAPS jammed > 0:** [QRH 20.02D, PDF 190]
        - *MAINTAIN SLAT/FLAP CONFIGURATION* [QRH 20.02D, PDF 190]
        - *Recommended speed for diversion: MAX SPEED - 10 kt* [QRH 20.02D, PDF 190]
        - **If HYD G+Y SYS LO PR:** [QRH 20.02D, PDF 190]
          - *MAINTAIN SPEED CLOSE TO VAPP* [QRH 20.02D, PDF 190]
        - *INCREASED FUEL CONSUMPTION* [QRH 20.02D, PDF 190]
- **CAUTION** For flight with SLATS or FLAPS extended, fuel consumption is increased. Refer to OPS Use of Fuel Penalty Factor Tables. [QRH 20.02D, PDF 190]

## 6. QRH and reference tables
### MAX SPEED 
Slats/flaps position displayed on the upper ECAM display.

| Slats \ Flaps | F = 0 | 0 < F ≤ 1 | 1 < F ≤ 2 | 2 < F ≤ 3 | F > 3 |
|---|---|---|---|---|---|
| S = 0 | NO LIMITATION | 215 kt | 200 kt | 185 kt | Not allowed (177 kt) |
| 0 < S < 1 | 230 kt | 215 kt | 200 kt | 185 kt | Not allowed (177 kt) |
| S = 1 | 230 kt | 215 kt | 200 kt | 185 kt | 177 kt |
| 1 < S ≤ 3 | 200 kt | 200 kt | 200 kt | 185 kt | 177 kt |
| S > 3 | 177 kt | 177 kt | 177 kt | 177 kt | 177 kt |
[FCOM PRO-ABN-F_CTL P 59/132, PDF 3532; FCOM PRO-ABN-F_CTL P 1/132, PDF 3474; QRH 20.02C, PDF 189]

### APPR SPD 
Slats/flaps position displayed on the upper ECAM display.

| Slats \ Flaps | F = 0 | 0 < F < 1 | 1 ≤ F < 2 | 2 ≤ F < 3 | F = 3 | F > 3 |
|---|---|---|---|---|---|---|
| S = 0 | VREF +60 (Appr), VREF +50 (Touch Down) | VREF +45 | VREF +30 | VREF +25 | VREF +25 | Not allowed |
| 0 < S < 1 | VREF +45 | VREF +45 | VREF +30 | VREF +25 | VREF +25 | Not allowed |
| 1 ≤ S ≤ 3 | VREF +25 | VREF +25 | VREF +15 | VREF +10 | VREF +10 | VREF +10 |
| S > 3 | VREF +25 | VREF +25 | VREF +15 | VREF +10 | VREF +10 | VREF +5 |
[FCOM PRO-ABN-F_CTL P 59/132, PDF 3532]

## 7. FCTM technique
- This procedure may reduce speed below the manoeuvring speed for the current configuration, which is acceptable if the speed stays above VLS. Reduce speed and configure preferably with wings level. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- Assuming VLS is displayed, VAPP should be close to VLS + wind correction, because this speed is computed from the current slat/flap position. VAPP can be lower than VLS: then disconnect the A/THR above VLS when reducing to VAPP. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- The AP may be used down to 500 ft AGL. It is not tuned for abnormal configurations: monitor it. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]
- In the arrival briefing, emphasize tail strike awareness, the go-around configuration, any deviation from standard callout, the speeds after a missed approach, and selected speed for acceleration at the acceleration altitude. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| F/CTL FLAPS FAULT/LOCKED | Leads here | See the FLAPS brief | [FCOM PRO-ABN-F_CTL P 1/132, PDF 3474] |
| F/CTL SLATS FAULT/LOCKED | Leads here | See the SLATS brief | [FCOM PRO-ABN-F_CTL P 1/132, PDF 3474] |
| HYD G+B / G+Y SYS LO PR | Leads here; their QRH summaries include these lines and add the hydraulic-specific speeds | See the HYD briefs | [QRH 23.02A, PDF 210; QRH 23.03A, PDF 212] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The QRH and FCOM word two lines differently: "Recommended speed for diversion" / "Recommended diversion speed", and "L/G GEAR NOT DOWN" / "L/G L/G NOT DOWN". The QRH wording is used. [QRH 20.02C, PDF 189; FCOM PRO-ABN-F_CTL P 2/132, PDF 3475]
- The procedure gives no PF/PM roles, and the PDP has no slide for it: the turns follow the task sharing for a QRH procedure, and the flap lever selection is shown as shared. [PDP Management of abnormal operations, PDF 427; FCTM AOP-20 P 1–2/10, PDF 68]
- "Any deviation from standard call out" is to be briefed, but the manuals do not list the deviations. [FCTM PR-AEP-F_CTL P 2/6, PDF 429]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| QRH | 20.02 — Landing with Slats or Flaps Jammed; OPS.04 — fuel penalty factors | 20.02B–D · OPS.04C, E | 188–190, 275, 277 | 26 MAY 26, 14 JUL 26 |
| FCOM | PRO-ABN-F_CTL — [QRH] procedure (HS-TX); FLAPS/SLATS tables | P 1–3, 59/132 | 3474–3476, 3532 | 26 MAY 26 |
| FCTM | PR-AEP-F_CTL — abnormal slats/flaps configuration | P 1–2/6 | 428–429 | 26 MAY 26 |
| PDP | Management of abnormal operations | — | 427 |  |
