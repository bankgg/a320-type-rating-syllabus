# ANTI ICE STBY PITOT or L(R) STAT or AOA — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX.

An amber caution: one standby probe (pitot, left or right static, or AOA) has lost its heating. There is no action line — it is crew awareness. If the standby instruments are being used, monitor the air data closely, because an unheated probe can ice up.

## 1. What it is
- **Trigger:** The heating system of the corresponding standby probe has failed. [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- Electrical heating protects pitot probes, static ports, AOA probes and TAT probes. Three independent Probe Heat Computers control the Captain, F/O and STBY probes. [FCOM DSC-30-50-10 P 1/2, PDF 1786]
- Probes are heated automatically in flight or with one engine running, or manually with PROBE/WINDOW HEAT ON. [FCOM DSC-30-50-10 P 1/2, PDF 1786; FCOM DSC-30-50-20 P 1/2, PDF 1788]
- ADR 3 and the standby speed use the same probe; STBY SPD UNCERTAIN appears when ADR 3 speed is declared faulty. [FCOM PRO-ABN-NAV P 3/124, PDF 3828; FCOM DSC-34-NAV-10-30-20 P 3/8, PDF 2112]

## 2. Key limits
- **Action:** Crew awareness [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- **Inhibited:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PM**
- “ANTI ICE STBY PITOT” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- Or STBY L(R) STAT / STBY AOA — announce the title shown [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
**1.2 PF**
- “ECAM ACTION” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]

### 2. Procedure
**2.1 PM**
- Crew awareness …… — [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- If standby instruments are used, monitor air data information [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
**2.2 PF**
- Fly as usual; be alert to standby airspeed/altitude discrepancies [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]

### 3. STATUS
**3.1 PM**
- “CLEAR ANTI ICE ?” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]
**3.2 PF**
- “CLEAR ANTI ICE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]
**3.3 PM**
- INOP SYS: STBY PITOT · STBY L(R) STAT · STBY AOA [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
**3.4 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]
**3.5 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-A-ICE)
- *Crew awareness.* [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- *If standby instruments are used, monitor air data information.* [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]

## 5. STATUS
**INOP SYS**
- STBY PITOT [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- STBY L(R) STAT [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- STBY AOA [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| [MEM] UNRELIABLE SPEED INDICATION | If standby/ADR 3 speed becomes erroneous | See the Unreliable speed brief | [FCOM PRO-ABN-NAV P 1/124, PDF 3826] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No FCTM technique for this caution in the supplied FCTM. [FCOM PRO-ABN-A-ICE P 39/42, PDF 2886]
- HS-TO version omitted (FCOM P 40/42). [FCOM PRO-ABN-A-ICE P 40/42, PDF 2887]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-A-ICE — ANTI ICE STBY PITOT or L(R) STAT or AOA | P 39/42 | 2886 | 18 FEB 26 |
| FCOM | DSC-30-50 Probes heat | P 1/2 | 1786, 1788 | 22 MAR 16 |
