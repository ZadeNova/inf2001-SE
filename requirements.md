# Software Requirements Specification: Aircon Service Workload Management System

> **Status: DRAFT for team review.** This draft was AI-assisted (Claude Code, 2026-09-30) from the brief, the lecturer's clarification and the four interview transcripts. See [ai-usage-log.md](ai-usage-log.md).
> Every row cites its source. Nothing is agreed until the team has reviewed it. Rows marked `Blocked` depend on a conflict between sources that the team must resolve first (§7).
> Priorities are **proposed** (MoSCoW). The team confirms them. Brief R1–R11 are the minimum deliverable, so they are always `Must`.
> Thresholds marked **†** were **not stated by any stakeholder**. They are placeholders the team must confirm with a stakeholder or replace.

**Status values:** `Draft` → `Agreed` (confirmed by the team or a stakeholder) → `Withdrawn`, or `Blocked` (waiting on a DEC).

---

## 1. Introduction

### 1.1 Purpose

This SRS specifies the functional and non-functional requirements of a web-based workload management system for the aircon service team of an aircon retailer. It is the input to the Milestone 1 use cases, class diagram and sequence diagrams.

### 1.2 Scope

The system lets the **Manager**:
- record Jobs
- form daily Van Crews and allocate Jobs one Planning Week at a time
- see Availability and Workload at a glance up to 1 month in advance
- handle Leave, late Availability changes and Job Rejections.

It lets **Staff** (Drivers and Technicians):
- enter Availability, Job Preferences and Leave
- see their Assignments and Workload
- record Job completion
- reject Jobs.

It lets the **IT Administrator** manage accounts, permissions and the public holiday calendar.

**Out of scope**, with the source for each exclusion:

| Excluded | Source |
|---|---|
| Wages, job costs and payroll ("handled by our accounts department") | INT-MGR [System Q1] |
| Live GPS tracking of Staff ("I don't need live GPS tracking") | INT-MGR [System Q3] |
| Customer self-booking. Customers call or message the office and the Manager enters the Job | INT-MGR [Process Q2] |
| Sunday or public holiday emergency jobs ("I handle that outside the system") | INT-MGR [Clarification Q8] |
| Same-day changes by phone call. The phone call itself happens outside the system, but the system records the change (FR-50) | INT-MGR [added follow-up: notifications]; INT-DCT [Process Q1 follow-up: updates] |
| Automatic route optimisation. Job order is set by the Manager (FR-42) | INT-DRV [Q5] |

### 1.3 Definitions

The canonical terms are in the [AGENTS.md glossary](AGENTS.md#glossary-canonical-terms). This SRS uses the terms below, which are **not yet in the glossary**. They are proposed for addition once the team agrees them.

| Proposed term | Meaning | Source |
|---|---|---|
| **Crew** | The Driver and 1–2 Technicians assigned to one Van for one working day | INT-MGR [Clarification Q4 follow-up]; Brief §Company ¶3–4 |
| **Planning Week** | The Monday–Saturday week being planned and published | INT-MGR [Process Q1], [Clarification Q7] |
| **Slot** | A half-day unit of Availability: `Morning` (09:00–13:00) or `Afternoon` (14:00–18:00) | INT-MGR [Clarification Q4] |
| **Late Availability Change Request** | A Staff request to change Availability after the Availability Deadline | INT-MGR [Conflicts Q2] |
| **Leave Request** | A Staff application for annual Leave, approved or rejected by the Manager | INT-MGR [Process Q4] |
| **Standard Duration** | Default Job duration: Servicing 1 h per unit, Installation 3 h per unit | INT-MGR [Process Q2 follow-up: hours] |
| **Travel Allowance** | A fixed 30 minutes added to each Job's hours | INT-MGR [Clarification Q7] |
| **Planned Hours / Actual Hours** | A Job's hours before and after completion is recorded | INT-MGR [Clarification Q7] |
| **Overtime** | Workload above 40 hours in a Planning Week | INT-MGR [Clarification Q7]; Brief R6 |
| **Unassigned Job** | A Job that is not assigned to any Van on any date | INT-MGR [Conflicts Q1], [Conflicts Q3] |

### 1.4 Sources and citation format

| Citation | Source |
|---|---|
| `Brief R<n>` / `Brief §<section> ¶<n>` | [brief/project-description.md](brief/project-description.md), including its Lecturer clarifications |
| `DEC-nn` | [decisions.md](decisions.md) |
| `INT-MGR [<label>]` | [elicitation/interviews/manager.md](elicitation/interviews/manager.md). The label is the question tag in the transcript. Where a tag repeats, a topic follows the colon |
| `INT-DCT [<label>]` | [elicitation/interviews/dct.md](elicitation/interviews/dct.md) |
| `INT-DRV [Q<n>]` | [elicitation/interviews/driver.md](elicitation/interviews/driver.md), numbered questions |
| `INT-ITA [Q: <topic>]` | [elicitation/interviews/ita.md](elicitation/interviews/ita.md). This file has no question tags, so it is cited by the question's topic |

The `INT-` citations are **proposed**. AGENTS.md currently allows only `Brief`, `MTG-nn` and `DEC-nn` as sources. The team should either add `INT-` to that list or give each interview an MTG ID and replace these citations. Answer-key rows (AK-nn) are **not** cited, because they are team summaries.

---

## 2. Overall description

### 2.1 User classes

| User class | Description | Source |
|---|---|---|
| **Manager** | Full-time and office-based. Enters Jobs, builds Crews, allocates and publishes the Weekly Roster, and approves Leave and late changes. Has no Availability, and their hours are not counted in Workload | Brief §Intro ¶4; INT-MGR [Clarification Q1] |
| **Driver** (Staff) | 6 in total. Drives the Van. Only Drivers are covered by the vehicle insurance. Uses a phone or the van tablet | Brief §Company ¶4; INT-MGR [Clarification Q3]; INT-DRV [Q1], [Q14] |
| **Technician** (Staff) | 11 in total: 2 dual-Brand, 5 M Electric only, 4 Dicon only. A Brand Certification covers both installation and servicing. Never drives. Uses their own Android phone | Brief §Company ¶4; INT-MGR [Clarification Q5]; INT-DCT [Clarification Q1], [System Q3] |
| **IT Administrator** | Creates accounts and manages permissions, account problems and the public holiday list | Brief R11; INT-ITA; INT-MGR [Clarification Q2], [Clarification Q8] |

The Manager says "Most of my staff aren't very technical" (INT-MGR [Closing]).

### 2.2 Operating environment

- The system is a web application (Brief R1).
- Browsers: Chrome is the most important, plus Edge, Firefox and DuckDuckGo (INT-ITA [Q: Devices]).
- Devices: company laptops and tablets, and modern phones, including Android (INT-ITA [Q: Devices]; INT-DCT [System Q3]).
- Staff use it in the field. Mobile data is usually fine, but there is no signal in some basements and car parks (INT-DCT [System Q3]).

### 2.3 Constraints

- The system is web-based, in a language of the team's choosing (Brief R1).
- Operations run Monday to Saturday. The company is closed on Sundays and public holidays, with no Jobs and no roster (INT-MGR [Clarification Q8]; Brief §Company ¶4).
- Fleet and headcount: 6 Vans, 6 Drivers and 11 Technicians (Brief §Company ¶3–4).

### 2.4 Weekly planning cycle (as described by the Manager)

1. Staff enter Availability until **18:00 on Wednesday**.
2. The Manager plans from Thursday: vans first, then crews, then Jobs.
3. The Manager publishes on **Monday** for the **following** Monday–Saturday week.

The Manager's example: "for the week starting Monday the 19th, availability is due by 6pm on Wednesday the 7th, I plan from Thursday the 8th, and I publish on Monday the 12th." Sources: INT-MGR [Process Q1], [Clarification Q6 follow-up]; Brief §Company ¶1.

---

## 3. Functional requirements

### 3.1 Accounts and access

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-01 | The system shall support three roles, each with its own Landing Page and permissions: **Staff** (Driver or Technician), **Manager** and **IT Administrator** | Brief R2, R7, R11; INT-ITA [Q: Onboarding], [Q: Permissions] | Must | Draft | Log in as each role and confirm the role-specific Landing Page and menu |
| FR-02 | The IT Administrator shall be able to create Staff and Manager accounts, recording name, email, contact number, role and an initial password that the user can change later | Brief R11; INT-ITA [Q: Account info]; INT-MGR [Clarification Q2] | Must | Draft | Create one account of each role and log in with the initial password. Confirm the user can change it |
| FR-03 | Only the IT Administrator shall be able to assign or change a user's role and permissions | INT-ITA [Q: Permissions], [Q: Onboarding] | Must | Draft | Attempt a role change as a Manager and as Staff. It must be refused |
| FR-04 | The IT Administrator shall be able to change an existing user's role, and the user's permissions shall update to match | INT-ITA [Q: Role change/leaver] | Must | Draft | Change a Driver to a Manager and confirm the permissions change on the next login |
| FR-05 | The IT Administrator shall be able to remove the account of a user who leaves the company | INT-ITA [Q: Role change/leaver] | Should | **Blocked** (DEC-34) | Delete vs deactivate, and what happens to that user's records, must be decided first |
| FR-06 | A user shall be able to reset a forgotten password through a forgot-password link that sends a confirmation to their company email | INT-ITA [Q: Passwords] | Should | Draft | Request a reset, follow the email link and log in with the new password |
| FR-07 | An account shall be locked after repeated failed login attempts, and only the IT Administrator shall be able to unlock it | INT-ITA [Q: Passwords] | Should | Draft | Failed-attempt threshold **†TBC**. Exceed it, then confirm the account is locked and that only the IT Administrator can unlock it |
| FR-08 | The IT Administrator shall be able to import existing employee records from a CSV export of the current employee portal | INT-ITA [Q: Existing systems], [Q: Priorities] | Should | Draft (see DEC-36) | Import a sample CSV and confirm the accounts are created with the correct fields |
| FR-09 | The IT Administrator shall be able to load the year's public holiday list. The system shall then block Crews and Assignments on those dates | INT-MGR [Clarification Q8] | Must | Draft | Load the list, then try to assign a Job on a listed date. It must be blocked |

### 3.2 Technician Certifications

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-10 | The system shall record each Technician's Certifications: Brand, certificate number and expiry date. A Technician may hold one or both Brands | Brief §Company ¶2, ¶4; INT-MGR [Clarification Q2 follow-up], [Clarification Q5] | Must | Draft (who maintains it: DEC-35) | Record a dual-Brand Technician. Both Brands must appear in the allocation comparison |
| FR-11 | The system shall remind the Manager one month before a Technician's Certification expires | INT-MGR [Clarification Q2 follow-up] | Should | Draft | Set an expiry 30 days ahead and confirm the reminder appears. Whether "one month" means 30 days or a calendar month is **†TBC** |
| FR-12 | The system shall allow a scanned copy of a Certification to be uploaded | INT-MGR [Clarification Q2 follow-up] ("nice, but it isn't essential") | Could | Draft | Upload a PDF or image and view it |

### 3.3 Availability

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-13 | Staff shall be able to add and edit their Availability per Slot (Morning 09:00–13:00, Afternoon 14:00–18:00) for each working day from Monday to Saturday, excluding public holidays | Brief R8; INT-MGR [Clarification Q4]; INT-DCT [Clarification Q2] | Must | Draft | Enter Morning-only for a day and confirm it is stored and shown. Sunday and public holiday Slots must not be offered |
| FR-14 | Staff shall be able to enter and edit Availability for dates up to 1 month in advance, and no further | Brief R8, §Intro ¶3 + Lecturer clarification; DEC-01 | Must | Draft (exact boundary: DEC-30) | Boundary test on the last allowed date and the day after it, once DEC-30 fixes the rule |
| FR-15 | The Manager shall be able to view the Availability of all Staff up to 1 month in advance as a calendar grid, with Staff down the side and days across. Cells are colour-coded as available, morning only, afternoon only, or on Leave | Brief §Intro ¶4 + Lecturer clarification; DEC-01; INT-MGR [System Q2], [Clarification Q6] | Must | Draft | Seed each of the four states and confirm each has a distinct colour. Scroll to +1 month |
| FR-16 | Availability for a Planning Week shall lock at 18:00 on the Wednesday 12 days before that week's Monday | Brief §Company ¶1; INT-MGR [Process Q1], [Clarification Q6 follow-up] | Must | Draft | Using the Manager's example, week of Monday 19th: an edit at 17:59 on Wednesday 7th is accepted, and an edit at 18:00 is refused |
| FR-17 | After the lock, Staff shall be able to submit a Late Availability Change Request with a reason. The Manager shall approve or reject it, and an approved request shall update the Availability | Brief §Company ¶1; INT-MGR [Conflicts Q2], [Clarification Q6 follow-up]; INT-DCT [Process Q1 follow-up: deadline] | Must | Draft | Submit a request after the lock. Approve it and confirm Availability changes. Reject another and confirm Availability is unchanged |
| FR-18 | The Manager shall be able to mark a Staff member unavailable for any date, including after the Weekly Roster is published (e.g. sick leave or an emergency) | INT-MGR [Process Q4], [Conflicts Q2] | Must | Draft | Mark an assigned Staff member unavailable. Their Assignment must be flagged for reassignment |
| FR-19 | Staff shall be able to copy the previous week's Availability into a new week | INT-DCT [Clarification Q2] ("It would be nice") | Could | Draft | Copy, then confirm all Slots match the source week |
| FR-20 | The system shall not require Availability from Managers or calculate Workload for them | INT-MGR [Clarification Q1] | Must | Draft | A Manager account has no Availability page and does not appear in the Workload views |

### 3.4 Job Preference

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-21 | Staff shall be able to indicate a Job Preference for each week, covering preferred area, preferred days or time of day, and preferred Job Type. Preferences are advisory: they are shown during allocation (FR-43) and only raise a warning (FR-45) | Brief R9, R5; INT-DCT [Clarification Q4]; INT-DRV [Q10]; INT-MGR [Process Q1 follow-up: ordering] ("tie-breaker, not a rule") | Must | Draft | Save a preference and confirm it appears in the allocation comparison. The preference deadline is **TBC** (see §6, DEC-07) |

### 3.5 Leave

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-22 | Staff shall be able to submit a Leave Request for one or more days, with an optional note | Brief §Company ¶4; INT-MGR [Process Q4], [Process Q4 follow-up]; INT-DCT [Process Q3] | Must | Draft | Submit with and without a note |
| FR-23 | The Manager shall be able to approve or reject a Leave Request. A rejection requires a reason, and the Staff member shall see the decision and the reason | INT-MGR [Process Q4], [Process Q4 follow-up] | Must | Draft | Try to reject without a reason, which must fail. Reject with a reason and confirm the Staff member sees it |
| FR-24 | Approved Leave shall automatically make the Staff member unavailable for those days, and the system shall block Assignments on them | INT-MGR [Process Q4]; INT-DRV [Q15] | Must | Draft | Approve Leave, then try to add the person to a Crew that day. It must be blocked |
| FR-25 | The system shall track each Staff member's Leave balance: 7 days per calendar year, with no carry-over. The remaining balance shall be shown to the Staff member and the Manager | Brief §Company ¶4; INT-MGR [Process Q4], [System Q1]; INT-DCT [Process Q3], [System Q2] | Must | Draft | Approve 2 days and confirm the balance is 5. On 1 Jan confirm it resets to 7 |
| FR-26 | When reviewing a Leave Request, the system shall show how many Vans could still be crewed on each requested day | INT-MGR [Process Q4] ("make sure we can still run at least three vans that day"). *Derived: supports a check the Manager described* | Could | Draft | Approve Leave that drops a day to 2 crewable Vans and confirm the count is shown |

### 3.6 Vans and Crews

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-27 | The system shall record each Van's number and licence plate | Brief §Company ¶3; INT-DRV [Q2]; INT-MGR [Process Q3] | Must | Draft | Six Vans are listed with plates |
| FR-28 | The system shall record Workshop Servicing dates, during which a Van is unavailable all day. The rotation: in odd months Vans 1, 2 and 3 go on the 1st, 11th and 21st, and in even months Vans 4, 5 and 6 go on the same dates. A date that falls on a Sunday or public holiday moves to the next working day | Brief §Company ¶5; INT-MGR [Process Q3] | Must | Draft (manual entry vs generated: §6, DEC-14) | Check a month where the 11th is a Sunday: the servicing must move to Monday the 12th. The Van cannot be crewed that day |
| FR-29 | The Manager shall be able to mark a Van unavailable for a date range (e.g. breakdown). Jobs assigned to that Van in the range shall become Unassigned Jobs | INT-MGR [Conflicts Q4]; INT-DRV [Q8] | Must | Draft | Mark a Van unavailable and confirm its Jobs appear in the Unassigned list |
| FR-30 | The Manager shall form a Crew for each Van on each working day. A Crew is exactly one Driver plus one or two Technicians (2–3 people). A Crew stays fixed for the day | Brief §Company ¶3–4; INT-MGR [Process Q1], [Clarification Q4 follow-up] | Must | Draft | Try a Crew with 0 Drivers, 2 Drivers, 0 Technicians or 3 Technicians. All must be refused |
| FR-31 | The system shall not allow a Technician to be the Driver of a Crew | INT-MGR [Clarification Q3]; INT-DCT [Clarification Q1] | Must | Draft | Try to set a Technician as Driver. It must be refused |
| FR-32 | The Technicians of a Crew shall hold Certifications covering the Brand of every Job assigned to its Van that day. For Jobs of both Brands, that means either one dual-Brand Technician or one Technician per Brand | Brief §Company ¶2–3; INT-MGR [Process Q1 follow-up: ordering], [Process Q2]; INT-DCT [Conflicts Q1 follow-up] | Must | Draft | Decision-table candidate for M2 black-box testing: Brands on the Van × Technician Certifications |
| FR-33 | The Manager shall be able to change the current day's Crew in an emergency, and the affected Staff shall be notified | INT-MGR [Clarification Q4 follow-up]; INT-DRV [Q7] | Must | Draft | Swap a Technician mid-day and confirm both Staff are notified and FR-32 is re-validated |

### 3.7 Jobs

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-34 | The Manager shall be able to create a Job. It records: customer name, customer phone, address (including unit number) and postal code, Brand, Job Type (Installation or Servicing), number of units, aircon model (optional), preferred date, preferred Slot, and notes (e.g. parking, lift access) | INT-MGR [Process Q2]; INT-DCT [Process Q1 follow-up: job info]; INT-DRV [Q2] | Must | Draft | Create a Job with only the optional fields left blank. It saves. Leave out any required field and it is refused |
| FR-35 | The system shall pre-fill a Job's duration from its Standard Duration (Servicing 1 h per unit, Installation 3 h per unit), and the Manager shall be able to adjust it | INT-MGR [Process Q2 follow-up: hours], [Clarification Q5 follow-up]; INT-DCT [Clarification Q3 follow-up] | Must | Draft | 2 Installation units pre-fill 6 h. Edit it to 7 h and confirm it saves |
| FR-36 | Each Job shall have exactly one Brand. A customer with units of both Brands is recorded as two Jobs at the same address, and the Crew sees them together | INT-MGR [Process Q2]; INT-DCT [Process Q1 follow-up: job info] | Must | Draft | Create two Jobs at one address and confirm the Staff view groups them |
| FR-37 | The Manager shall be able to update or cancel a Job. If the Job is assigned, the Crew shall be notified | INT-MGR [added follow-up: cancellations] | Must | Draft | Cancel an assigned Job and confirm the Crew is notified and the Job leaves their list |
| FR-38 | The system shall track each Job's status as at least Unassigned, Assigned, Completed or Cancelled | INT-MGR [Conflicts Q3], [Conflicts Q4], [added follow-up: cancellations], [Process Q1 follow-up: completion] | Must | Draft | Take a Job through each transition |
| FR-39 | A Crew member shall be able to mark an assigned Job Completed, recording the actual start and end times, a short remark, and whether a follow-up visit is needed | INT-DCT [Process Q1 follow-up: completion]; INT-MGR [Process Q1 follow-up: completion] | Must | Draft (see DEC-40) | Complete a Job and confirm all four fields are stored. End time before start time must be refused |
| FR-40 | When marking a Job Completed, the Crew shall be able to attach a photo of the invoice signed by the customer | INT-MGR [Process Q1 follow-up: completion] | Should | Draft (see DEC-40) | Attach a photo from a phone camera |

### 3.8 Job Allocation

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-41 | The Manager shall allocate Jobs one Planning Week at a time, by assigning each Job to a Van (and its Crew) on a date | Brief R3; INT-MGR [Process Q1], [Clarification Q6] | Must | Draft | Allocation is restricted to a single Planning Week |
| FR-42 | The Manager shall be able to set the order and time of Jobs within a Van's day | INT-DRV [Q5]; INT-MGR [Process Q2] (preferred Slot) | Should | Draft | Reorder two Jobs and confirm the Staff view reflects the new order |
| FR-43 | On the Job Allocation page, the Manager shall be able to select up to three Staff and compare them side by side. For each, show: Availability that day and week, Workload so far this week, Certifications, Job Preference, and location that day. Location is the area of their other Jobs that day, not GPS | Brief R4, R5; INT-MGR [System Q3] | Must | Draft | Selecting a 4th Staff member is refused. All five items are shown for each selected person |
| FR-44 | The system shall **block** an allocation or Crew change that would create any of these: a Technician without Certification for a Job's Brand; a double booking; Staff on Leave or unavailable in that Slot; a Van without a valid Crew; a Van that is unavailable (Workshop Servicing or breakdown); or a Sunday or public holiday | INT-MGR [System Q4], [Process Q3], [Clarification Q8] | Must | Draft | One negative test per rule. Decision-table candidate for M2 |
| FR-45 | The system shall **warn**, and let the Manager override, when an allocation would cause any of these: a Staff member exceeds 40 hours of Workload in the Planning Week; a Job Preference is not met; or fewer than 3 Vans are crewed on a Monday–Saturday working day | Brief §Company ¶4, R6; INT-MGR [System Q4], [Conflicts Q1] | Must | Draft | Trigger each warning, override it, and confirm the allocation saves |
| FR-46 | The system shall list the Unassigned Jobs and show how many there are | INT-MGR [Conflicts Q1], [System Q1 follow-up: ranking] | Must | Draft | Cancelling an Assignment increments the count |
| FR-47 | For each working day, the system shall show Staff who marked themselves available but have no Assignment | INT-MGR [Conflicts Q2 follow-up: standby] | Should | Draft | Seed one available, unallocated person and confirm they are listed |
| FR-48 | For an Unassigned Job, the system shall suggest Staff who are available, qualified and have the lowest Workload that week. The Manager chooses who to assign | INT-MGR [Conflicts Q2 follow-up: staff cancellation] | Should | Draft | The suggestion list excludes unqualified and unavailable Staff and is sorted by ascending Workload |
| FR-49 | The Manager shall be able to publish the Weekly Roster even when warnings are outstanding. Publishing notifies all affected Staff | INT-MGR [Process Q1], [Conflicts Q1], [added follow-up: notifications] | Must | Draft | Publish with a "fewer than 3 Vans" warning open. It succeeds and Staff are notified |
| FR-50 | After publication, the Manager shall be able to change Assignments, e.g. add a last-minute Job or reassign one. Affected Staff shall be notified | INT-MGR [Conflicts Q5], [Conflicts Q2 follow-up: staff cancellation] | Must | Draft | Add a Job to a published day and confirm the Crew is notified and Workload updates |
| FR-51 | The system shall show a weekly timeline with one row per Van, showing its Crew and Jobs | INT-MGR [System Q2] | Must | Draft | Six rows are shown for a Planning Week |

### 3.9 Workload and Landing Pages

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-52 | A Job's Planned Hours shall be its duration (FR-35) plus a 30-minute Travel Allowance. Breaks are not counted | INT-MGR [Clarification Q7], [Clarification Q5 follow-up]; INT-DCT [System Q1] | Must | **Blocked** (DEC-31) | A 1-unit Servicing Job gives 1.5 h |
| FR-53 | A Technician's Workload shall be the sum of the hours of the Jobs assigned to them. A Driver's Workload shall equal the hours of the Van they are on | INT-MGR [Clarification Q5 follow-up], [Clarification Q7] | Must | **Blocked** (DEC-39) | Depends on how Technician hours are counted on mixed or 3-person Vans |
| FR-54 | When a Job is Completed, its Actual Hours shall replace its Planned Hours in Workload | INT-MGR [Clarification Q7], [Conflicts Q5]; INT-DCT [Conflicts Q3] | Must | **Blocked** (DEC-40) | Depends on whether the Travel Allowance still applies to Actual Hours |
| FR-55 | Workload shall be calculated per Planning Week (Monday–Saturday). Workload **above** 40 hours is Overtime and shall be highlighted | Brief R6; INT-MGR [Clarification Q7], [Conflicts Q5] | Must | Draft | Boundary test: 40.0 h is not highlighted, 40.5 h is. Black-box candidate |
| FR-56 | The Manager's Landing Page shall show: this week's Workload for every Driver and Technician as a bar chart with a line at 40 hours, with Overtime highlighted; the three-lowest lists (FR-57); today's Vans and Crews; the number of Unassigned Jobs; and pending requests (Leave Requests, Late Availability Change Requests and Job Rejections) | Brief R2, R6; INT-MGR [System Q1 follow-up: landing page], [System Q2] | Must | Draft | Seed data covering each element and confirm all are visible on first load |
| FR-57 | The Landing Page shall show the three Technicians and the three Drivers with the lowest Workload this week, as **separate** lists, excluding Staff on Leave that week | Brief R6; INT-MGR [added follow-up: lowest three] | Must | Draft (ties and "on Leave that week": §6, DEC-05) | Put one Technician on Leave with the lowest hours. They must not appear |
| FR-58 | The Staff Landing Page shall show: a weekly calendar of their Assignments by day, with times and addresses; their total hours for the week against 40; their total hours for the month; and their Leave balance | Brief R7; INT-DCT [System Q2]; INT-DRV [Q13], [Q1] | Must | Draft ("month" definition: §6, DEC-04) | Seed a week of Jobs and check the totals |
| FR-59 | For each Assignment, Staff shall see: customer name and phone, address and postal code, Brand, model, number of units, Job Type, time Slot, notes, Van number and licence plate, and Crew members' names | INT-DRV [Q2], [Q1]; INT-DCT [Process Q1 follow-up: job info] | Must | Draft | All fields are visible on a phone-width screen |
| FR-60 | The Manager shall be able to view, per Staff member, hours this week and this month, and Leave taken and remaining. The Manager shall also see the number of Jobs completed per month | INT-MGR [System Q1], [System Q1 follow-up: ranking] | Should | Draft | Totals match the seeded data |
| FR-61 | The Manager shall be able to view how many days each Van was on the road in a month | INT-MGR [System Q1], [System Q1 follow-up: ranking] ("nice to have") | Could | Draft | Totals match the seeded Crews |

### 3.10 Job Rejection

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-62 | Staff shall be able to reject a Job assigned to them. Before confirming, the system shall warn them to discuss it with the Manager first. The Staff member must choose a reason: Personal emergency; Clash with another job; Not qualified or missing equipment; or Other, with a comment box. Telling the company ahead of time that a Job cannot be done uses this same function | Brief R10, §Intro ¶3; INT-MGR [Conflicts Q3], [added follow-up: early rejection]; INT-DCT [Process Q2], [Conflicts Q2]; INT-DRV [Q17] | Must | Draft | Cancel at the warning and confirm nothing changes. Try to confirm without a reason, which must fail. The Manager's "at least 48 hours' notice" preference has no system rule yet (**TBC**) |
| FR-63 | A confirmed rejection needs no approval. The Job leaves the Staff member's list and becomes an Unassigned Job. The Manager is notified immediately, and the Staff member sees a confirmation | INT-MGR [Conflicts Q3]; INT-DCT [Process Q2 follow-up: after reject] | Must | Draft (effect on the rest of the Crew: DEC-15) | After a rejection, the Job is in the Unassigned list, the Manager has a notification and the Staff member has a confirmation |

### 3.11 Notifications

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-64 | Staff shall be notified on their Landing Page and by email when: the Weekly Roster is published; one of their Assignments is added, changed or cancelled; their Crew changes; or a decision is made on their Leave Request or Late Availability Change Request | INT-MGR [added follow-up: notifications], [Conflicts Q5], [added follow-up: cancellations]; INT-DCT [Process Q1 follow-up: updates], [Conflicts Q2]; INT-DRV [Q7] | Must | Draft | One test per trigger, checking both channels |
| FR-65 | The Manager shall be notified on their Landing Page of new Job Rejections, Leave Requests and Late Availability Change Requests | INT-MGR [Conflicts Q3], [System Q1 follow-up: landing page] | Must | Draft | Each request type appears under pending requests. Whether the Manager also gets email is **TBC** |

### 3.12 Audit and records

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-66 | The system shall keep an audit log of account detail changes, password change requests and all schedule changes (Availability, Crews, Assignments), recording who made each change, what it was and when | INT-ITA [Q: Audit] | Should | Draft | Make each change type and confirm a log entry. Who can view the log is **TBC** (assumed IT Administrator) |
| FR-67 | Schedule records dated in the past or currently in progress shall not be deletable. Future ones may be deleted | INT-ITA [Q: Retention] | Should | Draft (see DEC-34) | Try to delete yesterday's Assignment, which must be refused. Deleting next week's is allowed |
| FR-68 | The system shall import existing schedules from a CSV export | INT-ITA [Q: Existing systems] | Could | **Blocked** (DEC-36) | Conflicts with the Manager's statement that there is no other system to import from |

---

## 4. Non-functional requirements

| ID | Category | Description (with measurable criterion) | Source / justification | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| NFR-01 | Performance | Main user actions (saving Availability, an Assignment or a request, or loading a Landing Page) shall respond within **5 seconds**, under the load in NFR-03 | INT-ITA [Q: Response time] ("maybe 3 or 5 seconds"); Brief R2 ("immediately") | Should | Draft (3 s vs 5 s: confirm) | Load test with 50 simulated users. The percentile used (e.g. 95th) is **†TBC** |
| NFR-02 | Performance | A saved change shall be visible to other users within **1 minute** | INT-ITA [Q: Response time] ("less than a minute or so") | Should | Draft | Save as the Manager and time how long until it appears in a Staff session |
| NFR-03 | Capacity | The system shall support at least **50 concurrent users**, including one person logged in on several devices | INT-ITA [Q: Concurrency]; Brief §Company ¶4 (17 Staff) | Must | Draft | Load test at 50 sessions |
| NFR-04 | Security | The system shall rate-limit requests per user to prevent high request volumes | INT-ITA [Q: Concurrency] | Should | Draft | Limit **†TBC**. Exceed it and confirm the requests are throttled |
| NFR-05 | Availability | The system shall be available 24/7. Scheduled maintenance happens only early morning or late night, avoiding the peaks (Monday early morning, Thursday) | INT-ITA [Q: Hours], [Q: Outage] | Must | Draft | Uptime target (%) and exact maintenance window are **†TBC** |
| NFR-06 | Recoverability | After a failure, the service shall be restored within **24 hours** | INT-ITA [Q: Outage] ("Not more than one day"), [Q: Restore] | Must | Draft | Restore drill from backup, timed |
| NFR-07 | Recoverability | No more than **1 hour** of data may be lost, so backups shall run at least hourly | INT-ITA [Q: Restore] ("losing an hour of schedule updates is not very impactful"), [Q: Outage] ("updated every hour or so") | Must | Draft | Check the backup schedule. Restore and compare against the pre-failure data |
| NFR-08 | Reliability / offline | Staff shall be able to view today's Assignments without a network connection. Updates made while offline are submitted once the connection returns | INT-DCT [System Q3]; INT-ITA [Q: Outage], [Q: Connection failure] | Should | Draft | In airplane mode, today's Jobs remain viewable. A completion entered offline syncs on reconnect |
| NFR-09 | Reliability | If a submission fails, the system shall keep it and retry. If it still cannot be saved, the system shall tell the user it failed and advise them to try again or contact the IT Administrator | INT-ITA [Q: Connection failure] | Should | Draft | Cut the network mid-submit and confirm the retry or the error message |
| NFR-10 | Security | Login shall use two-factor authentication through an email confirmation | INT-ITA [Q: Safeguards] ("would be good") | Should | Draft (see DEC-41) | Login is not completed until the email confirmation is done |
| NFR-11 | Security | Staff personal data and schedule data shall be encrypted at rest | INT-ITA [Q: Safeguards] | Must | Draft | Inspect storage: fields are not readable in plain text. Encryption in transit (HTTPS) is recommended but no stakeholder stated it |
| NFR-12 | Security | Access shall be role-based. Staff view and edit only their own Availability, Job Preference, Leave and Assignments. Managers view and edit all Staff schedules. Only the IT Administrator manages accounts and permissions | INT-ITA [Q: Onboarding], [Q: Permissions] | Must | Draft (colleague visibility: DEC-37) | Access-control test matrix: role × page × action |
| NFR-13 | Data retention | Schedule records shall be kept for at least **1 year** for yearly reviews | INT-ITA [Q: Retention] | Must | Draft (see DEC-34) | Confirm a record from 12 months ago is still retrievable |
| NFR-14 | Compatibility | The system shall work on current versions of Chrome (the priority), Edge, Firefox and DuckDuckGo | INT-ITA [Q: Devices] | Must | Draft | Cross-browser test of the main user flows |
| NFR-15 | Compatibility / usability | All Staff functions shall be usable on a smartphone, including Android, and on a tablet. The Manager's functions shall be usable on a laptop | INT-DCT [System Q3]; INT-DRV [Q14]; INT-ITA [Q: Devices] | Must | Draft | Test at phone width (**†**e.g. 360 px) with no horizontal scrolling on Staff pages |
| NFR-16 | Usability | The interface shall be simple enough for non-technical Staff | INT-MGR [Closing] ("Just keep it simple. Most of my staff aren't very technical.") | Must | Draft | Measurable target **†TBC**, e.g. a first-time user submits a week's Availability without help in under 3 minutes |
| NFR-17 | Constraint | The system shall be a web application | Brief R1 | Must | Draft | Runs in a browser with no install |

---

## 5. Coverage check: Brief initial requirements

| Brief | Summary (see brief for exact text) | FR / NFR IDs | Open DECs |
|---|---|---|---|
| R1 | Web-based | NFR-17, NFR-14 | — |
| R2 | Manager Landing Page shows staff workload | FR-56, NFR-01 | — |
| R3 | Allocate jobs one week at a time | FR-41 | — |
| R4 | Allocation page: up to three staff availability | FR-43 | — |
| R5 | Availability display: workload, preference, location, week availability | FR-43, FR-21 | — |
| R6 | Three lowest workload; highlight >40 hours | FR-55, FR-56, FR-57 | DEC-05 (ties) |
| R7 | Staff Landing Page: weekly assignments and monthly workload | FR-58, FR-59 | DEC-04 ("month") |
| R8 | Add/edit availability up to **1 month in advance** (the brief's "5 weeks" is superseded by the lecturer, DEC-01) | FR-13, FR-14 | DEC-30 |
| R9 | Weekly job preference | FR-21 | DEC-07 (deadline) |
| R10 | Reject jobs with warning | FR-62, FR-63 | DEC-15 (crew effect) |
| R11 | IT administrators add staff and managers | FR-01–FR-04, FR-08 | DEC-34, DEC-35, DEC-36 |

Every Brief requirement maps to at least one FR or NFR.

## 6. How the interviews bear on the open DECs

This section is for the team, to help close DECs. The DEC statuses in `decisions.md` are **unchanged**. Deciding them is the team's call.

| DEC | Answered by | What the interviews say | Still open | FRs |
|---|---|---|---|---|
| DEC-02 Availability Deadline | INT-MGR [Clarification Q6 follow-up], [Conflicts Q2] | Wednesday 18:00, 12 days before the week. Availability locks, and later changes become requests | — | FR-16, FR-17 |
| DEC-03 Availability granularity | INT-MGR [Clarification Q4]; INT-DCT [Clarification Q2] | Half-day Slots | Default (available or unavailable?) and whether entries can be deleted | FR-13 |
| DEC-04 Workload and the 40-hour period | INT-MGR [Clarification Q7] | Week is Monday–Saturday, above 40 h is Overtime, Travel Allowance applies | "Month" in R7 (calendar month?) | FR-52–FR-55, FR-58 |
| DEC-05 Top three | INT-MGR [added follow-up: lowest three] | Drivers and Technicians listed separately, Staff on Leave excluded | Tie-breaking. Does one Leave day exclude someone for the whole week? | FR-57 |
| DEC-06 Up to three staff | INT-MGR [System Q3] | The Manager selects up to three Staff to compare | — | FR-43 |
| DEC-07 Job Preference | INT-MGR [Process Q1 follow-up: ordering]; INT-DCT [Clarification Q4]; INT-DRV [Q10] | Area, time or days and Job Type, used as a tie-breaker | Preference deadline | FR-21 |
| DEC-08 Location | INT-MGR [System Q3] | Area of the Staff member's scheduled Jobs, no GPS | — | FR-43 |
| DEC-09 Van composition | INT-MGR [Process Q1 follow-up: ordering], [Clarification Q3], [Clarification Q4 follow-up]; INT-DCT [Conflicts Q1 follow-up] | One DCT can cover both Brands. Technicians never drive. The Crew is fixed for the day | — | FR-30–FR-32 |
| DEC-10 Unit of assignment | INT-MGR [Process Q1] | Crews are built first, then Jobs are allocated to Vans | — | FR-30, FR-41 |
| DEC-11 Job definition | INT-MGR [Process Q2], [Process Q2 follow-up: hours] | The Manager enters Jobs manually. Field list and Standard Durations given | — | FR-34–FR-36 |
| DEC-12 Working days | INT-MGR [Clarification Q8], [Clarification Q4] | Monday–Saturday, 09:00–18:00, closed Sundays and public holidays | — | FR-09, FR-13, FR-44 |
| DEC-13 Leave | INT-MGR [Process Q4] | Requested in the system, approved by the Manager, 7 days per calendar year, no carry-over. Sick leave is marked by the Manager | Half-day Leave? | FR-22–FR-25, FR-18 |
| DEC-14 Workshop Servicing | INT-MGR [Process Q3], [Conflicts Q4] | Fixed rotation. Breakdowns are handled manually | Are servicing dates generated by the system or entered? | FR-28, FR-29 |
| DEC-15 Job Rejection | INT-MGR [Conflicts Q3], [added follow-up: early rejection] | Reason required, warning shown, no approval, Job becomes Unassigned, Manager notified | What happens to the rest of the Crew. How the 48 h notice is enforced | FR-62, FR-63 |
| DEC-16 Allocation horizon | INT-MGR [Clarification Q6], [Conflicts Q5] | The Manager views 1 month ahead but allocates and publishes one week at a time. Post-publication changes are allowed | — | FR-41, FR-50 |
| DEC-17 IT Administrator | INT-ITA; INT-MGR [Clarification Q2] | A distinct actor who creates accounts, manages roles and permissions, and handles lockouts | Delete vs deactivate (DEC-34) | FR-02–FR-09 |
| DEC-18 Roles | INT-MGR [Clarification Q1] | The Manager is not Staff, has no Availability and no Workload | Multiple Managers? Other administrative staff? | FR-01, FR-20 |
| DEC-19 Rule enforcement | INT-MGR [System Q4], [Conflicts Q1] | Block / warn split given | — | FR-44, FR-45 |
| DEC-20 Hours engaged | INT-MGR [Clarification Q7]; INT-DCT [Process Q1 follow-up: completion] | Completion records actual times, and Actual Hours replace Planned Hours | See DEC-40 | FR-39, FR-54 |
| DEC-22 Job volume and duration | INT-MGR [Process Q2 follow-up: hours], [Process Q2 follow-up: advance] | Standard Durations. Bookings are usually 1–2 weeks ahead, rarely more than 4 | — | FR-35 |

Rubric DECs (21, 23–29) and DEC-30 are not affected by the interviews.

## 7. Source conflicts (new DEC entries)

These conflicts were found while drafting and are logged as **open** in [decisions.md](decisions.md). The affected rows are marked `Blocked` or carry a DEC reference.

| DEC | Conflict | Affects |
|---|---|---|
| DEC-31 | Travel time: a fixed 30-minute allowance (Manager) vs estimated driving time correlated with mileage logs (Driver) | FR-52 |
| DEC-32 | Overtime: "automatically flagged for approval" (Driver) vs a highlight plus an overridable warning with no approval step (Manager) | FR-45, FR-55 |
| DEC-33 | Real-time delay reporting by the Crew in the system (Driver) vs phone calls (Manager, DCT) | not included |
| DEC-34 | Leavers: "delete their account ... those should be removed" vs "Deletion of past or currently happening schedules should not be possible" (both from the IT Administrator) | FR-05, FR-67, NFR-13 |
| DEC-35 | Who maintains Certifications and staff details: the IT Administrator alone vs the Manager | FR-10, FR-11 |
| DEC-36 | Manual account creation vs CSV import (both from the IT Administrator). Schedule import (IT Administrator) vs "no other system to import from" (Manager) | FR-08, FR-68 |
| DEC-37 | What Staff may see about colleagues: "only ... the names and emails" (IT Administrator) vs the Manager's side-by-side comparison | NFR-12 |
| DEC-38 | "Thursday since they can start scheduling their slots then" (IT Administrator) vs Availability due Wednesday with Manager planning on Thursday | NFR-05 peak assumptions |
| DEC-39 | Technician Workload on a mixed-Brand or 3-person Van: only their own Jobs, or the whole Van day like the Driver? | FR-53 |
| DEC-40 | Actual Hours: does the Travel Allowance still apply? Who records completion? Is the invoice photo required? | FR-39, FR-40, FR-54 |
| DEC-41 | Email 2FA on every login vs "Just keep it simple" and the offline use in the field | NFR-10, NFR-08 |

## 8. Gaps to raise before M1

- **Stakeholder count:** Appendix A requires at least 5 Stakeholder Representatives. There are 4 transcripts (Manager, DCT, Driver, IT Administrator). `document-analysis.md` lists questions for a Single-Brand Technician (SBT), but there is no SBT transcript in the repo.
- **Interview metadata:** date, interviewer and interviewee are TBC for all four interviews, and the report needs attendance records ([elicitation/README.md](elicitation/README.md)).
- **Missing measurable targets:** every **†** threshold above needs a stakeholder-confirmed value, because the rubric requires each NFR to be "measurable and justified".
