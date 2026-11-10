# Software Requirements Specification: Aircon Service Workload Management System

> **Version 4.1.2 (2026-11-10), M2 working baseline.** Builds on v3.5, the submitted M1 report baseline (DEC-72), whose IDs it keeps. This revision applies the team's M2 Design Update Brief ([m2/design-update-brief.md](m2/design-update-brief.md)) and decisions DEC-73 to DEC-98. v4.1 applies the member-confirmed Active Hours, Standby credit, direct duties, replacement history and provisional-preference rules. The system is now scoped to schedule planning (DEC-73). Requirements are written with **"must"**. The separate **Mechanism** column records M2 design traceability: the class, method, trigger and timing; it is not part of the requirement statement. v4.1.1 records the consistency corrections in DEC-99/104 and the approved offline-copy and Draft-deletion resolutions in DEC-102/103. v4.1.2 clarifies encrypted offline storage, local password unlocking and the successful-online-load refresh trigger (DEC-105). The 2026-11-11 review correction broadens the quality assessment and makes the existing CSV transaction boundary explicit (DEC-106); requirement statements and policies are unchanged. This baseline incorporates the reviewed corrections recorded in DEC-99 and DEC-102–106; team ratification is not implied by their inclusion. v3.5 (the M1 report baseline) is in git history.
> **Change control:** any later requirement or use-case change needs a new DEC entry and a version bump.
> Every row cites its source. IDs follow the submitted M1 report and are never reused or renumbered (DEC-72, DEC-92). New M2 requirements continue from FR-51 and NFR-13. Withdrawn rows stay in §3.11, and §9 lists every change from M1.
> Priorities use MoSCoW. Brief R1–R11 are the minimum deliverable, so they are always `Must`.
> **†** marks a numeric threshold chosen by the team rather than stated by a stakeholder.

---

## 1. Introduction

### 1.1 Purpose

This SRS specifies the functional and non-functional requirements of a web-based workload management system for the aircon service team of an aircon retailer. It builds on the submitted M1 report baseline (v3.5, DEC-72) and is the baseline for the Milestone 2 final class diagram, component diagram, architecture, design pattern, tests and wireframes.

### 1.2 Scope

The system lets the **Manager**:
- upload the HR leave CSV and the van availability CSV
- record Jobs
- generate a Suggested Roster, review and edit its Crews and Standby Staff, allocate Jobs one Planning Week at a time and publish the Weekly Roster
- update the roster and Active Hours during and after the week, including direct Standby Jobs and Crew replacements
- see Availability and Workload at a glance up to 1 month in advance
- decide Job Rejection Requests.

It lets **Staff** (Drivers and Technicians):
- enter Availability
- request one provisional Standby day per week (Technicians only), then see its capacity-checked confirmation
- see their published Assignments, Standby days and Workload
- request to reject a Job (the Manager decides).

It lets the **IT Administrator** manage accounts, roles, lockouts and Technician profiles, and view the Audit Log.

**Out of scope**, with the source for each exclusion:

| Excluded | Source |
|---|---|
| Job completion: actual times, remarks, follow-ups and invoice photos | M2-Brief §2, §3.1; DEC-76 |
| Leave applications, approvals and balances. Leave is read from the HR CSV | M2-Brief §2, §3.1; DEC-73; DEC-74 |
| Late Availability changes after the Availability Deadline | M2-Brief §3.1; DEC-83 |
| Overtime approval. It is settled between the Manager and the Staff member | M2-Brief §2; DEC-32 |
| Van management, licence plates and Workshop Servicing. Only the Van count per date is imported | M2-Brief §2, §3.1; DEC-85 |
| Phoning a Standby when they are activated. The system only records the result | M2-Brief §2, §4 step 13; DEC-81 |
| Direct connection to the HR system or the van vendor. Data arrives by CSV upload | M2-Brief §2; DEC-74 |
| Wages, job costs, payroll and commission | INT-MGR [System Q1]; DEC-44 |
| Live GPS tracking and route optimisation. Job order is set by the Manager | INT-MGR [System Q3]; INT-DRV [Q5]; DEC-08 |
| Customer self-booking | INT-MGR [Process Q2] |
| Sunday emergency jobs | INT-MGR [Clarification Q8]; DEC-45 |
| In-app delay reporting | DEC-33 |

### 1.3 Definitions

The canonical terms are in the [AGENTS.md glossary](AGENTS.md#glossary-canonical-terms). This SRS also uses these terms:

| Term | Meaning | Source |
|---|---|---|
| **Working day** | Monday–Saturday, 09:00–18:00, with lunch 13:00–14:00: **8 h** of work | DEC-12 |
| **Planning Week** | A Monday–Saturday week. "The Planning Week" is the next week not yet published | DEC-04, DEC-16 |
| **Availability Deadline** | 18:00 on the Wednesday 12 days before a Planning Week's Monday. After it, that week's Availability and Standby Preferences are locked | DEC-02, DEC-79 |
| **Standard Duration** | Servicing 1 h per unit, Installation 3 h per unit | DEC-22 |
| **Planned Hours** | A Job's duration + the fixed 0.5 h Travel Allowance | DEC-31, DEC-78 |
| **Standby Day Hours** | A 4 h minimum credit per rostered Standby date, including dates with short activated duties | DEC-96 |
| **Active Hours** | Planned Hours of Jobs attributed to that Staff member, including direct duties and replacement Jobs; a reasoned Hours Edit corrects this figure | DEC-96, DEC-97 |
| **Total Credited Hours / day hours** | On a rostered Standby date: max(4, Active Hours); otherwise Active Hours. Full-day Leave without duties gives 0 h | DEC-96 |
| **Workload** | Sum of Total Credited Hours over the week/month. Used for the 40 h target and highlight; distinct from Active Hours used for rotation | DEC-96 |
| **Projected hours** | Before Job allocation, estimate Active/Credited hours as 8/8 per Crew day and 0/4 per Standby day. Demote projected Credited >=40 h; rank by last week's Active, then projected Active hours | DEC-80, DEC-96 |
| **Overtime** | Workload strictly above 40 h in a Planning Week | DEC-04, DEC-86 |
| **Zone distance** | 0 for the same zone. 1 if either zone is Central, or for North–East, North–West, South–East and South–West. 2 for North–South and East–West† | DEC-77 |
| **Standby source** | Why a Technician is on Standby: `Preference` (their pick), `Algorithm` (a Dual-Certified Technician with 20 or more Active Hours last week), `Leftover` (not placed in a Crew) or `Manager` (named by hand) | DEC-80, DEC-81 |
| **Full Standby cover** | A working day's Standby Technicians together hold valid Certifications for both Brands | DEC-81 |
| **Draft / Published** | The two states of a Weekly Roster. Staff see Published weeks only | DEC-16 |
| **Job Rejection Request** | An attributed Staff member's request to unassign a Crew or direct Job; the Manager decides | DEC-42, DEC-97 |
| **Activation count** | Distinct activated Standby dates in the rolling 12 months; repeated duties on one date count once | DEC-96 |

### 1.4 Sources and citation format

| Citation | Source |
|---|---|
| `Brief R<n>` / `Brief §<section> ¶<n>` | [brief/project-description.md](brief/project-description.md), including its Lecturer clarifications |
| `DEC-nn` | [decisions.md](decisions.md) |
| `M1 Report §<n>` | The submitted M1 report (9 Oct 2026), the M1 source of truth; IDs follow it (DEC-72) |
| `M2-Brief §<n>` | The team's [M2 Design Update Brief](m2/design-update-brief.md), recorded in DEC-73 to DEC-91 |
| `INT-MGR [<label>]`, `INT-DCT [<label>]` | Interview transcripts in [elicitation/interviews/](elicitation/interviews/). `INT-DCT [Questionnaire <question>: <response ID>]` resolves to [the Technician questionnaire](elicitation/interviews/technician-questionnaire.md) |
| `INT-DRV [Q<n>]` | Driver transcript, numbered questions |
| `INT-ITA [Q: <topic>]` | IT Administrator transcript, cited by question topic |

### 1.5 Assumptions

The report must state these assumptions explicitly.

| ID | Assumption | Source |
|---|---|---|
| A1 | Enough Drivers are available every working day. Drivers are not ranked, make no Standby Preference and are never on Standby | M2-Brief §3.6; DEC-82 |
| A2 | At least 3 Vans are available every working day, because the company's own servicing schedule keeps at least 5 available | DEC-85 |
| A3 | Confirmation uses the latest HR/Van CSVs. Later Leave overrides initial placement; show the conflict for Manager repair without revoking other confirmed picks. Preserve attributed earlier Jobs for a mid-day departure | DEC-74, DEC-97, DEC-98 |
| A4 | The Manager uploads both CSV files before planning starts on the Thursday after the Availability Deadline | DEC-74 |
| A5 | Before Jobs are allocated, estimate 8 Active/8 Credited hours for a Crew day and 0 Active/4 Credited for a Standby day; use actual attributed Planned Hours after allocation | DEC-80, DEC-96 |
| A6 | The 2-digit postal sector of every Singapore postal code maps to exactly one Zone through a fixed table | DEC-77 |

---

## 2. Overall description

### 2.1 User classes and external systems

| User class / system | Description | Source |
|---|---|---|
| **Manager** | Office-based. May be more than one account, all with identical permissions. Has no Availability or Workload in the system | INT-MGR [Clarification Q1]; DEC-18 |
| **Driver** (Staff) | 6 in total. The only role allowed to drive. Enters Availability only (A1) | Brief §Company ¶4; DEC-82 |
| **Technician** (Staff) | 11 in total: 2 Dual-Certified, 5 M Electric only, 4 Dicon only. Has a home zone and Certifications (Brand, expiry) | Brief §Company ¶4; DEC-75; DEC-77 |
| **IT Administrator** | Manages accounts, roles, lockouts and Technician profiles, and views the Audit Log | Brief R11; DEC-17; DEC-75 |
| **Email Service** «system» | Non-human actor that delivers email: initial login details, reset links, new-device codes and notifications | DEC-46; DEC-49; DEC-88 |
| **SMS Gateway** «system» | Non-human actor that delivers SMS notifications | DEC-48; DEC-88 |
| HR system, van vendor | **Not actors.** Their CSV exports are uploaded by the Manager | M2-Brief §2; DEC-74 |

### 2.2 Operating environment

- The application and its database run on an **on-site server** (NFR-13).
- Browsers: Chrome is the priority; Edge, Firefox and DuckDuckGo must also work.
- Devices: company laptops and tablets, and modern phones. Field use has patchy signal in basements and car parks.

Sources: INT-ITA [Q: Devices]; INT-DCT [Questionnaire C18/C19]; DEC-89.

### 2.3 Constraints

- The system is a web application (Brief R1).
- Operations run Monday–Saturday, 09:00–18:00. The company is closed on Sundays (DEC-12; DEC-45).
- Current headcount: 6 Drivers and 11 Technicians. The fleet is 6 Vans, of which the van CSV gives the number available per date (Brief §Company ¶3–4; DEC-85).

### 2.4 Weekly cycle

Example for the Planning Week starting Monday the 19th:

| Step | When |
|---|---|
| Staff enter Availability; Technicians request a provisional Standby day | Any time within the 1-month window, until the deadline |
| Availability Deadline (the week locks) | Wednesday the 7th, 18:00 |
| Manager uploads the HR and van CSVs, resolves provisional picks against minimum Crew/Standby capacity, generates the Suggested Roster, sets Crew zone coverage, edits permitted placements, then allocates Jobs | From Thursday the 8th (the roster is Draft) |
| Manager publishes | Monday the 12th (Staff are notified) |
| The week runs. The Manager records replacements, Standby activations and hours | Monday the 19th to Saturday the 24th, and afterwards |

Sources: Brief §Company ¶1; INT-MGR [Clarification Q6 follow-up]; DEC-02; DEC-16; DEC-74; DEC-80.

### 2.5 Design principle: the system suggests, the Manager decides

- **Declarations:** Staff set Availability until the Availability Deadline.
- **Provisional requests and guaranteed confirmation:** after the deadline and CSV checks, confirm only picks that leave three valid Crews and Full Standby cover feasible. A confirmed pick guarantees initial Standby placement; Leave overrides it and genuine activation remains possible (DEC-98).
- **Suggestions:** the system suggests Crews and Standby Staff and orders Standby Staff for activation. The Manager can change suggestions within hard rules, but cannot override confirmed preferences. Every change is logged (DEC-80, DEC-89, DEC-98).
- **Requests:** Staff submit Job Rejection Requests and the Manager decides them (DEC-42).

---

## 3. Functional requirements

The **Description** column states the required behaviour and sourced constraints. The separate **Mechanism** column gives design traceability through `Class.method()`, the triggering actor or event, and when it happens; it does not prescribe implementation as part of the requirement statement. «C» marks a control class, «E» an entity and «B» a boundary page, as in the final class diagram ([diagrams/CD-final.puml](diagrams/CD-final.puml)).

### 3.1 Job and Weekly Roster management

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-01 | The Manager must create a Job. **Required:** customer name, customer phone, address, postal code, Brand, Job Type (Installation or Servicing), number of units (≥1), preferred date (a working day) and preferred Slot. **Optional:** unit number, aircon model, notes. The system must derive the Job's **zone** from the postal code (A6) | «C» `JobController.createJob(details)` creates «E» `Job` and calls `Job.deriveZone()` (`Zone.fromPostalCode()`). Trigger: Manager on «B» `JobPage` | INT-MGR [Process Q2]; DEC-11; DEC-77 | Must | Agreed | Required fields only → saved with a zone. Units = 0 → refused. Sunday date → refused. Unknown postal sector → refused |
| FR-02 | The Job's duration must be pre-filled from its Standard Duration (Servicing 1 h per unit, Installation 3 h per unit). The Manager can adjust it | «C» `JobController.standardDuration(jobType, units)`; «E» `Job.durationHours`. Trigger: Job entry | INT-MGR [Process Q2 follow-up: hours]; DEC-22 | Must | Agreed | 2 Installation units → 6 h. Edited to 7 h → saved |
| FR-04 | The Manager must be able to edit a Job or delete it when the customer cancels. **Edit:** an Assigned Job is re-checked against FR-32; if it now breaks a rule it becomes Unassigned and the Manager is told why. **Delete:** notify its attributed Staff first only if the Assignment is Published; a Draft deletion sends no Staff notice. **Time limit:** a Job dated in the past or already started cannot be edited or deleted | «C» `JobController.editJob(job, changes)` → `Job.changeDetails()`, `RuleValidator.checkBlocking()`. `JobController.deleteJob(job)` checks the Weekly Roster state, calls «C» `NotificationService.notify(JobDeleted, attributedStaff)` only for a Published Assignment, then deletes the Job and its «E» `Assignment`. Trigger: Manager on «B» `JobPage` | M2-Brief §3.2; INT-MGR [added follow-up: cancellations]; DEC-19; DEC-76; DEC-103 | Must | Agreed | Change a Job's Brand to one the Crew can't do → Unassigned with reason. Delete an Assigned Draft Job → no Staff notice; delete a Published one → attributed Staff notified, Job gone. Yesterday's Job → no edit or delete |
| FR-05 | A Job must be `Unassigned` or `Assigned` only. Unassigned → Assigned on allocation. Assigned → Unassigned on an approved Job Rejection Request, an invalidating edit, an account change (FR-45, FR-46) or the Manager unassigning it. While a Job Rejection Request is pending the Job stays Assigned | «E» `Job.markAssigned()` and `Job.markUnassigned(reason)` via «C» `RosterController` or `JobController`; `RequestController` delegates approved unassignment and `AccountController` delegates future-roster removal to `RosterController`. Trigger: those events | M2-Brief §3.2; INT-MGR [Conflicts Q3]; DEC-42; DEC-76 | Must | Agreed | Test each transition. A third status cannot be set |
| FR-07 | The Manager must allocate Jobs one Draft Planning Week at a time. Normal Jobs go to a Crew with a start time. During the running day UC-17 can allocate an extra Job directly to one eligible Standby Technician without a Driver/Van. Show Crews with coverage zones, initial members, Standby, direct duties and Unassigned Jobs | `RosterController.allocateJob()` creates an `Assignment` with date and attributed Staff copied from `Crew.membersFor(job)`; `HoursController.activateForJob()` creates a direct Assignment (no Crew, exactly one Technician) | Brief R3; DEC-16; DEC-97 | Must | Agreed | Crew Job attributes its effective members. Direct Job attributes one certified Technician, no invented Van/Driver |
| FR-08 | Jobs must run within 09:00–18:00, skipping lunch 13:00–14:00. A Job may span Slots. Consecutive Jobs must leave the fixed 0.5 h Travel Allowance and not overlap, both per Crew and per attributed person across Crew/direct duties | `Assignment.startTime`, `endTime()`; `RuleValidator.checkAssignment()` before allocation, activation or move | DEC-12; DEC-31; DEC-97 | Should | Agreed | 3 h at 11:00 ends 15:00. Next duty at 15:10 refused; 15:30 accepted. Check direct-to-Crew transfers too |
| FR-09 | A Weekly Roster must remain Draft until publication. Staff see Assignments only after publication; preference decisions are separately visible/notified. Publish only with >=3 valid initial Crews per working day and no FR-32 violation; allow FR-33 warnings with logged reasons. Confirmed picks cannot be overridden. Notify affected Staff on publication | `RosterController.publish()` calls `RuleValidator.checkBlocking()`, `WeeklyRoster.publish()` and `NotificationService.notify()`; Manager edits write `AuditLog` | Brief R3; DEC-16; DEC-89; DEC-98 | Must | Agreed | 2 Crews blocks publication. Missing standby cover warns. Confirmed preference moved to initial Crew is blocked even with a reason |
| FR-10 | After publication the Manager must be able to add, move or unassign unstarted Jobs and change initial future Crews/Standby within FR-32/33. Today's replacements and direct duties use UC-17 and preserve earlier Job attribution. Past roster attribution is read-only; retrospective Active Hours corrections are allowed | `RosterController.allocateJob()`, `moveJob()`, `unassignJob()`, `changeCrew()`, `nameStandby()`; `HoursController` for activation/replacement. Notify after saved changes | DEC-16; DEC-88; DEC-97; DEC-98 | Must | Agreed | Today's Job 1 keeps Alex; replacement from Job 2 attributes Ben. Yesterday's roster cannot be rewritten; an audited Active Hours correction can be saved |
| FR-11 | The weekly timeline must show one row per Crew/Van per date with its coverage zones and Jobs, per-Job effective members, a Standby row and direct Standby duties labelled without a Van | `RosterController.buildTimeline(week)` reads `Crew`, `Assignment.assignedStaff`, `Replacement` and `Standby` | INT-MGR [System Q2]; DEC-85; DEC-97 | Must | Agreed | Four Crews show four Van rows; one direct duty does not create a fifth Van or change the initial Crew count |
| FR-55 | For a Draft week with locked inputs and HR/Van CSVs, the system must first resolve provisional picks (FR-51). **Classification, per day:** exclude unavailable/Leave Technicians; reserve confirmed picks; put duals with >=20 Active Hours last week on Algorithm Standby; rank the rest with projected Credited <40 h first, then last week's Active Hours, projected Active Hours and staff ID. **Formation:** form both-Brand Crews (one dual or an opposite-Brand pair) up to Van count, preserving Full Standby cover beyond three. **Minimum recovery:** if <3, recall Algorithm then Leftover Standby, lowest-ranked first, never confirmed picks. Use a feasible minimum arrangement if greedy choices would strand a Brand or lose feasible cover. Others become Leftover Standby. **Projection:** assign available Drivers by ID; estimate Crew 8/8 and Standby 0/4 Active/Credited hours before the next day. Report shortages. **Regeneration:** must retain confirmed picks and is refused if Jobs/manual roster edits would be discarded | `RosterController.prepareSuggestion()` coordinates `StandbyPreferenceController.confirmWeek()` and `CrewFormingService.suggestRoster()`; `classifyTechnicians()`, `formCrews()`, `ensureMinimumCrews()`, `assignDrivers()` use WorkloadRanking; `RuleValidator.findMinimumCoverage()` returns a feasible arrangement. Save Draft and audit | Brief R3; DEC-80; DEC-96; DEC-98 | Must | Agreed | WB-01–07 plus SC-10–12. A dual with 0 Active/24 Credited last week is ranked, not forced to Standby. Confirmed picks preserved; baseline minimum covered when feasible |

### 3.2 Availability and Standby Preference

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-12 | Staff must set each working day to `Available` or `Unavailable`, and may clear an entry. A day with no entry is **Not submitted** and counts as unavailable. Sundays are not offered | «E» `Availability(staff, date, state)`; «C» `AvailabilityController.save(edits)` → `Availability.setState(state)` / `Availability.clear()`. Trigger: Staff on «B» `AvailabilityPage` | Brief R8; INT-MGR [Clarification Q4]; DEC-03; DEC-83 | Must | Agreed | Set Tuesday Available → saved. Leave Wednesday blank → treated as unavailable by FR-55. No Sunday column |
| FR-13 | Staff must be able to enter or change Availability only for dates from **today through the same calendar date next month, inclusive** (clamped to that month's last day), and only before the Availability Deadline | «C» `AvailabilityController.checkWindowDeadline(dates)` using «C» `RuleValidator.availabilityDeadline(week)`. Trigger: each save | Brief R8 + Lecturer clarification; DEC-01; DEC-02; DEC-30 | Must | Agreed | From 15 Mar: 15 Apr accepted, 16 Apr refused. From 31 Jan: 28 Feb accepted (non-leap year), 1 Mar refused |
| FR-14 | The Manager must view all Staff's Availability up to 1 month in advance as a grid, with Staff down the side and days across. Each cell shows one of: Available; on Leave, Emergency Leave or MC (from the HR CSV); Unavailable or Not submitted. A Technician's Standby pick and Provisional/Confirmed/NotConfirmed status are marked in its cell | «C» `DashboardController.availabilityGrid(from, to)` reads «E» `Availability`, «E» `LeaveRecord` and «E» `StandbyPreference`. Trigger: Manager opens the grid on «B» `LandingPage` | Brief §Intro ¶4 + Lecturer clarification; INT-MGR [System Q2]; M2-Brief §3.2; DEC-74 | Must | Agreed | Seed each state and check its distinct colour and legend. A Leave Record overrides an Available entry |
| FR-15 | Availability and Standby Preferences for a Planning Week must lock at **18:00 on the Wednesday 12 days before** that week's Monday, in company local time | «C» `RuleValidator.availabilityDeadline(week)` is checked by `AvailabilityController.save()` and `StandbyPreferenceController.submitPick()` at save time. Trigger: each save | Brief §Company ¶1; DEC-02; DEC-79 | Must | Agreed | Week of Mon 19th: a save at Wed 7th 17:59 is accepted; at 18:00 it is refused |
| FR-51 | **Submission:** a Technician must be able to request one provisional Standby day/Brand slot per Planning Week before the Availability Deadline. One M Electric and one Dicon slot per day are reserved first come first served; a dual may take either. Submission checks deadline, availability/no Leave, valid Certification and free slot in that order. Change/withdraw frees the old slot; changing day/Brand resets submission time, while an unchanged resubmission preserves it. **Confirmation:** after the deadline and required CSVs, process requests by submission time/staff ID, confirming only if eligibility and >=3 valid Crews plus Full Standby cover remain feasible. **Outcome:** record Confirmed or NotConfirmed with reason/time and notify. Confirmed picks guarantee initial Standby, cannot be overridden, remain callable and yield to Leave | `StandbyPreferenceController.submitPick()/withdrawPick()`; `StandbyPreference` stores submittedAt/status/decidedAt/reason. `confirmWeek()` uses `RuleValidator.findMinimumCoverage(day, reservedPicks)` and eligibility checks; saves a day's decisions atomically and notifies through UC-15. Trigger: Technician before deadline; Manager's preparation of the Draft week after CSV upload | Brief R9; DEC-79; DEC-98 | Must | Agreed | BB-01–06 cover the six provisional-submission rules; BB-07 supplements R6 with an unchanged resubmission preserving submittedAt. SC-06–09 cover confirmation. Duplicate submissions cannot take the same slot; retrying confirmation cannot revoke or renotify a confirmed pick |

### 3.3 External data (CSV upload)

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-52 | The Manager must be able to upload an **HR CSV** with columns staff ID, date and type (`Leave`, `Emergency Leave` or `MC`). Each valid row creates a read-only Leave Record. A Leave Record makes that person unavailable that day, overriding their Availability and any initial Standby placement without erasing preference history; later clashes raise a staffing alert for Manager repair (DEC-98) | «C» `CsvImportController.upload(file, HRLeave)` creates «E» `CsvImport`; `CsvImport.parse(file)` returns rows. The controller checks required columns and each row with its application-layer «interface» `CsvRowMapper` (`HrLeaveCsvMapper`), collects whole-file errors and calls `CsvImport.recordValidation(errors)`. Only if error-free, it maps the validated rows and, in one transaction, replaces «E» `LeaveRecord`s for the file dates, calls `CsvImport.commit()` to mark the import `Committed`, and writes the successful-upload «E» `AuditLog` entry. Trigger: Manager on «B» `CsvUploadPage`, before planning (A4) | M2-Brief §2, §3.2; DEC-74; DEC-104; DEC-106 | Must | Agreed | Upload 3 valid rows → 3 Leave Records; the grid shows Leave. Upload a later file for the same dates → old records replaced |
| FR-53 | The Manager must be able to upload a **van CSV** with columns date and vans available (a whole number, 0 or more). Each valid row creates or replaces that date's Van Availability, which caps the number of Crews that day (FR-32) | As FR-52, with `CsvImportController.upload(file, VanAvailability)` and `VanAvailabilityCsvMapper` creating «E» `VanAvailability(date, vansAvailable)`. Trigger: Manager on «B» `CsvUploadPage` | M2-Brief §2, §3.1; DEC-74; DEC-85 | Must | Agreed | Upload "Mon 19th, 5" → 5 Crews allowed; a 6th → blocked |
| FR-54 | The system must validate a whole CSV file before saving any row. A missing column, an unknown staff ID, an invalid or Sunday date, an unknown type, a negative Van count or an empty file must reject the whole file, list every row error, and save nothing. Exact duplicate rows are saved once. Each upload is recorded with who, when, file type and outcome | «C» `CsvImportController.upload()` collects column, row and whole-file errors using `CsvRowMapper`, then calls «E» `CsvImport.recordValidation(errors)`. Errors set `status = Rejected` and save no Leave Record or Van Availability. Only an error-free file is mapped; in one transaction, the controller replaces the Leave Records or Van Availability for the dates in the file, calls `CsvImport.commit()` to mark the import `Committed`, and writes the successful-upload `AuditLog` entry. Trigger: each upload | M2-Brief §6.3, §7; DEC-74; DEC-104; DEC-106 | Must | Agreed | Wrong columns → rejected, 0 rows saved. Empty file → rejected. Duplicate row → 1 record. Mixed valid and invalid rows → rejected with the invalid rows listed |

### 3.4 Certifications and Crews

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-22 | The system must record each Technician's **home zone** and **Certifications**. A Certification is Brand and expiry date only; a Technician holds one or both Brands. The IT Administrator enters them at account creation and updates them later. A Certification is **valid on a date** when its expiry date is on or after that date | «E» `Technician.homeZone`; «E» `Certification(brand, expiryDate)` with `Certification.isValidOn(date)`. Updates by «C» `AccountController.updateTechnicianProfile(technician, homeZone, certifications)` → `Technician.setHomeZone()`, `Certification.renew(expiryDate)`. Trigger: IT Administrator | Brief §Company ¶2, ¶4; INT-MGR [Clarification Q5]; DEC-35; DEC-75; DEC-77 | Must | Agreed | Expiry equal to the Job date → valid. Expiry the day before → invalid (FR-32 blocks it) |
| FR-26 | Each initial Crew must have exactly one Driver and one or two Technicians on one Van per working day. Members must be available with no full-day Leave. A person has at most one initial Crew/Standby placement. Crew count cannot exceed the date's Van count. The Manager sets one or more coverage zones from the existing five. Operational replacements use FR-57; direct Standby Jobs use FR-07 and are not initial Van Crews | `Crew(date, vanNumber, zones)` with initial Driver/Technicians; `RosterController.changeCrew()/setCrewZones()`; `RuleValidator.checkCrew()` | Brief §Company ¶3–4; DEC-84; DEC-85; DEC-97 | Must | Agreed | 0/2 Drivers or 0/3 Technicians in an initial Crew is refused. Three Crews may share coverage of five Zones. Direct duty needs no Van |
| FR-27 | Attributed Technicians must hold valid Certification for every assigned Job's Brand. A single-Brand Crew is allowed if all its Jobs match. A direct duty requires its assigned Technician to hold that Job's Brand. A replacement must preserve coverage for every affected remaining Job | `Assignment.assignedStaff`, `Crew.coversBrands()` and `Certification.isValidOn()`; `RuleValidator.checkAssignment()/eligibleForDuty()` before ranking and save | Brief §Company ¶2–3; DEC-84; DEC-97 | Must | Agreed | M Electric-only candidate cannot replace the missing Dicon coverage; a valid dual can. Check later Jobs, not just the first affected Job |
| FR-30 | Standby is an available Technician initially outside every Crew, held for direct duties or replacement. The system must keep one record per Technician/date after activation. There is no maximum. Confirmed Preference placements cannot be manually removed or moved into initial Crews. Other manual changes are allowed within FR-32. Missing Full Standby cover warns; once activated, a busy Technician is not counted as currently available cover. The date's minimum credit remains 4 h | `Standby(technician, date, source, activated)`, `activate()` idempotent; `RosterController.nameStandby()/removeStandby()`; `RuleValidator.checkStandbyCover()` considers duty commitments | DEC-81; DEC-96; DEC-97; DEC-98 | Must | Agreed | Unused day 0 Active/4 Credited. Activated direct duty keeps the Standby record. A busy replacement is excluded from further call-outs |

### 3.5 Job Allocation and Workload

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-31 | The Manager must compare up to three Staff for a date/week: availability, Active Hours and Total Credited Workload this/last week, Certifications/expiry, provisional or decided preference, current duty/coverage zones or home Zone, and activated-day count | `RosterController.compare()` reads `Staff.activeHours()/workload()`, `Technician.locationOn()/activationCount()`, `StandbyPreference` | Brief R4, R5; DEC-77; DEC-96; DEC-98 | Must | Agreed | Fourth selection refused; label both hours distinctly and show preference status/reason |
| FR-32 | The system must block changes/publication causing invalid role/Brand/Certification, unavailable or Leave Staff in a future duty, person-level overlapping duties or insufficient travel, two initial Crews or simultaneous initial Crew/Standby placement, invalid Crew, Van-cap violation or Sunday. Block manual removal/reassignment of a confirmed preference. Retained activated Standby history is allowed with its duties. Publication requires >=3 valid initial Crews per day; later unavoidable staffing loss raises an alert for repair without rewriting history | `RuleValidator.checkBlocking()` called before atomic saves by RosterController, JobController and HoursController; validate attributed Staff and all remaining replacement Jobs | DEC-19; DEC-85; DEC-97; DEC-98 | Must | Agreed | Test direct-duty overlap, invalid replacement, confirmed-pick override, and 2-Crew publication. Valid activation of a confirmed pick succeeds |
| FR-33 | The system must warn and allow a logged reasoned override for Total Credited Workload >40 h, Job zone outside Crew coverage, start outside customer preference, missing Full Standby cover or missing Van CSV. Missing CSV still prevents suggestion/preference confirmation until capacity is known; manual publication must satisfy FR-32. Fewer than three Crews and confirmed-preference overrides are not overridable warnings | `RuleValidator.checkWarnings()`, `RosterController.confirmWarnings()`, `AuditLog.record()` | Brief R6; DEC-19; DEC-77; DEC-96; DEC-98 | Must | Agreed | 40 h no highlight; 40.5 h highlighted. A zone in a Crew's coverage set needs no override |
| FR-34 | The system must list the Jobs with status **Unassigned** and show their count | «C» `JobController.listUnassigned()`. Trigger: Manager opens «B» `JobAllocationPage` or «B» `LandingPage` | INT-MGR [Conflicts Q1] | Must | Agreed | Approve a Job Rejection Request → count +1. Delete an Unassigned Job → count −1 |
| FR-35 | Active Hours per Staff/date must be the latest reasoned Active Hours Edit, otherwise the sum of Planned Hours (duration + 0.5 h Travel Allowance) on Assignments attributed to that person. Total Credited Hours must be max(4, Active Hours) for a rostered Standby date, otherwise Active Hours. No duties/full-day Leave gives 0 h unless a valid Standby entitlement exists; Leave overrides unworked Standby. Preserve earlier duties on a mid-day departure. Workload sums Total Credited Hours over the week/month; show Active Hours separately | `Staff.activeHoursOn(date)` reads attributed Assignments/HoursEdit; `hoursOn(date)` applies the once-daily Standby floor; `activeHours(week)`, `workload(week)`, `monthlyWorkload(month)`. Derived on demand | DEC-31; DEC-96; DEC-97 | Must | Agreed | SC-01–05: Standby 0/4, 2/4, 4/4, 5/5; two duties 2+3 =>5/5. Alex retains Job 1; Ben receives only remaining Jobs |
| FR-36 | Workload is summed per Planning Week (Monday–Saturday). Workload **strictly above 40 h** is Overtime and must be highlighted wherever Workload is shown. The 40 h target/highlight uses Total Credited Hours (DEC-96). | «E» `Staff.isOvertime(week)` = `workload(week) > 40`. Trigger: Workload display | Brief R6; INT-MGR [Clarification Q7]; DEC-04; DEC-86 | Must | Agreed | **Boundary:** 40.0 h → not highlighted; 40.5 h → highlighted |

### 3.6 Roster updates and hours

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-56 | For a direct duty or Crew replacement, list eligible Standby Technicians only: available/no Leave, valid needed Brands and no conflicting duties/travel. Replacement candidates must fit every remaining Job. Rank by fewest activated dates in rolling 12 months, then home-Zone distance, then staff ID; show both hours totals and count. Repeated direct duties are allowed when non-overlapping; a Technician committed to a replacement Crew is excluded elsewhere. Highlight the recommended candidate to the Manager; a low count alone is not a misconduct indicator | `StandbyActivationService.listStandbysForJob(job, date, crew, outStaff)` filters using `RuleValidator.eligibleForDuty()` then ActivationRanking; recheck before save | DEC-96; DEC-97 | Must | Agreed | Wrong-Brand candidate with count 0 excluded before eligible count-2 candidate. Same-day second direct duty can be eligible but count remains one |
| FR-57 | **Operational update:** the Manager must record a direct Standby Job or a replacement from an unstarted Crew Job, preserving earlier Assignment Staff. Activate the date's retained Standby record once; count distinct activated dates. A replacement stores who/out/in/Crew/fromJobId/effectiveFrom/reason/time/Manager and updates only affected future Job attribution. **Hours correction:** Active Hours corrections for the last 12 months require reason and value 0–24; derive Total Credited Hours with the Standby floor, never add it twice. Operational replacements/direct assignments apply today; retrospective corrections change hours, not past attendance. **Save:** atomically save, audit and notify affected Staff | `HoursController.activateForJob()` or `recordReplacement()` creates Assignment/Replacement and calls `Standby.activate()`; `editHours(staff,date,newActiveHours,reason)` creates HoursEdit with oldActiveHours/newActiveHours. RuleValidator checks before save; NotificationService after commit | DEC-96; DEC-97 | Must | Agreed | 2 h activation =>2 Active/4 Credited/count+1; later 3 h =>5/5/count unchanged. Replacement from Job 2 leaves Job 1 unchanged. Missing reason/25 h refused |

### 3.7 Job Rejection Requests and notifications

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-37 | A Staff member must be able to submit a **Job Rejection Request** for a Crew or direct Job attributed to them in a Published week before the Job starts. Before submitting, the system must warn them to discuss it with the Manager first. They must pick a reason: Personal emergency; Missing equipment or parts; or Other, which needs a comment. Only one request may be pending per Assignment. The Manager is notified. Telling the company ahead of time that a Job can't be done uses this same function | «C» `RequestController.submitRejection(staff, assignment, reason, comment)` creates «E» `JobRejectionRequest` (status Pending) and calls «C» `NotificationService.notify(RejectionSubmitted, manager)`. Trigger: attributed Staff member on «B» `RequestPage`, after confirming the warning dialog | Brief R10, §Intro ¶3; INT-MGR [Conflicts Q3]; INT-DRV [Q17]; DEC-42; DEC-66 | Must | Agreed | Cancel at the warning → nothing saved. "Other" with no comment → refused. A second request on the same Assignment → refused |
| FR-38 | The Manager must approve or refuse each Job Rejection Request. While pending, the Job stays Assigned. **Approved:** the Job becomes Unassigned and leaves its Crew or direct allocation, and all attributed Staff are notified. **Refused:** the Assignment stands and the requester is notified with any reason. A request still pending when the Job starts lapses and the requester is notified | «E» `JobRejectionRequest.approve()`, `refuse(reason)` and `lapse()` via «C» `RequestController.decideJobRejection(request, decision, reason)`; `RequestController.onJobStart(assignment)` is triggered by the Clock at the Job's start time. Trigger: Manager on «B» `RequestReviewPage`, or the start time | Brief R10; DEC-42 | Must | Agreed | Approve → the Job is Unassigned. Refuse → unchanged. Pending at the start time → Lapsed |
| FR-39 | Staff must be notified **on their Landing Page, by email and by SMS** when: a week with their Assignments or Standby days is published; after publication, one of their Assignments, Crew places or Standby days is added, changed or removed, or one of their Assigned Jobs is deleted; their Job Rejection Request is decided or lapses; or an Hours Edit is recorded for them. Draft Assignment changes, including Job deletion, send nothing until publication. Each message names the Job or date, what changed, and links to the details. **Exception to Draft suppression:** FR-51 preference confirmation outcomes are notified immediately and do not expose Draft Assignments (DEC-98) | «C» `NotificationService.notify(event, recipients)` creates one «E» `Notification` per recipient and sends it through «interface» `NotificationChannel` (`EmailChannel` → Email Service, `SmsChannel` → SMS Gateway); `Notification.markSent(channel)` or `markFailed(channel)`. Trigger: FR-04, FR-09, FR-10, FR-38, FR-51, FR-57 | M2-Brief §3.2; INT-MGR [added follow-up: notifications]; DEC-46; DEC-48; DEC-64; DEC-88; DEC-103 | Must | Agreed | One test per trigger, checking Landing Page, email and SMS. A Draft Assignment change/deletion → nothing sent; Published Assigned Job deletion → attributed Staff notified; preference confirmation → outcome only sent once |

### 3.8 Landing Pages and Assignment information

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-40 | The Manager's Landing Page must show the current week by default and allow switching to the Planning Week. It must show: every Driver's and Technician's Workload with a 40 h line and Overtime highlighted; separate lists of the three lowest-Workload Drivers and Technicians, excluding anyone with a Leave Record that week, ties broken by name; today's Crews with zones and Standby Staff; the Unassigned Job count; pending Job Rejection Requests; Jobs made Unassigned by account changes; Certifications expiring within 1 month; and working days in the next month with no Van Availability uploaded. Show Active Hours separately, provisional/confirmed preference status, staffing-shortage alerts and activated-day counts; highlight the eligible call-up recommendation when UC-17 is opened (DEC-96–98). | «C» `DashboardController.loadDashboard(week)` and `lowestThree(drivers, technicians)`. Alerts are «E» `Notification` rows of type DashboardAlert; `DashboardController.markHandled(alert)` calls `Notification.markHandled()`. Trigger: Manager logs in | Brief R2, R6; INT-MGR [System Q1 follow-up: landing page], [added follow-up: lowest three]; DEC-05; DEC-63; DEC-74 | Must | Agreed | Seed every element, the Leave exclusion and a tie. Check each is shown |
| FR-41 | The Staff Landing Page must show: a weekly calendar of their Assignments and Standby days for the current week, switchable to the next Published week, with times, addresses and the status of any Job Rejection Request; their Workload for that week against 40 h; and their Workload for the **calendar month**. Display Active Hours separately from Total Credited Workload and show provisional/confirmed/not-confirmed preference results even before roster publication (DEC-96, DEC-98). | «C» `DashboardController.loadStaffHome(staff, week)` reading `Staff.workload()` and `Staff.monthlyWorkload()`. Trigger: Staff logs in | Brief R7; INT-DRV [Q13]; DEC-04; DEC-16 | Must | Agreed | Seeded totals match. A Draft week is not selectable |
| FR-42 | For each Assignment, Staff must see: customer name and phone, address, unit number, postal code and zone, Brand, model, number of units, Job Type, start time, notes, the day's Van number, and the Crew members' names and contact numbers. Show attributed members for this Job; direct duties are labelled paid transport/no Van (DEC-97). | «E» `Assignment.getDetails()`. Trigger: Staff selects an Assignment on «B» `LandingPage` | INT-DRV [Q1], [Q2]; DEC-37; DEC-85 | Must | Agreed | All fields fit a 360 px-wide screen (NFR-11) |

### 3.9 Accounts, access and records

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-43 | The system must support three roles, each with its own Landing Page: **Staff** (subtypes Driver and Technician), **Manager** and **IT Administrator** | Role in «E» `Account.role`. «C» `AuthController.logIn()` checks credentials, then «B» `LandingPage.show(role)`. Trigger: any user logs in | Brief R2, R7, R11; INT-ITA [Q: Permissions]; DEC-18 | Must | Agreed | Log in as each role and check that the correct Landing Page appears |
| FR-44 | The IT Administrator must create Staff and Manager accounts with name, email, contact number and role. A Technician account must also have a home zone and at least one Certification (FR-22). The system must email the initial login details to the new user, who may then change the password | «C» `AccountController.createAccount(details)` creates the `User` subclass and «E» `Account`, plus «E» `Certification` for a Technician, and sends the email through `NotificationChannel` (`EmailChannel`). If that email fails, `AccountController.resendInitialLogin(account)` resends it without creating a second account. Trigger: IT Administrator submits «B» `AccountAdminPage` | Brief R11; INT-ITA [Q: Account info]; DEC-35; DEC-49; DEC-75; DEC-77 | Must | Agreed | Missing required field → refused. Duplicate email → refused. Technician without home zone → refused. Valid → email sent and login works |
| FR-45 | The IT Administrator must be able to change a user's role, effective from the user's next login. If a Staff member becomes a Manager, their future Crew places, direct-duty participation and Standby duties are removed and the affected Jobs become Unassigned | «E» `Account.setRole(role)`, then «C» `RosterController.removeFromFutureRoster(staff)`. Trigger: IT Administrator, «B» `AccountAdminPage.manageAccess()` | INT-ITA [Q: Role change/leaver]; DEC-17 | Must | Agreed | Change a Driver with a future Crew place into a Manager. On next login they see the Manager page; the Crew loses its Driver and the Manager is warned |
| FR-46 | The IT Administrator must be able to **deactivate** the account of a leaver. The user can no longer log in, their future Crew places and Standby days are removed (those Jobs become Unassigned), and their past attributed Staff, Replacement and activated Standby history are kept until the FR-58 purge | «E» `Account.deactivate()`, then «C» `RosterController.removeFromFutureRoster(staff)`. Trigger: IT Administrator | INT-ITA [Q: Role change/leaver], [Q: Retention]; DEC-34 | Must | Agreed | Deactivate a user. Login fails; the future Job is Unassigned; last month's Assignments are still visible |
| FR-47 | A user must be able to reset a forgotten password through a single-use link sent to their company email. A successful reset must invalidate every outstanding reset token for that Account | «E» `PasswordResetToken.generate(account)` on «C» `AuthController.requestReset(email)`. `AuthController.resetPassword(token, password)` calls `PasswordResetToken.validate()`, `Account.setPassword()` and `PasswordResetToken.invalidateAll(account)`. Trigger: user on «B» `LoginPage` | INT-ITA [Q: Passwords]; DEC-71; M2-Brief §3.2 | Should | Agreed | Valid token → reset works. Expired or already-used token → refused. Two links requested, one used → both unusable |
| FR-48 | An account must lock after **5†** consecutive failed logins within **15 minutes†**. Only the IT Administrator can unlock it | «E» `Account.recordFailedAttempt()` then `Account.lock()`; `Account.unlock()` by IT Administrator via «C» `AccountController.manageAccess()`. Trigger: each failed login | INT-ITA [Q: Passwords]; DEC-17 | Should | Agreed | 4 failures → still usable. 5th → locked. Unlocked → login works |
| FR-49 | The system must log, with who, what, when and a reason where one is required: account, role and Technician profile changes; password reset requests; CSV uploads; Suggested Roster runs; every Manager change to a suggested or published roster, including overridden warnings; Hours Edits and Standby activations; Job creation, edits and deletions; and Job Rejection decisions. Only the IT Administrator can view the Audit Log | «E» `AuditLog.record(actor, action, target, reason)` called by every control class that saves these changes. `AuditLog.search(filter)` via «C» `AccountController.searchAuditLog()` on «B» `AuditLogPage`. Trigger: each change | M2-Brief §3.2; INT-ITA [Q: Audit]; DEC-17; DEC-89 | Must | Agreed | Make each change type → an entry exists with a reason where required. Manager opens the log → refused |
| FR-50 | No user may delete records dated in the past or in progress. Only a future Job may be deleted, on customer cancellation (FR-04). Future Availability entries may be cleared (FR-12) and Standby picks withdrawn before the deadline (FR-51). All other records are removed only by FR-58 | No delete operation on past records. «C» `JobController.deleteJob()` refuses past and started Jobs. Trigger: n/a | INT-ITA [Q: Retention]; DEC-34; DEC-76 | Must | Agreed | Try to delete yesterday's Job → no option. Delete a future Job → allowed |
| FR-58 | Every day at **02:00†** the system must purge records and Audit Log entries dated more than **12 months** ago: Jobs, Assignments, Crews, Replacements, Standby, Availability, Standby Preferences, Leave Records, Van Availability, Hours Edits, Job Rejection Requests, Notifications, CSV Imports and Audit Log entries. Accounts are not purged | «C» `RetentionJob.runDaily()` → `purgeOlderThan(12 months)`. Trigger: the Clock, inside the NFR-03 maintenance window | M2-Brief §3.2; INT-ITA [Q: Retention]; DEC-34; DEC-89 | Must | Agreed | A record dated 12 months + 1 day ago → purged. 11 months → kept. The activation count ignores purged records |

### 3.10 Requirement-to-use-case summary

| Use case | FR |
|---|---|
| UC-01 Log In/out | FR-43, FR-48, NFR-07 |
| UC-02 Reset Password | FR-47 |
| UC-03 Create User Account | FR-44, FR-22 |
| UC-04 Manage User Access | FR-45, FR-46, FR-48, FR-22, FR-49 |
| UC-05 Manage Job | FR-01, FR-02, FR-04, FR-05, FR-34, FR-50 |
| UC-07 Allocate Jobs / Set Weekly Schedule | FR-51, FR-26, FR-27, FR-07, FR-08, FR-32, FR-33, FR-34, FR-09, FR-10, FR-11, FR-30, FR-55 |
| UC-08 Compare Staff | FR-31 |
| UC-09 Decide Job Rejection Request | FR-05, FR-34, FR-38 |
| UC-10 View Manpower Dashboard | FR-14, FR-34, FR-35, FR-36, FR-40 |
| UC-11 Set Availability | FR-12, FR-13, FR-15 |
| UC-12 Submit Job Rejection Request | FR-41, FR-37 |
| UC-13 View My Assignments and Workload | FR-35, FR-36, FR-41, FR-42, NFR-05 |
| UC-15 Notify Staff | FR-09, FR-39 |
| UC-16 Upload CSV | FR-52, FR-53, FR-54 |
| UC-17 Update Roster and Hours | FR-07, FR-08, FR-10, FR-27, FR-30, FR-32, FR-35, FR-56, FR-57 |
| UC-18 Set Standby Preference | FR-15, FR-51 |
| No use case (system event) | FR-58 (Clock) |

### 3.11 Withdrawn functional requirements

These report IDs have **Status: Withdrawn** in v4.0 and are not part of the active baseline. They remain reserved and must not be reused (DEC-72, DEC-92). Draft IDs withdrawn before the M1 report are listed in v3.5 §9 (git history).

| ID | Former scope | Disposition |
|---|---|---|
| FR-03 | Linked Jobs | **Withdrawn v4.0** (DEC-90) |
| FR-06 | Technician marks a Job Completed | **Withdrawn v4.0** (DEC-76) |
| FR-16 | Late Availability Change Request | **Withdrawn v4.0:** handled outside the system (DEC-83) |
| FR-17 | Advisory Job Preference | **Withdrawn v4.0:** replaced by FR-51 Standby Preference (DEC-79) |
| FR-18 | Submit a Leave Request | **Withdrawn v4.0:** Leave comes from the HR CSV, FR-52 (DEC-73, DEC-74) |
| FR-19 | Manager decides a Leave Request | **Withdrawn v4.0** (DEC-73) |
| FR-20 | Approved Leave blocks Assignments | **Withdrawn v4.0:** replaced by Leave Records in FR-32 and FR-52 |
| FR-21 | 7-day Leave balance | **Withdrawn v4.0** (DEC-73, DEC-90) |
| FR-23 | Van number and licence plate list | **Withdrawn v4.0:** replaced by FR-53 Van Availability (DEC-85) |
| FR-24 | Generated Workshop Servicing dates | **Withdrawn v4.0** (DEC-73, DEC-85) |
| FR-25 | Mark a Van unavailable | **Withdrawn v4.0:** replaced by the van CSV, FR-53 (DEC-85) |
| FR-28 | Emergency Crew change during the day | **Withdrawn v4.0:** merged into FR-57 (DEC-81) |
| FR-29 | Crew invalidated by a later event; Needs attention | **Withdrawn v4.0** (DEC-90) |

---

## 4. Non-functional requirements

| ID | Category | Description (with measurable criterion) | Mechanism / where it is met | Source / justification | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|---|
| NFR-01 | Performance | With the NFR-02 load and reference dataset, **95%†** of main user actions (saving Availability, a Standby pick, an Assignment or a Job Rejection Request; loading a Landing Page) must complete within **5 s**, measured at the server. Generating a Suggested Roster for one Planning Week must complete within **10 s†**. A saved change must be visible to other logged-in users within **60 s** | Application layer on the on-site server; `CrewFormingService.suggestRoster()` | INT-ITA [Q: Response time] ("maybe 3 or 5 seconds"; "less than a minute or so"); Brief R2 ("immediately"); DEC-80 | Should | Agreed | Report the 95th percentile per action; time a full-week suggestion on the reference dataset |
| NFR-02 | Capacity | The system must support **50 concurrent sessions**, including one person on up to 3† devices, with a reference dataset of up to 6 Crews per day, 17 Staff, 25 Jobs per working day† (above the brief's "more than 20") and 13 months of records (the 12-month retention plus the 1-month window) | Server sizing and database indexes | INT-ITA [Q: Concurrency]; Brief §Company ¶4–5; DEC-34; DEC-89 | Must | Agreed | Load test at 50 sessions on the reference dataset |
| NFR-03 | Availability | The system must be available 24/7 with **≥ 99%† monthly uptime**, excluding planned maintenance between **00:00 and 05:00†**, never on a Monday or Thursday (the peak days) | On-site server operations; `RetentionJob` runs inside the window | INT-ITA [Q: Hours], [Q: Outage]; DEC-38 | Must | Agreed | Monthly uptime report from monitoring |
| NFR-04 | Recoverability | After a failure, service and data must be restored within **24 h** of detection, with no more than **1 h** of saved data lost. Backups must run at least hourly, and a failed backup must alert the IT Administrator | Hourly database backup on the on-site server | INT-ITA [Q: Outage] ("Not more than one day"), [Q: Restore]; DEC-47 | Must | Agreed | Timed restore drill: service within 24 h and a recovery point no older than 1 h |
| NFR-05 | Reliability / offline | Staff must be able to view their **Published Assignments for today** without a connection, using a per-user read-only browser copy limited to those Assignments. Each successful online load of those Assignments must refresh the encrypted copy without requiring a fresh login. After the app was closed, reopening the copy offline must require the Staff member's password, checked only on the device; no connection or server login is needed. The system must not prompt again while the copy remains unlocked. The copy must be cleared at logout and expire when its date passes. Changes are not accepted offline | «B» `LandingPage.cacheToday(staff, assignments)` refreshes the encrypted copy after a successful online load of today's Published Assignments; `loadCachedToday()` checks Staff/date and locked state; `unlockCachedToday(password)` unlocks locally; `logOut()` calls `clearCachedToday()` | INT-DCT [Questionnaire C18/C19]; INT-ITA [Q: Outage]; DEC-76; DEC-102; DEC-105 | Should | Agreed | After a successful online load, reopen in airplane mode → password prompt; correct password → only that Staff member's today Published Assignments, changes disabled; wrong password → stays locked; revisit while unlocked → no repeated prompt. Another user, logout or a passed date → unavailable |
| NFR-06 | Reliability | A failed submission must be retried automatically up to **3†** times. If it still fails, the user sees a message saying it was not saved and advising them to try again or contact the IT Administrator | Web UI request handling | INT-ITA [Q: Connection failure] | Should | Agreed | Cut the network mid-submit → retries, then the message |
| NFR-07 | Security | Login from a device not used in the last **30 days** must require an email confirmation (2FA), for all roles | `Account.isKnownDevice()`, `rememberDevice()`; Email Service | INT-ITA [Q: Safeguards]; DEC-41 | Should | Agreed | New device → email confirmation required. Same device the next day → not required |
| NFR-08 | Security | Staff personal data and schedule data must be encrypted at rest, including the NFR-05 offline Assignment copy. That copy must be persisted only in encrypted form and must not be readable from the device's stored data without the Staff member's password. Its encryption key must be derived from or protected by that password; no readable decryption key may be persistently stored. Passwords and reset tokens are stored only as salted hashes† | On-site database encryption; `Account.passwordHash`; `PasswordResetToken.tokenHash`; `LandingPage` encrypts the offline copy and unlocks it locally under NFR-05. The algorithm, library and key derivation/protection technique are deferred implementation choices (DEC-105) | INT-ITA [Q: Safeguards] ("encrypted properly in the backend"); DEC-105 | Must | Agreed | Inspect database and browser storage: no readable personal/Assignment fields, plaintext passwords/tokens or readable persisted decryption key. Reopen the copy offline: without the correct password it remains locked; the correct password reveals only the permitted data |
| NFR-09 | Security | Access must be role-based, following the **permission matrix in §4.1** | Each control class checks `Account.role` before acting | INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-18; DEC-37 | Must | Agreed | Test every role × action cell in §4.1. Every ✗ must be refused |
| NFR-10 | Data retention | All records and Audit Log entries must be kept for **12 months** from their date and then purged (FR-58). Deactivated users' records follow the same rule | `RetentionJob` (FR-58) | M2-Brief §3.2; INT-ITA [Q: Retention] ("up to one year"); DEC-34; DEC-89 | Must | Agreed | A record from 11 months ago is retrievable; one from 13 months ago is gone |
| NFR-11 | Compatibility / usability | The system must be a browser-based web application requiring no installation, supporting the latest stable Chrome, Edge, Firefox and DuckDuckGo on Windows, Android and iOS. Staff pages must work at **360 px†** width without horizontal scrolling, and Manager pages at **1366 px†** or wider | Presentation layer | Brief R1; INT-ITA [Q: Devices]; INT-DCT [Questionnaire C18/C19]; INT-DRV [Q14] | Must | Agreed | Run the main flows in each browser; check layouts at 360 px and 1366 px |
| NFR-12 | Usability | In a walkthrough with **3†** non-technical users, each must complete "enter a week's Availability", "pick a Standby day" and "submit a Job Rejection Request" without help, in under **3 minutes†** each | Wireframe prototype | INT-MGR [Closing] ("Just keep it simple. Most of my staff aren't very technical.") | Must | Agreed | Moderated walkthrough on the wireframe prototype |
| NFR-13 | Deployment | The application and its database must run on an **on-site server**. Authoritative records and logs must be stored only there. The bounded per-user read-only browser copy permitted by NFR-05 is the exception for offline viewing; its logout and date-expiry limits apply | On-site application/data hosting (architecture, report §3.1); the presentation-layer offline copy follows NFR-05 | M2-Brief §3.2; DEC-89; DEC-102 | Must | Agreed | Inspect deployment: authoritative database records and logs are on-site. Inspect the browser copy against the NFR-05 scope and lifecycle |
| NFR-14 | Privacy (data minimisation) | The system must store only the personal data that a requirement uses: name, email, contact number, role, home zone, Certifications (Brand and expiry), Availability, and Leave Records (date and type only, with no medical or reason detail). Active Hours, Total Credited Workload and activated-day counts are computed, not stored. Store per-Job Staff attribution, Replacement history and preference decision metadata required by DEC-96–98 | Entity attributes in the final class diagram; derived methods (DEC-87) | M2-Brief writing rules ("don't collect what you don't need"); DEC-75; DEC-87 | Must | Agreed | Review the entity attributes against this list; the HR CSV import ignores any extra columns |

### 4.1 Permission matrix (NFR-09)

✓ = allowed, ✗ = refused, "own" = only for the user's own records, "crew" = only for Jobs on their own Crew.

| Action | Staff (Driver) | Staff (Technician) | Manager | IT Administrator |
|---|---|---|---|---|
| Set Availability | own | own | ✗ | ✗ |
| Pick a Standby day | ✗ | own | ✗ | ✗ |
| View Assignments and Standby days | own, Published weeks only | own, Published weeks only | all | ✗ |
| View Crew-mates' names and contact numbers | crew | crew | all | ✗ |
| View other Staff's Availability, Leave or Workload | ✗ | ✗ | ✓ | ✗ |
| Submit a Job Rejection Request | crew | crew | ✗ | ✗ |
| Upload CSV files | ✗ | ✗ | ✓ | ✗ |
| Create, edit or delete Jobs; generate the Suggested Roster; form Crews; name Standby; allocate; publish | ✗ | ✗ | ✓ | ✗ |
| Record replacements, Standby activations and Hours Edits | ✗ | ✗ | ✓ | ✗ |
| Decide Job Rejection Requests | ✗ | ✗ | ✓ | ✗ |
| Create or deactivate accounts; change roles; unlock accounts; update Technician profiles | ✗ | ✗ | ✗ | ✓ |
| View the Audit Log | ✗ | ✗ | ✗ | ✓ |

Sources: INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-37; DEC-42; DEC-75; DEC-79; DEC-82.

### 4.2 Rationale for team-set thresholds (†)

No stakeholder gave these numbers. The team set them, and each has a one-line justification to meet the rubric's "measurable and justified".

| Row | Threshold | Justification |
|---|---|---|
| FR-55 / A5 | 8 h projected per Crew day | A Crew works a full working day (DEC-12); Jobs are not yet allocated when Crews are suggested |
| FR-56 / DEC-77 | Zone distance 0 / 1 / 2 | Central borders every zone; adjacent outer zones share a border; opposite zones need a cross-island trip |
| NFR-01 | 95th percentile; suggestion in 10 s | Percentile targets ignore rare network outliers. 10 s keeps the Manager's Thursday planning interactive for 6 days × 11 Technicians |
| NFR-02 | Up to 3 devices per person; 25 Jobs per day; 13 months of data | 25 is about 25% headroom over "more than 20 jobs … daily". 13 months = 12-month retention + 1-month window |
| NFR-03 | ≥ 99% monthly uptime; maintenance 00:00–05:00 | About 7 h of downtime a month, within "Not more than one day", outside working hours |
| NFR-06 | 3 automatic retries | Covers brief signal drops in basements without a long wait |
| NFR-08 | Salted hashes | Passwords and reset tokens should never be recoverable |
| NFR-11 | 360 px (Staff) / 1366 px (Manager) | 360 px is a common small Android screen width, and Technicians use their own Android phones. 1366 px is a common laptop width for the office-based Manager |
| NFR-12 | 3 users, under 3 minutes, no help | A feasible walkthrough of the three most frequent Staff tasks |

## 5. Prioritisation (MoSCoW)

| Priority | Rule applied | Count |
|---|---|---|
| **Must** | Required by Brief R1–R11; **or** needed for the weekly cycle to work end-to-end (CSV upload → Availability and picks → Suggested Roster → allocation → publish → updates and hours → Workload); **or** a rule the Manager called "never acceptable" to break (INT-MGR [System Q4]); **or** basic account, data protection and retention | 42 FR, 10 NFR |
| **Should** | Asked for by a stakeholder and clearly valuable, but the weekly cycle still works without it (password reset, lockout, start-time rules, 2FA, offline view, retries, response time) | 3 FR, 4 NFR |
| **Could** | None in the active baseline | 0 FR, 0 NFR |
| **Withdrawn in v4.0** | Out of M2 scope (DEC-73), kept in §3.11 | 13 FR, 0 NFR |

Active baseline: **45 FRs and 14 NFRs**. FR-01 to FR-58 = 45 active + 13 withdrawn in v4.0; NFR-01 to NFR-14 are all active.

**Stakeholder ranking used as a tie-breaker:** the Manager ranked their needs as "Staff workload first, then unassigned jobs, then leave. Van usage is nice to have" (INT-MGR [System Q1 follow-up: ranking]). What mattered most was "Allocating jobs with valid crews, and seeing the workload at a glance" (INT-MGR [Closing]).

## 6. Coverage check: Brief initial requirements

| Brief | Summary (see brief for exact text) | FR / NFR IDs |
|---|---|---|
| R1 | Web-based | NFR-11 |
| R2 | Manager Landing Page shows staff workload | FR-40, NFR-01 |
| R3 | Allocate jobs one week at a time | FR-07, FR-09, FR-55 |
| R4 | Allocation page: up to three staff availability | FR-31 |
| R5 | Availability display: workload, preference, location, week availability | FR-31 (Standby pick as the preference; Crew or home zone as the location) |
| R6 | Three lowest workload; highlight >40 hours | FR-36, FR-40 |
| R7 | Staff Landing Page: weekly assignments and monthly workload | FR-41, FR-42 |
| R8 | Add/edit availability up to **1 month in advance** (the brief's "5 weeks" is superseded, DEC-01) | FR-12, FR-13 |
| R9 | Weekly job preference: met by the guaranteed weekly Standby-day pick (DEC-79) | FR-51 |
| R10 | Reject jobs with warning (a request the Manager decides, DEC-42) | FR-37, FR-38 |
| R11 | IT administrators add staff and managers | FR-44, NFR-09 |

## 7. M2 testing targets

| Rubric item | Target | Why it qualifies |
|---|---|---|
| Black box (decision table) | FR-51: `StandbyPreferenceController.submitPick()` | Five independent conditions (deadline, Available, certified for the Brand, slot free, already picked this week) and two effects (accepted or changed pick; refusal with a reason) |
| White box (CFG ≥ 8 nodes, ≥ 2 decisions) | FR-55: `CrewFormingService.classifyTechnicians()` | A loop over Technicians with four decisions (working that day, Standby pick, dual with 20 h or more, 40 h or more) and a final sort |

Worked tests are in [m2/testing.md](m2/testing.md) (DEC-94).

## 8. Open items affecting this SRS

DEC-25, DEC-28 and DEC-29 (rubric wording) remain Open and DEC-27 is Asked. Authentication/notification details in DEC-61/62 and optional questionnaire requests in DEC-70 remain separate follow-ups. The §1.5 assumptions must appear in the report. The postal-sector lookup table (A6) and cancelled-Leave CSV representation still need specification; this revision does not invent either. DEC-100 and DEC-101 are historical questions resolved by DEC-102 and DEC-103 respectively: a bounded per-user offline copy of today's Published Assignments is permitted, and Draft Job deletion follows notification suppression. Their original entries remain unchanged. DEC-105 adds the approved offline encryption/unlock rule and refresh trigger. Algorithm/library and key derivation/protection details, including lifecycle across existing online sessions and password change/reset, still need specification and verification; DEC-61 remains Open. No offline attempt limit or new session policy is assumed.

## 9. Updates from M1 (for report §1.2)

| Change | IDs |
|---|---|
| **New in v4.0** | FR-51 Standby Preference; FR-52 HR CSV; FR-53 van CSV; FR-54 CSV validation; FR-55 Suggested Roster; FR-56 Standby activation list; FR-57 Update Roster and Hours; FR-58 retention purge; NFR-13 on-site deployment; NFR-14 data minimisation |
| **Changed in v4.0** | FR-01 (zone), FR-04 (delete on cancel), FR-05 (two statuses), FR-07, FR-09 (override logging), FR-10, FR-11, FR-12 (per day), FR-14 (Leave Records, picks), FR-15 (picks lock), FR-22 (no certificate number; IT Administrator updates), FR-26 (Van count, zone), FR-27 (flexible Brands), FR-30, FR-31 (pick, zone, activations), FR-32, FR-33, FR-35 (planned and Standby hours), FR-36, FR-37 (no Short notice), FR-38, FR-39, FR-40, FR-41 (no Leave balance), FR-42 (no plate, no Linked Jobs), FR-44 (home zone), FR-45/46 (future Crew places), FR-47 (token class), FR-49, FR-50; NFR-01, NFR-02, NFR-05, NFR-08, NFR-10, NFR-12 |
| **Withdrawn in v4.0** | FR-03, FR-06, FR-16, FR-17, FR-18, FR-19, FR-20, FR-21, FR-23, FR-24, FR-25, FR-28, FR-29 |
| **Changed in v4.1** | FR-08 (person-level overlap and travel checks across Crew/direct duties; DEC-97). Other v4.1 changes refine the v4.0 rows above; see §10 |
| **Corrected/clarified in v4.1.1** | FR-04/39 (Draft deletion suppression, DEC-103); NFR-05/13 (bounded offline copy, DEC-102); FR-36 wording, FR-05/52–54 design mechanisms and NFR-09 cross-reference (DEC-99/104). Clause labels in FR-04/51/55/57 improve readability without changing their policies |
| **Clarified in v4.1.2** | NFR-05/08: encrypted today-only copy, local password unlock after reopening offline, no repeated prompt while unlocked and successful-online-load refresh (DEC-105) |
| **Unchanged behaviour** | FR-02, FR-34, FR-43, FR-48; NFR-03, NFR-04, NFR-06, NFR-07, NFR-09, NFR-11 |

All IDs are the submitted M1 report's numbers, so this table can go into the report as is.

## 10. v4.1 clarification delta (DEC-96–98)

- Separate Active Hours from Total Credited Hours; keep the 4 h daily Standby minimum after short activation and count distinct activated dates.
- Add direct Standby duties, eligibility before ranking, per-Job Staff attribution and Replacement history; keep paid transport outside the system.
- Confirm provisional preferences after locked inputs/CSV feasibility checks; confirmed initial placement is binding, while activation and Leave remain valid.
- Cover multiple existing Zones with each Crew. Minimum initial Crews precede preference confirmation; publish cannot hide a shortage.
- Existing IDs, Strategy/layered architecture and historical M1 sources are retained. Updated current UCs, diagrams, screens and scenario checks are indexed in traceability.md.


## 11. Requirement quality review (v4.1.2; DEC-104–106)

The requesting member supplied lecture screenshots titled **“What Makes a Requirement Good? (1/2)”** and **“What Makes a Requirement Good? (2/2)”**. The table uses their seven traits and assesses this SRS; no lecturer name, slide date or publication metadata is inferred. Evidence below is a specification/design review, not executed production tests. Labels clarify clauses in FR-04/51/55/57 while preserving their IDs and agreed rules.

| Lecture trait and criterion | Assessment of this SRS |
|---|---|
| **Verifiable:** inspection, analysis or demonstration can check it | FR-08/36 define observable timing and 40 h boundaries; BB-01–07, WB-01–07 and SC-01–15 specify checks. NFR-01/02 require measured load tests and NFR-04 a timed restore. Those production checks have not been run, so verifiability is supported but satisfaction is not claimed. |
| **Clear & Concise:** one requirement, understandable to nontechnical readers, unambiguous | Canonical terms, units and explicit Draft/Published wording reduce ambiguity. Clause labels improve the long FR-04/51/55/57 rows. Those rows, together with FR-32/33/39/40 and NFR-05, bundle related obligations under retained IDs. Single-requirement conformance remains partial. |
| **Traceable:** unique identity/number; cannot be separated or broken into smaller requirements; trace through specification, design and testing | Unique unchanged IDs, source columns and traceability.md link requirements to UCs, classes, components, tests and screens. FR-04/32/33/39/40/51/55/57 and NFR-05 remain divisible into separate obligations, so the lecture's indivisibility criterion is only partly met. “SRS note” or planned tests are trace links, not execution evidence. |
| **Viable:** achievable with existing technology, budget, schedule and skills | The small fixed Staff population, on-site layered design and bounded feasibility search support technical plausibility. A prototype demonstrates screen flows. No verified implementation estimate, deployment budget or team-skills assessment is available; full viability is pending that evidence. |
| **Consistent:** no conflicts/duplication; same terminology | DEC-102/103/105 align the offline-copy scope, encryption/local unlock and Draft-deletion rules; Active/Total Credited Hours and canonical terms align across current artefacts. Some repetition remains (for example FR-09/32 publication constraints and FR-04/50 deletion limits); those cross-references repeat rules rather than define different outcomes. No claim of a contradiction-free implementation is made. |
| **Implementation Free:** developers choose suitable technology | Functional descriptions state behaviour and agreed policy; the separate Mechanism column gives proposed design traceability. CSV, browser, on-site hosting and security constraints are sourced or team-decided (FR-52–54; NFR-05/08/11/13). For NFR-08, INT-ITA [Q: Safeguards] supports the backend-encryption goal; salted hashes† are team-set, and password/key protection of the offline copy comes from DEC-105, a valid team-decision source rather than stakeholder testimony. FR-55 retains the agreed algorithmic policy from M2-Brief §4 / DEC-80, refined by DEC-96/98. These constraints and policies limit developer choice; unrestricted technology choice is not claimed. |
| **Complete:** all necessary information, including limits/units | Deadlines, working hours, durations, 0.5 h travel, 4 h credit, 20/40 h thresholds and the offline-copy lifecycle are explicit. The authoritative postal-sector lookup (A6), cancelled-Leave CSV representation and offline key-lifecycle details remain unspecified in §8. Completeness is therefore partial pending those source decisions. |
