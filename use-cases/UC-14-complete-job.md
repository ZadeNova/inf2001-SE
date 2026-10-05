# UC-14: Complete Job

> **Status: Draft v0.2 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-14 |
| **Name** | Complete Job |
| **Primary actor** | Technician |
| **Secondary actors** | None |
| **Description** | A Technician on the assigned Crew records actual work details and a signed-invoice photo to complete a Job. |
| **Trigger** | Work on an Assigned Job has finished. |
| **Linked requirements** | FR-38, FR-39, FR-53, NFR-08, NFR-09 |
| **Source** | INT-DCT [Process Q1 follow-up: completion], [System Q3], [Conflicts Q3]; INT-MGR [Process Q1 follow-up: completion], [Clarification Q7]; DEC-40; DEC-47 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-14](../diagrams/SD-14-complete-job.puml) |
| **Status** | Draft |

## Preconditions

1. The Technician is logged in and belongs to the Job's Van Crew.
2. The Job has status Assigned.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Assigned Job and chooses Complete. | Shows actual start/end, remark, follow-up and invoice-photo fields. |
| 2 | Enters actual start and end times, a short remark and whether follow-up is needed. | Validates that both times are on the Job date and end is after start (FR-39). |
| 3 | Attaches a photo of the customer-signed invoice. | Validates that the mandatory photo is present (FR-39). |
| 4 | Submits completion. | Sets the Job to Completed and calculates Actual Hours as elapsed work plus 0.5 h (FR-38, FR-53). |
| 5 | Reviews confirmation. | Replaces Planned Hours with Actual Hours in Crew Workload. |

## Alternative flows

### A1: Complete while offline (branches at step 4)

1. The system queues the completion with its photo locally.
2. When the connection returns, it submits the queued completion automatically (NFR-08).

## Exception flows

### E1: Actor is a Driver or outside the Crew (branches at step 1)

1. The system refuses access to completion (FR-39, NFR-12).

### E2: Invalid times or missing photo (branches at steps 2 or 3)

1. The system identifies the error and refuses submission.

### E3: Online submission fails (branches at step 4)

1. The system follows NFR-09.

## Postconditions

- **Success:** The Job is Completed, evidence is stored and Workload uses Actual Hours.
- **Failure:** The Job remains Assigned, except while a valid offline completion is explicitly queued.

## Business rules / notes

- Completed is a final Job status (FR-38).
- Hours remain credited to the Crew that held the completed work (FR-33).

## Open questions

- Define conflict handling if the Job changes before a queued offline completion is submitted.
