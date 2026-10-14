# Managing abnormal operations — rules that apply to every ECAM plan

Faithful extracts (wording kept as close to the source as practicable) from the FCTM and FCOM in `books/`. All passages below are `Applicable to: ALL`. Cite them in the plan with the locator shown. Locator format: `<BOOK> <section code> P x/y (PDF p)`.

If you suspect an edition change (different filename in `books/`), re-verify these extracts with `manuals.py show fctm 68-99` and `manuals.py show fcom 2824-2835`.

---

## 1. Order of procedures and the "one procedure at a time" rule
Source: FCTM AOP-30-10 P 1/2 (PDF 78)

- ECAM procedures, QRH procedures and OEB procedures are performed using **READ & DO** (except MEMORY items or OEB immediate actions).
- Sequence, as appropriate: **MEMORY ITEMS or OEB immediate actions → OEB → ECAM → QRH**. The crew should use judgment and adapt the sequence to the real conditions.
- **One procedure at a time:** complete a procedure unless an action requests to apply/consider another procedure, or the crew must update their situation assessment due to an unexpected abnormal or emergency situation (e.g. smoke reported by cabin crew, volcanic ash).
- **Use of AP:** the AP is not certified in all configurations; if used, extra vigilance is required and it must be disconnected if the aircraft deviates from the desired or safe flight path. (AOP-30-10 P 1–2/2, PDF 78–79)

## 2. LAND ASAP
Source: FCTM AOP-30-10 P 2/2 (PDF 79)

- **Red LAND ASAP**: land as soon as possible at the nearest airport at which a safe landing can be made (time-critical).
- **Amber LAND ASAP**: consider landing at the nearest suitable airport (suitability per operator policy).

## 3. Task sharing in abnormal operations
Sources: FCTM AOP-20 P 1–2/10 (PDF 68–69); FCTM AOP-30-30 P 1/6 (PDF 82)

- **PF**: FLY, NAVIGATE, and **COMMUNICATE** after initiation of the ECAM actions or of a QRH procedure. The PF also initiates the ECAM/QRH/OEB actions that the PM performs, and communicates until the PM announces "ECAM ACTIONS COMPLETE" or "XXX procedure complete" (QRH/OEB).
- **PM**: MONITOR the flight path and navigation; perform the ECAM actions or apply the QRH/OEB procedure — Read & Do in a spoken voice, and **obtain PF confirmation before clearing any ECAM**.
- The COM task moves to the PF during ECAM/QRH/OEB management because the PM's cognitive capacity is dedicated to the procedure.
- The PF usually remains PF for the whole flight, unless the captain re-allocates tasks, or **a failure impacts the PF's "FLY" task** (e.g. loss of the PF's flight instruments).

## 4. Before any READ & DO
Source: FCTM AOP-30-30 P 1/6 (PDF 82)

- First priority: **maintain a safe flight path**.
- At takeoff or go-around, delay READ & DO actions until **at least 400 ft AGL** (may start earlier only if the flight path is safe).
- Time-critical situations: apply MEMORY ITEMS / OEB immediate actions strictly by memory.

## 5. Cockpit controls and overhead panel
Source: FCTM AOP-30-20 P 1–2/2 (PDF 80–81)

- In flight, PF and PM **crosscheck before any action** on: ENG MASTER lever, IR MODE selector, **all guarded controls**, cockpit C/Bs. Method: PM indicates the control and asks confirmation → PF verifies and confirms → PM operates.
- **Thrust levers** are operated by the PF only: PF indicates the lever and asks confirmation → PM verifies and confirms → PF moves it.
- Overhead actions: PM points to the panel/control and announces **system name – control – action** (e.g. "AIR, XBLEED, CLOSE"), then checks the SD page to confirm the result.
- System resets: only those listed in the QRH; never from memory.
- **Reset authorization (QRH 02.01A, PDF 50, verified visually):** in flight, a reset is authorized only if the ECAM/OEB/FCOM/QRH procedure requests it, or the alert is *listed and authorized* in the system reset table (02.02); on ground, also if the affected system is NOT listed. In all other cases: **RESET NOT AUTHORIZED** (red WARNING). Several failures of the same system: not authorized if at least one reset is not. One reset at a time. Standard reset: CKPT CTL OFF, 3 s, ON — or C/B CROSSCHECK (both), PULL, 5 s, PUSH — then 3 s, RESET(S) RECORD in logbook.
- **A table entry covers only the alert it names.** A single-unit entry ("FWS FWC 1(2) FAULT") does not cover the dual failure; dual cases are named explicitly when covered ("NAV FLS 1(2) (1+2) FAULT", "FUEL FQI CH 1+2 FAULT"). So FWC 1 + 2 FAULT has no reset in flight, and SDAC (not in the table at all) has none in flight but the standard reset on ground.

## 6. ECAM handling sequence (PF/PM table)
Source: FCTM AOP-30-30 P 2–4/6 (PDF 83–85, graphical table — verified visually); callouts also FCOM PRO-ABN-ABN-00 P 8/12 (PDF 2831)

| # | PF | PM |
|---|----|----|
| 1 | First crewmember who notices: MASTER WARNING/CAUTION — RESET | (same) |
| 2 | | For each ECAM procedure: "Title of failure" — ANNOUNCE; ECAM — CONFIRM (check overhead panel and/or SD to analyse and confirm the failure before any action; sensors may differ from those that triggered the alert) |
| 3 | OEB — CONSIDER (both) | |
| 4 | **"ECAM ACTIONS"** — ORDER (for the first ECAM only when several failures are displayed). Apply AOP-20 task sharing for abnormal operations. | |
| 5 | | ECAM/OEB ACTIONS — PERFORM; **"CLEAR (name of the system)?"** — REQUEST |
| 6 | ECAM ACTIONS PERFORMED — CHECK; **"CLEAR (name of the system)"** — CONFIRM | CLR pb — PRESS (only after checking all actions were performed) |
| 7 | For each SD page: SD page — ANALYZE (both); "CLEAR (name of the system)" — CONFIRM | "CLEAR (name of the system)?" — REQUEST; CLR pb — PRESS |
| 8 | When STATUS appears: **"STOP ECAM"** — ORDER | **"STATUS"** — ANNOUNCE; ECAM ACTIONS — STOP |
| 9 | Consider the acceleration flow pattern, any normal C/L, system reset, or additional procedure, as applicable; then **"CONTINUE ECAM"** — ORDER | |
| 10 | | STATUS — READ (preview associated procedures to evaluate workload; perform them at the appropriate flight phase); **"REMOVE STATUS?"** — REQUEST |
| 11 | **"REMOVE STATUS"** — CONFIRM | STS pb — PRESS; **"ECAM ACTIONS COMPLETE"** — ANNOUNCE |

FCOM standard callouts (PRO-ABN-ABN-00 P 8/12, PDF 2831): 1) "ECAM ACTION" commanded by PF when required; 2) "CLEAR __ (title of the system) ?" asked by PM (e.g. "CLEAR HYDRAULIC ?"); 3) "CLEAR __ (title of the system)" by PF — for the status page "REMOVE STATUS"; 4) "ECAM ACTIONS COMPLETE" by PM when all applicable actions are complete; 5) "STOP ECAM" / "CONTINUE ECAM" ordered by PF to interrupt/resume. (FCOM says "ECAM ACTION", FCTM table says "ECAM ACTIONS" — quote the FCOM wording and note the FCTM variant.)

ECAM detail (AOP-30-30 P 2–4/6, PDF 83–85):
- If an ECAM procedure requests a QRH procedure: **keep the ECAM procedure displayed** and apply the QRH procedure (avoids disturbance by lower-priority alerts).
- **STOP ECAM** when actions need both pilots (ATC communication, configuration change, baro setting). **Always stop before reading STATUS** to: ensure the acceleration flow pattern (after takeoff: flaps and gear retracted); do pending normal C/L; consider system resets (QRH reset table only); consider ENG RELIGHT after an engine failure with no damage.
- **STATUS page**: overview of the technical status for all flight phases; check the whole page; read the associated procedures to anticipate workload per flight phase.
- If an ECAM warning/caution **disappears** during the procedure, it can be considered no longer applicable; the procedure can be stopped.

## 7. QRH procedures
Source: FCTM AOP-30-30 P 5/6 (PDF 86)

- PM finds the procedure through the QRH Abnormal and Emergency Procedures table of contents.
- **Read the notes before performing the action** they relate to.
- A QRH abnormal procedure can be stopped if its application conditions disappear.

## 8. After ECAM/QRH/OEB actions are completed
Source: FCTM AOP-30-30 P 5/6 (PDF 86)

1. Resume normal-operations task sharing.
2. If time permits, review the FCOM for the procedure (do not prolong the flight to do so).
3. Assess the situation — recall STATUS when convenient: fuel penalty factor and remaining fuel at destination/diversion; landing distance penalty and landing distance computation; operational, maintenance and commercial aspects.
4. Make the decision.
5. Inform ATC, cabin crew, passengers and airline operations as required.

## 9. Use of QRH summaries (ELEC EMER CONFIG and dual hydraulic failures)
Source: FCTM AOP-30-60 P 1–4/4 (PDF 92–95, diagrams verified visually)

Summaries have four sections: CRUISE, APPROACH, LANDING, GO-AROUND.
- Steps 1–2: **apply the ECAM first** (procedure and STATUS). PM announces "ECAM ACTIONS COMPLETE", then refers to the QRH summary.
- Step 3: after STATUS, PM reads the **CRUISE** section (remaining systems — ELEC EMER CONFIG only — main limitations, flight capability) → assess situation and select a runway.
- Steps 4–5: performance application or QRH chapters for **increased fuel consumption** and **landing performance** at the selected airport → DECISION.
- Approach preparation (steps 6–8): while checking STATUS, use APPROACH, LANDING and GO-AROUND sections to prepare the approach and the FMGS. These sections include, when appropriate, LANDING WITH SLATS OR FLAPS JAMMED and L/G GRAVITY EXTENSION.
- Arrival briefing (steps 9–10): brief with the APPROACH, LANDING and GO-AROUND sections while crosschecking STATUS.
- Approach (steps 11–12): fly with the APPROACH section; in final configuration rapidly review LANDING and GO-AROUND (braking, NWS, reversers, L/G retraction for go-around); PM finally checks STATUS and that all APPR PROC actions are completed.

## 10. Advisories and spurious cautions
Sources: FCTM AOP-30-40 P 1/2 (PDF 88); AOP-30-50 P 1/2 (PDF 90)

- Advisory: first crewmember announces "ADVISORY on XYZ system"; PF asks PM to monitor; PM may consult the QRH if time permits.
- Spurious caution: EMER CANC pb deletes the aural alert and the caution for the rest of the flight ("CANCELLED CAUTION" on STATUS). For a red warning it only inhibits the aural.

## 11. Golden rules
Source: FCTM AOP-40 P 1–4/4 (PDF 96–99)

1. **Fly, Navigate, Communicate** — in this order, with appropriate task sharing. In abnormal and emergency situations, the PF must recover a steady flight path, the crew identifies the situation, then the PF informs ATC and cabin crew of the situation and intentions. "Fly the aircraft".
2. Use the appropriate level of automation at all times (manual flight decided by both pilots, considering malfunctions, fatigue, weather, traffic, familiarity).
3. Understand the FMA at all times (monitor, announce, confirm, understand).
4. Take action if things do not go as expected: PF changes automation level (managed → selected → manual); PM communicates, challenges, takes over if necessary.

## 12. Emergency calls and memory-item callouts
Source: FCOM PRO-ABN-ABN-00 P 9–11/12 (PDF 2832–2834)

- Cockpit → cabin PA: "PURSER TO COCKPIT, PLEASE!"; "ATTENTION CREW! AT STATIONS!" (evacuation may soon be required); "CABIN CREW and PASSENGERS REMAIN SEATED!"; "EVACUATE, EVACUATE". Cabin → cockpit interphone: "PRIO CAPT".
- Memory-item announcements: "PULL UP TOGA", "WINDSHEAR TOGA", "UNRELIABLE SPEED", "TCAS blue" / "TCAS, I have control", "EMERGENCY DESCENT", "LOSS OF BRAKING", "STALL, I have control", "STALL, TOGA 15°".
- Malfunction before V1: CAPT "GO" / "STOP"; F/O "REVERSE GREEN" (or "NO REVERSE ENGINE__"/"NO REVERSE"), "DECEL" (or "NO DECEL"); "MANUAL BRAKING" (CAPT) / "AUTOBRAKE OFF" (F/O).

Include only the items relevant to the procedure being planned.

### Company (THAI) phraseology — overrides the generic FCOM/PDP wording
User-specified operator wording (2026-10-14). Use it in every brief and note the substitution under Gaps:
- PA to alert the cabin (evacuation may be required): **"CABIN CREW, AT YOUR STATIONS"** — not "ATTENTION CREW AT STATIONS".
- PA when evacuation is not required: **"REMAIN SEATED, RESUME NORMAL DUTIES"** — not "CABIN CREW and PASSENGERS REMAIN SEATED".
- Radio call sign: **"THA {flight number}"** (THAI), e.g. "THA ___, STOPPING" — not "AIRBUS ___".

## 13. How to read an FCOM procedure page
Source: FCOM PRO-ABN-ABN-00 P 2–8/12 (PDF 2825–2831)

- Large letters = shown on ECAM; small letters = not on ECAM. The text extraction prefixes layers as `L1`/`L2`/`L12`: layer 2 is the expanded information (identifies particular failures, explains non-obvious actions, gives background). Only the FCOM version of a procedure carries layer 2/3 information (P 2/12).
- ANNUNCIATIONS = triggering conditions + flight phase inhibition (phases defined in DSC-31-15).
- **Black square** = start of one of several procedures under the same title, or mutually exclusive parts. **Black dot** = precondition. **Indentation** = action depends on the precondition above it; items aligned with a precondition do not depend on it.
- **Boxed items** = memory items, OEB immediate actions or "At ANY TIME of the procedure" items.
- PROCEDURES AND STATUS section = procedure + STATUS (limitations, approach procedure, INOP SYS).

## 14. Airbus PDP tutorial — task sharing and callouts (generic A320/A330)
Source: `books/Airbus Tutorial PDP Jan 2024.pdf`, module *Management of abnormal operations* (PDF 420–435). Slides verified visually. Use these to complete the PF/PM flow; FCOM/FCTM wording wins if they differ.

- **Detection** (PDF 423): the first pilot who notices — MASTER WARNING / MASTER CAUTION … RESET. Maintain a safe flight path first; READ & DO not before 400 ft AGL at takeoff/go-around unless the path is safe.
- **ECAM actions** (PDF 424): PM ANNOUNCE "title of the failure" (e.g. "AIR APU BLEED FAULT"); PM ECAM … CONFIRM with SD page and overhead panel; OEB … CONSIDER; PF ORDER **"ECAM ACTIONS"** (first ECAM only, PDF 430); tasksharing for abnormal operations — PF flies, navigates, **communicates after the initiation of the ECAM actions**; PM ECAM/OEB ACTIONS … PERFORM; PM "CLEAR (name of the SYSTEM)?" → PF ECAM ACTIONS PERFORMED … CHECK, "CLEAR (SYSTEM)" (e.g. "CLEAR AIR") → PM CLR pb.
- **Actions confirmed by both pilots** (PDF 432): in flight, crosscheck before any action on guarded controls, ENG MASTER levers, IR MODE selectors, cockpit C/Bs (and before PF moves thrust levers). Example ENG 1 FAIL: PM reads "ENGINE MASTER 1 OFF", indicates the control, asks **"CONFIRM?"**; PF verifies, answers **"CONFIRMED"**; PM performs. Not applicable on ground.
- **SD pages** (PDF 425): SD page … ANALYZE; PM "CLEAR (SYS)?" / PF "CLEAR (SYS)", e.g. "CLEAR FLIGHT CONTROL?".
- **STATUS** (PDF 426): PM "STATUS"; PF **"STOP ECAM"**; PM ECAM ACTIONS … STOP; consider the ACCELERATION flow pattern, any normal C/L, system/computer reset (QRH [RESET]), any additional procedure (e.g. ENG RELIGHT IN FLIGHT); PF **"CONTINUE ECAM"**; PM STATUS … READ; PM "REMOVE STATUS?" / PF "REMOVE STATUS"; PM STS pb, **"ECAM ACTIONS COMPLETED"**; back to normal task sharing.
- **When to stop ECAM** (PDF 430): for actions needing both pilots (ATC, configuration change, baro setting) — PF "STOP ECAM" … PF "CONTINUE ECAM".
- **ECAM asks for a QRH procedure** (PDF 431): "(name) PROC … APPLY" → stop the ECAM actions, refer to the QRH, perform it; the QRH says when to come back to ECAM, otherwise continue ECAM when the QRH procedure is completed.
- **QRH procedures** (PDF 427): first pilot noticing a defect without ECAM advises the other; OEB … CONSIDER; PF ORDER **"(name of the procedure) PROCEDURE"**; PF communicates; PM QRH/OEB ACTIONS … READ AND DO; PM **"(name) PROCEDURE COMPLETED"**.
- **Actions completed** (PDF 428): assess (STATUS recall, LAND ASAP, weather, fuel penalty, landing performance, RVSM/RNP/approach capability), decide, inform (ATC, cabin crew, PAX, airline operations).
- **Advisory** (PDF 421): "ADVISORY ON (system) SYSTEM"; PF requests drifting-parameter monitoring; PM analyzes SD and monitors; if time permits, QRH advisory conditions.
- **Memory items** (PDF 422): ANNOUNCE the appropriate callout (title of the procedure, e.g. "EMERGENCY DESCENT").
