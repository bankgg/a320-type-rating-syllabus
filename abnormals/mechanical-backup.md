# MECHANICAL BACKUP — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Technique · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL (FCOM DSC and FCTM).

When the fly-by-wire control is lost, the aircraft is flown mechanically: pitch with the pitch trim wheel (THS), lateral with the rudder pedals. The aim is not accurate flying but a safe, stabilized attitude while the lost systems are restored. Move the trim wheel smoothly, because the THS is very powerful. Rudder makes the aircraft roll after a short delay, so apply some rudder, wait, and release early to level the wings.

## 1. What it is
- **Trigger:** No ECAM alert of its own. The last level of flight control reconfiguration: it covers a temporary total electrical loss, the temporary loss of the five fly-by-wire computers, the loss of both elevators, or the total loss of ailerons and spoilers. The PFDs show MAN PITCH TRIM ONLY in red. [FCOM DSC-27-20-20 P 18/20, PDF 1629; FCOM DSC-27-20-20 P 19/20, PDF 1630; FCTM AOP-10-30-20 P 2/2, PDF 63]
- **Flight phase inhibition:** none [FCOM DSC-27-20-20 P 18/20, PDF 1629; FCOM DSC-27-20-20 P 19/20, PDF 1630; FCTM AOP-10-30-20 P 2/2, PDF 63]
- Three levels of reconfiguration: alternate law, direct law, mechanical. [FCOM DSC-27-20-20 P 1/20, PDF 1612]
- The purpose of the mechanical backup is to achieve all safety objectives in MMEL dispatch condition: to manage a temporary and total electrical loss, the temporary loss of five fly-by-wire computers, the loss of both elevators, or the total loss of ailerons and spoilers. [FCOM DSC-27-20-20 P 18/20, PDF 1629]
- Pitch: the pilot manually applies trim to the THS; the PFDs display MAN PITCH TRIM ONLY in red. Lateral: the pilot uses the rudder pedals. [FCOM DSC-27-20-20 P 19/20, PDF 1630]
- MAN PITCH TRIM ONLY is displayed on the FMA (line 3) in case of loss of L + R elevators. [FCOM DSC-22_30-80-20 P 26/36, PDF 1251]
- The pilots can use conventional rudder pedals to control the rudder mechanically. [FCOM DSC-27-10-20 P 13/16, PDF 1578]
- Pitch trim wheels: mechanical control of the THS, priority over electrical control; an action on the wheel disconnects the AP. [FCOM DSC-27-20-30 P 2/22, PDF 1633]

## 2. Key limits
- **Pitch:** Pitch trim wheel (THS) [FCOM DSC-27-20-20 P 19/20, PDF 1630; FCTM AOP-10-30-20 P 2/2, PDF 63]
- **Lateral:** Rudder pedals [FCOM DSC-27-20-20 P 19/20, PDF 1630; FCTM AOP-10-30-20 P 2/2, PDF 63]
- **THS needs:** G or Y hydraulic [FCOM DSC-27-10-20 P 3/16, PDF 1568]
- **PFD:** MAN PITCH TRIM ONLY (red) [FCOM DSC-27-20-20 P 19/20, PDF 1630]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF + PM**
- PFDs show MAN PITCH TRIM ONLY in red [FCOM DSC-27-20-20 P 19/20, PDF 1630; FCOM DSC-22_30-80-20 P 26/36, PDF 1251]
- Objective: keep the aircraft attitude safe and stabilized, not accurate flying, to allow restoration of the lost systems [FCTM AOP-10-30-20 P 2/2, PDF 63]
**1.2 PF**
- Fly the aircraft: pitch trim wheel for pitch, rudder pedals for lateral control [FCOM DSC-27-20-20 P 19/20, PDF 1630; FCTM AOP-10-30-20 P 2/2, PDF 63]

### 2. Pitch control
**2.1 PF**
- Use the pitch trim wheel to control pitch; apply any action smoothly — the THS effect is significant due to its large size [FCTM AOP-10-30-20 P 2/2, PDF 63]
- Mechanical THS control is available at any time if the green or yellow hydraulic system works; the trim wheel has priority over electrical control [FCOM DSC-27-10-20 P 3/16, PDF 1568; FCOM DSC-27-20-30 P 2/22, PDF 1633]

### 3. Lateral control
**3.1 PF**
- Apply some rudder to turn and wait for the aircraft reaction — rudder induces a significant roll with a slight delay [FCTM AOP-10-30-20 P 2/2, PDF 63]
- To stabilize and level the wings, anticipate by releasing the rudder pedals [FCTM AOP-10-30-20 P 2/2, PDF 63]

### 4. Restore
**4.1 PM**
- Restore the lost systems with the ECAM / QRH procedures of the failure that caused the mechanical backup [FCTM AOP-10-30-20 P 2/2, PDF 63; FCTM AOP-30-30 P 1/6, PDF 82]
**4.2 PF**
- Fly, navigate, communicate in this order [FCTM AOP-40 P 1/4, PDF 96]

## 4. Procedure
## 7. FCTM technique
- The objective is not to fly the aircraft accurately, but to maintain the aircraft attitude safe and stabilized, in order to allow the restoration of lost systems. [FCTM AOP-10-30-20 P 2/2, PDF 63]
- Pitch: pitch trim wheel, applied smoothly — the THS effect is significant due to its large size. [FCTM AOP-10-30-20 P 2/2, PDF 63]
- Lateral: rudder gives a significant roll with a slight delay. Apply some rudder to turn and wait; release the pedals early to stabilize and level the wings. [FCTM AOP-10-30-20 P 2/2, PDF 63]

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- There is no ECAM or QRH procedure titled mechanical backup in the supplied manuals; the brief uses FCOM DSC-27 and FCTM AOP-10-30-20 only. [FCOM DSC-27-20-20 P 18/20, PDF 1629; FCTM AOP-10-30-20 P 2/2, PDF 63]
- No PDP slide covers mechanical-backup handling, and no callouts or thrust technique are given for it. [FCTM AOP-10-30-20 P 2/2, PDF 63]
- Which ECAM alerts accompany the mechanical backup depends on the causing failure (electrical, fly-by-wire computers, elevators); those procedures are not reproduced here. [FCOM DSC-27-20-20 P 18/20, PDF 1629]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | DSC-27-20-20 — reconfiguration, mechanical back-up | P 1/20, 18–19/20 | 1612, 1629–1630 | 18 FEB 26 |
| FCOM | DSC-27-10-20 / DSC-27-20-30 — THS mechanical control, rudder, pitch trim wheel | P 3/16, 13/16 · P 2/22 | 1568, 1578, 1633 | 18 FEB 26 |
| FCOM | DSC-22_30-80-20 — FMA MAN PITCH TRIM ONLY | P 26/36 | 1251 | 26 MAY 26 |
| FCTM | AOP-10-30-20 — mechanical backup | P 2/2 | 63 | 25 FEB 25 |
