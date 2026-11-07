# Use-case list (M2)

> **Status: v3.1 (2026-11-07).** M2 baseline aligned to SRS v4.1 (DEC-91, DEC-96–98). It supersedes v2.3 (M1), which is kept in git history.
> **Totals:** 16 active use cases: 14 Main, 1 Extends and 1 Included. UC-06 and UC-14 are Withdrawn and their IDs are never reused.

## Actors

| Actor | Kind | Notes |
|---|---|---|
| **User** | Abstract | Staff, Manager and IT Administrator specialise User |
| **Staff** | Primary | Drivers and Technicians |
| **Technician** | Primary | Adds UC-18 Set Standby Preference. Drivers are outside the scheduling logic (DEC-82) |
| **Manager** | Primary | CSV upload, Jobs, Weekly Rosters, updates and hours, Job Rejection decisions, dashboard |
| **IT Administrator** | Primary | Accounts, access, Technician profiles, Audit Log |
| **Email Service** «system» | Secondary, non-human | Login confirmation (UC-01), reset link (UC-02), initial login (UC-03), notifications (UC-15) |
| **SMS Gateway** «system» | Secondary, non-human | Notifications (UC-15) |
| **Clock** | Secondary, time event | Lapses a Pending Job Rejection Request at Job start (UC-09) |

HR system and van vendor are **not actors**. The Manager uploads their CSV files (DEC-74).

## Use cases

| ID | Use case | Primary actor | Connection | SRS requirements | Wireframe |
|---|---|---|---|---|---|
| UC-01 | Log In/out | User | Main | FR-43, FR-48, NFR-07 | W-01 |
| UC-02 | Reset Password | User | Main (standalone, DEC-91) | FR-47 | W-02 |
| UC-03 | Create User Account | IT Administrator | Main | FR-44, FR-22 | W-13 |
| UC-04 | Manage User Access | IT Administrator | Main | FR-45, FR-46, FR-48, FR-22, FR-49 | W-13 |
| UC-05 | Manage Job | Manager | Main; includes UC-15 | FR-01, FR-02, FR-04, FR-05, FR-34, FR-50 | W-04 |
| UC-06 | ~~Manage Vans and Workshop Servicing~~ | — | **Withdrawn** (DEC-85, DEC-91) | — | — |
| UC-07 | Allocate Jobs / Set Weekly Schedule | Manager | Main; includes UC-15 | FR-51, FR-26, FR-27, FR-07, FR-08, FR-32, FR-33, FR-34, FR-09, FR-10, FR-11, FR-35, FR-36, FR-30, FR-55 | W-06 |
| UC-08 | Compare Staff | Manager | Extends UC-07 | FR-31 | W-07 |
| UC-09 | Decide Job Rejection Request | Manager (+ Clock) | Main; includes UC-15 | FR-05, FR-34, FR-38 | W-16 |
| UC-10 | View Manpower Dashboard | Manager | Main | FR-14, FR-34, FR-35, FR-36, FR-40 | W-03, W-08 |
| UC-11 | Set Availability | Staff | Main | FR-12, FR-13, FR-15 | W-12 |
| UC-12 | Submit Job Rejection Request | Staff | Main | FR-41, FR-37 | W-15 |
| UC-13 | View My Assignments and Workload | Staff | Main | FR-35, FR-36, FR-41, FR-42, NFR-05 | W-11 |
| UC-14 | ~~Complete Job~~ | — | **Withdrawn** (DEC-76, DEC-91) | — | — |
| UC-15 | Notify Staff | (included) | Included by UC-05, UC-07, UC-09, UC-17 | FR-09, FR-39 | W-11, W-03 |
| UC-16 | Upload CSV | Manager | Main | FR-52, FR-53, FR-54 | W-05 |
| UC-17 | Update Roster and Hours | Manager | Main; includes UC-15 | FR-07, FR-08, FR-10, FR-27, FR-30, FR-32, FR-35, FR-56, FR-57 | W-09, W-10 |
| UC-18 | Set Standby Preference | Technician | Main | FR-15, FR-51 | W-14 |

## «extend» check (lecturer feedback, DEC-91)

| Relationship | M1 | M2 | Why |
|---|---|---|---|
| Reset Password → Log In/out | «extend» | **Removed.** UC-02 is a standalone use case of User | A forgotten-password user starts it without logging in, and it does not continue or change the login. It is its own goal |
| Compare Staff → Allocate Jobs | «extend» | **Kept**, at extension point "Compare Staff", condition {Manager selects 1–3 Staff} | Allocation completes without it; the Manager opens it only when choosing between Staff |

## Changes from M1 (v2.3)

| Change | Use cases |
|---|---|
| Withdrawn | UC-06, UC-14 |
| New | UC-16 Upload CSV, UC-17 Update Roster and Hours, UC-18 Set Standby Preference |
| Narrowed and renamed | UC-09 (Job Rejection only), UC-11 (Availability only), UC-12 (Job Rejection only) |
| Relationship changes | UC-02 no longer extends UC-01; UC-06's include of UC-15 removed; UC-17 includes UC-15 |
| Actor changes | "Email/Phone" stick figure replaced by «system» Email Service and SMS Gateway |

## v3.1 clarification update

UC-07 resolves provisional picks during preparation (FR-51), then suggests/publishes the roster; UC-17 supports direct duties and per-Job replacements; UC-18 exposes provisional/confirmed/not-confirmed status. UC-08/10/13 distinguish Active and Total Credited Hours. UC-09/12 cover attributed Staff on direct Jobs too. IDs and use-case relationships are unchanged; confirmation notifications are part of UC-07's existing include of UC-15.
