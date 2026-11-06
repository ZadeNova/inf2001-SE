# UC-07: Allocate Jobs / Set Weekly Schedule

> **Status: M2 v1.0 (2026-11-06).** Starts from the system's Suggested Roster (FR-55). The Manager reviews and edits it, sets Crew zones, allocates Jobs and publishes (DEC-80).

| Field | Value |
|---|---|
| **ID** | UC-07 |
| **Name** | Allocate Jobs / Set Weekly Schedule |
| **Primary actor** | Manager |
| **Secondary actors** | Email Service, SMS Gateway «system» through UC-15 |
| **Description** | The Manager prepares one Planning Week: generates the Suggested Roster, edits Crews and Standby, sets zones, allocates and times Jobs, resolves warnings and publishes the Weekly Roster. |
| **Trigger** | Planning starts on the Thursday after the Availability Deadline. |
| **Extension point** | **Compare Staff:** at steps 3–5, when the Manager selects Staff to compare (UC-08) |
| **Linked requirements** | FR-26, FR-27, FR-07, FR-08, FR-32, FR-33, FR-34, FR-09, FR-10, FR-11, FR-35, FR-36, FR-30, FR-55 |
| **Source** | Brief R3–R6; INT-MGR [Process Q1], [System Q4]; M2-Brief §4; DEC-16; DEC-19; DEC-80; DEC-81; DEC-82; DEC-84; DEC-85 |
| **Classes** | JobAllocationPage, RosterController, CrewFormingService, TechnicianRanking, WorkloadRanking, RuleValidator, NotificationService, WeeklyRoster, Crew, Standby, Assignment, Job, VanAvailability, LeaveRecord, StandbyPreference, AuditLog |
| **Wireframe** | W-06 Job Allocation; W-07 Compare Staff |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in.
2. The Planning Week is Draft and its Availability Deadline has passed.
3. The HR CSV and van CSV for the week have been uploaded (UC-16, assumption A4).

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Planning Week. | Shows each day with its Van Availability, Unassigned Jobs and any existing Draft Crews (FR-07, FR-34, FR-11). |
| 2 | Chooses "Suggest roster". | `CrewFormingService.suggestRoster(week)` forms Draft Crews (Van 1…n), Drivers and Standby Staff for each day and logs the run (FR-55). |
| 3 | Reviews each day; sets each Crew's zone; changes Crew members or Standby where needed. | `RosterController.setCrewZone()`, `changeCrew()`, `nameStandby()`/`removeStandby()`. `RuleValidator.checkCrew()` blocks FR-32 violations and `checkWarnings()` raises FR-33 warnings. Each change is logged as an override with a reason (FR-09). |
| 4 | Drags an Unassigned Job onto a Crew and sets the start time. | `RosterController.allocateJob()` creates the Assignment after `RuleValidator.checkAssignment()` checks Brands, times and the zone match (FR-27, FR-08, FR-32, FR-33). |
| 5 | Repeats steps 3–4. | Recalculates Workload with the 40 h highlight (FR-35, FR-36). |
| 6 | Chooses Publish. | Refuses any FR-32 violation and lists outstanding warnings. |
| 7 | Confirms, giving a reason for each overridden warning. | `WeeklyRoster.publish()`; notifies every Staff member with an Assignment or Standby day through UC-15 (FR-09, FR-39). |

## Alternative flows

### A1: Compare Staff (extension point, steps 3–5)

1. The Manager selects up to three Staff, and UC-08 runs.

### A2: Fewer than 3 Crews or no Full Standby cover (branches at step 2 or 3)

1. The suggestion has already pulled Standby Staff back in, lowest-ranked first, without using Standby picks (FR-55 step 6).
2. The system warns. The Manager accepts with a reason or edits the day (FR-33).

### A3: Regenerate (branches at step 3)

1. The Manager runs the suggestion again. The previous suggestion for the week is replaced, and the run is logged.

### A4: Revise a Published roster (branches at step 1)

1. For today or future dates, the Manager adds, moves or unassigns Jobs or changes Crews or Standby.
2. Validation runs again and the affected Staff are notified through UC-15 (FR-10).

## Exception flows

### E1: Blocking violation (steps 3–6)

1. The system explains the FR-32 rule and refuses the change.

### E2: No van CSV for a day (step 1)

1. The system warns and treats that day's Van count as unknown. The Manager uploads the file (UC-16) or overrides with a reason (FR-33).

### E3: Save fails

1. The system follows NFR-06; an unsaved roster change is not shown as complete.

## Postconditions

- **Success:** A valid Weekly Roster exists, Draft or Published, with Crews, zones, Standby and timed Assignments. Every Manager override is logged.
- **Failure:** Invalid changes are not applied.

## Business rules / notes

- The system suggests and the Manager decides (SRS §2.5).
- Drivers are placed by staff ID only (assumption A1, DEC-82).
- Changes during the running week that involve replacements or hours are made in UC-17.
