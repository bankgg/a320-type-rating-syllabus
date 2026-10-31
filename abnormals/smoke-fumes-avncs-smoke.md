# SMOKE / FUMES / AVNCS SMOKE — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**QRH procedure · red LAND ASAP · no memory items**  
**Applicability:** HS-TXA..TXO, HS-TXP..TXU — The QRH lines are the same for all HS-TX. Only the FCOM STATUS after a smoke ELEC EMER CONFIG differs slightly.

Time is critical: red LAND ASAP, and be prepared to divert immediately. Immediate actions protect the crew, stop further contamination and open communication with the cabin. If the source is not immediately isolated, start the diversion and the descent to FL 100 / MEA-MORA. Then identify the source: air conditioning, cabin equipment, or avionics/electrical. At any time after the immediate actions, consider REMOVAL OF SMOKE / FUMES, ELEC EMER CONFIG or an immediate landing.

## 1. What it is
- **Trigger:** Flight or cabin crew suspect smoke/fumes from the avionics, the air conditioning or the cabin equipment; the AVIONICS SMOKE alert triggers; or there is a smell of smoke/fumes in the cockpit. For another ECAM SMOKE alert (cargo, lavatory), apply the ECAM first. [FCOM PRO-ABN-SMOKE P 1/50, PDF 3958; FCTM PR-AEP-SMOKE P 1/10, PDF 498; PDP Smoke, PDF 536]
- **Flight phase inhibition:** none [FCOM PRO-ABN-SMOKE P 1/50, PDF 3958; FCTM PR-AEP-SMOKE P 1/10, PDF 498; PDP Smoke, PDF 536]
- This procedure includes all the steps of the AVIONICS SMOKE procedure. [FCOM PRO-ABN-SMOKE P 1/50, PDF 3958; PDP Smoke, PDF 536]
- The immediate actions are common to all cases of smoke or fumes, whatever the source. Their objectives are flight crew protection, avoiding further contamination of the cockpit/cabin, and communication with the cabin crew. [FCTM PR-AEP-SMOKE P 5/10, PDF 502; PDP Smoke, PDF 537]
- A diversion may be avoided if the source is obvious, accessible and extinguishable, or confirmed isolated after the immediate actions. [FCOM PRO-ABN-SMOKE P 1/50, PDF 3958]
- Guidelines for the source: smoke/fumes first from the ventilation outlets, or detected in the cabin, suggest air conditioning, and several SMOKE alerts will follow shortly (apply the ECAM procedures). After an ENG or APU failure they may come through the bleed system and recirculate until they disappear. Only the AVIONICS SMOKE alert suggests avionics. Smoke while an equipment is declared faulty suggests that equipment. [FCOM PRO-ABN-SMOKE P 3/50, PDF 3960; FCTM PR-AEP-SMOKE P 6/10, PDF 503; FCTM PR-AEP-SMOKE P 7/10, PDF 504]
- A smell of smoke/fumes similar to orange peels: suspect a toxic leak of rain repellent fluid. Similar to pine needles: suspect a non-toxic leak. [FCOM PRO-ABN-SMOKE P 1/50, PDF 3958]
- With VENTILATION BLOWER and EXTRACT both in OVRD, a single pack may not be able to maintain the cabin pressure. Restore normal configuration if PACK 2 is not suspected to cause smoke/fumes. [FCOM PRO-ABN-SMOKE P 4/50, PDF 3961]
- CARGO AFT ISOL VALVE OFF prevents a cargo smoke warning from being triggered by cabin smoke. [FCOM PRO-ABN-SMOKE P 4/50, PDF 3961]
- Partial shedding was removed from the procedure: shedding one side and then the other with a battery charging leaves DC 1, DC 2 and the BAT bus bars inoperative for the rest of the flight. Full ELEC EMER CONFIG lets the crew recover the normal electrical configuration for landing, particularly normal braking. [FCTM PR-AEP-SMOKE P 7/10, PDF 504]
- EMER ELEC GEN 1 LINE OFF opens the GEN 1 line contactor: GEN 1 keeps running and supplies one fuel pump in each wing tank, and AC BUS 1 is supplied by GEN 2 through the bus tie contactor. [FCOM PRO-ABN-SMOKE P 6/50, PDF 3963]

## 2. Key limits
- **Landing:** LAND ASAP (red) [QRH 27.01B, PDF 245]
- **Descent if not isolated:** FL 100 / MEA-MORA [QRH 27.01B, PDF 245]
- **Smoke gone within:** 5 min: restore normal ventilation [QRH 27.01D, PDF 247]
- **Generators restored:** 3 min or 2 000 ft AAL before landing [QRH 27.01E, PDF 248]

## 3. Flow (PF / PM)
### 1. Order
**1.1 PF + PM**
- Smoke or fumes perceptible: confirmed visually or by smell [FCTM PR-AEP-SMOKE P 1/10, PDF 498; PDP Smoke, PDF 535]
- No ECAM alert: refer directly to this procedure. AVIONICS SMOKE: refer to it directly, or apply the ECAM first. Other ECAM SMOKE alert: apply the ECAM, then this procedure if in doubt about the origin [FCTM PR-AEP-SMOKE P 1/10, PDF 498; PDP Smoke, PDF 535; PDP Smoke, PDF 536]
**1.2 PF**
- “SMOKE / FUMES / AVNCS SMOKE PROCEDURE” [PDP Management of abnormal operations, PDF 427]
- Red LAND ASAP: anticipate the diversion, time is critical [QRH 27.01B, PDF 245; FCTM PR-AEP-SMOKE P 4/10, PDF 501; PDP Smoke, PDF 537]
**1.3 PM**
- READ AND DO the QRH lines aloud [PDP Management of abnormal operations, PDF 427; FCTM AOP-30-30 P 5/6, PDF 86]

### 2. Immediate actions
**2.1 PF + PM**
- CREW OXY MASKS (if required) …… USE/100%/EMERG [QRH 27.01B, PDF 245]
- If required, or if not sure, all flight crew must don the mask. Establish crew communication; turn the emergency knob to clear condensation or smoke from the mask [FCTM PR-AEP-SMOKE P 6/10, PDF 503; FCOM PRO-ABN-SMOKE P 2/50, PDF 3959]
**2.2 PM**
- VENTILATION BLOWER …… OVRD [QRH 27.01B, PDF 245]
- VENTILATION EXTRACT …… OVRD [QRH 27.01B, PDF 245]
- Avionics ventilation air is extracted overboard [FCOM PRO-ABN-SMOKE P 2/50, PDF 3959]
- CAB FANS …… OFF [QRH 27.01B, PDF 245]
- Prevents smoke/fumes from entering the cockpit and cabin [FCOM PRO-ABN-SMOKE P 2/50, PDF 3959]
- GALY & CAB …… OFF [QRH 27.01B, PDF 245]
- SIGNS …… ON [QRH 27.01B, PDF 245]
**2.3 PF**
- CKPT / CAB COM …… ESTABLISH [QRH 27.01B, PDF 245]
- The cabin crew estimate and report the density of the smoke/fumes and the severity of the situation [FCTM PR-AEP-SMOKE P 2/10, PDF 499; FCOM PRO-ABN-SMOKE P 2/50, PDF 3959]

### 3. Isolate or divert
**3.1 PM**
- **If smoke/fumes source immediately obvious, accessible, and extinguishable** [QRH 27.01B, PDF 245]
  - FAULTY EQPT …… ISOLATE [QRH 27.01B, PDF 245]
**3.2 PF**
- **If smoke/fumes source not immediately isolated** [QRH 27.01B, PDF 245]
  - DIVERSION …… INITIATE [QRH 27.01B, PDF 245]
  - DESCENT TO FL 100 / MEA-MORA …… INITIATE [QRH 27.01B, PDF 245]
  - Initiate the diversion before entering the identification part of the procedure [FCTM PR-AEP-SMOKE P 5/10, PDF 502]

### 4. At any time after the immediate actions
**4.1 PF + PM**
- **If smoke/fumes become the GREATEST THREAT** [QRH 27.01B, PDF 245]
  - REMOVAL OF SMOKE / FUMES …… CONSIDER [QRH 27.01B, PDF 245]
  - ELEC EMER CONFIG …… CONSIDER [QRH 27.01C, PDF 246]
  - See the REMOVAL OF SMOKE / FUMES brief, and TO SET ELEC EMER CONFIG below [QRH 27.01B, PDF 245; QRH 27.01C, PDF 246; PDP Smoke, PDF 539; PDP Smoke, PDF 540]
- **If situation becomes UNMANAGEABLE** [QRH 27.01C, PDF 246]
  - IMMEDIATE LANDING …… CONSIDER [QRH 27.01C, PDF 246]
  - The Captain can consider an overweight landing, a tailwind landing, a ditching, a forced landing, etc. [FCOM PRO-ABN-SMOKE P 2/50, PDF 3959]

### 5. Identify and fight the source
**5.1 PM**
- **If AIR COND smoke/fumes suspected** [QRH 27.01C, PDF 246]
  - APU BLEED …… OFF [QRH 27.01C, PDF 246]
  - VENTILATION BLOWER …… AUTO [QRH 27.01C, PDF 246]
  - VENTILATION EXTRACT …… AUTO [QRH 27.01C, PDF 246]
  - CARGO AFT ISOL VALVE …… OFF [QRH 27.01C, PDF 246]
  - PACK 1 …… OFF [QRH 27.01C, PDF 246]
  - **If smoke/fumes continue** [QRH 27.01C, PDF 246]
    - PACK 1 …… ON [QRH 27.01C, PDF 246]
    - PACK 2 …… OFF [QRH 27.01C, PDF 246]
    - **If smoke/fumes persist** [QRH 27.01C, PDF 246]
      - PACK 2 …… ON [QRH 27.01C, PDF 246]
      - VENTILATION BLOWER …… OVRD [QRH 27.01C, PDF 246]
      - VENTILATION EXTRACT …… OVRD [QRH 27.01C, PDF 246]
  - REMOVAL OF SMOKE / FUMES …… CONSIDER [QRH 27.01C, PDF 246]
- **If CABIN EQPT smoke/fumes suspected** [QRH 27.01C, PDF 246]
  - **If smoke/fumes continue** [QRH 27.01C, PDF 246]
    - EMER EXIT LIGHT …… ON [QRH 27.01C, PDF 246]
    - COMMERCIAL …… OFF [QRH 27.01C, PDF 246]
    - SMOKE / FUMES DISSIPATION …… CHECK [QRH 27.01D, PDF 247]
    - FAULTY EQPT …… SEARCH / ISOLATE [QRH 27.01D, PDF 247]
    - **If smoke/fumes persist or when faulty equipment confirmed isolated** [QRH 27.01D, PDF 247]
      - COMMERCIAL …… NORM [QRH 27.01D, PDF 247]
    - REMOVAL OF SMOKE / FUMES …… CONSIDER [QRH 27.01D, PDF 247]
- **If smoke/fumes source cannot be determined and persist or AVNCS / ELECTRICAL smoke/fumes suspected** [QRH 27.01D, PDF 247]
  - ELEC EMER CONFIG …… CONSIDER [QRH 27.01D, PDF 247]
  - Also enter this paragraph if the source is not identified, or if the air conditioning or cabin equipment paragraphs were unsuccessful [FCTM PR-AEP-SMOKE P 7/10, PDF 504]
- **If smoke/fumes disappear within 5 minutes** [QRH 27.01D, PDF 247]
  - NORMAL VENTILATION …… RESTORE [QRH 27.01D, PDF 247]

### 6. To set ELEC EMER CONFIG
**6.1 PF**
- Decide to set it: shed as much equipment as possible to try to isolate the source [FCTM PR-AEP-SMOKE P 7/10, PDF 504; PDP Smoke, PDF 540]
**6.2 PM**
- Read the QRH line and point to the guarded control [QRH 27.01D, PDF 247; FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**6.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the control the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**6.4 PM**
- EMER ELEC GEN 1 LINE …… OFF [QRH 27.01D, PDF 247]
- EMER ELEC PWR …… MAN ON [QRH 27.01D, PDF 247]
- **When EMER GEN AVAIL** [QRH 27.01D, PDF 247]
  - APU GEN …… OFF [QRH 27.01D, PDF 247]
  - GEN 2 …… OFF [QRH 27.01D, PDF 247]
  - APPLY ELEC EMER CONFIG PROCEDURE, BUT DO NOT RESET GEN, EVEN IF REQUESTED BY ECAM [QRH 27.01D, PDF 247]
- If AVIONICS SMOKE was triggered first, the ECAM shows its specific ELEC EMER CONFIG procedure instead. See the ELEC EMER CONFIG brief for handling the ECAM and its STATUS [FCOM PRO-ABN-SMOKE P 6/50, PDF 3963; FCTM PR-AEP-SMOKE P 8/10, PDF 505]

### 7. Before landing
**7.1 PM**
- **At 3 min or 2 000 ft AAL before landing** [QRH 27.01E, PDF 248]
  - GEN 2 …… ON [QRH 27.01E, PDF 248]
  - EMER ELEC GEN 1 LINE …… ON [QRH 27.01E, PDF 248]
  - Restored this late to recover normal braking while minimizing possible reactivation of a smoke source [FCOM PRO-ABN-SMOKE P 6/50, PDF 3963]
- **When aircraft stopped** [QRH 27.01E, PDF 248]
  - ALL GENs …… OFF [QRH 27.01E, PDF 248]
- “SMOKE / FUMES / AVNCS SMOKE PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

## 4. Procedure
### SMOKE / FUMES / AVNCS SMOKE (QRH 27.01B–E) (QRH 27.01B–E)
- **LAND ASAP (red)** [QRH 27.01B, PDF 245]
- **IF PERCEPTIBLE SMOKE / FUMES APPLY IMMEDIATELY:** [QRH 27.01B, PDF 245]
- CREW OXY MASKS (if required) …… USE/100%/EMERG [QRH 27.01B, PDF 245]
- VENTILATION BLOWER …… OVRD [QRH 27.01B, PDF 245]
- VENTILATION EXTRACT …… OVRD [QRH 27.01B, PDF 245]
- CAB FANS …… OFF [QRH 27.01B, PDF 245]
- GALY & CAB …… OFF [QRH 27.01B, PDF 245]
- SIGNS …… ON [QRH 27.01B, PDF 245]
- CKPT / CAB COM …… ESTABLISH [QRH 27.01B, PDF 245]
- **If smoke/fumes source immediately obvious, accessible, and extinguishable:** [QRH 27.01B, PDF 245]
  - FAULTY EQPT …… ISOLATE [QRH 27.01B, PDF 245]
- **If smoke/fumes source not immediately isolated:** [QRH 27.01B, PDF 245]
  - DIVERSION …… INITIATE [QRH 27.01B, PDF 245]
  - DESCENT TO FL 100 / MEA-MORA …… INITIATE [QRH 27.01B, PDF 245]
- **At ANY TIME of the procedure, if SMOKE / FUMES become the GREATEST THREAT:** [QRH 27.01B, PDF 245]
  - REMOVAL OF SMOKE / FUMES …… CONSIDER — Refer to ABN-27 Removal of Smoke / Fumes [QRH 27.01B, PDF 245]
  - ELEC EMER CONFIG …… CONSIDER — Refer to the end of the procedure to set ELEC EMER CONFIG. [QRH 27.01C, PDF 246]
- **At ANY TIME of the procedure, if situation becomes UNMANAGEABLE:** [QRH 27.01C, PDF 246]
  - IMMEDIATE LANDING …… CONSIDER [QRH 27.01C, PDF 246]
- **If AIR COND smoke/fumes suspected:** [QRH 27.01C, PDF 246]
  - APU BLEED …… OFF [QRH 27.01C, PDF 246]
  - VENTILATION BLOWER …… AUTO [QRH 27.01C, PDF 246]
  - VENTILATION EXTRACT …… AUTO [QRH 27.01C, PDF 246]
  - CARGO AFT ISOL VALVE …… OFF [QRH 27.01C, PDF 246]
  - PACK 1 …… OFF [QRH 27.01C, PDF 246]
  - **If smoke/fumes continue:** [QRH 27.01C, PDF 246]
    - PACK 1 …… ON [QRH 27.01C, PDF 246]
    - PACK 2 …… OFF [QRH 27.01C, PDF 246]
    - **If smoke/fumes persist:** [QRH 27.01C, PDF 246]
      - PACK 2 …… ON [QRH 27.01C, PDF 246]
      - VENTILATION BLOWER …… OVRD [QRH 27.01C, PDF 246]
      - VENTILATION EXTRACT …… OVRD [QRH 27.01C, PDF 246]
  - REMOVAL OF SMOKE / FUMES …… CONSIDER — Refer to ABN-27 Removal of Smoke / Fumes [QRH 27.01C, PDF 246]
- **If CABIN EQPT smoke/fumes suspected:** [QRH 27.01C, PDF 246]
  - **If smoke/fumes continue:** [QRH 27.01C, PDF 246]
    - EMER EXIT LIGHT …… ON [QRH 27.01C, PDF 246]
    - COMMERCIAL …… OFF [QRH 27.01C, PDF 246]
    - SMOKE / FUMES DISSIPATION …… CHECK [QRH 27.01D, PDF 247]
    - FAULTY EQPT …… SEARCH / ISOLATE [QRH 27.01D, PDF 247]
    - **If smoke/fumes persist or when faulty equipment confirmed isolated:** [QRH 27.01D, PDF 247]
      - COMMERCIAL …… NORM [QRH 27.01D, PDF 247]
    - REMOVAL OF SMOKE / FUMES …… CONSIDER — Refer to ABN-27 Removal of Smoke / Fumes [QRH 27.01D, PDF 247]
- **If smoke/fumes source cannot be determined and persist or AVNCS / ELECTRICAL smoke/fumes suspected:** [QRH 27.01D, PDF 247]
  - ELEC EMER CONFIG …… CONSIDER — Refer to the end of the procedure to set ELEC EMER CONFIG. [QRH 27.01D, PDF 247]
- **If smoke/fumes disappear within 5 minutes:** [QRH 27.01D, PDF 247]
  - NORMAL VENTILATION …… RESTORE [QRH 27.01D, PDF 247]

### TO SET ELEC EMER CONFIG (QRH 27.01D–E)
- EMER ELEC GEN 1 LINE …… OFF [QRH 27.01D, PDF 247]
- EMER ELEC PWR …… MAN ON [QRH 27.01D, PDF 247]
- **When EMER GEN AVAIL:** [QRH 27.01D, PDF 247]
  - APU GEN …… OFF [QRH 27.01D, PDF 247]
  - GEN 2 …… OFF [QRH 27.01D, PDF 247]
  - *APPLY ELEC EMER CONFIG PROCEDURE, BUT DO NOT RESET GEN, EVEN IF REQUESTED BY ECAM.* [QRH 27.01D, PDF 247]
  - **At 3 min or 2 000 ft AAL before landing:** [QRH 27.01E, PDF 248]
    - GEN 2 …… ON [QRH 27.01E, PDF 248]
    - EMER ELEC GEN 1 LINE …… ON [QRH 27.01E, PDF 248]
  - **When aircraft stopped:** [QRH 27.01E, PDF 248]
    - ALL GENs …… OFF [QRH 27.01E, PDF 248]

## 6. QRH and reference tables
### Fumes with odors and suspected causes 
Most reported cause listed first.

| Odor | Suspected cause |
|---|---|
| Acrid | Electrical equipment/IFE; engine oil leak |
| Burning | Electrical equipment; galley equipment; bird ingestion |
| Chemical | Contaminated bleed ducts; APU ingestion |
| Chlorine | Smoke hood; blocked door area drain |
| Electrical | Electrical equipment |
| Dirty socks | APU or engine oil leaks |
| Foul | Lavatories |
| Fuel | APU FCU/fuel line |
| Oil | Engine or APU oil leak |
| Skydrol | Engine hydraulic |
| Sulphur | Wiring; avionics filter water contamination; light bulb |
[FCTM PR-AEP-SMOKE P 7/10, PDF 504]

## 7. FCTM technique
- An immediate diversion should be considered as soon as smoke/fumes are detected. If the source is not immediately obvious, accessible and extinguishable, initiate it without delay. [FCTM PR-AEP-SMOKE P 1/10, PDF 498]
- The boxed items may be applied at any time in the procedure, but not before the immediate actions. After the first steps of REMOVAL OF SMOKE / FUMES, come back here for the suspected source while descending to FL 100; reaching FL 100, complete REMOVAL OF SMOKE / FUMES. [FCTM PR-AEP-SMOKE P 8/10, PDF 505; PDP Smoke, PDF 539]
- Remain in ELEC EMER CONFIG until a late stage, and restore some generation a few minutes before landing. [PDP Smoke, PDF 540; FCTM PR-AEP-SMOKE P 8/10, PDF 505]
- Coordination with the cabin crew is a key element. [FCTM PR-AEP-SMOKE P 2/10, PDF 499]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| REMOVAL OF SMOKE / FUMES | Boxed item: when smoke/fumes become the greatest threat. | See the REMOVAL OF SMOKE / FUMES brief | [QRH 27.01B, PDF 245] |
| ELEC EMER CONFIG | Boxed item, and the AVNCS / ELECTRICAL or unknown-source paragraph. | See the ELEC EMER CONFIG brief; Do not reset the generators, even if requested by ECAM | [QRH 27.01D, PDF 247; FCOM PRO-ABN-SMOKE P 6/50, PDF 3963; FCOM PRO-ABN-SMOKE P 8/50, PDF 3965] |
| SMOKE AFT CARGO SMOKE | Other ECAM SMOKE alerts: apply the ECAM procedure first. | See the SMOKE AFT CARGO SMOKE brief | [FCOM PRO-ABN-SMOKE P 1/50, PDF 3958; FCTM PR-AEP-SMOKE P 1/10, PDF 498] |

## 9. HS-TX differences
| Topic | HS-TXA..TXO | HS-TXP..TXU | Ref |
|---|---|---|---|
| FCOM STATUS after a smoke ELEC EMER CONFIG | Lists CTR TK FUEL UNUSABLE; ENG 1+2 N1 DEGRADED MODE marked "IAE-powered aircraft" | No CTR TK FUEL UNUSABLE line; no IAE marking | [FCOM PRO-ABN-SMOKE P 8/50, PDF 3965; FCOM PRO-ABN-SMOKE P 17/50, PDF 3974] |

## 10. Gaps and omissions
- The QRH line "CKPT / CAB COM" names no pilot; the PF is shown because the PF communicates, confirmed by the user. The PM is shown for the panel lines as read & do. [QRH 27.01B, PDF 245; FCTM AOP-20 P 1–2/10, PDF 68]
- The HS-TO-only version (QRH 27.01A, FCOM P 19–27/50) is excluded, including its PACK (AFFECTED SIDE) line. [QRH 27.01A, PDF 244; FCOM PRO-ABN-SMOKE P 19/50, PDF 3976]
- The manuals have no paragraph specific to smoke in the aft cabin. Cabin smoke is treated by the suspected source, confirmed by the user: FCTM says smoke/fumes detected in the cabin may suggest AIR COND, otherwise CABIN EQPT. [FCTM PR-AEP-SMOKE P 6/10, PDF 503; QRH 27.01C, PDF 246]
- FCOM and QRH line wording differs slightly (OXY MASK / GOGGLE, CKPT / CABIN COM, "within 5 min"). The brief quotes the QRH. [FCOM PRO-ABN-SMOKE P 2/50, PDF 3959; QRH 27.01B, PDF 245]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| QRH | 27.01 SMOKE / FUMES / AVNCS SMOKE | 27.01B–E | 245–248 | 14 JUL 26 |
| FCOM | PRO-ABN-SMOKE — [QRH] SMOKE / FUMES / AVNCS SMOKE | P 1–18/50 | 3958–3975 | 14 JUL 26 |
| FCTM | PR-AEP-SMOKE — smoke/fumes procedure | P 1–8/10 | 498–505 | 24 NOV 25 |
| PDP | Smoke (XFTDA1SMOKE0001) | ECAM alerts, immediate actions, procedure | 534–540 | JAN 2024 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
