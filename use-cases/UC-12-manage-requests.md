# UC-12: Submit Job Rejection Request

> **Status: M2 v1.1 (2026-11-07).** Renamed from "Manage Requests". Leave and late-change submissions are removed, and Short notice is retired (DEC-73, DEC-83, DEC-90, DEC-91). File name kept for link stability.

| Field | Value |
|---|---|
| **ID** | UC-12 |
| **Name** | Submit Job Rejection Request |
| **Primary actor** | Staff |
| **Secondary actors** | Email Service, SMS Gateway «system» through UC-15 (Manager alert) |
| **Description** | An attributed Staff member asks for a Crew or direct Job to be unassigned, after a warning to discuss it with the Manager first. |
| **Trigger** | An attributed Staff member cannot do an assigned Job, or knows ahead of time that it can't be done. |
| **Linked requirements** | FR-41, FR-37, NFR-12 |
| **Source** | Brief R10, §Intro ¶3; INT-MGR [Conflicts Q3]; INT-DRV [Q17]; DEC-42; DEC-66 |
| **Classes** | RequestPage, RequestController, JobRejectionRequest, Assignment, NotificationService |
| **Wireframe** | W-15 Job rejection (warning dialog) |
| **Status** | Agreed |

## Preconditions

1. The Staff member is logged in and holds the Assignment in a Published week.
2. The Job has not started.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Assignment and chooses Reject. | Shows a warning: "Please discuss this with your Manager before rejecting." |
| 2 | Confirms the warning. | Shows the reasons: Personal emergency, Missing equipment or parts, Other. |
| 3 | Picks a reason (with a comment if Other) and submits. | `RequestController.submitRejection()` creates a Pending `JobRejectionRequest` and notifies the Manager (FR-37). |
| 4 | — | Shows the status "Pending" on the Staff Landing Page (FR-41). The Job stays Assigned until UC-09. |

## Exception flows

### E1: Cancels at the warning (step 2)

1. Nothing is saved.

### E2: "Other" without a comment (step 3)

1. Submission is refused.

### E3: Job is not eligible (step 1 or 3)

1. Refuse a Job not attributed to this Staff member, outside the Published week, no longer Assigned, or already started (FR-37).

### E4: Another request is already Pending for this Assignment (step 3)

1. Submission is refused and the existing request's status is shown (DEC-66).

### E5: Submission fails

1. The system follows NFR-06 and does not show a Pending request unless saved.

## Postconditions

- **Success:** A Pending request exists for UC-09.
- **Failure:** Nothing changes.

**v1.1 basis:** DEC-96–98; SRS v4.1. Historical M1 sequence sources require review before reuse.
