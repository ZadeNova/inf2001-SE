# UC-13: View My Assignments and Workload

> **Status: M2 v1.2 (2026-11-14).** SRS v4.2; client processing assigned under DEC-109; encrypted offline viewing and local password unlocking follow DEC-102/105. Shows Standby days. Workload is Total Credited Hours; Active Hours are shown separately (DEC-96). Leave balance, Linked Jobs and the Van plate are removed (DEC-78, DEC-90).

| Field | Value |
|---|---|
| **ID** | UC-13 |
| **Name** | View My Assignments and Workload |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | A Staff member sees this week's Assignments and Standby days, the next Published week, and their weekly and monthly Workload. |
| **Trigger** | The Staff member opens the Staff Landing Page after login, or reopens today's saved copy offline. |
| **Linked requirements** | FR-35, FR-36, FR-41, FR-42, FR-39, NFR-05, NFR-08, NFR-13 |
| **Source** | Brief R7; INT-DRV [Q1], [Q2], [Q13]; DEC-04; DEC-16; DEC-37; DEC-78; DEC-102; DEC-105; DEC-109 |
| **Classes** | LandingPage, OfflineAssignmentController, DashboardController, Staff, Assignment, Standby, Job, Crew, Notification |
| **Wireframe** | W-11 Staff Landing Page |
| **Status** | Agreed |

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Logs in. | `DashboardController.loadStaffHome()` shows a weekly calendar of Assignments and Standby days, the weekly Total Credited Workload against 40 h and separate Active Hours, the calendar-month Workload and recent notifications (FR-41, FR-39). After each successful online load of today's Published Assignments, `OfflineAssignmentController.cacheToday(staff, assignments)` refreshes the encrypted per-user copy; an existing authenticated session does not require a fresh login (NFR-05/08; DEC-105). |
| 2 | Selects an Assignment. | `Assignment.getDetails()`: customer, address, postal code and zone, Brand, units, Job Type, start time, notes, Van number if a Crew duty, per-Job attributed colleagues and their phones; a direct Standby duty shows paid transport/no Van (FR-42). |
| 3 | Switches to the next week. | Shows Assignments only if Published (FR-41). Preference status/reason is visible independently before publication (DEC-98). |

## Alternative flows

### A1: Offline (step 1)

1. `OfflineAssignmentController.loadCachedToday()` checks the per-user encrypted copy's Staff member and date. A different Staff member or a passed date is refused (E2).
2. If the app was closed and the copy is reopened offline, prompt for this Staff member's password. `OfflineAssignmentController.unlockCachedToday(password)` checks it on the device only; no connection or server login is needed. A copy that remains unlocked opens without a repeated prompt.
3. On successful local unlock, show only that Staff member's Published Assignments for today, with changes disabled. The encrypted copy expires when its date passes and is cleared at logout through UC-01 (NFR-05/08/13; DEC-102/105).

### A2: Current week is Draft (step 1)

1. Show "not yet published" without exposing Draft Assignments (FR-09). Show preference decisions separately; these do not expose the Draft roster.

### A3: Reject a Job (step 2)

1. The Staff member starts UC-12.

## Exception flows

### E1: Next week is Draft (step 3)

1. The system does not offer the Draft week to Staff (FR-09).

### E2: No cached offline data (A1)

1. The system explains that today's Assignments are unavailable offline. This also applies after logout, for a different Staff member or when the copy's date has passed.

### E3: Incorrect offline password (A1 step 2)

1. Explain that the password did not unlock the copy. Keep it locked and reveal no Assignment data. This is a local unlock failure, not a server login; no new offline attempt limit is specified (DEC-105).

**v1.2 basis:** DEC-96–98; DEC-102/105/109; SRS v4.2. Historical M1 sequence sources require review before reuse.
