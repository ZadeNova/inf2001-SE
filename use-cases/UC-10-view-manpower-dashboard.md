# UC-10: View Manpower Dashboard

> **Status: Draft v0.2 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-10 |
| **Name** | View Manpower Dashboard |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager views Availability, Workload and operational alerts, and maintains Technician Certifications from the dashboard context. |
| **Trigger** | The Manager opens the Landing Page or Availability view. |
| **Linked requirements** | FR-10, FR-15, FR-46, FR-53, FR-55, FR-56 |
| **Source** | Brief R2, R6; INT-MGR [System Q1], [System Q2], [Clarification Q2 follow-up], [Clarification Q7]; INT-DCT [System Q1]; DEC-04; DEC-05; DEC-18; DEC-30; DEC-35; DEC-39; DEC-40; DEC-42; DEC-43; DEC-45; DEC-47 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Landing Page. | Shows the current week by default and permits switching to the Planning Week (FR-56). |
| 2 | Reviews the dashboard. | Shows every Staff member's Workload chart, 40-hour line, Overtime, separate lowest-three lists, today's Vans/Crews, Unassigned count, pending requests, Standby, Needs attention and Certification reminders (FR-56). |
| 3 | Opens the Availability view. | Shows the one-month colour-coded Staff calendar (FR-15). |

## Alternative flows

### A1: Maintain a Technician Certification (branches at step 2)

1. The Manager opens a Certification reminder or Technician record.
2. The system displays Brand, certificate number and expiry date (FR-10).
3. The Manager updates the Certification record.
4. The system validates and saves it; affected Crew validity follows FR-70.

### A2: Mark an alert handled (branches at step 2)

1. The Manager marks a Landing Page notification handled.
2. The system removes it from the active alert list (FR-56).

## Exception flows

### E1: Save of Certification fails (branches at A1 step 4)

1. The system follows NFR-09.

## Postconditions

- **Success:** Requested dashboard information is displayed, an alert may be handled, or a Certification is updated.
- **Failure:** Read data remains available; failed write data remains unchanged.

## Business rules / notes

- Workload uses Planned Hours for Assigned Jobs and Actual Hours for Completed Jobs (FR-53).
- Overtime is strictly above 40 hours in a Planning Week (FR-55).
- Certification maintenance is placed here because the finalized list merged away its standalone use case (DEC-45).

## Open questions

- Confirm whether the team prefers Certification maintenance as a dashboard subflow or within another finalized Manager use case before diagrams are drawn.
