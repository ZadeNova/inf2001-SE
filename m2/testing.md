# M2 Test Design (report §4)

> **Status: Draft v1.0 (2026-11-06).** Built from SRS v4.0 and CD-final (DEC-94). The black-box and white-box sections use **different methods**, as the template requires.
> Example dates: Planning Week Monday 19 to Saturday 24; Availability Deadline Wednesday 7, 18:00.

---

## 1. Black-box testing: decision table for `StandbyPreferenceController.submitPick()`

### 1.1 Method and expected behaviour

`submitPick(technician, week, day, brand)` saves a Technician's one Standby day for a Planning Week (FR-51, UC-18). It calls `RuleValidator.checkStandbyPick()`, which checks the conditions **in the order below and reports the first that fails**. If every check passes, it saves the pick, replacing any earlier pick the Technician had that week and freeing that slot.

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
| E5 | Save the new pick |
| E6 | Replace the existing pick: free the old slot and save the new one |

### 1.3 Complete decision table (2⁵ = 32 combinations)

| # | C1 | C2 | C3 | C4 | C5 | Effect | Reduced rule |
|---|---|---|---|---|---|---|---|
| 1 | T | T | T | T | T | E6 Replace existing pick (free old slot) | R6 |
| 2 | T | T | T | T | F | E5 Save new pick | R5 |
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
| R5 | T | T | T | T | F | E5 Save new pick | 1 (#2) |
| R6 | T | T | T | T | T | E6 Replace existing pick | 1 (#1) |

Check: 16 + 8 + 4 + 2 + 1 + 1 = 32.

### 1.5 Test cases (one per reduced rule)

Setup: Technician **T07** (M Electric only, Certification expiry 30 Jun). Planning Week Mon 19 – Sat 24. **T03** already holds Wed 21 / Dicon.

| TC | Rule | Inputs (now, day, Brand, other state) | Expected output |
|---|---|---|---|
| BB-01 | R1 | Now Wed 7, 18:00; Tue 20; M Electric | Refused: "This week is locked". No record saved |
| BB-02 | R2 | Now Mon 5, 10:00; Thu 22 where T07 has a Leave Record (MC); M Electric | Refused: "You are not available that day" |
| BB-03 | R3 | Now Mon 5, 10:00; Tue 20; **Dicon**; T07 Available | Refused: "You are not certified for this Brand on that day" |
| BB-04 | R4 | Now Mon 5, 10:00; Wed 21; M Electric; **T09 already holds Wed 21 / M Electric** | Refused: "This slot has just been taken" |
| BB-05 | R5 | Now Mon 5, 10:00; Tue 20; M Electric; T07 has no pick this week | Saved: T07 → Tue 20 / M Electric. Tue 20's M Electric slot shows as taken |
| BB-06 | R6 | Now Mon 5, 10:00; Fri 23; M Electric; T07 already holds Tue 20 / M Electric | Saved: T07 → Fri 23 / M Electric. Tue 20's M Electric slot is free again |

Extra boundary checks (equivalence partitions and boundary values, not required by the template): C1 at 17:59 → passes and at 18:00 → fails. C3 with expiry equal to the day → passes and the day before → fails. A Dual-Certified Technician on a day where only the Dicon slot is free → can take Dicon (R5).

---

## 2. White-box testing: `CrewFormingService.classifyTechnicians()`

### 2.1 Method

`classifyTechnicians(day)` carries out FR-55 steps 1–4 for one working day. It drops Technicians who are not working, puts Standby picks and Dual-Certified Technicians with 20 h or more last week on Standby, and splits everyone else into an under-40 h group and a 40 h-or-more group. Each group is then ordered by `WorkloadRanking` (the Strategy, report §3.2).

### 2.2 Pseudocode

```text
classifyTechnicians(day):
 1  standby ← []; ranked ← []; bottom ← []
 2  for each t in activeTechnicians():
 3      if not t.isWorkingOn(day) then          // Unavailable, Not submitted or Leave Record
 4          continue
 5      if hasStandbyPick(t, day) then
 6          standby.add(t, Preference)
 7      else if t.isDual(day) and t.lastWeekHours(week) >= 20 then
 8          standby.add(t, Algorithm)           // treated as based in Central
 9      else if t.projectedWeekHours(day) >= 40 then
10          bottom.add(t)
11      else
12          ranked.add(t)
13  end for
14  ranked ← ranking.order(ranked, day)        // last week, projected hours, staff ID
15  bottom ← ranking.order(bottom, day)
16  return (ranked + bottom, standby)
```

Line 7 is a short-circuit `and`, so it becomes **two** decision nodes in the CFG (N7 `isDual`, N8 `>= 20`).

### 2.3 Control flow graph

Source: [diagrams/CFG-classify-technicians.puml](../diagrams/CFG-classify-technicians.puml).

| Node | Pseudocode line(s) | Kind |
|---|---|---|
| N1 | 1 | Statement |
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
| WB-04 | B4 | T05, Available, Standby pick Wed 21 / Dicon | standby = [T05 (Preference)]; ranked = [] |
| WB-05 | B5 | T01, Dual-Certified, Available, no pick, last week **19.5 h**, projected 16 h | ranked = [T01]; standby = [] |
| WB-06 | B6 | T02, Dual-Certified, Available, no pick, last week **20 h** | standby = [T02 (Algorithm, Central)]; ranked = [] |
| WB-07 | B7 | T06, Dicon only, Available, no pick, projected **40 h** | ranked = [T06] (from the 40 h-or-more group, so placed after any under-40 h Technician); standby = [] |

WB-05/WB-06 test the 20 h boundary (19.5 vs 20) and WB-07 tests the 40 h ranking boundary (DEC-86). A further integration case with all of T01–T06 checks the final order: under-40 h first by last week's hours, then the 40 h-or-more group.
