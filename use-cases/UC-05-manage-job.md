# UC-05: Manage Job

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-05 |
| **Name** | Manage Job |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager creates, edits, links or cancels a Job while the system preserves valid status transitions and records. |
| **Trigger** | Customer work must be recorded or an existing Job must change. |
| **Linked requirements** | FR-01 to FR-05, FR-32, FR-39, FR-50, NFR-06 |
| **Source** | INT-MGR [Process Q2], [Process Q2 follow-up: hours], [added follow-up: cancellations], [Conflicts Q3], [Conflicts Q4]; INT-DCT [Questionnaire C5]; INT-DRV [Q2]; DEC-11; DEC-19; DEC-22; DEC-34; DEC-40; DEC-42; DEC-58; DEC-67; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-05](../diagrams/SD-05-manage-job.puml) |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in.
2. For edit, link or cancellation, the target Job exists and is not Completed.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Chooses to create a Job. | Displays required and optional Job fields (FR-01). |
| 2 | Enters customer, address, Brand, Job Type, unit count, preferred date and Slot. | Pre-fills duration from the Standard Duration (FR-02). |
| 3 | Adjusts duration or optional details and submits. | Validates required data, a positive unit count and a Monday–Saturday preferred date. |
| 4 | — | Creates the Job as Unassigned and preserves the FR-05 status model. |
| 5 | Reviews the saved Job. | Shows it in the Unassigned Job list for UC-07 (FR-34). |

## Alternative flows

### A1: Link Jobs (branches at step 3)

1. The Manager selects Jobs of different Brands at the same address.
2. The system links them and enforces same-Van and same-date allocation (FR-03).

### A2: Edit a Job (branches at step 1)

1. The Manager changes a non-Completed Job.
2. The system rechecks an Assigned Job against FR-32.
3. A valid edit is saved; an invalidating edit returns the Job to Unassigned and states why (FR-04).

### A3: Cancel a Job (branches at step 1)

1. The Manager confirms cancellation of an Unassigned or Assigned Job.
2. The system sets Cancelled, removes it from active allocation, and notifies affected Crew members through UC-15 (FR-04, FR-05, FR-39).

## Exception flows

### E1: Invalid or final-state change (branches at steps 3 or A2/A3)

1. The system refuses missing required fields, zero units, a Sunday date, or any change from Completed or Cancelled (FR-01, FR-05).

### E2: Save fails

1. The system follows NFR-06.

## Postconditions

- **Success:** The Job is created, changed, linked or cancelled with a valid status and audit record.
- **Failure:** The prior Job data and status remain unchanged.

## Business rules / notes

- Records dated in the past or in progress cannot be deleted; cancellation preserves the record (FR-50).
- Allocation and scheduling belong to UC-07.
- Link validation refuses same-Brand Jobs, different addresses or conflicting existing Van/date placements. Draft roster payloads are withheld centrally by SD-20; Published Assigned-Job changes still notify after saving.

## Open questions

- Confirm whether non-status fields of a Cancelled Job remain editable.

## Linked Jobs rules

An invalid edit that unassigns a Job also unassigns its active Linked partners. Cancellation cancels only the selected Job and unassigns active Linked partners; Completed/Cancelled partners remain unchanged. End affected placements and audit atomically, then notify eligible affected Staff after commit (FR-03/04/05).
