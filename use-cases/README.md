# Formal use-case drafts (M1)

> **Status: Draft v0.3 (2026-10-01).** These 15 files implement the team's finalized list v2.2 against the minimum SRS v3.3 baseline (DEC-45 to DEC-47).

## File convention

- One file per finalized use case: `UC-nn-<kebab-case-name>.md`.
- Each file follows [UC-TEMPLATE.md](UC-TEMPLATE.md).
- Every flow step cites an SRS requirement or DEC basis.
- Diagram IDs stay pending until the team selects the key use cases for OOA and M1 diagrams.

## Index

| ID | Formal draft | Primary actor | Connection |
|---|---|---|---|
| UC-01 | [Log In/out](UC-01-log-in-out.md) | User | Main |
| UC-02 | [Reset Password](UC-02-reset-password.md) | User | Extends UC-01 |
| UC-03 | [Create User Account](UC-03-create-user-account.md) | IT Administrator | Main |
| UC-04 | [Manage User Access](UC-04-manage-user-access.md) | IT Administrator | Main |
| UC-05 | [Manage Job](UC-05-manage-job.md) | Manager | Main |
| UC-06 | [Manage Vans and Workshop Servicing](UC-06-manage-vans-and-workshop-servicing.md) | Manager | Main |
| UC-07 | [Allocate Jobs/set weekly schedule](UC-07-allocate-jobs-set-weekly-schedule.md) | Manager | Main |
| UC-08 | [Compare Staff](UC-08-compare-staff.md) | Manager | Extends UC-07 |
| UC-09 | [Manage Staff Request](UC-09-manage-staff-request.md) | Manager | Main |
| UC-10 | [View Manpower Dashboard](UC-10-view-manpower-dashboard.md) | Manager | Main |
| UC-11 | [Set Availability + Preferences](UC-11-set-availability-and-preferences.md) | Staff | Main |
| UC-12 | [Manage Requests](UC-12-manage-requests.md) | Staff | Main |
| UC-13 | [View My Assignments and Workload](UC-13-view-my-assignments-and-workload.md) | Staff | Main |
| UC-14 | [Complete Job](UC-14-complete-job.md) | Technician | Main |
| UC-15 | [Notify Staff](UC-15-notify-staff.md) | Email/Phone | Included |

## Merged-scope notes

- UC-07 owns the full weekly scheduling goal: Crew formation, Standby selection, Job allocation, validation, Published-roster changes and publication.
- UC-09 owns Manager decisions for all three Staff request types.
- UC-12 owns Staff submission and status review for those request types.
- UC-10 includes Manager Certification maintenance because the finalized list has no separate Certification use case.
- UC-04 includes read-only audit-log viewing because the finalized list has no separate audit use case.
- UC-15 delivers the system-triggered notifications through Email/Phone.
- Retired requirement IDs are preserved in the SRS history tables and have no active use-case mapping.

## Review before OOA

Team review should confirm the Certification and audit-log placement, the exactly-48-hour boundary, offline completion conflicts and the FR-44/FR-70 precedence. Once the core flows are stable, derive candidate classes, attributes, relationships and responsibilities, then develop the class and sequence diagrams together.
