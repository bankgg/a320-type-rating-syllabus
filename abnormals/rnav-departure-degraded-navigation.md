# RNAV DEPARTURE · DEGRADED NAVIGATION — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Technique · no memory items**  
**Applicability:** all HS-TX — FCOM PBN blocks for ALL aircraft. No ECAM or QRH procedure covers the degradation as a whole.

There is no single procedure: the FCOM PBN chapter says what to do for RNAV 1(2) and RNP 1 airspace, and both lists are the same. A message on one side: continue on the FMGC that provides the correct position. A message on both sides or a position disagreement: find the correct FMGC on the MCDU PROG page and continue on it. NAV ACCUR DOWNGRAD on both sides: tell ATC the capability is lost.

## 1. What it is
- **Trigger:** On an RNAV SID in RNAV 1(2) or RNP 1 airspace: GPS PRIMARY LOST, NAV ACCUR DOWNGRAD, FMS1/FMS2 POS DIFF, CHECK IRS 1(2)(3)/FM POSITION, CHECK A/C POSITION or NAV FM/GPS POS DISAGREE. [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
- **Flight phase inhibition:** none [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
- RNAV 1(2) operations correspond to P-RNAV terminal RNAV; the AIP may specify that GPS is required. RNP 1 operations correspond to RNP 1 terminal operations. [FCOM PRO-SPO-51 P 4/14, PDF 4603; FCOM PRO-SPO-51 P 9/14, PDF 4608]
- For RNP 1, RAIM/AIME availability should be confirmed during flight preparation. [FCOM PRO-SPO-51 P 9/14, PDF 4608]
- If GPS PRIMARY LOST is displayed, navigation accuracy stays sufficient for RNP operations provided the RNP value is checked or entered and HIGH accuracy is displayed. [FCOM LIM-AFS-10 P 4/8, PDF 4669; FCOM LIM-AFS-10 P 5/8, PDF 4670]
- GPS jamming or spoofing can cause NAV ACCUR DOWNGRAD, GPS PRIMARY LOST and NAV FM/GPS POS DISAGREE. [FCOM PRO-NOR-SUP-GPSINT P 1/18, PDF 4418]

## 2. Key limits
- **RNP accuracy, terminal area:** 0.5 NM with AP ON; 0.51 NM with AP OFF [FCOM LIM-AFS-10 P 4/8, PDF 4669]
- **RNP accuracy, en route:** 1 NM (AP OFF, FD OFF: 1.1 NM) [FCOM LIM-AFS-10 P 3/8, PDF 4668]
- **NAV ACCUR DOWNGRAD on both sides:** Inform ATC that the capability is lost [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]

## 3. Flow (PF / PM)
### 1. Before the RNAV SID
**1.1 PF**
- Crosscheck the terminal procedure from the chart against the F-PLN page: waypoint sequences, tracks, distances, altitude or speed constraints [FCOM PRO-SPO-51 P 4/14, PDF 4603; FCOM PRO-SPO-51 P 9/14, PDF 4608]
- Do not modify the database procedure unless ATC requires it (DIR TO, radar vectoring, insertion of waypoints from the database) [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 9/14, PDF 4608]
**1.2 PF + PM**
- Check the minimum equipment for the airspace (see What it is) [FCOM PRO-SPO-51 P 4/14, PDF 4603; FCOM PRO-SPO-51 P 9/14, PDF 4608]

### 2. Message on one side — continue
**2.1 PM**
- **GPS PRIMARY LOST or NAV ACCUR DOWNGRAD on one ND/MCDU** [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
  - Announce the message to the PF [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
**2.2 PF**
- Resume navigation with the FMGC that provides the correct position [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
**2.3 PM**
- Monitor the flight path and navigation [FCTM AOP-20 P 1–2/10, PDF 68]

### 3. Both sides or a position disagreement — find the correct FMGC
**3.1 PM**
- **GPS PRIMARY LOST on both NDs/MCDUs · FMS1/FMS2 POS DIFF · CHECK IRS 1(2)(3)/FM POSITION · CHECK A/C POSITION · NAV FM/GPS POS DISAGREE** [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
  - Check the position data on the MCDU PROG page to identify which FMGC position is correct [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
**3.2 PF**
- Resume navigation with the FMGC that provides the correct position [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]

### 4. NAV ACCUR DOWNGRAD on both sides — tell ATC
**4.1 PF**
- **NAV ACCUR DOWNGRAD on both sides** [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
  - Inform ATC that the RNAV 1(2) or RNP 1 capability is lost [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
- The PF communicates during abnormal management [FCTM AOP-20 P 1–2/10, PDF 68]

### 5. NAV FM/GPS POS DISAGREE on ECAM
**5.1 PM**
- A/C POS …… CHECK [FCOM PRO-ABN-NAV P 79/124, PDF 3904]
- FMS POSITION/MONITOR page; for the rest of the flight consider periodic NAV ACCURACY checks [FCOM PRO-ABN-NAV P 79/124, PDF 3904]

## 4. Procedure
### Management of degraded navigation, RNAV 1(2) (FCOM PRO-SPO-51)
- **If one of the following messages is displayed, the flight crew should resume navigation with the FMGC that provides the correct position:** [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *GPS PRIMARY LOST on one ND/MCDU* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *NAV ACCUR DOWNGRAD on one ND/MCDU* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
- **If one of the following MCDU or ECAM messages is displayed, the flight crew should check the position data via the MCDU PROG page in order to identify which FMGC position is correct:** [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *GPS PRIMARY LOST on both NDs/MCDUs* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *FMS1/FMS2 POS DIFF* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *CHECK IRS 1(2)(3)/FM POSITION* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *CHECK A/C POSITION* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *NAV FM/GPS POS DISAGREE* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *The flight crew should resume navigation with the FMGC that provides the correct position.* [FCOM PRO-SPO-51 P 5/14, PDF 4604]
- **If NAV ACCUR DOWNGRAD is displayed on both sides:** [FCOM PRO-SPO-51 P 5/14, PDF 4604]
  - *The flight crew should inform the ATC that the RNAV 1(2) capability is lost.* [FCOM PRO-SPO-51 P 5/14, PDF 4604]

### Management of degraded navigation, RNP 1 (FCOM PRO-SPO-51)
- *The same lists as RNAV 1(2).* [FCOM PRO-SPO-51 P 9/14, PDF 4608; FCOM PRO-SPO-51 P 10/14, PDF 4609]
- **If NAV ACCUR DOWNGRAD is displayed on both sides:** [FCOM PRO-SPO-51 P 10/14, PDF 4609]
  - *The flight crew should inform the ATC that the RNP 1 capability is lost.* [FCOM PRO-SPO-51 P 10/14, PDF 4609]

### NAV FM/GPS POS DISAGREE (amber caution) (FCOM PRO-ABN-NAV)
- A/C POS …… CHECK — Use the FMS POSITION/MONITOR page. For the remainder of the flight, consider periodic NAV ACCURACY check. [FCOM PRO-ABN-NAV P 79/124, PDF 3904]

## 6. QRH and reference tables
### Minimum equipment to enter the airspace 
The temporary display of ND information via the PFD/ND sw is permitted on the PM side.

| Item | RNAV 1(2) | RNP 1 |
|---|---|---|
| FMGC | One | One |
| MCDU | One | One |
| Position update | One GPS or one DME receiver | One GPS |
| IRS | Two | Two |
| FD | One in NAV mode | One in NAV mode |
| ND | Two | Two |
[FCOM PRO-SPO-51 P 4/14, PDF 4603; FCOM PRO-SPO-51 P 9/14, PDF 4608]

### RNP accuracy with GPS PRIMARY 
AP or FD in NAV.

| Phase | AP ON | AP OFF, FD ON | AP OFF, FD OFF |
|---|---|---|---|
| En route | 1 NM | 1 NM | 1.1 NM |
| Terminal area | 0.5 NM | 0.51 NM | 0.51 NM |
[FCOM LIM-AFS-10 P 3/8, PDF 4668; FCOM LIM-AFS-10 P 4/8, PDF 4669]

## 7. FCTM technique
- Fly, navigate, communicate in that order: keep a safe flight path first, and start READ & DO actions no lower than 400 ft AGL unless the path is safe. [FCTM AOP-30-30 P 1/6, PDF 82]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| FMGC faults | An FMGC failure as the system failure on the SID | See the FMGC faults brief | [FCOM PRO-SPO-51 P 4/14, PDF 4603] |
| RNP approach · degraded navigation | Different limits apply once on an RNAV(GNSS) or RNAV(RNP) approach | See the RNP approach brief | [FCOM PRO-NOR-SOP-18-C P 16/36, PDF 4251] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The manuals have no ECAM or QRH procedure for degraded navigation on a SID: this brief is built from the FCOM PBN lists. The PF/PM turns are arranged from the general task sharing, not from a PDP slide. [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCTM AOP-20 P 1–2/10, PDF 68]
- The manuals do not say how to continue the SID once the capability is lost (for example conventional navigation or vectors); they say only to inform ATC. [FCOM PRO-SPO-51 P 5/14, PDF 4604; FCOM PRO-SPO-51 P 10/14, PDF 4609]
- The syllabus does not name the failure, so the brief covers the listed messages. The required specification (RNAV 1 or RNP 1) comes from the departure chart, which is not in the supplied books. [FCOM PRO-SPO-51 P 4/14, PDF 4603; FCOM PRO-SPO-51 P 9/14, PDF 4608]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-SPO-51 — RNAV 1(2), RNP 1 | P 4–5, 9–10/14 | 4603–4604, 4608–4609 | 18 FEB 26 |
| FCOM | LIM-AFS-10 — navigation performance | P 3–5/8 | 4668–4670 | 18 FEB 26 |
| FCOM | PRO-ABN-NAV — NAV FM/GPS POS DISAGREE | P 79/124 | 3904 | 26 MAY 26 |
| FCOM | PRO-NOR-SUP-GPSINT — GPS interference | P 1/18 | 4418 | 14 JUL 26 |
| FCTM | AOP-20 · AOP-30-30 | P 1–2/10 · P 1/6 | 68–69, 82 |  |
