# Software Requirements Specification: Aircon Service Workload Management System

> **Version 2 (2026-09-30).** This is an AI-assisted draft (Claude Code), built from the brief, the lecturer's clarification, the four interview transcripts and the team decisions in [decisions.md](decisions.md). v2 applies the resolutions of DEC-02 to DEC-41 and the fixes from [requirements-review.md](requirements-review.md). See [ai-usage-log.md](ai-usage-log.md).
> Every row cites its source. Where the interviews were silent, the row cites the DEC entry that records the team's choice.
> All rows are `Draft` until the team reviews them and marks them `Agreed`. IDs are stable: FR-68 is withdrawn, and FR-69 and FR-70 are new in v2.
> Priorities use MoSCoW. Brief R1–R11 are the minimum deliverable, so they are always `Must`.
> **†** marks a numeric threshold chosen by the team rather than stated by a stakeholder.

---

## 1. Introduction

### 1.1 Purpose

This SRS specifies the functional and non-functional requirements of a web-based workload management system for the aircon service team of an aircon retailer. It is the baseline for the Milestone 1 use cases, class diagram, activity diagrams and sequence diagrams.

### 1.2 Scope

The system lets the **Manager**:
- record Jobs
- form a daily Crew for each Van, allocate Jobs one Planning Week at a time and publish the Weekly Roster
- see Availability and Workload at a glance up to 1 month in advance
- handle Leave Requests, Late Availability Change Requests and Job Rejections.

It lets **Staff** (Drivers and Technicians):
- enter Availability, Job Preferences and Leave Requests
- see their published Assignments and Workload
- record Job completion (Technicians)
- reject Jobs.

It lets the **IT Administrator** manage accounts, roles, the public holiday list and the audit log.

**Out of scope**, with the source for each exclusion:

| Excluded | Source |
|---|---|
| Wages, job costs and payroll | INT-MGR [System Q1] |
| Live GPS tracking | INT-MGR [System Q3]; DEC-08 |
| Customer self-booking | INT-MGR [Process Q2] |
| Sunday and public holiday emergency jobs | INT-MGR [Clarification Q8] |
| Route optimisation. Job order is set by the Manager | INT-DRV [Q5] |
| In-app delay reporting. Delays are reported by phone | DEC-33 |
| Overtime approval workflow | DEC-32 |
| Importing existing schedules | DEC-36 |
| Real-time phone calls. The system only records the resulting change | INT-MGR [added follow-up: notifications] |

### 1.3 Definitions

The canonical terms are in the [AGENTS.md glossary](AGENTS.md#glossary-canonical-terms). This SRS also uses these terms:

| Term | Meaning | Source |
|---|---|---|
| **Crew** | The Driver and one or two Technicians assigned to one Van for one working day | DEC-09 |
| **Planning Week** | A Monday–Saturday week. "The Planning Week" is the next week not yet published | DEC-04, DEC-16 |
| **Slot** | A half-day unit: `Morning` (09:00–13:00) or `Afternoon` (14:00–18:00). Lunch is 13:00–14:00 | DEC-03, DEC-12 |
| **Availability Lock** | 18:00 on the Wednesday 12 days before a Planning Week's Monday | DEC-02 |
| **Late Availability Change Request** | A Staff request to set or change Availability for a locked week | DEC-02 |
| **Leave Request** | A request for full days of annual Leave, which the Manager approves or rejects | DEC-13 |
| **Standard Duration** | Servicing 1 h per unit, Installation 3 h per unit | DEC-22 |
| **Travel Allowance** | A fixed 0.5 h added to each Job's hours | DEC-31 |
| **Planned Hours / Actual Hours** | Planned Hours = duration + Travel Allowance. Actual Hours = (actual end − actual start) + Travel Allowance | DEC-31, DEC-40 |
| **Overtime** | Workload strictly above 40 h in a Planning Week | DEC-04 |
| **On service** | A Van with a valid Crew and at least one Job on that day | DEC-19 |
| **Needs attention** | A Van-day whose Crew became invalid after publication and is waiting for the Manager | DEC-19 |
| **Draft / Published** | The two states of a Weekly Roster. Staff see Published weeks only | DEC-16 |
| **Linked Jobs** | Jobs of different Brands at the same address, which must go on the same Van and date | DEC-11 |

### 1.4 Sources and citation format

| Citation | Source |
|---|---|
| `Brief R<n>` / `Brief §<section> ¶<n>` | [brief/project-description.md](brief/project-description.md), including its Lecturer clarifications |
| `DEC-nn` | [decisions.md](decisions.md) |
| `INT-MGR [<label>]`, `INT-DCT [<label>]` | Interview transcripts in [elicitation/interviews/](elicitation/interviews/). The label is the transcript's question tag. Where a tag repeats, a topic follows the colon |
| `INT-DRV [Q<n>]` | Driver transcript, numbered questions |
| `INT-ITA [Q: <topic>]` | IT Administrator transcript, cited by question topic |

`INT-` is added to the allowed source list in AGENTS.md in the same commit as this version.

---

## 2. Overall description

### 2.1 User classes

| User class | Description | Source |
|---|---|---|
| **Manager** | Office-based. May be more than one account, all with identical permissions. Has no Availability, Leave or Workload in the system | INT-MGR [Clarification Q1]; DEC-18 |
| **Driver** (Staff) | 6 in total. The only role allowed to drive. Uses a phone or the van tablet | Brief §Company ¶4; INT-MGR [Clarification Q3]; INT-DRV [Q14] |
| **Technician** (Staff) | 11 in total: 2 dual-Brand, 5 M Electric only, 4 Dicon only. A Brand Certification covers both Installation and Servicing. Uses their own Android phone | Brief §Company ¶4; INT-MGR [Clarification Q5]; INT-DCT [System Q3] |
| **IT Administrator** | Manages accounts, roles, lockouts, the public holiday list and the audit log | Brief R11; INT-ITA; DEC-17 |

### 2.2 Operating environment

- Browsers: Chrome is the priority; Edge, Firefox and DuckDuckGo must also work.
- Devices: company laptops and tablets, and modern phones.
- Field use has patchy signal in basements and car parks.

Sources: INT-ITA [Q: Devices]; INT-DCT [System Q3].

### 2.3 Constraints

- The system is a web application (Brief R1).
- Operations run Monday–Saturday, 09:00–18:00. The company is closed on Sundays and public holidays (DEC-12).
- Current fleet and headcount: 6 Vans, 6 Drivers and 11 Technicians (Brief §Company ¶3–4). The fleet size is data, not a hard limit.

### 2.4 Weekly cycle

Example for the Planning Week starting Monday the 19th:

| Step | When |
|---|---|
| Staff enter Availability and Job Preference | Any time within the 1-month window |
| Availability Lock | Wednesday the 7th, 18:00 |
| Manager plans: Crews first, then Jobs | From Thursday the 8th (the roster is Draft) |
| Manager publishes | Monday the 12th (Staff are notified) |
| The week runs | Monday the 19th to Saturday the 24th |

Sources: INT-MGR [Clarification Q6 follow-up]; DEC-02; DEC-16.

---

## 3. Functional requirements

### 3.1 Accounts and access

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-01 | The system shall support three roles, each with its own Landing Page: **Staff** (subtypes Driver and Technician), **Manager** and **IT Administrator** | Brief R2, R7, R11; INT-ITA [Q: Permissions]; DEC-18 | Must | Draft | Log in as each role and check that the correct Landing Page appears |
| FR-02 | The IT Administrator shall create Staff and Manager accounts. Required fields: name, email, contact number and role. Technician accounts also record their Certifications (FR-10). The account starts with an initial password that the user can change | Brief R11; INT-ITA [Q: Account info]; INT-MGR [Clarification Q2]; DEC-35 | Must | Draft | Missing required field → refused. Duplicate email → refused. Valid → the user can log in and change the password |
| FR-03 | Only the IT Administrator shall be able to assign or change roles and permissions | INT-ITA [Q: Permissions] | Must | Draft | Manager or Staff attempt → refused |
| FR-04 | The IT Administrator shall be able to change a user's role, effective from the user's next login. If a Staff member becomes a Manager, their future Assignments are removed and those Jobs become Unassigned | INT-ITA [Q: Role change/leaver]; DEC-17 | Must | Draft | Change a Driver with a future Assignment into a Manager. On next login they see the Manager page, and the Job is Unassigned |
| FR-05 | The IT Administrator shall be able to **deactivate** the account of a leaver. The user can no longer log in, their future Assignments are removed (those Jobs become Unassigned), and their past records are kept | INT-ITA [Q: Role change/leaver], [Q: Retention]; DEC-34 | Must | Draft | Deactivate a user. Login fails, the future Job is Unassigned, and last month's Assignments are still visible to the Manager |
| FR-06 | A user shall be able to reset a forgotten password through a link sent to their company email | INT-ITA [Q: Passwords] | Should | Draft | Request a reset, follow the link, set a new password and log in |
| FR-07 | An account shall lock after **5†** consecutive failed logins within **15 minutes†**. Only the IT Administrator can unlock it | INT-ITA [Q: Passwords]; DEC-17 | Should | Draft | 4 failures → still usable. 5th failure → locked. IT Administrator unlocks → login works |
| FR-08 | The IT Administrator shall be able to import employees once from a CSV export of the current employee portal. Rows with a missing required field or a duplicate email are rejected and listed in an import report | INT-ITA [Q: Existing systems], [Q: Priorities]; DEC-36 | Should | Draft | Import a file with 3 valid rows, 1 missing email and 1 duplicate: 3 accounts are created and 2 rows are reported |
| FR-09 | The IT Administrator shall load each year's public holiday list. Those dates then cannot have Crews or Jobs | INT-MGR [Clarification Q8]; DEC-12 | Must | Draft | Load the list, then try to form a Crew on a listed date → blocked. For adding a holiday after a roster exists, see FR-70 |

### 3.2 Technician Certifications

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-10 | The system shall record each Technician's Certifications: Brand, certificate number and expiry date. A Technician may hold one or both Brands. The IT Administrator enters them at account creation, and the Manager maintains them afterwards. A Certification is **valid for a Job** when its expiry date is on or after the Job's date | Brief §Company ¶2, ¶4; INT-MGR [Clarification Q2 follow-up], [Clarification Q5]; DEC-35; DEC-19 | Must | Draft | Expiry equal to the Job date → valid. Expiry the day before → invalid (FR-44 blocks it) |
| FR-11 | The Manager's Landing Page shall show a reminder for each Certification that expires within 1 month. The window uses the DEC-30 rule | INT-MGR [Clarification Q2 follow-up]; DEC-30 | Should | Draft | From 15 Mar: expiry on 15 Apr → shown; expiry on 16 Apr → not shown |
| FR-12 | The Manager may attach a scanned copy (PDF/JPG/PNG) to a Certification | INT-MGR [Clarification Q2 follow-up] | Could | Draft | Upload a file and view it |

### 3.3 Availability

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-13 | Staff shall set each **Slot** (Morning or Afternoon) of each working day to `Available` or `Unavailable`, and may clear an entry. A Slot with no entry is **Not submitted** and counts as unavailable for allocation | Brief R8; INT-MGR [Clarification Q4]; INT-DCT [Clarification Q2]; DEC-03 | Must | Draft | Set Morning = Available and leave Afternoon blank. Allocation treats the afternoon as unavailable. Sunday and public holiday Slots are not offered |
| FR-14 | Staff shall be able to enter or change Availability only for dates from **today through the same calendar date next month, inclusive** (clamped to that month's last day), and only before the Availability Lock | Brief R8 + Lecturer clarification; DEC-01; DEC-30; DEC-02 | Must | Draft | From 15 Mar: 15 Apr accepted, 16 Apr refused. From 31 Jan: 28 Feb accepted (non-leap year), 1 Mar refused |
| FR-15 | The Manager shall view the Availability of all Staff up to 1 month in advance (the FR-14 window) as a calendar grid, with Staff down the side and days across. Each cell shows one of five colour-coded states: available all day, morning only, afternoon only, on Leave, or unavailable / not submitted | Brief §Intro ¶4 + Lecturer clarification; INT-MGR [System Q2]; DEC-03 | Must | Draft | Seed each state and check that each has a distinct colour and a legend |
| FR-16 | Availability and Job Preference for a Planning Week shall lock at **18:00 on the Wednesday 12 days before** that week's Monday, in company local time | Brief §Company ¶1; INT-MGR [Clarification Q6 follow-up]; DEC-02; DEC-07 | Must | Draft | Week of Mon 19th: an edit at Wed 7th 17:59 is accepted, an edit at 18:00 is refused |
| FR-17 | For a locked week, Staff shall submit a **Late Availability Change Request** to set or change one or more Slots, with a reason. The Manager approves or rejects it. Approval applies the change, and FR-70 applies if the change affects a Crew. Rejection leaves Availability unchanged. The Staff member is notified either way | Brief §Company ¶1; INT-MGR [Conflicts Q2]; INT-DCT [Process Q1 follow-up: deadline]; DEC-02 | Must | Draft | Request without a reason → refused. Approve → Slot updated. Reject → unchanged. Both outcomes notify the Staff member |
| FR-18 | The Manager shall be able to mark a Staff member unavailable for one or more dates (e.g. sick leave, emergency), including in a published week. FR-70 applies | INT-MGR [Process Q4], [Conflicts Q2] | Must | Draft | Mark a Crew member unavailable. They are removed from the Crew, the Van-day shows Needs attention, and they are notified |
| FR-19 | Staff may copy the previous week's Availability into a week that is open for editing. Copied Slots must obey FR-14 and FR-16, and public holidays are skipped | INT-DCT [Clarification Q2] | Could | Draft | Copy into a week containing a public holiday: that day stays blank |
| FR-20 | Managers shall have no Availability, Leave or Workload, and shall not appear in Workload views | INT-MGR [Clarification Q1]; DEC-18 | Must | Draft | A Manager account has no Availability page and is absent from Workload charts |

### 3.4 Job Preference

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-21 | Staff shall be able to set a weekly Job Preference with optional fields: preferred area(s), preferred days, preferred Slot and preferred Job Type. It locks with Availability (FR-16). Preferences are advisory: they are shown in the comparison (FR-43), and violating one only raises a warning (FR-45) | Brief R9, R5; INT-DCT [Clarification Q4]; INT-DRV [Q10]; INT-MGR [Process Q1 follow-up: ordering]; DEC-07 | Must | Draft | Save a preference and see it in the comparison. Allocate against it → warning only. An empty preference is allowed |

### 3.5 Leave

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-22 | Staff shall submit a Leave Request for one or more **full working days**, with an optional note. A request cannot exceed the remaining balance or overlap an existing pending or approved request | Brief §Company ¶4; INT-MGR [Process Q4], [Process Q4 follow-up]; INT-DCT [Process Q3]; DEC-13 | Must | Draft | With 2 days left, a 3-day request → refused. An overlapping request → refused. A range including a Sunday deducts working days only |
| FR-23 | The Manager shall approve or reject a Leave Request. A rejection requires a reason. The Staff member is notified of the decision and any reason | INT-MGR [Process Q4], [Process Q4 follow-up]; DEC-13 | Must | Draft | Reject without a reason → refused. Reject with a reason → Staff sees it |
| FR-24 | Approved Leave makes the Staff member unavailable on those days, and FR-44 blocks Assignments on them. If the person is already in a Crew on those days, the Manager is warned before approving, and on approval FR-70 applies | INT-MGR [Process Q4]; INT-DRV [Q15]; DEC-13; DEC-19 | Must | Draft | Approve Leave for a Crew member → warning first. After confirming, they are removed from the Crew and the Van-day shows Needs attention |
| FR-25 | Each Staff member has **7 Leave days per calendar year**, with no carry-over. Days are deducted on approval, and the remaining balance is shown to the Staff member and the Manager | Brief §Company ¶4; INT-MGR [Process Q4], [System Q1]; INT-DCT [System Q2]; DEC-13 | Must | Draft | Approve 2 days → balance 5. On 1 Jan the balance resets to 7 |
| FR-26 | When reviewing a Leave Request, the system shall show, for each requested day, how many Vans would still be on service if it were approved | INT-MGR [Process Q4]; DEC-19 | Could | Draft | Approving would drop a day from 3 to 2 Vans on service → the count shows 2 |

### 3.6 Vans and Crews

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-27 | The system shall store each Van's number and licence plate. The Manager maintains the Van list | Brief §Company ¶3; INT-DRV [Q2]; DEC-14 | Must | Draft | Six Vans are listed with plates. Adding a seventh is possible |
| FR-28 | The system shall **generate** Workshop Servicing dates from the rotation: odd months Vans 1, 2 and 3; even months Vans 4, 5 and 6; on the 1st, 11th and 21st respectively. A date that falls on a Sunday or public holiday moves forward **day by day until it reaches a working day**. The Van is unavailable all that day. The Manager may adjust a generated date | Brief §Company ¶5; INT-MGR [Process Q3]; DEC-14 | Must | Draft | 11th = Sunday and 12th = public holiday → the servicing is on the 13th. **White-box candidate for M2** |
| FR-29 | The Manager shall be able to mark a Van unavailable for a date range (e.g. breakdown). Its not-yet-completed Jobs in that range become Unassigned, its Crew for those days is released, and the Crew members are notified | INT-MGR [Conflicts Q4]; INT-DRV [Q8] | Must | Draft | Completed Jobs are untouched. Assigned Jobs appear in the Unassigned list |
| FR-30 | For each Van that is to be on service on a working day, the Manager shall form a Crew of **exactly one Driver and one or two Technicians**. Each Crew member must be available for every Slot in which the Van has Jobs. A person may be in only one Crew per day. The Crew is fixed for the day, except under FR-33 | Brief §Company ¶3–4; INT-MGR [Process Q1], [Clarification Q4 follow-up]; DEC-09 | Must | Draft | 0 or 2 Drivers → refused. 0 or 3 Technicians → refused. A Technician available Morning only on a Van with an afternoon Job → refused |
| FR-31 | A Technician shall never be the Driver of a Crew | INT-MGR [Clarification Q3]; INT-DCT [Clarification Q1] | Must | Draft | Setting a Technician as Driver → refused |
| FR-32 | Together, a Crew's Technicians shall hold **valid Certifications (FR-10) for the Brand of every Job** on the Van that day. For Jobs of both Brands, this means either one dual-Brand Technician or one Technician per Brand | Brief §Company ¶2–3; INT-MGR [Process Q1 follow-up: ordering], [Process Q2]; INT-DCT [Conflicts Q1 follow-up]; DEC-09 | Must | Draft | **Black-box decision table for M2:** Brands on the Van × Technician Certifications × expiry |
| FR-33 | The Manager shall be able to change a Crew during the day in an emergency. The removed and added Staff are notified. Hours for Jobs already completed stay credited to whoever was on the Crew when each Job was completed | INT-MGR [Clarification Q4 follow-up]; INT-DRV [Q7]; DEC-39 | Must | Draft | After a swap, the new Technician is credited only with the remaining Jobs. FR-30 and FR-32 are re-checked |

### 3.7 Jobs

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-34 | The Manager shall create a Job. **Required:** customer name, customer phone, address, postal code, Brand, Job Type (Installation or Servicing), number of units (≥1), preferred date (a working day) and preferred Slot. **Optional:** unit number, aircon model, notes | INT-MGR [Process Q2]; INT-DCT [Process Q1 follow-up: job info]; INT-DRV [Q2]; DEC-11 | Must | Draft | Required fields only → saved. Units = 0 → refused. Preferred date on a Sunday → refused |
| FR-35 | The Job's duration shall be pre-filled from its Standard Duration (Servicing 1 h per unit, Installation 3 h per unit). The Manager can adjust it | INT-MGR [Process Q2 follow-up: hours]; INT-DCT [Clarification Q3 follow-up]; DEC-22 | Must | Draft | 2 Installation units → 6 h pre-filled. Edited to 7 h → saved |
| FR-36 | Each Job has exactly one Brand. The Manager can **link** Jobs of different Brands at the same address. Linked Jobs must be allocated to the same Van on the same date, and Staff see them grouped | INT-MGR [Process Q2]; INT-DCT [Process Q1 follow-up: job info]; DEC-11 | Must | Draft | Allocate one of two linked Jobs to a different Van → blocked |
| FR-37 | The Manager shall be able to edit or cancel a Job that is not Completed. An edited, assigned Job is re-checked against FR-44. If it now breaks a rule, it becomes Unassigned and the Manager is told why. The Crew is notified of any change or cancellation | INT-MGR [added follow-up: cancellations]; DEC-19 | Must | Draft | Change an assigned Job's Brand to one the Crew can't do → Job becomes Unassigned and a reason is shown. Cancel → Crew notified |
| FR-38 | Job status shall follow these transitions only: Unassigned → Assigned (allocation). Assigned → Unassigned (rejection, Van unavailable, invalidating edit, deactivated Staff or the Manager unassigning it). Assigned → Completed (FR-39). Unassigned or Assigned → Cancelled. Completed and Cancelled are final | INT-MGR [Conflicts Q3], [Conflicts Q4], [added follow-up: cancellations]; DEC-15; DEC-40 | Must | Draft | Test each allowed transition. Completed → Cancelled → refused |
| FR-39 | A **Technician** on the Van's Crew shall mark an assigned Job Completed. They record: actual start and end time (end after start, both on the Job's date), a short remark, whether a follow-up visit is needed, and the invoice photo (FR-40) | INT-DCT [Process Q1 follow-up: completion]; INT-MGR [Process Q1 follow-up: completion]; DEC-40 | Must | Draft | A Driver attempts it → refused. End before start → refused |
| FR-40 | Completing a Job **requires** a photo of the invoice signed by the customer. If the Technician is offline, it can be queued (NFR-08) | INT-MGR [Process Q1 follow-up: completion]; DEC-40 | Must | Draft | Submit without a photo → refused |

### 3.8 Job Allocation

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-41 | The Manager shall allocate Jobs **one Planning Week at a time** (the next unpublished week), assigning each Job to a Van with a Crew on a date within that week | Brief R3; INT-MGR [Process Q1], [Clarification Q6]; DEC-10; DEC-16 | Must | Draft | Try to allocate to a date outside the Planning Week → refused (published weeks change via FR-50) |
| FR-42 | The Manager shall set each Job's start time on the Van's day. Rules: Jobs run within 09:00–18:00 and skip lunch (13:00–14:00). A Job may span both Slots. Consecutive Jobs must be at least the 0.5 h Travel Allowance apart. Jobs on the same Van must not overlap | INT-DRV [Q5]; INT-MGR [Clarification Q4], [Clarification Q7]; DEC-12; DEC-31 | Should | Draft | A 3 h Job at 11:00 runs 11:00–13:00, pauses for lunch and ends 15:00. A Job at 15:10 → refused (needs 15:30 or later) |
| FR-43 | On the Job Allocation page, the Manager shall select **up to three** Staff and compare them side by side for the Job's date and Planning Week. For each, show: Availability that day and week, Workload in that Planning Week, Certifications with expiry, Job Preference, and location that day (postal districts of their other Jobs, or "No Jobs") | Brief R4, R5; INT-MGR [System Q3]; DEC-06; DEC-08 | Must | Draft | A 4th selection → refused. All five items are shown for each person |
| FR-44 | The system shall **block** any allocation, Crew change, Job edit or approval that would cause: an invalid or expired Certification for a Job's Brand (FR-32); a double booking (a person in two Crews on one day, or overlapping Jobs on a Van); a Crew member unavailable, not submitted or on Leave for a Slot the Van works; an invalid Crew (FR-30, FR-31); linked Jobs split across Vans (FR-36); a Van that is unavailable; or a Sunday or public holiday | INT-MGR [System Q4], [Process Q3], [Clarification Q8]; DEC-19 | Must | Draft | One negative test per rule. **Black-box decision-table candidate** |
| FR-45 | The system shall **warn**, allow an override and log it, when an allocation would cause: a Staff member's Workload above 40 h in the Planning Week; a Job Preference not met; a Job starting outside the customer's preferred Slot; or fewer than 3 Vans on service on a working day. Overtime has no approval step | Brief §Company ¶4, R6; INT-MGR [System Q4], [Conflicts Q1]; DEC-19; DEC-32 | Must | Draft | Trigger each warning, override it, and see the override in the audit log (FR-66) |
| FR-46 | The system shall list the Jobs with status **Unassigned** and show their count. Cancelled Jobs are excluded | INT-MGR [Conflicts Q1], [System Q1 follow-up: ranking] | Must | Draft | Reject an assigned Job → count +1. Cancel an Unassigned Job → count −1 |
| FR-47 | For each working day and Slot, the system shall list Staff who are available but not in any Crew | INT-MGR [Conflicts Q2 follow-up: standby] | Should | Draft | Seed one available, uncrewed person → listed |
| FR-48 | For an Unassigned Job, the system shall suggest replacement Staff. Candidates must: hold a valid Certification for the Job's Brand (Technicians); be available for the Job's Slots; and be either uncrewed that day or already on a Van with room in its Crew. The list is sorted by Planning Week Workload, lowest first, then by name. The Manager chooses | INT-MGR [Conflicts Q2 follow-up: staff cancellation]; DEC-19 | Should | Draft | Unqualified and unavailable Staff are excluded. The order is checked on seeded data |
| FR-49 | The Manager shall **publish** a Planning Week's roster, changing it from Draft to Published. Publishing is refused while any FR-44 violation exists, and allowed with FR-45 warnings outstanding. Every Staff member with Assignments that week is notified | INT-MGR [Process Q1], [Conflicts Q1], [added follow-up: notifications]; DEC-16; DEC-19 | Must | Draft | Publish with a "fewer than 3 Vans" warning → allowed. Publish with an invalid Crew → refused |
| FR-50 | After publication, the Manager shall be able to add, move or unassign Jobs and change Crews for current and future dates. Changes are re-checked (FR-44 and FR-45). The removed and added Staff are notified | INT-MGR [Conflicts Q5], [Conflicts Q2 follow-up: staff cancellation]; DEC-16 | Must | Draft | Add a Job to a published day → Crew notified and Workload updated. Past dates → read-only |
| FR-51 | The system shall show a weekly timeline for a selected week, with one row per Van: its Crew and Jobs, and unavailable days shaded | INT-MGR [System Q2] | Must | Draft | A Van on Workshop Servicing shows a shaded day |
| FR-69 | Each Planning Week's roster is **Draft** until published. Staff see Assignments only for Published weeks. The Manager sees both | DEC-16 | Must | Draft | Assign a Job in a Draft week → invisible to Staff until publication |
| FR-70 | When a later event makes an existing Crew invalid, the system shall remove the affected person from that Crew for the affected dates, mark each affected Van-day **Needs attention** on the Manager's Landing Page, and notify the removed person. Triggering events: approved Leave, the Manager marking someone unavailable, an approved Late Availability Change Request, a Certification expiring, or a public holiday being added. The Van's Jobs stay on the Van until the Manager fixes the Crew. (A Van becoming unavailable is handled by FR-29 instead) | DEC-19; INT-MGR [Process Q4], [Conflicts Q2] | Must | Draft | Approve Leave for the only Driver of a Van → Driver removed, Van-day flagged, Jobs still on the Van |

### 3.9 Workload and Landing Pages

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-52 | A Job's **Planned Hours** = its duration (FR-35) + a 0.5 h Travel Allowance. Breaks are not counted | INT-MGR [Clarification Q7]; INT-DCT [System Q1]; DEC-31 | Must | Draft | 1 Servicing unit → 1.5 h. 2 Installation units → 6.5 h |
| FR-53 | Every Crew member (the Driver and each Technician) is credited with the hours of **all Jobs on their Van that day**. Workload counts Assigned Jobs at Planned Hours and Completed Jobs at Actual Hours. Unassigned and Cancelled Jobs count zero | INT-MGR [Clarification Q7], [Clarification Q4 follow-up]; DEC-39; DEC-40 | Must | Draft | A Van with 7 h of Jobs → Driver and both Technicians each get 7 h |
| FR-54 | When a Job is Completed, its **Actual Hours** = (actual end − actual start) + 0.5 h, and they replace its Planned Hours in Workload | INT-MGR [Clarification Q7], [Conflicts Q5]; INT-DCT [Conflicts Q3]; DEC-40 | Must | Draft | Planned 1.5 h, actual 10:00–11:30 → counts 2.0 h |
| FR-55 | Workload is summed per Planning Week (Monday–Saturday). Workload **strictly above 40 h** is Overtime and is highlighted wherever Workload is shown | Brief R6; INT-MGR [Clarification Q7]; DEC-04 | Must | Draft | **Boundary test:** 40.0 h → not highlighted, 40.5 h → highlighted |
| FR-56 | The Manager's Landing Page shall show, for the current week by default and switchable to the Planning Week: a Workload bar chart for every Driver and Technician with a line at 40 h and Overtime highlighted; the lowest-three lists (FR-57); today's Vans and Crews; the Unassigned Job count (FR-46); **requests awaiting a decision** (Leave Requests, Late Availability Change Requests); **rejected Jobs awaiting reassignment**; Van-days marked Needs attention; and Certification reminders (FR-11) | Brief R2, R6; INT-MGR [System Q1 follow-up: landing page], [System Q2]; DEC-15; DEC-19 | Must | Draft | Seed each element and check they are all visible without navigating away |
| FR-57 | The Landing Page shall show two lists for the displayed week: the three **Technicians** and the three **Drivers** with the lowest Workload. Staff with any approved Leave day in that week are excluded. Ties are broken by name (A–Z). If fewer than three are eligible, show those who are | Brief R6; INT-MGR [added follow-up: lowest three]; DEC-05 | Must | Draft | A Technician on Leave on Tuesday → excluded. Two Drivers tied at 20 h → alphabetical order |
| FR-58 | The Staff Landing Page shall show: a weekly calendar of their Assignments for the current week, switchable to the next Published week, with times and addresses; their Workload for that week against 40 h; their Workload for the **calendar month**; and their Leave balance | Brief R7; INT-DCT [System Q2]; INT-DRV [Q13]; DEC-04; FR-69 | Must | Draft | Seeded totals match. A Draft week is not selectable |
| FR-59 | For each Assignment, Staff shall see: customer name and phone, address, unit number and postal code, Brand, model, number of units, Job Type, start time, notes, Van number and licence plate, the Crew members' names and contact numbers, and any Linked Jobs | INT-DRV [Q1], [Q2]; INT-DCT [Process Q1 follow-up: job info]; DEC-37 | Must | Draft | All fields fit a 360 px-wide screen (NFR-15) |
| FR-60 | The Manager shall view, per Staff member, Workload for a selected week and calendar month, and Leave taken and remaining. The Manager also sees the number of Jobs Completed per calendar month | INT-MGR [System Q1], [System Q1 follow-up: ranking]; DEC-04 | Should | Draft | Totals match the seeded data |
| FR-61 | The Manager shall view, per Van, the days in a calendar month it was **on the road**, meaning it had at least one Completed Job that day | INT-MGR [System Q1] ("nice to have") | Could | Draft | A day with only cancelled Jobs is not counted |

### 3.10 Job Rejection

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-62 | Any Crew member shall be able to reject a Job assigned to their Van in a Published week. Before confirming, the system warns them to discuss it with the Manager first. If the Job starts within 48 hours, the warning also says the Manager expects 48 hours' notice except in emergencies. The Staff member must pick a reason: Personal emergency; Clash with another job; Not qualified or missing equipment; or Other, which requires a comment. Telling the company ahead of time that a Job can't be done uses this same function | Brief R10, §Intro ¶3; INT-MGR [Conflicts Q3], [added follow-up: early rejection]; INT-DCT [Process Q2], [Conflicts Q2]; INT-DRV [Q17]; DEC-15 | Must | Draft | Cancel at the warning → nothing changes. "Other" with no comment → refused. A Job starting within 48 h → the extra warning text appears |
| FR-63 | A confirmed rejection needs **no approval**. The Job becomes Unassigned and is removed from the whole Van. The Manager is notified immediately, the other Crew members are notified, and the rejecting person sees a confirmation | INT-MGR [Conflicts Q3]; INT-DCT [Process Q2 follow-up: after reject]; DEC-15 | Must | Draft | After rejecting: the Job is in the Unassigned list, gone from all Crew members' views, and the Manager has a notification |

### 3.11 Notifications

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-64 | Staff shall be notified **on their Landing Page and by email** when: a week containing their Assignments is published; one of their Assignments is added, changed, cancelled or rejected by a Crew-mate; they are added to or removed from a Crew; or a decision is made on their Leave Request or Late Availability Change Request | INT-MGR [added follow-up: notifications], [Conflicts Q5], [added follow-up: cancellations]; INT-DCT [Process Q1 follow-up: updates], [Conflicts Q2]; INT-DRV [Q7] | Must | Draft | One test per trigger, checking both channels and both the removed and added Staff |
| FR-65 | The Manager shall be notified on their Landing Page of: new Job Rejections; new Leave Requests and Late Availability Change Requests; newly flagged Needs attention Van-days; and Certification reminders. Each item can be marked handled | INT-MGR [Conflicts Q3], [System Q1 follow-up: landing page]; DEC-15; DEC-19 | Must | Draft | Each event type appears. Marking an item handled removes it from the list |

### 3.12 Audit and records

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-66 | The system shall log, with who, what and when: account and role changes, password change requests, and every change to Availability, Crews, Assignments, Jobs and Leave, including overridden warnings. Only the IT Administrator can view the audit log | INT-ITA [Q: Audit]; DEC-17 | Should | Draft | Make each change type → log entry exists. Manager tries to open the log → refused |
| FR-67 | No user may delete records dated in the past or in progress. Jobs are Cancelled rather than deleted. Future Availability entries may be cleared (FR-13) | INT-ITA [Q: Retention]; DEC-34 | Must | Draft | Try to delete yesterday's Job → no delete option exists. Cancelling a future Job is allowed |
| FR-68 | ~~Import existing schedules from a CSV export~~ | INT-ITA [Q: Existing systems]; DEC-36 | Won't | **Withdrawn** | Withdrawn by DEC-36: no schedule import |

---

## 4. Non-functional requirements

| ID | Category | Description (with measurable criterion) | Source / justification | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| NFR-01 | Performance | With the NFR-03 load and reference dataset, **95%†** of main user actions (saving Availability, a Leave Request, an Assignment or a rejection; loading a Landing Page) shall complete within **5 s**, measured at the server | INT-ITA [Q: Response time] ("maybe 3 or 5 seconds"); Brief R2 ("immediately") | Should | Draft | Load test, reporting the 95th percentile per action |
| NFR-02 | Performance | A saved change shall be visible to other logged-in users within **60 s** | INT-ITA [Q: Response time] ("less than a minute or so") | Should | Draft | Save as the Manager and time until it appears in an open Staff session |
| NFR-03 | Capacity | The system shall support **50 concurrent sessions**, including one person on up to 3† devices, with a reference dataset of 6 Vans, 17 Staff, 25 Jobs per working day† (above the brief's "more than 20") and 13 months of records (the 12-month retention plus the 1-month window) | INT-ITA [Q: Concurrency]; Brief §Company ¶4–5; DEC-34 | Must | Draft | Load test at 50 sessions on the reference dataset |
| NFR-04 | Security | Each user shall be limited to **60 requests per minute†**. Excess requests are rejected with a "try again shortly" message, and normal service resumes after the minute | INT-ITA [Q: Concurrency] | Should | Draft | Script 61 requests in one minute → the 61st is rejected |
| NFR-05 | Availability | The system shall be available 24/7 with **≥ 99%† monthly uptime**, excluding planned maintenance between **00:00 and 05:00†**, which must not fall on Monday or Thursday mornings (peak periods) | INT-ITA [Q: Hours], [Q: Outage]; DEC-38 | Must | Draft | Monthly uptime report from monitoring |
| NFR-06 | Recoverability | After a failure, service and data shall be restored within **24 h** of the failure being detected | INT-ITA [Q: Outage] ("Not more than one day"), [Q: Restore] | Must | Draft | Timed restore drill from backup on a test environment |
| NFR-07 | Recoverability | No more than **1 h** of saved data may be lost. Backups run at least hourly, and a failed backup raises an alert to the IT Administrator | INT-ITA [Q: Restore], [Q: Outage] | Must | Draft | Restore the latest backup and confirm the newest record is at most 1 h older than the failure point |
| NFR-08 | Reliability / offline | Staff shall be able to view **today's** published Assignments without a connection. A Job completion (with its photo) entered offline is queued and submitted automatically when the connection returns | INT-DCT [System Q3]; INT-ITA [Q: Outage], [Q: Connection failure] | Should | Draft | In airplane mode, today's Jobs are viewable and a completion is queued. Reconnect → it is saved |
| NFR-09 | Reliability | A failed submission shall be retried automatically up to **3†** times. If it still fails, the user sees a message saying it was not saved and advising them to try again or contact the IT Administrator | INT-ITA [Q: Connection failure] | Should | Draft | Cut the network mid-submit → retries, then the message |
| NFR-10 | Security | Login from a device not used in the last **30 days** shall require an email confirmation (2FA), for all roles | INT-ITA [Q: Safeguards]; DEC-41 | Should | Draft | New device → email confirmation required. Same device the next day → not required |
| NFR-11 | Security | Staff personal data and schedule data shall be encrypted at rest. Passwords are stored only as salted hashes† | INT-ITA [Q: Safeguards] ("encrypted properly in the backend") | Must | Draft | Inspect the database: personal fields are unreadable and there are no plaintext passwords |
| NFR-12 | Security | Access shall be role-based, following the **permission matrix in §4.1** | INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-18; DEC-37 | Must | Draft | Test every role × action cell in §4.1. Every ✗ must be refused |
| NFR-13 | Data retention | Schedule records (Jobs, Crews, Assignments, Availability, Leave) shall be kept for **12 months** from their date, and may then be purged. Deactivated users' records follow the same rule | INT-ITA [Q: Retention] ("up to one year"); DEC-34 | Must | Draft | A record from 11 months ago is retrievable |
| NFR-14 | Compatibility | The system shall work on the latest stable versions of Chrome, Edge, Firefox and DuckDuckGo at the time of the M2 demo, on Windows, Android and iOS | INT-ITA [Q: Devices] | Must | Draft | Run the main flows on each browser. Record the versions tested |
| NFR-15 | Compatibility / usability | All Staff pages shall work at **360 px† width** without horizontal scrolling. The Manager's pages shall work at **1366 px† width or more** | INT-DCT [System Q3]; INT-DRV [Q14]; INT-ITA [Q: Devices] | Must | Draft | Responsive check at those widths |
| NFR-16 | Usability | In a walkthrough with **3†** non-technical users, each shall complete "enter a week's Availability" and "reject a Job" without help, in under **3 minutes†** each | INT-MGR [Closing] ("Just keep it simple. Most of my staff aren't very technical.") | Must | Draft | Moderated walkthrough on the wireframe prototype |
| NFR-17 | Constraint | The system shall be a web application that runs in a browser with no install | Brief R1 | Must | Draft | Open it in a browser |

### 4.1 Permission matrix (NFR-12)

✓ = allowed, ✗ = refused, "own" = only for the user's own records, "crew" = only for Jobs on their own Van.

| Action | Staff (Driver) | Staff (Technician) | Manager | IT Administrator |
|---|---|---|---|---|
| Set Availability, Job Preference; request Leave or a late change | own | own | ✗ | ✗ |
| View Assignments | own, Published weeks only | own, Published weeks only | all | ✗ |
| View Crew-mates' names and contact numbers | crew | crew | all | ✗ |
| View other Staff's Availability, Leave or Workload | ✗ | ✗ | ✓ | ✗ |
| Reject a Job | crew | crew | ✗ | ✗ |
| Mark a Job Completed | ✗ | crew | ✗ | ✗ |
| Create, edit or cancel Jobs; form Crews; allocate; publish | ✗ | ✗ | ✓ | ✗ |
| Approve or reject Leave and late changes; mark Staff unavailable | ✗ | ✗ | ✓ | ✗ |
| Maintain Vans, Workshop Servicing dates and Certifications (after creation) | ✗ | ✗ | ✓ | ✗ |
| Create, import or deactivate accounts; change roles; unlock accounts | ✗ | ✗ | ✗ | ✓ |
| Load public holidays; view the audit log | ✗ | ✗ | ✗ | ✓ |

Sources: INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-35; DEC-37; DEC-40.

---

## 5. Coverage check: Brief initial requirements

| Brief | Summary (see brief for exact text) | FR / NFR IDs |
|---|---|---|
| R1 | Web-based | NFR-17, NFR-14 |
| R2 | Manager Landing Page shows staff workload | FR-56, NFR-01 |
| R3 | Allocate jobs one week at a time | FR-41, FR-69 |
| R4 | Allocation page: up to three staff availability | FR-43 |
| R5 | Availability display: workload, preference, location, week availability | FR-43, FR-21 |
| R6 | Three lowest workload; highlight >40 hours | FR-55, FR-56, FR-57 |
| R7 | Staff Landing Page: weekly assignments and monthly workload | FR-58, FR-59 |
| R8 | Add/edit availability up to **1 month in advance** (the brief's "5 weeks" is superseded, DEC-01) | FR-13, FR-14 |
| R9 | Weekly job preference | FR-21 |
| R10 | Reject jobs with warning | FR-62, FR-63 |
| R11 | IT administrators add staff and managers | FR-02, FR-03 |

## 6. Candidate M2 testing targets

| Rubric item | Candidate | Why it qualifies |
|---|---|---|
| Black-box (decision table) | FR-32 / FR-44: Crew and Brand validity | Several conditions: Brands on the Van, each Technician's Certifications, expiry vs Job date, Crew size |
| Black-box (alternative) | FR-62 / FR-63: Job Rejection | Conditions: published week, within 48 h, reason = Other, comment present |
| White-box (CFG with ≥8 nodes and ≥2 decisions) | FR-28: generate Workshop Servicing dates | A loop over Vans and dates, an odd/even month branch, and a Sunday/public-holiday shift loop |

## 7. Open items affecting this SRS

None of the SRS-level DECs are open. The remaining open entries are rubric and lecturer questions (DEC-21, DEC-23 to DEC-29). They affect the report and diagrams, not the requirements.
