# ANTI ICE L(R) WINDOW — handling plan (HS-TX)

> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH (14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. Generated 2026-10-14 with the `a320-ecam-abnormal` skill.

**Amber caution · no memory items**  
**Applicability:** all HS-TX — One version for all HS-TX.

An amber caution: the heating of the left or right cockpit side window has failed. There is no action line, only crew awareness, and STATUS shows L(R) WNDW HEAT as INOP SYS. A reset is allowed only on the ground, from the QRH reset table, when a spurious alert is likely (packs OFF with the OAT above 40 °C, or the windshield in direct sunlight). It is not authorized in flight.

## 1. What it is
- **Trigger:** This alert triggers when the heating system of the left(right) cockpit window is failed. [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]
- **Flight phase inhibition:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]
- Electrical heating protects the flight compartment windows (hot air protects slats and engine intakes). [FCOM DSC-30-10-10 P 1/2, PDF 1766]
- Electrical heating anti-ices each windshield and defogs the cockpit side windows. Two independent WHCs, one on each side, regulate the system, protect it against overheating and indicate faults. [FCOM DSC-30-40-10 P 1/2, PDF 1782]
- Window heating comes ON automatically when at least one engine is running or in flight, and manually before engine start when PROBE/WINDOW HEAT is switched ON. [FCOM DSC-30-40-10 P 1/2, PDF 1782]
- The windshield heats at low power on ground and normal power in flight; the windows have only one heating level. [FCOM DSC-30-40-10 P 1/2, PDF 1782]
- PROBE/WINDOW HEAT pb: AUTO = heated in flight, or on ground with one engine running (except TAT probes). ON = blue light, probes and windows heated permanently. Ensure the probe covers are removed before selecting ON. [FCOM DSC-30-50-20 P 1/2, PDF 1788]
- Two different C/B sets: the reset uses the WHC C/Bs X13 / W13 (ANTI ICE / WHC / 1 / 2); the arcing procedure pulls the heating C/Bs ANTI ICE/WINDOWS L X14 / R W14 (122VU) or L/R WSHLD AF10 / AF03 (123VU). [QRH 02.09A, PDF 62; QRH 25.05A, PDF 223]

## 2. Key limits
- **Action:** Crew awareness [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]
- **Inhibited:** phases 3, 4, 5, 7, 8 [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]
- **Reset in flight:** Not authorized [QRH 02.09A, PDF 62]
- **Ground reset:** PACK 1+2 ON, wait 5 min, then C/B pull · 5 s · push [QRH 02.09A, PDF 62]

## 3. Flow (PF / PM)
### 1. Recognise
**1.1 PF + PM**
- First to notice: MASTER CAUTION reset [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.2 PM**
- “ANTI ICE L WINDOW” [FCTM AOP-30-30 P 2/6, PDF 83; FCOM PRO-ABN-A-ICE P 37/42, PDF 2884; PDP Management of abnormal operations, PDF 424]
- Or ANTI ICE R WINDOW — announce the title shown [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]
- ECAM — confirm the failure before any action [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
**1.3 PF**
- “ECAM ACTION” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831]
- PF now flies, navigates and communicates [FCTM AOP-20 P 1–2/10, PDF 68; PDP Management of abnormal operations, PDF 424]

### 2. Procedure
**2.1 PM**
- Crew awareness …… — [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]

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
- Consider a system reset: QRH System Reset table lists ANTI ICE L(R) WINDSHIELD (WINDOW) → WHC [QRH 02.02A, PDF 51; FCTM AOP-30-30 P 4/6, PDF 85]
- **In flight** [QRH 02.09A, PDF 62]
  - Reset not authorized [QRH 02.09A, PDF 62]
- “CONTINUE ECAM” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.7 PM**
- Read the whole STATUS page; preview APPR PROC workload [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
- “REMOVE STATUS ?” [FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.8 PF**
- “REMOVE STATUS” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; FCTM AOP-30-30 P 3/6, PDF 84; PDP Management of abnormal operations, PDF 426]
**3.9 PM**
- “ECAM ACTIONS COMPLETE” [FCOM PRO-ABN-ABN-00 P 8/12, PDF 2831; PDP Management of abnormal operations, PDF 426]

### 4. On ground: QRH reset (spurious alert)
**4.1 PF**
- “ANTI ICE L(R) WINDSHIELD (WINDOW) PROCEDURE” [PDP Management of abnormal operations, PDF 427; QRH 02.09A, PDF 62]
- Found from the QRH System Reset table (02.02A) [QRH 02.02A, PDF 51]
**4.2 PM**
- **If the packs are OFF with the OAT above 40 °C, and/or the windshield is under direct sunlight** [QRH 02.09A, PDF 62]
  - PACK 1+2 …… ON [QRH 02.09A, PDF 62]
  - Wait …… 5 min [QRH 02.09A, PDF 62]
  - On 122VU: [QRH 02.09A, PDF 62]
  - **If ANTI ICE L WINDSHIELD** [QRH 02.09A, PDF 62]
    - C/B X13 (ANTI ICE / WHC / 1) …… PULL — wait 5 s — PUSH [QRH 02.09A, PDF 62]
  - **If ANTI ICE R WINDSHIELD** [QRH 02.09A, PDF 62]
    - C/B W13 (ANTI ICE / WHC / 2) …… PULL — wait 5 s — PUSH [QRH 02.09A, PDF 62]
- “ANTI ICE L(R) WINDSHIELD (WINDOW) PROCEDURE COMPLETED” [PDP Management of abnormal operations, PDF 427]

### 5. Assess and decide
**5.1 PF + PM**
- Assess: recall STATUS, approach capability, operational and maintenance aspects; decide; inform as required [FCTM AOP-30-30 P 5/6, PDF 86; PDP Management of abnormal operations, PDF 428]
- QRH CAT 2/CAT 3 equipment list: WINDSHIELD HEAT (L or R windshield) 1 for PF; side window heat is not listed [QRH OPS.08D, PDF 285]

## 4. Procedure
### ECAM procedure (FCOM PRO-ABN-A-ICE)
- *Crew awareness.* [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]

### ANTI ICE L(R) WINDSHIELD (WINDOW) — system reset (QRH 02.09A)
- **In flight:** [QRH 02.09A, PDF 62]
  - *Not authorized.* [QRH 02.09A, PDF 62]
- **On ground:** [QRH 02.09A, PDF 62]
  - *If the air conditioning packs are OFF with the OAT above 40 °C, and/or the windshield is under direct sunlight, a spurious ANTI ICE L(R) WINDSHIELD (WINDOW) alert may trigger. In this case, apply the following reset procedure:* [QRH 02.09A, PDF 62]
  - PACK 1+2 …… ON [QRH 02.09A, PDF 62]
  - *Wait 5 min* [QRH 02.09A, PDF 62]
  - *On 122VU:* [QRH 02.09A, PDF 62]
  - **If ANTI ICE L WINDSHIELD:** [QRH 02.09A, PDF 62]
    - C/B X13 (ANTI ICE / WHC / 1) …… PULL [QRH 02.09A, PDF 62]
    - *Wait 5 s* [QRH 02.09A, PDF 62]
    - C/B X13 (ANTI ICE / WHC / 1) …… PUSH [QRH 02.09A, PDF 62]
  - **If ANTI ICE R WINDSHIELD:** [QRH 02.09A, PDF 62]
    - C/B W13 (ANTI ICE / WHC / 2) …… PULL [QRH 02.09A, PDF 62]
    - *Wait 5 s* [QRH 02.09A, PDF 62]
    - C/B W13 (ANTI ICE / WHC / 2) …… PUSH [QRH 02.09A, PDF 62]

## 5. STATUS
**INOP SYS**
- L(R) WNDW HEAT [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]

## 8. Related procedures
| Procedure | Why | Key actions | Ref |
|---|---|---|---|
| Ground operations in cold weather (FCOM supplementary) | Cold-weather preflight selects PROBE/WINDOW HEAT ON, so window heat runs before engine start; this alert is not inhibited in that phase | WINDSHIELD AND UPPER COCKPIT FUSELAGE — ICE/SNOW REMOVED (caution: melted ice or snow could re-freeze on the forward fuselage near the probes); PROBE COVERS — CHECK REMOVED; PROBE/WINDOW HEAT — ON; After first engine start: PROBE/WINDOW HEAT — AUTO | [FCOM PRO-NOR-SUP-ADVWXR P 4/24, PDF 4365; FCOM PRO-NOR-SUP-ADVWXR P 6/24, PDF 4367; FCOM DSC-30-40-10 P 1/2, PDF 1782; FCOM PRO-ABN-A-ICE P 37/42, PDF 2884; FCTM PR-NP-SP-10-10-1 P 1/8, PDF 350] |
| COCKPIT WINDSHIELD / WINDOW ARCING | Electrical arcing of a windshield/window, or burning smell or smoke from the bottom corner of a windshield | Affected WINDOW/WINDSHIELD ANTI ICE C/B — PULL; ANTI ICE/WINDOWS L C/B X14 · R C/B W14 [122VU]; ANTI ICE L WSHLD C/B AF10 · R WSHLD C/B AF03 [123VU] | [QRH 25.05A, PDF 223; FCOM PRO-ABN-MISC P 10/30, PDF 3805] |

## 9. HS-TX differences
None — the content applies to every HS-TX registration.

## 10. Gaps and omissions
- No FCTM technique and no PDP module for this caution; the flow uses the generic ECAM and QRH task sharing (FCTM AOP-30-30, PDP abnormal operations). [FCTM AOP-30-30 P 2/6, PDF 83; PDP Management of abnormal operations, PDF 424]
- The QRH reset title covers WINDSHIELD (WINDOW), but its steps name only “If ANTI ICE L WINDSHIELD” / “If ANTI ICE R WINDSHIELD”. No separate step is given for the L(R) WINDOW alert. [QRH 02.09A, PDF 62]
- Dispatch with window heat inoperative (MEL) is not covered by the supplied manuals. [FCOM PRO-ABN-A-ICE P 37/42, PDF 2884]
- HS-TO cold-weather AFTER START version omitted. [FCOM PRO-NOR-SUP-ADVWXR P 5–6/24, PDF 4366]

## Sources
| Book | Section | Pages | PDF | Rev |
|---|---|---|---|---|
| FCOM | PRO-ABN-A-ICE — ANTI ICE L(R) WINDOW | P 37/42 | 2884 | 18 FEB 26 |
| QRH | 02.02A System reset table · 02.09A ANTI ICE L(R) WINDSHIELD (WINDOW) | 02.02A, 02.09A | 51, 62 | 26 MAY 26 |
| QRH | 25.05A Cockpit windshield / window arcing | 25.05A | 223 | 18 FEB 26 |
| QRH | OPS.08D Required equipment for CAT 2 and CAT 3 | OPS.08D | 285 | 14 JUL 26 |
| FCOM | DSC-30-10 / 30-40 / 30-50 Ice and rain protection | P 1/2 | 1766, 1782, 1788 | 15 FEB 23 |
| FCOM | PRO-NOR-SUP-ADVWXR Ground operations in cold weather | P 4–6/24 | 4365–4367 | 26 MAY 26 |
| FCOM | PRO-ABN-MISC Cockpit windshield / window arcing | P 10/30 | 3805 | 18 FEB 26 |
| FCTM | PR-NP-SP-10-10-1 Cold weather operations | P 1/8 | 350 | 21 MAY 25 |
