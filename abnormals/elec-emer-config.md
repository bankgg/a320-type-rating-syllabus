# ELEC EMER CONFIG — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Red warning · red LAND ASAP · no memory items · QRH summary**  
**Applicability:** HS-TXA..TXO, HS-TXP..TXU — Procedure lines identical; STATUS INOP SYS and centre-tank fuel differ.

Both AC main buses are lost. The RAT drives the emergency generator, leaving essentially CM1 instruments, VHF1/HF1/ATC1 and alternate law (direct law with gear down). CM1 flies manually as PF while the PM works the ECAM; after STATUS the crew uses the QRH summary to decide, prepare and fly the approach at no less than 140 kt.

## 1. What it is
- **Trigger:** AC BUS 1 and AC BUS 2 are not supplied. [FCOM PRO-ABN-ELEC P 90/122, PDF 3215]
- **Flight phase inhibition:** phases 4, 8 [FCOM PRO-ABN-ELEC P 90/122, PDF 3215]
- RAT extends automatically when AC BUS 1 and 2 are lost above 100 kt; blue hydraulics drive the EMER GEN, which supplies AC ESS and (via ESS TR) DC ESS. [FCOM DSC-24-10-30-30 P 4/10, PDF 1455; FCTM PR-AEP-ELEC P 1/2, PDF 400]
- If the RAT stalls, the network transfers to the batteries and static inverter, and AC/DC SHED ESS are shed. On ground: DC BAT BUS connected below 100 kt; AC ESS shed below 50 kt (all displays lost). [FCOM DSC-24-10-30-30 P 4/10, PDF 1455; FCTM PR-AEP-ELEC P 1/2, PDF 400]
- EMER ELEC PWR MAN ON (guarded): manual RAT extension; EMER GEN couples 3 s after the RAT supplies it. Red FAULT light: EMER GEN not supplying power. [FCOM DSC-24-20 P 7/22, PDF 1470]
- Remaining: FLY — PFD1, alternate law; NAVIGATE — ND1, FMGC1, RMP1, VOR1/ILS1, DME1; COMMUNICATE — VHF1, HF1, ATC1. On batteries FAC1 and FMGC1 are also lost. [FCTM PR-AEP-ELEC P 2/2, PDF 401]
- Secondary failures are inhibited on the ECAM in ELEC EMER CONFIG. [FCOM DSC-31-15 P 5/12, PDF 1842]

## 2. Key limits
- **MIN RAT SPEED:** 140 kt [FCOM PRO-ABN-ELEC P 91/122, PDF 3216; FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **MAX SPEED:** 320 kt [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **MAX BRK PR:** 1 000 PSI [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **FOR LDG:** FLAP LVR 3 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **APPR SPD:** VREF +10 / 140 kt [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **MAX FL:** 4 000 ft below REC MAX FL [QRH 18.01A, PDF 152]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF + PM**
- First to notice: MASTER WARNING reset [FCTM AOP-30-30 P 2/6, PDF 83]
**1.2 PF**
- Fly the aircraft; safe flight path first [FCTM AOP-30-30 P 1/6, PDF 82]
**1.3 PM**
- “ELEC EMER CONFIG” [FCTM AOP-30-30 P 2/6, PDF 83]
- Expect RAT extension; batteries carry the network ~8 s until EMER GEN couples [FCOM DSC-24-10-30-30 P 4/10, PDF 1455]

### 2. Stabilise and roles
**2.1 PF**
- Left-seat pilot (CM1) is PF — only PFD1 is available [FCTM PR-AEP-ELEC P 1/2, PDF 400]
- Fly manually: no AP/FD, no A/THR; alternate law [FCTM PR-AEP-ELEC P 1/2, PDF 400]
- Keep speed 140–320 kt [FCOM PRO-ABN-ELEC P 91/122, PDF 3216; FCOM PRO-ABN-ELEC P 93/122, PDF 3218]
- “MAYDAY” [FCTM PR-AEP-ELEC P 1/2, PDF 400]
- Transmit on VHF1 via the ACP — reselect the transmission key [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
**2.2 PM**
- Monitor flight path; only the EWD remains — use the ECP with discipline [FCTM PR-AEP-ELEC P 1/2, PDF 400]

### 3. ECAM actions
**3.1 PF**
- “ECAM ACTION” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- Communicate with ATC while the PM works the procedure [FCTM AOP-20 P 1–2/10, PDF 68]
**3.2 PM**
- MIN RAT SPEED …… 140 KT [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- GEN 1 + 2 …… OFF THEN ON [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- **IF UNSUCCESSFUL** [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - BUS TIE …… OFF [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - GEN 1 + 2 …… OFF THEN ON [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - If any generator reset is successful, reset both FACs [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - **If EMER GEN not in line** [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
    - EMER ELEC PWR …… MAN ON [FCOM PRO-ABN-ELEC P 91/122, PDF 3216; FCOM DSC-24-20 P 7/22, PDF 1470]
    - “CONFIRM?” [PDP Management of abnormal operations, PDF 432]
    - Guarded: PM points at it; PF answers “CONFIRMED”; then press [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
  - ENG MODE SEL …… IGN [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- VHF1/HF1/ATC1 …… USE [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- PROC : GRVTY FUEL FEEDING …… APPLY (QRH) [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- Keep the ECAM displayed while doing the QRH procedure [FCTM AOP-30-30 P 2/6, PDF 83]
- FAC 1 …… OFF THEN ON [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- BUS TIE …… AUTO [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- APU (IF AVAIL) …… START [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- Not before 45 s after the generators were lost; below FL 250 [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- BLOWER + EXTRACT …… OVRD [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]

### 4. STOP ECAM · STATUS
**4.1 PM**
- “CLEAR ELEC ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.2 PF**
- “CLEAR ELEC” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**4.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**4.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**4.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 5. Decide
**5.1 PM**
- QRH summary CRUISE: limits, max FL, fuel, COM/NAV [QRH 18.01A, PDF 152; PDP Use of summary, PDF 440]
- Fuel: predictions unreliable — apply fuel penalty method, monitor actual burn [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; QRH OPS.03A, PDF 271]
- Landing performance: EFB application, LDG DIST PROC [QRH 18.01A, PDF 152; FCOM EFB-LDG-50 P 3/4, PDF 4890]
**5.2 PF**
- Red LAND ASAP — nearest airport for a safe landing; avoid a poorly equipped field in marginal weather; do not prolong the flight [FCTM AOP-30-10 P 2/2, PDF 79; FCTM PR-AEP-ELEC P 1/2, PDF 400]
- Inform ATC, cabin crew, passengers, company [FCTM AOP-30-30 P 5/6, PDF 86]

### 6. Approach
**6.1 PF**
- Brief with STATUS + QRH APPROACH / LANDING / GO-AROUND [FCTM AOP-30-60 P 2–3/4, PDF 93]
**6.2 PM**
- Check STATUS: all APPR PROC actions done [FCTM AOP-30-60 P 4/4, PDF 95]
**6.3 PF**
- FLAP LVR 3, VREF +10 kt, never below 140 kt [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222; FCTM PR-AEP-ELEC P 2/2, PDF 401]
- Gear down → direct law: USE MAN PITCH TRIM [QRH 18.01A, PDF 152; FCTM PR-AEP-ELEC P 2/2, PDF 401]
**6.4 PM**
- Make the radio-height callouts (RA 1+2 lost) [FCTM PR-AEP-ELEC P 2/2, PDF 401]

### 7. Landing
**7.1 PF**
- Direct-law flare, only 2 spoilers per wing [QRH 18.01B, PDF 153]
- No reversers; alternate braking without anti-skid, max 1 000 PSI; no nosewheel steering [QRH 18.01B, PDF 153; FCTM PR-AEP-ELEC P 2/2, PDF 401]
**7.2 PF + PM**
- All display units are lost approaching 50 kt [FCTM PR-AEP-ELEC P 2/2, PDF 401; FCOM DSC-24-10-30-30 P 4/10, PDF 1455]

### 8. Go-around
**8.1 PF**
- When L/G uplocked: ALTN LAW, PROT LOST; keep ≥ 140 kt [QRH 18.01B, PDF 153; FCOM PRO-ABN-ELEC P 91/122, PDF 3216]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-ELEC)
- **LAND ASAP (red)** [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- MIN RAT SPEED …… 140 KT [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- **CAUTION** The RAT is able to supply the EMER GEN down to 125 kt, however it may not be able to supply the EMER GEN during flare at these speeds. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- GEN 1 + 2 …… OFF THEN ON — Turn off then on all generators one after the other. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- **IF UNSUCCESSFUL:** [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - BUS TIE …… OFF [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - GEN 1 + 2 …… OFF THEN ON — If any generator reset is successful, reset both FACs. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - EMER ELEC PWR …… MAN ON — Displayed if the emergency generator is not in line. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
  - ENG MODE SEL …… IGN — Engines are fed by gravity only. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- VHF1/HF1/ATC1 …… USE — Both ACP remain available; reselect the transmission key to transmit. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- *The flight crew can recover FMGC 1, which is lost temporarily, through the MCDU MENU page.* [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- *FUEL GRVTY FEED — avoid negative G* [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- PROC : GRVTY FUEL FEEDING …… APPLY [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- FAC 1 …… OFF THEN ON — Rudder trim recovered, no indication. [FCOM PRO-ABN-ELEC P 91/122, PDF 3216]
- BUS TIE …… AUTO [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- APU (IF AVAIL) …… START — Not available for 45 s after loss of both engine generators; below FL 250. [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- BLOWER + EXTRACT …… OVRD [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- *FUEL CONSUMPT INCRSD · FMS PRED UNRELIABLE* [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]
- *Associated procedure: F/CTL ALTN LAW (PROT LOST)* [FCOM PRO-ABN-ELEC P 92/122, PDF 3217]

## 5. STATUS
**Limitations**
- MIN RAT SPEED ....... 140 KT [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- MAX SPEED ....... 320 KT [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- MAX BRK PR ....... 1 000 PSI [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- FUEL GRVTY FEED [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- AVOID NEGATIVE G FACTOR [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
**Information**
- Airspeed discrepancy CM1 PFD vs STBY: disregard the STBY indication (probe not de-iced). [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- FUEL CONSUMPT INCRSD · FMS PRED UNRELIABLE — disregard FMS fuel predictions; use QRH fuel penalty factors. [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222; FCOM PRO-ABN-ELEC P 94/122, PDF 3219]
- ALTN LAW: PROT LOST · WHEN L/G DN: DIRECT LAW (pitch and roll) [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- SLATS/FLAPS SLOW · FLS LIMITED TO F-APP + RAW [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **[HS-TXA..TXO]** Centre tank fuel is unusable. [FCOM PRO-ABN-ELEC P 94/122, PDF 3219]
- **[HS-TXP..TXU]** Centre tank fuel can be transferred to the wings by gravity (jet pumps), except the last two tons. [FCOM PRO-ABN-ELEC P 98/122, PDF 3223]
**APPR PROC**
- FOR LDG …… FLAP LVR 3 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- APPR SPD …… VREF +10/140 KT — At least the minimum RAT speed (140 kt). [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- LDG DIST PROC …… APPLY [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
**INOP SYS**
- F/CTL PROT [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- REVERSER 1+2 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- ADR 2+3 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- IR 2+3 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- RA 1+2 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- SPLR 1+2+5 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- ELAC 2 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- SEC 2+3 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- A/CALL OUT [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- AP 1+2 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- A/THR [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- FMGC 2 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- FUEL PUMPS [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- ANTI SKID [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- N/W STRG [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- CAT 2 [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222]
- **[HS-TXA..TXO]** STEEP APPR [FCOM PRO-ABN-ELEC P 93/122, PDF 3218]

## 6. QRH and reference tables
### ELEC EMER CONFIG SUMMARY
**CRUISE**
- MAX SPD : 320 kt · MAX FL : 4000FT BELOW REC MAX FL [QRH 18.01A, PDF 152]
- ALTN LAW: PROT LOST [QRH 18.01A, PDF 152]
- ONLY CAPT PITOT AND AOA HEATED [QRH 18.01A, PDF 152]
- **[HS-TXA..TXO]** FUEL: CTR TK UNUSABLE — FUEL GRAVITY FEEDING [QRH 18.01A, PDF 152]
- **[HS-TXP..TXU]** FUEL: CTR TK USABLE BY GRAVITY: 2 t (4 400 lb) UNUSABLE — FUEL GRAVITY FEEDING [QRH 18.01A, PDF 152]
- COM: VHF1, HF1, ATC1, RMP1 only · NAV: ILS1, VOR1, GPS1 (if MMR is installed) only [QRH 18.01A, PDF 152]
- For landing performance assessment, use the performance application of the EFB. [QRH 18.01A, PDF 152]
**APPROACH**
- CAT 2 INOP [QRH 18.01A, PDF 152]
- MINIMUM RAT SPEED 140 KT [QRH 18.01A, PDF 152]
- SLATS / FLAPS SLOW [QRH 18.01A, PDF 152]
- FOR LDG : FLAP LVR 3 [QRH 18.01A, PDF 152]
- When L/G down: USE MAN PITCH TRIM (DIRECT LAW) [QRH 18.01A, PDF 152]
**LANDING**
- FLARE: Only 2 spoilers per wing. Direct law [QRH 18.01B, PDF 153]
- NO REVERSER [QRH 18.01B, PDF 153]
- BRAKING: ALTERNATE without antiskid · MAX BRK PR : 1 000 PSI [QRH 18.01B, PDF 153]
- NO NOSEWHEEL STEERING [QRH 18.01B, PDF 153]
**GO-AROUND**
- When L/G uplocked: ALTN LAW: PROT LOST [QRH 18.01B, PDF 153]
### SYS REMAINING — highlights
**On EMER GEN / on batteries**
- ND1 lost on batteries; PFD1, upper ECAM, DMC 1/3, SDAC 1/FWC 1 normal (lost below 50 kt on ground). [QRH 18.02C, PDF 156]
- IR, ADR, VOR, MMR, DME, ATC N°1 only (DME, ATC, ADF lost on batteries). IR2/IR3 lost 5 min after main generators fail unless IR3 replaces IR1. [QRH 18.02E–F, PDF 158]
- FMGC, MCDU, FAC N°1 only (lost on batteries); FCU ch 1 only. [QRH 18.02A, PDF 154]
- ELAC, SEC, FCDC, SFCC N°1 only. [QRH 18.02D, PDF 157]
- HF1 and CVR lost on batteries; VHF1, RMP1, ACPs, interphone normal. [QRH 18.02C, PDF 156]
- ENG FIRE EXT bottle 1 only; IGNITION A only; MAN PRESS CTL inop. [QRH 18.02B–D, PDF 155]
## 7. FCTM technique
- Red LAND ASAP, but approaching a poorly equipped airfield in marginal weather is unwise; prolonged flight is not recommended. [FCTM PR-AEP-ELEC P 1/2, PDF 400]
- A clear reading of STATUS is essential to sequence actions during the approach. [FCTM PR-AEP-ELEC P 1/2, PDF 400]
- Complex procedure: use the QRH summary after the ECAM procedure. [FCTM PR-AEP-ELEC P 2/2, PDF 401]
- BSCUs lost: no NWS or anti-skid; alternate braking with yellow hydraulics up to 1 000 PSI; no reversers. [FCTM PR-AEP-ELEC P 2/2, PDF 401]
- RA 1+2 lost with their automatic callouts — the PM makes the callouts. [FCTM PR-AEP-ELEC P 2/2, PDF 401]
- Approaching 50 kt on the landing roll, all display units are lost. [FCTM PR-AEP-ELEC P 2/2, PDF 401]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [QRH] GRAVITY FUEL FEEDING | ECAM line PROC : GRVTY FUEL FEEDING | ENG MODE SEL IGN; avoid negative G; Gravity feed ceiling (HS-TXA..TXT): current FL if > 30 min above FL 300; FL 300 if < 30 min; FL 150 or 7 000 ft above departure if FL 300 never exceeded; FL 100 for JET B; Gravity feed ceiling (HS-TXU): FL 360 / FL 260 / FL 150 or 7 000 ft; At the ceiling: FUEL X FEED OFF | [FCOM PRO-ABN-FUEL P 13/76, PDF 3618; FCOM PRO-ABN-FUEL P 12/76, PDF 3617; QRH 21.10A–B, PDF 206] |
| F/CTL ALTN LAW (PROT LOST) | Associated procedure | Protections lost except manoeuvre protection; MAX SPEED 320 KT; Respect stall warning in TAWS manoeuvres | [FCOM PRO-ABN-F_CTL P 9–12/132, PDF 3482] |
| F/CTL DIRECT LAW | At landing gear extension | MAN PITCH TRIM USE; MAX SPEED 320/.77; Manoeuvre with care; manual thrust recommended | [FCOM PRO-ABN-F_CTL P 19–20/132, PDF 3492] |

## 9. HS-TX differences
| Topic | HS-TXA..TXO | HS-TXP..TXU | Ref |
|---|---|---|---|
| STATUS INOP SYS | includes STEEP APPR | no STEEP APPR | [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222] |
| Centre tank fuel | unusable | usable by gravity except last 2 t | [FCOM PRO-ABN-ELEC P 94/122, PDF 3219; FCOM PRO-ABN-ELEC P 98/122, PDF 3223; QRH 18.01A, PDF 152] |

## 10. Gaps and omissions
- No ELEC EMER CONFIG row in the HS-TX fuel penalty tables although FCOM points to them. [QRH OPS.04C/E, PDF 275]
- FCOM STATUS shows FLS LIMITED TO F-APP + RAW; the HS-TX QRH approach summary does not. [FCOM PRO-ABN-ELEC P 93/122, PDF 3218; FCOM PRO-ABN-ELEC P 97/122, PDF 3222; QRH 18.01A, PDF 152]
- HS-TO-only material omitted (FCOM P 98–105/122 and HS-TO QRH/FCTM blocks). [FCOM PRO-ABN-ELEC P 98–105/122, PDF 3223]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-ELEC — ELEC EMER CONFIG | P 90–98/122 | 3215–3223 | 26 MAY 26 |
| FCOM | DSC-24 Electrical | DSC-24-10-30-30 P 4–7; DSC-24-20 P 7 | 1455–1458, 1470 | 21 MAY 25 |
| QRH | 18.01 Summary · 18.02 Sys remaining | 18.01A–18.02F | 152–159 | 18 FEB 26 |
| FCTM | PR-AEP-ELEC | P 1–2/2 | 400–401 | 26 MAY 26 |
| FCTM | AOP-20 · AOP-30 | — | 68–95 | 26 MAY 26 |
| PDP | Management of abnormal operations · Use of summary | XFTDN6ECAM00001 · XFTDN1USESUMM01 | 420–442 | JAN 2024 |
