# Traceability Matrix

> **M2 working baseline v4.2 (2026-11-14):** SRS v4.2 (DEC-99/102–109), use-case list v3.1, [CD-final](diagrams/CD-final.puml), [CMP-system](diagrams/CMP-system.puml), [m2/testing.md](m2/testing.md) and [m2/wireframes.md](m2/wireframes.md) (DEC-73 to DEC-98).
> Builds on the M1 report baseline (DEC-72): SRS v3.5, 43-class analysis model and 21 sequence diagrams SD-01–SD-21, whose matrix is in git history. M1 diagram status after the M2 changes is in §5; the draft SD-18 Allocate Job was already archived before M2.
> Component names match the CD-final packages. W-nn = wireframe screen. BB/WB = black-box and white-box test cases.

## 1. Requirement → Use case → Class → Component → Test → Wireframe

| Requirement | Source (main) | Use case(s) | Key classes (CL-) | Component | Test | Wireframe |
|---|---|---|---|---|---|---|
| FR-43 | Brief R2, R7, R11; DEC-18 | UC-01 | Account, AuthController, LandingPage | Authentication | SRS note | W-01 |
| FR-44 | Brief R11; DEC-49; DEC-75; DEC-77 | UC-03 | AccountController, User, Technician, Certification, Account, EmailChannel | Account Management | SRS note | W-13 |
| FR-45 | DEC-17 | UC-04 | AccountController, Account, RosterController | Account Management | SRS note | W-13 |
| FR-46 | DEC-34 | UC-04 | AccountController, Account, RosterController | Account Management | SRS note | W-13 |
| FR-47 | DEC-71; M2-Brief §3.2 | UC-02 | AuthController, PasswordResetToken, Account | Authentication | SRS note | W-02 |
| FR-48 | DEC-17 | UC-01, UC-04 | Account, AuthController, AccountController | Authentication | SRS note | W-01, W-13 |
| FR-22 | DEC-75; DEC-77 | UC-03, UC-04 | Technician, Certification, AccountController | Account Management | BB extra (expiry boundary) | W-13 |
| FR-12 | Brief R8; DEC-83 | UC-11 | Availability, AvailabilityController | Staff Inputs | SRS note | W-12 |
| FR-13 | Brief R8; DEC-01; DEC-30 | UC-11 | AvailabilityController, RuleValidator | Staff Inputs | SRS note | W-12 |
| FR-14 | Brief §Intro ¶4; DEC-74 | UC-10 | DashboardController, Availability, LeaveRecord, StandbyPreference | Roster & Hours | SRS note | W-08 |
| FR-15 | Brief §Company ¶1; DEC-02; DEC-79 | UC-11, UC-18 | RuleValidator, AvailabilityController, StandbyPreferenceController | Scheduling Engine | BB-01 | W-12, W-14 |
| FR-26 | Brief §Company ¶3–4; DEC-84; DEC-85; DEC-97 | UC-07 | Crew, RosterController, RuleValidator, VanAvailability | Roster & Hours | SC-08, SC-12 | W-06 |
| FR-27 | Brief §Company ¶2–3; DEC-84; DEC-97 | UC-07, UC-17 | Assignment, Crew, Certification, RuleValidator | Scheduling Engine | SC-13 | W-06, W-10 |
| FR-01 | DEC-11; DEC-77 | UC-05 | Job, JobController, Zone | Job Management | SRS note | W-04 |
| FR-02 | DEC-22 | UC-05 | JobController, Job | Job Management | SRS note | W-04 |
| FR-04 | DEC-76; DEC-103 | UC-05 | JobController, Job, NotificationService | Job Management | SRS note | W-04 |
| FR-05 | DEC-42; DEC-76 | UC-05, UC-09 | Job, RequestController, AccountController, RosterController | Job Management, Staff Inputs, Account Management, Roster & Hours | SRS note | W-04, W-16 |
| FR-07 | Brief R3; DEC-16; DEC-97 | UC-07, UC-17 | RosterController, HoursController, Assignment, Job | Roster & Hours | SC-05, SC-14 | W-06, W-09 |
| FR-08 | DEC-12; DEC-31; DEC-97 | UC-07, UC-17 | Assignment, RuleValidator | Roster & Hours | SC-14 | W-06, W-09 |
| FR-31 | Brief R4, R5; DEC-77; DEC-79 | UC-08 | RosterController, Technician, StandbyPreference | Roster & Hours | SRS note | W-07 |
| FR-32 | DEC-19; DEC-85; DEC-97, DEC-98 | UC-07, UC-17 | RuleValidator | Scheduling Engine | SC-12–15 | W-06, W-09 |
| FR-33 | Brief R6; DEC-19; DEC-74; DEC-77; DEC-98; DEC-107; DEC-108 | UC-07, UC-16 | RuleValidator, RosterController, AuditLog | Scheduling Engine, Roster & Hours | SRS note; missing CSV returns to UC-16 | W-06 |
| FR-34 | INT-MGR [Conflicts Q1] | UC-05, UC-07, UC-09, UC-10 | JobController, Job | Job Management | SRS note | W-03, W-06 |
| FR-09 | Brief R3; DEC-16; DEC-80; DEC-98 | UC-07 | WeeklyRoster, RosterController, StandbyPreferenceController, NotificationService | Roster & Hours | SC-12, SC-15 | W-06 |
| FR-10 | DEC-16; DEC-88; DEC-97, DEC-98 | UC-07, UC-17 | RosterController, HoursController, Assignment, Replacement | Roster & Hours | SC-05, SC-15 | W-06, W-09 |
| FR-11 | INT-MGR [System Q2]; DEC-85 | UC-07 | RosterController, Crew | Roster & Hours | SRS note | W-06 |
| FR-35 | DEC-31; DEC-78; DEC-96, DEC-97 | UC-07, UC-10, UC-13, UC-17 | Staff, Job, Assignment, Replacement, Standby, HoursEdit | Domain Model | SC-01–05 | W-03, W-09, W-11 |
| FR-36 | Brief R6; DEC-04; DEC-86; DEC-104 | UC-07, UC-10, UC-13 | Staff | Domain Model | SRS boundary 40.0/40.5; Driver/Technician display check | W-03, W-06, W-07, W-09, W-10, W-11 |
| FR-40 | Brief R2, R6; DEC-05 | UC-10 | DashboardController, Notification | Roster & Hours | SRS note | W-03 |
| FR-41 | Brief R7 | UC-12, UC-13 | DashboardController, Staff | Roster & Hours | SRS note | W-11 |
| FR-42 | DEC-37 | UC-13 | Assignment | Domain Model | SRS note | W-11 |
| FR-37 | Brief R10; DEC-42; DEC-66 | UC-12 | RequestController, JobRejectionRequest, RequestPage | Staff Inputs | SRS note | W-15 |
| FR-38 | Brief R10; DEC-42 | UC-09 | RequestController, JobRejectionRequest, RosterController, Assignment, Job | Staff Inputs, Roster & Hours | SRS note | W-16 |
| FR-39 | DEC-46; DEC-48; DEC-88; DEC-103 | UC-15 | NotificationService, NotificationChannel, EmailChannel, SmsChannel, Notification | Notification | SRS note | W-11, W-03 |
| FR-49 | DEC-17; DEC-89 | UC-04 (view); all changing UCs | AuditLog, AccountController | Domain Model | SRS note | W-13 |
| FR-50 | DEC-34; DEC-76 | UC-05 | JobController | Job Management | SRS note | W-04 |
| FR-30 | DEC-81; DEC-96, DEC-97, DEC-98 | UC-07, UC-17 | Standby, RosterController, RuleValidator | Roster & Hours | SC-01–04, SC-15 | W-06, W-09 |
| FR-51 | Brief R9; DEC-79; DEC-98; DEC-104; DEC-108 | UC-18; confirmation in UC-07 | StandbyPreferenceController, StandbyPreference, RuleValidator, NotificationService | Staff Inputs | BB-01–06 (six submission rules), BB-07 (R6 no-op); SC-06–09, SC-15 (confirmation) | W-06, W-14 |
| FR-52 | DEC-74; DEC-104; DEC-106; DEC-108 | UC-16 | CsvImportController, CsvImport, HrLeaveCsvMapper, LeaveRecord | CSV Import | SRS note | W-05 |
| FR-53 | DEC-74; DEC-85 | UC-16 | CsvImportController, CsvImport, VanAvailabilityCsvMapper, VanAvailability | CSV Import | SRS note | W-05 |
| FR-54 | DEC-74; DEC-104; DEC-106; DEC-108 | UC-16 | CsvImportController, CsvImport, CsvRowMapper | CSV Import | SRS note | W-05 |
| FR-55 | Brief R3; DEC-80; DEC-96, DEC-98; DEC-108 | UC-07 | RosterController, StandbyPreferenceController, CrewFormingService, RuleValidator, TechnicianRanking, WorkloadRanking, Crew, Standby | Roster & Hours, Staff Inputs, Scheduling Engine | WB-01–07; SC-10–12 | W-06 |
| FR-56 | DEC-81; DEC-96, DEC-97 | UC-17 | StandbyActivationService, RuleValidator, ActivationRanking, Standby | Scheduling Engine | SC-13, SC-14 | W-10 |
| FR-57 | DEC-78; DEC-81; DEC-96, DEC-97 | UC-17 | HoursController, HoursEdit, Standby, Assignment, Replacement | Roster & Hours | SC-01–05, SC-14 | W-09 |
| FR-58 | DEC-89 | — (Clock) | RetentionJob | Audit & Retention | SRS note | — |
| NFR-01 | INT-ITA [Q: Response time] | All | — | All | Load test | — |
| NFR-02 | INT-ITA [Q: Concurrency] | All | — | All | Load test | — |
| NFR-03, NFR-04 | INT-ITA [Q: Outage], [Q: Restore] | — | RetentionJob | Database | Ops check | — |
| NFR-05 | INT-DCT [Questionnaire C18/C19]; DEC-102/105; DEC-109 | UC-01, UC-13 | LandingPage, OfflineAssignmentController | Web UI | Successful-online-load refresh; local unlock/wrong-password/no-repeat checks; offline scope, per-user isolation, logout and date expiry | W-11 |
| NFR-06 | INT-ITA [Q: Connection failure] | All | — | Web UI | SRS note | — |
| NFR-07 | DEC-41 | UC-01 | Account | Authentication | SRS note | W-01 |
| NFR-08 | INT-ITA [Q: Safeguards]; DEC-105; DEC-109 | UC-01–UC-03, UC-13 | Account, PasswordResetToken, LandingPage, OfflineAssignmentController | Database, Web UI | DB/browser storage inspection; no readable persisted decryption key; offline correct/incorrect password unlock | W-11 |
| NFR-09 | DEC-17; DEC-18 | All | all controllers | Application layer | Permission matrix | — |
| NFR-10 | DEC-34; DEC-89 | — | RetentionJob | Audit & Retention | SRS note | — |
| NFR-11 | Brief R1 | All | all boundaries | Web UI | Browser matrix | All |
| NFR-12 | INT-MGR [Closing] | UC-11, UC-12, UC-18 | — | Web UI | Walkthrough | W-12, W-14, W-15 |
| NFR-13 | DEC-89; DEC-102; DEC-109 | UC-13 (offline exception) | LandingPage, OfflineAssignmentController | Database, Web UI | On-site authoritative-store check; NFR-05 cache-scope/lifecycle checks | W-11 |
| NFR-14 | DEC-87 | — | all entities | Domain Model | Attribute review | — |

Withdrawn requirements (SRS §3.15, §4.1) have no row here.

## 2. Use case → Diagram, wireframe and tests

| Use case | Actor(s) | Use case diagram | Main components | Wireframe | Tests |
|---|---|---|---|---|---|
| [UC-01](use-cases/UC-01-log-in-out.md) | User; Email Service «system» | [UCD-system](diagrams/UCD-system.puml) | Web UI, Authentication | W-01 | — |
| [UC-02](use-cases/UC-02-reset-password.md) | User; Email Service «system» | UCD-system | Authentication | W-02 | — |
| [UC-03](use-cases/UC-03-create-user-account.md) | IT Administrator; Email Service «system» | UCD-system | Account Management | W-13 | — |
| [UC-04](use-cases/UC-04-manage-user-access.md) | IT Administrator | UCD-system | Account Management | W-13 | — |
| [UC-05](use-cases/UC-05-manage-job.md) | Manager | UCD-system | Job Management | W-04 | — |
| UC-06 | — | — (Withdrawn) | — | — | — |
| [UC-07](use-cases/UC-07-allocate-jobs-set-weekly-schedule.md) | Manager | UCD-system | Scheduling Engine, Roster & Hours | W-06 | WB-01 to WB-07 |
| [UC-08](use-cases/UC-08-compare-staff.md) | Manager | UCD-system | Roster & Hours | W-07 | — |
| [UC-09](use-cases/UC-09-manage-staff-request.md) | Manager; Clock | UCD-system | Staff Inputs, Roster & Hours | W-16 | — |
| [UC-10](use-cases/UC-10-view-manpower-dashboard.md) | Manager | UCD-system | Roster & Hours | W-03, W-08 | — |
| [UC-11](use-cases/UC-11-set-availability-and-preferences.md) | Staff | UCD-system | Staff Inputs | W-12 | — |
| [UC-12](use-cases/UC-12-manage-requests.md) | Staff | UCD-system | Staff Inputs | W-15 | — |
| [UC-13](use-cases/UC-13-view-my-assignments-and-workload.md) | Staff | UCD-system | Roster & Hours | W-11 | — |
| UC-14 | — | — (Withdrawn) | — | — | — |
| [UC-15](use-cases/UC-15-notify-staff.md) | Email Service, SMS Gateway «system» | UCD-system | Notification | W-11, W-03 | — |
| [UC-16](use-cases/UC-16-upload-csv.md) | Manager | UCD-system | CSV Import | W-05 | — |
| [UC-17](use-cases/UC-17-update-roster-and-hours.md) | Manager | UCD-system | Roster & Hours, Scheduling Engine | W-09, W-10 | — |
| [UC-18](use-cases/UC-18-set-standby-preference.md) | Technician | UCD-system | Staff Inputs | W-14 | BB-01 to BB-06 |

## 3. Class index (CD-final)

| Class ID | Stereotype | Component / package | Requirements | Status vs M1 |
|---|---|---|---|---|
| CL-User | entity (abstract) | Domain Model | FR-43, FR-44 | Kept |
| CL-Account | entity | Domain Model | FR-43, FR-45, FR-46, FR-47, FR-48, NFR-07 | Kept |
| CL-PasswordResetToken | entity | Domain Model | FR-47 | **New** |
| CL-Manager | entity | Domain Model | FR-43 | Kept |
| CL-ITAdministrator | entity | Domain Model | FR-44, FR-45 | Kept |
| CL-Staff | entity (abstract) | Domain Model | FR-12, FR-35, FR-36 | Changed (no Leave balance) |
| CL-Driver | entity | Domain Model | FR-26 | Kept (assumption A1) |
| CL-Technician | entity | Domain Model | FR-22, FR-31, FR-51, FR-55, FR-56 | Changed (homeZone; derived hours) |
| CL-Certification | entity | Domain Model | FR-22, FR-27 | Changed (no number) |
| CL-Availability | entity | Domain Model | FR-12, FR-13, FR-14, FR-15 | Changed (per day) |
| CL-StandbyPreference | entity | Domain Model | FR-51 | **New** (provisional/confirmed decision; replaces CL-JobPreference) |
| CL-LeaveRecord | entity | Domain Model | FR-52 | **New** (replaces CL-LeaveRequest) |
| CL-VanAvailability | entity | Domain Model | FR-53 | **New** (replaces CL-Van) |
| CL-CsvImport | entity | Domain Model | FR-52, FR-53, FR-54 | **New** |
| CL-Job | entity | Domain Model | FR-01, FR-02, FR-03, FR-04, FR-05 | Changed (zone; two statuses) |
| CL-WeeklyRoster | entity | Domain Model | FR-09 | Kept |
| CL-Crew | entity | Domain Model | FR-26, FR-27 | Changed (vanNumber, coverage zones, initial/effective members) |
| CL-Assignment | entity | Domain Model | FR-07, FR-08, FR-35, FR-42, FR-57 | Optional Crew; dutyDate and per-Job attributed Staff |
| CL-Replacement | entity | Domain Model | FR-10, FR-35, FR-57 | **New in v4.1**; effective boundary and outgoing/incoming Staff |
| CL-Standby | entity | Domain Model | FR-30, FR-56, FR-57 | Changed (retained source/activated record, once-daily floor/count) |
| CL-HoursEdit | entity | Domain Model | FR-35, FR-57 | **New** |
| CL-JobRejectionRequest | entity | Domain Model | FR-37, FR-38 | Simplified (no Short notice) |
| CL-AuditLog | entity | Domain Model | FR-49, FR-58 | Kept (reason added) |
| CL-Notification | entity | Domain Model | FR-40, FR-39 | Kept (explicit) |
| CL-AuthController | control | Authentication | FR-43, FR-47, FR-48 | Kept |
| CL-AccountController | control | Account Management | FR-44, FR-45, FR-46, FR-22, FR-49 | Changed |
| CL-AvailabilityController | control | Staff Inputs | FR-12, FR-13 | Changed |
| CL-StandbyPreferenceController | control | Staff Inputs | FR-51 | **New** |
| CL-RequestController | control | Staff Inputs | FR-37, FR-38 | Trimmed |
| CL-CsvImportController | control | CSV Import | FR-52, FR-53, FR-54 | **New** |
| CL-CsvRowMapper | interface | CSV Import | FR-52, FR-53, FR-54 | **New** |
| CL-HrLeaveCsvMapper | class | CSV Import | FR-52 | **New** |
| CL-VanAvailabilityCsvMapper | class | CSV Import | FR-53 | **New** |
| CL-JobController | control | Job Management | FR-01, FR-02, FR-03, FR-04, FR-05, FR-34, FR-50 | Changed |
| CL-CrewFormingService | control | Scheduling Engine | FR-55 | **New** |
| CL-StandbyActivationService | control | Scheduling Engine | FR-56 | **New** |
| CL-TechnicianRanking | interface | Scheduling Engine | FR-55, FR-56 | **New** (Strategy) |
| CL-WorkloadRanking | class | Scheduling Engine | FR-55 | **New** |
| CL-ActivationRanking | class | Scheduling Engine | FR-56 | **New** |
| CL-RuleValidator | control | Scheduling Engine | FR-13, FR-15, FR-26, FR-27, FR-32, FR-33, FR-30, FR-51 | Changed |
| CL-RosterController | control | Roster & Hours | FR-45, FR-26, FR-07, FR-31, FR-33, FR-09, FR-10, FR-11, FR-30 | Changed |
| CL-HoursController | control | Roster & Hours | FR-57 | **New** |
| CL-DashboardController | control | Roster & Hours | FR-14, FR-40, FR-41 | Changed |
| CL-NotificationService | control | Notification | FR-39 | Kept |
| CL-NotificationChannel | interface | Notification | FR-39 | **New** |
| CL-EmailChannel | class | Notification | FR-44, FR-47, FR-39 | **New** |
| CL-SmsChannel | class | Notification | FR-39 | **New** |
| CL-RetentionJob | control | Audit & Retention | FR-58, NFR-10 | **New** |
| CL-LoginPage | boundary | Web UI | FR-43, FR-47 | Kept |
| CL-LandingPage | boundary | Web UI | FR-14, FR-40, FR-41 | Kept; rendering/input only (DEC-109) |
| CL-OfflineAssignmentController | control | Web UI (browser) | NFR-05, NFR-08, NFR-13; DEC-109 | New; approved local-copy processing |
| CL-AccountAdminPage | boundary | Web UI | FR-44, FR-45, FR-46, FR-22 | Kept |
| CL-AuditLogPage | boundary | Web UI | FR-49 | **New** (split from AccountAdminPage) |
| CL-JobPage | boundary | Web UI | FR-01, FR-04 | Kept |
| CL-CsvUploadPage | boundary | Web UI | FR-52, FR-53, FR-54 | **New** |
| CL-JobAllocationPage | boundary | Web UI | FR-07, FR-31, FR-09, FR-55 | Changed |
| CL-UpdateRosterPage | boundary | Web UI | FR-57 | **New** |
| CL-StandbyListView | boundary | Web UI | FR-56 | **New** |
| CL-AvailabilityPage | boundary | Web UI | FR-12 | Changed |
| CL-StandbyPreferencePage | boundary | Web UI | FR-51 | **New** |
| CL-RequestPage | boundary | Web UI | FR-37 | Trimmed |
| CL-RequestReviewPage | boundary | Web UI | FR-38 | Trimmed |

**Removed classes (M1 → M2):** CL-Van, CL-WorkshopServicing, CL-LeaveRequest, CL-LateAvailabilityChangeRequest, CL-JobPreference, CL-VanController, CL-CompletionController, CL-VanPage, CL-JobCompletionPage (DEC-73, DEC-76, DEC-79, DEC-83, DEC-85).

## 4. M2 diagram source index

| Source | Report section | Status |
|---|---|---|
| [UCD-system](diagrams/UCD-system.puml) | §1.2 (use-case summary) | v3.1; rendered locally with PlantUML 1.2026.8; team review pending |
| [CD-final](diagrams/CD-final.puml) | §1.3 | v4.1 rules; rendered locally with PlantUML 1.2026.8; team review pending |
| [CMP-system](diagrams/CMP-system.puml) | §2 | v4.1 rules; rendered locally with PlantUML 1.2026.8; team review pending |
| [ARCH-layered](diagrams/ARCH-layered.puml) | §3.1 | v4.1 rules; rendered locally with PlantUML 1.2026.8; team review pending |
| [DP-strategy-ranking](diagrams/DP-strategy-ranking.puml) | §3.2 | v4.1 rules; rendered locally with PlantUML 1.2026.8; team review pending |
| [DP-strategy-standard](diagrams/DP-strategy-standard.puml) | §3.2 | Standard pattern-role exposition; DEC-93/99; no additional domain classes or requirements |
| [CFG-classify-technicians](diagrams/CFG-classify-technicians.puml) | §4.2 | v4.1 rules; rendered locally with PlantUML 1.2026.8; team review pending |

## 5. M1 diagrams after the M2 changes

Sequence and activity diagrams are not M2 deliverables (template §1–§5). Their status is recorded so that no outdated diagram is reused by mistake.

| Diagram | M2 status | Reason |
|---|---|---|
| CD-domain, CD-control, CD-boundary | **Superseded by CD-final** | DEC-73 to DEC-98 |
| AD-01 Weekly roster | Needs rework before reuse | Suggested Roster, CSV upload, no Leave decisions (DEC-74, DEC-80) |
| AD-02 Set availability | Needs rework before reuse | Per-day Availability; no late-change request (DEC-83) |
| AD-03 Job rejection | Needs update before reuse | Short notice and Linked partners retired (DEC-90) |
| AD-04 Create user account | Needs update before reuse | Home zone; no certificate number (DEC-75, DEC-77) |
| SD-01 | Still valid in substance | — |
| SD-08 | Needs update before reuse | Confirmed picks, minimum-Crew publication check and preference outcome notification (DEC-98) |
| SD-02, SD-03, SD-04, SD-05, SD-07, SD-09, SD-12, SD-13, SD-14, SD-17, SD-18, SD-20 | Need update before reuse | Class and rule changes above (SD-07 needs the Suggested Roster) |
| SD-06, SD-10, SD-11, SD-15, SD-16, SD-19, SD-21 | **Withdrawn** (IDs kept) | Their use cases or requirements were withdrawn (DEC-76, DEC-83, DEC-85, DEC-90) |

## 6. M1 history

### M1 sequence source index (report §4.3)

| Source | Title | Related use cases |
|---|---|---|
| [SD-01](diagrams/SD-01-log-in-out.puml) | Log In/out (UC-01) | UC-01 |
| [SD-02](diagrams/SD-02-reset-password.puml) | Reset Password (UC-02) | UC-02 |
| [SD-03](diagrams/SD-03-create-user-account.puml) | Create User Account (UC-03) | UC-03 |
| [SD-04](diagrams/SD-04-manage-user-access.puml) | Manage User Access (UC-04) | UC-04 |
| [SD-05](diagrams/SD-05-manage-job.puml) | Manage Job (UC-05) | UC-05 |
| [SD-06](diagrams/SD-06-manage-vans-and-workshop-servicing.puml) | Manage Vans and Workshop Servicing (UC-06) | UC-06 |
| [SD-07](diagrams/SD-07-form-crews-and-standby.puml) | Form Crews and Standby (UC-07) | UC-07 |
| [SD-08](diagrams/SD-08-publish-weekly-roster.puml) | Publish Weekly Roster (UC-07) | UC-07 |
| [SD-09](diagrams/SD-09-compare-staff.puml) | Compare Staff (UC-08) | UC-08 |
| [SD-10](diagrams/SD-10-decide-leave-request.puml) | Decide Leave Request (UC-09) | UC-09 |
| [SD-11](diagrams/SD-11-decide-late-availability-change.puml) | Decide Late Availability Change (UC-09) | UC-09 |
| [SD-12](diagrams/SD-12-decide-job-rejection-request.puml) | Decide or Lapse Job Rejection Request (UC-09) | UC-09 |
| [SD-13](diagrams/SD-13-view-manpower-dashboard.puml) | View Manpower Dashboard (UC-10) | UC-10 |
| [SD-14](diagrams/SD-14-set-availability-and-preferences.puml) | Set Availability + Preferences (UC-11) | UC-11 |
| [SD-15](diagrams/SD-15-submit-leave-request.puml) | Submit Leave Request (UC-12) | UC-12 |
| [SD-16](diagrams/SD-16-submit-late-availability-change.puml) | Submit Late Availability Change (UC-12) | UC-11, UC-12 |
| [SD-17](diagrams/SD-17-submit-job-rejection-request.puml) | Submit Job Rejection Request (UC-12) | UC-12 |
| [SD-18](diagrams/SD-18-view-my-assignments-and-workload.puml) | View My Assignments and Workload (UC-13) | UC-13 |
| [SD-19](diagrams/SD-19-complete-job.puml) | Complete Job (UC-14) | UC-14 |
| [SD-20](diagrams/SD-20-notify-staff.puml) | Notify Staff (UC-15) | UC-15 |
| [SD-21](diagrams/SD-21-handle-invalidated-crew.puml) | Handle Invalidated Crew and Certification Expiry (FR-29, no UC) | UC-09, UC-10 |

The draft IDs SD-07, SD-09, SD-12 and SD-26 to SD-30 were consolidated before submission (DEC-57) and the draft SD-18 Allocate Job is not in the report. Their sources are in `diagrams/archive/` under their draft numbers.


## 7. v4.1 clarification coverage

| Decision | Current design / use cases | Verification |
|---|---|---|
| DEC-96 Active/Credited Hours and distinct activated dates | CD-final Staff/Technician/Standby/HoursEdit; DP/CFG; UC-08/10/13/17 | BB/CFG structure; SC-01–05, SC-10 |
| DEC-97 Direct duty, eligible replacement, per-Job history, coverage Zones | CD-final Assignment/Replacement/Crew; CMP/ARCH; UC-05/07/09/12/17 | SC-05, SC-11, SC-13/14 |
| DEC-98 Provisional confirmation, no override, capacity | CD-final StandbyPreference/RuleValidator; CMP IStaffInputs; UC-07/18 and UC-15 exception | BB-01–06; SC-06–09, SC-12, SC-15 |

The 16 active UC IDs and 45 active FR IDs are unchanged. M1 sources/interviews and historical decision entries are preserved. Current diagrams render locally; this is design verification, not execution of an implemented scheduling application. The corrected prototype is retained in m2/wireframes-prototype.html. Screenshots are report illustrations; production-code execution is not claimed.



## 8. v4.1.1 second-review coverage

| Decision | Current design / use cases | Verification |
|---|---|---|
| DEC-102 resolves historical DEC-100 | NFR-05/13; LandingPage cache methods/note; ARCH-layered; UC-01/13; W-11 | Per-user today-only offline scope, no changes, logout clear and date expiry; on-site authoritative-store inspection |
| DEC-103 resolves historical DEC-101 | FR-04/39; UC-05/15; W-04 | Draft deletion sends no Staff notice; Published Assigned Job deletion notifies attributed Staff; existing preference exception retained |
| DEC-104 source/quality/design presentation corrections | SRS §11 lecture-trait assessment; CsvImportController → CsvRowMapper checks → CsvImport.recordValidation(errors); CD/CMP/ARCH; UC-16; W-06 | BB-07 supplements R6 without a seventh rule; full 32-combination table and CFG unchanged; Driver >40 h display; prototype syntax/data checks and report/source parity |

The v4.1.1 baseline includes uncommitted corrections on codex/m2-review-fixes above 0ab8f1e. Historical decision/log entries are preserved; no new commit or team review is claimed.


## 9. v4.1.2 encrypted offline-copy clarification

| Decision | Current design / use cases | Verification |
|---|---|---|
| DEC-105: NFR-08 covers the offline copy; approved Option A local password unlock and successful-online-load refresh | NFR-05/08; LandingPage cache/unlock methods and note; ARCH-layered; UC-13; W-11; design notes | Planned inspection of persisted encrypted data/key protection; successful online refresh; offline reopened locked state, wrong password stays locked, correct password reveals only today Published data, no repeated prompt while unlocked. Prototype demonstrates sample states only; encryption and key lifecycle remain to be implemented/verified |

Current baseline: SRS v4.1.3, incorporating the reviewed corrections recorded in DEC-99 and DEC-102–107. Earlier baseline sections remain historical. Existing-session key lifecycle, password change/reset handling and DEC-61 authentication details remain follow-ups; no additional offline attempt limit or session policy is inferred.


## 10. 2026-11-11 review representation corrections

| Decision | Current artefacts | Verification |
|---|---|---|
| DEC-106: D1–D4 editorial/design clarification; no behavioural decision change | SRS §11; FR-52/54 mechanisms; UC-16; CD-final CsvImport note; design and wireframe prose; report | Source/report parity; one transaction includes file-date replacement, Committed status and successful-upload AuditLog; all requirement statements, IDs, class definitions/relationships, tests and prototype unchanged |

The SRS remains v4.1.2. Historical decision/log entries remain unchanged; the correction does not resolve existing source gaps or add a workflow.


## 11. Targeted report and representation corrections (DEC-107)

SRS v4.1.3 expresses actor capabilities from the system perspective, preserving all IDs, permissions and established behaviour. FR-33 treats missing Van CSV as the FR-40 planning alert and follows UC-07's existing CSV precondition/return to UC-16; it is not a reasoned capacity override. W-14's Awaiting CSV display remains Provisional and locked. The applied Strategy view explicitly elaborates ranking-to-Technician read dependencies from existing operations; CD-final still has 75 definitions and 96 explicit relationships. Component contracts are mapped to their provider operations in the design notes/report without adding class-level interfaces. The report retains the DEC-104/106 requirement-quality limitations.


## Current v4.2 changes (2026-11-14)

| Decision | Affected trace | Verification design |
|---|---|---|
| DEC-108 complete weekly HR snapshot | FR-33/51/52/54/55; UC-16, UC-07/18; CsvImport.coversWeek and metadata; RosterController.checkCsvReadiness; W-05/06/14 | CSV-01–08: header-only coverage, replacement/other-week isolation, invalid/partial input, failed-save prior coverage and Availability independence |
| DEC-109 browser controller allocation | NFR-05/08/13; LandingPage and OfflineAssignmentController; CD-final/CMP/ARCH; UC-13; W-11 | Same approved offline lifecycle design checks; explicit View/client Controller/server deployment distinction |

Current baseline: SRS v4.2. CD-final: 76 definitions and 99 explicit relationships. Earlier baseline counts/entries above describe their historical revisions. Core BB/WB tables and all seven basis paths remain. Prototype sample states are not evidence of production transaction, encryption or authentication execution.
