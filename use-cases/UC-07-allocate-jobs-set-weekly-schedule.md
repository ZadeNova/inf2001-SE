# UC-07: Allocate Jobs / Set Weekly Schedule

> **Status: M2 v1.1 (2026-11-07).** SRS v4.1; DEC-96–98. Confirm provisional preferences after capacity checks, then suggest the roster.

| Field | Value |
|---|---|
| **ID** | UC-07 |
| **Name** | Allocate Jobs / Set Weekly Schedule |
| **Primary actor** | Manager |
| **Secondary actors** | Email Service, SMS Gateway through UC-15 |
| **Description** | Prepare a Draft week with binding confirmed preferences, valid initial Crews, coverage zones, Standby and timed Jobs; review and publish. |
| **Trigger** | Thursday planning after the Availability Deadline. |
| **Extension point** | Compare Staff: optional during steps 3–5 (UC-08). |
| **Linked requirements** | FR-07–FR-11, FR-26, FR-27, FR-30–FR-36, FR-51, FR-55 |
| **Source** | Brief R3–R6; DEC-16, DEC-19, DEC-80, DEC-82, DEC-84, DEC-85, DEC-96–98 |
| **Classes** | JobAllocationPage, RosterController, StandbyPreferenceController, CrewFormingService, RuleValidator, TechnicianRanking, WorkloadRanking, NotificationService, WeeklyRoster, Crew, Standby, Assignment, Replacement, Job, VanAvailability, LeaveRecord, StandbyPreference, AuditLog |
| **Wireframe** | W-06; W-07 |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in; the Planning Week is Draft and its Availability Deadline has passed.
2. The week's HR and Van CSVs are present (UC-16). No suggestion or preference confirmation uses an unknown Van count.

## Main flow

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Planning Week. | Shows CSV readiness, provisional/decided preferences, Crews, Standby and Unassigned Jobs. |
| 2 | Chooses Suggest roster. | RosterController.prepareSuggestion() calls StandbyPreferenceController.confirmWeek(): resolve provisional requests in submission order using current eligibility and feasible >=3 Crews plus Full Standby cover. Persist decisions/reasons and notify once (FR-51). CrewFormingService.suggestRoster() then reserves confirmed picks and follows FR-55. |
| 3 | Reviews Crew members, Standby and coverage zones. | Set one or more existing Zones per Crew. Permit valid edits with audit reasons; block changes to confirmed initial Standby placements (FR-26, FR-32). |
| 4 | Allocates an Unassigned Job to a Crew and sets its time. | Check Brand, availability and time/travel rules. Copy the effective Crew members into the Assignment's attributed Staff (FR-07/08/27). |
| 5 | Optionally compares Staff and repeats allocation. | Show Active Hours separately from Total Credited Workload; apply the 40 h highlight to the latter (FR-31/35/36). |
| 6 | Chooses Publish. | Recheck >=3 valid initial Crews/day, confirmed picks and every FR-32 rule. List only overridable FR-33 warnings. |
| 7 | Confirms permitted warnings with reasons. | Publish, audit and notify Staff with Assignments/Standby; do not send preference-decision notifications a second time (FR-09/39). |

## Alternative flows

### A1: Compare Staff
UC-08 runs at the extension point.

### A2: Capacity shortage
1. Recall eligible Algorithm/Leftover Staff before conceding a shortage. Confirmed picks remain reserved.
2. Use the feasible minimum arrangement if greedy pairing strands a Brand.
3. Fewer than three valid initial Crews: show shortage and block publication.
4. Three Crews but no Full Standby cover: no further preference confirmations; warn and allow the Manager to acknowledge missing cover (FR-33). Direct duties do not count as initial Crews.

### A3: Regenerate
Only an unedited Draft suggestion without Job allocations can be regenerated. Preserve confirmed preference decisions, avoid duplicate notification and log the run. Otherwise explain that existing Jobs/manual edits must be resolved explicitly; discard nothing.

### A4: Revise a Published roster
For today/future dates, change only unstarted Jobs/initial future placements within FR-32/33. Changes needing direct Standby duties or replacements use UC-17. Earlier attribution remains unchanged; notify affected Staff.

## Exceptions

- Missing CSV: show missing dates and return to UC-16; do not guess capacity.
- Invalid edit or attempt to override a confirmed pick: refuse even if a reason is supplied.
- Later Leave/account change: show shortage and require repair while preserving confirmed-request history and earlier Job attribution.
- Save failure: NFR-06; no partial roster/confirmation state or premature notification.

## Postconditions

A Draft or Published roster exists with traceable preference decisions, Crew coverage, per-Job Staff and derived hours. Three is the minimum, not a fixed Crew count. Driver assignment remains staff-ID order under A1.
