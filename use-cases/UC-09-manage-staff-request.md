# UC-09: Manage Staff Request

> **Status: Draft v0.3 (2026-10-04).**

| Field | Value |
|---|---|
| **ID** | UC-09 |
| **Name** | Manage Staff Request |
| **Primary actor** | Manager |
| **Secondary actors** | Email/Phone through UC-15; Clock for independent Job-start lapse (DEC-59, DEC-68) |
| **Description** | The Manager reviews and decides Leave, Late Availability Change and Job Rejection Requests submitted by Staff. |
| **Trigger** | A pending Staff request appears on the Manager's Landing Page, or Clock signals Job start for a Pending Job Rejection Request. |
| **Linked requirements** | FR-17, FR-23 to FR-25, FR-46, FR-63, FR-64, FR-70 |
| **Source** | Brief R10; INT-MGR [Process Q4], [Conflicts Q2], [Conflicts Q3], [System Q1 follow-up: landing page]; INT-DRV [Q15]; DEC-02; DEC-13; DEC-19; DEC-42; DEC-43; DEC-45; DEC-47; DEC-51; DEC-52; DEC-58; DEC-59; DEC-69 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-03](../diagrams/AD-03-job-rejection.puml); [SD-16](../diagrams/SD-16-handle-invalidated-crew.puml); [SD-20](../diagrams/SD-20-decide-leave-request.puml); [SD-21](../diagrams/SD-21-decide-late-availability-change.puml); [SD-22](../diagrams/SD-22-decide-job-rejection-request.puml) |
| **Status** | Draft |

## Preconditions

1. For Manager decisions, the Manager is logged in. The Clock-triggered lapse does not require a Manager session.
2. A request submitted through UC-12 is pending.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens pending requests. | Lists Leave, Late Availability Change and Job Rejection Requests; Short-notice rejection requests are highlighted (FR-56). |
| 2 | Selects a request. | Shows request details and the current roster impact; for a Late Availability Change Request, shows current Availability beside the proposed Slots and Pending status. |
| 3 | Chooses Approve or Reject/Refuse and supplies a reason where required. | Validates the decision and checks affected roster rules (FR-23, FR-24, FR-44). |
| 4 | Confirms the decision. | Applies the request-specific outcome and records the decision. |
| 5 | — | Invokes UC-15 for the requester and any other affected Staff (FR-64). |

## Alternative flows

### A1: Approve Leave (branches at step 4)

1. Inside the approval save, the system rechecks the remaining balance, refuses insufficient balance, then deducts working days and marks them as Leave/Unavailable (FR-22/24/25, DEC-58).
2. After warning and confirmation, apply FR-70 inside the same approval transaction; deliver returned notification events only after commit (DEC-58).

### A2: Decide Late Availability Change (branches at step 4)

1. Approval updates the requested Slots and applies FR-70 if a Crew becomes invalid.
2. Rejection leaves Availability unchanged (FR-17). Show the decision alongside the requested Slots and current Availability, including a reason when supplied (DEC-69).

### A3: Decide Job Rejection Request (branches at step 4)

1. Approval makes the Job Unassigned, removes it from the Van and updates the Unassigned count (FR-46, FR-63).
2. Refusal leaves the Assignment in place.
3. At Job start, the independent Clock event in SD-22 lapses a still-Pending request; the Assignment remains. Record and notify the newly saved lapse (FR-63, DEC-59).

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
- Later events that invalidate an existing Crew follow FR-70 rather than being blocked by FR-44 (DEC-51).
- Short notice means strictly less than 48 hours; exactly 48 hours is normal (DEC-52).

- Leave balance recheck/deduction and affected Crew changes share the approval transaction. Late Availability changes and Crew invalidation also commit together. SD-16 returns events; delivery follows commit. Clock-triggered lapse is drawn in SD-22, independent of Manager action, audited and notified after commit (DEC-58/59).

## Open questions

- Exactly 48 hours remains normal under DEC-52. Confirm whether Late Availability rejection and Job Rejection refusal reasons become mandatory, and whether request decision timestamps/history need additional fields (DEC-70). Leave rejection reasons remain required by FR-23.

## Round-3 clarification

Approval of a Job Rejection Request unassigns the requested Job and its active Linked partners atomically (DEC-67). Clock independently lapses the zero-or-one Pending request for a shared Assignment at Job start; no Manager session is required (DEC-59/66/68). Leave approval balance serialization is traced to DEC-65.
