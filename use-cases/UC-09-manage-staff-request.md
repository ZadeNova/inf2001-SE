# UC-09: Manage Staff Request

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-09 |
| **Name** | Manage Staff Request |
| **Primary actor** | Manager |
| **Secondary actors** | Email/Phone through UC-15; Clock for independent Job-start lapse |
| **Description** | The Manager reviews and decides Leave, Late Availability Change and Job Rejection Requests submitted by Staff. |
| **Trigger** | A pending Staff request appears on the Manager's Landing Page, or Clock signals Job start for a Pending Job Rejection Request. |
| **Linked requirements** | FR-16, FR-19 to FR-21, FR-34, FR-38, FR-39, FR-29 |
| **Source** | Brief R10; INT-MGR [Process Q4], [Conflicts Q2], [Conflicts Q3], [System Q1 follow-up: landing page]; INT-DRV [Q15]; DEC-02; DEC-13; DEC-19; DEC-42; DEC-43; DEC-45; DEC-47; DEC-51; DEC-52; DEC-58; DEC-59; DEC-65; DEC-66; DEC-67; DEC-69; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-03](../diagrams/AD-03-job-rejection.puml); [SD-10](../diagrams/SD-10-decide-leave-request.puml); [SD-11](../diagrams/SD-11-decide-late-availability-change.puml); [SD-12](../diagrams/SD-12-decide-job-rejection-request.puml); [SD-21](../diagrams/SD-21-handle-invalidated-crew.puml) |
| **Status** | Agreed |

## Preconditions

1. For Manager decisions, the Manager is logged in. The Clock-triggered lapse does not require a Manager session.
2. A request submitted through UC-12 is pending.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens pending requests. | Lists Leave, Late Availability Change and Job Rejection Requests; Short-notice rejection requests are highlighted (FR-40). |
| 2 | Selects a request. | Shows request details and current roster impact; late changes show current Availability beside the proposed Slots and Pending status. |
| 3 | Chooses Approve or Reject/Refuse and supplies a reason where required. | Validates the decision and checks affected roster rules (FR-19, FR-20, FR-32). |
| 4 | Confirms the decision. | Applies the request-specific outcome and records the decision. |
| 5 | — | Invokes UC-15 for the requester and any other affected Staff (FR-39). |

## Alternative flows

### A1: Approve Leave (branches at step 4)

1. Inside the approval save, the system rechecks the remaining balance, refuses insufficient balance, then deducts working days and marks them as Leave/Unavailable (FR-18/20/21).
2. After warning and confirmation, apply FR-29 inside the same approval transaction; deliver returned notification events only after commit.

### A2: Decide Late Availability Change (branches at step 4)

1. Approval updates the requested Slots and applies FR-29 if a Crew becomes invalid.
2. Rejection leaves Availability unchanged (FR-16). Show the decision beside the requested Slots and current Availability, including a reason when supplied.

### A3: Decide Job Rejection Request (branches at step 4)

1. Approval makes the Job Unassigned, removes it from the Van and updates the Unassigned count (FR-34, FR-38).
2. Refusal leaves the Assignment in place.
3. At Job start, the independent Clock event in SD-12 lapses a still-Pending request; the Assignment remains. Record and notify the newly saved lapse (FR-38).

## Exception flows

### E1: Leave rejection has no reason (branches at step 3)

1. The system refuses the decision until the Manager enters a reason (FR-19).

### E2: Request is no longer pending (branches at step 4)

1. The system displays the current state and does not apply a second decision.

### E3: Save fails

1. The system follows NFR-06 and leaves the request pending.

## Postconditions

- **Success:** The request has a final or lapsed status, resulting data is updated, and required notifications are issued.
- **Failure:** The request remains pending and operational data is unchanged.

## Business rules / notes

- Staff submission belongs to UC-12; the Manager decision belongs here.
- The Manager cannot directly overwrite Staff Availability.
- Later events that invalidate an existing Crew follow FR-29 rather than being blocked by FR-32.
- Short notice means strictly less than 48 hours; exactly 48 hours is normal.
- Leave balance recheck/deduction and affected Crew changes share the approval transaction. Late Availability changes and Crew invalidation also commit together. SD-21 returns events; delivery follows commit. Clock-triggered lapse is drawn in SD-12, independent of Manager action, audited and notified after commit.

## Open questions

- Exactly 48 hours remains normal. Confirm whether Late Availability rejection and Job Rejection refusal reasons become mandatory, and whether additional request-history/decision-time fields are required. Leave rejection reasons remain required by FR-19.

## Additional rules

Approval of a Job Rejection Request unassigns the requested Job and its active Linked partners atomically. Clock independently lapses the zero-or-one Pending request for a shared Assignment at Job start; no Manager session is required. Leave approval rechecks the remaining balance when it is saved, so two approvals cannot exceed it.
