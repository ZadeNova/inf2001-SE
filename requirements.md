# Software Requirements Specification: Aircon Service Workload Management System

> **Version 4.0 (2026-11-07), M2 baseline.** Builds on v3.5, the submitted M1 report baseline (DEC-72), whose IDs it keeps. This revision applies the team's M2 Design Update Brief ([m2/design-update-brief.md](m2/design-update-brief.md)) and the decisions DEC-73 to DEC-95. The system is now scoped to schedule planning (DEC-73). Requirements are written with **"must"**, and every functional requirement names its **mechanism**: the class that holds the data, the method that changes it, who triggers it and when. v3.5 (the M1 report baseline) is in git history.
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
- update the roster and record hours during and after the week, including Standby activations
- see Availability and Workload at a glance up to 1 month in advance
- decide Job Rejection Requests.

It lets **Staff** (Drivers and Technicians):
- enter Availability
- pick one Standby day per week (Technicians only)
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
| **Standby Day Hours** | 4 h, half a working day, credited for a Standby day that is not activated | DEC-78 |
| **Day hours** | A Staff member's hours on one date: the latest Hours Edit if any; else the Planned Hours of their Crew's Jobs; else 4 h if on Standby; else 0 h | DEC-78 |
| **Projected hours** | The estimate the Suggested Roster uses before Jobs are allocated: 8 h† per suggested Crew day, 4 h per Standby day | DEC-80 |
| **Overtime** | Workload strictly above 40 h in a Planning Week | DEC-04, DEC-86 |
| **Zone distance** | 0 for the same zone. 1 if either zone is Central, or for North–East, North–West, South–East and South–West. 2 for North–South and East–West† | DEC-77 |
| **Standby source** | Why a Technician is on Standby: `Preference` (their pick), `Algorithm` (a Dual-Certified Technician with 20 h or more last week, treated as in Central), `Leftover` (not placed in a Crew) or `Manager` (named by hand) | DEC-80, DEC-81 |
| **Full Standby cover** | A working day's Standby Technicians together hold valid Certifications for both Brands | DEC-81 |
| **Draft / Published** | The two states of a Weekly Roster. Staff see Published weeks only | DEC-16 |
| **Job Rejection Request** | A Crew member's request to take a Job off their Crew. The Manager approves or refuses it | DEC-42 |

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
| A3 | An uploaded HR CSV does not add Leave on a day where the person already has a Standby pick or a Crew place. If it does, Leave wins and the Manager fixes the roster with FR-57 | DEC-74 |
| A4 | The Manager uploads both CSV files before planning starts on the Thursday after the Availability Deadline | DEC-74 |
| A5 | Each suggested Crew day counts as a full 8 h working day for ranking, because Jobs are allocated after Crews are suggested | DEC-80 |
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
| Staff enter Availability; Technicians pick a Standby day | Any time within the 1-month window, until the deadline |
| Availability Deadline (the week locks) | Wednesday the 7th, 18:00 |
| Manager uploads the HR and van CSVs, generates the Suggested Roster, sets Crew zones, edits Crews and Standby, then allocates Jobs | From Thursday the 8th (the roster is Draft) |
| Manager publishes | Monday the 12th (Staff are notified) |
| The week runs. The Manager records replacements, Standby activations and hours | Monday the 19th to Saturday the 24th, and afterwards |

Sources: Brief §Company ¶1; INT-MGR [Clarification Q6 follow-up]; DEC-02; DEC-16; DEC-74; DEC-80.

### 2.5 Design principle: the system suggests, the Manager decides

- **Declarations:** Staff set Availability until the Availability Deadline.
- **Guaranteed picks:** a Technician's Standby Preference is accepted only while it has room, and every accepted pick is followed (DEC-79).
- **Suggestions:** the system suggests Crews and Standby Staff and orders Standby Staff for activation. The Manager can change any suggestion, and every change is logged (DEC-80, DEC-89).
- **Requests:** Staff submit Job Rejection Requests and the Manager decides them (DEC-42).

---

## 3. Functional requirements

The **Mechanism** column gives `Class.method()`, the triggering actor or event, and when it happens. «C» marks a control class, «E» an entity and «B» a boundary page, as in the final class diagram ([diagrams/CD-final.puml](diagrams/CD-final.puml)).

### 3.1 Job and Weekly Roster management

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-01 | The Manager must create a Job. **Required:** customer name, customer phone, address, postal code, Brand, Job Type (Installation or Servicing), number of units (≥1), preferred date (a working day) and preferred Slot. **Optional:** unit number, aircon model, notes. The system must derive the Job's **zone** from the postal code (A6) | «C» `JobController.createJob(details)` creates «E» `Job` and calls `Job.deriveZone()` (`Zone.fromPostalCode()`). Trigger: Manager on «B» `JobPage` | INT-MGR [Process Q2]; DEC-11; DEC-77 | Must | Agreed | Required fields only → saved with a zone. Units = 0 → refused. Sunday date → refused. Unknown postal sector → refused |
| FR-02 | The Job's duration must be pre-filled from its Standard Duration (Servicing 1 h per unit, Installation 3 h per unit). The Manager can adjust it | «C» `JobController.standardDuration(jobType, units)`; «E» `Job.durationHours`. Trigger: Job entry | INT-MGR [Process Q2 follow-up: hours]; DEC-22 | Must | Agreed | 2 Installation units → 6 h. Edited to 7 h → saved |
| FR-04 | The Manager must be able to edit a Job, or delete it when the customer cancels. An edited Assigned Job is re-checked against FR-32; if it now breaks a rule it becomes Unassigned and the Manager is told why. Deleting an Assigned Job notifies its Crew first. A Job dated in the past or already started cannot be edited or deleted | «C» `JobController.editJob(job, changes)` → `Job.changeDetails()`, `RuleValidator.checkBlocking()`. `JobController.deleteJob(job)` → «C» `NotificationService.notify(JobDeleted, crew)`, then deletes the Job and its «E» `Assignment`. Trigger: Manager on «B» `JobPage` | M2-Brief §3.2; INT-MGR [added follow-up: cancellations]; DEC-19; DEC-76 | Must | Agreed | Change a Job's Brand to one the Crew can't do → Unassigned with reason. Delete an Assigned Job → Crew notified, Job gone. Yesterday's Job → no edit or delete |
| FR-05 | A Job must be `Unassigned` or `Assigned` only. Unassigned → Assigned on allocation. Assigned → Unassigned on an approved Job Rejection Request, an invalidating edit, an account change (FR-45, FR-46) or the Manager unassigning it. While a Job Rejection Request is pending the Job stays Assigned | «E» `Job.markAssigned()` and `Job.markUnassigned(reason)`, called only by «C» `RosterController`, `JobController`, `RequestController` and `AccountController`. Trigger: those events | M2-Brief §3.2; INT-MGR [Conflicts Q3]; DEC-42; DEC-76 | Must | Agreed | Test each transition. A third status cannot be set |
| FR-07 | The Manager must allocate Jobs **one Planning Week at a time** (the next unpublished week), assigning each Job to a Crew on a date within that week. The page must show each day's Crews with zones and members, the Standby list and the Unassigned Jobs | «C» `RosterController.allocateJob(job, crew, startTime)` creates «E» `Assignment` and calls `Job.markAssigned()`. Trigger: Manager on «B» `JobAllocationPage` | Brief R3; INT-MGR [Process Q1]; DEC-10; DEC-16 | Must | Agreed | Date outside the Planning Week → refused. Allocated Job leaves the Unassigned list |
| FR-08 | The Manager must set each Job's start time on its Crew's day. Jobs run within 09:00–18:00 and skip lunch (13:00–14:00). A Job may span both Slots. Consecutive Jobs on a Crew must be at least the 0.5 h Travel Allowance apart and must not overlap | «E» `Assignment.startTime`, `Assignment.endTime()`; checked by «C» `RuleValidator.checkAssignment()`. Trigger: allocation or a move | INT-DRV [Q5]; INT-MGR [Clarification Q4], [Clarification Q7]; DEC-12; DEC-31 | Should | Agreed | A 3 h Job at 11:00 ends at 15:00. The next Job at 15:10 → refused; 15:30 → accepted |
| FR-09 | A Weekly Roster must stay `Draft` until the Manager publishes it. Staff see Assignments and Standby days only after publication. Publishing is refused while any FR-32 violation exists and allowed with FR-33 warnings outstanding. Every change the Manager makes to a suggested Crew or Standby place must be logged as an override with a reason. On publication every Staff member with an Assignment or a Standby day that week is notified | «E» `WeeklyRoster.publish()` via «C» `RosterController.publish(week)`, which calls `RuleValidator.checkBlocking()` and then «C» `NotificationService.notify(RosterPublished, staff)`. Overrides go to «E» `AuditLog`. Trigger: Manager clicks Publish on «B» `JobAllocationPage` | Brief R3; INT-MGR [Process Q1], [added follow-up: notifications]; DEC-16; DEC-64; DEC-80; DEC-89 | Must | Agreed | A Draft Assignment is hidden from Staff. Publish with a warning → allowed. With an FR-32 violation → refused. Moving a suggested Technician → logged |
| FR-10 | After publication, the Manager must be able to add, move or unassign Jobs and change Crews and Standby for today and future dates. Changes are re-checked against FR-32 and FR-33. Removed and added Staff are notified | «C» `RosterController.allocateJob()`, `moveJob()`, `unassignJob()`, `changeCrew()`, `nameStandby()`, each followed by `NotificationService.notify(RosterChanged, affected)`. Trigger: Manager | INT-MGR [Conflicts Q5]; DEC-16; DEC-88 | Must | Agreed | Add a Job to a published day → Crew notified and Workload updated. Past dates → read-only |
| FR-11 | The system must show a weekly timeline for a selected week, with one row per Crew (Van n) per day showing its zone, members and Jobs, and a row listing that day's Standby Staff | «C» `RosterController.buildTimeline(week)`. Trigger: Manager opens the timeline | INT-MGR [System Q2]; DEC-85 | Must | Agreed | A day with 4 Crews shows 4 rows plus the Standby row |
| FR-55 | For a Draft Planning Week, the system must generate a **Suggested Roster** of Crews and Standby Staff for each working day, in date order, following DEC-80: (1) exclude Technicians with a Leave Record or without Availability; (2) put that day's Standby picks on Standby; (3) put Dual-Certified Technicians with 20 h or more last week on Standby (source Algorithm); (4) rank the rest: projected hours this week under 40 h first, then last week's Workload, then projected hours this week, then staff ID; (5) form Crews from the top, each covering both Brands, up to the day's Van count, stopping after the third Crew if one more would leave no Full Standby cover; (6) if fewer than 3 Crews, return Algorithm and then Leftover Standby Staff to the pool, lowest-ranked first, and form Crews again, never using a Standby pick; (7) put the rest on Standby (source Leftover); (8) assign one Available Driver per Crew in staff-ID order; (9) add projected hours (A5) before the next day. The Manager may generate it again, which replaces the previous suggestion | «C» `CrewFormingService.suggestRoster(week)` → per day `classifyTechnicians(day)`, `formCrews(day, ranked)`, `ensureMinimumCrews(day)`, `assignDrivers(day)`. Ranking through «interface» `TechnicianRanking` (`WorkloadRanking`). Creates Draft «E» `Crew` and «E» `Standby` rows in «E» `WeeklyRoster` and writes «E» `AuditLog`. Trigger: Manager clicks "Suggest roster" on «B» `JobAllocationPage` | Brief R3; M2-Brief §3.5, §4; DEC-80; DEC-81; DEC-82 | Must | Agreed | **White-box target (DEC-94): `classifyTechnicians()`.** Seed 11 Technicians and check each step. A dual with 20 h last week → Standby; 19.5 h → ranked. With 2 Crews formable → a Standby is pulled back, never a pick |

### 3.2 Availability and Standby Preference

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-12 | Staff must set each working day to `Available` or `Unavailable`, and may clear an entry. A day with no entry is **Not submitted** and counts as unavailable. Sundays are not offered | «E» `Availability(staff, date, state)`; «C» `AvailabilityController.save(edits)` → `Availability.setState(state)` / `Availability.clear()`. Trigger: Staff on «B» `AvailabilityPage` | Brief R8; INT-MGR [Clarification Q4]; DEC-03; DEC-83 | Must | Agreed | Set Tuesday Available → saved. Leave Wednesday blank → treated as unavailable by FR-55. No Sunday column |
| FR-13 | Staff must be able to enter or change Availability only for dates from **today through the same calendar date next month, inclusive** (clamped to that month's last day), and only before the Availability Deadline | «C» `AvailabilityController.checkWindowDeadline(dates)` using «C» `RuleValidator.availabilityDeadline(week)`. Trigger: each save | Brief R8 + Lecturer clarification; DEC-01; DEC-02; DEC-30 | Must | Agreed | From 15 Mar: 15 Apr accepted, 16 Apr refused. From 31 Jan: 28 Feb accepted (non-leap year), 1 Mar refused |
| FR-14 | The Manager must view all Staff's Availability up to 1 month in advance as a grid, with Staff down the side and days across. Each cell shows one of: Available; on Leave, Emergency Leave or MC (from the HR CSV); Unavailable or Not submitted. A Technician's Standby pick is marked in its cell | «C» `DashboardController.availabilityGrid(from, to)` reads «E» `Availability`, «E» `LeaveRecord` and «E» `StandbyPreference`. Trigger: Manager opens the grid on «B» `LandingPage` | Brief §Intro ¶4 + Lecturer clarification; INT-MGR [System Q2]; M2-Brief §3.2; DEC-74 | Must | Agreed | Seed each state and check its distinct colour and legend. A Leave Record overrides an Available entry |
| FR-15 | Availability and Standby Preferences for a Planning Week must lock at **18:00 on the Wednesday 12 days before** that week's Monday, in company local time | «C» `RuleValidator.availabilityDeadline(week)` is checked by `AvailabilityController.save()` and `StandbyPreferenceController.submitPick()` at save time. Trigger: each save | Brief §Company ¶1; DEC-02; DEC-79 | Must | Agreed | Week of Mon 19th: a save at Wed 7th 17:59 is accepted; at 18:00 it is refused |
| FR-51 | A Technician must be able to pick **one Standby day per Planning Week**, with a Brand slot (M Electric or Dicon). Each working day has at most one M Electric pick and one Dicon pick, first come first served. The system must accept a pick only when: it is before the Availability Deadline; the Technician is Available that day and has no Leave Record; the Technician holds a valid Certification for the chosen Brand on that day; and that Brand slot is still free. A Dual-Certified Technician may take either free slot. Before the deadline the Technician may change or withdraw the pick, which frees the slot. The page must grey out days with no free slot the Technician could take. Every accepted pick is followed by FR-55 | «E» `StandbyPreference(technician, weekStart, chosenDay, brandSlot)`, unique per technician-week and per day-Brand. «C» `StandbyPreferenceController.submitPick(technician, week, day, brand)` calls «C» `RuleValidator.checkStandbyPick()`, which checks deadline, availability, Certification and slot in that order and reports the first failure, then creates or replaces the record. `withdrawPick()` deletes it. Trigger: Technician on «B» `StandbyPreferencePage` | Brief R9; M2-Brief §1, §3.4; DEC-79 | Must | Agreed | **Black-box decision table (DEC-94):** deadline × available × certified × slot free × already picked. Two Technicians submitting the same slot at once → only the first is saved |

### 3.3 External data (CSV upload)

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-52 | The Manager must be able to upload an **HR CSV** with columns staff ID, date and type (`Leave`, `Emergency Leave` or `MC`). Each valid row creates a read-only Leave Record. A Leave Record makes that person unavailable that day, overriding their Availability and any Standby pick | «C» `CsvImportController.upload(file, HRLeave)` creates «E» `CsvImport`, which calls `parse()` and `validate()` through «interface» `CsvRowMapper` (`HrLeaveCsvMapper`). `commit()` replaces «E» `LeaveRecord`s for the dates in the file and writes «E» `AuditLog`. Trigger: Manager on «B» `CsvUploadPage`, before planning (A4) | M2-Brief §2, §3.2; DEC-74 | Must | Agreed | Upload 3 valid rows → 3 Leave Records; the grid shows Leave. Upload a later file for the same dates → old records replaced |
| FR-53 | The Manager must be able to upload a **van CSV** with columns date and vans available (a whole number, 0 or more). Each valid row creates or replaces that date's Van Availability, which caps the number of Crews that day (FR-32) | As FR-52, with `CsvImportController.upload(file, VanAvailability)` and `VanAvailabilityCsvMapper` creating «E» `VanAvailability(date, vansAvailable)`. Trigger: Manager on «B» `CsvUploadPage` | M2-Brief §2, §3.1; DEC-74; DEC-85 | Must | Agreed | Upload "Mon 19th, 5" → 5 Crews allowed; a 6th → blocked |
| FR-54 | The system must validate a whole CSV file before saving any row. A missing column, an unknown staff ID, an invalid or Sunday date, an unknown type, a negative Van count or an empty file must reject the whole file, list every row error, and save nothing. Exact duplicate rows are saved once. Each upload is recorded with who, when, file type and outcome | «E» `CsvImport.validate()` collects `errors`; `status` becomes `Rejected` or `Committed`. Trigger: each upload | M2-Brief §6.3, §7; DEC-74 | Must | Agreed | Wrong columns → rejected, 0 rows saved. Empty file → rejected. Duplicate row → 1 record. Mixed valid and invalid rows → rejected with the invalid rows listed |

### 3.4 Certifications and Crews

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-22 | The system must record each Technician's **home zone** and **Certifications**. A Certification is Brand and expiry date only; a Technician holds one or both Brands. The IT Administrator enters them at account creation and updates them later. A Certification is **valid on a date** when its expiry date is on or after that date | «E» `Technician.homeZone`; «E» `Certification(brand, expiryDate)` with `Certification.isValidOn(date)`. Updates by «C» `AccountController.updateTechnicianProfile(technician, homeZone, certifications)` → `Technician.setHomeZone()`, `Certification.renew(expiryDate)`. Trigger: IT Administrator | Brief §Company ¶2, ¶4; INT-MGR [Clarification Q5]; DEC-35; DEC-75; DEC-77 | Must | Agreed | Expiry equal to the Job date → valid. Expiry the day before → invalid (FR-32 blocks it) |
| FR-26 | Each Crew must be **exactly one Driver and one or two Technicians** on one Van for one whole working day. Only Drivers may fill the Driver place. A person may be in only one Crew per day and not also on Standby that day. Every member must be Available with no Leave Record that day. Crews are numbered Van 1…n for the day, and n must not exceed that day's Van Availability. The Manager must set each Crew's zone | «E» `Crew(date, vanNumber, zone)` linked to «E» `Driver` and «E» `Technician`. «C» `RosterController.changeCrew(crew, members)` and `setCrewZone(crew, zone)`, checked by «C» `RuleValidator.checkCrew(proposal)`. Trigger: Manager edits a Crew on «B» `JobAllocationPage`, or FR-55 | Brief §Company ¶3–4; DEC-09; DEC-84; DEC-85; M2-Brief §3.2 | Must | Agreed | 0 or 2 Drivers → refused. 0 or 3 Technicians → refused. A Technician with a Leave Record that day → refused. A 6th Crew when Van Availability is 5 → refused |
| FR-27 | Together, a Crew's Technicians must hold **valid Certifications (FR-22) for the Brand of every Job** assigned to the Crew. A single-Brand Crew is allowed when all its Jobs are that Brand | «E» `Crew.coversBrands(brands, date)` uses `Certification.isValidOn(date)`. Checked by «C» `RuleValidator.checkAssignment()` and `checkCrew()`. Trigger: allocation, Crew change, Job edit, publish | Brief §Company ¶2–3; DEC-09; DEC-84 | Must | Agreed | Dicon Job on a Crew with an M Electric-only Technician → blocked. All-M-Electric Jobs on that Crew → allowed |
| FR-30 | A **Standby** is a Technician not in any Crew on a working day. The Manager must be able to add or remove Standby Staff (source Manager) for any Draft or future date. A working day without Full Standby cover must raise a warning (FR-33), not a block. There is no maximum. Placing a Standby into a Crew removes them from Standby that day. An unused Standby day counts as 4 h (FR-35) | «E» `Standby(technician, date, source, activated)`. «C» `RosterController.nameStandby()` and `removeStandby()`; «C» `RuleValidator.checkStandbyCover(day)`. Trigger: Manager on «B» `JobAllocationPage`, or FR-55 | M2-Brief §3.5; DEC-81 | Must | Agreed | A day with only M Electric Standby → warning. Name someone already in a Crew that day → blocked |

### 3.5 Job Allocation and Workload

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-31 | On the Job Allocation page, the Manager must be able to select **up to three** Staff and compare them side by side for a date and its Planning Week. For each person show: Availability that day and week; Workload this week and last week; Certifications with expiry; their Standby pick for the week; their location that day (their Crew's zone, or their home zone if not in a Crew); and their Standby activation count | «C» `RosterController.compare(selection, date)` reads `Staff.availabilityOn()`, `Staff.workload(week)`, `Technician.certifications()`, «E» `StandbyPreference`, `Technician.locationOn(date)` and `Technician.activationCount(date)`. Trigger: Manager selects Staff on «B» `JobAllocationPage` (UC-08) | Brief R4, R5; DEC-06; DEC-77; DEC-79 | Must | Agreed | A 4th selection → refused. All six items are shown for each person |
| FR-32 | The system must **block** any allocation, Crew or Standby change, Job edit or publication that would cause: a Crew lacking a valid Certification for a Job's Brand (FR-27); a double booking (a person in two Crews on one day, in a Crew and on Standby on one day, or overlapping Jobs on a Crew); a Crew member Unavailable, Not submitted or with a Leave Record that day; an invalid Crew (FR-26); more Crews on a day than its Van Availability; or a Sunday | «C» `RuleValidator.checkBlocking(proposal)` called by `RosterController`, `JobController` and `HoursController` before saving. Trigger: every such change | INT-MGR [System Q4]; DEC-19; DEC-75; DEC-85 | Must | Agreed | One negative test per rule |
| FR-33 | The system must **warn**, allow an override with a reason and log it, when a change or a publication would cause: a Staff member's Workload above 40 h in the Planning Week; a Job's zone different from its Crew's zone; a Job starting outside the customer's preferred Slot; fewer than 3 Crews on a working day; a working day without Full Standby cover; a Standby pick placed into a Crew; or a working day with no Van Availability uploaded. Overtime has no approval step | «C» `RuleValidator.checkWarnings(context)`; «C» `RosterController.confirmWarnings(choice, reason)` → «E» `AuditLog.record(actor, action, target, reason)`. Trigger: each change and publication | Brief §Company ¶4, R6; INT-MGR [System Q4]; DEC-19; DEC-32; DEC-77; DEC-79; DEC-81 | Must | Agreed | Trigger each warning, override with a reason and find the Audit Log entry. Override without a reason → refused |
| FR-34 | The system must list the Jobs with status **Unassigned** and show their count | «C» `JobController.listUnassigned()`. Trigger: Manager opens «B» `JobAllocationPage` or «B» `LandingPage` | INT-MGR [Conflicts Q1] | Must | Agreed | Approve a Job Rejection Request → count +1. Delete an Unassigned Job → count −1 |
| FR-35 | A Staff member's hours for a date must be: the latest Hours Edit for that date, if any; otherwise, if in a Crew, the Planned Hours (duration + 0.5 h Travel Allowance) of every Job assigned to that Crew that day; otherwise 4 h if on Standby and not activated; otherwise 0 h. Leave counts 0 h. Workload is the sum over a Planning Week or a calendar month | «E» `Staff.hoursOn(date)`, `Staff.workload(week)`, `Staff.monthlyWorkload(month)`, computed on demand from «E» `HoursEdit`, «E» `Assignment` (`Job.plannedHours()`) and «E» `Standby` (DEC-87). Trigger: any page that shows Workload | M2-Brief §1, §3.3; INT-MGR [Clarification Q7]; DEC-31; DEC-39; DEC-78 | Must | Agreed | A Crew with a 1 h Job → each member 1.5 h. An unused Standby day → 4 h. An activated Standby with a 6 h Hours Edit → 6 h |
| FR-36 | Workload is summed per Planning Week (Monday–Saturday). Workload **strictly above 40 h** is Overtime and must be highlighted wherever Workload is shown. Standby Day Hours count | «E» `Staff.isOvertime(week)` = `workload(week) > 40`. Trigger: Workload display | Brief R6; INT-MGR [Clarification Q7]; DEC-04; DEC-86 | Must | Agreed | **Boundary:** 40.0 h → not highlighted; 40.5 h → highlighted |

### 3.6 Roster updates and hours

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-56 | When a Crew member drops out, the Manager must be able to see the day's Standby Staff who are not yet activated, ordered by: (1) fewest activations in the last 12 months; (2) zone distance from the Standby's zone (Central for source Algorithm, otherwise their home zone) to the affected Job's zone; (3) staff ID. Each entry shows activation count, zone, distance and Brands | «C» `StandbyActivationService.listStandbysForJob(job, date)` through «interface» `TechnicianRanking` (`ActivationRanking`), reading «E» `Standby.effectiveZone()` and `Technician.activationCount(date)`. Trigger: Manager opens «B» `StandbyListView` from «B» `UpdateRosterPage` | M2-Brief §3.5, §4 step 12; DEC-77; DEC-81 | Must | Agreed | Two Standby Staff with 0 and 2 activations → the 0 is first. Equal counts → the nearer zone first. A Central-based dual for a North Job → distance 1 |
| FR-57 | After phoning a Standby outside the system, or to correct hours, the Manager must be able to record: a **replacement** (who replaces whom on which Crew, from which Job); a **Standby activation**, which moves the Standby into that Crew, ends their Standby place and adds one to their activation count; and an **Hours Edit** for any Staff member and date in the last 12 months (0–24 h, reason required), which replaces that day's computed hours. Each record is logged and the affected Staff are notified | «C» `HoursController.recordReplacement(crew, outStaff, inStandby, fromJob, reason)` → «E» `Standby.activate()`, `Crew.changeMembers()`, then `HoursController.editHours(staff, date, newHours, reason)` → «E» `HoursEdit(staff, date, oldHours, newHours, reason, editedBy)`, «E» `AuditLog.record()`, «C» `NotificationService.notify(HoursEdited / RosterChanged)`. Trigger: Manager on «B» `UpdateRosterPage` | M2-Brief §3.2, §3.3, §4 step 13; DEC-78; DEC-81; DEC-89 | Must | Agreed | Activate a Standby and enter 5 h → their day is 5 h, not 4 + 5. Activation count +1. Hours Edit without a reason → refused. 25 h → refused |

### 3.7 Job Rejection Requests and notifications

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-37 | A Crew member must be able to submit a **Job Rejection Request** for a Job assigned to their Crew in a Published week before the Job starts. Before submitting, the system must warn them to discuss it with the Manager first. They must pick a reason: Personal emergency; Missing equipment or parts; or Other, which needs a comment. Only one request may be pending per Assignment. The Manager is notified. Telling the company ahead of time that a Job can't be done uses this same function | «C» `RequestController.submitRejection(staff, assignment, reason, comment)` creates «E» `JobRejectionRequest` (status Pending) and calls «C» `NotificationService.notify(RejectionSubmitted, manager)`. Trigger: Crew member on «B» `RequestPage`, after confirming the warning dialog | Brief R10, §Intro ¶3; INT-MGR [Conflicts Q3]; INT-DRV [Q17]; DEC-42; DEC-66 | Must | Agreed | Cancel at the warning → nothing saved. "Other" with no comment → refused. A second request on the same Assignment → refused |
| FR-38 | The Manager must approve or refuse each Job Rejection Request. While pending, the Job stays Assigned. **Approved:** the Job becomes Unassigned and leaves the Crew, and the Crew is notified. **Refused:** the Assignment stands and the requester is notified with any reason. A request still pending when the Job starts lapses and the requester is notified | «E» `JobRejectionRequest.approve()`, `refuse(reason)` and `lapse()` via «C» `RequestController.decideJobRejection(request, decision, reason)`; `RequestController.onJobStart(assignment)` is triggered by the Clock at the Job's start time. Trigger: Manager on «B» `RequestReviewPage`, or the start time | Brief R10; DEC-42 | Must | Agreed | Approve → the Job is Unassigned. Refuse → unchanged. Pending at the start time → Lapsed |
| FR-39 | Staff must be notified **on their Landing Page, by email and by SMS** when: a week with their Assignments or Standby days is published; after publication, one of their Assignments, Crew places or Standby days is added, changed or removed; one of their Jobs is deleted; their Job Rejection Request is decided or lapses; or an Hours Edit is recorded for them. Changes to a Draft week send nothing until publication. Each message names the Job or date, what changed, and links to the details | «C» `NotificationService.notify(event, recipients)` creates one «E» `Notification` per recipient and sends it through «interface» `NotificationChannel` (`EmailChannel` → Email Service, `SmsChannel` → SMS Gateway); `Notification.markSent(channel)` or `markFailed(channel)`. Trigger: FR-04, FR-09, FR-10, FR-38, FR-57 | M2-Brief §3.2; INT-MGR [added follow-up: notifications]; DEC-46; DEC-48; DEC-64; DEC-88 | Must | Agreed | One test per trigger, checking Landing Page, email and SMS. A Draft change → nothing sent |

### 3.8 Landing Pages and Assignment information

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-40 | The Manager's Landing Page must show the current week by default and allow switching to the Planning Week. It must show: every Driver's and Technician's Workload with a 40 h line and Overtime highlighted; separate lists of the three lowest-Workload Drivers and Technicians, excluding anyone with a Leave Record that week, ties broken by name; today's Crews with zones and Standby Staff; the Unassigned Job count; pending Job Rejection Requests; Jobs made Unassigned by account changes; Certifications expiring within 1 month; and working days in the next month with no Van Availability uploaded | «C» `DashboardController.loadDashboard(week)` and `lowestThree(drivers, technicians)`. Alerts are «E» `Notification` rows of type DashboardAlert; `DashboardController.markHandled(alert)` calls `Notification.markHandled()`. Trigger: Manager logs in | Brief R2, R6; INT-MGR [System Q1 follow-up: landing page], [added follow-up: lowest three]; DEC-05; DEC-63; DEC-74 | Must | Agreed | Seed every element, the Leave exclusion and a tie. Check each is shown |
| FR-41 | The Staff Landing Page must show: a weekly calendar of their Assignments and Standby days for the current week, switchable to the next Published week, with times, addresses and the status of any Job Rejection Request; their Workload for that week against 40 h; and their Workload for the **calendar month** | «C» `DashboardController.loadStaffHome(staff, week)` reading `Staff.workload()` and `Staff.monthlyWorkload()`. Trigger: Staff logs in | Brief R7; INT-DRV [Q13]; DEC-04; DEC-16 | Must | Agreed | Seeded totals match. A Draft week is not selectable |
| FR-42 | For each Assignment, Staff must see: customer name and phone, address, unit number, postal code and zone, Brand, model, number of units, Job Type, start time, notes, the day's Van number, and the Crew members' names and contact numbers | «E» `Assignment.getDetails()`. Trigger: Staff selects an Assignment on «B» `LandingPage` | INT-DRV [Q1], [Q2]; DEC-37; DEC-85 | Must | Agreed | All fields fit a 360 px-wide screen (NFR-11) |

### 3.9 Accounts, access and records

| ID | Description | Mechanism (owner · method · trigger) | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| FR-43 | The system must support three roles, each with its own Landing Page: **Staff** (subtypes Driver and Technician), **Manager** and **IT Administrator** | Role in «E» `Account.role`. «C» `AuthController.logIn()` checks credentials, then «B» `LandingPage.show(role)`. Trigger: any user logs in | Brief R2, R7, R11; INT-ITA [Q: Permissions]; DEC-18 | Must | Agreed | Log in as each role and check that the correct Landing Page appears |
| FR-44 | The IT Administrator must create Staff and Manager accounts with name, email, contact number and role. A Technician account must also have a home zone and at least one Certification (FR-22). The system must email the initial login details to the new user, who may then change the password | «C» `AccountController.createAccount(details)` creates the `User` subclass and «E» `Account`, plus «E» `Certification` for a Technician, and sends the email through `NotificationChannel` (`EmailChannel`). If that email fails, `AccountController.resendInitialLogin(account)` resends it without creating a second account. Trigger: IT Administrator submits «B» `AccountAdminPage` | Brief R11; INT-ITA [Q: Account info]; DEC-35; DEC-49; DEC-75; DEC-77 | Must | Agreed | Missing required field → refused. Duplicate email → refused. Technician without home zone → refused. Valid → email sent and login works |
| FR-45 | The IT Administrator must be able to change a user's role, effective from the user's next login. If a Staff member becomes a Manager, their future Crew places and Standby days are removed and the affected Jobs become Unassigned | «E» `Account.setRole(role)`, then «C» `RosterController.removeFromFutureRoster(staff)`. Trigger: IT Administrator, «B» `AccountAdminPage.manageAccess()` | INT-ITA [Q: Role change/leaver]; DEC-17 | Must | Agreed | Change a Driver with a future Crew place into a Manager. On next login they see the Manager page; the Crew loses its Driver and the Manager is warned |
| FR-46 | The IT Administrator must be able to **deactivate** the account of a leaver. The user can no longer log in, their future Crew places and Standby days are removed (those Jobs become Unassigned), and their past records are kept until the FR-58 purge | «E» `Account.deactivate()`, then «C» `RosterController.removeFromFutureRoster(staff)`. Trigger: IT Administrator | INT-ITA [Q: Role change/leaver], [Q: Retention]; DEC-34 | Must | Agreed | Deactivate a user. Login fails; the future Job is Unassigned; last month's Assignments are still visible |
| FR-47 | A user must be able to reset a forgotten password through a single-use link sent to their company email. A successful reset must invalidate every outstanding reset token for that Account | «E» `PasswordResetToken.generate(account)` on «C» `AuthController.requestReset(email)`. `AuthController.resetPassword(token, password)` calls `PasswordResetToken.validate()`, `Account.setPassword()` and `PasswordResetToken.invalidateAll(account)`. Trigger: user on «B» `LoginPage` | INT-ITA [Q: Passwords]; DEC-71; M2-Brief §3.2 | Should | Agreed | Valid token → reset works. Expired or already-used token → refused. Two links requested, one used → both unusable |
| FR-48 | An account must lock after **5†** consecutive failed logins within **15 minutes†**. Only the IT Administrator can unlock it | «E» `Account.recordFailedAttempt()` then `Account.lock()`; `Account.unlock()` by IT Administrator via «C» `AccountController.manageAccess()`. Trigger: each failed login | INT-ITA [Q: Passwords]; DEC-17 | Should | Agreed | 4 failures → still usable. 5th → locked. Unlocked → login works |
| FR-49 | The system must log, with who, what, when and a reason where one is required: account, role and Technician profile changes; password reset requests; CSV uploads; Suggested Roster runs; every Manager change to a suggested or published roster, including overridden warnings; Hours Edits and Standby activations; Job creation, edits and deletions; and Job Rejection decisions. Only the IT Administrator can view the Audit Log | «E» `AuditLog.record(actor, action, target, reason)` called by every control class that saves these changes. `AuditLog.search(filter)` via «C» `AccountController.searchAuditLog()` on «B» `AuditLogPage`. Trigger: each change | M2-Brief §3.2; INT-ITA [Q: Audit]; DEC-17; DEC-89 | Must | Agreed | Make each change type → an entry exists with a reason where required. Manager opens the log → refused |
| FR-50 | No user may delete records dated in the past or in progress. Only a future Job may be deleted, on customer cancellation (FR-04). Future Availability entries may be cleared (FR-12) and Standby picks withdrawn before the deadline (FR-51). All other records are removed only by FR-58 | No delete operation on past records. «C» `JobController.deleteJob()` refuses past and started Jobs. Trigger: n/a | INT-ITA [Q: Retention]; DEC-34; DEC-76 | Must | Agreed | Try to delete yesterday's Job → no option. Delete a future Job → allowed |
| FR-58 | Every day at **02:00†** the system must purge records and Audit Log entries dated more than **12 months** ago: Jobs, Assignments, Crews, Standby, Availability, Standby Preferences, Leave Records, Van Availability, Hours Edits, Job Rejection Requests, Notifications, CSV Imports and Audit Log entries. Accounts are not purged | «C» `RetentionJob.runDaily()` → `purgeOlderThan(12 months)`. Trigger: the Clock, inside the NFR-03 maintenance window | M2-Brief §3.2; INT-ITA [Q: Retention]; DEC-34; DEC-89 | Must | Agreed | A record dated 12 months + 1 day ago → purged. 11 months → kept. The activation count ignores purged records |

### 3.10 Requirement-to-use-case summary

| Use case | FR |
|---|---|
| UC-01 Log In/out | FR-43, FR-48, NFR-07 |
| UC-02 Reset Password | FR-47 |
| UC-03 Create User Account | FR-44, FR-22 |
| UC-04 Manage User Access | FR-45, FR-46, FR-48, FR-22, FR-49 |
| UC-05 Manage Job | FR-01, FR-02, FR-04, FR-05, FR-34, FR-50 |
| UC-07 Allocate Jobs / Set Weekly Schedule | FR-26, FR-27, FR-07, FR-08, FR-32, FR-33, FR-34, FR-09, FR-10, FR-11, FR-30, FR-55 |
| UC-08 Compare Staff | FR-31 |
| UC-09 Decide Job Rejection Request | FR-05, FR-34, FR-38 |
| UC-10 View Manpower Dashboard | FR-14, FR-34, FR-35, FR-36, FR-40 |
| UC-11 Set Availability | FR-12, FR-13, FR-15 |
| UC-12 Submit Job Rejection Request | FR-41, FR-37 |
| UC-13 View My Assignments and Workload | FR-35, FR-36, FR-41, FR-42, NFR-05 |
| UC-15 Notify Staff | FR-09, FR-39 |
| UC-16 Upload CSV | FR-52, FR-53, FR-54 |
| UC-17 Update Roster and Hours | FR-10, FR-35, FR-56, FR-57 |
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
| NFR-05 | Reliability / offline | Staff must be able to view **today's** published Assignments without a connection. Changes are not accepted offline | Cached copy on «B» `LandingPage.loadCachedToday()` | INT-DCT [Questionnaire C18/C19]; INT-ITA [Q: Outage]; DEC-76 | Should | Agreed | In airplane mode, today's Jobs are viewable and submit buttons are disabled |
| NFR-06 | Reliability | A failed submission must be retried automatically up to **3†** times. If it still fails, the user sees a message saying it was not saved and advising them to try again or contact the IT Administrator | Web UI request handling | INT-ITA [Q: Connection failure] | Should | Agreed | Cut the network mid-submit → retries, then the message |
| NFR-07 | Security | Login from a device not used in the last **30 days** must require an email confirmation (2FA), for all roles | `Account.isKnownDevice()`, `rememberDevice()`; Email Service | INT-ITA [Q: Safeguards]; DEC-41 | Should | Agreed | New device → email confirmation required. Same device the next day → not required |
| NFR-08 | Security | Staff personal data and schedule data must be encrypted at rest. Passwords and reset tokens are stored only as salted hashes† | On-site database encryption; `Account.passwordHash`; `PasswordResetToken.tokenHash` | INT-ITA [Q: Safeguards] ("encrypted properly in the backend") | Must | Agreed | Inspect the database: no readable personal fields, plaintext passwords or tokens |
| NFR-09 | Security | Access must be role-based, following the **permission matrix in §4.2** | Each control class checks `Account.role` before acting | INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-18; DEC-37 | Must | Agreed | Test every role × action cell in §4.2. Every ✗ must be refused |
| NFR-10 | Data retention | All records and Audit Log entries must be kept for **12 months** from their date and then purged (FR-58). Deactivated users' records follow the same rule | `RetentionJob` (FR-58) | M2-Brief §3.2; INT-ITA [Q: Retention] ("up to one year"); DEC-34; DEC-89 | Must | Agreed | A record from 11 months ago is retrievable; one from 13 months ago is gone |
| NFR-11 | Compatibility / usability | The system must be a browser-based web application requiring no installation, supporting the latest stable Chrome, Edge, Firefox and DuckDuckGo on Windows, Android and iOS. Staff pages must work at **360 px†** width without horizontal scrolling, and Manager pages at **1366 px†** or wider | Presentation layer | Brief R1; INT-ITA [Q: Devices]; INT-DCT [Questionnaire C18/C19]; INT-DRV [Q14] | Must | Agreed | Run the main flows in each browser; check layouts at 360 px and 1366 px |
| NFR-12 | Usability | In a walkthrough with **3†** non-technical users, each must complete "enter a week's Availability", "pick a Standby day" and "submit a Job Rejection Request" without help, in under **3 minutes†** each | Wireframe prototype | INT-MGR [Closing] ("Just keep it simple. Most of my staff aren't very technical.") | Must | Agreed | Moderated walkthrough on the wireframe prototype |
| NFR-13 | Deployment | The application and its database must run on an **on-site server**. Records and logs are stored only there | Data layer (architecture, report §3.1) | M2-Brief §3.2; DEC-89 | Must | Agreed | Deployment check: no record store outside the on-site server |
| NFR-14 | Privacy (data minimisation) | The system must store only the personal data that a requirement uses: name, email, contact number, role, home zone, Certifications (Brand and expiry), Availability, and Leave Records (date and type only, with no medical or reason detail). Workload, activation counts and "based in Central" are computed, not stored | Entity attributes in the final class diagram; derived methods (DEC-87) | M2-Brief writing rules ("don't collect what you don't need"); DEC-75; DEC-87 | Must | Agreed | Review the entity attributes against this list; the HR CSV import ignores any extra columns |

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

DEC-25, DEC-28 and DEC-29 (rubric wording) remain Open and DEC-27 is Asked. None blocks this baseline. The §1.5 assumptions must appear in the report.

## 9. Updates from M1 (for report §1.2)

| Change | IDs |
|---|---|
| **New in v4.0** | FR-51 Standby Preference; FR-52 HR CSV; FR-53 van CSV; FR-54 CSV validation; FR-55 Suggested Roster; FR-56 Standby activation list; FR-57 Update Roster and Hours; FR-58 retention purge; NFR-13 on-site deployment; NFR-14 data minimisation |
| **Changed in v4.0** | FR-01 (zone), FR-04 (delete on cancel), FR-05 (two statuses), FR-07, FR-09 (override logging), FR-10, FR-11, FR-12 (per day), FR-14 (Leave Records, picks), FR-15 (picks lock), FR-22 (no certificate number; IT Administrator updates), FR-26 (Van count, zone), FR-27 (flexible Brands), FR-30, FR-31 (pick, zone, activations), FR-32, FR-33, FR-35 (planned and Standby hours), FR-36, FR-37 (no Short notice), FR-38, FR-39, FR-40, FR-41 (no Leave balance), FR-42 (no plate, no Linked Jobs), FR-44 (home zone), FR-45/46 (future Crew places), FR-47 (token class), FR-49, FR-50; NFR-01, NFR-02, NFR-05, NFR-08, NFR-10, NFR-12 |
| **Withdrawn in v4.0** | FR-03, FR-06, FR-16, FR-17, FR-18, FR-19, FR-20, FR-21, FR-23, FR-24, FR-25, FR-28, FR-29 |
| **Unchanged** | FR-02, FR-08, FR-34, FR-43, FR-48; NFR-03, NFR-04, NFR-06, NFR-07, NFR-09, NFR-11 |

All IDs are the submitted M1 report's numbers, so this table can go into the report as is.
