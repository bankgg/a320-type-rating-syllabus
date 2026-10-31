# AUTO FLT FCU 1 + 2 FAULT — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — FCOM procedure applies to ALL; the QRH reset used here is the all HS-TX version.

Both FCU channels are lost, so every FCU control is inoperative. A/THR, both APs and both FDs are not available, except in LAND or GO AROUND mode where only A/THR is lost. The PFD barometric reference goes to 1 013 hPa, so set the actual setting on the standby altimeter and make the minimum callouts from it. The QRH reset table lists this alert, so consider the C/B reset at the STOP ECAM pause.

## 1. What it is
- **Trigger:** The FCU is completely lost (both channels failed). [FCOM PRO-ABN-AUTO_FLT P 21/42, PDF 2998]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-AUTO_FLT P 21/42, PDF 2998]
- All FCU controls are inoperative. A/THR, AP 1 + 2 and FD 1 + 2 are not available (except in LAND or GO AROUND mode, where only A/THR is lost). [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- On the PFD: altitude alert inoperative; ILS/GLS/MLS deviation scales displayed; flight path vector displayed; Mach indication inoperative; FMA lost except in LAND or GA mode. [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- On the ND: ARC mode with map (20 NM range) is displayed. Needle 1 is related to VOR1 only; needle 2 to ADF 2 only. The weather radar image may be lost; if it remains displayed it must be disregarded. In all cases the WXR RNG message is displayed. [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- An A/THR disconnection caused by a failure is a non-standard disconnection: the engines hold the thrust set before it, THR LK flashes on the FMA and ENG THRUST LOCKED appears every 5 s. The lock ends as soon as the thrust levers are moved. [FCOM DSC-22_30-50-40 P 2/4, PDF 1193; FCOM PRO-ABN-ENG P 224/226, PDF 3471; FCOM DSC-22_30-80-20 P 34/36, PDF 1259]
- Alpha-floor protection is inhibited when both FCU channels are failed. [FCOM DSC-22_40-30 P 4/4, PDF 1279]

## 2. Key limits
- **PFD BARO REF:** STD ONLY [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999; FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- **Standby altimeter:** Set the actual barometer setting [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- **MDA (MDH):** Do not insert on PERF APPR [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- **In LAND or GA:** CAT 2 ONLY [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- **Reset in flight:** Both C/Bs pulled, wait 5 s [QRH 02.15B, PDF 74]

## 3. Flow (PF / PM)
### 1. Detection
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PF**
- Fly the aircraft: AP 1 + 2 and FD 1 + 2 are not available, except in LAND or GO AROUND mode [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999; FCTM AOP-30-30 P 1/6, PDF 82]
- A/THR is lost: move the thrust levers. Thrust stays frozen at its last value until they are moved [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999; FCOM DSC-22_30-50-40 P 2/4, PDF 1193; FCOM PRO-ABN-ENG P 224/226, PDF 3471]
**1.3 PM**
- “AUTO FLT FCU 1 + 2 FAULT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-AUTO_FLT P 21/42, PDF 2998; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.4 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- PFD BARO REF …… STD ONLY [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- Use the standby altimeter and change it to the actual barometer setting [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- The barometer reference on the PFD has gone to 1 013 hPa automatically [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]

### 3. Stop ECAM
**3.1 PM**
- “CLEAR AUTO FLT ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR AUTO FLT” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]

### 4. QRH reset
**4.1 PF**
- Consider the reset: the QRH reset table lists AUTO FLT FCU 1 + 2 FAULT, so it is authorized in flight [QRH 02.02B, PDF 52; QRH 02.01A, PDF 50; FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
**4.2 PM**
- Read the QRH lines; point to each cockpit C/B [QRH 02.15B, PDF 74; FCTM AOP-30-20 P 1/2, PDF 80; PDP Management of abnormal operations, PDF 432]
- “CONFIRM?” [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**4.3 PF**
- “CONFIRMED” [PDP Management of abnormal operations, PDF 432]
- After verifying the C/B the PM points to [PDP Management of abnormal operations, PDF 432; FCTM AOP-30-20 P 1/2, PDF 80]
**4.4 PM**
- C/B B05 (AUTO FLT / FCU / 1) on 49VU …… PULL [QRH 02.15B, PDF 74]
- C/B M21 (AUTO FLT / FCU / 2) on 121VU …… PULL [QRH 02.15B, PDF 74]
- Wait 5 s [QRH 02.15B, PDF 74]
- C/B B05 (AUTO FLT / FCU / 1) on 49VU …… PUSH [QRH 02.15B, PDF 74]
- C/B M21 (AUTO FLT / FCU / 2) on 121VU …… PUSH [QRH 02.15B, PDF 74]
**4.5 PF + PM**
- FCU TARGETS AND SELECTIONS …… CHECK [QRH 02.15B, PDF 74]
- BAROMETRIC REFERENCE …… SET/CROSSCHECK [QRH 02.15B, PDF 74]

### 5. Continue ECAM
**5.1 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.2 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.3 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**5.4 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 6. Approach
**6.1 PF + PM**
- Do not insert the MDA (MDH) on the PERF APPR page: PFD altitude is referenced to STD [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
**6.2 PM**
- Make the standard callouts using the STBY altimeter [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- “HUNDRED ABOVE” [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- “MINIMUM” [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]

## 4. Procedure
### AUTO FLT FCU 1 + 2 FAULT (ECAM) (FCOM PRO-ABN-AUTO_FLT P 22/42)
- *PFD BARO REF: STD ONLY* [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- *With both FCU channels failed, the barometer reference automatically goes to 1 013 hPa. Use standby altimeter, and change this to the actual barometer setting.* [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- *Do not insert the MDA (MDH) value on the PERF APPR page (because the PFD altitude is referenced to STD, and not to the correct barometric value).* [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- *The PM must then perform the standard callouts ("HUNDRED ABOVE" and "MINIMUM"), using the STBY altimeter.* [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]

### AUTO FLT FCU 1+2 FAULT — reset (QRH 02.15B–C) (QRH 02.15B–C)
- **In flight:** [QRH 02.15B, PDF 74]
  - C/B B05 (AUTO FLT / FCU / 1), on 49VU …… PULL [QRH 02.15B, PDF 74]
  - C/B M21 (AUTO FLT / FCU / 2), on 121VU …… PULL [QRH 02.15B, PDF 74]
  - *Wait 5 s* [QRH 02.15B, PDF 74]
  - C/B B05 (AUTO FLT / FCU / 1), on 49VU …… PUSH [QRH 02.15B, PDF 74]
  - C/B M21 (AUTO FLT / FCU / 2), on 121VU …… PUSH [QRH 02.15B, PDF 74]
  - FCU TARGETS AND SELECTIONS …… CHECK [QRH 02.15B, PDF 74]
  - BAROMETRIC REFERENCE …… SET/CROSSCHECK [QRH 02.15B, PDF 74]
- **On ground:** [QRH 02.15B, PDF 74]
  - C/B B05 (AUTO FLT / FCU / 1), on 49VU …… PULL [QRH 02.15B, PDF 74]
  - C/B M21 (AUTO FLT / FCU / 2), on 121VU …… PULL [QRH 02.15B, PDF 74]
  - *Wait 5 s* [QRH 02.15B, PDF 74]
  - C/B B05 (AUTO FLT / FCU / 1), on 49VU …… PUSH [QRH 02.15B, PDF 74]
  - C/B M21 (AUTO FLT / FCU / 2), on 121VU …… PUSH [QRH 02.15B, PDF 74]
  - **If AUTO FLT FCU 1+2 FAULT disappears:** [QRH 02.15B, PDF 74]
    - FCU TARGETS AND SELECTIONS …… CHECK [QRH 02.15B, PDF 74]
    - BAROMETRIC REFERENCE …… SET/CROSSCHECK [QRH 02.15B, PDF 74]
  - **If AUTO FLT FCU 1+2 FAULT remains:** [QRH 02.15B, PDF 74]
    - C/B B05 (AUTO FLT / FCU / 1), on 49VU …… PULL [QRH 02.15B, PDF 74]
    - C/B M21 (AUTO FLT / FCU / 2), on 121VU …… PULL [QRH 02.15B, PDF 74]
    - *Wait 7 min* [QRH 02.15B, PDF 74]
    - C/B B05 (AUTO FLT / FCU / 1), on 49VU …… PUSH [QRH 02.15C, PDF 75]
    - *Within 5 s, on 121VU:* [QRH 02.15C, PDF 75]
    - C/B M21 (AUTO FLT / FCU / 2) …… PUSH [QRH 02.15C, PDF 75]
    - *Wait at least 30 s for FCU 1 and FCU 2 safety tests completion.* [QRH 02.15C, PDF 75]
    - FCU TARGETS AND SELECTIONS …… CHECK [QRH 02.15C, PDF 75]
    - BAROMETRIC REFERENCE …… SET/CROSSCHECK [QRH 02.15C, PDF 75]

## 5. STATUS
**Limitations**
- PFD BARO REF : STD ONLY [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- If in LAND or GA: CAT 2 ONLY [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
**INOP SYS**
- FCU 1 + 2 [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- AP 1 + 2 (if not LAND or GA) [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- A/THR [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- CAT 3 (if in LAND or GA mode) [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- CAT 2 (if not LAND or GA) [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- GPWS TERR [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]
- ROW/ROP [FCOM PRO-ABN-AUTO_FLT P 23/42, PDF 3000]

## 7. FCTM technique
- STOP ECAM before reading STATUS to consider system resets, from the QRH reset table only. Baro setting is one of the actions that needs both pilots. [FCTM AOP-30-30 P 3/6, PDF 84; FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 430]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ENG THRUST LOCKED | Triggers if the thrust levers are not moved within 5 s after an involuntary A/THR disconnection. | THR LEVERS: MOVE | [FCOM PRO-ABN-ENG P 224/226, PDF 3471] |
| AUTO FLT FCU 1(2) FAULT | One channel only remains operative. A separate alert with its own QRH reset (02.14). | BARO REF: X CHECK | [FCOM PRO-ABN-AUTO_FLT P 20/42, PDF 2997; QRH 02.14A, PDF 69] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The FCTM has no technique for this failure (PR-AEP-AUTOFLT covers FMGC failure only), and the PDP has no module for it. Fly/thrust items come from the FCOM layer 2 text and the DSC thrust-lock description. [FCTM PR-AEP-AUTOFLT P 1/2, PDF 394; FCOM DSC-22_30-50-40 P 2/4, PDF 1193]
- The FCOM names no pilot for changing the standby altimeter; the brief shows the PM, confirmed by the user. It names no pilot for not inserting the MDA (MDH), shown for both pilots. It names the PM only for the callouts. [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999]
- The FCOM says the FMA is lost except in LAND or GA mode, and also that THR LK flashes on the FMA. The manuals do not reconcile the two. The brief only states the conflict, confirmed by the user. [FCOM PRO-ABN-AUTO_FLT P 22/42, PDF 2999; FCOM DSC-22_30-50-40 P 2/4, PDF 1193]
- HS-TO-only QRH version of the reset (02.15A) is excluded. [QRH 02.15A, PDF 73]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-AUTO_FLT — AUTO FLT FCU 1 + 2 FAULT | P 21–23/42 | 2998–3000 | 26 MAY 26 |
| QRH | 02.15 AUTO FLT FCU 1+2 FAULT; 02.02 reset table | 02.15B–C, 02.02B, 02.01A | 50, 52, 74–75 | 26 MAY 26 |
| FCOM | DSC-22_30-50-40 thrust lock; DSC-22_40-30 alpha-floor; PRO-ABN-ENG ENG THRUST LOCKED | P 2/4; P 4/4; P 224/226 | 1193, 1279, 3471 | 26 MAY 26 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
