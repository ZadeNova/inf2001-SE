# UC-09: Manage Staff Request

> **Status: Draft v0.2 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-09 |
| **Name** | Manage Staff Request |
| **Primary actor** | Manager |
| **Secondary actors** | Email/Phone through UC-15 |
| **Description** | The Manager reviews and decides Leave, Late Availability Change and Job Rejection Requests submitted by Staff. |
| **Trigger** | A pending Staff request appears on the Manager's Landing Page. |
| **Linked requirements** | FR-17, FR-23 to FR-25, FR-46, FR-63, FR-64, FR-70 |
| **Source** | Brief R10; INT-MGR [Process Q4], [Conflicts Q2], [Conflicts Q3], [System Q1 follow-up: landing page]; INT-DRV [Q15]; DEC-02; DEC-13; DEC-19; DEC-42; DEC-43; DEC-45; DEC-47 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The Manager is logged in.
2. A request submitted through UC-12 is pending.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens pending requests. | Lists Leave, Late Availability Change and Job Rejection Requests; Short-notice rejection requests are highlighted (FR-56). |
| 2 | Selects a request. | Shows request details and the current roster impact. |
| 3 | Chooses Approve or Reject/Refuse and supplies a reason where required. | Validates the decision and checks affected roster rules (FR-23, FR-24, FR-44). |
| 4 | Confirms the decision. | Applies the request-specific outcome and records the decision. |
| 5 | — | Invokes UC-15 for the requester and any other affected Staff (FR-64). |

## Alternative flows

### A1: Approve Leave (branches at step 4)

1. The system deducts working days from the seven-day annual balance and marks them as Leave (FR-24, FR-25).
2. If an existing Crew is affected, the system applies FR-70 after warning the Manager.

### A2: Decide Late Availability Change (branches at step 4)

1. Approval updates the requested Slots and applies FR-70 if a Crew becomes invalid.
2. Rejection leaves Availability unchanged (FR-17).

### A3: Decide Job Rejection Request (branches at step 4)

1. Approval makes the Job Unassigned, removes it from the Van and updates the Unassigned count (FR-46, FR-63).
2. Refusal leaves the Assignment in place.
3. A pending request lapses when its Job starts and the Assignment remains (FR-63).

## Exception flows

### E1: Leave rejection has no reason (branches at step 3)

1. The system refuses the decision until the Manager enters a reason (FR-23).

### E2: Request is no longer pending (branches at step 4)

1. The system displays the current state and does not apply a second decision.

### E3: Save fails

1. The system follows NFR-09 and leaves the request pending.

## Postconditions

- **Success:** The request has a final or lapsed status, resulting data is updated, and required notifications are issued.
- **Failure:** The request remains pending and operational data is unchanged.

## Business rules / notes

- Staff submission belongs to UC-12; the Manager decision belongs here.
- The Manager cannot directly overwrite Staff Availability (DEC-45).

## Open questions

- Confirm whether exactly 48 hours before a Job counts as Short notice.
