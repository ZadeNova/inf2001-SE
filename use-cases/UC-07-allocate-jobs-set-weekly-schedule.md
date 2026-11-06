# UC-07: Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster)

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-07 |
| **Name** | Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster) |
| **Primary actor** | Manager |
| **Secondary actors** | Email/Phone through UC-15 |
| **Description** | The Manager prepares one Planning Week by forming daily Crews, naming Standby Staff, assigning and timing Jobs, resolving validation results and publishing the Weekly Roster. |
| **Trigger** | Planning begins for the next unpublished Planning Week or a current/future Published roster needs revision. |
| **Linked requirements** | FR-07 to FR-11, FR-26 to FR-28, FR-30 to FR-36, FR-39 |
| **Source** | Brief R3 to R6; INT-MGR [Process Q1], [System Q2], [System Q4], [Conflicts Q1], [Conflicts Q2 follow-up: standby], [Conflicts Q5]; INT-DRV [Q5], [Q7]; DEC-09; DEC-10; DEC-16; DEC-19; DEC-31; DEC-32; DEC-39; DEC-43; DEC-45; DEC-47; DEC-51; DEC-69; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-01](../diagrams/AD-01-weekly-roster.puml); [SD-07](../diagrams/SD-07-form-crews-and-standby.puml); [SD-08](../diagrams/SD-08-publish-weekly-roster.puml) |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in.
2. The next unpublished Planning Week exists.
3. Jobs to allocate exist with status Unassigned.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Planning Week. | Shows the weekly Van timeline, Unassigned Jobs, eligible Staff, Availability, Workload and existing Draft data (FR-07, FR-34, FR-11). |
| 2 | Selects a Van-day and chooses one Driver and one or two Technicians. The Manager may optionally invoke **UC-08** to compare up to three candidate Staff before confirming the selection. | Validates Crew size, roles, Availability, double booking and Certifications (FR-26 to FR-27, FR-32). |
| 3 | Names eligible Standby Staff for the day. | Validates full-day Availability and absence from another Crew; warns when coverage is incomplete (FR-33, FR-30). |
| 4 | Selects an Unassigned Job, date and Van. | Checks the Planning Week, Crew, Van, Linked Jobs and Brand rules (FR-07, FR-32). |
| 5 | Sets the Job start time. | Calculates its working interval, lunch interruption and travel gap; blocks overlap (FR-08). |
| 6 | Repeats steps 2–5 until planning is complete, updating or re-allocating resources as needed. | Recalculates Workload and displays blocking errors and overridable warnings (FR-32, FR-33). |
| 7 | Chooses Publish. | Refuses any FR-32 violation and shows outstanding FR-33 warnings. |
| 8 | Confirms publication and any warning overrides. | Changes Draft to Published and invokes UC-15 for assigned and Standby Staff (FR-09, FR-39). |

## Alternative flows

### A1: Revise a Published roster (branches at step 1)

1. The Manager selects an existing Published roster for a current or future date, including making emergency or ad-hoc adjustments during an active working day. The Manager adds, moves or unassigns Jobs, or modifies existing Crews (FR-10, FR-28).
2. The system reruns validation for affected Jobs, Crews and assignments, recalculates Workload, and preserves completed-work credit where applicable (FR-32, FR-10). For mid-day Crew changes, the system rechecks the applicable Crew constraints for every affected Crew, including the original Crew when a Technician is moved (FR-26, FR-27, FR-28, FR-32).
3. The system applies valid changes and invokes **UC-15** to notify affected Staff (FR-10, FR-28, FR-39).

## Exception flows

### E1: Blocking violation (branches at steps 2–7)

1. The system explains the FR-32 violation and refuses the change or publication.

### E2: Warning (branches at steps 3, 6 or 7)

1. The Manager may revise the schedule or override the warning.
2. The system logs an override with who, what and when (FR-33, FR-49).

### E3: Save fails

1. The system follows NFR-06; an unsaved roster change is not shown as complete.

## Postconditions

- **Success:** A valid Draft or Published Weekly Roster exists, with Crews, Standby and timed Assignments.
- **Failure:** Invalid changes are not applied and publication state does not change.

## Business rules / notes

- The Crew is fixed for a Van-day except for the FR-28 emergency change.
- Past roster dates are read-only.
- FR-29 is the later-event exception to FR-32; later approved Leave, approved Availability changes or Certification changes may leave an existing Crew marked Needs attention.
- Validation is embedded in this merged use case rather than represented as a separate use case.

## Open questions

- None.
