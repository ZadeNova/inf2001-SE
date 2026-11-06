# Software Requirements Specification: Aircon Service Workload Management System

> **Version 3.5 (2026-11-07), M1 submitted baseline.** This version aligns the repo with §2.2 of the **submitted M1 report** (INF2001 P8-1 M1 Report, 9 October 2026), which the team made the M1 source of truth (DEC-72). Requirement IDs, wording, groupings and priorities follow the report exactly. The repo adds the Source and Test columns, which the report does not print.
> **Renumbering:** the report numbers requirements by process area, so the repo IDs from SRS v3.4 changed. §9 maps every v3.4 draft ID to its report ID. Draft IDs that were withdrawn before submission are not part of the report and have no report ID. From this baseline on, IDs are never reused or renumbered (DEC-72).
> **Change control:** any later requirement or use-case change needs a new DEC entry and a version bump.
> 50 active functional requirements and 12 active non-functional requirements, aligned with UC-01 to UC-15.
> Priorities use MoSCoW. Brief R1–R11 are the minimum deliverable, so they are always `Must`.
> **†** marks a numeric threshold chosen by the team rather than stated by a stakeholder.

---

## 1. Introduction

### 1.1 Purpose

This SRS specifies the functional and non-functional requirements of a web-based workload management system for the aircon service team of an aircon retailer. It matches §2.2 of the submitted Milestone 1 report (INF2001 P8-1 M1 Report, 9 October 2026), which is the M1 source of truth (DEC-72).

### 1.2 Scope

The system lets the **Manager**:
- record Jobs
- form a daily Crew for each Van, name each day's Standby Staff, allocate Jobs one Planning Week at a time and publish the Weekly Roster
- see Availability and Workload at a glance up to 1 month in advance
- decide Leave Requests, Late Availability Change Requests and Job Rejection Requests.

It lets **Staff** (Drivers and Technicians):
- enter Availability, Job Preferences and Leave Requests
- see their published Assignments and Workload
- record Job completion (Technicians)
- request to reject a Job (the Manager decides).

It lets the **IT Administrator** manage accounts, roles and the audit log.

**Out of scope**, with the source for each exclusion:

| Excluded | Source |
|---|---|
| Wages, job costs, payroll and commission. The pay model (basic salary and shifts, plus per-Job commission for Technicians) is background only | INT-MGR [System Q1]; DEC-44 |
| Live GPS tracking | INT-MGR [System Q3]; DEC-08 |
| Customer self-booking | INT-MGR [Process Q2] |
| Sunday emergency jobs | INT-MGR [Clarification Q8]; DEC-45 |
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
| **Availability Deadline** | 18:00 on the Wednesday 12 days before a Planning Week's Monday. After it, that week's Availability and Job Preference are locked | DEC-02 |
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
| **Standby** | A Staff member named by the Manager to back up a working day's Jobs. Not in any Crew that day. Counts 0 h of Workload unless placed into a Crew | DEC-43 |
| **Job Rejection Request** | A Crew member's request to take a Job off their Van. The Manager approves or refuses it | DEC-42 |
| **Short notice** | A Job Rejection Request made less than 48 hours before the Job starts | DEC-42 |

### 1.4 Sources and citation format

| Citation | Source |
|---|---|
| `Brief R<n>` / `Brief §<section> ¶<n>` | [brief/project-description.md](brief/project-description.md), including its Lecturer clarifications |
| `DEC-nn` | [decisions.md](decisions.md) |
| `INT-MGR [<label>]`, `INT-DCT [<label>]` | Interview transcripts in [elicitation/interviews/](elicitation/interviews/). Historical DCT transcript tags remain historical evidence. Current `INT-DCT [Questionnaire <question>: <response ID>]` citations resolve to [the Technician questionnaire](elicitation/interviews/technician-questionnaire.md) and its linked primary Sheet; an omitted response ID covers that question across both roles |
| `INT-DRV [Q<n>]` | Driver transcript, numbered questions |
| `INT-ITA [Q: <topic>]` | IT Administrator transcript, cited by question topic |
| `M1 Report §<n>` | The submitted M1 report (9 Oct 2026). Requirement wording and IDs follow it exactly (DEC-72) |

---

## 2. Overall description

### 2.1 User classes

| User class | Description | Source |
|---|---|---|
| **Manager** | Office-based. May be more than one account, all with identical permissions. Has no Availability, Leave or Workload in the system | INT-MGR [Clarification Q1]; DEC-18 |
| **Driver** (Staff) | 6 in total. The only role allowed to drive. Uses a phone or the van tablet | Brief §Company ¶4; INT-MGR [Clarification Q3]; INT-DRV [Q14] |
| **Technician** (Staff) | 11 in total: 2 dual-Brand, 5 M Electric only, 4 Dicon only. A Brand Certification covers both Installation and Servicing. Respondents use Android or iOS phones; browser support follows NFR-11 | Brief §Company ¶4; INT-MGR [Clarification Q5]; INT-DCT [Questionnaire C18/C19] |
| **IT Administrator** | Manages accounts, roles, lockouts and the audit log | Brief R11; INT-ITA; DEC-17; DEC-45 |

### 2.2 Operating environment

- Browsers: Chrome is the priority; Edge, Firefox and DuckDuckGo must also work.
- Devices: company laptops and tablets, and modern phones.
- Field use has patchy signal in basements and car parks.

Sources: INT-ITA [Q: Devices]; INT-DCT [Questionnaire C18/C19].

### 2.3 Constraints

- The system is a web application (Brief R1).
- Operations run Monday–Saturday, 09:00–18:00. The company is closed on Sundays (DEC-12; DEC-45).
- Current fleet and headcount: 6 Vans, 6 Drivers and 11 Technicians (Brief §Company ¶3–4). The fleet size is data, not a hard limit.

### 2.4 Weekly cycle

Example for the Planning Week starting Monday the 19th:

| Step | When |
|---|---|
| Staff enter Availability and Job Preference | Any time within the 1-month window |
| Availability Deadline (the week locks) | Wednesday the 7th, 18:00 |
| Manager plans: Crews and Standby first, then Jobs | From Thursday the 8th (the roster is Draft) |
| Manager publishes | Monday the 12th (Staff are notified) |
| The week runs | Monday the 19th to Saturday the 24th |

Sources: INT-MGR [Clarification Q6 follow-up]; DEC-02; DEC-16; DEC-43.

### 2.5 Design principle: Staff submit, the Manager decides

Staff inputs are one of three kinds:
- **declarations:** Availability, until the Availability Deadline
- **advisory information** the Manager sees while allocating: Job Preference
- **requests** the Manager decides case by case: Leave Requests, Late Availability Change Requests and Job Rejection Requests.

Staff set their own Availability while a week is open. For a locked week, they submit a Late Availability Change Request for the Manager to decide. The Manager has no separate operation to overwrite Staff Availability (DEC-45).

The final decision on anything that changes the Weekly Roster rests with the Manager (DEC-42).

---

## 3. Functional requirements

The requirements are grouped by process area, as in the report (Tables 2.4–2.10).

### 3.1 Job and Weekly Roster management

*Report Table 2.4.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-01 | The Manager shall create a Job. Required: customer name, customer phone, address, postal code, Brand, Job Type (Installation or Servicing), number of units (≥1), preferred date (a working day) and preferred Slot. Optional: unit number, aircon model, notes | INT-MGR [Process Q2]; INT-DCT [Questionnaire C5]; INT-DRV [Q2]; DEC-11 | Must | Agreed | Required fields only → saved. Units = 0 → refused. Preferred date on a Sunday → refused |
| FR-02 | The Job's duration shall be pre-filled from its Standard Duration (Servicing 1 h per unit, Installation 3 h per unit). The Manager can adjust it | INT-MGR [Process Q2 follow-up: hours]; DEC-22 | Must | Agreed | 2 Installation units → 6 h pre-filled. Edited to 7 h → saved |
| FR-03 | Each Job has exactly one Brand. The Manager can link Jobs of different Brands at the same address. Linked Jobs must be allocated to the same Van on the same date, and Staff see them grouped | INT-MGR [Process Q2]; INT-DCT [Questionnaire C5]; DEC-11 | Must | Agreed | Allocate one of two linked Jobs to a different Van → blocked |
| FR-04 | The Manager shall be able to edit or cancel a Job that is not Completed. An edited, assigned Job is re-checked against FR-32. If it now breaks a rule, it becomes Unassigned and the Manager is told why. The Crew is notified of any change or cancellation | INT-MGR [added follow-up: cancellations]; DEC-19 | Must | Agreed | Change an assigned Job's Brand to one the Crew can't do → Job becomes Unassigned and a reason is shown. Cancel → Crew notified |
| FR-05 | Job status shall follow these transitions only: Unassigned → Assigned (allocation). Assigned → Unassigned (an approved Job Rejection Request, Van unavailable, invalidating edit, deactivated Staff or the Manager unassigning it). While a Job Rejection Request is pending, the Job stays Assigned. Assigned → Completed (FR-06). Unassigned or Assigned → Cancelled. Completed and Cancelled are final | INT-MGR [Conflicts Q3], [Conflicts Q4], [added follow-up: cancellations]; DEC-42; DEC-40 | Must | Agreed | Test each allowed transition. Completed → Cancelled → refused |
| FR-06 | A Technician on the Van's Crew shall mark an Assigned Job Completed. They shall record actual start and end time (end after start, both on the Job's date), a short remark, whether a follow-up visit is needed, and a required photo of the customer-signed invoice. An offline completion and its photo may be queued under NFR-05 | INT-DCT [Questionnaire C17/C18]; INT-MGR [Process Q1 follow-up: completion]; DEC-40; DEC-47 | Must | Agreed | Driver attempts completion → refused. End before start or missing invoice photo → refused. Valid submission → Completed |
| FR-07 | The Manager shall allocate Jobs one Planning Week at a time (the next unpublished week), assigning each Job to a Van with a Crew on a date within that week. The allocation view shall list Staff who are available and not already in a Crew for the selected day/Slot, marking anyone named as Standby | Brief R3; INT-MGR [Process Q1], [Clarification Q6], [Conflicts Q2 follow-up: standby]; DEC-10; DEC-16; DEC-43; DEC-47 | Must | Agreed | Date outside the Planning Week → refused. Available, uncrewed Staff → listed; named Standby → marked |
| FR-08 | The Manager shall set each Job's start time on the Van's day. Rules: Jobs run within 09:00-18:00 and skip lunch (13:00-14:00). A Job may span both Slots. Consecutive Jobs must be at least the 0.5 h Travel Allowance apart. Jobs on the same Van must not overlap | INT-DRV [Q5]; INT-MGR [Clarification Q4], [Clarification Q7]; DEC-12; DEC-31 | Should | Agreed | A 3 h Job at 11:00 runs 11:00–13:00, pauses for lunch and ends 15:00. A Job at 15:10 → refused (needs 15:30 or later) |
| FR-09 | Each Planning Week's Weekly Roster shall remain Draft until the Manager publishes it. The Manager sees Draft and Published rosters; Staff see Assignments only after publication. Publishing is refused while any FR-32 violation exists and allowed with FR-33 warnings outstanding. Every Staff member with Assignments or Standby days that week is notified | INT-MGR [Process Q1], [Conflicts Q1], [added follow-up: notifications]; DEC-16; DEC-19; DEC-43; DEC-47 | Must | Agreed | A Draft Assignment is hidden from Staff. Publish with a warning → allowed. Publish with an FR-32 violation → refused |
| FR-10 | After publication, the Manager shall be able to add, move or unassign Jobs and change Crews for current and future dates. Changes are re-checked (FR-32 and FR-33). The removed and added Staff are notified | INT-MGR [Conflicts Q5], [Conflicts Q2 follow-up: staff cancellation]; DEC-16 | Must | Agreed | Add a Job to a published day → Crew notified and Workload updated. Past dates → read-only |
| FR-11 | The system shall show a weekly timeline for a selected week, with one row per Van: its Crew and Jobs, and unavailable days shaded | INT-MGR [System Q2] | Must | Agreed | A Van on Workshop Servicing shows a shaded day |

### 3.2 Availability and Leave management

*Report Table 2.5.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-12 | Staff shall set each Slot (Morning or Afternoon) of each working day to Available or Unavailable, or set the whole day in one step (both Slots at once), and may clear an entry. A Slot with no entry is Not submitted and counts as unavailable for allocation | Brief R8; INT-MGR [Clarification Q4]; INT-DCT [Questionnaire C6]; DEC-03; DEC-45 | Must | Agreed | Set a whole day Available → both Slots Available. Set Morning = Available and leave Afternoon blank → allocation treats the afternoon as unavailable. Sunday Slots are not offered |
| FR-13 | Staff shall be able to enter or change Availability only for dates from today through the same calendar date next month, inclusive (clamped to that month's last day), and only before the Availability Deadline | Brief R8 + Lecturer clarification; DEC-01; DEC-30; DEC-02 | Must | Agreed | From 15 Mar: 15 Apr accepted, 16 Apr refused. From 31 Jan: 28 Feb accepted (non-leap year), 1 Mar refused |
| FR-14 | The Manager shall view the Availability of all Staff up to 1 month in advance (the FR-13 window) as a calendar grid, with Staff down the side and days across. Each cell shows one of five colour-coded states: available all day, morning only, afternoon only, on Leave, or unavailable / not submitted | Brief §Intro ¶4 + Lecturer clarification; INT-MGR [System Q2]; DEC-03 | Must | Agreed | Seed each state and check that each has a distinct colour and a legend |
| FR-15 | Availability and Job Preference for a Planning Week shall lock at 18:00 on the Wednesday 12 days before that week's Monday, in company local time | Brief §Company ¶1; INT-MGR [Clarification Q6 follow-up]; DEC-02; DEC-07 | Must | Agreed | Week of Mon 19th: an edit at Wed 7th 17:59 is accepted, an edit at 18:00 is refused |
| FR-16 | For a locked week, Staff shall submit a Late Availability Change Request to set or change one or more Slots, with a reason. The Manager approves or rejects it. Approval applies the change, and FR-29 applies if the change affects a Crew. Rejection leaves Availability unchanged. Staff see current Availability beside the proposed Slots and request status, with any supplied decision reason. The Staff member is notified either way | Brief §Company ¶1; INT-MGR [Conflicts Q2]; INT-DCT [Questionnaire C12/C13]; DEC-02; DEC-69 | Must | Agreed | Request without a reason → refused. Approve → Slot updated. Reject → unchanged. Both outcomes notify the Staff member |
| FR-17 | Staff shall be able to set a weekly Job Preference with optional fields: preferred area(s), preferred days, preferred Slot and preferred Job Type. It locks with Availability (FR-15). Preferences are advisory: they are shown in the comparison (FR-31), and violating one only raises a warning (FR-33) | Brief R9, R5; INT-DCT [Questionnaire C7]; INT-DRV [Q10]; INT-MGR [Process Q1 follow-up: ordering]; DEC-07 | Must | Agreed | Save a preference and see it in the comparison. Allocate against it → warning only. An empty preference is allowed |
| FR-18 | Staff shall submit a Leave Request for one or more full working days, with an optional note. A request cannot exceed the remaining balance or overlap an existing pending or approved request | Brief §Company ¶4; INT-MGR [Process Q4], [Process Q4 follow-up]; INT-DCT [Questionnaire C11]; DEC-13 | Must | Agreed | With 2 days left, a 3-day request → refused. An overlapping request → refused. A range including a Sunday deducts working days only |
| FR-19 | The Manager shall approve or reject a Leave Request. A rejection requires a reason. The Staff member is notified of the decision and any reason | INT-MGR [Process Q4], [Process Q4 follow-up]; DEC-13 | Must | Agreed | Reject without a reason → refused. Reject with a reason → Staff sees it |
| FR-20 | Approved Leave makes the Staff member unavailable on those days, and FR-32 blocks Assignments on them. If the person is already in a Crew on those days, the Manager is warned before approving, and on approval FR-29 applies | INT-MGR [Process Q4]; INT-DRV [Q15]; DEC-13; DEC-19 | Must | Agreed | Approve Leave for a Crew member → warning first. After confirming, they are removed from the Crew and the Van-day shows Needs attention |
| FR-21 | Each Staff member has 7 Leave days per calendar year, with no carry-over. Days are deducted on approval, and the remaining balance is shown to the Staff member and the Manager | Brief §Company ¶4; INT-MGR [Process Q4], [System Q1]; INT-DCT [Questionnaire C10/C11]; DEC-13 | Must | Agreed | Approve 2 days → balance 5. On 1 Jan the balance resets to 7 |

### 3.3 Certifications, Vans and Crews

*Report Table 2.6.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-22 | The system shall record each Technician's Certifications: Brand, certificate number and expiry date. A Technician may hold one or both Brands. The IT Administrator enters them at account creation, and the Manager maintains them afterwards. A Certification is valid for a Job when its expiry date is on or after the Job's date | Brief §Company ¶2, ¶4; INT-MGR [Clarification Q2 follow-up], [Clarification Q5]; DEC-35; DEC-19 | Must | Agreed | Expiry equal to the Job date → valid. Expiry the day before → invalid (FR-32 blocks it) |
| FR-23 | The system shall store each Van's number and licence plate. The Manager maintains the Van list | Brief §Company ¶3; INT-DRV [Q2]; DEC-14 | Must | Agreed | Six Vans are listed with plates. Adding a seventh is possible |
| FR-24 | The system shall generate Workshop Servicing dates from the rotation: odd months Vans 1, 2 and 3; even months Vans 4, 5 and 6; on the 1st, 11th and 21st respectively. A date that falls on a Sunday moves to Monday. The Van is unavailable all that day. The Manager may adjust a generated date. If servicing needs more than one day, the Manager records the extra days as Van unavailability (FR-25) | Brief §Company ¶5; INT-MGR [Process Q3]; DEC-14; DEC-45 | Must | Agreed | 11th = Sunday → servicing is on Monday the 12th. **White-box candidate for M2** |
| FR-25 | The Manager shall be able to mark a Van unavailable for a date range (e.g. breakdown). Its not-yet-completed Jobs in that range become Unassigned, its Crew for those days is released, and the Crew members are notified | INT-MGR [Conflicts Q4]; INT-DRV [Q8] | Must | Agreed | Completed Jobs are untouched. Assigned Jobs appear in the Unassigned list |
| FR-26 | For each Van that is to be on service on a working day, the Manager shall form a Crew of exactly one Driver and one or two Technicians. Only Staff with the Driver role may fill the Driver position; a Technician shall never drive. Each Crew member must be available for every Slot in which the Van has Jobs. A person may be in only one Crew per day. The Crew is fixed for the day, except under FR-28 | Brief §Company ¶3–4; INT-MGR [Process Q1], [Clarification Q3], [Clarification Q4 follow-up]; INT-DCT [Questionnaire D1/D2]; DEC-09; DEC-47 | Must | Agreed | 0 or 2 Drivers → refused. Technician as Driver → refused. 0 or 3 Technicians → refused. A Technician available Morning only on a Van with an afternoon Job → refused |
| FR-27 | Together, a Crew's Technicians shall hold valid Certifications (FR-22) for the Brand of every Job on the Van that day. For Jobs of both Brands, this means either one Dual-Certified Technician or one Technician per Brand | Brief §Company ¶2–3; INT-MGR [Process Q1 follow-up: ordering], [Process Q2]; INT-DCT [Questionnaire D2]; DEC-09 | Must | Agreed | **Black-box decision table for M2:** Brands on the Van × Technician Certifications × expiry |
| FR-28 | The Manager shall be able to change a Crew during the day in an emergency. The removed and added Staff are notified. Hours for Jobs already completed stay credited to whoever was on the Crew when each Job was completed | INT-MGR [Clarification Q4 follow-up]; INT-DRV [Q7]; DEC-39 | Must | Agreed | After a swap, the new Technician is credited only with the remaining Jobs. FR-26 and FR-27 are re-checked |
| FR-29 | When approved Leave, an approved Late Availability Change Request or a Certification expiry makes an existing Crew invalid, the system shall remove the affected person from that Crew for the affected dates, mark each affected Van-day Needs attention on the Manager's Landing Page, and notify the removed person and that day's eligible Standby Staff. The Manager decides the replacement. The Van's Jobs stay on the Van until the Manager fixes the Crew. A Van becoming unavailable is handled by FR-25 | DEC-19; DEC-43; INT-MGR [Process Q4], [Conflicts Q2]; DEC-45 | Must | Agreed | Approve Leave for the only Driver of a Van → Driver removed, Van-day flagged, Standby Driver notified, Jobs still on the Van |
| FR-30 | For each working day of the Planning Week, the Manager shall be able to name Standby Staff from those available for the whole day and not in any Crew that day. Full cover means at least one Standby Driver, plus Standby Technicians holding valid Certifications for both Brands (one Dual-Certified Technician, or one per Brand). Missing cover raises a warning (FR-33), not a block. Standby Staff back up every Job that day. They are notified when named (at publication, or immediately if the week is already Published) and when needed (FR-38, FR-29). Placing a Standby into a Crew removes them from Standby for that day. A Standby day counts 0 h of Workload unless the Standby is placed into a Crew | DEC-43; INT-MGR [Conflicts Q2 follow-up: standby] | Should | Agreed | Name someone who is in a Crew that day → blocked (FR-32). A day with no Standby Driver → warning. A Standby placed into a Crew → no longer Standby, and Workload counted from then |

### 3.4 Job Allocation and Workload

*Report Table 2.7.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-31 | On the Job Allocation page, the Manager shall select up to three Staff and compare them side by side for the Job's date and Planning Week. For each, show: Availability that day and week, Workload in that Planning Week, Certifications with expiry, Job Preference, and location that day (postal districts of their other Jobs, or "No Jobs") | Brief R4, R5; INT-MGR [System Q3]; DEC-06; DEC-08 | Must | Agreed | A 4th selection → refused. All five items are shown for each person |
| FR-32 | The system shall block any allocation, Crew change, Job edit or approval that would cause: an invalid or expired Certification for a Job's Brand (FR-27); a double booking (a person in two Crews on one day, a person both in a Crew and on Standby on one day, or overlapping Jobs on a Van); a Crew member unavailable, not submitted or on Leave for a Slot the Van works; an invalid Crew (FR-26); Linked Jobs split across Vans (FR-03); a Van that is unavailable; or a Sunday | INT-MGR [System Q4], [Process Q3], [Clarification Q8]; DEC-19; DEC-43; DEC-45; DEC-47 | Must | Agreed | One negative test per rule. **Black-box decision-table candidate** |
| FR-33 | The system shall warn, allow an override and log it, when an allocation or a publication would cause: a Staff member's Workload above 40 h in the Planning Week; a Job Preference not met; a Job starting outside the customer's preferred Slot; fewer than 3 Vans on service on a working day; or a working day without Standby cover (FR-30). Overtime has no approval step | Brief §Company ¶4, R6; INT-MGR [System Q4], [Conflicts Q1]; DEC-19; DEC-32; DEC-43 | Must | Agreed | Trigger each warning, override it, and see the override in the audit log (FR-49) |
| FR-34 | The system shall list the Jobs with status Unassigned and show their count. Cancelled Jobs are excluded | INT-MGR [Conflicts Q1], [System Q1 follow-up: ranking] | Must | Agreed | Approve a Job Rejection Request → count +1. Cancel an Unassigned Job → count −1 |
| FR-35 | Workload shall credit every Crew member with all Jobs on their Van that day. An Assigned Job contributes Planned Hours equal to its duration (FR-02) plus the 0.5 h Travel Allowance. A Completed Job instead contributes Actual Hours equal to actual end minus actual start plus 0.5 h. Breaks are excluded; Unassigned and Cancelled Jobs contribute zero | INT-MGR [Clarification Q7], [Clarification Q4 follow-up], [Conflicts Q5]; INT-DCT [Questionnaire C9], [Questionnaire C9]; DEC-31; DEC-39; DEC-40; DEC-47 | Must | Agreed | A 1 h Assigned Job contributes 1.5 h to every Crew member; if completed 10:00–11:30 it contributes 2 h instead |
| FR-36 | Workload is summed per Planning Week (Monday–Saturday). Workload strictly above 40 h is Overtime and is highlighted wherever Workload is shown | Brief R6; INT-MGR [Clarification Q7]; DEC-04 | Must | Agreed | **Boundary test:** 40.0 h → not highlighted, 40.5 h → highlighted |

### 3.5 Job Rejection Requests and notifications

*Report Table 2.8.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-37 | Any Crew member shall be able to submit a Job Rejection Request for a Job assigned to their Van in a Published week. Before submitting, the system warns them to discuss it with the Manager first. They must pick a reason: Personal emergency; Missing equipment or parts; or Other, which requires a comment. If the Job starts less than 48 hours after submission, a written explanation is also required and the request is marked Short notice. Telling the company ahead of time that a Job can't be done uses this same function | Brief R10, §Intro ¶3; INT-MGR [Conflicts Q3], [added follow-up: early rejection]; INT-DCT [Questionnaire C14/C15], [Questionnaire C15/C16]; INT-DRV [Q17]; DEC-42 | Must | Agreed | Cancel at the warning → nothing changes. "Other" with no comment → refused. A Job starting within 48 h: no explanation → refused; with one → submitted as Short notice. **Black-box decision-table candidate** |
| FR-38 | Every Job Rejection Request needs the Manager's approval, decided case by case. While it is pending, the Job stays Assigned, the Crew is still expected to do it, and the requester sees it as pending. Approved: the Job becomes Unassigned and leaves the whole Van, and the requester, the other Crew members and that day's Standby Staff are notified. Refused: the Assignment stands and the requester is notified. A request still pending when the Job starts lapses, and the Assignment stands | Brief R10; INT-MGR [System Q1 follow-up: landing page] (rejections listed as "pending requests"); DEC-42; DEC-43 | Must | Agreed | Pending → the Job is still in the Crew's list. Approve → the Job is in the Unassigned list and the Standby is notified. Refuse → the Job is unchanged. Still pending at the start time → lapsed |
| FR-39 | Staff shall be notified on their Landing Page and by email and phone when: a week containing their Assignments is published; one of their Assignments is added, changed, cancelled, or removed after an approved Job Rejection Request; they are added to or removed from a Crew; they are named as Standby, or someone they back up drops out; or a decision is made on their Leave Request, Late Availability Change Request or Job Rejection Request. Each message identifies the affected Job/request and date, saved outcome, relevant changed timing/Crew, any supplied decision reason and a link to current details | INT-MGR [added follow-up: notifications], [Conflicts Q5], [added follow-up: cancellations]; INT-DCT [Questionnaire C16], [Questionnaire C15/C16]; INT-DRV [Q7]; DEC-42; DEC-43; DEC-46; DEC-69 | Must | Agreed | One test per trigger, checking Landing Page, email and phone delivery for both the removed and added Staff |

### 3.6 Landing Pages and Assignment information

*Report Table 2.9.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-40 | The Manager's Landing Page shall show the current week by default and allow switching to the Planning Week. It shall show: every Driver's and Technician's Workload with a 40 h line and Overtime highlighted; separate lists of the three lowest-Workload Drivers and Technicians, excluding Staff with approved Leave and breaking ties by name; today's Vans, Crews and Standby Staff; the Unassigned Job count; pending Leave, Late Availability Change and Job Rejection Requests with Short-notice requests highlighted; Needs attention Van-days; Jobs made Unassigned by account changes; and Certifications expiring within 1 month. Alert items may be marked handled | Brief R2, R6; INT-MGR [System Q1 follow-up: landing page], [System Q2], [added follow-up: lowest three], [Clarification Q2 follow-up], [Conflicts Q3]; DEC-05; DEC-19; DEC-30; DEC-42; DEC-43; DEC-47 | Must | Agreed | Seed every element, Leave exclusion, tie and alert type; verify the dashboard and handled-state behaviour |
| FR-41 | The Staff Landing Page shall show: a weekly calendar of their Assignments and Standby days for the current week, switchable to the next Published week, with times, addresses and the status of any Job Rejection Request; their Workload for that week against 40 h; their Workload for the calendar month; and their Leave balance | Brief R7; INT-DCT [Questionnaire C10/C11]; INT-DRV [Q13]; DEC-04; DEC-16; DEC-42; DEC-43; DEC-47 | Must | Agreed | Seeded totals match. A Draft week is not selectable |
| FR-42 | For each Assignment, Staff shall see: customer name and phone, address, unit number and postal code, Brand, model, number of units, Job Type, start time, notes, Van number and licence plate, the Crew members' names and contact numbers, and any Linked Jobs | INT-DRV [Q1], [Q2]; INT-DCT [Questionnaire C5]; DEC-37 | Must | Agreed | All fields fit a 360 px-wide screen (NFR-11) |

### 3.7 Accounts and access

*Report Table 2.10.*

| ID | Description | Source | Priority | Status | Test / verification note |
|---|---|---|---|---|---|
| FR-43 | The system shall support three roles, each with its own Landing Page: Staff (subtypes Driver and Technician), Manager and IT Administrator | Brief R2, R7, R11; INT-ITA [Q: Permissions]; DEC-18 | Must | Agreed | Log in as each role and check that the correct Landing Page appears |
| FR-44 | The IT Administrator shall create Staff and Manager accounts. Required fields: name, email, contact number and role. Technician accounts also record their Certifications (FR-22). The account starts with an initial password that the user can change | Brief R11; INT-ITA [Q: Account info]; INT-MGR [Clarification Q2]; DEC-35 | Must | Agreed | Missing required field → refused. Duplicate email → refused. Valid → the user can log in and change the password |
| FR-45 | The IT Administrator shall be able to change a user's role, effective from the user's next login. If a Staff member becomes a Manager, their future Assignments are removed and those Jobs become Unassigned | INT-ITA [Q: Role change/leaver]; DEC-17 | Must | Agreed | Change a Driver with a future Assignment into a Manager. On next login they see the Manager page, and the Job is Unassigned |
| FR-46 | The IT Administrator shall be able to deactivate the account of a leaver. The user can no longer log in, their future Assignments are removed (those Jobs become Unassigned), and their past records are kept | INT-ITA [Q: Role change/leaver], [Q: Retention]; DEC-34 | Must | Agreed | Deactivate a user. Login fails, the future Job is Unassigned, and last month's Assignments are still visible to the Manager |
| FR-47 | A User shall be able to reset a forgotten password through a link sent to their company email. A successful reset shall atomically invalidate all outstanding password-reset tokens for that Account | INT-ITA [Q: Passwords]; DEC-71 | Should | Agreed | Request two reset emails; complete a reset with one link, then verify both links are unusable and the new password allows login. Concurrent reset attempts cannot commit with an invalidated token |
| FR-48 | An account shall lock after **5†** consecutive failed logins within **15 minutes†**. Only the IT Administrator can unlock it | INT-ITA [Q: Passwords]; DEC-17 | Should | Agreed | 4 failures → still usable. 5th failure → locked. IT Administrator unlocks → login works |
| FR-49 | The system shall log, with who, what and when: account and role changes, password change requests, and every change to Availability, Crews, Assignments, Jobs and Leave, including overridden warnings. Only the IT Administrator can view the audit log | INT-ITA [Q: Audit]; DEC-17 | Should | Agreed | Make each change type → log entry exists. Manager tries to open the log → refused |
| FR-50 | No user may delete records dated in the past or in progress. Jobs are Cancelled rather than deleted. Future Availability entries may be cleared (FR-12) | INT-ITA [Q: Retention]; DEC-34 | Must | Agreed | Try to delete yesterday's Job → no delete option exists. Cancelling a future Job is allowed |

### 3.8 Additional business rules

*Report §2.2.1, "Additional business rules".*

- Account deactivation and Staff-to-Manager changes also remove future Crew membership and mark affected Van-days Needs attention while ending future Assignments and making their Jobs Unassigned. Role changes take effect at the next login. (UC-04; FR-45, FR-46.)
- Invalidating Job edits and approved Job Rejection Requests also unassign active Linked partners. Cancellation only cancels the selected Job and unassigns its active Linked partners; Completed or already Cancelled partners remain unchanged. (UC-05, UC-09; FR-03–FR-05, FR-38.)
- A Workshop Servicing booking date with an existing Crew is blocked and a warning is shown, preserving the existing Assignments. (UC-06; FR-24.)
- Only one Pending Job Rejection Request is allowed per shared Assignment. Short notice means strictly less than 48 h; exactly 48 h is normal. A Job-start event lapses a request that is still Pending independently of Manager action, retains the Assignment and notifies the requester after the lapse is saved. (UC-09, UC-12; FR-37, FR-38.)
- Draft roster notifications are withheld from Staff on all channels. Notifications follow a saved business event; email or SMS failure does not undo that event. The phone-notification channel is SMS. (UC-15; FR-09, FR-39.)

---

## 4. Non-functional requirements

*Report Table 2.11.*

| ID | Category | Description (with measurable criterion) | Source / justification | Priority | Status | Test / verification note |
|---|---|---|---|---|---|---|
| NFR-01 | Performance | With the NFR-02 load and reference dataset, **95%†** of main user actions (saving Availability, a Leave Request, an Assignment or a Job Rejection Request; loading a Landing Page) shall complete within **5 s**, measured at the server. A saved change shall be visible to other logged-in users within **60 s** | INT-ITA [Q: Response time] ("maybe 3 or 5 seconds"; "less than a minute or so"); Brief R2 ("immediately"); DEC-47 | Should | Agreed | Report the 95th percentile per action and time cross-session visibility after a save |
| NFR-02 | Capacity | The system shall support **50 concurrent sessions**, including one person on up to 3† devices, with a reference dataset of 6 Vans, 17 Staff, 25 Jobs per working day† (above the brief's "more than 20") and 13 months of records (the 12-month retention plus the 1-month window) | INT-ITA [Q: Concurrency]; Brief §Company ¶4–5; DEC-34 | Must | Agreed | Load test at 50 sessions on the reference dataset |
| NFR-03 | Availability | The system shall be available 24/7 with **≥ 99%† monthly uptime**, excluding planned maintenance between **00:00 and 05:00†**, never on a Monday or Thursday (the peak days) | INT-ITA [Q: Hours], [Q: Outage]; DEC-38 | Must | Agreed | Monthly uptime report from monitoring |
| NFR-04 | Recoverability | After a failure, service and data shall be restored within **24 h** of detection, with no more than **1 h** of saved data lost. Backups shall run at least hourly, and a failed backup shall alert the IT Administrator | INT-ITA [Q: Outage] ("Not more than one day"), [Q: Restore]; DEC-47 | Must | Agreed | Timed restore drill confirms service restoration within 24 h and a recovery point no older than 1 h |
| NFR-05 | Reliability / offline | Staff shall be able to view **today's** published Assignments without a connection. A Job completion (with its photo) entered offline is queued and submitted automatically when the connection returns. Each queued Job shows local/waiting, uploading, received or failed state and photo status. Details/photo are retained after failure for retry; success is confirmed only when both are received. Repeated taps or retries cannot create another completion or duplicate Workload credit | INT-DCT [Questionnaire C18/C19]; INT-ITA [Q: Outage], [Q: Connection failure]; DEC-69 | Should | Agreed | In airplane mode, today's Jobs are viewable and each queued completion/photo is labelled local or waiting. Reconnect → uploading, then received after both are saved. Photo/network failure retains the item for retry. Repeat submission → no second completion or Workload credit |
| NFR-06 | Reliability | A failed submission shall be retried automatically up to **3†** times. If it still fails, the user sees a message saying it was not saved and advising them to try again or contact the IT Administrator | INT-ITA [Q: Connection failure] | Should | Agreed | Cut the network mid-submit → retries, then the message |
| NFR-07 | Security | Login from a device not used in the last **30 days** shall require an email confirmation (2FA), for all roles | INT-ITA [Q: Safeguards]; DEC-41 | Should | Agreed | New device → email confirmation required. Same device the next day → not required |
| NFR-08 | Security | Staff personal data and schedule data shall be encrypted at rest. Passwords are stored only as salted hashes† | INT-ITA [Q: Safeguards] ("encrypted properly in the backend") | Must | Agreed | Inspect the database: personal fields are unreadable and there are no plaintext passwords |
| NFR-09 | Security | Access shall be role-based, following the **permission matrix in §4.2** | INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-18; DEC-37; DEC-45; DEC-47 | Must | Agreed | Test every role × action cell in §4.2. Every ✗ must be refused |
| NFR-10 | Data retention | Schedule records (Jobs, Crews, Assignments, Availability, Leave) shall be kept for **12 months** from their date, and may then be purged. Deactivated users' records follow the same rule | INT-ITA [Q: Retention] ("up to one year"); DEC-34 | Must | Agreed | A record from 11 months ago is retrievable |
| NFR-11 | Compatibility / usability | The system shall be a browser-based web application requiring no installation. At the M2 demo it shall support the latest stable Chrome, Edge, Firefox and DuckDuckGo on Windows, Android and iOS. Staff pages shall work at **360 px†** width without horizontal scrolling, and Manager pages at **1366 px†** or wider | Brief R1; INT-ITA [Q: Devices]; INT-DCT [Questionnaire C18/C19]; INT-DRV [Q14]; DEC-47 | Must | Agreed | Run the main flows in each named browser and platform; verify responsive layouts at 360 px and 1366 px |
| NFR-12 | Usability | In a walkthrough with **3†** non-technical users, each shall complete "enter a week's Availability" and "submit a Job Rejection Request" without help, in under **3 minutes†** each | INT-MGR [Closing] ("Just keep it simple. Most of my staff aren't very technical.") | Must | Agreed | Moderated walkthrough on the wireframe prototype |

### 4.1 Permission matrix (NFR-09)

*Report Table 2.12.* ✓ = allowed, ✗ = refused, "own" = only the User's own records, "crew" = only Jobs on the Staff member's own Van. Staff see only Published Assignments. Each prohibited role/action combination must be refused.

| Action | Staff (Driver) | Staff (Technician) | Manager | IT Administrator |
|---|---|---|---|---|
| Set Availability, Job Preference; request Leave or a late change | own | own | ✗ | ✗ |
| View Assignments and Standby days | own, Published weeks only | own, Published weeks only | all | ✗ |
| View Crew-mates' names and contact numbers | crew | crew | all | ✗ |
| View other Staff's Availability, Leave or Workload | ✗ | ✗ | ✓ | ✗ |
| Submit a Job Rejection Request | crew | crew | ✗ | ✗ |
| Mark a Job Completed | ✗ | crew | ✗ | ✗ |
| Create, edit or cancel Jobs; form Crews; name Standby; allocate; publish | ✗ | ✗ | ✓ | ✗ |
| Decide Leave, Late Availability Change and Job Rejection Requests | ✗ | ✗ | ✓ | ✗ |
| Maintain Vans, Workshop Servicing dates and Certifications (after creation) | ✗ | ✗ | ✓ | ✗ |
| Create or deactivate accounts; change roles; unlock accounts | ✗ | ✗ | ✗ | ✓ |
| View the audit log | ✗ | ✗ | ✗ | ✓ |

Sources: INT-ITA [Q: Onboarding], [Q: Permissions]; DEC-17; DEC-35; DEC-37; DEC-40; DEC-42; DEC-43; DEC-45.

### 4.2 Rationale for team-set criteria (†)

*Report Table 2.13.* These values are team choices recorded in the SRS, rather than stakeholder thresholds. We use them to make the requirements measurable and feasible to verify.

| ID | Team-set criterion | Rationale |
|---|---|---|
| FR-48 | 5 failed logins in 15 min → lock | Stops password guessing while tolerating a non-technical user mistyping a few times. The IT Administrator asked for lockouts but gave no number |
| NFR-01 | 95th percentile | Response-time targets are normally stated as a percentile, so that rare network outliers don't fail an otherwise responsive system. 5 s is the upper of the IT Administrator's "3 or 5 seconds" |
| NFR-02 | Up to 3 devices per person; 25 Jobs per day; 13 months of data | The IT Administrator named multiple devices per person (phone, tablet, laptop). 25 is about 25% headroom over the brief's "more than 20 jobs … daily". 13 months = the 12-month retention + the 1-month window |
| NFR-03 | ≥ 99% monthly uptime; maintenance 00:00–05:00 | 99% allows about 7 h of downtime a month, well within the IT Administrator's "Not more than one day". The window matches their "early morning or late night" and falls outside working hours (09:00–18:00) |
| NFR-06 | 3 automatic retries | Covers brief signal drops in basements without leaving the user waiting long |
| NFR-08 | Salted password hashes | Standard practice for "encrypted properly in the backend". Passwords should never be recoverable |
| NFR-11 | 360 px (Staff) / 1366 px (Manager) | 360 px is a common small Android screen width, and Technicians use their own Android phones. 1366 px is a common laptop width for the office-based Manager |
| NFR-12 | 3 users, under 3 minutes, no help | A small walkthrough is feasible for the team. The two tasks are the most frequent Staff actions, and 3 minutes is a reasonable ceiling for a weekly task |

## 5. Prioritisation (MoSCoW)

*Report §2.2.1, "Prioritisation".* Must requirements cover the brief's minimum requirements, the complete weekly workflow, blocking business rules and basic account/data protection. Should requirements are valuable stakeholder needs that do not prevent the weekly workflow from operating. The active baseline contains **45 Must and 5 Should FRs, plus 8 Must and 4 Should NFRs**; no Could requirement remains in this scope.

**Stakeholder ranking used as a tie-breaker:** the Manager ranked their needs as "Staff workload first, then unassigned jobs, then leave. Van usage is nice to have" (INT-MGR [System Q1 follow-up: ranking]). They said what mattered most was "Allocating jobs with valid crews, and seeing the workload at a glance" (INT-MGR [Closing]).

## 6. Coverage check: Brief initial requirements

| Brief | Summary (see brief for exact text) | FR / NFR IDs |
|---|---|---|
| R1 | Web-based | NFR-11 |
| R2 | Manager Landing Page shows staff workload | FR-40, NFR-01 |
| R3 | Allocate jobs one week at a time | FR-07, FR-09 |
| R4 | Allocation page: up to three staff availability | FR-31 |
| R5 | Availability display: workload, preference, location, week availability | FR-31, FR-17 |
| R6 | Three lowest workload; highlight >40 hours | FR-36, FR-40 |
| R7 | Staff Landing Page: weekly assignments and monthly workload | FR-41, FR-42 |
| R8 | Add/edit availability up to **1 month in advance** (the brief's "5 weeks" is superseded, DEC-01) | FR-12, FR-13 |
| R9 | Weekly job preference | FR-17 |
| R10 | Reject jobs with warning (implemented as a request the Manager approves, DEC-42) | FR-37, FR-38 |
| R11 | IT administrators add staff and managers | FR-44, NFR-09 |

## 7. Assumptions and unresolved issues

*Report §2.1.5, verbatim.*

**Assumptions**

- We adopted the lecturer's one-month clarification over the conflicting five-week wording. Entry/editing and Manager viewing run from today through the same calendar date next month, inclusive, clamped to month end. Availability and Job Preference lock at 18:00 on Wednesday, 12 days before the Planning Week. (FR-13–FR-15; UC-10, UC-11.)
- We adopted a Job-based Workload for every Crew member: Job duration plus 0.5 h Travel Allowance per Job, replaced by actual working time plus that allowance on completion; breaks are excluded. Overtime means strictly above 40 h and raises a warning. Lowest-three rankings are separate by role, exclude approved Leave and use name A–Z for ties. These adopted rules reconcile shift-based hours and route estimates. The Technician questionnaire responses ask for the calculation to be explained; they do not independently confirm its numeric values. (FR-35, FR-36, FR-40.)
- We retained Manager-decided Job Rejection Requests, consistent with the Technician questionnaire. Pending Jobs stay Assigned; approval unassigns the Job and active Linked partners, while refusal or lapse at Job start retains the Assignment. There is one Pending request per shared Assignment. Short notice means less than 48 h and requires an explanation; exactly 48 h is normal. (UC-09, UC-12.)
- We keep existing Availability while a Late Availability Change Request is Pending and update it only on approval; there is no late Job Preference route. We adopted a named Standby Staff who is Available all day and outside every Crew. Later approved Leave, Availability changes or Certification expiry can mark an existing Van-day Needs attention for Manager repair. (FR-16, FR-29, FR-30.)
- We refined account deletion to deactivation, preserving past records for 12 months and removing future Assignments. We chose email for initial login details and SMS for the phone-notification channel. The adopted scope uses area, day, Slot and Job Type preferences; Crew-mate preferences, calendar administration and automatic replacement suggestions are outside the adopted scope. (UC-03, UC-04, UC-11, UC-15; NFR-10.)
- We translated approximate performance and usability expectations into measurable SRS targets. Team-chosen values, including the 95% response criterion, 99% uptime, three retries and viewport/walkthrough thresholds, are identified as such in the SRS rather than attributed verbatim to interviewees. (NFR-01, NFR-03, NFR-06, NFR-11, NFR-12.)
- The Manager proposed excluding public holidays from scheduling and moving affected Workshop Servicing dates to the next working day. The team has not adopted public-holiday handling in the current baseline. The system treats Monday–Saturday as working days, including public holidays, and moves Sunday Workshop Servicing to Monday. The Manager must manually avoid allocating Jobs on public holidays and adjust affected servicing dates. Automatic public-holiday validation and public-holiday calendar administration are outside scope.

**Unresolved issues**

- We still need the IT Administrator/team to confirm reset-link and email-confirmation-code lifetimes and password-complexity rules. Successful reset invalidates all outstanding reset tokens for that Account. (UC-01, UC-02.)
- We need to confirm what happens to an already active session when its Account is deactivated or its role changes. (UC-04.)
- We need to confirm whether non-status fields of a Cancelled Job can be edited. Completed and Cancelled remain final Job statuses. (UC-05.)
- We need to define the automatic Workshop Servicing rotation for Vans added beyond the current six. Existing-Crew conflicts are already resolved by blocking that booking date. (UC-06.)
- We need to confirm how today's offline Assignment cache is prepared and refreshed, and how a queued completion is handled if its Job changes before upload. (UC-13, UC-14.)
- We need the Manager/IT Administrator/team to confirm email/SMS acknowledgement and duplicate-delivery policies (UC-15). The Technician questionnaire also raises open questions about Availability reminders, extra daily/count statistics and calendar overlays, request-history timestamps, mandatory refusal explanations and mapping exact-hour Availability to the adopted Slots. These additions are not assumed to be in scope.

## 8. Candidate M2 testing targets

| Rubric item | Candidate | Why it qualifies |
|---|---|---|
| Black-box (decision table) | FR-27 / FR-32: Crew and Brand validity | Several conditions: Brands on the Van, each Technician's Certifications, expiry vs Job date, Crew size |
| Black-box (alternative) | FR-37 / FR-38: Job Rejection Request | Conditions: Published week; within 48 h; reason Other with or without a comment; explanation present; Manager's decision; still pending at the start time |
| White-box (CFG with ≥8 nodes and ≥2 decisions) | FR-24: generate Workshop Servicing dates | A loop over Vans and dates, an odd/even month branch, and a Sunday shift branch |

## 9. Draft-ID mapping (SRS v3.4 → submitted report)

The repo used draft IDs up to SRS v3.4. The report renumbered the active requirements by process area. Older repo records that are kept as history (decisions.md DEC-01 to DEC-71, the sequence-review notes in diagrams/ and requirements-review.md) still cite the draft IDs; use this table to read them.

| Draft ID (v3.4) | Report ID | | Draft ID (v3.4) | Report ID |
|---|---|---|---|---|
| FR-01 | FR-43 | | FR-45 | FR-33 |
| FR-02 | FR-44 | | FR-46 | FR-34 |
| FR-03 | — (withdrawn before submission) | | FR-47 | — (withdrawn before submission) |
| FR-04 | FR-45 | | FR-48 | — (withdrawn before submission) |
| FR-05 | FR-46 | | FR-49 | FR-09 |
| FR-06 | FR-47 | | FR-50 | FR-10 |
| FR-07 | FR-48 | | FR-51 | FR-11 |
| FR-08 | — (withdrawn before submission) | | FR-52 | — (withdrawn before submission) |
| FR-09 | — (withdrawn before submission) | | FR-53 | FR-35 |
| FR-10 | FR-22 | | FR-54 | — (withdrawn before submission) |
| FR-11 | — (withdrawn before submission) | | FR-55 | FR-36 |
| FR-12 | — (withdrawn before submission) | | FR-56 | FR-40 |
| FR-13 | FR-12 | | FR-57 | — (withdrawn before submission) |
| FR-14 | FR-13 | | FR-58 | FR-41 |
| FR-15 | FR-14 | | FR-59 | FR-42 |
| FR-16 | FR-15 | | FR-60 | — (withdrawn before submission) |
| FR-17 | FR-16 | | FR-61 | — (withdrawn before submission) |
| FR-18 | — (withdrawn before submission) | | FR-62 | FR-37 |
| FR-19 | — (withdrawn before submission) | | FR-63 | FR-38 |
| FR-20 | — (withdrawn before submission) | | FR-64 | FR-39 |
| FR-21 | FR-17 | | FR-65 | — (withdrawn before submission) |
| FR-22 | FR-18 | | FR-66 | FR-49 |
| FR-23 | FR-19 | | FR-67 | FR-50 |
| FR-24 | FR-20 | | FR-68 | — (withdrawn before submission) |
| FR-25 | FR-21 | | FR-69 | — (withdrawn before submission) |
| FR-26 | — (withdrawn before submission) | | FR-70 | FR-29 |
| FR-27 | FR-23 | | FR-71 | FR-30 |
| FR-28 | FR-24 | | NFR-01 | NFR-01 |
| FR-29 | FR-25 | | NFR-02 | — (withdrawn before submission) |
| FR-30 | FR-26 | | NFR-03 | NFR-02 |
| FR-31 | — (withdrawn before submission) | | NFR-04 | — (withdrawn before submission) |
| FR-32 | FR-27 | | NFR-05 | NFR-03 |
| FR-33 | FR-28 | | NFR-06 | NFR-04 |
| FR-34 | FR-01 | | NFR-07 | — (withdrawn before submission) |
| FR-35 | FR-02 | | NFR-08 | NFR-05 |
| FR-36 | FR-03 | | NFR-09 | NFR-06 |
| FR-37 | FR-04 | | NFR-10 | NFR-07 |
| FR-38 | FR-05 | | NFR-11 | NFR-08 |
| FR-39 | FR-06 | | NFR-12 | NFR-09 |
| FR-40 | — (withdrawn before submission) | | NFR-13 | NFR-10 |
| FR-41 | FR-07 | | NFR-14 | NFR-11 |
| FR-42 | FR-08 | | NFR-15 | — (withdrawn before submission) |
| FR-43 | FR-31 | | NFR-16 | NFR-12 |
| FR-44 | FR-32 | | NFR-17 | — (withdrawn before submission) |
