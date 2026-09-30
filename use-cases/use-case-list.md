# Use-case list (M1)

> **Status: FINAL v1.0 (2026-09-30).** Derived from the team's whiteboard session (30 Sep) and checked against SRS v3.0 (`srs-v3.0`).
> **IDs are fixed.** Any change needs a DEC entry. Never renumber: mark a dropped use case `Withdrawn`. Each use case gets its own file: `use-cases/UC-nn-<slug>.md`, from [UC-TEMPLATE.md](UC-TEMPLATE.md).
> **Totals:** 28 use cases = 23 main + 3 extensions + 2 included. By type: 16 are not CRUD, 8 are CRUD with rules, 4 are read-only.

## Actors

| Actor | Kind | Notes |
|---|---|---|
| **User** | Abstract | General actor for Log In. Staff, Manager and IT Administrator all specialise it |
| **Staff** | Primary | Specialised by **Driver** and **Technician**. Shared Staff use cases attach to Staff |
| **Technician** | Primary | Adds Complete Job |
| **Driver** | Primary | Has only the Staff use cases |
| **Manager** | Primary | — |
| **IT Administrator** | Primary | — |
| **Email Service** | Secondary (external system) | Delivers emails for Reset Password (UC-02), 2FA in Log In (UC-01) and Notify Staff (UC-28) |

## Use cases

**Type** is Main, Extends (`<<extend>>`) or Included (`<<include>>`). **Kind** is Process (not CRUD: a workflow, rules or a state change), CRUD+ (CRUD with business rules) or Read.

| ID | Use case | Primary actor | Type | Kind | SRS requirements | From the whiteboard |
|---|---|---|---|---|---|---|
| UC-01 | Log In | User | Main | Process | FR-01, FR-07, NFR-10 | 1. login |
| UC-02 | Reset Password | User | Extends UC-01 | Process | FR-06 | 4. reset PW |
| UC-03 | Create User Account | IT Administrator | Main | CRUD+ | FR-02, FR-03, FR-08 (bulk import as an alternative flow), FR-10 | IT 1. new staff to system |
| UC-04 | Manage User Access | IT Administrator | Main | CRUD+ | FR-03, FR-04, FR-05, FR-07 | IT 2. update staff info + IT 3. revoke/remove privileges |
| UC-05 | Load Public Holidays | IT Administrator | Main | CRUD+ | FR-09, FR-70 | *New (SRS)* |
| UC-06 | View Audit Log | IT Administrator | Main | Read | FR-66 | IT 4. manage audit log (renamed) |
| UC-07 | Manage Job | Manager | Main | CRUD+ | FR-34 to FR-38, FR-67 | M 5. add jobs |
| UC-08 | Maintain Certifications | Manager | Main | CRUD+ | FR-10, FR-11, FR-12, FR-70 | *New (SRS)* |
| UC-09 | Manage Vans and Workshop Servicing | Manager | Main | CRUD+ | FR-27, FR-28, FR-29 | M 9. manage van |
| UC-10 | Form Van Crew | Manager | Main | Process | FR-30 to FR-33 | M 6. set schedule (part) |
| UC-11 | Name Standby Staff | Manager | Main | Process | FR-71, FR-47 | *New (SRS, DEC-43)* |
| UC-12 | Allocate Jobs | Manager | Main | Process | FR-41, FR-42, FR-46, FR-50, FR-51 | M 6. set schedule + M 11. edit schedule |
| UC-13 | Compare Staff | Manager | Extends UC-12 | Read | FR-43 | M 12. compare staff performance (renamed) |
| UC-14 | Suggest Replacement Staff | Manager | Extends UC-12 and UC-17 | Process | FR-48 | *New (SRS)* |
| UC-15 | Publish Weekly Roster | Manager | Main | Process | FR-49, FR-69 | M 13. publish schedule |
| UC-16 | Approve or Reject Staff Request | Manager | Main | Process | FR-17, FR-23 to FR-26, FR-70 | M 7. manage approvals (Leave and late availability changes) |
| UC-17 | Approve or Refuse Job Rejection Request | Manager | Main | Process | FR-63, FR-46 | M 7. manage approvals (Job rejections) |
| UC-18 | Mark Staff Unavailable | Manager | Main | Process | FR-18, FR-70 | *New (SRS)* |
| UC-19 | View Manpower Dashboard | Manager | Main | Read | FR-11, FR-15, FR-20, FR-52 to FR-57, FR-60, FR-61, FR-65 | M 10. view staff availability + M 8. view job progress |
| UC-20 | Set Availability | Staff | Main | CRUD+ | FR-13, FR-14, FR-16, FR-19 | T 3. add availability + T 7. edit availability |
| UC-21 | Set Job Preference | Staff | Main | CRUD+ | FR-21, FR-16 | *New (SRS, **brief R9**)* |
| UC-22 | Request Leave | Staff | Main | Process | FR-22, FR-25 | 3. apply leave (Staff only) |
| UC-23 | Request Late Availability Change | Staff | Main | Process | FR-17 | T 8. edit request |
| UC-24 | View My Assignments and Workload | Staff | Main | Read | FR-52 to FR-55, FR-58, FR-59, FR-69, NFR-08 | T 4. view job dashboard |
| UC-25 | Submit Job Rejection Request | Staff | Main | Process | FR-62 | T 5. req to reject jobs (now Drivers too) |
| UC-26 | Complete Job | Technician | Main | Process | FR-39, FR-40, FR-54, NFR-08 | T 9. complete job + T 6. upload photo |
| UC-27 | Validate Roster Rules | — (system) | Included | Process | FR-44, FR-45 | *New (SRS)* |
| UC-28 | Notify Staff | — (system) | Included | Process | FR-64 | *New (SRS)* |

Every active FR (FR-01 to FR-71, except the withdrawn FR-68) is covered by at least one use case. NFRs attach to use cases as constraints.

## Relationships for the use-case diagram

- **Generalisation:** Driver → Staff; Technician → Staff; Staff, Manager and IT Administrator → User.
- **Secondary actor:** Email Service is associated with Log In (2FA), Reset Password and Notify Staff.
- **`<<extend>>`:**
  - Reset Password → Log In
  - Compare Staff → Allocate Jobs
  - Suggest Replacement Staff → Allocate Jobs, and → Approve or Refuse Job Rejection Request
- **`<<include>>`:**
  - Validate Roster Rules is included by Manage Job, Form Van Crew, Allocate Jobs, Publish Weekly Roster, and Approve or Reject Staff Request.
  - Notify Staff is included by Form Van Crew, Publish Weekly Roster, Approve or Reject Staff Request, Approve or Refuse Job Rejection Request, and Mark Staff Unavailable.

## Changes from the whiteboard

| Change | Reason |
|---|---|
| **Dropped** Logout | It isn't a user goal and has no SRS requirement |
| **Merged** add and edit availability → Set Availability | Separate add and edit use cases are the CRUD split to avoid |
| **Merged** set and edit schedule → Allocate Jobs, with Form Van Crew split out | Split by goal, not by operation. Crew formation and Job allocation have different rules |
| **Merged** upload photo → Complete Job | The photo is required at completion (FR-40), not a separate goal |
| **Merged** view job progress → View Manpower Dashboard | The SRS tracks Job status, not live progress (DEC-33) |
| **Merged** update staff info and revoke privileges → Manage User Access | One goal: controlling a user's access |
| **Split** manage approvals → UC-16 and UC-17 | Job rejections have their own rules (48 h, Short notice, Standby notified) |
| **Renamed** "compare staff performance" → Compare Staff | Brief R4 compares availability, workload, preference and location for allocation. Performance appraisal is out of scope |
| **Renamed** "manage audit log" → View Audit Log | Audit entries must not be edited or deleted (FR-66, FR-67) |
| **Restricted** apply leave to Staff | Managers and the IT Administrator have no leave in the system (FR-20, DEC-18) |
| **Extended** job rejection to Drivers | Any crew member can submit a rejection request (DEC-42) |
| **Added** Set Job Preference, Form Van Crew, Name Standby Staff, Mark Staff Unavailable, Maintain Certifications, Load Public Holidays, Suggest Replacement Staff, Validate Roster Rules, Notify Staff | They are required by the SRS. Set Job Preference is required by the brief itself (R9) |
| **Replaced** arrows from Technician to Driver with actor generalisation | This is the correct UML way to share use cases between actors |
| **Added** Email Service as a secondary actor | The system sends emails for notifications (FR-64), password reset (FR-06) and 2FA (NFR-10). The rubric requires "all actors" |

## Open check before drawing

- Confirm with the lecture slides that included use cases without an actor (UC-27, UC-28) are acceptable, and whether Log In should be a precondition or an `<<include>>`. If the slides discourage system-only use cases, withdraw UC-27 and UC-28 and write their rules into the flows instead.

## How to write each use case

1. Copy [UC-TEMPLATE.md](UC-TEMPLATE.md) to `UC-nn-<slug>.md`, e.g. `UC-25-submit-job-rejection-request.md`.
2. Use the name, actor and requirements from the table above exactly as written, with glossary terms from [AGENTS.md](../AGENTS.md).
3. Main flow: numbered actor and system steps. Each alternative or exception flow names the step it branches from.
4. The blocks and warnings in FR-44 and FR-45 become exception and alternative flows.
5. Fill in [traceability.md](../traceability.md) as you go (requirement → use case).
