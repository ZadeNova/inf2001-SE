# UC-08: Compare Staff

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-08 |
| **Name** | Compare Staff |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | During weekly allocation, the Manager compares up to three Staff using the information needed to choose Crew members. |
| **Trigger** | The Manager requests a comparison while performing UC-07. |
| **Linked requirements** | FR-31, FR-35, FR-36 |
| **Source** | Brief R4, R5; INT-MGR [System Q3]; DEC-06; DEC-08; corrected finalized connection supplied 2026-10-01; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-01](../diagrams/AD-01-weekly-roster.puml); [SD-09](../diagrams/SD-09-compare-staff.puml) |
| **Status** | Agreed |

## Preconditions

1. UC-07 is active for a Job date and Planning Week.
2. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Compare Staff from UC-07. | Shows eligible Staff for selection. |
| 2 | Selects up to three Staff. | Displays each person's Availability for the day and week, Planning Week Workload, Certifications and expiry, Job Preference, and location from other Jobs (FR-31). |
| 3 | Reviews the side-by-side information and selects a Staff member or closes the comparison. | Returns the selection to UC-07 without allocating automatically. |

## Alternative flows

### A1: Staff member has no Jobs that day (branches at step 2)

1. The system shows the location as "No Jobs" (FR-31).

### A2: Overtime boundary is reached (branches at step 2)

1. The system highlights Workload only when it is strictly above 40 hours (FR-36).

## Exception flows

### E1: Fourth Staff selection (branches at step 2)

1. The system refuses the fourth selection and retains the first three (FR-31).

## Postconditions

- **Success:** The Manager returns to UC-07 with comparison information and an optional selection.
- **Failure:** The schedule and Staff records remain unchanged.

## Business rules / notes

- Comparison informs the Manager; it does not allocate Staff automatically.
- UC-08 extends UC-07.

## Open questions

- None.
