# M2 Test Design (report §4)

> **Status: Draft v1.2 (2026-11-14).** Built from SRS v4.2 and CD-final (DEC-94/104/108). The original BB/WB/CFG/basis-path cases are retained; weekly HR snapshot cases supplement them. The black-box and white-box sections use **different methods**, as the template requires.
> Example dates: Planning Week 19–24 October 2026; Availability Deadline 7 October 2026, 18:00. Test fixtures are synthetic and independent.

---

## 1. Black-box testing: decision table for `StandbyPreferenceController.submitPick()`

### 1.1 Method and expected behaviour

`submitPick(technician, week, day, brand)` saves a Technician's one **provisional** Standby-day request for a Planning Week (FR-51, UC-18). It calls `RuleValidator.checkStandbyPick()`, which checks the conditions **in the order below and reports the first that fails**. If every check passes, it saves a Provisional pick with submittedAt, replacing a different earlier pick the Technician had that week and freeing that slot. Re-submitting the same day/Brand is a no-op and preserves submittedAt (UC-18 Alternatives).

### 1.2 Causes (conditions) and effects

| ID | Cause | True means |
|---|---|---|
| C1 | Before the Availability Deadline | Now is earlier than 18:00 on the Wednesday 12 days before the week (FR-15) |
| C2 | Available that day | The Technician's Availability for the day is `Available` and there is no Leave Record for that day (FR-12, FR-52) |
| C3 | Certified for the Brand | The Technician holds a Certification for the chosen Brand whose expiry date is on or after the day (FR-22) |
| C4 | Slot free | No other Technician holds that day's slot for that Brand (the Technician's own current pick counts as free) |
| C5 | Already has a pick this week | The Technician already holds a Standby Preference for this Planning Week |

| ID | Effect |
|---|---|
| E1 | Refuse: "This week is locked" |
| E2 | Refuse: "You are not available that day" |
| E3 | Refuse: "You are not certified for this Brand on that day" |
| E4 | Refuse: "This slot has just been taken" |
| E5 | Save the new provisional pick |
| E6 | If day/Brand changed, replace the existing provisional pick, free the old slot and reset submittedAt; the same day/Brand is a no-op preserving submittedAt |

### 1.3 Complete decision table (2⁵ = 32 combinations)

| # | C1 | C2 | C3 | C4 | C5 | Effect | Reduced rule |
|---|---|---|---|---|---|---|---|
| 1 | T | T | T | T | T | E6 Existing pick: change or retain unchanged (R6 constraint) | R6 |
| 2 | T | T | T | T | F | E5 Save provisional pick | R5 |
| 3 | T | T | T | F | T | E4 Refuse: slot already taken | R4 |
| 4 | T | T | T | F | F | E4 Refuse: slot already taken | R4 |
| 5 | T | T | F | T | T | E3 Refuse: not certified for this Brand | R3 |
| 6 | T | T | F | T | F | E3 Refuse: not certified for this Brand | R3 |
| 7 | T | T | F | F | T | E3 Refuse: not certified for this Brand | R3 |
| 8 | T | T | F | F | F | E3 Refuse: not certified for this Brand | R3 |
| 9 | T | F | T | T | T | E2 Refuse: not available that day | R2 |
| 10 | T | F | T | T | F | E2 Refuse: not available that day | R2 |
| 11 | T | F | T | F | T | E2 Refuse: not available that day | R2 |
| 12 | T | F | T | F | F | E2 Refuse: not available that day | R2 |
| 13 | T | F | F | T | T | E2 Refuse: not available that day | R2 |
| 14 | T | F | F | T | F | E2 Refuse: not available that day | R2 |
| 15 | T | F | F | F | T | E2 Refuse: not available that day | R2 |
| 16 | T | F | F | F | F | E2 Refuse: not available that day | R2 |
| 17 | F | T | T | T | T | E1 Refuse: week locked | R1 |
| 18 | F | T | T | T | F | E1 Refuse: week locked | R1 |
| 19 | F | T | T | F | T | E1 Refuse: week locked | R1 |
| 20 | F | T | T | F | F | E1 Refuse: week locked | R1 |
| 21 | F | T | F | T | T | E1 Refuse: week locked | R1 |
| 22 | F | T | F | T | F | E1 Refuse: week locked | R1 |
| 23 | F | T | F | F | T | E1 Refuse: week locked | R1 |
| 24 | F | T | F | F | F | E1 Refuse: week locked | R1 |
| 25 | F | F | T | T | T | E1 Refuse: week locked | R1 |
| 26 | F | F | T | T | F | E1 Refuse: week locked | R1 |
| 27 | F | F | T | F | T | E1 Refuse: week locked | R1 |
| 28 | F | F | T | F | F | E1 Refuse: week locked | R1 |
| 29 | F | F | F | T | T | E1 Refuse: week locked | R1 |
| 30 | F | F | F | T | F | E1 Refuse: week locked | R1 |
| 31 | F | F | F | F | T | E1 Refuse: week locked | R1 |
| 32 | F | F | F | F | F | E1 Refuse: week locked | R1 |

### 1.4 Reduced decision table

Rules with the same effect are merged where the remaining conditions do not change the outcome ("–" = don't care).

| Rule | C1 | C2 | C3 | C4 | C5 | Effect | Combinations merged |
|---|---|---|---|---|---|---|---|
| R1 | F | – | – | – | – | E1 Refuse: week locked | 16 (#17–32) |
| R2 | T | F | – | – | – | E2 Refuse: not available | 8 (#9–16) |
| R3 | T | T | F | – | – | E3 Refuse: not certified | 4 (#5–8) |
| R4 | T | T | T | F | – | E4 Refuse: slot taken | 2 (#3–4) |
| R5 | T | T | T | T | F | E5 Save provisional pick | 1 (#2) |
| R6 | T | T | T | T | T | E6 Existing pick (see constraint below) | 1 (#1) |

Check: 16 + 8 + 4 + 2 + 1 + 1 = 32.

**R6 constraint:** C5 covers both an actual change and re-submitting the same slot. It does not imply a new timestamp for the latter. For example, a pick submitted Mon 5 at 09:00 for Tue 20 / M Electric, re-submitted unchanged at 10:00, retains 09:00 and its slot. The six-rule reduction is unchanged (FR-51; UC-18 Alternatives).

### 1.5 Test cases (one per reduced rule)

Setup: Technician **T07** (M Electric only, Certification expiry 30 Jun 2027). Planning Week Mon 19 – Sat 24. **T03** already holds Wed 21 / Dicon.

| TC | Rule | Inputs (now, day, Brand, other state) | Expected output |
|---|---|---|---|
| BB-01 | R1 | Now Wed 7, 18:00; Tue 20; M Electric | Refused: "This week is locked". No record saved |
| BB-02 | R2 | Now Mon 5, 10:00; Thu 22 where T07 has a Leave Record (MC); M Electric | Refused: "You are not available that day" |
| BB-03 | R3 | Now Mon 5, 10:00; Tue 20; **Dicon**; T07 Available | Refused: "You are not certified for this Brand on that day" |
| BB-04 | R4 | Now Mon 5, 10:00; Wed 21; M Electric; **T09 already holds Wed 21 / M Electric** | Refused: "This slot has just been taken" |
| BB-05 | R5 | Now Mon 5, 10:00; Tue 20; M Electric; T07 has no pick this week | Provisional (not yet guaranteed): T07 → Tue 20 / M Electric. Tue 20's M Electric slot shows as taken |
| BB-06 | R6 | Now Mon 5, 10:00; Fri 23; M Electric; T07 already holds Tue 20 / M Electric | Provisional (not yet guaranteed): T07 → Fri 23 / M Electric. Tue 20's M Electric slot is free again |

### 1.6 Supplementary check for R6 (no new reduced rule)

| TC | Existing rule | Independent setup and action | Expected output |
|---|---|---|---|
| BB-07 | R6 / complete combination #1 | T07 is Available with no Leave and valid M Electric Certification on 20 Oct 2026. One Provisional pick for 20 Oct / M Electric was saved on 5 Oct 2026 at 09:00; its own slot counts as free. Re-submit the same day/Brand at 10:00 on 5 Oct, before the 7 Oct deadline. | Keep the original submittedAt = 09:00, the same held slot and exactly one Provisional request. Do not release/recreate the slot or change its submission priority. |

BB-07 checks the unchanged branch within R6; BB-06 checks the changed branch. The complete table still has 32 combinations and six reduced rules (FR-51; UC-18 Alternatives; DEC-104). These are designed expected results, not claimed production execution.

Extra boundary checks (equivalence partitions and boundary values, not required by the template): C1 at 17:59 → passes and at 18:00 → fails. C3 with expiry equal to the day → passes and the day before → fails. A Dual-Certified Technician on a day where only the Dicon slot is free → can take Dicon (R5).

---

## 2. White-box testing: `CrewFormingService.classifyTechnicians()`

### 2.1 Method

`classifyTechnicians(day)` carries out FR-55 steps 1–4 for one working day. It drops Technicians who are not working, puts confirmed Standby picks and Dual-Certified Technicians with 20 Active Hours or more last week on Standby, and splits everyone else into an under-40 h group and a 40 projected-Credited-hours-or-more group. Each group is then ordered by `WorkloadRanking` (the Strategy, report §3.2).

### 2.2 Pseudocode

```text
classifyTechnicians(day):
 1  week ← planningWeekContaining(day); standby ← []; ranked ← []; bottom ← []
 2  for each t in activeTechnicians():
 3      if not t.isWorkingOn(day) then          // Unavailable, Not submitted or Leave Record
 4          continue
 5      if hasConfirmedStandbyPick(t, day) then
 6          standby.add(t, Preference)
 7      else if t.isDual(day) and t.lastWeekActiveHours(week) >= 20 then
 8          standby.add(t, Algorithm)           // use home Zone
 9      else if t.projectedCreditedHours(day) >= 40 then
10          bottom.add(t)
11      else
12          ranked.add(t)
13  end for
14  ranked ← ranking.order(ranked, day)        // last week's Active, projected Active, staff ID
15  bottom ← ranking.order(bottom, day)
16  return (ranked + bottom, standby)
```

Line 7 is a short-circuit `and`, so it becomes **two** decision nodes in the CFG (N7 `isDual`, N8 `>= 20`).

### 2.3 Control flow graph

Source: [diagrams/CFG-classify-technicians.puml](../diagrams/CFG-classify-technicians.puml).

| Node | Pseudocode line(s) | Kind |
|---|---|---|
| N1 | 1 (derive Planning Week and initialise lists) | Statement |
| N2 | 2 (loop test: more Technicians?) | **Decision** |
| N3 | 3 | **Decision** |
| N4 | 4 | Statement (back to N2) |
| N5 | 5 | **Decision** |
| N6 | 6 | Statement |
| N7 | 7 (`isDual`) | **Decision** |
| N8 | 7 (`>= 20`) | **Decision** |
| N9 | 8 | Statement |
| N10 | 9 | **Decision** |
| N11 | 10 | Statement |
| N12 | 12 | Statement |
| N13 | 13 (end of iteration) | Junction |
| N14 | 14–16 | Statement (exit) |

Edges (19): N1→N2; N2→N3 (T); N2→N14 (F); N3→N4 (T); N3→N5 (F); N4→N2; N5→N6 (T); N5→N7 (F); N6→N13; N7→N8 (T); N7→N10 (F); N8→N9 (T); N8→N10 (F); N9→N13; N10→N11 (T); N10→N12 (F); N11→N13; N12→N13; N13→N2.

The CFG has 14 nodes and 6 decision points, which meets the rubric's "at least eight nodes and two decision points".

### 2.4 Cyclomatic complexity

- V(G) = E − N + 2 = 19 − 14 + 2 = **7**
- V(G) = decision nodes + 1 = 6 + 1 = **7**
- V(G) = regions of the planar graph = **7**

So 7 basis paths are needed.

### 2.5 Basis paths (baseline method)

Baseline: one Technician who is working, has no pick, is single-Brand and is under 40 h. Each later path flips one decision of the baseline.

| Path | Flip | Node sequence |
|---|---|---|
| B1 (baseline) | — | N1-N2-N3-N5-N7-N10-N12-N13-N2-N14 |
| B2 | N2 → F | N1-N2-N14 |
| B3 | N3 → T | N1-N2-N3-N4-N2-N14 |
| B4 | N5 → T | N1-N2-N3-N5-N6-N13-N2-N14 |
| B5 | N7 → T | N1-N2-N3-N5-N7-N8-N10-N12-N13-N2-N14 |
| B6 | N8 → T (on B5) | N1-N2-N3-N5-N7-N8-N9-N13-N2-N14 |
| B7 | N10 → T | N1-N2-N3-N5-N7-N10-N11-N13-N2-N14 |

Together the 7 paths cover all 19 edges.

### 2.6 Test cases

Day = Wed 21 of the Planning Week. Each case has one active Technician, so the loop runs once (zero times for B2).

| TC | Path | Input | Expected output |
|---|---|---|---|
| WB-01 | B1 | T03, M Electric only, Available, no pick, projected 16 h | ranked = [T03]; standby = [] |
| WB-02 | B2 | No active Technicians | ranked = []; standby = [] |
| WB-03 | B3 | T04 with a Leave Record (Leave) on Wed 21 | ranked = []; standby = [] (T04 excluded) |
| WB-04 | B4 | T05, Available, confirmed Standby pick Wed 21 / Dicon | standby = [T05 (Preference)]; ranked = [] |
| WB-05 | B5 | T01, Dual-Certified, Available, no pick, last week's Active Hours **19.5 h**, projected 16 h | ranked = [T01]; standby = [] |
| WB-06 | B6 | T02, Dual-Certified, Available, no pick, last week's Active Hours **20 h** | standby = [T02 (Algorithm, home Zone)]; ranked = [] |
| WB-07 | B7 | T06, Dicon only, Available, no pick, projected Credited **40 h** | ranked = [T06] (from the 40 h-or-more group, so placed after any under-40 h Technician); standby = [] |

WB-05/WB-06 test the 20 h boundary (19.5 vs 20) and WB-07 tests the 40 h ranking boundary (DEC-86). A further integration case with all of T01–T06 checks the final order: under-40 h first by last week's Active Hours, then the 40 h-or-more group.

## 3. Cross-rule scenarios for the clarified design (DEC-96–98)

These extend the required decision-table/CFG evidence; they do not replace it. The repo contains design/pseudocode, not an executable scheduling application. All hour inputs below include the agreed Travel Allowance.

| Scenario | Setup / action | Expected |
|---|---|---|
| SC-01 | Rostered Standby, no duties | Active 0, Credited 4, activated dates +0 |
| SC-02 | First direct duty 2 h | Active 2, Credited 4, count +1 |
| SC-03 | First duty exactly 4 h; separately test 5 h | 4/4 or 5/5; each date counts once |
| SC-04 | Separate duties 2 h then 3 h on one date | First 2/4, then 5/5; count remains +1. Replaying the save is idempotent |
| SC-05 | Alex attributed to Job 1 (2 h); Ben replaces from Job 2 (6 h remaining) | Job 1 retains Alex; later Jobs name Ben. Alex 2/2; Ben 6/6; no 4+6 credit |
| SC-06 | Provisional pick before deadline; missing HR/Van CSV after deadline | Remains Provisional; no confirmation, no false guarantee |
| SC-07 | 3 ME + 3 DI, no dual; request one ME Standby | Three Crews possible without Standby but not with full cover; pick NotConfirmed with staffing reason. Minimum Crews take priority |
| SC-08 | 4 ME + 4 DI, no dual; one ME and one DI request | Both can confirm, leaving 3 mixed Crews and both-Brand Standby cover |
| SC-09 | 2 ME + 2 DI + 2 duals; dual A requests first, dual B second | A confirms: B + two pairs form 3 Crews, A covers Standby. B cannot also confirm; NotConfirmed. Submission order is preserved |
| SC-10 | Dual has last week Active 0 / Credited 24 from six unused Standby days | Included in ranking, not the >=20 Active Hours Standby branch |
| SC-11 | 2 ME + 2 DI + 2 duals; greedy pairing consumes all six in three pairs | Feasible fallback uses two single-dual Crews + one opposite-Brand pair, leaving full cover; minimum/cover cannot be lost by greedy ordering |
| SC-12 | Two Crews, enough Vans, no eligible way to form a third | Show shortage, confirm no new picks and block publication; do not count direct duties as a Van Crew |
| SC-13 | Missing Dicon member; ME-only Standby count 0, valid dual count 2 | Filter ME-only candidate before ranking; dual recommended if available for all remaining Jobs |
| SC-14 | Technician has a direct duty until 15:00; another starts 15:10 or 15:30 | Reject 15:10; allow 15:30 if all other rules pass. Replacement-Crew commitment prevents a second Crew assignment |
| SC-15 | Manager tries to move a confirmed pick into the initial Crew; later genuinely activates that person | Initial override blocked; activation allowed with proper eligibility, attribution and audit. Reconfirmation/regeneration does not duplicate notices |

### 3.1 Confirmation/coverage check

Use current available/certified Technicians, available Drivers and Van count. Reserved confirmed picks stay outside initial Crews. A small search enumerates valid both-Brand groups (one dual, or two opposite-Brand Technicians), chooses three disjoint groups and checks that all remaining Technicians, including reserved picks, provide both-Brand Standby cover. Return that arrangement or no solution. Confirmation requires the solution; the same arrangement is available to the roster as a fallback. There are only 11 Technicians, so this needs no optimiser. Ordinary shortage handling still distinguishes three Crews without cover from fewer than three.

Resolve provisional requests in submittedAt/staff-ID order, saving each day's results atomically. Previously confirmed decisions are immutable/idempotent. Recheck eligibility and capacity at publication; later Leave overrides placement without erasing preference history.

### 3.2 Hours and activation invariants

- Active(date) = latest corrected Active Hours, otherwise sum of attributed Planned Hours on that date.
- Credited(date) = max(4, Active(date)) when rostered Standby; otherwise Active(date). Full-day Leave without duties has no floor.
- ActivationCount(asOf) = distinct activated Standby dates in the rolling 12 months ending asOf. Ignore later dates; a date at the retained cutoff follows the same calendar-month boundary as retention.
- Only the first activation changes the date flag. A failed phone call does not activate. No count/credit is added per Job.
- Initial Crew members and earlier Assignment snapshots remain unchanged by replacement. Later Jobs use Crew.membersFor(job), applying replacements by effectiveFrom.

### 3.3 Verification scope

Check the 32 unique black-box combinations/reduced-rule outcomes; the CFG's 19 edges and seven basis paths; class/method/FR/UC links; scenario arithmetic and minimum-coverage examples; and locally render the six current M2 diagram sources. These verify the design and examples, not production scheduling code or completed wireframe screens.

**Verification performed (2026-11-07):** checked all 32 unique submission combinations and their 16/8/4/2/1/1 reduced-rule counts; checked CFG/source edge equality, seven valid paths and full edge coverage (V=7); independently calculated minimum-coverage examples SC-07–12 and the hours/attribution examples; checked SRS method references against CD-final. All six current M2 sources rendered locally to SVG/PNG with PlantUML 1.2026.8 and were visually inspected; CFG node labels were enclosed to avoid crossing edges. Full class/component views are large and should be used as zoomable SVGs or laid out for the report by their owners. This does not claim application execution or completed wireframes.


## Supplemental CSV snapshot design cases (DEC-108, SRS v4.2)

These cases supplement FR-52/54 and UC-07/16/18; they are **designed, not executed against a production implementation**. Each starts from independent fixtures. Keep the selected week's existing Leave, another week's Leave, prior committed coverage, preferences and earlier Assignment attribution for before/after comparison.

| Case | Input / trigger | Expected outcome |
|---|---|---|
| CSV-01 | Complete confirmed HR snapshot, valid headers/rows all in selected Mon–Sat week; duplicate included | Commit unique rows; selected-week records exactly match snapshot; week/uploader/time/outcome and success Audit Log commit together; other week unchanged |
| CSV-02 | Required HR headers and zero data rows, complete-export confirmed; no existing Leave | Commit zero Leave Records and successful week coverage; UC-07/18 HR-ready despite no records; still require each Van count and locked Availability |
| CSV-03 | Header-only complete snapshot replacing a week with existing Leave; first cancel, then confirm | Explicit warning identifies week and clearing effect; cancel preserves rows/coverage; confirmation clears only selected-week Leave and commits coverage/log; preserve preference history and earlier Job Staff |
| CSV-04 | Wholly blank file, missing header, mixed valid/invalid rows, Sunday, unknown Staff/type, or one row outside selected week (independent variants) | Reject entire import; list relevant errors; business rows and previous successful coverage unchanged |
| CSV-05 | Selected week but complete-export confirmation absent, or export declared partial/delta | Refuse commitment as complete snapshot; week selection alone does not establish completeness; no replacement |
| CSV-06 | Valid confirmed replacement but transaction fails after business changes are staged; earlier successful coverage exists | Roll back selected-week rows, committed metadata and success Audit Log together; preserve previous successful coverage; retain failed attempt outcome; planning still uses prior committed coverage |
| CSV-07 | Van file has headers/no rows; then a valid explicit count of 0 for one date | Empty van file rejected; explicit zero accepted as zero capacity for that date only; do not infer missing dates' capacity or HR coverage |
| CSV-08 | Valid no-Leave week coverage; Staff has no Availability entry; later snapshot adds Leave over a confirmed placement | Staff remains unavailable without Availability. Later Leave makes Staff ineligible and raises the existing Manager-repair alert; preserve confirmation history and earlier Job attribution; no silent roster rewrite |
