# APU AUTO (EMER) SHUT DOWN — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — Applicable to ALL.

The APU has shut down, either by itself after a failure (AUTO) or by the APU FIRE pb, the APU SHUT OFF sw or a detected fire on ground (EMER). The only ECAM line is MASTER SW OFF. After an automatic shutdown a restart can be considered, within the limit on start attempts.

## 1. What it is
- **Trigger:** APU AUTO SHUT DOWN: automatic APU shutdown for a reason other than a fire. APU EMER SHUT DOWN: APU SHUT OFF sw on the External Power Panel pushed, APU FIRE pb pushed, or APU fire on ground detected. [FCOM PRO-ABN-APU P 1/4, PDF 2972]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-APU P 1/4, PDF 2972]
- In the case of an APU failure or misbehavior, the APU may automatically shut down, without a cooling period, in order to avoid subsequent damage. [FCOM DSC-49-30 P 1/2, PDF 2584]
- An immediate emergency shutdown, without a cooling period, occurs when the APU FIRE pb on the overhead panel or the APU SHUT OFF sw on the external power panel is pressed. [FCOM DSC-49-30 P 2/2, PDF 2585]
- Some shutdown conditions apply only on ground with the engines not running: ECB failure, N overspeed and no speed. An APU fire shuts the APU down automatically on ground only. The full list is in FCOM DSC-49-30. [FCOM DSC-49-30 P 1/2, PDF 2584]
- The FAULT light on the APU MASTER SW pb comes on when the APU has failed, an automatic shutdown is in progress, or an emergency shutdown has occurred. [FCOM DSC-49-20 P 2/10, PDF 2575]

## 2. Key limits
- **APU restart:** Can be considered after an auto shut down [FCOM PRO-ABN-APU P 1/4, PDF 2972]
- **After 3 consecutive start attempts:** Wait 60 min [FCOM PRO-ABN-APU P 1/4, PDF 2972]

## 3. Flow (PF / PM)
### 1. Detection and ECAM actions
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “APU AUTO SHUT DOWN” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-APU P 1/4, PDF 2972; PDP Management of abnormal operations, PDF 424]
- Or APU EMER SHUT DOWN, as displayed [FCOM PRO-ABN-APU P 1/4, PDF 2972]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]
**1.4 PM**
- MASTER SW …… OFF [FCOM PRO-ABN-APU P 1/4, PDF 2972]

### 2. STATUS
**2.1 PM**
- “CLEAR APU ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**2.2 PF**
- “CLEAR APU” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**2.3 PM**
- “STATUS” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.4 PF**
- “STOP ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.5 PM**
- ECAM ACTIONS …… STOP [PDP Management of abnormal operations, PDF 426]
**2.6 PF**
- Normal C/L as applicable; system resets only per QRH [FCTM AOP-30-30 P 4/6, PDF 85; PDP Management of abnormal operations, PDF 426]
- **After an APU auto shut down** [FCOM PRO-ABN-APU P 1/4, PDF 2972]
  - APU restart can be considered; after three consecutive start attempts, wait 60 min before a new attempt [FCOM PRO-ABN-APU P 1/4, PDF 2972]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**2.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

## 4. Procedure
### APU AUTO (EMER) SHUT DOWN (FCOM PRO-ABN-APU P 1/4)
- MASTER SW …… OFF [FCOM PRO-ABN-APU P 1/4, PDF 2972]
- *In the case of APU auto shut down, APU restart can be considered. After three consecutive APU start attempts, the flight crew must wait 60 min before a new start attempt.* [FCOM PRO-ABN-APU P 1/4, PDF 2972]

## 5. STATUS
**INOP SYS**
- APU [FCOM PRO-ABN-APU P 2/4, PDF 2973]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| APU FIRE | Pushing the APU FIRE pb triggers APU EMER SHUT DOWN. | See the APU FIRE brief | [FCOM PRO-ABN-APU P 1/4, PDF 2972; FCOM PRO-ABN-APUF P 1/2, PDF 2976] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- The procedure limits a restart "after three consecutive" start attempts; the system description says "after more than three consecutive" attempts, and "should" rather than "must". The brief uses the procedure wording, confirmed by the user. [FCOM PRO-ABN-APU P 1/4, PDF 2972; FCOM DSC-49-30 P 1/2, PDF 2584]
- The FCTM and the PDP have no technique specific to this alert; the flow is the standard ECAM sequence. [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- The QRH reset table does not list this alert. [QRH 02.02B, PDF 52]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-APU — APU AUTO (EMER) SHUT DOWN | P 1–2/4 | 2972–2973 | 17 AUG 22 |
| FCOM | DSC-49-20 / DSC-49-30 — APU controls, abnormal operations | P 2/10; P 1–2/2 | 2575, 2584–2585 | 24 NOV 25 |
| FCTM | AOP-20 / AOP-30 — task sharing and ECAM handling | AOP-20 P 1–2/10, AOP-30 P 1–6/6 | 68–69, 79–86 | 26 MAY 26 |
| PDP | Management of abnormal operations (XFTDN6ECAM00001) | ECAM actions, STATUS, QRH, confirm | 424–432 | JAN 2024 |
