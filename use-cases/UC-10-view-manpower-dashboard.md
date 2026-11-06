# UC-10: View Manpower Dashboard

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-10 |
| **Name** | View Manpower Dashboard |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager views Availability, Workload and operational alerts, and maintains Technician Certifications from the dashboard context. |
| **Trigger** | The Manager opens the Landing Page or Availability view. |
| **Linked requirements** | FR-22, FR-14, FR-34, FR-35, FR-36, FR-40 |
| **Source** | Brief R2, R6; INT-MGR [System Q1], [System Q2], [Clarification Q2 follow-up], [Clarification Q7]; INT-DCT [Questionnaire C9]; DEC-04; DEC-05; DEC-18; DEC-30; DEC-35; DEC-39; DEC-40; DEC-42; DEC-43; DEC-45; DEC-47; DEC-51; DEC-58; DEC-59; DEC-63; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-13](../diagrams/SD-13-view-manpower-dashboard.puml); [SD-21](../diagrams/SD-21-handle-invalidated-crew.puml) |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the Landing Page. | Shows the current week by default and permits switching to the Planning Week (FR-40). |
| 2 | Reviews the dashboard. | Shows every Staff member's Workload chart, 40-hour line, Overtime, separate lowest-three lists, today's Vans/Crews, Unassigned count, pending requests, Standby, Needs attention and Certification reminders (FR-40). |
| 3 | Opens the Availability view. | Shows the one-month colour-coded Staff calendar (FR-14). |

## Alternative flows

### A1: Maintain a Technician Certification (branches at step 2)

1. The Manager opens a Certification reminder or Technician record.
2. The system displays Brand, certificate number and expiry date (FR-22).
3. The Manager updates the Certification record.
4. The system validates and saves it; affected Crew validity follows FR-29.

### A2: Mark an alert handled (branches at step 2)

1. The Manager marks a Landing Page notification handled.
2. The system removes it from the active alert list (FR-40).

## Exception flows

### E1: Save of Certification fails (branches at A1 step 4)

1. The system follows NFR-06.

## Postconditions

- **Success:** Requested dashboard information is displayed, an alert may be handled, or a Certification is updated.
- **Failure:** Read data remains available; failed write data remains unchanged.

## Business rules / notes

- Workload uses Planned Hours for Assigned Jobs and Actual Hours for Completed Jobs (FR-35).
- Overtime is strictly above 40 hours in a Planning Week (FR-36).
- Certification maintenance is included here because the Manager reaches expiring Certifications from the dashboard alerts.
- Handling a Manager alert sends no Staff message. Certification edit and invalidating Crew changes save together. Clock-driven expiry is drawn in SD-21, not dependent on opening the dashboard.

## Open questions

- None.
