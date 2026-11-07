# UC-10: View Manpower Dashboard

> **Status: M2 v1.1 (2026-11-07).** Leave comes from Leave Records. Certification maintenance moved to UC-04 (DEC-75). Leave-request and Needs-attention alerts are removed (DEC-90).

| Field | Value |
|---|---|
| **ID** | UC-10 |
| **Name** | View Manpower Dashboard |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager sees Workload, the lowest-Workload Staff, Overtime, today's Crews and Standby, alerts and the 1-month Availability grid. |
| **Trigger** | The Manager logs in or opens the Availability grid. |
| **Linked requirements** | FR-14, FR-34, FR-35, FR-36, FR-40 |
| **Source** | Brief R2, R6, §Intro ¶4 + Lecturer clarification; INT-MGR [System Q1 follow-up: landing page], [System Q2]; DEC-05; DEC-63; DEC-74; DEC-86 |
| **Classes** | LandingPage, DashboardController, Staff, Technician, Driver, Availability, LeaveRecord, StandbyPreference, Crew, Standby, Notification, VanAvailability |
| **Wireframe** | W-03 Manager Landing Page; W-08 Availability grid |
| **Status** | Agreed |

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Logs in. | `DashboardController.loadDashboard(currentWeek)` shows every Staff member's Workload (Total Credited Hours), plus separate Active Hours, with a 40 h line and Overtime highlighted (strictly above 40 h), plus the three lowest-Workload Drivers and Technicians (FR-36, FR-40). |
| 2 | — | Also shows today's Crews with zones and Standby, the Unassigned count, pending Job Rejection Requests, expiring Certifications, and days with no van CSV, staffing shortages and activated-day counts. Opening the Standby list highlights the eligible call-up recommendation; low count alone does not imply misconduct. |
| 3 | Switches to the Planning Week. | Reloads the same view for that week. |
| 4 | Opens the Availability grid. | `DashboardController.availabilityGrid()` shows 1 month: Available, Leave/Emergency Leave/MC, or Unavailable/Not submitted, with provisional/confirmed/not-confirmed Standby picks marked (FR-14). |

## Alternative flows

### A1: Mark an alert handled

1. `LandingPage.markHandled(alert)` calls `DashboardController.markHandled(alert)`, which calls `Notification.markHandled()` to hide it from the alert list.

**v1.1 basis:** DEC-96–98; SRS v4.1. Historical M1 sequence sources require review before reuse.
