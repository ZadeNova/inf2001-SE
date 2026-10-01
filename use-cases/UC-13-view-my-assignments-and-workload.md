# UC-13: View My Assignments and Workload

> **Status: Draft v0.2 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-13 |
| **Name** | View My Assignments and Workload |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | Staff view Published Assignments, Standby days, Crew and Job details, weekly and monthly Workload, request status and Leave balance. |
| **Trigger** | A Staff member opens their Landing Page or selects an Assignment. |
| **Linked requirements** | FR-49, FR-53, FR-55, FR-58, FR-59, NFR-08 |
| **Source** | Brief R7; INT-DCT [System Q1], [System Q2], [System Q3], [Process Q1 follow-up: job info]; INT-DRV [Q1], [Q2], [Q13]; INT-ITA [Q: Outage], [Q: Connection failure]; DEC-04; DEC-16; DEC-31; DEC-37; DEC-39; DEC-40; DEC-42; DEC-43; DEC-47 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The Staff member is logged in.
2. At least the current week is available.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Staff Landing Page. | Shows the current week's Published Assignments and Standby days, weekly Workload against 40 hours, monthly Workload and Leave balance (FR-58). |
| 2 | Optionally switches to the next Published week. | Shows it; Draft weeks remain hidden (FR-49). |
| 3 | Selects an Assignment. | Shows customer, address, Job, Van, Crew, contact and Linked Job details (FR-59). |
| 4 | Reviews Workload. | Uses Planned Hours for Assigned Jobs and Actual Hours for Completed Jobs, crediting every Crew member (FR-53, FR-55). |

## Alternative flows

### A1: Offline current-day view (branches at step 1)

1. With no connection, the Staff member opens cached data.
2. The system shows today's Published Assignments (NFR-08).

### A2: Job Rejection Request is pending (branches at step 3)

1. The system shows the pending status while keeping the Assignment visible (FR-58, FR-63).

## Exception flows

### E1: Next week is Draft (branches at step 2)

1. The system does not offer the Draft week to Staff (FR-49).

### E2: No cached offline data (branches at A1)

1. The system explains that today's Assignments are unavailable offline.

## Postconditions

- **Success:** The requested read-only Assignment and Workload data is displayed.
- **Failure:** No schedule or Workload data is changed.

## Business rules / notes

- Overtime is strictly above 40 hours per Planning Week.
- Standby contributes zero Workload unless the Staff member is placed into a Crew (FR-71).

## Open questions

- Confirm how and when today's offline cache is prepared.
