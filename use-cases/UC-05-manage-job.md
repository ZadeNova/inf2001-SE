# UC-05: Manage Job

> **Status: Draft v0.1 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-05 |
| **Name** | Manage Job |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager creates, edits, links or cancels a Job while the system preserves valid status transitions and records. |
| **Trigger** | Customer work must be recorded or an existing Job must change. |
| **Linked requirements** | FR-34 to FR-38, FR-44, FR-64, FR-67, NFR-09 |
| **Source** | INT-MGR [Process Q2], [Process Q2 follow-up: hours], [added follow-up: cancellations], [Conflicts Q3], [Conflicts Q4]; INT-DCT [Questionnaire C5]; INT-DRV [Q2]; DEC-11; DEC-19; DEC-22; DEC-34; DEC-40; DEC-42; DEC-58 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-05](../diagrams/SD-05-manage-job.puml) |
| **Status** | Draft |

## Preconditions

1. The Manager is logged in.
2. For edit, link or cancellation, the target Job exists and is not Completed.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Chooses to create a Job. | Displays required and optional Job fields (FR-34). |
| 2 | Enters customer, address, Brand, Job Type, unit count, preferred date and Slot. | Pre-fills duration from the Standard Duration (FR-35). |
| 3 | Adjusts duration or optional details and submits. | Validates required data, a positive unit count and a Monday–Saturday preferred date. |
| 4 | — | Creates the Job as Unassigned and preserves the FR-38 status model. |
| 5 | Reviews the saved Job. | Shows it in the Unassigned Job list for UC-07 (FR-46). |

## Alternative flows

### A1: Link Jobs (branches at step 3)

1. The Manager selects Jobs of different Brands at the same address.
2. The system links them and enforces same-Van and same-date allocation (FR-36).

### A2: Edit a Job (branches at step 1)

1. The Manager changes a non-Completed Job.
2. The system rechecks an Assigned Job against FR-44.
3. A valid edit is saved; an invalidating edit returns the Job to Unassigned and states why (FR-37).

### A3: Cancel a Job (branches at step 1)

1. The Manager confirms cancellation of an Unassigned or Assigned Job.
2. The system sets Cancelled, removes it from active allocation, and notifies affected Crew members through UC-15 (FR-37, FR-38, FR-64).

## Exception flows

### E1: Invalid or final-state change (branches at steps 3 or A2/A3)

1. The system refuses missing required fields, zero units, a Sunday date, or any change from Completed or Cancelled (FR-34, FR-38).

### E2: Save fails

1. The system follows NFR-09.

## Postconditions

- **Success:** The Job is created, changed, linked or cancelled with a valid status and audit record.
- **Failure:** The prior Job data and status remain unchanged.

## Business rules / notes

- Records dated in the past or in progress cannot be deleted; cancellation preserves the record (FR-67).
- Allocation and scheduling belong to UC-07.

- Link validation refuses same-Brand Jobs, different addresses or conflicting existing Van/date placements. Draft roster payloads are withheld centrally by SD-15; Published Assigned-Job changes still notify after saving (DEC-58).

## Open questions

- Confirm whether non-status fields of a Cancelled Job remain editable.


## Round-3 Linked Jobs clarification

An invalid edit that unassigns a Job also unassigns its active Linked partners. Cancellation cancels only the selected Job and unassigns active Linked partners; Completed/Cancelled partners remain unchanged. End affected placements and audit atomically, then notify eligible affected Staff after commit (FR-36/37/38; DEC-67).
