# UC-14: Complete Job

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-14 |
| **Name** | Complete Job |
| **Primary actor** | Technician |
| **Secondary actors** | None |
| **Description** | A Technician on the assigned Crew records actual work details and a signed-invoice photo to complete a Job. |
| **Trigger** | Work on an Assigned Job has finished. |
| **Linked requirements** | FR-05, FR-06, FR-35, NFR-05, NFR-06 |
| **Source** | INT-DCT [Questionnaire C17/C18], [Questionnaire C18/C19], [Questionnaire C9]; INT-MGR [Process Q1 follow-up: completion], [Clarification Q7]; DEC-40; DEC-47; DEC-69; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-19](../diagrams/SD-19-complete-job.puml) |
| **Status** | Agreed |

## Preconditions

1. The Technician is logged in and belongs to the Job's Van Crew.
2. The Job has status Assigned.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Assigned Job and chooses Complete. | Shows actual start/end, remark, follow-up and invoice-photo fields. |
| 2 | Enters actual start and end times, a short remark and whether follow-up is needed. | Validates that both times are on the Job date and end is after start (FR-06). |
| 3 | Attaches a photo of the customer-signed invoice. | Validates that the mandatory photo is present (FR-06). |
| 4 | Submits completion. | Rechecks Assigned state and completion authority in the atomic save. Saves details/photo together, sets Completed and calculates Actual Hours as elapsed work plus 0.5 h (FR-05, FR-06, FR-35). |
| 5 | Reviews confirmation. | Replaces Planned Hours with Actual Hours in Crew Workload. |

## Alternative flows

### A1: Complete while offline (branches at step 4)

1. The system retains completion details and the invoice photo locally, showing each queued Job as local/waiting with photo status. A local save is not a server completion.
2. When the connection returns, it shows Uploading and automatically submits through the same validation/save path (NFR-05). Confirm Received only after details and photo are saved. Failure identifies what failed and retains the item for retry without retyping or losing the photo (NFR-06).

## Exception flows

### E1: Actor is a Driver or outside the Crew (branches at step 1)

1. The system refuses access to completion (FR-06, NFR-09).

### E2: Invalid times or missing photo (branches at steps 2 or 3)

1. The system identifies the error and refuses submission.

### E3: Online submission fails (branches at step 4)

1. The system follows NFR-06.

## Postconditions

- **Success:** The Job is Completed, evidence is stored and Workload uses Actual Hours.
- **Failure:** No new completion is applied. A locally queued item is labelled awaiting upload or failed and retained for retry; the server Job remains Assigned unless another valid action changes it.

## Business rules / notes

- Completed is a final Job status (FR-05). Repeated taps/retries cannot complete the Job or credit hours twice. If already Completed, show the current outcome and retain any unconfirmed queued evidence for reconciliation.
- Hours remain credited to the Crew that held the completed work (FR-28).

## Open questions

- Define reconciliation if the Job/Crew changes or another Technician completes the Job before a queued offline completion uploads. Do not silently overwrite or discard the retained item.
