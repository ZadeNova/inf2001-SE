# UC-13: View My Assignments and Workload

> **Status: M2 v1.0 (2026-11-06).** Shows Standby days. Workload is planned and Standby hours. Leave balance, Linked Jobs and the Van plate are removed (DEC-78, DEC-90).

| Field | Value |
|---|---|
| **ID** | UC-13 |
| **Name** | View My Assignments and Workload |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | A Staff member sees this week's Assignments and Standby days, the next Published week, and their weekly and monthly Workload. |
| **Trigger** | The Staff member logs in. |
| **Linked requirements** | FR-35, FR-36, FR-41, FR-42, FR-39, NFR-05 |
| **Source** | Brief R7; INT-DRV [Q1], [Q2], [Q13]; DEC-04; DEC-16; DEC-37; DEC-78 |
| **Classes** | LandingPage, DashboardController, Staff, Assignment, Standby, Job, Crew, Notification |
| **Wireframe** | W-11 Staff Landing Page |
| **Status** | Agreed |

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Logs in. | `DashboardController.loadStaffHome()` shows a weekly calendar of Assignments and Standby days, the weekly Workload against 40 h, the calendar-month Workload and recent notifications (FR-41, FR-39). |
| 2 | Selects an Assignment. | `Assignment.getDetails()`: customer, address, postal code and zone, Brand, units, Job Type, start time, notes, Van number, and Crew-mates' names and phones (FR-42). |
| 3 | Switches to the next week. | Shows it only if it is Published (FR-41). |

## Alternative flows

### A1: Offline (step 1)

1. `LandingPage.loadCachedToday()` shows today's Assignments from cache. Changes are disabled (NFR-05).

### A2: Current week is Draft (step 1)

1. Show "not yet published" without exposing Draft Assignments (FR-09).

### A3: Reject a Job (step 2)

1. The Staff member starts UC-12.

## Exception flows

### E1: Next week is Draft (step 3)

1. The system does not offer the Draft week to Staff (FR-09).

### E2: No cached offline data (A1)

1. The system explains that today's Assignments are unavailable offline.
