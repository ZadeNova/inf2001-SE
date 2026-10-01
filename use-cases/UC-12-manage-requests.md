# UC-12: Manage Requests

> **Status: Draft v0.1 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-12 |
| **Name** | Manage Requests |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | Staff submit and review their Leave, Late Availability Change and Job Rejection Requests. |
| **Trigger** | A Staff member needs Leave, needs to change a locked week's Availability, or wants a Job removed from the Crew's Van. |
| **Linked requirements** | FR-17, FR-22, FR-25, FR-58, FR-62 |
| **Source** | Brief R10, §Company ¶1, ¶4; INT-MGR [Process Q4], [Conflicts Q2], [Conflicts Q3]; INT-DCT [Process Q2], [Process Q3]; INT-DRV [Q15], [Q17]; DEC-02; DEC-13; DEC-42; DEC-45 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The Staff member is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Requests and selects the request type. | Displays the corresponding form and current request statuses. |
| 2 | Enters the required dates, Slots, Job and/or reason. | Validates request-type rules. |
| 3 | Reviews the summary and submits. | Creates a pending request shown on the Manager's Landing Page (FR-56). |
| 4 | Reviews the pending status. | Keeps operational data unchanged until UC-09 decides the request. |

## Alternative flows

### A1: Submit Leave Request (branches at step 1)

1. The Staff member selects full working days and may add a note.
2. The system rejects overlap or a request exceeding the remaining seven-day annual balance (FR-22, FR-25).

### A2: Submit Late Availability Change Request (branches at step 1)

1. The Staff member selects one or more locked-week Slots, the new Availability and a reason.
2. The system requires the reason and creates a pending request (FR-17).

### A3: Submit Job Rejection Request (branches at step 1)

1. The Staff member selects a Job assigned to the Crew's Van in a Published week.
2. The system warns the Staff member to discuss it with the Manager first.
3. The Staff member selects Personal emergency, Missing equipment or parts, or Other; Other requires a comment.
4. Within 48 hours of the Job start, the system requires a written explanation and marks the request Short notice (FR-62).

## Exception flows

### E1: Required information is missing (branches at step 2)

1. The system identifies the missing reason, comment, explanation or date and refuses submission.

### E2: Job is not eligible (branches at A3 step 1)

1. The system refuses a Job outside the Staff member's Crew or outside a Published week (FR-62).

### E3: Submission fails

1. The system follows NFR-09 and does not show a pending request unless saved.

## Postconditions

- **Success:** A valid request is pending for UC-09 and visible to the Staff member.
- **Failure:** No request is created and Availability, Leave and Assignments remain unchanged.

## Business rules / notes

- Staff submit; the Manager decides through UC-09.
- While a Job Rejection Request is pending, the Job stays Assigned (FR-63).

## Open questions

- Confirm whether exactly 48 hours before the Job start is Short notice.
