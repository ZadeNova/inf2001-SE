# UC-08: Compare Staff

> **Status: Draft v0.1 (2026-10-01).** Extends UC-07.

| Field | Value |
|---|---|
| **ID** | UC-08 |
| **Name** | Compare Staff |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | During weekly allocation, the Manager compares up to three Staff using the information needed to choose Crew members. |
| **Trigger** | The Manager requests a comparison while performing UC-07. |
| **Linked requirements** | FR-43, FR-53, FR-55 |
| **Source** | Brief R4, R5; INT-MGR [System Q3]; DEC-06; DEC-08; corrected finalized connection supplied 2026-10-01 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. UC-07 is active for a Job date and Planning Week.
2. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Compare Staff from UC-07. | Shows eligible Staff for selection. |
| 2 | Selects up to three Staff. | Displays each person's Availability for the day and week, Planning Week Workload, Certifications and expiry, Job Preference, and location from other Jobs (FR-43). |
| 3 | Reviews the side-by-side information and selects a Staff member or closes the comparison. | Returns the selection to UC-07 without allocating automatically. |

## Alternative flows

### A1: Staff member has no Jobs that day (branches at step 2)

1. The system shows the location as “No Jobs” (FR-43).

### A2: Overtime boundary is reached (branches at step 2)

1. The system highlights Workload only when it is strictly above 40 hours (FR-55).

## Exception flows

### E1: Fourth Staff selection (branches at step 2)

1. The system refuses the fourth selection and retains the first three (FR-43).

## Postconditions

- **Success:** The Manager returns to UC-07 with comparison information and an optional selection.
- **Failure:** The schedule and Staff records remain unchanged.

## Business rules / notes

- Comparison informs the Manager; it does not allocate Staff automatically.
- UC-08 extends UC-07 as corrected by the user.

## Open questions

- None identified for the current draft.
