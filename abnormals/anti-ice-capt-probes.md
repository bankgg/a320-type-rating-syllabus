# ANTI ICE CAPT PROBES — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-31 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX.

An amber caution: the captain probe heat computer has failed, so the captain probes are no longer heated. ADIRU 1 takes its air data from those probes. The one action is AIR DATA SWTG to CAPT 3, which replaces ADR 1 with ADR 3, unless ADR 3 is not available.

## 1. What it is
- **Trigger:** This alert triggers when the captain probe heat computer is failed. [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- Three independent Probe Heat Computers automatically control and monitor the captain, F/O and standby probes. They protect against overheating and indicate faults. [FCOM DSC-30-50-10 P 1/2, PDF 1786]
- Heating protects the pitot probes, static ports, AOA probes and TAT probes. [FCOM DSC-30-50-10 P 1/2, PDF 1786]
- ADIRU 1 is supplied by the CAPT probes, ADIRU 2 by the F/O probes, and ADIRU 3 by the STBY probes and CAPT TAT. [FCOM DSC-34-NAV-10-10 P 3/4, PDF 2098]
- With the selector in NORM, ADIRU 1 supplies PFD 1 and ND 1. CAPT 3 replaces ADR 1 with ADR 3. [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]

## 2. Key limits
- **AIR DATA SWTG:** CAPT 3 — not if ADR 3 is not available [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- **Inhibited:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- **Reset in flight:** Not authorized: not in the reset table [QRH 02.01A, PDF 50; QRH 02.02A, PDF 51]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF + PM**
- First to notice: MASTER WARNING / CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “ANTI ICE CAPT PROBES” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-A-ICE P 19/42, PDF 2866; PDP Management of abnormal operations, PDF 424]
- Confirm the failure on the SD page and overhead panel before acting [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTIONS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. ECAM actions
**2.1 PM**
- AIR DATA SWTG …… CAPT 3 [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- Not to CAPT 3 if ADR 3 is not available [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- ADR 3 replaces ADR 1 [FCOM DSC-34-NAV-10-20 P 3/6, PDF 2102]

### 3. STATUS
**3.1 PM**
- “CLEAR ANTI ICE ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
**3.2 PF**
- “CLEAR ANTI ICE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 424]
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

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-A-ICE)
- AIR DATA SWTG …… CAPT 3 [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]
- *AIR DATA SWTG should not be selected to CAPT 3 if ADR 3 is not available.* [FCOM PRO-ABN-A-ICE P 19/42, PDF 2866]

## 5. STATUS
**INOP SYS**
- CAPT PROBES [FCOM PRO-ABN-A-ICE P 20/42, PDF 2867]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| ANTI ICE STBY PITOT or L(R) STAT or AOA | ADIRU 3, which replaces ADIRU 1 here, uses the standby probes | See the standby probe heat brief | [FCOM DSC-34-NAV-10-10 P 3/4, PDF 2098] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- ANTI ICE CAPT PROBES is not in the QRH reset table, so a reset is not authorized in flight; on ground the standard reset rule for unlisted systems applies. [QRH 02.01A, PDF 50; QRH 02.02A, PDF 51]
- The manuals give no limitation or icing advice on the ANTI ICE CAPT PROBES STATUS page beyond the INOP SYS line. [FCOM PRO-ABN-A-ICE P 20/42, PDF 2867]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-A-ICE — ANTI ICE CAPT PROBES (HS-TX) | P 19–20/42 | 2866–2867 | 18 FEB 26 |
| FCOM | DSC-30-50-10 — probes heat | P 1/2 | 1786 | 22 MAR 16 |
| FCOM | DSC-34-NAV-10 — probes schematic, AIR DATA selector | P 3/4 · P 3/6 | 2098, 2102 | 18 FEB 26 |
| QRH | 02.01–02.02 — reset rule and table | 02.01A–02.02A | 50–51 | 26 MAY 26 |
