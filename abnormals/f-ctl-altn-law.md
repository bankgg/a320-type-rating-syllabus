# F/CTL ALTN LAW — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** HS-TXA..TXF, HS-TXG..TXU — Two FCOM units (HS-TXA..TXF, HS-TXG..TXU) with identical procedure and STATUS. The law reconfiguration after FAC / yaw damper failures differs (see HS-TX differences).

An amber caution: the flight controls are in alternate law (PROT LOST). Pitch handling stays like normal law, but all protections except the maneuver (load factor) protection are lost. Respect MAX SPEED 320 kt and maneuver with care; if an elevator has failed, do not use the speed brakes. Land in CONF 3 at VREF + 10 kt; when the gear goes down (and the AP is off) the law becomes DIRECT, so trim manually.

## 1. What it is
- **Trigger:** This alert triggers when alternate laws are active. Inhibited in flight phases 4, 5, 7 and 8. [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- **Flight phase inhibition:** phases 4, 5, 7, 8 [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- Three levels of reconfiguration: alternate law (with or without reduced protections), direct law, mechanical. The ECAM and PFD indicate any control law degradation. [FCOM DSC-27-20-20 P 1/20, PDF 1612]
- In flight, pitch alternate law is based on load factor demand; the basic high speed protection, pitch attitude protection and angle-of-attack protection are not available. [FCOM DSC-27-20-20 P 11/20, PDF 1622; FCOM DSC-27-20-20 P 14/20, PDF 1625]
- Alternate law without reduced protection: identical to alternate law but without the low-speed or high-speed stability — only the load factor limitation remains. [FCOM DSC-27-20-20 P 17/20, PDF 1628]
- Low energy aural alert is lost in alternate law. [PDP Reconfiguration laws, PDF 514]
- The AP disconnects if the speed exceeds VMO/MMO or the bank angle exceeds 45°. [FCOM DSC-27-20-20 P 13/20, PDF 1624; FCOM DSC-27-20-20 P 16/20, PDF 1627]
- If the aircraft goes far outside the normal envelope, the abnormal attitude law engages (F/CTL DIRECT LAW on ECAM); after recovery, alternate law without reduced protection remains for the rest of the flight (F/CTL ALTN LAW on ECAM). [FCOM DSC-27-20-20 P 18/20, PDF 1629]

## 2. Key limits
- **MAX SPEED:** 320 KT (320/.77 if dual HYD LO PR) [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- **SPD BRK:** DO NOT USE if L or R elevator fails [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- **FOR LDG:** FLAP LVR 3 [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- **APPR SPD:** VREF + 10 KT [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- **Law at L/G DN:** DIRECT (with AP: when L/G DN and AP OFF) [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- PFD: amber X replace the green = protection symbols; the speed scale shows the black/red barber pole (stall warning) [FCOM DSC-27-20-20 P 1/20, PDF 1612; FCOM DSC-27-20-20 P 12/20, PDF 1623; PDP Reconfiguration laws, PDF 512]
**1.2 PM**
- “F/CTL ALTN LAW” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; PDP Management of abnormal operations, PDF 424]
- Confirm on the F/CTL SD page and the PFD before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- (PROT LOST) …… — [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- Always respect stall warnings when applying the TAWS alerts procedures [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- MAX SPEED …… 320 KT [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- 320/.77 if dual hydraulic system low pressure [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- MANEUVER WITH CARE …… — [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- Displayed depending on the failure [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- **If L or R elevator fails** [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
  - SPD BRK …… DO NOT USE [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
**2.2 PF**
- Respect MAX SPEED; at high speed maneuver with care using small control inputs [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484; FCTM AOP-10-30-20 P 1/2, PDF 62]
- At high altitude, descend to increase the buffet margin (about 4 000 ft below REC MAX ALT) [FCTM AOP-10-30-20 P 1/2, PDF 62]
- Outside the normal flight envelope there is no protection: take the preventive actions of any non-protected aircraft [FCTM AOP-10-30-20 P 1/2, PDF 62]

### 3. STATUS
**3.1 PM**
- “CLEAR FLIGHT CONTROL ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR FLIGHT CONTROL” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**3.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 4. Approach and landing
**4.1 PF**
- Brief: CONF 3 landing at VREF + 10 kt, landing distance with the LDG DIST PROC, law change to DIRECT at gear extension [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
**4.2 PM**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
**4.3 PF**
- **If AP engaged** [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
  - DIRECT LAW when L/G DN and AP OFF [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- **If no AP engaged** [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
  - DIRECT LAW when L/G DN [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- In direct law USE MAN PITCH TRIM is displayed: trim manually with the pitch trim wheel [FCOM DSC-27-20-20 P 17/20, PDF 1628; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492]
- In pitch alternate law the flight mode changes to flare mode (direct stick-to-elevator) when the gear is selected down [FCOM DSC-27-20-20 P 12/20, PDF 1623; FCOM DSC-27-20-20 P 15/20, PDF 1626]

## 4. Procedure
### F/CTL ALTN LAW (FCOM PRO-ABN-F_CTL (HS-TXA..TXF and HS-TXG..TXU, identical))
- *Refer to Reconfiguration Control Laws for flight characteristics. Depending on the failure, the AP may be available.* [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- *(PROT LOST)* [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- *All protections, except maneuver protections, are lost. Depending on the failure, static stability may be introduced.* [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- *Always respect stall warnings when applying the TAWS alerts procedures.* [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- MAX SPEED …… 320 KT — Maximum speed is 320/.77 if dual hydraulic system low pressure. This line is inhibited if DBUS is in use. [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- MANEUVER WITH CARE …… — — This line can be displayed depending on the failure. [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- **If L or R elevator fails:** [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
  - SPD BRK …… DO NOT USE [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]

## 5. STATUS
**Limitations**
- If dual hydraulic system low pressure: MAX SPEED …… 320/.77 [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- In all other cases: MAX SPEED …… 320 KT [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- If L or R elevator fault: SPD BRK …… DO NOT USE [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
**Information**
- ALTN LAW : PROT LOST [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- If AP engaged: WHEN L/G DN AND AP OFF : DIRECT LAW [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- If no AP engaged: WHEN L/G DN : DIRECT LAW [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- At landing gear extension, flight control reverts to direct law in both pitch and roll (depending on aircraft configuration, the control remains in alternate law in the case of yaw damper loss or both FACs failure). [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 — Replaced by "FOR LDG: FLAP LVR 3" when CONF 3 is selected, as a reminder. [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- GPWS LDG FLAP 3 …… ON [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- APPR SPD …… VREF + 10 KT [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
**INOP SYS**
- F/CTL PROT [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]
- STEEP APPR [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 12/132, PDF 3485]

## 6. QRH and reference tables
### Alternate law — what remains 
FCOM DSC-27 alternate law with reduced protections.

| Function | In alternate law |
|---|---|
| Pitch (flight mode) | Load factor demand, like normal law |
| Load factor limitation | Available (as normal law) |
| Pitch attitude protection | None — amber X on PFD |
| Low speed | Low speed stability (nose-down demand) replaces AoA protection; stall warning; α floor inoperative |
| High speed | High speed stability above VMO/MMO (can be overridden); overspeed warning available |
| Roll | Direct law |
| Yaw | Alternate: yaw damping only (±5° rudder) |
| Flare (L/G down) | Direct stick-to-elevator |
[FCOM DSC-27-20-20 P 11/20, PDF 1622; FCOM DSC-27-20-20 P 12/20, PDF 1623; FCOM DSC-27-20-20 P 13/20, PDF 1624; FCOM DSC-27-20-20 P 14/20, PDF 1625; FCOM DSC-27-20-20 P 15/20, PDF 1626; FCOM DSC-27-20-20 P 16/20, PDF 1627]

## 7. FCTM technique
- Within the normal flight envelope, alternate-law handling in pitch is identical to normal law. Outside it, the PF must take appropriate preventive actions to avoid losing control or high speed excursions. [FCTM AOP-10-30-20 P 1/2, PDF 62]
- At high altitude, descend about 4 000 ft below REC MAX ALT to reduce stall warnings in turbulence. At high speed, maneuver with care using small inputs. [FCTM AOP-10-30-20 P 1/2, PDF 62]
- Protections are not structural limits; the PF must not deliberately exceed the normal flight envelope. [FCTM AOP-10-30-10 P 1/2, PDF 60]
- Direct law: be careful with large thrust changes or sudden speedbrake movements, particularly with an aft CG. Retract speedbrakes gently to give time to re-trim. At go-around, TOGA thrust gives a large pitch-up moment — apply nose-down trim to avoid excessive pitch-up or a transient stall warning. [FCTM AOP-10-30-20 P 1/2, PDF 62]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| F/CTL DIRECT LAW | Active from landing gear extension (with AP: when L/G down and AP off). | MAN PITCH TRIM USE; MAX SPEED 320/.77; Maneuver and use speed brakes with care | [FCOM PRO-ABN-F_CTL P 10/132, PDF 3483; FCOM PRO-ABN-F_CTL P 19/132, PDF 3492] |

## 9. HS-TX differences
| Topic | HS-TXA..TXF | HS-TXG..TXU | Ref |
|---|---|---|---|
| 2 FAC, yaw damper, FAC 1 + HYD Y or FAC 2 + HYD G failure | Pitch ALTN (reduced protection), roll DIRECT, yaw MECH | Pitch and roll stay NORM, yaw MECH; ALTN LAW is indicated; no reversion to DIRECT LAW at L/G extension | [FCOM DSC-27-20-20 P 2/20, PDF 1613; FCOM DSC-27-20-20 P 4/20, PDF 1615] |
| Bank angle above 45° in alternate law | BANK BANK message on both PFDs and "BANK BANK" aural alert | HS-TXN..TXU: as HS-TXA..TXF. HS-TXG..TXM: bank angle protection not provided (no BANK BANK alert described) | [FCOM DSC-27-20-20 P 13/20, PDF 1624; FCOM DSC-27-20-20 P 16/20, PDF 1627; FCOM DSC-31-40 P 50/54, PDF 1941] |

## 10. Gaps and omissions
- The two FCOM procedure units differ only by effectivity; their visible content (lines, STATUS, inhibition) is identical. [FCOM PRO-ABN-F_CTL P 9/132, PDF 3482; FCOM PRO-ABN-F_CTL P 11/132, PDF 3484]
- The bank-angle alert splits the fleet differently (HS-TXA..TXF, HS-TXN..TXU vs HS-TXG..TXM) from the procedure units. [FCOM DSC-27-20-20 P 13/20, PDF 1624; FCOM DSC-27-20-20 P 16/20, PDF 1627; FCOM DSC-31-40 P 50/54, PDF 1941]
- No FCTM abnormal-procedure chapter or PDP task-sharing module is specific to F/CTL ALTN LAW; the flow uses the generic ECAM handling, the FCTM reconfiguration-law technique and the PDP law slides. [FCTM AOP-10-30-20 P 1/2, PDF 62; PDP Reconfiguration laws, PDF 512]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-F_CTL — F/CTL ALTN LAW (HS-TXA..TXF; HS-TXG..TXU) | P 9–12/132 | 3482–3485 | 26 MAY 26 |
| FCOM | DSC-27-20-20 — reconfiguration control laws | P 1–5/20, 11–18/20 | 1612–1616, 1622–1629 | 18 FEB 26 |
| FCTM | AOP-10-30 — fly-by-wire, flying in reconfiguration laws | AOP-10-30-10 P 1/2, AOP-10-30-20 P 1/2 | 60, 62 | 25 FEB 25 |
| PDP | Reconfiguration laws (EFTDN1RCFGLAW01) | Flight control laws, alternate, direct | 512–515 | OCT 2018 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30-30 P 1–4/6 | 68–69, 82–85 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS | 424–426 | JAN 2024 |
