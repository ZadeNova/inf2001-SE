# Use-case list (M1)

> **Status: FINAL v2.2 (2026-10-01).** This is the team's finalized 15-use-case structure (DEC-45 to DEC-47), aligned to the minimum SRS v3.3 baseline.
> Each use case has one formal file named `UC-nn-<slug>.md`. Names, IDs, actors and connections below are preserved from the supplied list.
> **Totals:** 15 use cases: 12 Main, 2 Extends and 1 Included.

## Actors

| Actor | Kind | Notes |
|---|---|---|
| **User** | Abstract | Staff, Manager and IT Administrator specialise User |
| **Staff** | Primary | Drivers and Technicians |
| **Technician** | Primary | Adds UC-14 Complete Job |
| **Manager** | Primary | Manages Jobs, Vans, Weekly Rosters, requests and manpower information |
| **IT Administrator** | Primary | Manages accounts and access |
| **Email Service** | Secondary | Delivers reset and confirmation emails for UC-01 and UC-02 |
| **Email/Phone** | Primary for UC-15 | Delivers system-triggered Staff notifications by email and phone |

## Finalized use cases

| ID | Use case | Primary actor | Connection | SRS requirements |
|---|---|---|---|---|
| UC-01 | Log In/out | User | Main | FR-01, FR-07, NFR-10; logout scope DEC-45 |
| UC-02 | Reset Password | User | Extends UC-01 | FR-06 |
| UC-03 | Create User Account | IT Administrator | Main | FR-02, FR-10 |
| UC-04 | Manage User Access | IT Administrator | Main | FR-04, FR-05, FR-07, FR-66 |
| UC-05 | Manage Job | Manager | Main | FR-34 to FR-38, FR-67 |
| UC-06 | Manage Vans and Workshop Servicing | Manager | Main | FR-27 to FR-29 |
| UC-07 | Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster) | Manager | Main | FR-30, FR-32, FR-33, FR-41 to FR-46, FR-49 to FR-51, FR-53, FR-55, FR-71 |
| UC-08 | Compare Staff | Manager | Extends UC-07 | FR-43 |
| UC-09 | Manage Staff Request | Manager | Main | FR-17, FR-23 to FR-25, FR-46, FR-63, FR-70 |
| UC-10 | View Manpower Dashboard | Manager | Main | FR-10, FR-15, FR-46, FR-53, FR-55, FR-56 |
| UC-11 | Set Availability + Preferences | Staff | Main | FR-13, FR-14, FR-16, FR-21 |
| UC-12 | Manage Requests | Staff | Main | FR-17, FR-22, FR-25, FR-62 |
| UC-13 | View My Assignments and Workload | Staff | Main | FR-49, FR-53, FR-55, FR-58, FR-59, NFR-08 |
| UC-14 | Complete Job | Technician | Main | FR-39, FR-53, NFR-08 |
| UC-15 | Notify Staff | Email/Phone | Included | FR-64, FR-71 |

The 50 active FRs map to the finalized use cases. Twenty-one retired FR IDs remain in the SRS history table and have no active use case (DEC-47).

## Relationships

- **Generalisation:** Driver → Staff; Technician → Staff; Staff, Manager and IT Administrator → User.
- **Secondary actor:** Email Service participates in UC-01 and UC-02.
- **Notification actor:** Email/Phone participates in UC-15.
- **`<<extend>>`:** UC-02 extends UC-01; UC-08 extends UC-07.
- **`<<include>>`:** UC-15 is included by UC-07 and UC-09 whenever their successful flows trigger FR-64 notifications. Other SRS events may also call it.

## Merge record

| Final use case | Capabilities merged into it |
|---|---|
| UC-01 | Log In and Log Out |
| UC-04 | Role, lockout and deactivation administration; audit-log viewing is an alternative flow |
| UC-07 | Form Crew, name Standby Staff, allocate or revise Jobs, validate roster rules and publish the Weekly Roster |
| UC-09 | Decide Leave, Late Availability Change and Job Rejection Requests |
| UC-10 | Dashboard reporting and Manager maintenance of Technician Certifications |
| UC-11 | Availability and Job Preference |
| UC-12 | Submit Leave, Late Availability Change and Job Rejection Requests |
| UC-15 | Email and phone notification behaviour formerly separated as a system include |

## Formal files

The drafts are indexed in [README.md](README.md). Each follows [UC-TEMPLATE.md](UC-TEMPLATE.md), cites the SRS/DEC basis for every flow, and keeps diagram IDs pending until OOA and diagram selection.
