# RNP APPROACH · DEGRADED NAVIGATION — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Technique · no memory items**  
**Applicability:** all HS-TX — FCOM SOP blocks for all HS-TX. No ECAM procedure covers the degradation as a whole.

There is no single procedure: the FCOM SOP lists what to do under Management of Degraded Navigation, and the crew reviews it in the arrival briefing. This brief leads with RNAV(GNSS) approaches with LNAV/VNAV minima; RNAV(RNP) rules are kept for reference under From the manuals. A loss on one side only: continue on the remaining AP/FD. A loss on both sides, XTK above 0.3 NM or 75 ft below the path: discontinue unless visual references are enough to proceed visually. Hand-flying needs the FD: in approach, AP and FD both off is not authorized without F-LOC deviation.

## 1. What it is
- **Trigger:** During an RNAV(GNSS) or RNAV(RNP) approach: GPS PRIMARY LOST, NAV ACCUR DOWNGRAD, NAV FM/GPS POS DISAGREE, excessive XTK or V/DEV, FINAL APP not engaging, or a failure of a guidance system. [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251; FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
- **Flight phase inhibition:** none [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251; FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
- "RNP APCH" corresponds to RNAV(GNSS) approaches and "RNP AR" to RNAV(RNP). Both use FINAL APP with V/DEV and XTK deviations. [FCOM PRO-SPO-51 P 10/14, PDF 4609; FCOM PRO-SPO-51 P 12/14, PDF 4611; PDP 3D approach, PDF 246]
- Minimum equipment to start RNP APCH: one FMGC, one GPS, two IRS, one MCDU, one FD, one PFD on the PF side, two NDs, two FCU channels. [FCOM PRO-SPO-51 P 11/14, PDF 4610]
- If GPS PRIMARY LOST is displayed, navigation accuracy stays sufficient for RNP operations provided the RNP value is checked or entered and HIGH accuracy is displayed. An RNAV(GNSS) approach, however, requires GPS PRIMARY. [FCOM LIM-AFS-10 P 4/8, PDF 4669; FCOM LIM-AFS-10 P 5/8, PDF 4670]
- GPS jamming or spoofing can cause NAV ACCUR DOWNGRAD, GPS PRIMARY LOST and NAV FM/GPS POS DISAGREE. [FCOM PRO-NOR-SUP-GPSINT P 1/18, PDF 4418]

## 2. Key limits
- **PM callouts:** "CROSS TRACK" XTK > 0.1 NM · "VDEV" V/DEV > ½ dot (50 ft) [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249; FCOM PRO-NOR-SCO P 5/10, PDF 4314; PDP 3D approach, PDF 261]
- **Discontinue, lateral:** XTK > 0.3 NM [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- **Discontinue, vertical:** 75 ft below the path (V/DEV > ¾ dot) [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- **RNP accuracy in approach:** 0.3 NM with AP ON, or AP OFF with FD ON [FCOM LIM-AFS-10 P 4/8, PDF 4669]
- **Altimeter difference:** 100 ft maximum [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]

## 3. Flow (PF / PM)
### 1. Before the approach
**1.1 PF**
- GO-AROUND STRATEGY …… REVIEW [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
- The briefing includes Management of Degraded Navigation [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
- **At 10 000 ft AAL** [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
  - NAV ACCURACY …… CHECK [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
  - LOW: use TRK FPA for the approach [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
  - GPS PRIMARY …… CHECK [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
  - Available on at least one FMS [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248]
**1.2 PF + PM**
- BAROMETRIC REFERENCE …… SET/CROSSCHECK [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]

### 2. Final approach — monitor
**2.1 PF**
- Fly with FD or AP/FD: AP OFF with FD ON gives 0.3 NM in approach [FCOM LIM-AFS-10 P 3/8, PDF 4668; FCOM LIM-AFS-10 P 4/8, PDF 4669]
- APP NAV …… CHECK ARMED or ENGAGED [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]
- FINAL …… CHECK ARMED [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]
- FINAL APP (at the FDP) …… CHECK ENGAGED [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]
- **FINAL does not engage at the start of the final descent** [FCTM PR-NP-SOP-190-GUI P 21/36, PDF 290]
  - Consider interrupting the approach, unless visual references can be kept throughout [FCTM PR-NP-SOP-190-GUI P 21/36, PDF 290]
**2.2 PM**
- FLIGHT PARAMETERS …… MONITOR [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]
- Watch XTK on the ND, V/DEV on the PFD, and altitude crossings at the FAF and final approach waypoints [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]
- **XTK above 0.1 NM** [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249; FCOM PRO-NOR-SCO P 5/10, PDF 4314]
  - “CROSS TRACK” [FCOM PRO-NOR-SCO P 5/10, PDF 4314; PDP 3D approach, PDF 261]
- **V/DEV above ½ dot** [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249; FCOM PRO-NOR-SCO P 5/10, PDF 4314]
  - “VDEV” [FCOM PRO-NOR-SCO P 5/10, PDF 4314; PDP 3D approach, PDF 261]

### 3. Degradation on one side — continue
**3.1 PF**
- **GPS PRIMARY LOST or NAV ACCUR DOWNGRAD on one ND** [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - Use the appropriate remaining AP/FD [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
**3.2 PM**
- FLIGHT PARAMETERS …… MONITOR [FCOM PRO-NOR-SOP-18-C P 14/36, PDF 4249]

### 4. Both sides or excessive deviation — discontinue
**4.1 PF + PM**
- **If external visual references are not sufficient to proceed visually** [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - GPS PRIMARY LOST on both NDs [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - XTK > 0.3 NM [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - NAV FM/GPS POS DISAGREE [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - NAV ACCUR DOWNGRAD on both NDs [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- **In all cases** [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - 75 ft below the vertical path (V/DEV > ¾ dot) [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
**4.2 PF**
- THRUST LEVERS …… TOGA [FCOM PRO-NOR-SOP-20 P 1/4, PDF 4284]
- ROTATION …… PERFORM [FCOM PRO-NOR-SOP-20 P 1/4, PDF 4284]
- GO AROUND …… ANNOUNCE [FCOM PRO-NOR-SOP-20 P 1/4, PDF 4284]
- During an RF leg, check that NAV engages immediately; if it does not, engage it manually [FCTM PR-NP-SP-30 P 2/4, PDF 383]
**4.3 PM**
- FLIGHT PARAMETERS …… MONITOR [FCOM PRO-NOR-SOP-20 P 1/4, PDF 4284]
- FLAPS …… RETRACT ONE STEP [FCOM PRO-NOR-SOP-20 P 1/4, PDF 4284]

### 5. ECAM alerts during the approach
**5.1 PM**
- **NAV FM/GPS POS DISAGREE** [FCOM PRO-ABN-NAV P 79/124, PDF 3904]
  - A/C POS …… CHECK [FCOM PRO-ABN-NAV P 79/124, PDF 3904]
  - FMS POSITION/MONITOR page; for the rest of the flight consider periodic NAV ACCURACY checks [FCOM PRO-ABN-NAV P 79/124, PDF 3904]
- **NAV ALT DISCREPANCY** [FCOM PRO-ABN-NAV P 61/124, PDF 3886]
  - ALT …… X CHECK [FCOM PRO-ABN-NAV P 61/124, PDF 3886]
  - Against the standby altimeter [FCOM PRO-ABN-NAV P 61/124, PDF 3886]
  - AIR DATA SWTG …… AS RQRD [FCOM PRO-ABN-NAV P 61/124, PDF 3886]
  - ADR 3 to the faulty side [FCOM PRO-ABN-NAV P 61/124, PDF 3886]

## 4. Procedure
### Management of degraded navigation — RNAV(GNSS) (FCOM PRO-NOR-SOP-18-C)
- **Use the appropriate remaining AP/FD in the following cases:** [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - *GPS PRIMARY LOST on one ND* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - *NAV ACCUR DOWNGRAD on one ND* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- **Discontinue the approach in the following cases, if external visual references are not sufficient to proceed visually:** [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - *GPS PRIMARY LOST on both NDs* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - *XTK > 0.3 NM* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - *NAV FM/GPS POS DISAGREE* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
  - *NAV ACCUR DOWNGRAD on both NDs* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- *LNAV minima: be prepared to continue the approach by reverting to NAV-FPA, if the vertical guidance is not satisfactory.* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- *LNAV/VNAV minima: discontinue the approach in the case of deviation of 75 ft below the vertical path (V/DEV > ¾ dot).* [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]

### For reference — RNAV(RNP) differs (FCOM PRO-NOR-SOP-18-C)
- *GPS PRIMARY must be available on both FMS, with both GPS in NAV or SBAS. If one FMS is inoperative or one GPS is not in NAV or SBAS before the IAF, RNAV(RNP) is not permitted.* [FCOM PRO-NOR-SOP-18-C P 18/36, PDF 4253]
- **The approach may be continued in the case of single failure of:** [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *GPS (MMR) · FMGC · EFIS DU · MCDU · AP* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
- **Discontinue the approach in the following cases:** [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *FINAL APP does not engage* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *GPS PRIMARY LOST on both NDs* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *Dual NAV ACCUR DOWNGRAD* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *FM/GPS POSITION DISAGREE* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *FMS1/FMS2 POS DIFF* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *Dual loss of FMGC or dual loss of FINAL APP mode* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *Loss of GPWS TERRAIN function in case of inconsistencies affecting obstacles or terrain computation* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
  - *NAV ALT DISCREPANCY* [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
- *Go-around must be initiated if XTK reaches 1 RNP or V/DEV reaches ¾ dot below the vertical profile.* [FCOM PRO-NOR-SOP-18-C P 19/36, PDF 4254]

### NAV FM/GPS POS DISAGREE (amber caution) (FCOM PRO-ABN-NAV)
- A/C POS …… CHECK — Use the FMS POSITION/MONITOR page. For the remainder of the flight, consider periodic NAV ACCURACY check. [FCOM PRO-ABN-NAV P 79/124, PDF 3904]

### NAV ALT DISCREPANCY (amber caution) (FCOM PRO-ABN-NAV)
- ALT …… X CHECK — Crosscheck with the standby altimeter. [FCOM PRO-ABN-NAV P 61/124, PDF 3886]
- AIR DATA SWTG …… AS RQRD — Select ADR 3 to the faulty side. [FCOM PRO-ABN-NAV P 61/124, PDF 3886]

## 6. QRH and reference tables
### RNP accuracy with GPS PRIMARY 
AP or FD in NAV, or F-LOC in approach phase.

| Phase | AP ON | AP OFF, FD ON | AP OFF, FD OFF |
|---|---|---|---|
| En route | 1 NM | 1 NM | 1.1 NM |
| Terminal area | 0.5 NM | 0.51 NM | 0.51 NM |
| In approach | 0.3 NM | 0.3 NM | 0.3 NM with F-LOC deviation; not authorized without |
[FCOM LIM-AFS-10 P 3/8, PDF 4668; FCOM LIM-AFS-10 P 4/8, PDF 4669]

## 7. FCTM technique
- If NAV accuracy is LOW before the approach, use TRK FPA, and establish on the final course against navaid raw data. [FCOM PRO-NOR-SOP-18-C P 13/36, PDF 4248; FCTM PR-NP-SOP-190-GUI P 24/36, PDF 293]
- Monitor the final approach with the blue start-of-descent symbol, FMA, V/DEV, XTK and F-PLN, confirmed by needles and distance/altitude. [FCTM PR-NP-SOP-190-GUI P 21/36, PDF 290]
- With one engine inoperative, the bank limit can be below 30° when IAS is below manoeuvring speed; retracting flaps at the usual speeds may affect the turn radius. [FCTM PR-NP-SP-30 P 3/4, PDF 384; FCTM PR-NP-SP-30 P 4/4, PDF 385]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| FMGC faults | FMGC failure as the system failure | See the FMGC faults brief | [FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255] |
| GPS interference (FCOM supplementary) | Expected spoofing during approach | GLS, RNAV(GNSS) or RNAV(RNP) approaches should not be considered; GPS DESELECT | [FCOM PRO-NOR-SUP-GPSINT P 14/18, PDF 4431] |
| Go-around, one engine inoperative | Engine failure during the go-around | See the ENG 1(2) FAIL brief | [FCTM PR-NP-SP-30 P 3/4, PDF 384] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The manuals have no ECAM or QRH procedure for "RNP degradation": this brief is built from the FCOM SOP lists. The PF/PM turns are arranged from the SOP role labels, not from a PDP slide. [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251; FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
- The SOP does not list NAV ALT DISCREPANCY as a reason to discontinue an RNAV(GNSS) approach; it does for RNAV(RNP). [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251; FCOM PRO-NOR-SOP-18-C P 20/36, PDF 4255]
- The manuals do not say how to continue by hand when the PF-side FD is the one lost; they say only to use the appropriate remaining AP/FD. [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251]
- RNP AR contingency detail is in the Airbus ACD and airline procedures, which are not in the supplied books. [FCOM PRO-SPO-51 P 12/14, PDF 4611; FCOM PRO-SPO-51 P 13/14, PDF 4612]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-NOR-SOP-18-C — FINAL APP guidance, RNAV(RNP), degraded navigation | P 13–20/36 | 4248–4255 | 26 MAY 26 |
| FCOM | PRO-NOR-SCO — approach callouts | P 5/10 | 4314 | 26 MAY 26 |
| FCOM | LIM-AFS-10 — navigation performance, RNAV approach | P 3–5/8 | 4668–4670 | 18 FEB 26 |
| FCOM | PRO-SPO-51 — RNP APCH, RNP AR | P 10–13/14 | 4609–4612 | 18 FEB 26 |
| FCOM | PRO-ABN-NAV — NAV FM/GPS POS DISAGREE, NAV ALT DISCREPANCY | P 61, 79/124 | 3886, 3904 | 26 MAY 26 |
| FCOM | PRO-NOR-SOP-20 — go-around | P 1/4 | 4284 | 18 FEB 26 |
| FCOM | PRO-NOR-SUP-GPSINT — GPS interference | P 1, 14/18 | 4418, 4431 | 14 JUL 26 |
| FCTM | PR-NP-SOP-190-GUI · PR-NP-SP-30 | P 21, 24/36 · P 2–4/4 | 290, 293, 383–385 | 26 MAY 26 |
| PDP | 3D approach (XFTDN13DAPPRO01) | — | 246, 261 |  |
