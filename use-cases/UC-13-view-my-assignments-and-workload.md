# UC-13: View My Assignments and Workload

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-13 |
| **Name** | View My Assignments and Workload |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | Staff view Published Assignments, Standby days, Crew and Job details, weekly and monthly Workload, request status and Leave balance. |
| **Trigger** | A Staff member opens their Landing Page or selects an Assignment. |
| **Linked requirements** | FR-09, FR-35, FR-36, FR-41, FR-42, NFR-05 |
| **Source** | Brief R7; INT-DCT [Questionnaire C9], [Questionnaire C10/C11], [Questionnaire C18/C19], [Questionnaire C5]; INT-DRV [Q1], [Q2], [Q13]; INT-ITA [Q: Outage], [Q: Connection failure]; DEC-04; DEC-16; DEC-31; DEC-37; DEC-39; DEC-40; DEC-42; DEC-43; DEC-47; DEC-58; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-01](../diagrams/AD-01-weekly-roster.puml); [AD-03](../diagrams/AD-03-job-rejection.puml); [SD-18](../diagrams/SD-18-view-my-assignments-and-workload.puml) |
| **Status** | Agreed |

## Preconditions

1. The Staff member is logged in.
2. At least the current week is available.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Staff Landing Page. | Shows the current week's Published Assignments and Standby days, weekly Workload against 40 hours, monthly Workload and Leave balance (FR-41). |
| 2 | Optionally switches to the next Published week. | Shows it; Draft weeks remain hidden (FR-09). |
| 3 | Selects an Assignment. | Shows customer, address, Job, Van, Crew, contact and Linked Job details (FR-42). |
| 4 | Reviews Workload. | Uses Planned Hours for Assigned Jobs and Actual Hours for Completed Jobs, crediting every Crew member (FR-35, FR-36). |

## Alternative flows

### A1: Offline current-day view (branches at step 1)

1. With no connection, the Staff member opens cached data.
2. The system shows today's Published Assignments (NFR-05).

### A2: Job Rejection Request is pending (branches at step 3)

1. The system shows the pending status while keeping the Assignment visible (FR-41, FR-38).

### A3: Current week is Draft (branches at step 1)

1. Show not yet published and the Leave balance, without exposing Draft Assignments (FR-09).

## Exception flows

### E1: Next week is Draft (branches at step 2)

1. The system does not offer the Draft week to Staff (FR-09).

### E2: No cached offline data (branches at A1)

1. The system explains that today's Assignments are unavailable offline.

## Postconditions

- **Success:** The requested read-only Assignment and Workload data is displayed.
- **Failure:** No schedule or Workload data is changed.

## Business rules / notes

- Overtime is strictly above 40 hours per Planning Week.
- Standby contributes zero Workload unless the Staff member is placed into a Crew (FR-30).
- If the current week is Draft, show not yet published and the Leave balance; disclose no Draft Assignments. Published-week and cached Published-today views remain read-only.

## Open questions

- Confirm how and when today's offline cache is prepared. Also confirm whether daily totals, assigned/completed counts or Availability/Leave overlays are added; weekly/monthly Workload and Leave balance remain the adopted scope.
