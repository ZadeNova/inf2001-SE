# UC-13: View My Assignments and Workload

> **Status: M2 v1.1 (2026-11-07).** Shows Standby days. Workload is Total Credited Hours; Active Hours are shown separately (DEC-96). Leave balance, Linked Jobs and the Van plate are removed (DEC-78, DEC-90).

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
| 1 | Logs in. | `DashboardController.loadStaffHome()` shows a weekly calendar of Assignments and Standby days, the weekly Total Credited Workload against 40 h and separate Active Hours, the calendar-month Workload and recent notifications (FR-41, FR-39). |
| 2 | Selects an Assignment. | `Assignment.getDetails()`: customer, address, postal code and zone, Brand, units, Job Type, start time, notes, Van number if a Crew duty, per-Job attributed colleagues and their phones; a direct Standby duty shows paid transport/no Van (FR-42). |
| 3 | Switches to the next week. | Shows Assignments only if Published (FR-41). Preference status/reason is visible independently before publication (DEC-98). |

## Alternative flows

### A1: Offline (step 1)

1. `LandingPage.loadCachedToday()` shows today's Assignments from cache. Changes are disabled (NFR-05).

### A2: Current week is Draft (step 1)

1. Show "not yet published" without exposing Draft Assignments (FR-09). Show preference decisions separately; these do not expose the Draft roster.

### A3: Reject a Job (step 2)

1. The Staff member starts UC-12.

## Exception flows

### E1: Next week is Draft (step 3)

1. The system does not offer the Draft week to Staff (FR-09).

### E2: No cached offline data (A1)

1. The system explains that today's Assignments are unavailable offline.

**v1.1 basis:** DEC-96–98; SRS v4.1. Historical M1 sequence sources require review before reuse.
