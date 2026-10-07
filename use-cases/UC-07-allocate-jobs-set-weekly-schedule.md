# UC-07: Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster)

> **Status: Draft v0.3 (2026-10-04).** This merged use case includes forming Van Crews and publishing the Weekly Roster.

| Field | Value |
|---|---|
| **ID** | UC-07 |
| **Name** | Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster) |
| **Primary actor** | Manager |
| **Secondary actors** | Email/Phone through UC-15 |
| **Description** | The Manager prepares one Planning Week by forming daily Crews, naming Standby Staff, assigning and timing Jobs, resolving validation results and publishing the Weekly Roster. |
| **Trigger** | Planning begins for the next unpublished Planning Week or a current/future Published roster needs revision. |
| **Linked requirements** | FR-30, FR-32, FR-33, FR-41 to FR-46, FR-49 to FR-51, FR-53, FR-55, FR-64, FR-71 |
| **Source** | Brief R3 to R6; INT-MGR [Process Q1], [System Q2], [System Q4], [Conflicts Q1], [Conflicts Q2 follow-up: standby], [Conflicts Q5]; INT-DRV [Q5], [Q7]; DEC-09; DEC-10; DEC-16; DEC-19; DEC-31; DEC-32; DEC-39; DEC-43; DEC-45; DEC-47; DEC-51; DEC-69 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-01](../diagrams/AD-01-weekly-roster.puml); [SD-17](../diagrams/SD-17-form-crews-and-standby.puml); [SD-18](../diagrams/SD-18-allocate-job.puml); [SD-19](../diagrams/SD-19-publish-weekly-roster.puml) |
| **Status** | Draft |

## Preconditions

1. The Manager is logged in.
2. The next unpublished Planning Week exists.
3. Jobs to allocate exist with status Unassigned.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Planning Week. | Shows the weekly Van timeline, Unassigned Jobs, eligible Staff, Availability, Workload and existing Draft data (FR-41, FR-46, FR-51). |
| 2 | Selects a Van-day and chooses one Driver and one or two Technicians. | Validates Crew size, roles, Availability, double booking and Certifications (FR-30 to FR-32, FR-44). |
| 3 | Names eligible Standby Staff for the day. | Validates full-day Availability and absence from another Crew; warns when coverage is incomplete (FR-45, FR-71). |
| 4 | Selects an Unassigned Job, date and Van. | Checks the Planning Week, Crew, Van, Linked Jobs and Brand rules (FR-41, FR-44). |
| 5 | Sets the Job start time. | Calculates its working interval, lunch interruption and travel gap; blocks overlap (FR-42). |
| 6 | Repeats steps 2–5 until planning is complete. | Recalculates Workload and displays blocking errors and overridable warnings (FR-44, FR-45). |
| 7 | Chooses Publish. | Refuses any FR-44 violation and shows outstanding FR-45 warnings. |
| 8 | Confirms publication and any warning overrides. | Changes Draft to Published and invokes UC-15 for assigned and Standby Staff (FR-49, FR-64). |

## Alternative flows

### A1: Compare Staff (branches at step 2 or 4)

1. The Manager invokes UC-08 for up to three candidate Staff.
2. On return, the Manager continues Crew formation or allocation.

### A2: Change a Crew during the day (branches at step 2)

1. The Manager removes and adds Staff.
2. The system rechecks FR-30, FR-32 and FR-44 for every affected Crew, including the original Crew when a Technician is moved. It preserves completed-work credit and invokes UC-15 (FR-33, FR-64; INT-DCT [Questionnaire D2: DB01]; DEC-69).

### A3: Revise a Published roster (branches at step 1)

1. The Manager adds, moves or unassigns Jobs or changes Crews for current/future dates.
2. The system reruns validation, updates Workload and invokes UC-15 for affected Staff (FR-50).

## Exception flows

### E1: Blocking violation (branches at steps 2–7)

1. The system explains the FR-44 violation and refuses the change or publication.

### E2: Warning (branches at steps 3, 6 or 7)

1. The Manager may revise the schedule or override the warning.
2. The system logs an override with who, what and when (FR-45, FR-66).

### E3: Save fails

1. The system follows NFR-09; an unsaved roster change is not shown as complete.

## Postconditions

- **Success:** A valid Draft or Published Weekly Roster exists, with Crews, Standby and timed Assignments.
- **Failure:** Invalid changes are not applied and publication state does not change.

## Business rules / notes

- The Crew is fixed for a Van-day except for the FR-33 emergency change.
- Past roster dates are read-only.
- FR-70 is the later-event exception to FR-44; later approved Leave, approved Availability changes or Certification changes may leave an existing Crew marked Needs attention (DEC-51).
- Validation is embedded in this merged use case rather than represented as a separate use case (DEC-45).

## Open questions

- Resolved by DEC-51: FR-70 is the later-event exception to FR-44. No remaining open question in this draft.
