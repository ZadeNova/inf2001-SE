# Use-case list (M1)

> **Status: v2.4 (2026-11-07), M1 submitted baseline.** The 15 use cases, actors and requirement links match §3 of the submitted M1 report (DEC-72); SRS v3.5. v2.3 (2026-10-03) is in git history.
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
| **Email Service** | Secondary | Delivers reset and confirmation emails for UC-01 and UC-02, and initial login details for UC-03 |
| **Email/Phone** | Primary for UC-15 | External delivery actor shown in the UCD for system-triggered Staff notifications (UC-15). Email Service and SMS Gateway realise its email and phone channels |
| **SMS Gateway** | External (sequence analysis) | Realises the phone channel as SMS (UC-15). Not a separate human role or use case |
| **Clock** | Secondary system-event actor | Job-start lapse in UC-09 (SD-12) and daily Certification-expiry checks under FR-22/FR-29 (SD-21). No separate use case |

## Finalized use cases

| ID | Use case | Primary actor | Connection | SRS requirements |
|---|---|---|---|---|
| UC-01 | Log In/out | User | Main | FR-43, FR-48, NFR-07, NFR-09, NFR-11 |
| UC-02 | Reset Password | User | Extends UC-01 | FR-47, FR-49, NFR-06, NFR-08 |
| UC-03 | Create User Account | IT Administrator | Main | FR-44, FR-22, FR-49, NFR-06, NFR-09 |
| UC-04 | Manage User Access | IT Administrator | Main | FR-45, FR-46, FR-48, FR-49, NFR-09, NFR-10 |
| UC-05 | Manage Job | Manager | Main | FR-01 to FR-05, FR-32, FR-39, FR-50, NFR-06 |
| UC-06 | Manage Vans and Workshop Servicing | Manager | Main | FR-23, FR-24, FR-25, FR-05, FR-39 |
| UC-07 | Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster) | Manager | Main | FR-07 to FR-11, FR-26 to FR-28, FR-30 to FR-36, FR-39 |
| UC-08 | Compare Staff | Manager | Extends UC-07 | FR-31, FR-35, FR-36 |
| UC-09 | Manage Staff Request | Manager | Main | FR-16, FR-19 to FR-21, FR-34, FR-38, FR-39, FR-29 |
| UC-10 | View Manpower Dashboard | Manager | Main | FR-22, FR-14, FR-34, FR-35, FR-36, FR-40 |
| UC-11 | Set Availability + Preferences | Staff | Main | FR-12, FR-13, FR-15, FR-17 |
| UC-12 | Manage Requests | Staff | Main | FR-16, FR-18, FR-21, FR-41, FR-37 |
| UC-13 | View My Assignments and Workload | Staff | Main | FR-09, FR-35, FR-36, FR-41, FR-42, NFR-05 |
| UC-14 | Complete Job | Technician | Main | FR-05, FR-06, FR-35, NFR-05, NFR-06 |
| UC-15 | Notify Staff | Email/Phone | Included | FR-09, FR-39, FR-30, NFR-01, NFR-06 |

The requirement links are the *Linked requirements* printed for each use case in the report. The 50 active FRs and 12 NFRs are listed in [requirements.md](../requirements.md).

## Relationships

- **Generalisation:** Driver → Staff; Technician → Staff; Staff, Manager and IT Administrator → User.
- **Secondary actor:** Email Service participates in UC-01, UC-02 and UC-03.
- **Notification actor:** Email/Phone participates in UC-15.
- **`<<extend>>`:** UC-02 extends UC-01; UC-08 extends UC-07.
- **`<<include>>`:** UC-15 is included by UC-05, UC-06, UC-07 and UC-09 whenever their successful flows trigger FR-39 notifications. Other SRS events may also call it.

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
