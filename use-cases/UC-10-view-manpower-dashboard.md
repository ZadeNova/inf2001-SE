# UC-10: View Manpower Dashboard

> **Status: Draft v0.3 (2026-10-04).**

| Field | Value |
|---|---|
| **ID** | UC-10 |
| **Name** | View Manpower Dashboard |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager views Availability, Workload and operational alerts, and maintains Technician Certifications from the dashboard context. |
| **Trigger** | The Manager opens the Landing Page or Availability view. |
| **Linked requirements** | FR-10, FR-15, FR-46, FR-53, FR-55, FR-56 |
| **Source** | Brief R2, R6; INT-MGR [System Q1], [System Q2], [Clarification Q2 follow-up], [Clarification Q7]; INT-DCT [Questionnaire C9]; DEC-04; DEC-05; DEC-18; DEC-30; DEC-35; DEC-39; DEC-40; DEC-42; DEC-43; DEC-45; DEC-47; DEC-51; DEC-58; DEC-59; DEC-63 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-10](../diagrams/SD-10-view-manpower-dashboard.puml); [SD-16](../diagrams/SD-16-handle-invalidated-crew.puml) |
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

- Manager alerts use Notification kind DashboardAlert; handling an alert sends no Staff message. Certification edit and invalidating Crew changes save together. Clock-driven expiry is drawn in SD-16, not dependent on opening the dashboard (DEC-58/59/63).

## Open questions

- Resolved by DEC-45: Certification maintenance is a UC-10 dashboard subflow. No remaining open question in this draft.
