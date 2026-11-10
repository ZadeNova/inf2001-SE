# UC-09: Decide Job Rejection Request

> **Status: M2 v1.1 (2026-11-07).** Renamed from "Manage Staff Request". Leave and Late Availability decisions are removed (DEC-73, DEC-83, DEC-91). File name kept for link stability.

| Field | Value |
|---|---|
| **ID** | UC-09 |
| **Name** | Decide Job Rejection Request |
| **Primary actor** | Manager |
| **Secondary actors** | Email Service, SMS Gateway «system» through UC-15; Clock (lapse at Job start) |
| **Description** | The Manager approves or refuses an attributed Staff member's Job Rejection Request. |
| **Trigger** | A pending request appears on the Manager's Landing Page, or the Job's start time arrives while it is pending. |
| **Linked requirements** | FR-05, FR-34, FR-40, FR-38, FR-39, FR-49 |
| **Source** | Brief R10; INT-MGR [Conflicts Q3]; DEC-42; DEC-59; DEC-66; DEC-91 |
| **Classes** | RequestReviewPage, RequestController, JobRejectionRequest, Assignment, Job, NotificationService, AuditLog |
| **Wireframe** | W-16 Request review |
| **Status** | Agreed |

## Preconditions

1. A Job Rejection Request is Pending (UC-12).

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens pending requests. | Lists Pending Job Rejection Requests with the Job, date, Crew or direct Technician, reason and comment (FR-40). |
| 2 | Chooses Approve or Refuse, optionally with a reason. | `RequestController.decideJobRejection()`. |
| 3 | — | **Approve:** `JobRejectionRequest.approve()` and `Job.markUnassigned()`; the Job leaves its Crew or direct allocation and the Unassigned count rises (FR-34). **Refuse:** `refuse(reason)`; the Assignment stands. |
| 4 | — | Logs the decision and notifies the requester and affected attributed Staff through UC-15 (FR-39, FR-49). |

## Alternative flows

### A1: Job starts while still Pending (Clock)

1. `RequestController.onJobStart()` calls `JobRejectionRequest.lapse()`. The Assignment stands and the requester is notified (FR-38).

### A2: Approved, and the Crew needs a replacement

1. The Manager continues in UC-17 to place a Standby if needed.

## Exception flows

### E1: The request is no longer Pending

1. The system shows its current state and applies no second decision.

### E2: Save fails

1. The system follows NFR-06 and leaves the request Pending.

## Postconditions

- **Success:** The request is Approved, Refused or Lapsed, logged, and notified.

**v1.1 basis:** DEC-96–98; SRS v4.1. Historical M1 sequence sources require review before reuse.
