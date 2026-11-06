# Formal use cases (M2)

> **Status: M2 v1.0 (2026-11-06).** 18 IDs, 16 active, aligned to SRS v4.0 and use-case list v3.0 (DEC-91). The M1 drafts (v0.3) are in git history.

## File convention

- One file per finalized use case: `UC-nn-<kebab-case-name>.md`.
- Each file follows [UC-TEMPLATE.md](UC-TEMPLATE.md).
- Every flow step cites an SRS requirement or DEC basis.
- Diagram IDs stay pending until the team selects the key use cases for OOA and M1 diagrams.

## Index

> **M2 (2026-11-06):** the authoritative list is [use-case-list.md](use-case-list.md) v3.0 (DEC-91). Each active file is at "M2 v1.0" and lists the classes and wireframe it maps to.

| ID | File | Primary actor | Connection |
|---|---|---|---|
| UC-01 | [Log In/out](UC-01-log-in-out.md) | User | Main |
| UC-02 | [Reset Password](UC-02-reset-password.md) | User | Main (standalone) |
| UC-03 | [Create User Account](UC-03-create-user-account.md) | IT Administrator | Main |
| UC-04 | [Manage User Access](UC-04-manage-user-access.md) | IT Administrator | Main |
| UC-05 | [Manage Job](UC-05-manage-job.md) | Manager | Main |
| UC-06 | [Manage Vans and Workshop Servicing](UC-06-manage-vans-and-workshop-servicing.md) | — | **Withdrawn** |
| UC-07 | [Allocate Jobs / Set Weekly Schedule](UC-07-allocate-jobs-set-weekly-schedule.md) | Manager | Main |
| UC-08 | [Compare Staff](UC-08-compare-staff.md) | Manager | Extends UC-07 |
| UC-09 | [Decide Job Rejection Request](UC-09-manage-staff-request.md) | Manager | Main |
| UC-10 | [View Manpower Dashboard](UC-10-view-manpower-dashboard.md) | Manager | Main |
| UC-11 | [Set Availability](UC-11-set-availability-and-preferences.md) | Staff | Main |
| UC-12 | [Submit Job Rejection Request](UC-12-manage-requests.md) | Staff | Main |
| UC-13 | [View My Assignments and Workload](UC-13-view-my-assignments-and-workload.md) | Staff | Main |
| UC-14 | [Complete Job](UC-14-complete-job.md) | — | **Withdrawn** |
| UC-15 | [Notify Staff](UC-15-notify-staff.md) | (included) | Included |
| UC-16 | [Upload CSV](UC-16-upload-csv.md) | Manager | Main |
| UC-17 | [Update Roster and Hours](UC-17-update-roster-and-hours.md) | Manager | Main |
| UC-18 | [Set Standby Preference](UC-18-set-standby-preference.md) | Technician | Main |

File names of UC-09, UC-11 and UC-12 keep their M1 slugs so existing links still work.
