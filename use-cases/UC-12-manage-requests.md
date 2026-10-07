# UC-12: Manage Requests

> **Status: Draft v0.2 (2026-10-04).**

| Field | Value |
|---|---|
| **ID** | UC-12 |
| **Name** | Manage Requests |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | Staff submit and review their Leave, Late Availability Change and Job Rejection Requests. |
| **Trigger** | A Staff member needs Leave, needs to change a locked week's Availability, or wants a Job removed from the Crew's Van. |
| **Linked requirements** | FR-17, FR-22, FR-25, FR-58, FR-62 |
| **Source** | Brief R10, §Company ¶1, ¶4; INT-MGR [Process Q4], [Conflicts Q2], [Conflicts Q3]; INT-DCT [Process Q2], [Process Q3]; INT-DRV [Q15], [Q17]; DEC-02; DEC-13; DEC-42; DEC-45; DEC-52; DEC-58; DEC-59 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-02](../diagrams/AD-02-set-availability.puml); [AD-03](../diagrams/AD-03-job-rejection.puml); [SD-23](../diagrams/SD-23-submit-leave-request.puml); [SD-24](../diagrams/SD-24-submit-late-availability-change.puml); [SD-25](../diagrams/SD-25-submit-job-rejection-request.puml) |
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
4. When the Job starts in strictly less than 48 hours, the system requires a written explanation and marks the request Short notice; exactly 48 hours is normal (FR-62, DEC-52).

## Exception flows

### E1: Required information is missing (branches at step 2)

1. The system identifies the missing reason, comment, explanation or date and refuses submission.

### E2: Job is not eligible (branches at A3 step 1)

1. Refuse a Job outside the Staff member's Crew/Published week, no longer Assigned, already started, or with another Pending request for the same Assignment (FR-62/63, DEC-66).

### E3: Submission fails

1. The system follows NFR-09 and does not show a pending request unless saved.

## Postconditions

- **Success:** A valid request is pending for UC-09 and visible to the Staff member.
- **Failure:** No request is created and Availability, Leave and Assignments remain unchanged.

## Business rules / notes

- Staff submit; the Manager decides through UC-09.
- While a Job Rejection Request is pending, the Job stays Assigned (FR-63).

- A second Pending Job Rejection Request for the same Assignment is refused, even from another Crew member; recheck under the atomic save. Store the less-than-48-hour Short-notice flag. Historical decided requests remain. SD-23/25 start from Staff navigation; Job-start lapse is drawn in SD-22 (DEC-66/59).

## Open questions

- Resolved by DEC-52: exactly 48 hours is normal; Short notice means strictly less than 48 hours. No remaining open question in this draft.
