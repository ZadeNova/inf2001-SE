# Decisions and Open Questions

> Every ambiguity, contradiction or gap in the brief or the rubrics gets a DEC entry **before** anyone picks an interpretation (see [AGENTS.md](AGENTS.md)).
> Anyone may add entries, but never edit someone else's entry. Resolve an entry by filling in Decision / Decided by / Source and setting its Status.
> IDs are never reused.

**Status:** `Open` (not asked yet) · `Asked` (waiting for an answer) · `Decided` · `Superseded by DEC-nn`
**Ask whom:** `Stakeholder` (via an elicitation meeting) · `Lecturer` (course admin/rubric) · `Team` (internal design choice)

Quotes are verbatim from [brief/project-description.md](brief/project-description.md) ("Brief") and [brief/rubric-m1.md](brief/rubric-m1.md) / [brief/rubric-m2.md](brief/rubric-m2.md) / [brief/assessment-overview.md](brief/assessment-overview.md).
DEC-01 to DEC-30 were raised on 2026-09-30 (AI-assisted analysis, see `ai-usage-log.md`). The options listed are possibilities for discussion and are **not recommendations**. The index shows which entries have since been decided. DEC-02 to DEC-41 (except the rubric entries DEC-21, DEC-23 to DEC-29) were decided on 2026-09-30 for SRS v2: the Manager's interview answer was adopted where one exists, and the simplest option consistent with the brief was chosen otherwise. Each decision says which parts were chosen by the team. They are open to change at team review.

> **ID note (2026-11-07, DEC-72):** the submitted M1 report renumbered the requirements and sequence diagrams. **DEC-01 to DEC-71 below are kept as written and cite the repo's draft IDs** (SRS v3.0–v3.4 and the 22-diagram draft). Read their FR/NFR numbers with the mapping in [requirements.md §9](requirements.md) and their SD numbers with [diagrams/README.md](diagrams/README.md). DEC-72 onwards use the report's IDs.

## Index

| ID | Topic | Category | Ask whom | Status |
|---|---|---|---|---|
| DEC-01 | Availability horizon: one month vs 5 weeks | Contradiction | Lecturer | **Decided**: 1 month in advance |
| DEC-02 | Availability Deadline mechanics (Wed / Thu / Mon) | Ambiguity | Stakeholder | **Amended by DEC-83** (late changes now outside the system) |
| DEC-03 | Availability granularity, default and deletion | Missing definition | Stakeholder | **Amended by DEC-83** (per working day) |
| DEC-04 | Workload unit and the period behind the 40-hour highlight | Ambiguity | Stakeholder | **Decided** |
| DEC-05 | "Top three staff with the lowest workload" | Ambiguity | Stakeholder | **Decided** |
| DEC-06 | "Up to three staff" on the allocation page | Ambiguity | Stakeholder | **Decided** |
| DEC-07 | What a Job Preference is | Missing definition | Stakeholder | **Superseded by DEC-79** |
| DEC-08 | "Staff's location at a particular date" | Missing definition | Stakeholder | **Superseded by DEC-77** |
| DEC-09 | Van crew composition and capacity | Ambiguity | Stakeholder | **Amended by DEC-84** |
| DEC-10 | Unit of assignment: Staff or Van crew | Ambiguity | Stakeholder | **Decided** |
| DEC-11 | What a Job contains and who creates Jobs | Missing definition | Stakeholder | **Amended by DEC-90** (Linked Jobs retired) |
| DEC-12 | Working days: Saturday and Sunday | Ambiguity | Stakeholder | **Amended by DEC-45** |
| DEC-13 | How Leave is handled | Missing definition | Stakeholder | **Superseded by DEC-73, DEC-74** |
| DEC-14 | Van Workshop Servicing in the system | Missing definition | Stakeholder | **Superseded by DEC-85** |
| DEC-15 | What happens after a Job Rejection | Missing definition | Stakeholder | **Superseded by DEC-42** |
| DEC-16 | Allocate one week vs visualise one month | Ambiguity | Stakeholder | **Decided** |
| DEC-17 | IT Administrator: distinct actor and scope | Missing definition | Stakeholder | **Decided** |
| DEC-18 | Roles: Staff vs Manager vs "administrative staff" | Ambiguity | Stakeholder | **Decided** |
| DEC-19 | Does the system enforce the business rules? | Missing definition | Stakeholder | **Amended by DEC-90** (Needs attention retired) |
| DEC-20 | "Working hours engaged/assigned" | Ambiguity | Stakeholder | **Decided** |
| DEC-21 | Deliverable scope: working web app vs wireframe | Rubric | Lecturer | **Decided** (DEC-94) |
| DEC-22 | Job volume and duration vs crew capacity | Missing definition | Stakeholder | **Decided** |
| DEC-23 | M1 activity diagram examples ("subscription, announcement, notification") | Rubric | Lecturer | **Decided** |
| DEC-24 | M1 Formatting rubric lists M2 artefacts and a "required template" | Rubric | Lecturer | **Decided** |
| DEC-25 | Appendix C subsections labelled B.1–B.4 | Rubric | Lecturer | Open |
| DEC-26 | M2 "provided report template" not in our materials | Rubric | Lecturer | **Decided** (DEC-94) |
| DEC-27 | Week numbering and M1 presentation timing | Rubric | Lecturer | **Asked** |
| DEC-28 | Stakeholder rule: "same project" restriction | Rubric | Lecturer | Open |
| DEC-29 | Weighting labels and unweighted Introduction items | Rubric | Lecturer | Open |
| DEC-30 | How "1 month in advance" is measured | Ambiguity | Team | **Decided** |
| DEC-31 | Travel time: fixed allowance vs estimated driving time | Contradiction (interviews) | Stakeholder | **Decided** |
| DEC-32 | Overtime: approval step or warning only? | Contradiction (interviews) | Stakeholder | **Decided** |
| DEC-33 | Real-time delay reporting by the Crew | Scope (interviews) | Stakeholder | **Decided** |
| DEC-34 | Leavers: delete accounts vs retain records | Contradiction (interviews) | Stakeholder | **Amended by DEC-89** (purge is required) |
| DEC-35 | Who maintains Certifications and staff details | Contradiction (interviews) | Stakeholder | **Amended by DEC-75** |
| DEC-36 | Account and schedule import vs manual entry | Contradiction (interviews) | Stakeholder | **Decided** |
| DEC-37 | What Staff may see about colleagues | Ambiguity (interviews) | Stakeholder | **Decided** |
| DEC-38 | IT Administrator's Thursday peak vs the weekly cycle | Contradiction (interviews) | Stakeholder | **Decided** |
| DEC-39 | Technician Workload on mixed or 3-person Vans | Missing definition | Stakeholder | **Amended by DEC-78** |
| DEC-40 | Actual Hours, Travel Allowance and completion evidence | Missing definition | Stakeholder | **Superseded by DEC-76, DEC-78** |
| DEC-41 | Email 2FA vs simplicity and field use | Tension (interviews) | Stakeholder / Team | **Decided** |
| DEC-42 | Job Rejection needs Manager approval (\"Staff submit, the Manager decides\") | Team decision (overrides interviews) | Team | **Decided** |
| DEC-43 | Daily Standby Staff as backup for every Job | Team decision (overrides interview) | Team | **Superseded by DEC-81** |
| DEC-44 | Pay model (salary, shifts, commission) is background only | Scope | Team | **Decided** |
| DEC-45 | Final 15-use-case structure and scope alignment | Team decision | Team | **Amended by DEC-91** |
| DEC-46 | UC-15 uses Email/Phone | Team decision | Team | **Decided** |
| DEC-47 | Consolidate requirements to minimum active baseline | Team decision | Team | **Decided** |
| DEC-48 | UC-15 phone channel is SMS | Team decision | Team | **Decided** |
| DEC-49 | Initial password delivered by email | Team decision | Team | **Decided** |
| DEC-50 | UC-05 and UC-06 notifications use UC-15 | Team decision | Team | **Decided** |

---

## A. Availability and planning cycle

### DEC-01: Availability horizon: one month vs 5 weeks

| Category | Contradiction | Ask whom | Lecturer | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief §Intro ¶3: "employees should be able to indicate their availabilities up to one month earlier."
- Brief §Intro ¶4: "The administrative staff (usually the manager) should be able to visualise the manpower availability at any time up to one month earlier."
- Brief R8: "Staff can add and edit their availabilities up to 5 weeks ahead of time."

**Question:** How far ahead can Staff enter Availability, and how far ahead can the Manager view it: one month, 5 weeks, or different limits for each? Also, "earlier" is presumably meant as "ahead/in advance". Please confirm.

**Why it matters:** This sets the date-range validation (an FR plus a testable boundary), the calendar range in the UI and black-box test boundaries in M2. "One month" also varies from 28 to 31 days, while 5 weeks is exactly 35 days.

**Options:**
1. 5 weeks for both input and viewing (numbered requirements override the narrative).
2. One calendar month for both.
3. Staff input up to 5 weeks, Manager view up to one month (or the reverse).
4. A rolling window aligned to planning weeks (e.g. the current week plus the next 4 weeks).

**Decision:** Option 2. The Availability horizon is **1 month in advance** for both Staff input (R8) and the Manager's view. "5 weeks" in R8 is superseded. "Earlier" means **"in advance"**, i.e. a forward-looking window from the current date and not a past window.
- Lecturer's replies (verbatim): *"Sorry for the confusion caused. It should be "1 month" for consistency."* and *"to avoid the ambiguity, the "earlier" is now changed to "in advance"."*
- Not addressed by the reply: whether "1 month" means a calendar month or a fixed number of days. See DEC-30.

**Decided by:** Prof Guan (lecturer), in reply to Team P8-1's email · **Decision source:** Lecturer email, recorded 2026-09-30

### DEC-02: Availability Deadline mechanics (Wed / Thu / Mon)

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶1: "work allocation is assigned weekly every Monday. The workload allocation planning will start every Thursday of the week. Hence, all employee's availabilities must be informed in the system every Wednesday to be considered in the planning. If employees miss the weekly deadline, requests would be dealt with on a case-by-case basis."

**Question:**
- Wednesday's deadline covers which week: the week starting the following Monday, or later weeks too?
- What exact time is the cut-off (e.g. Wed 23:59)?
- Is "assigned every Monday" the day the Assignments are published, or the first day of the week being planned?
- After the deadline, can Staff still edit Availability for that week (R8 says "add and edit")?
- Is the "case-by-case" late request handled inside the system (a request/approval flow) or outside it?

**Why it matters:** This defines the core weekly process for the activity diagrams, whether Availability becomes locked, and whether a "late availability request" use case exists.

**Options:**
1. Hard lock after Wed cut-off, with late changes handled off-system by the Manager.
2. Hard lock plus an in-system late-change request that the Manager approves or rejects.
3. Soft deadline: edits are allowed but flagged as late to the Manager.

**Decision:** Hard lock plus in-system late-change request (Option 2). Availability for a Planning Week locks at **18:00 on the Wednesday 12 days before** that week's Monday; the Manager plans from Thursday and publishes on the Monday 7 days before the week. After the lock, Staff submit a Late Availability Change Request with a reason; the Manager approves or rejects it.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q1], [Clarification Q6 follow-up], [Conflicts Q2]; INT-DCT [Process Q1 follow-up: deadline]

### DEC-03: Availability granularity, default and deletion

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief R8: "Staff can add and edit their availabilities up to 5 weeks ahead of time." Brief R5: "...and availabilities for the week should be shown"

**Question:** Is Availability recorded per day, per half-day (AM/PM) or per time slot? Are Staff assumed available unless they say otherwise, or unavailable unless they declare Availability? R8 says "add and edit". Can Staff also delete an entry?

**Why it matters:** This shapes the Availability class attributes, the input UI and how "available" is computed for allocation.

**Options:**
1. Whole-day available/unavailable, defaulting to available.
2. Half-day slots, defaulting to available.
3. Explicit time ranges, defaulting to unavailable.

**Decision:** Half-day Slots: Morning 09:00–13:00, Afternoon 14:00–18:00. Each Slot is `Available` or `Unavailable`; a Slot with no entry is **Not submitted** and is treated as unavailable for allocation. Staff may change or clear any Slot until the lock.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q4]; INT-DCT [Clarification Q2]; default and clearing chosen by the team

**Amended** 2026-09-30 (team review, ZadeNova): Staff can also set a whole day in one step, which sets both Slots (FR-13).

### DEC-16: Allocate one week at a time vs visualise one month

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief R3: "The manager should be able to allocate jobs to staff for one week at a time"
- Brief §Intro ¶4: "visualise the manpower availability at any time up to one month earlier"

**Question:** Can the Manager allocate Jobs only for the upcoming planning week, or for any single week inside the visible horizon? Can Assignments for the current week be changed after Monday (e.g. to cover a rejection or sickness)?

**Why it matters:** This affects the preconditions of the allocate-jobs use case and the reassignment flows.

**Options:**
1. Only the next planning week can be allocated, and the current week is read-only.
2. Any single week within the horizon can be allocated.
3. The next week is allocated normally, and the current week is editable for reassignments only.

**Decision:** Option 3: the Manager allocates one Planning Week at a time (the next unpublished week) and may view up to 1 month ahead. Each week's roster is Draft until published; Staff see Published weeks only. After publication the Manager may still change Assignments; affected Staff are notified.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief R3; INT-MGR [Clarification Q6], [Conflicts Q5]; Draft/Published states chosen by the team

## B. Workload and the Manager's views

### DEC-04: Workload unit and the period behind the 40-hour highlight

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief R6: "...and highlight all staff over 40 hours of jobs allocated"
- Brief R2: "The manager should be able to visualise the staff workload immediately on the landing page"
- Brief R7: "Staff should be able to view their weekly job assignments and overall workload for the month on their landing page"

**Question:**
- Is the 40-hour threshold per week, and if so which week (current or next planning week)?
- Is Workload measured in hours of Job duration only, or does it include travel time?
- Is it "over 40" (>40) or "40 and above" (≥40)?
- For R7, is "the month" a calendar month or a rolling four or five weeks?

**Why it matters:** Workload is the central metric of the system, and this highlight rule is an obvious black-box test candidate. The boundary (>40 vs ≥40) must be exact.

**Options:**
1. Weekly, current week, Job duration only, >40.
2. Weekly, upcoming planning week, >40.
3. A configurable period and threshold.

**Decision:** Workload is measured in hours per **Planning Week (Monday–Saturday)**; **strictly above 40 hours** is Overtime and is highlighted. "The month" in R7 is the **calendar month**. Travel is counted per DEC-31.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief R6; INT-MGR [Clarification Q7]; calendar month chosen by the team

### DEC-05: "Top three staff with the lowest workload"

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief R6: "On the manager'slanding page, the top three staff with the lowest workload should be shown"

**Question:**
- Over what period (see DEC-04)?
- Across all Staff, or separately for Drivers and Technicians (or per Brand Certification)?
- Should Staff on Leave or unavailable be excluded?
- How are ties broken?

**Why it matters:** Ranking Drivers and Technicians together may not help the Manager fill a Van, since a van needs both roles. Tie-breaking has to be defined before this can be tested.

**Options:**
1. All Staff in one list.
2. The top three per role (Driver / Technician).
3. The top three among Staff available in the period.

**Decision:** Two lists: the three **Technicians** and the three **Drivers** with the lowest Workload in the displayed week. Staff with **any approved Leave day in that week** are excluded. Ties are broken by name (A–Z). If fewer than three are eligible, show those who are.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [added follow-up: lowest three]; tie-break and partial-Leave rule chosen by the team

### DEC-06: "Up to three staff" on the allocation page

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief R4: "The manager should be able to view up to three staff availability and any relevant information to make the job assignment easier on the job allocation page"
- Brief §Intro ¶4: "visualise manpower availabilities, job assignments, and allocate jobs. Individual employee workload and availabilities should be able to be visualised at a glance."

**Question:** Does R4 mean the allocation page shows a side-by-side comparison of at most three selected Staff, or that it recommends three Staff? Can the Manager still see the full roster somewhere else (e.g. on the landing page)? Why three? It might match a Van crew of up to 3 people.

**Why it matters:** This drives the design of the main Manager screen and the allocation use case flow.

**Options:**
1. The Manager selects up to three Staff to compare while assigning a Job.
2. The system suggests three candidate Staff for a Job.
3. The allocation page shows one Van crew (up to three people) at a time.

**Decision:** Option 1: the Manager selects up to three Staff and compares them side by side while allocating.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [System Q3]

### DEC-20: "Working hours engaged/assigned"

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Intro ¶3: "an interactive and visual way for the employee to see their job assignments, working hours engaged/assigned"

**Question:** Does "engaged" mean hours actually worked, which would need Job completion or time recording, or is it a synonym for "assigned"? Is Job completion recorded in the system at all?

**Why it matters:** If actual hours count, a new use case is needed (record completion or hours) along with new attributes.

**Options:**
1. Assigned hours only, with no completion tracking.
2. Staff or the Manager mark Jobs completed and actual hours are recorded.

**Decision:** Option 2: a Technician on the Crew marks Jobs completed with actual start and end times; Actual Hours replace Planned Hours (see DEC-40).

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q7], [Process Q1 follow-up: completion]; INT-DCT [Process Q1 follow-up: completion]

## C. Staff inputs

### DEC-07: What a Job Preference is

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief R9: "Staff can indicate their job preference for the week". Brief R5: "staff's job preference"

**Question:** What can Staff express as a preference: Brand, Job Type (installation vs servicing), area or region, particular days, or preferred colleagues or Van? Does it apply to Drivers? Is it binding or advisory? Does it share the Wednesday deadline?

**Why it matters:** The JobPreference class attributes and the preference UI both depend on this.

**Options:**
1. Job Type only.
2. Job Type plus area/region.
3. Free text shown to the Manager.
4. A structured set of fields to be agreed with stakeholders.

**Decision:** Job Preference = preferred area, preferred days, preferred Slot and preferred Job Type, all optional. It is advisory (a tie-breaker that raises only a warning) and locks together with that week's Availability.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q1 follow-up: ordering]; INT-DCT [Clarification Q4]; INT-DRV [Q10]; deadline chosen by the team

### DEC-08: "Staff's location at a particular date"

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief R5: "When displaying the staff availability, the workload assigned, staff's job preference, staff's location at a particular date, and availabilities for the week should be shown"

**Question:** Where does this location come from? Possibilities include the location of the Staff member's assigned Job that day (derived), a location the Staff member enters with their Availability, their home or base area, or live GPS. Who enters it, and at what granularity (address, postal district, region)?

**Why it matters:** This decides whether location is derived from the Job, becomes a Staff input field, or needs an external integration. Live GPS would bring privacy NFRs.

**Options:**
1. Derived from the address of the Job assigned on that date.
2. Staff enter an expected location or region with each day's Availability.
3. A fixed home or base region stored on the Staff profile.
4. Live device location (out of scope?).

**Decision:** Option 1: location = the areas (postal districts) of the Staff member's other Jobs on that date; "No Jobs" if none. No GPS.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [System Q3]

### DEC-15: What happens after a Job Rejection

| Category | Missing definition | Ask whom | Stakeholder | Status | **Superseded by DEC-42** |
|---|---|---|---|---|---|

**Source text:**
- Brief R10: "Staff can reject jobs assigned to them, but they will be warned to discuss the jobs with their manager before proceeding with the rejection"
- Brief §Intro ¶3: "Employees should be able to indicate to the company any assigned jobs they cannot fulfil ahead of time."

**Question:**
- Is a reason required?
- Is the Manager notified, and how (in-app or email)?
- Does the Job return to "unassigned" automatically, or does the Manager have to approve the rejection?
- Is there a cut-off (e.g. no rejection within 24 hours of the Job)?
- Are rejections counted or limited?
- Is "indicate ... cannot fulfil ahead of time" the same feature as R10?
- If one crew member rejects, what happens to the rest of the Van crew's Assignment?

**Why it matters:** This is a key process for an activity diagram and a strong candidate for black-box decision-table testing.

**Options:**
1. Immediate rejection, the Job becomes unassigned and the Manager is notified.
2. A rejection request that the Manager approves or denies.
3. Rejection allowed only until a cut-off, after which the Staff member must contact the Manager.

**Decision:** Option 1: any Crew member may reject a Job assigned to their Van. Warning first, reason required (comment required for "Other"). No approval: the Job is removed from the Van and becomes Unassigned; the whole Crew and the Manager are notified; the rejecter gets a confirmation. If the Job starts within 48 hours the warning also states the Manager's 48-hour-notice expectation (not a block). "Indicating ahead of time" is the same function.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief R10; INT-MGR [Conflicts Q3], [added follow-up: early rejection]; INT-DCT [Process Q2], [Process Q2 follow-up: after reject]; crew-wide effect chosen by the team

**Superseded** on 2026-09-30 by DEC-42 (team review): every Job Rejection is now a request that needs the Manager's approval.

## D. Domain: Vans, Jobs, Leave, calendar

### DEC-09: Van crew composition and capacity

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶3–4: "Currently, there are six vans. Each van is made up of one driver and a qualified technician for each brand. Unless the van is servicing or installing only a particular brand, then one driver and a qualified technician for the brand." / "The team consist of 6 drivers and 11 technicians. Currently, only 2 technicians are qualified to service for both brands. There are five technicians qualified only to work on M Electric aircons and four technicians only for Dicon. The minimum manpower for a van is two and the maximum is three."

*Checked:* 2 + 5 + 4 = 11 Technicians, which matches the stated total. A crew of 1 Driver plus 1 or 2 Technicians fits the 2–3 limit.

**Question:**
- Can one dual-Brand Technician cover both Brands in a Van (Driver + 1 dual Technician, 2 people)? Or does the rule "a qualified technician for each brand" require two Technicians?
- Are Drivers tied to a specific Van?
- Can a Technician drive?
- Are crews fixed for the week or assembled daily?
- Six Vans with 2 Technicians each would need 12 Technicians, but there are only 11. Is running all six Vans with mixed-Brand crews ever expected?

**Why it matters:** These rules define the Van–Staff associations in the class diagram and the validation rules in allocation.

**Options:**
1. A dual-certified Technician satisfies both Brands, so a crew of 2 can cover both.
2. Mixed-Brand Vans always carry two Technicians, one per Brand.
3. Drivers are fixed to Vans, and Technicians are assigned to a Van each day.
4. Crews are fully flexible each day.

**Decision:** A Crew is exactly one Driver plus one or two Technicians. One dual-Brand Technician can cover both Brands. Technicians never drive. Crews are formed per Van per day and stay fixed for the day except for Manager emergency changes.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief §Company ¶3–4; INT-MGR [Process Q1 follow-up: ordering], [Clarification Q3], [Clarification Q4 follow-up]; INT-DCT [Clarification Q1], [Conflicts Q1 follow-up]

### DEC-10: Unit of assignment: Staff or Van crew

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief R3: "allocate jobs to staff for one week at a time"
- Brief §Company ¶3: "The weekly roster is dependent on the team's availability and the job required."
- Brief §Company ¶4: "at least three vans can be on service daily"

**Question:** Does the Manager assign Jobs to individual Staff, or to a Van (whose crew is then assigned for the day)? Or both: crew to Van first, then Jobs to Van? Does a Driver hold "Job Assignments" and Workload in the same way a Technician does?

**Why it matters:** This is the core domain model decision. It changes the Assignment class, how Workload is calculated for Drivers, and the whole allocation sequence diagram.

**Options:**
1. Job → individual Staff (the Van is implicit).
2. Staff → Van per day, then Job → Van, with each crew member inheriting the Job hours.
3. Job → Van crew as an explicit entity (a DailyCrew or similar).

**Decision:** Option 2: the Manager first forms each Van's Crew for the day, then assigns Jobs to the Van on that date. Every Crew member inherits the Van's Jobs (see DEC-39).

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q1]

### DEC-11: What a Job contains and who creates Jobs

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶2: "Only certified technicians for the brand are qualified to do the installation or servicing." ¶5: "On average, there are more than 20 jobs for aircon installation and servicing daily." The brief never says how Jobs enter the system.

**Question:**
- What attributes does a Job have? Candidates: customer, address/location, date, time slot, estimated duration, Brand, Job Type (installation/servicing), number of units, status.
- Who creates Jobs: the Manager, other administrative staff, or an import from a sales/booking system?
- Can a single Job involve both Brands?

**Why it matters:** Job is the central entity. Without a definition, the class diagram and the Workload calculation (hours) can't be specified, and "create Job" may or may not be a use case.

**Options:**
1. The Manager creates Jobs manually in the system.
2. Jobs are imported from an external sales system, which is out of scope and treated as an external actor.
3. Jobs are pre-loaded (seeded) for the prototype.

**Decision:** Option 1: the Manager creates Jobs manually. Required fields: customer name, customer phone, address, postal code, Brand, Job Type, number of units (≥1), preferred date, preferred Slot. Optional: unit number, aircon model, notes. One Brand per Job; a two-Brand customer is recorded as two linked Jobs that must go on the same Van and date.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q2]; INT-DCT [Process Q1 follow-up: job info]

### DEC-12: Working days: Saturday and Sunday

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶4: "there should be at least three vans can be on service daily except for Sunday."

**Question:**
- Is Saturday a normal working day?
- Does the Sunday exception mean no work at all, or only that the minimum of three Vans does not apply?
- What are the working hours per day?

**Why it matters:** Availability calendars, the minimum-Vans check and Workload baselines (e.g. how 40 hours relates to a 5.5- or 6-day week) all depend on this.

**Options:**
1. Mon–Sat working, no work on Sundays.
2. Mon–Sat working, with Sunday work allowed but no minimum.
3. A configurable working calendar maintained by the Manager or IT Administrator.

**Decision:** Option 1: working days are Monday–Saturday, 09:00–18:00 with lunch 13:00–14:00; closed on Sundays (no Jobs, no Crews). Calendar-management scope was removed by DEC-45.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q4], [Clarification Q8]

### DEC-13: How Leave is handled

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶4: "All staff are given 7 days annual leave."

**Question:**
- Is Leave applied for and approved in this system, or just entered as unavailability?
- Should the system track the remaining balance of 7 days (per calendar year?)?
- Does Leave follow the Wednesday deadline?
- Does it apply to Managers as well?

**Why it matters:** This may add a leave use case and a LeaveBalance-type attribute, or it may be out of scope.

**Options:**
1. Out of scope: Staff simply mark themselves unavailable.
2. A Leave type of unavailability, with the balance tracked but no approval.
3. A full leave request and approval flow.

**Decision:** Option 3: full-day Leave Requests on working days, with optional note; Manager approves or rejects (reason required on rejection). Balance: 7 days per calendar year, no carry-over, deducted on approval; a request may not exceed the remaining balance. Sick leave is recorded by the Manager as unavailability, not Leave. Managers do not use Leave in this system.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief §Company ¶4; INT-MGR [Process Q4], [Process Q4 follow-up], [Clarification Q1]; full-day and balance cap chosen by the team

### DEC-14: Van Workshop Servicing in the system

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶5: "A van will be sent to the workshop for servicing every two months."

**Question:** Should the system record Van Workshop Servicing dates so the Van shows as unavailable? Who schedules them? For how long is a Van out? Must the three-Van minimum still hold on workshop days?

**Why it matters:** This decides whether Van availability is modelled at all, i.e. whether Van needs its own availability or status.

**Options:**
1. Not modelled: the Manager just doesn't allocate that Van.
2. Van unavailability dates entered by the Manager.
3. The system auto-schedules servicing every two months.

**Decision:** The system **generates** Workshop Servicing dates from the fixed rotation (odd months Vans 1–3, even months Vans 4–6, on the 1st/11th/21st), moving a Sunday date to Monday. The Manager can adjust a generated date and can mark ad-hoc unavailability (breakdowns). Current scope follows DEC-45.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q3], [Conflicts Q4]; generation chosen by the team

**Amended** 2026-09-30 (team review, ZadeNova): when servicing needs more than one day, the Manager records the extra days as Van unavailability (FR-29).

### DEC-22: Job volume and duration vs crew capacity

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶5: "On average, there are more than 20 jobs for aircon installation and servicing daily." ¶4: "at least three vans can be on service daily"

**Question:** What is the typical duration of an installation vs a servicing Job? How many Jobs can one Van do per day? This is needed to check whether 3–6 Vans can realistically cover more than 20 Jobs a day.

**Why it matters:** It sets data-volume and performance NFRs (e.g. more than 20 Jobs/day × 1 month ≈ 500+ Jobs in view, per DEC-01) and realistic Workload hours.

**Options:**
1. Stakeholders provide standard durations per Job Type.
2. Duration is entered per Job.

**Decision:** Option 1: Standard Durations of 1 h per unit for Servicing and 3 h per unit for Installation, pre-filled and editable per Job. Customers usually book 1–2 weeks ahead, rarely beyond 4 weeks; no booking limit.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q2 follow-up: hours], [Process Q2 follow-up: advance]; INT-DCT [Clarification Q3 follow-up]

## E. Actors and system rules

### DEC-17: IT Administrator: distinct actor and scope

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Brief R11: "The company's IT administrators will oversee adding new staff and managers to the system"

**Question:**
- Is the IT Administrator a separate system actor with its own login, or does "oversee" mean they supervise a process done by someone else?
- Can they also edit, deactivate or remove users, reset passwords, or change roles and Brand Certifications?
- Do they see any workload data?

**Why it matters:** This decides whether there is an actor in the use-case diagram and user-management use cases, and it drives security/access NFRs.

**Options:**
1. A distinct actor with add-only rights, exactly as R11 is written.
2. A distinct actor with full user CRUD, including Certifications.
3. Not a system actor; accounts are provisioned outside the system.

**Decision:** A distinct actor. The IT Administrator creates accounts, imports employees once at go-live (DEC-36), changes roles and permissions, unlocks accounts, deactivates leavers (DEC-34), and views the audit log. Role changes take effect at the user's next login. Current scope follows DEC-45.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief R11; INT-ITA [Q: Onboarding], [Q: Permissions], [Q: Role change/leaver], [Q: Passwords], [Q: Audit]; INT-MGR [Clarification Q8]; session rule and audit viewer chosen by the team

### DEC-18: Roles: Staff vs Manager vs "administrative staff"

| Category | Ambiguity | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief §Intro ¶4: "The administrative staff (usually the manager)"
- Brief R11: "adding new staff and managers"
- Brief §Company ¶4: "All staff are given 7 days annual leave."

**Question:**
- Are there administrative staff other than the Manager who use the system, and with what rights?
- Is there one Manager or several (and if several, do they share all Staff)?
- Is a Manager also "Staff", with their own Availability or Assignments?
- Do Drivers use the same Staff features as Technicians (Job Preference, rejection)?

**Why it matters:** This affects the actor list, actor generalisation in the use-case diagram, and User/Staff/Manager inheritance in the class diagram.

**Options:**
1. Three actors (Staff, Manager, IT Administrator), with Driver and Technician as Staff subtypes.
2. Add an "Administrative Staff" actor that the Manager specialises.
3. A single User with roles.

**Decision:** Option 1: three roles (Staff, Manager, IT Administrator); Driver and Technician are Staff subtypes. There may be more than one Manager account, all with identical permissions. No other administrative role. Managers are not Staff: no Availability, Leave or Workload.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q1]; multiple-Manager rule chosen by the team

### DEC-19: Does the system enforce the business rules?

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Brief §Company ¶2: "Only certified technicians for the brand are qualified to do the installation or servicing."
- Brief §Company ¶4: "The manager will make their assignments such that there should be at least three vans can be on service daily" / "The minimum manpower for a van is two and the maximum is three."

**Question:** When the Manager allocates, should the system block, warn about, or ignore each of these:
- assigning a Technician to a Brand they aren't certified for
- fewer than three Vans on a working day
- a Van with fewer than 2 or more than 3 crew
- assigning Staff who are unavailable
- going over 40 hours

**Why it matters:** This is the main source of conditional logic. It feeds the decision table (M2 black-box) and the white-box method (M2 needs at least 8 CFG nodes and 2 decisions).

**Options:**
1. Hard-block every rule.
2. Hard-block Certification, warn on the rest.
3. Warnings only, leaving the Manager to decide.

**Decision:** The Manager's split. **Block:** uncertified or expired Certification, double booking, Staff unavailable/not submitted/on Leave, invalid Crew, unavailable Van, or Sunday. **Warn (overridable, override logged):** Workload over 40 hours, Job Preference not met, fewer than 3 Vans on service on a working day, Job start outside the customer's preferred Slot. A Van is *on service* when it has a valid Crew and at least one Job. When approved Leave, an approved Late Availability Change Request or Certification expiry invalidates a Crew, the affected person is removed and the Van-day is flagged *Needs attention*. Current scope follows DEC-45.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** Brief §Company ¶2–4; INT-MGR [System Q4], [Conflicts Q1]; expiry, preferred-Slot warning, 'on service' and invalidation handling chosen by the team

### DEC-21: Deliverable scope: working web app vs wireframe prototype

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:**
- Brief R1: "The app should be Web-based in a language of your choosing"
- Rubric M2: "Wireframe (3%) — screenshot and description"
- Rubric M2 B.1.2.2: "The presentation slides or demo should cover focus on presenting the prototype wireframe"

**Question:** Does the module expect working code, or is an (interactive) wireframe prototype sufficient? The M2 rubric only grades wireframes, yet the white-box testing criteria refer to "the method's pseudocode".

**Why it matters:** It determines whether implementation appears in the WBS and timeline (M1 Project Management) and how testing is done in M2.

**Options:**
1. Wireframe or clickable prototype only (e.g. Figma), with pseudocode for testing.
2. A partial working web app.
3. A full working web app.

**Decision:** — · **Decided by:** — · **Decision source:** —

## F. Rubric and assessment issues

### DEC-23: M1 activity diagram examples do not match this project

| Category | Rubric | Ask whom | Lecturer | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** Rubric M1 B.4, Activity diagrams: "Clear workflows modelled for all key processes (subscription, announcement, notification)."

**Question:** The Aircon Retailer brief has no subscription or announcement process, and notification is at most implied by DEC-15. This looks like a template carry-over from another project. Should we model *our* key processes (e.g. submit Availability, allocate Jobs, reject Job) instead?

**Why it matters:** Activity diagrams are part of the 5% Use Cases component. We need to know which processes will be graded as "key".

**Options:**
1. Treat it as a carry-over and model this project's key processes, with a sentence in the report explaining our choice.
2. Also model a notification process if one emerges from DEC-15.

**Decision:** Option 1: treat the rubric's "(subscription, announcement, notification)" as a template carry-over. The team models this project's own key processes; which ones is chosen by the team when drawing the activity diagrams.

**Decided by:** ZadeNova (team) · **Decision date:** 2026-09-30 · **Decision source:** Team decision, 2026-09-30

### DEC-24: M1 Formatting rubric lists M2 artefacts and a "required template"

| Category | Rubric | Ask whom | Lecturer | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- Rubric M1 B.4, Presentation / Formatting: "Professionally structured report following the required template..." and "Strong alignment and traceability across requirements, use cases, final class diagram, component diagram, detailed design, testing artefacts, and prototype wireframes."
- Rubric M1 B.1.2.1, by contrast: "All artifacts align (e.g., requirements ↔ use cases ↔ diagrams)."

**Question:** The M1 B.4 Formatting row is identical to the M2 row and lists artefacts that don't exist in M1. Is there an M1 report template we should be following? If not, is the B.1.2.1 wording the one that applies to M1?

**Why it matters:** This is 2% of the M1 grade, and we need to know which template or structure is expected.

**Options:**
1. Assume a carry-over: follow B.1.2.1 and the M1 chapter list.
2. Obtain and follow the M2 template for M1 as well.

**Decision:** A report template exists and the team has it; the M1 report follows that template.

**Decided by:** ZadeNova (team) · **Decision date:** 2026-09-30 · **Decision source:** Team confirmation, 2026-09-30

### DEC-25: Appendix C subsections labelled B.1–B.4

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:** Under "Appendix C. Design and Prototype for Milestone 2 (2nd half)", the subsections are headed "B.1 Requirements for Milestone 2 Report (20%)", "B.2 Submissions", "B.3 Peer Evaluation" and "B.4 Rubrics", duplicating Appendix B's labels.

**Question:** Confirm that these mean C.1–C.4. How should we cite them unambiguously?

**Why it matters:** Low impact, but it matters for references in our reports and repo. We currently cite them as "Rubric M2 B.x".

**Options:**
1. Cite as "Rubric M2 B.x" (current repo convention).
2. Cite as "Appendix C.x".

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-26: M2 "provided report template" not in our materials

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:** Rubric M2 (Appendix C intro): "The Milestone 2 Report should follow the provided report template, which serves as a guide for the required structure and content."

**Question:** Where is the template (LMS)? Should we adopt its structure now so that M1 and M2 are consistent?

**Why it matters:** Following the template is part of the Formatting criteria.

**Options:**
1. Locate it on LMS and add a copy or conversion to `brief/`.
2. Ask the lecturer for it.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-27: Week numbering and M1 presentation timing

| Category | Rubric | Ask whom | Lecturer | Status | **Asked** |
|---|---|---|---|---|---|

**Source text:**
- Rubric M1: "submit a Milestone 1 Report and make a group presentation by Week 6"
- Appendix A: "All engagements (in-person, email, virtually) must end by Week 6 of the trimester."
- Rubric M1 B.2: "The deadline for submission is: 11:59PM, 9 Oct 2026 (Friday)."
- Rubric M1 B.1.2.2: "Logistics information, e.g., presentation date and time, will be shared later."

**Question:** What calendar dates are Week 2 and Week 6? Does "end by Week 6" mean the start or the end of Week 6? Is the presentation before or after the 9 Oct submission, and how long is the "allocated time"?

**Why it matters:** This fixes the real cut-off for stakeholder meetings and the anchor dates for the project timeline (M1 Project Management).

**Options:**
1. Confirm from the SIT academic calendar or LMS and record the dates here.

**Decision:** Partial: the M1 presentation is expected next week (week of 5 Oct 2026); exact date and time still to be announced. Week 2 / Week 6 calendar dates still to be recorded.

**Decided by:** — · **Decision date:** 2026-09-30 · **Decision source:** Team information, 2026-09-30

### DEC-28: Stakeholder rule: "same project" restriction

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:** Appendix A: "Each student cannot be acting as Stakeholder Representatives for more than two teams (including your own team) and cannot be engaged in Stakeholder meetings for the same project." Also: "Every team should have engage at least 5 Stakeholder Representatives with at most 2 representatives from your own team."

**Question:**
- Does "the same project" mean a student cannot be a stakeholder for another team working on the *same project description* (Aircon Retailer) as their own team?
- Does "including your own team" mean that our two internal reps can each serve only one external team?

**Why it matters:** It limits whom we can recruit, and whom other teams can recruit from us.

**Options:**
1. Interpretation: no stakeholder may come from another Aircon Retailer team, and internal reps count one of their two slots.
2. Ask the lecturer.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-29: Weighting labels and unweighted Introduction items

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:**
- Rubric M1/M2: "B.1 Requirements for Milestone 1 Report (20%)", which contains "B.1.2 Presentation (5%)", which contains "Group Presentation (3%)".
- Rubric M2 Introduction includes "Final Class diagram" with no weighting, yet Formatting requires traceability to the "final class diagram".

**Question:** Is the 20% for the report alone, or report plus presentation? (The sums show Content 15% + Formatting 2% + Group Presentation 3% = 20%.) Is the M2 final class diagram assessed only through Formatting and alignment?

**Why it matters:** Low impact on the work itself, but it affects how much effort to put into the M2 Introduction's final class diagram.

**Options:**
1. Treat 20% as covering the whole milestone (report and presentation), and treat the final class diagram as essential because the component diagram and pattern criteria are checked against it.

**Decision:** — · **Decided by:** — · **Decision source:** —

## G. Follow-ups

### DEC-30: How "1 month in advance" is measured

| Category | Ambiguity | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-09-30, as a follow-up to DEC-01

**Source text:** Lecturer's reply (DEC-01): "It should be "1 month" for consistency." and "the "earlier" is now changed to "in advance"."

**Question:** How exactly is the 1-month window computed? For example, if today is 30 Sep, is the last allowed date 30 Oct (calendar month), 29 Oct (30 days), or the end of the last planning week that starts within the month? What happens on 31 Jan (there is no 31 Feb)? Does the window start today or at the next planning week?

**Why it matters:** This is the exact boundary for the Availability date validation FR and the M2 black-box test cases. It is a design choice within the lecturer's ruling, so the team can decide it, and optionally confirm it with a stakeholder.

**Options:**
1. Same date next calendar month (clamped to month end), inclusive.
2. Fixed 30 days from today.
3. Whole planning weeks (Mon–Sun) that start within one calendar month from today.

**Decision:** Option 1: the allowed range is **today through the same calendar date next month, inclusive**, clamped to that month's last day (e.g. from 31 Jan the last date is 28/29 Feb). The same rule is used for the Certification reminder.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** DEC-01; chosen by the team

## H. Conflicts between interview transcripts

Raised on 2026-09-30 while drafting the SRS (AI-assisted, see `ai-usage-log.md`). Quotes are verbatim from `elicitation/interviews/`. Citation format: see [requirements.md §1.4](requirements.md#14-sources-and-citation-format). The options are for discussion and are **not recommendations**.

### DEC-31: Travel time: fixed allowance vs estimated driving time

| Category | Contradiction (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-MGR [Clarification Q7]: "The system won't know real travel times, so I'd like a fixed allowance of 30 minutes per job, added on top of the job duration."
- INT-DRV [Q4]: "it must include estimated driving time between job locations so my total weekly workload accurately reflects actual hours and flags if I exceed 40 hours. We track this workload by correlating estimated route hours alongside the vehicle's daily mileage logs."

**Question:** Is travel counted as a fixed 30 minutes per Job, or as estimated driving time (route estimates or mileage logs)? If mileage logs are used, who records them?

**Why it matters:** Workload drives the 40-hour highlight and the lowest-three lists (now FR-53 and FR-56 after DEC-47). Mileage-based travel would need new data entry and a new attribute.

**Options:**
1. A fixed 30-minute allowance per Job (the Manager's statement).
2. Estimated driving time between Job locations.
3. The fixed allowance for planning, with mileage-based actuals after the day.

**Decision:** Option 1: a fixed 30-minute Travel Allowance per Job. The system holds no route or mileage data.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q7] (process owner)

### DEC-32: Overtime: approval step or warning only?

| Category | Contradiction (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-DRV [Q6]: "When delays occur, the remaining jobs are typically pushed back to another day, or overtime (OT) is automatically flagged for approval if we must complete it that evening."
- INT-MGR [System Q4]: "It should only warn me for over forty hours, a preference not being met, or fewer than three vans in a day. Sometimes I have to accept those, so I want to be able to override the warning."
- INT-MGR [Conflicts Q5]: "Anything above forty hours in the week shows up as overtime."

**Question:** Does Overtime need an approval workflow, or is it only highlighted and warned about?

**Why it matters:** An approval flow would add a use case, a request type and a notification (FR-45, FR-55).

**Options:**
1. Highlight and overridable warning only (the Manager's statements).
2. Add an Overtime approval request that the Manager approves.

**Decision:** Option 1: no approval step. Overtime (over 40 h) is highlighted and raises an overridable warning.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [System Q4], [Conflicts Q5] (process owner)

### DEC-33: Real-time delay reporting by the Crew

| Category | Scope (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-DRV [Q6]: "I need a way to see real-time updates or inform the manager if a job will breach working hour limits or conflict with another appointment."
- INT-DCT [Conflicts Q3]: "The driver calls the next customer to say we're running late, and I let the manager know."
- INT-MGR [Conflicts Q5]: "If a job overruns, the crew finishes it and records the actual time when they mark it complete."

**Question:** Should the Crew be able to report a delay or overrun in the system, or is a phone call to the Manager enough?

**Why it matters:** An in-system report would add a use case and a Manager notification. The SRS currently leaves it out.

**Options:**
1. Out of scope: phone call, then actual time recorded on completion.
2. Add a "report delay" action that notifies the Manager.

**Decision:** Option 1: out of scope. Delays are reported by phone; the actual time is recorded on completion.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Conflicts Q5]; INT-DCT [Conflicts Q3]

### DEC-34: Leavers: delete accounts vs retain records

| Category | Contradiction (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** all from INT-ITA.
- [Q: Role change/leaver]: "If they leave then, IT admin will delete their account. If they had any outstanding schedules, those should be removed when the account is deleted."
- [Q: Retention]: "All schedules should exist up to one year in our system, we need to be able to track our staff and their movements for each yearly review. Deletion of past or currently happening schedules should not be possible, but if they have yet to pass then deletion should be ok."

**Question:** When someone leaves, is their account deleted or deactivated? Are their past Assignments, Workload and Leave records kept for the 1-year retention?

**Why it matters:** Deleting the account would also delete history that the retention rule and monthly Workload need (FR-05, FR-67, NFR-13).

**Options:**
1. Deactivate the account, remove only future Assignments, and keep history for 1 year.
2. Delete the account, remove future Assignments, and anonymise past records.
3. Delete the account after the 1-year retention period.

**Decision:** Option 1: leavers' accounts are **deactivated**, not deleted: they cannot log in, their future Assignments are removed (those Jobs become Unassigned), and past records are kept. Schedule records are kept for **12 months** from their date and may be purged after that. Past and in-progress records cannot be deleted by any user; Jobs are cancelled, not deleted.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-ITA [Q: Role change/leaver], [Q: Retention]; deactivation chosen by the team to satisfy both statements

### DEC-35: Who maintains Certifications and staff details

| Category | Contradiction (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-ITA [Q: Permissions]: "Only the IT admins should have any permissions to grant or edit access permissions."
- INT-ITA [Q: Account info]: "All accounts will be need name, email, default password that user can change later."
- INT-MGR [Clarification Q2]: "I just give them the details: name, contact number, role, and for technicians, which brands they're certified for."
- INT-MGR [Clarification Q2 follow-up]: "Certificates are renewed every two years, so the system should remind me a month before one expires."

**Question:** Who enters and updates Certifications (Brand, number, expiry): the IT Administrator or the Manager? The IT Administrator also didn't list contact number or Certifications as account data.

**Why it matters:** This decides which actor performs "Maintain Certification" in the use-case diagram, and which fields a user account holds (FR-02, FR-10).

**Options:**
1. The IT Administrator enters everything at account creation, and the Manager maintains Certifications afterwards.
2. The IT Administrator maintains everything, and the Manager only receives reminders.

**Decision:** Option 1: the IT Administrator records Certifications when creating a Technician's account; afterwards the Manager maintains them and receives expiry reminders.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q2], [Clarification Q2 follow-up]; INT-ITA [Q: Account info]

### DEC-36: Account and schedule import vs manual entry

| Category | Contradiction (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-ITA [Q: Onboarding]: "Ideally, we manually create the user so as to ensure correctness in our procedures and details."
- INT-ITA [Q: Existing systems]: "we need to have all employees from that ported over. We have our employees and current schedules be able to be exported in CSV format so that can help with transferring data."
- INT-MGR [Process Q2]: "There's no other system to import from. Today it's all in a spreadsheet."

**Question:**
- Are accounts created manually, bulk-imported once from the employee portal, or both?
- Which "current schedules" exist to import?
- Does the Manager's spreadsheet of Jobs need importing?

**Why it matters:** This decides whether there are import use cases (FR-08, FR-68).

**Options:**
1. A one-off CSV import of employees, with manual creation afterwards, and no schedule import.
2. Manual creation only.
3. Import both employees and the existing spreadsheet schedules.

**Decision:** Option 1: a one-off CSV import of employees at go-live, then manual account creation. No schedule import (FR-68 withdrawn).

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-ITA [Q: Onboarding], [Q: Existing systems]; INT-MGR [Process Q2]

### DEC-37: What Staff may see about colleagues

| Category | Ambiguity (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:** INT-ITA [Q: Safeguards]: "On the scheduler the only things that should be displayed are the names and emails of who put their schedule in that timeslot." By contrast, INT-MGR [System Q3] wants to compare "their availability that day, their hours so far this week, their brand certifications, their preferences, and where they'll be that day".

**Question:** Does the IT Administrator's rule apply to what **Staff** see of colleagues (e.g. Crew-mates), with the Manager keeping full visibility? What exactly may Staff see about their Crew-mates (FR-59 shows names)?

**Why it matters:** This sets the privacy rule in NFR-12 and the content of the Staff views.

**Options:**
1. Staff see only colleagues' names (and emails) and the Manager sees everything.
2. Staff see no colleague information beyond Crew names.

**Decision:** Option 1: Staff see only the names and contact numbers of their own Crew-mates for their own Assignments, and nothing of other Staff's Availability, Leave or Workload. Managers see all Staff schedules.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-ITA [Q: Safeguards], [Q: Permissions]; INT-MGR [System Q3]; INT-DRV [Q2]

### DEC-38: IT Administrator's Thursday peak vs the weekly cycle

| Category | Contradiction (interviews) | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-ITA [Q: Hours]: "Another peak period would be Thursday since they can start scheduling their slots then."
- INT-MGR [Process Q1]: "Staff update their availability by 6pm on Wednesday. On Thursday I start planning."

**Question:** Does anything open to Staff on Thursday, such as Availability for a new week? Or did the IT Administrator mean the Manager's planning day?

**Why it matters:** It affects the peak-load assumptions (NFR-05) and whether an Availability window opens on Thursday.

**Options:**
1. Treat Thursday as the Manager's planning peak only.
2. Confirm with the IT Administrator.

**Decision:** Option 1: Thursday is the Manager's planning peak; nothing opens to Staff on Thursday. Peak periods for NFRs: Monday early morning and Thursday.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Process Q1]; INT-ITA [Q: Hours]

### DEC-39: Technician Workload on mixed or 3-person Vans

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-MGR [Clarification Q5 follow-up]: "A technician's allocated hours are just the total of their jobs, plus travel."
- INT-MGR [Clarification Q7]: "Drivers get the same hours as the van they're on, because they're with the crew the whole time, helping carry equipment."
- INT-MGR [Clarification Q4 follow-up]: Crews "stay together for the whole day, in the same van."
- INT-DCT [Conflicts Q1 follow-up]: "For big installations there's sometimes a second technician with me, but usually it's just me and the driver."

**Question:** On a Van with two Technicians, is each Technician credited with only the Jobs of their Brand, or with every Job on the Van (like the Driver)? Which Technician "owns" a Job when both are certified for it?

**Why it matters:** This defines the Workload calculation (FR-53) and whether an Assignment links a Job to individual Technicians or only to the Van.

**Options:**
1. Each Technician is credited with the whole Van day, the same as the Driver.
2. Each Job is assigned to specific Technician(s), who get only those hours.

**Decision:** Option 1: every Crew member (Driver and Technicians) is credited with the hours of all Jobs on their Van that day, since the Crew stays together all day. Completed Jobs stay credited to whoever was on the Crew when the Job was completed.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q7], [Clarification Q4 follow-up]; chosen by the team

**Confirmed** 2026-09-30 by the team (review round 2, ZadeNova): whole-Van hours for every Crew member (Option 1).

### DEC-40: Actual Hours, Travel Allowance and completion evidence

| Category | Missing definition | Ask whom | Stakeholder | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-MGR [Clarification Q7]: "The hours should show the planned time first, and once a job is completed, use the actual time instead."
- INT-MGR [Process Q1 follow-up: completion]: "They should mark the job as completed in the system with a photo of the invoice signed by the customer."
- INT-DCT [Process Q1 follow-up: completion]: "In the system, I'd mark the job as complete, with the actual start and end time, a short remark, and whether a follow-up visit is needed". The DCT does not mention an invoice photo.

**Question:**
- When actual time replaces planned time, is the 30-minute Travel Allowance still added?
- Who can mark a Job complete (any Crew member, or Technicians only)?
- Is the invoice photo mandatory?

**Why it matters:** This shapes the completion use case, its validation and the Workload formula (now FR-39 and FR-53 after DEC-47).

**Options:**
1. Actual Hours = end − start + 30 min. Technicians complete Jobs. The photo is optional.
2. Actual Hours = end − start. Any Crew member completes Jobs. The photo is mandatory.

**Decision:** Actual Hours = (actual end − actual start) + the 30-minute Travel Allowance. Only a Technician on the Crew can mark a Job completed. The signed-invoice photo is **mandatory**. Cancelled and Unassigned Jobs count zero hours.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-MGR [Clarification Q7], [Process Q1 follow-up: completion]; INT-DCT [Process Q1 follow-up: completion]; travel on actuals chosen by the team

**Confirmed** 2026-09-30 by the team (review round 2, ZadeNova): Actual Hours include the Travel Allowance.

### DEC-41: Email 2FA vs simplicity and field use

| Category | Tension (interviews) | Ask whom | Stakeholder / Team | Status | **Decided** |
|---|---|---|---|---|---|

**Source text:**
- INT-ITA [Q: Safeguards]: "2FA when logging in would be good, send confirmation to user email before they can login."
- INT-MGR [Closing]: "Just keep it simple. Most of my staff aren't very technical."
- INT-DCT [System Q3]: "in basements and some condo car parks there's no signal."

**Question:** Is email 2FA required on every login, on new devices only, or only for Manager and IT Administrator accounts?

**Why it matters:** It is a trade-off between security (NFR-10) on one side and usability and offline access in the field (NFR-16, NFR-08) on the other.

**Options:**
1. 2FA on every login for all roles.
2. 2FA on new devices only, with a remembered-device session.
3. 2FA for the Manager and IT Administrator only.

**Decision:** Option 2: email 2FA when a user logs in from a new device, for all roles; the device is then remembered for 30 days.

**Decided by:** ZadeNova, adopting an AI-proposed resolution (Claude Code) for team review · **Decision date:** 2026-09-30 · **Decision source:** INT-ITA [Q: Safeguards]; INT-MGR [Closing]; 30-day period chosen by the team

## I. Team review decisions (round 1)

These entries were made by the team on 2026-09-30 while reviewing SRS v2. They are the team's own decisions: the flow details were proposed by AI (Claude Code), and the team chose them from the options given. **DEC-42 and DEC-43 deliberately override what a stakeholder said in an interview.** The rationale is recorded so that the report and presentation can explain it.

### DEC-42: Job Rejection needs Manager approval

| Category | Team decision (overrides interviews) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-09-30 by ZadeNova (team review of SRS v2)

**Source text:**
- Brief R10: "Staff can reject jobs assigned to them, but they will be warned to discuss the jobs with their manager before proceeding with the rejection"
- INT-MGR [Conflicts Q3]: "It doesn't need my approval to go through, but the job goes back to unassigned, and I get notified straight away so I can reassign it."
- INT-DCT [Process Q2 follow-up: after reject]: "The job should disappear from my list, and the manager gets told, so he can give it to someone else."
- INT-MGR [System Q1 follow-up: landing page]: "Below that, today's vans and crews, the number of jobs still unassigned, and any pending requests: leave, late availability changes and rejections."

**Question:** Should a Job Rejection take effect immediately (as in DEC-15), or need the Manager's approval?

**Why it matters:** It changes the rejection use case, the Job status transitions, the Manager's pending requests and notifications (FR-38, FR-46, FR-56, FR-62 to FR-65).

**Options:**
1. Immediate, with no approval. This is what the Manager and the DCT said in their interviews (DEC-15).
2. Every rejection is a request that the Manager decides.

**Decision:** Option 2, following the team principle **"Staff submit, the Manager decides"**: the final decision on Leave, late Availability changes and Job Rejections rests with the Manager (SRS §2.5).
- **Reason required:** Personal emergency; Missing equipment or parts; or Other, with a comment.
  - "Clash with another job" is removed. The Manager assigns all work, and FR-44 blocks double bookings, so a clash can't occur.
  - "Not qualified" is removed for the same reason, because FR-32 and FR-44 block unqualified Technicians.
- **Short notice:** if the Job starts within 48 hours, a written explanation is also required and the request is marked Short notice. The Manager decides case by case.
- **While pending,** the Job stays Assigned.
- **Approved:** the Job becomes Unassigned and leaves the whole Van. The requester, the Crew and that day's Standby Staff are notified.
- **Refused:** the Assignment stands.
- **Still pending when the Job starts:** the request lapses and the Assignment stands.

**Rationale for overriding the interviews:**
- The team wants the Manager to keep control of the roster.
- The Manager's own landing-page answer already lists rejections among "pending requests".
- It makes rejections consistent with Leave Requests (FR-23) and Late Availability Change Requests (FR-17).
- The Brief's warning to discuss with the Manager (R10) is kept.

**Decided by:** ZadeNova (team review) · **Decision date:** 2026-09-30 · **Decision source:** Team review of SRS v2. The flow was proposed by AI and chosen by the team. Supersedes DEC-15.

### DEC-43: Daily Standby Staff as backup for every Job

| Category | Team decision (overrides interview) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-09-30 by ZadeNova (team review of SRS v2)

**Source text:**
- INT-MGR [Conflicts Q2 follow-up: standby]: "No dedicated standby staff. But anyone who marked themselves available and didn't get allocated is effectively on standby, so I'd like the system to show me who that is."
- Team review (ZadeNova): "There will be a backup crewmember for each job." and "The crew member on standby is notified."

**Question:** How is a backup provided for each Job?

**Why it matters:** It is a new concept that affects Crew formation, validation, warnings, notifications and Workload (FR-44, FR-45, FR-47 to FR-49, FR-58, FR-63, FR-64, FR-70, FR-71).

**Options:**
1. Daily Standby Staff named by the Manager, with a warning when cover is missing.
2. A named backup for each Job.
3. No named standby: the interview model, where anyone available and not in a Crew is "effectively on standby".

**Decision:** Option 1 (FR-71).
- **Who:** for each working day, the Manager names Standby Staff from people who are available for the whole day and not in a Crew.
- **Full cover:** at least one Standby Driver, plus Standby Technicians holding valid Certifications for both Brands.
- **Role:** they back up every Job that day.
- **Missing cover:** a warning, not a block, because capacity can't guarantee it (6 Drivers for 6 Vans).
- **Workload:** a Standby day counts 0 h unless the Standby is placed into a Crew.
- **Notifications:** Standby Staff are notified when named, and when someone they could replace drops out. The Manager decides the replacement.

**Rationale for overriding the interview:**
- The team wants a known first call for every Job.
- The Manager's "effectively on standby" pool (FR-47) is where Standby Staff are chosen from.
- A named backup per Job (Option 2) would mean more than 20 names a day, and is often impossible for Drivers.

**Decided by:** ZadeNova (team review) · **Decision date:** 2026-09-30 · **Decision source:** Team review of SRS v2. The options were proposed by AI and chosen by the team.

### DEC-44: Pay model is background only

| Category | Scope | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-09-30 by ZadeNova (team review of SRS v2)

**Source text:**
- INT-MGR [System Q1]: "Wages and costs are handled by our accounts department, so I don't need those here."
- Brief R6: "highlight all staff over 40 hours of jobs allocated"
- Team review (ZadeNova): Drivers are on basic salary and shift work. Technicians are on basic salary, shift work and per-Job commission.

**Question:** Should the pay model change the SRS? For example: the Workload definition, a pay calculation, or recording which Technician did each Job.

**Why it matters:** A pay calculation would contradict the Manager's interview and add sensitive pay data. Workload defined by shifts rather than Job hours would break Brief R6.

**Options:**
1. Record data for Accounts (shifts, Completed Jobs per Technician), with no pay calculation.
2. Calculate pay in the system.
3. Background only.

**Decision:** Option 3.
- Payroll and commission stay out of scope (SRS §1.2).
- Workload stays in hours of Jobs (FR-53 and FR-55 after DEC-47), as Brief R6 requires.
- No per-Technician Job attribution is added.

**Decided by:** ZadeNova (team review) · **Decision date:** 2026-09-30 · **Decision source:** Team review of SRS v2.

---

## J. Final use-case structure

### DEC-45: Final 15-use-case structure and scope alignment

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-01 by the requesting member during the authorised Codex drafting task.

**Source text:** The requesting member supplied the finalized table of UC-01 to UC-15 and corrected UC-08 to “Extends UC-07”.

**Question:** Which use-case IDs, names, actors and connections form the M1 baseline, and how should the SRS align with capabilities removed from that list?

**Decision:** Adopt the supplied 15-use-case table as use-case list v2.0.

- UC-01 combines Log In and Log Out.
- UC-07 combines Crew formation, Standby selection, Job allocation, roster validation, Published-roster changes and publication. DEC-47 later removed automatic replacement suggestions.
- UC-08 Compare Staff extends UC-07.
- UC-09 combines Manager decisions for Leave, Late Availability Change and Job Rejection Requests.
- UC-11 combines Availability and Job Preference.
- UC-12 combines Staff submission and review of the three request types.
- UC-15 remains included system behaviour; its actor and delivery channels are amended by DEC-46.
- Audit-log viewing is documented within UC-04 and Manager Certification maintenance within UC-10 so FR-10 to FR-12 and FR-66 remain traceable.
- FR-09 and FR-18 are Withdrawn because the finalized scope has no managed non-working-day calendar and no separate Manager operation to overwrite Staff Availability. FR-68 remains Withdrawn.
- Working days are Monday–Saturday; Sunday remains non-working.
- Earlier UC numbering is superseded by this finalized table. Current artefacts use the new IDs without creating tombstone files for the superseded draft list.

**Decided by:** Requesting member (identity TBC) · **Decision date:** 2026-10-01 · **Decision source:** direct team instruction in this task.

---

### DEC-46: UC-15 uses Email/Phone

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-01 by the requesting member during the authorised Codex drafting task.

**Source text:** The requesting member stated, "uc15 should be email/phone, update it".

**Question:** Which actor and delivery channels should UC-15 use?

**Decision:** UC-15 uses `Email/Phone` as its primary actor and delivers each required Staff notification by email and phone, in addition to the existing Landing Page notification. The exact phone mechanism remains open for team review.

**Decided by:** Requesting member (identity TBC) — **Decision date:** 2026-10-01 — **Decision source:** direct team instruction in this task.

---

### DEC-47: Consolidate requirements to minimum active baseline

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-01 during review of the 15 finalized use cases.

**Source text:** The requesting member asked to trim duplicate, vague and unnecessary requirements to the minimum, reviewed the proposed count, then instructed Codex to perform the edit on the same branch.

**Question:** Which requirements remain standalone in the minimum SRS baseline?

**Decision:** Adopt SRS v3.3 with **50 active FRs and 12 active NFRs**.

- Consolidate 11 FRs into related active FRs or the permission model: FR-03, FR-11, FR-20, FR-31, FR-40, FR-47, FR-52, FR-54, FR-57, FR-65 and FR-69.
- Remove 7 optional FRs from active scope: FR-08, FR-12, FR-19, FR-26, FR-48, FR-60 and FR-61.
- Consolidate 4 NFRs: NFR-02, NFR-07, NFR-15 and NFR-17.
- Remove NFR-04 from active scope as unnecessary implementation-level detail.
- Preserve the three prior withdrawals FR-09, FR-18 and FR-68.
- Retain all 26 retired IDs in compact history tables with `Withdrawn` status; IDs are not reused.
- Update the 15 formal use cases and traceability matrix so they reference only the active baseline.

**Decided by:** Requesting member (identity TBC) — **Decision date:** 2026-10-01 — **Decision source:** direct team instruction in this task.

---

### DEC-48: UC-15 phone channel is SMS

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-03 by the requesting member (identity TBC).

**Source text:** DEC-46: "The exact phone mechanism remains open for team review." UC-15 open question: "Confirm what the phone channel means operationally (for example SMS, application push notification or voice call)." The requesting member specified "SMS" in the diagram-review conversation.

**Question:** What does the phone channel of UC-15 mean?

**Decision:** The phone channel is SMS. Staff notifications are delivered on the Landing Page, by email and by SMS. The UC-15 actor keeps the name Email/Phone (DEC-46).

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-03 - **Decision source:** direct user instruction in the diagram-review conversation, reaffirmed by the instruction to apply the review fixes. Recorded as UC-15 draft v0.4; the SRS v3.3 phone-channel requirement is refined, not replaced.

---

### DEC-49: Initial password delivered by email

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-03 by the requesting member (identity TBC).

**Source text:** FR-02: "The account starts with an initial password that the user can change." UC-03 open question: "Confirm how the initial password is delivered." The requesting member specified "receieve through email" in the diagram-review conversation.

**Question:** How does a new user receive the initial password?

**Decision:** After the account is saved, the system emails the initial login details to the user's company email through Email Service. Changing the password stays optional (FR-02). Initial credential delivery belongs to UC-03, not UC-15.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-03 - **Decision source:** direct user instruction in the diagram-review conversation, reaffirmed by the instruction to apply the review fixes. Recorded as UC-03 draft v0.3 and use-case list v2.3.

---

### DEC-50: UC-05 and UC-06 notifications use UC-15

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-03 by the requesting member (identity TBC).

**Source text:** UC-05 A3 step 2: "The system sets Cancelled, removes it from active allocation, and notifies affected Crew members through UC-15 (FR-37, FR-38, FR-64)." UC-06 A1 step 3: "The system invokes UC-15 for released Crew members (FR-64)." The supplied diagram-fixes.md recommends option A: add the two missing include relationships.

**Question:** Should the diagram and use-case list show the UC-15 calls already specified in UC-05 and UC-06?

**Decision:** Adopt option A. UC-05, UC-06, UC-07 and UC-09 include UC-15 when their successful flows trigger FR-64 notifications. Add UC-05 and UC-06 include arrows to UC-15; preserve their existing formal flow wording. No new use case or notification event is introduced.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-03 - **Decision source:** instruction to apply the supplied review, using its recommended option consistent with the existing formal flows. Recorded as use-case list v2.3 and UC-15 draft v0.4.

---

## Entry template (copy for new entries)

### DEC-nn: <short title>

| Category | Contradiction / Ambiguity / Missing definition / Rubric | Ask whom | Stakeholder / Lecturer / Team | Status | Open |
|---|---|---|---|---|---|

**Raised:** YYYY-MM-DD by <member>

**Source text:** exact quote(s), with location

**Question:**

**Why it matters:**

**Options:**
1.
2.

**Decision:** — · **Decided by:** — · **Decision source:** — (MTG-nn / lecturer email / team meeting, with date)


## K. Sequence diagram decisions

| ID | Topic | Category | Ask whom | Status |
|---|---|---|---|---|
| DEC-51 | FR-70 is the later-event exception to FR-44 | Team decision | Team | **Superseded by DEC-90** |
| DEC-52 | Short notice means less than 48 hours | Team decision | Team | **Superseded by DEC-90** |
| DEC-53 | Boundary, control and entity sequence lifelines | Analysis design | Team | **Decided** |

### DEC-51: FR-70 is the later-event exception to FR-44

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC).

**Source text:** SRS v3.3 FR-44: "The system shall **block** any allocation, Crew change, Job edit or approval that would cause: an invalid or expired Certification for a Job's Brand (FR-32); a double booking (a person in two Crews on one day, a person both in a Crew and on Standby on one day, or overlapping Jobs on a Van); a Crew member unavailable, not submitted or on Leave for a Slot the Van works; an invalid Crew (FR-30); Linked Jobs split across Vans (FR-36); a Van that is unavailable; or a Sunday" SRS v3.3 FR-70: "When approved Leave, an approved Late Availability Change Request or a Certification expiry makes an existing Crew invalid, the system shall remove the affected person from that Crew for the affected dates, mark each affected Van-day **Needs attention** on the Manager's Landing Page, and notify the removed person and that day's eligible Standby Staff. The Manager decides the replacement. The Van's Jobs stay on the Van until the Manager fixes the Crew. A Van becoming unavailable is handled by FR-29" The supplied `sequence-diagrams.md` condition C2 says: "FR-70 is the later-event exception to FR-44".

**Question:** Does FR-44 prevent a later approved request or Certification event from invalidating an existing Crew?

**Why it matters:** UC-07 explicitly required this precedence to be settled before finalizing sequence diagrams.

**Decision:** FR-44 blocks a proposed allocation or Crew change. FR-70 is the exception for later approved Leave, an approved Late Availability Change Request or a Certification expiry/change that invalidates an existing Crew: remove the affected person, mark the Van-day Needs attention, notify the removed person and eligible Standby, and retain the Van's Jobs while the Manager chooses the replacement. A Van becoming unavailable remains FR-29.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** the member's previously accepted least-impact recommendation and direct instruction to implement condition C2 of the supplied review. This records that choice; it does not add a new workflow.

---

### DEC-52: Short notice means less than 48 hours

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC).

**Source text:** SRS v3.3 FR-62: "If the Job starts within 48 hours, a written explanation is also required and the request is marked **Short notice**." The requesting member specified "less than 48 hours". The supplied review condition C2 says: "Short notice means the Job starts in less than 48 h; exactly 48 h is normal."

**Question:** Is a Job Rejection Request submitted exactly 48 hours before the Job starts Short notice?

**Why it matters:** UC-09 and UC-12 kept this boundary open.

**Decision:** Short notice applies when the Job starts in strictly less than 48 hours. Exactly 48 hours is a normal request. The Other reason still requires a comment; a Short-notice request also requires a written explanation. Manager approval and pending/lapsed behaviour remain DEC-42 and FR-63.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** direct user choice in the diagram-review conversation, reaffirmed by the instruction to implement condition C2.

---

### DEC-53: Boundary, control and entity sequence lifelines

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC), from the supplied Claude Opus review.

**Source text:** `sequence-diagrams.md` condition C3: "sequence diagrams use boundary, control and entity lifelines"; section 3 lists ten boundary classes and eleven control classes; section 4 lists the required entity operations. `diagrams/README.md`: "actor, then boundary/control/entity lifelines, activation bars, dashed return messages, and `alt`/`opt`/`loop` fragments with guards."

**Question:** Which analysis classes connect the formal use cases to the sequence diagrams?

**Why it matters:** The sequence lifelines and entity messages must match the identified classes and their operations.

**Decision:** Adopt the ten boundary and eleven control classes named in the supplied section 3 as analysis responsibilities, with CL IDs in traceability and glossary entries. Add Audit Log (FR-66) and Notification (FR-56, FR-64) and section 4's operations to the local CD-domain model. Keep the 16 supplied sequence sources verbatim. Boundary/control responsibilities are design choices, not new stakeholder requirements or database/service implementation commitments.

- The supplied sequences call `Audit Log.record(actor, action)` while section 4 also requires `record(actor, action, target)`; show both overloads in the class model.
- SD-09 calls the late-change request's `reject()` while section 4 also specifies `reject(reason)`; show both overloads without making a rejection reason mandatory for that request.
- The Notification recipient associations requested in section 4 are mutually exclusive ({xor}); SD-15 creates one Notification for each recipient. A Notification belongs to Staff or Manager, not both.
- Existing class attributes and associations are preserved. The expanded class diagram and sequence package remain subject to review; Google Docs receives only the already-approved six images until further approval.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** direct instruction to follow the supplied `sequence-diagrams.md` build instructions. Human PR review and Opus review of rendered outputs remain pending.

---


## L. Sequence review corrections

| ID | Topic | Category | Ask whom | Status |
|---|---|---|---|---|
| DEC-54 | Workshop Servicing conflicts preserve existing Crews | Team decision | Team | **Decided** |
| DEC-55 | Split sequence workflows and analysis class views | Analysis design | Team | **Decided** |
| DEC-56 | Adopted sequence review corrections and operation signatures | Analysis design | Team | **Decided** |

### DEC-54: Workshop Servicing conflicts preserve existing Crews

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC).

**Source text:** SRS v3.3 FR-28: "The system shall **generate** Workshop Servicing dates from the rotation: odd months Vans 1, 2 and 3; even months Vans 4, 5 and 6; on the 1st, 11th and 21st respectively. A date that falls on a Sunday moves to Monday. The Van is unavailable all that day. The Manager may adjust a generated date. If servicing needs more than one day, the Manager records the extra days as Van unavailability (FR-29)". The supplied sequence-diagram-review.md M2 says: "either reuses the FR-29 release loop or blocks with a warning". The member selected: "Block that servicing date and show a warning (recommended: least impact on existing Assignments)."

**Question:** What happens if a proposed Workshop Servicing date already has a Crew?

**Decision:** Check for an existing Crew before booking the servicing date or making the Van unavailable. Block a conflicting proposed date, warn the Manager and preserve the Crew and Jobs. A generated conflicting date remains an unbooked proposal for the Manager to adjust; the analysis class represents this with an optional scheduledDate. Generate each month's rotation once, retaining both booked dates and conflicting proposals. When an adjusted date has no Crew, book it and mark the Van unavailable; free the previous booked date only if it exists and no other unavailability reason still applies. Breakdown and extra-day unavailability continue to follow FR-29.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** direct answer to the review's M2 question. Draft UC-06 and SD-06 record the chosen exception without changing SRS v3.3.

---

### DEC-55: Split sequence workflows and analysis class views

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC), from the supplied review.

**Source text:** sequence-diagram-review.md M5: "New IDs are allowed. Do not reuse SD-16; use SD-17 onwards or the a/b/c suffixes, and record the split in a DEC."

**Decision:** Retain SD-01 to SD-16. SD-07 becomes the Weekly Roster overview and calls SD-17 (Crew/Standby overview), SD-18 (Job allocation) and SD-19 (publication). SD-17 calls SD-26 (form/change Crew) and SD-27 (name Standby). SD-18/19 call SD-30 (confirm warnings before save). SD-09 becomes the request-decision overview and calls SD-20 (Leave overview), SD-21 (Late Availability Change) and SD-22 (Job Rejection). SD-20 calls SD-28 (reject Leave) or SD-29 (approve Leave). SD-12 becomes the submission overview and calls SD-23 (Leave), SD-24 (Late Availability Change) and SD-25 (Job Rejection). SD-16 remains the shared FR-70 fragment with no separate use case.

Class definitions remain one identified model with 43 classes. Keep the 22 entity classes in CD-domain and show the ten boundary classes in CD-boundary and eleven controls in CD-control for readability. The views introduce no new domain associations. All sequence lifelines and operations must agree with these views.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** instruction to apply the supplied review, including its permitted split. Human review of the rendered revision remains pending.

---

### DEC-56: Adopted sequence review corrections and operation signatures

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC), from the supplied review.

**Source text:** SRS v3.3 FR-45: "The system shall **warn**, allow an override and log it, when an allocation or a publication would cause: a Staff member's Workload above 40 h in the Planning Week; a Job Preference not met; a Job starting outside the customer's preferred Slot; fewer than 3 Vans on service on a working day; or a working day without Standby cover (FR-71). Overtime has no approval step". FR-66: "The system shall log, with who, what and when: account and role changes, password change requests, and every change to Availability, Crews, Assignments, Jobs and Leave, including overridden warnings. Only the IT Administrator can view the audit log". Review m3 says "add" the operations "invalidateToken()" and "record(user, password changed)" after "setPassword"; m9 says "Split into" the separate "Email Service" and "SMS Gateway" lifelines.

**Decision:** Adopt B2/B3, M1/M3/M4 and m1-m10 as corrections to the DEC-53 draft. Validate and obtain warning confirmation before creating/changing Assignments; cancellation saves nothing. Linked Jobs share the proposed Van/date and are validated together. End previous placements before published moves/unassignments (FR-50). Missing Leave rejection reason makes no change and sends no decision notification. Notify the Crew after a valid Assigned-Job edit, or tell it that an invalidating edit made the Job Unassigned. Record the specified mutations and submitted requests in Audit Log. Referenced fragments use the matching receiving lifeline and an explicit entry message; human confirmation gates connect to the overview's page.

Show status checks before credentials, failed-attempt recording/lockout, authority refusal, concrete account subclasses, single-use reset-token invalidation and password-change audit. Token lifetime and password complexity remain open. Replace alternative labels with guarded branches or a generic edit(details). Propagate optional Late-change/Job-refusal reasons without making them mandatory; apply Late changes per Slot. Check affected Crews before SD-16. Email Service and SMS Gateway realise the existing Email/Phone actor (DEC-48) with separate initial sends and up to three retries on each failed channel. Acknowledgement, deduplication and lapse-notification questions remain open.

Update the class operations to the messages actually used. reject(reason) and refuse(reason) supersede the zero-argument draft calls; no extra mandatory reasons are introduced. complete(details) groups the existing completion fields shown in SD-14. Formatting changes and splits supersede DEC-53's verbatim-source retention for this revision. Boundary/control classes remain analysis responsibilities rather than implementation or stakeholder facts.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** direct instruction to fix the supplied Opus review. Local draft corrections and class views await Opus and human PR review; no commit, push or Google Docs change is performed for this revision.

---


### DEC-57: Consolidate the sequence review into 22 active diagrams

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-04 by the requesting member (identity TBC).

**Source text:** Direct member instruction: "create the consolidated 22 SD instead and output here as a zip file for opus review".

**Decision:** Supersede the 30-diagram presentation in DEC-55 with 22 active diagrams. Withdraw the redundant SD-07, SD-09 and SD-12 overview interactions, retaining their opening/listing steps in the detailed workflows. Fold SD-26 and SD-27 into SD-17 (Form Crews and Standby), SD-28 and SD-29 into SD-20 (Decide Leave Request), and SD-30 warning confirmation into SD-18 (allocation) and SD-19 (publication). Retain SD-17/18/19 for UC-07, SD-20/21/22 for UC-09 and SD-23/24/25 for UC-12. SD-11 calls SD-24 directly for the locked-week route. SD-15 remains reusable notification delivery and SD-16 remains the shared FR-70 interaction with no separate use case.

The active IDs are SD-01 to SD-06, SD-08, SD-10, SD-11 and SD-13 to SD-25. Do not reuse or renumber withdrawn IDs. Their exact earlier sources are archived in diagrams/archive/sequence-r2-2026-10-04/ and listed as Withdrawn in traceability.md. The review ZIP contains only the 22 active sequence sources and their PNG/SVG exports; archive files stay in the repository.

Preserve the adopted Opus corrections in DEC-54/56, including warning confirmation before save, cancellation without changes, the missing Leave rejection reason guard, valid Assigned-Job edit notifications, audit coverage, matched interaction-entry messages and Workshop Servicing conflict handling. Detailed workflows show the applicable human actor and page. Add the corresponding page confirmation operations in CD-boundary; keep the 43 identified classes and domain relationships. These are analysis presentation changes, not additional stakeholder facts. Google Docs, the binding brief and the SRS remain unchanged.

**Decided by:** Requesting member (identity TBC) - **Decision date:** 2026-10-04 - **Decision source:** explicit consolidation request. Opus review and human PR review remain pending; no commit, push or report update.

---


### DEC-58: Adopt round-2 consistency, atomicity and UML corrections

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** diagrams/sequence-diagram-review-round-2.md B1, M1, M3-M5, m1-m11; direct request to follow the review; FR-10/13/17/22/24/25/36/49/62/63/66/70; DEC-53/56/57.

**Decision:** Adopt B1, M1, M3-M5 and m1-m11 in the supplied round-2 critique as corrections to the existing analysis model. SD-15 partitions multi-week events by the affected week and suppresses Draft roster payloads before creating Staff messages or sending email/SMS (FR-49); non-roster request decisions remain visible. Publication delivers after the roster becomes Published.

Leave approval rechecks the remaining working-day balance inside the same atomic save as request status, balance deduction and Crew removal/Needs attention. Serialize the approval check and deduction for each Staff/calendar year, so two non-overlapping four-day requests against seven days cannot both approve (FR-22/25). Validation excludes the selected request from checking overlap with other pending/approved requests. Approved Leave counts as Unavailable (FR-24).

Late-change approval and Certification edit also include affected Crew changes and audit entries in their own atomic save. The callable SD-16 branch joins that transaction and returns events; callers deliver only after commit. Failed submissions preserve prior data under NFR-09. Atomic guards prevent a second decision.

Adopt the review's duplicate rule: at most one Pending Job Rejection Request per Assignment, across Crew members. Decided request history remains unconstrained. SD-25 checks and rechecks eligibility and this constraint inside the save, recomputes less-than-48-hour Short notice and stores its flag. This is an adopted team rule from m9, not a claim that the SRS specified the duplicate policy.

Correct interaction-use scopes, single-line canonical lifeline names, input gates, generic login refusal and invalid confirmation-code handling, initial-email failure/resend, link validation, blank Availability creation, and Draft current-week visibility. Boundary/control operation additions are analysis responsibilities under DEC-53, not infrastructure requirements.

**Recorded by:** OpenAI Codex from the member's instruction to apply Opus round-2 review. Member identity remains TBC. This is a local review draft on CL/sequence-diagrams; no commit, push, merge or Google Docs edit.

---

### DEC-59: Draw clock-driven events within the existing 22 diagrams

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** Direct member reply on 2026-10-05; supplied round-2 review M2/m9; FR-10/63/70; DEC-19/42/51/57.

**Confirmed member choice:** "Keep 22 and add the clock flows to SD-22 and SD-16 (recommended: least impact)".

**Decision:** Keep exactly the active IDs in DEC-57; do not reuse retired SD-26 or introduce SD-31. Clock is an external system-event actor, not a domain class or human User. SD-22 receives a Job-start event at the Job's start time and atomically lapses requests still Pending; it does not wait for Manager action or a polling interval. The Assignment stands. Record a newly saved lapse and notify its requester after commit, adopting M2/m9 and closing the lapse-notification question noted in DEC-56.

SD-16 draws a daily 00:00 Certification-expiry check. The expiry date itself remains valid; the check concerns expiryDate earlier than today (FR-10). Check current/future Crews using the affected Technician and apply FR-70 only where a Crew became invalid. Save Crew removal, Needs attention and audit together; deliver only after commit, subject to SD-15 Draft privacy. The schedule is an analysis choice adopted from the review's 00:00 example, not an interview fact. Retries follow NFR-09.

Clock-driven branches share the existing controllers and interactions. They add no new use case and do not change the 22-diagram count.

**Recorded by:** OpenAI Codex from the member's instruction to apply Opus round-2 review. Member identity remains TBC. This is a local review draft on CL/sequence-diagrams; no commit, push, merge or Google Docs edit.

---

### DEC-60: Remove future Crew membership during account cleanup

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** Direct member reply on 2026-10-05; supplied round-2 review M7; FR-04/05/49/66/70; DEC-17/34/51.

**Confirmed member choice:** "Mark Needs attention (recommended: reuse the existing flag)".

**Decision:** For account deactivation or a Staff-to-Manager role change, remove the person from affected future Crews and mark those Van-days Needs attention. SD-04 saves account changes, future Crew removal, future Assignment removal, Jobs becoming Unassigned and the relevant audit entries atomically. Notify affected Crew members and eligible Standby after commit; SD-15 suppresses any Draft-week roster information.

Keep FR-04/05's removal of future Assignments and Unassigned Jobs. This differs from the FR-70 Leave/Availability/Certification handler, which keeps the Van's Jobs. Therefore SD-04 shares the flag and notification mechanism but does not blindly invoke SD-16. Retain past records (NFR-13); role access still takes effect at next login (FR-04). Existing active-session handling remains an open UC-04 question.

**Recorded by:** OpenAI Codex from the member's instruction to apply Opus round-2 review. Member identity remains TBC. This is a local review draft on CL/sequence-diagrams; no commit, push, merge or Google Docs edit.

---

### DEC-61: Authentication token lifetimes and password complexity

| Category | Analysis design | Ask whom | IT Administrator / Team | Status | **Open** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** Supplied round-2 review B1/m4; UC-01/02; FR-06, NFR-10/11; DEC-41/56.

**Question:** What reset-link lifetime, email-confirmation-code lifetime and password-complexity rules should apply?

**Why it remains open:** FR-06 and NFR-10/11 specify reset/email confirmation and salted password hashing, but do not specify these values. UC-02 and DEC-56 already identify the reset/password questions; the wrong/expired-code branch in SD-01 also needs a configured expiry policy.

**Current representation:** SD-01 and SD-02 validate against the eventual policy without choosing a duration or complexity threshold. Single-use reset tokens remain the adopted DEC-56 behaviour. Resolve with the IT Administrator/team before implementation; the diagrams do not invent values.

**Recorded by:** OpenAI Codex from the member's instruction to apply Opus round-2 review. Member identity remains TBC. This is a local review draft on CL/sequence-diagrams; no commit, push, merge or Google Docs edit.

---

### DEC-62: External notification acknowledgement and deduplication

| Category | Analysis design | Ask whom | Manager / IT Administrator / Team | Status | **Open** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** Supplied round-2 review B1; UC-15; FR-64, NFR-09; DEC-46/48/56.

**Question:** Is accepting an outbound email/SMS request enough, or must delivery acknowledgement be tracked? What identity/time window should suppress duplicate delivery attempts?

**Why it remains open:** FR-64 and NFR-09 define channels and retries, not these transport policies. DEC-56 retained the question.

**Current representation:** SD-15 records accepted/failed channel submission and preserves the Landing Page message after channel failure. It assigns no delivery-acknowledgement or deduplication values. This transport question is separate from DEC-58's adopted one-Pending-request-per-Assignment business constraint and atomic no-second-decision guards. Resolve with the Manager/IT Administrator/team before implementation.

**Recorded by:** OpenAI Codex from the member's instruction to apply Opus round-2 review. Member identity remains TBC. This is a local review draft on CL/sequence-diagrams; no commit, push, merge or Google Docs edit.

---

### DEC-63: Reuse Notification for typed Manager dashboard alerts

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** Supplied round-2 review m12; direct request to adopt review fixes; FR-56/64; DEC-53.

**Decision:** Choose review m12's existing-class option. Notification represents a recipient-specific item with a handled state. Add NotificationKind values DashboardAlert and StaffMessage to the analysis class view.

DashboardAlert represents FR-56 Manager operational alerts, such as Needs attention or Jobs made Unassigned by account changes; SD-10 marks the selected alert handled through alert:Notification. StaffMessage represents the Staff Landing Page event delivered through SD-15 with existing email/SMS channels (FR-64). Typing a Manager alert does not trigger Staff delivery or add a new email/SMS policy.

Keep the per-recipient Staff-or-Manager xor association and the existing 43 identified classes (22 domain, ten boundary, eleven control). An enumeration is a value type, not a new Alert class. Names and traceability are aligned in the same local revision.

**Recorded by:** OpenAI Codex from the member's instruction to apply Opus round-2 review. Member identity remains TBC. This is a local review draft on CL/sequence-diagrams; no commit, push, merge or Google Docs edit.

---

### DEC-64: Suppress delivery of Draft roster events

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** DEC-16, DEC-50, DEC-58; FR-49; supplied round-3 B1; member instruction to apply the review.

**Decision:** Split this rule out of the historical combined DEC-58 decision. Partition notifications by affected week. A roster-related Draft event creates no Staff message and sends no email/SMS. Published roster events and non-roster request decisions deliver after commit. This is a traceability clarification, not a new rule.

**Recorded by:** OpenAI Codex for the member-requested round-3 correction draft. Local branch only; human integration/review pending.

---

### DEC-65: Serialize Leave approval balance checks

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** DEC-13, DEC-58; FR-22/24/25; supplied round-3 B1; member instruction to apply the review.

**Decision:** Split this rule out of DEC-58. Check remaining Leave balance and deduct working days within one serialized approval transaction per Staff/calendar year, together with request status and affected Crew changes. Two four-day requests against seven remaining days cannot both be approved. Insufficient balance leaves the request Pending; this is refusal to approve, not rejection of the request.

**Recorded by:** OpenAI Codex for the member-requested round-3 correction draft. Local branch only; human integration/review pending.

---

### DEC-66: One Pending Job Rejection Request per shared Assignment

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** DEC-39, DEC-42, DEC-58; FR-62/63; supplied round-3 m19; direct member reply on 2026-10-05.

**Decision:** The member confirmed: "One Pending request per Assignment (recommended)". The limit is across the Crew, not per Staff member. Other Crew members see the existing Pending status. SD-25 checks and creates atomically; SD-22 pendingRejectionFor returns zero or one request. Historical decided requests remain. This explicitly confirmed team policy replaces the duplicate-rule citation to the combined DEC-58; it is not claimed to be an interview fact.

**Recorded by:** OpenAI Codex for the member-requested round-3 correction draft. Local branch only; human integration/review pending.

---

### DEC-67: Propagate unassignment to active Linked partners

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** DEC-11, DEC-42; FR-36/37/38/63; supplied round-3 M9; direct member reply on 2026-10-05.

**Decision:** The member confirmed: "Also unassign the active Linked partner (recommended)". If an invalid edit or approved Job Rejection Request unassigns a Job, atomically end the current placements of that Job and its active Linked partners and mark them Unassigned. Cancellation cancels only the selected Job, ends its placement, and unassigns active Linked partners. Completed and already Cancelled partners remain unchanged. Audit each affected placement; notify the requester where applicable, affected Crew and eligible Standby after commit, subject to DEC-64. Keep the links for future same-Van/date allocation. This resolves the Linked-partner ambiguity; it is a member-approved team rule, not a stakeholder quotation.

**Recorded by:** OpenAI Codex for the member-requested round-3 correction draft. Local branch only; human integration/review pending.

---

### DEC-68: Align Clock, UML references and round-3 presentation

| Category | Analysis design | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-05 by the requesting member (identity TBC).

**Source:** DEC-53, DEC-57, DEC-59; supplied round-3 M6/M8 and m1/m13-m22; member instruction to apply the latest review.

**Decision:** Append-only clarification of DEC-59: Clock is the secondary system-event actor for UC-09 Job-start lapse and for FR-10/70 Certification-expiry behaviour. Include it in UC-09 secondary actors and a UCD footnote; no extra use case or sequence diagram. SD-16 is explicitly system behaviour with no UC owner. Keep all existing Withdrawn ID rows under DEC-57. Apply the review's atomic Van-breakdown save/failure handling, publication weekWorkload operation, failed-confirmation-email branch, contiguous reference scopes and single Staff comparison lifeline. The Technician-only certifications operation is dynamically dispatched on that same Staff object when it is a Technician. Shorten presentation labels without changing audit content (who, what, when). DEC-58 remains historical; its three separate business-rule citations are now DEC-64/65/66. No commit, push, main merge or Google Docs change is authorized by this correction work.

**Recorded by:** OpenAI Codex for the member-requested round-3 correction draft. Local branch only; human integration/review pending.

---

### DEC-69: Current Technician questionnaire and focused refinements

| Category | Team adoption / analysis refinement | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-07 by the requesting member (identity TBC).

**Source:** [Current Technician questionnaire](elicitation/interviews/technician-questionnaire.md), primary Sheet A1:AA12; D2/C13/C16/C18, especially DB01/DB02. The member instructed: "perform the updates" and "focused on only the necessary diagrams/content" after the read-only impact assessment.

**Decision:** Use the latest questionnaire for current Technician findings; retain the old DCT transcript and historic decisions as history. Adopt original/proposed Availability and Pending/decision visibility, contextual notification content with a current-details link, and per-Job completion/photo upload feedback with retained retry data and no duplicate completion or Workload credit. A completion is confirmed only when its required evidence is saved. Recheck completion state/authority at save time and distinguish local queuing from server completion. Clarify that an emergency move validates all affected Crews, including the original Crew. These refine FR-17, FR-64, NFR-08 and existing FR-30/32/38/39/44/53 without new UCs, actors, domain classes or numeric thresholds. Preserve optional refusal reasons and existing offline-conflict questions until DEC-70 is answered.

**Recorded by:** OpenAI Codex for the member-authorized focused update. No fabricated interview metadata, commit or push.

---

### DEC-70: Additional questionnaire requests outside the retained baseline

| Category | Scope / policy clarification | Ask whom | Manager / team | Status | **Open** |
|---|---|---|---|---|---|

**Raised:** 2026-10-07 while reconciling the latest Technician questionnaire.

**Source:** Current questionnaire C6/C8/C10/C11/C13/C16/C18; existing DEC-47/56/61/62 and UC-13/14 open questions.

**Questions:** Are pre-deadline reminders required, and with what timing, recipients and channels? Should daily Workload totals, assigned/completed counts or Availability/Leave overlays be added after optional statistics were removed? Should request-history timestamps and mandatory Late Availability rejection/Job Rejection refusal reasons be added? How should exact-hour Availability responses map to the adopted half-day Slots? How is an offline queued completion reconciled if its Job or Crew changes, or another Technician completes it before upload? Confirm questionnaire timestamp locale and the participant-ID-to-attendance mapping before asserting names or dates.

**Current boundary:** Displayed deadlines, existing weekly/monthly totals, required Leave rejection reasons, optional other refusal reasons and the current Slot model remain. Do not invent reminder schedules, statistics, conflict-resolution policy or attendance. Per-Job upload states and duplicate prevention adopted in DEC-69 do not settle the remaining conflict policy.

**Recorded by:** OpenAI Codex; awaiting a team decision.

---

### DEC-71: Invalidate all outstanding reset tokens after successful password reset

| Category | Account safeguard / team policy | Ask whom | Team / IT Administrator | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-10-07 by the requesting member (identity TBC).

**Source:** Member's UC-02 resubmission review and explicit instruction to "follow through with the reccomendation and update the diagram"; FR-06, DEC-56 and DEC-61.

**Decision:** A successful password reset atomically validates the supplied reset token, saves the new salted password hash and invalidates **all outstanding password-reset tokens for that Account**, including earlier emails. The password change is audited. Resubmission can issue another reset link; it does not itself revoke previous links. Once any reset succeeds, no token issued before that save can reset the password again. Concurrent reset attempts recheck validity within the same atomic save, so an already invalidated token cannot commit. A failed transaction preserves the prior password and token state. Token lifetime, password complexity and device-confirmation-code policy remain open under DEC-61. This is a member-approved safeguard, not an attributed stakeholder statement.

**Recorded by:** OpenAI Codex for the authorized focused update; no commit or push.

---

## M. M1 report alignment (2026-11-07)

| ID | Topic | Category | Ask whom | Status |
|---|---|---|---|---|
| DEC-72 | The submitted M1 report is the M1 source of truth; repo IDs follow it | Team decision | Team | **Decided** |

### DEC-72: The submitted M1 report is the M1 source of truth; repo IDs follow it

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-07 by JunKeatLim.

**Source text:** JunKeatLim, 2026-11-07: "after the initial M1 report draft, we made multiple changes to the report but not the repo. I have uploaded the final M1 report that we submitted. ... refer to the M1 report and use it as the source of truth. anything that is not in the report (i.e FR requirements) or any contradictions in rules, inconsistencies in numbering, etc fix it all based on the report."

**Question:** The repo (SRS v3.4, 22 SDs) and the submitted report (9 Oct 2026) use different requirement and diagram numbers and slightly different wording. Which governs?

**Decision:**
1. The **submitted M1 report** (INF2001 P8-1 M1 Report, 9 Oct 2026) is the source of truth for M1 artefacts. Where the repo and the report differ, the repo is changed to match the report.
2. **Requirements:** the repo uses the report's FR-01–FR-50 and NFR-01–NFR-12 with the report's wording, groups and priorities (SRS v3.5). Source and Test columns are kept from the repo. Draft IDs that were withdrawn before submission are dropped from the active SRS; requirements.md §9 maps every draft ID.
3. **Use cases:** UC-01 to UC-15 are transcribed from report §3.2. The repo's Source rows are kept.
4. **Sequence diagrams:** the report's SD-01 to SD-21 numbering and titles. The draft SD-18 Allocate Job is not in the report and is archived (`diagrams/archive/pre-report-2026-10-09/`). The report and its AI declaration say "21 sequence diagrams", which replaces DEC-57's 22.
5. **Glossary, WBS, AI declaration:** AGENTS.md and the root files `Glossary.md`, `WBS and Timeline.md` and `AI Usage Declaration.md` follow report Tables 1.2, 1.3, 5.1 and 5.2. The team is 6 members (report cover), not 5. File owners follow the report WBS (Table 5.1), pending team confirmation.
6. **ID rule:** this is a one-off renumbering to match the submitted report. From this baseline on, IDs are never reused or renumbered. DEC-01 to DEC-71, the sequence-review notes, the archives, `requirements-review.md`, `phases.md` and `M1 Report Gap Analysis.md` are history and keep their draft IDs.

**Known report issue (not changed):** report Figure 4.8 (SD-07) labels its Compare Staff reference "SD-08"; in the report's own numbering Compare Staff is SD-09. The repo source uses SD-09.

**Decided by:** JunKeatLim · **Decision date:** 2026-11-07 · **Decision source:** direct instruction in a Claude Code session, 2026-11-07; submitted M1 report.

## N. M2 design update (2026-11-06)

These entries apply on top of the M1 report baseline (DEC-72) and use its IDs. They record the team's M2 Design Update Brief ([m2/design-update-brief.md](m2/design-update-brief.md), cited as `M2-Brief §<n>`) and the answers JunKeatLim gave on 2026-11-06 to the open points it raised. M2-Brief §1–§4 are final team decisions. Where JunKeatLim delegated a point ("do whatever you think is suitable"), the entry says so and the choice was proposed by Claude Code. All entries stay open to change at team review. Earlier entries are not edited; where an entry below replaces one, the earlier entry's index status is updated.

| ID | Topic | Category | Ask whom | Status |
|---|---|---|---|---|
| DEC-73 | M2 scope: schedule planning only | Team decision | Team | **Decided** |
| DEC-74 | External data enters by CSV upload | Team decision | Team | **Decided** |
| DEC-75 | Certification is Brand and expiry only | Team decision | Team | **Decided** |
| DEC-76 | No Job completion; two Job statuses; cancelled Jobs are deleted | Team decision | Team | **Decided** |
| DEC-77 | Zones, Job zone from postal code, home zone | Team decision | Team | **Decided** |
| DEC-78 | Workload is planned hours, Standby hours and Manager edits | Team decision | Team | **Decided** |
| DEC-79 | Standby Preference replaces Job Preference | Team decision | Team | **Decided** |
| DEC-80 | Crew-forming algorithm suggests the roster | Team decision | Team | **Decided** |
| DEC-81 | Standby cover and Standby activation | Team decision | Team | **Decided** |
| DEC-82 | Drivers are outside the scheduling logic | Team decision | Team | **Decided** |
| DEC-83 | Availability is per working day, 1 month in advance | Team decision | Team | **Decided** |
| DEC-84 | Crew Brand coverage is flexible; Crews stay together all day | Team decision | Team | **Decided** |
| DEC-85 | Van count comes from the van CSV; no Van entity | Team decision | Team | **Decided** |
| DEC-86 | Two 40-hour boundaries | Team decision (delegated) | Team | **Decided** |
| DEC-87 | Derive values instead of storing them | Team decision (delegated) | Team | **Decided** |
| DEC-88 | Notification triggers and non-human delivery actors | Team decision | Team | **Decided** |
| DEC-89 | Audit Log scope, on-site storage and 12-month purge | Team decision | Team | **Decided** |
| DEC-90 | Retire Linked Jobs, Short notice, Needs attention and Leave balance | Team decision (delegated) | Team | **Decided** |
| DEC-91 | M2 use-case structure | Team decision | Team | **Decided** |
| DEC-92 | ID policy for M2 and the report's numbering | Team decision (delegated) | Team | **Decided** |
| DEC-93 | Architecture and design pattern | Team decision (delegated) | Team | **Decided** |
| DEC-94 | M2 testing targets; close DEC-21 and DEC-26 | Rubric | Team | **Decided** |
| DEC-95 | M2 report numbering and §1.2 content | Rubric | Team | **Decided** |

### DEC-73: M2 scope: schedule planning only

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §2: "The system is **primarily focused on schedule planning**. Nothing else." It lists as outside the system: "job completion", "leave applications and approvals", "overtime approval (settled between the manager and the technician)", "van management and van servicing", "contacting standbys when they are activated (manager phones them)". M2-Brief §1 records the lecturer's M1 feedback that "Too much unnecessary data was stored (certificate numbers, van licence plates, workshop servicing, job completion details)".

**Decision:** The system plans and publishes Weekly Rosters and shows Workload. Job completion, Leave applications and approvals, Late Availability Change Requests, Overtime approval, van management, Workshop Servicing and phoning Standby Staff all happen outside the system. Requirements and classes for them are Withdrawn (DEC-92).

**Replaces:** the in-system parts of DEC-02 (late-change request), DEC-13 (Leave Requests and balance), DEC-14 (Workshop Servicing), DEC-40 (completion evidence). DEC-32 already kept Overtime approval out of scope.

**Decided by:** Team (M2-Brief §1–§3) · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §2, §3.1; confirmed by JunKeatLim in a Claude Code session, 2026-11-06.

---

### DEC-74: External data enters by CSV upload

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §2: "The manager downloads a CSV from each external system and uploads it into our system: **HR system CSV:** who is on leave / emergency leave / MC, and on which dates. **Van vendor CSV:** how many vans are available on each date." "The HR system and the van vendor are **not actors** in our use case diagram". M2-Brief §7 left the upload deadline, re-uploads and bad files open.

**Decision:**
1. The Manager uploads two CSV types (UC-16). An HR CSV creates read-only **Leave Records** (Technician or Driver, date, type: Leave, Emergency Leave or MC). A van CSV creates **Van Availability** (date, number of Vans available).
2. HR and the van vendor are not actors. The Manager is the only actor.
3. **Timing (JunKeatLim, 2026-11-06):** the Manager uploads both files before planning the week, which is the Thursday after the Availability Deadline (DEC-02). The system does not enforce an upload deadline. It warns at planning time when no van CSV covers a day of the Planning Week.
4. **Bad files (delegated):** the whole file is validated before anything is saved. Missing columns, unknown Staff, unknown dates or types, a negative Van count, or an empty file reject the whole file and list each row error. Duplicate rows are saved once.
5. **Re-upload (delegated):** a later file of the same type replaces the records for the dates it contains.
6. **Clash assumption (JunKeatLim, 2026-11-06):** Leave is booked well ahead and Standby picks are made in the week before planning, so an upload is assumed not to add Leave on a day where the person already has a Standby pick or a Crew place. If it does, Leave wins (M2-Brief §3.4) and the Manager fixes the roster through UC-17. The report states this as an assumption.

**Decided by:** Team (M2-Brief §2); items 3 and 6 by JunKeatLim; items 4 and 5 delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §2, §3.2, §7; Claude Code session, 2026-11-06.

---

### DEC-75: Certification is Brand and expiry only

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.7: "Store only **Brand** and **expiry date** per technician." "The system blocks placing a technician in a crew for a brand whose certification has expired." M2-Brief §5.1: "IT Administrator | Keep | Creates accounts, sets home zone and certifications at creation".

**Decision:** The certificate number is removed. A Certification holds Brand and expiry date, and is valid for a date when the expiry date is on or after that date. The IT Administrator enters Certifications and home zone at account creation and **also updates them later** (UC-04, delegated). This replaces DEC-35's "the Manager maintains them afterwards", so that one role owns the update method.

**Decided by:** Team (M2-Brief §3.7); the later-update owner delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §3.7, §5.1; Claude Code session, 2026-11-06.

---

### DEC-76: No Job completion; two Job statuses; cancelled Jobs are deleted

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.1: "No actual start/end time, remark, follow-up flag or invoice photo. No "Completed" job status." M2-Brief §3.2: "**Job status** | Only **Assigned** or **Unassigned**." "When a customer cancels, the job is **deleted**. Affected staff are notified."

**Decision:** A Job is Unassigned or Assigned. A customer cancellation deletes the Job, and its Crew is notified first. Past and in-progress Jobs cannot be deleted. They are kept until the 12-month purge (DEC-89). UC-14 Complete Job is Withdrawn.

**Decided by:** Team · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §3.1, §3.2.

---

### DEC-77: Zones, Job zone from postal code, home zone

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §1: "Zones were missing. Singapore should be divided so vans don't travel across the island." M2-Brief §3.2: "Jobs are sorted into **North, East, South, West, Central**. The manager decides which zone each van/crew covers; the algorithm does not." "**Home zone** | New attribute on every technician. Used to find the closest standby." M2-Brief §7 asked how a Job gets its zone.

**Decision:**
1. Zones are North, East, South, West and Central.
2. **A Job's zone is derived from its postal code (JunKeatLim, 2026-11-06)** using a fixed table from the 2-digit postal sector to a Zone. The Manager does not type it.
3. Every Technician has a home zone, set by the IT Administrator.
4. The Manager sets each Crew's zone. Allocating a Job to a Crew whose zone differs from the Job's zone raises a warning, not a block (delegated).
5. **Zone distance (delegated, †):** 0 for the same zone. 1 when either zone is Central, or for the adjacent pairs North–East, North–West, South–East and South–West. 2 for the opposite pairs North–South and East–West.
6. A Technician's location on a date (Brief R5) is shown as their Crew's zone that day, or their home zone if they are not in a Crew. This replaces DEC-08's postal-district list.

**Decided by:** Team (M2-Brief §3.2); item 2 by JunKeatLim; items 4 and 5 delegated to Claude Code · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §1, §3.2, §7; Claude Code session, 2026-11-06.

---

### DEC-78: Workload is planned hours, Standby hours and Manager edits

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §1: "Hours must be tracked on **planned** time, not actual time (people could stall to inflate hours)." M2-Brief §3.3: "**Workload** = a technician's **active hours**: planned job hours + activated standby hours + manager edits." "An **unused standby day** counts as **half hours** (e.g. 4 h for an 8 h day)." "If a standby is **activated**, the actual hours entered by the manager **replace** the half hours (not added on top)." "**Leave does not count as hours.**" "Half hours **do** count toward the 40-hour highlight."

**Decision:** A Staff member's hours for one working day are:
1. the latest **Hours Edit** for that person and date, if the Manager recorded one; otherwise
2. in a Crew: the Planned Hours of every Job assigned to that Crew that day (duration + 0.5 h Travel Allowance, DEC-31); otherwise
3. on Standby and not activated: **4 h** (half of the 8 h working day 09:00–18:00 less lunch, DEC-12); otherwise
4. 0 h (Leave, not working, or a Driver not in a Crew).

Workload is the sum of these over a Planning Week (Monday–Saturday) or a calendar month. Actual Hours are removed. When a Standby is activated, the Manager enters the hours worked as an Hours Edit, which replaces the 4 h (UC-17). This replaces DEC-40, the 0 h Standby rule in DEC-43, and the completed-work credit in DEC-39.

**Decided by:** Team · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §1, §3.3, §4 step 10 and 13.

---

### DEC-79: Standby Preference replaces Job Preference

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** Brief R9: "Staff can indicate their job preference for the week". M2-Brief §1: "Job preferences were "one-sided": the system accepted preferences it could not guarantee. If the system offers a preference, it must follow it." M2-Brief §3.4: "The only preference is the **standby day**: each technician picks **one standby day per week**." "Each day allows **at most 2 picks: one M Electric slot and one Dicon slot**, first come first served. A dual-brand technician can take either slot. Once both slots are taken, that day is greyed out." "Priority order: **leave / emergency leave / MC > preference pick > normal standby**."

**Decision:**
1. A Technician may make one **Standby Preference** per Planning Week: a working day and a Brand slot (M Electric or Dicon).
2. A pick is accepted only if all of these hold:
   - it is made before the Availability Deadline;
   - the Technician is Available that day with no Leave Record;
   - they hold a valid Certification for the chosen Brand on that day;
   - that Brand slot on that day is still free.
3. A Technician may change or withdraw their pick before the deadline, which frees the slot.
4. **Timing (JunKeatLim, 2026-11-06):** picks close with Availability at the Availability Deadline (DEC-02), so they are known when planning starts on Thursday.
5. Every accepted pick is followed. The algorithm never pulls a pick into a Crew (DEC-80). A Manager who moves a pick into a Crew must override a warning, and the override is logged.
6. **R9 argument (JunKeatLim, 2026-11-06):** the standby day is the Technician's weekly preference for which day they do not drive out on Jobs. The report must state that this is how R9 is met, and why: an advisory preference the system cannot guarantee was criticised at M1.

This replaces DEC-07 (Job Preference). Drivers do not make Standby Preferences (DEC-82).

**Decided by:** Team (M2-Brief §3.4); items 4 and 6 by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §1, §3.4; Claude Code session, 2026-11-06.

---

### DEC-80: Crew-forming algorithm suggests the roster

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §4: "The algorithm **suggests** a roster. The **manager reviews, edits and publishes** it (the brief says the manager allocates; the algorithm only assists)." Steps 3–11 as written there. JunKeatLim, 2026-11-06, on step 8: "if there is not enough to form 3 available crews, it will pick the staff that are ranked low on the algorithm", and confirmed option (a), the bottom of the ranking first.

**Decision:** For each working day of the Planning Week, in date order, the system:
1. Excludes Technicians with a Leave Record or without Availability that day.
2. Puts that day's Standby Preference picks on Standby (source Preference).
3. Puts Dual-Certified Technicians whose **last week's Workload is 20 h or more** on Standby (source Algorithm, treated as based in Central).
4. Ranks the remaining Technicians by:
   - projected hours this week: under 40 h first, 40 h or more last (DEC-86);
   - then last week's Workload, lowest first;
   - then projected hours this week, lowest first;
   - then staff ID.

   New staff count as 0 h.
5. Forms Crews from the top of the ranking. A Dual-Certified Technician forms a Crew alone. Otherwise the top Technician is paired with the highest-ranked Technician of the other Brand. It stops when:
   - the Van count for that day is reached (DEC-85);
   - no other Crew covering both Brands can be formed; or
   - after the third Crew, forming one more would leave Standby without cover for both Brands (DEC-81).
6. If fewer than 3 Crews were formed, it returns Standby Staff of source Algorithm, then Leftover, to the pool, **lowest-ranked first** (JunKeatLim, option (a)), and repeats step 5 until there are 3 Crews or the pool is used up. It never uses a Preference pick or anyone on Leave. If there are still fewer than 3 Crews, the Manager is warned (FR-33).
7. Puts everyone left on Standby (source Leftover).
8. Assigns one available Driver to each Crew in staff-ID order (DEC-82).
9. Adds **projected hours** before the next day: **8 h† per Crew day and 4 h per Standby day** (delegated). Jobs are usually not yet allocated when Crews are suggested, so a full working day is the estimate. Real Workload is recalculated from Assignments (DEC-78).

The suggestion is a Draft. The Manager then sets each Crew's zone, edits Crews and Standby, allocates Jobs and publishes. Every change to the suggestion is logged as an override (DEC-89). The Manager may run the suggestion again for a Draft week, which replaces the unedited suggestion.

**Decided by:** Team (M2-Brief §4); step 6 order by JunKeatLim; steps 5 (stop rules), 8 and 9 delegated to Claude Code · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §3.5, §4; Claude Code session, 2026-11-06.

---

### DEC-81: Standby cover and Standby activation

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.5: "**Standby** = technicians who are available but were not placed in a crew that day." "**Minimum standby per day:** one team covering both brands (1 M Electric + 1 Dicon, or 1 dual). No maximum." "If there are not enough people for both 3 crews and a standby team, **3 crews win**." "The system tracks each technician's **activation count** over a **rolling 12 months**". M2-Brief §4 steps 12–13.

**Decision:**
1. A Standby is a Technician not in any Crew on a working day, with source Preference, Algorithm, Leftover or Manager.
2. Full cover means the day's Standby Technicians hold valid Certifications for both Brands. Missing cover is a warning (FR-33). There is no maximum number of Standby Staff.
3. When a Crew member drops out, the Manager opens the Standby list for that day and the affected Job's zone. The list is ordered by:
   1. fewest activations in the last 12 months;
   2. zone distance (DEC-77) from the Standby's zone to the Job's zone, where the Standby's zone is Central for source Algorithm and the home zone otherwise;
   3. staff ID.
4. The Manager phones the person outside the system, then records the change in UC-17:
   - who replaces whom;
   - the hours worked by each, as Hours Edits;
   - the activation, which ends that person's Standby place that day and adds one to their activation count.

   The affected Staff are notified.
5. The activation count is **counted** from activated Standby records dated in the last 12 months, not stored as a number (DEC-87).

This replaces DEC-43 (Manager-named Standby with 0 h and a Standby Driver).

**Decided by:** Team (M2-Brief §3.5, §4); ordering tie-break and the counted activation delegated to Claude Code · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §3.5, §4; Claude Code session, 2026-11-06.

---

### DEC-82: Drivers are outside the scheduling logic

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.6: "Drivers are deliberately kept simple: **assumed always available, one per van**. The system's scheduling logic (ranking, preferences, standby) applies to **technicians only**. State this explicitly as an assumption in the report." Brief R8: "Staff can add and edit their availabilities".

**Decision:**
1. **Assumption:** enough Drivers are available every working day. The report states this.
2. Each Crew has exactly one Driver. The suggestion fills Drivers in staff-ID order from those Available that day with no Leave Record, and the Manager may change them.
3. Drivers are not ranked, make no Standby Preference and are never on Standby.
4. Drivers still enter Availability, which keeps R8 for all Staff, and the suggestion uses it (delegated).
5. Driver Workload follows DEC-78 and is shown with the Technicians'.

**Decided by:** Team (M2-Brief §3.6); item 4 delegated to Claude Code · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §3.6; Claude Code session, 2026-11-06.

---

### DEC-83: Availability is per working day, 1 month in advance

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §5.1: "Staff still indicate availability up to 5 weeks ahead (brief requirement 8)." JunKeatLim, 2026-11-06: "Keep it to 1 month in advance, no more 5 weeks ahead." M2-Brief §3.2: "Crews | Stay together **all day**."

**Decision:**
1. The horizon stays **1 month in advance** (DEC-01, DEC-30). The "5 weeks" in M2-Brief §5.1 is superseded.
2. Because Crews work the whole day, Availability is set **per working day** (`Available` or `Unavailable`), not per Slot (delegated). A day with no entry is Not submitted and counts as unavailable (DEC-03).
3. Slots remain only as a Job's preferred time.
4. Availability locks at the Availability Deadline (DEC-02). A later change is handled outside the system, so the Late Availability Change Request is Withdrawn.

**Decided by:** Item 1 by JunKeatLim; item 2 delegated to Claude Code; item 4 by the team (M2-Brief §3.1) · **Decision date:** 2026-11-06 · **Decision source:** Brief R8 + Lecturer clarification; M2-Brief §3.1, §3.2; Claude Code session, 2026-11-06.

---

### DEC-84: Crew Brand coverage is flexible; Crews stay together all day

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** Brief §Company ¶3: "Each van is made up of one driver and a qualified technician for each brand. Unless the van is servicing or installing only a particular brand, then one driver and a qualified technician for the brand." M2-Brief §4 step 7: "Each crew must **cover both brands**". JunKeatLim, 2026-11-06: "i think this is suppose to be flexible". M2-Brief §3.2: "Crews | Stay together **all day**. They **can go home** after their last job (no reporting back to base)."

**Decision:**
1. A Crew is one Driver and one or two Technicians for one Van on one working day.
2. Together, its Technicians must hold valid Certifications for **the Brand of every Job assigned to it**. A single-Brand Crew is therefore allowed when all its Jobs are that Brand.
3. The suggestion still forms Crews covering both Brands by default (DEC-80).
4. A Crew stays together for the whole day. Members go home after the last Job, so the system stores no end-of-day location.

**Decided by:** Item 2 by JunKeatLim; the rest by the team · **Decision date:** 2026-11-06 · **Decision source:** Brief §Company ¶3; M2-Brief §3.2, §4; Claude Code session, 2026-11-06.

---

### DEC-85: Van count comes from the van CSV; no Van entity

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.1: "Van details (number, licence plate), the Van list and the Workshop Servicing rotation are removed. Van availability comes from the vendor CSV." Brief §Company ¶4: "at least three vans can be on service daily except for Sunday". JunKeatLim, 2026-11-06: "We have a schedule set that ensures there to be at least 5 vans at all times, so just assume we will not have lesser than 3 vans avail. But 3 available crews is a different thing."

**Decision:**
1. The system stores no Van identity or plate.
2. For each date, the number of Vans available comes from the van CSV and caps the number of Crews that day.
3. Crews are numbered **Van 1 … n** per day (delegated).
4. **Assumption:** the company's own servicing schedule keeps at least 5 Vans available, so at least 3 are always available. The "at least 3 Vans on service" check concerns Crews (DEC-80), not Vans.

This replaces DEC-14.

**Decided by:** Item 4 by JunKeatLim; item 3 delegated to Claude Code; the rest by the team · **Decision date:** 2026-11-06 · **Decision source:** Brief §Company ¶4–5; M2-Brief §3.1; Claude Code session, 2026-11-06.

---

### DEC-86: Two 40-hour boundaries

| Category | Team decision (delegated) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim.

**Source text:** Brief R6: "highlight all staff over 40 hours of jobs allocated". DEC-04: "**strictly above 40 hours** is Overtime and is highlighted". M2-Brief §4 step 6: "anyone at **40 h or more** goes to the **bottom**".

**Decision:** Two rules with two purposes, each stated in its own requirement:
- **Highlight (R6):** Workload **strictly above 40 h** in a Planning Week. 40.0 h is not highlighted and 40.5 h is.
- **Ranking (algorithm):** projected hours this week of **40 h or more** go to the bottom, because that person has already reached the target.

**Decided by:** Delegated to Claude Code by JunKeatLim ("the rest just do whatever you think is suitable") · **Decision date:** 2026-11-06 · **Decision source:** Brief R6; DEC-04; M2-Brief §4.

---

### DEC-87: Derive values instead of storing them

| Category | Team decision (delegated) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim.

**Source text:** M2-Brief writing rules: "If no decision depends on a piece of data, do not store it (PDPA principle: don't collect what you don't need)." M2-Brief §5.1 suggests storing "homeZone, lastWeekHours, currentWeekHours, activationCount" on Technician and "basedInCentral (for duals)" on Standby.

**Decision:** Only `homeZone` is stored. These values are **computed by methods** from records that already exist, so they cannot fall out of step:
- last week's hours and this week's hours (from Assignments, Standby records and Hours Edits);
- the activation count (from activated Standby records in the last 12 months);
- "based in Central" (from Standby source = Algorithm).

**Decided by:** Delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief writing rules, §5.1.

---

### DEC-88: Notification triggers and non-human delivery actors

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.2: "Sent for the **initial roster publication and every later change** (roster changes, job changes, deletions, standby assignment, job rejection outcomes)." "**Notification class** | New/explicit class to back FR-40–42." M2-Brief writing rules: "External services (Email/SMS) are **non-human actors**, not stick figures."

**Decision:**
1. Staff are notified on their Landing Page, by email and by SMS (DEC-46, DEC-48) when:
   - a week with their Assignments or Standby days is published;
   - after publication, one of their Assignments, Crew places or Standby days is added, changed or removed;
   - one of their Jobs is deleted;
   - a Job Rejection Request they made is decided or lapses;
   - the Manager records an Hours Edit for them.
2. The Manager is notified when a Job Rejection Request is submitted.
3. Each message is a stored Notification.
4. **Email Service** and **SMS Gateway** are drawn as «system» actors (rectangles), not stick figures. The system sends through the `NotificationChannel` interface.

**Decided by:** Team; the Hours-Edit trigger delegated to Claude Code · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §1, §3.2; DEC-46; DEC-48.

---

### DEC-89: Audit Log scope, on-site storage and 12-month purge

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §3.2: "Every hours edit and every manager override of the suggested roster is logged: who, what changed, why, when." "Records and logs are saved on an **on-site server backend** (persistent storage)." "Records and logs are kept for a **rolling 12 months**, then purged."

**Decision:**
1. The Audit Log records who, what, when and, where one applies, why. It covers:
   - account and role changes;
   - Technician profile changes;
   - CSV uploads;
   - suggestion runs and every Manager change to a suggested or published roster, each change with a reason;
   - Hours Edits and Standby activations;
   - Job creation, edits and deletion;
   - Job Rejection decisions.
2. The data lives in a database on an on-site server.
3. A daily **Retention Job** purges records and log entries dated more than 12 months ago. This makes DEC-34's "may then be purged" a "must".

**Decided by:** Team · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §3.2; DEC-34.

---

### DEC-90: Retire Linked Jobs, Short notice, Needs attention and Leave balance

| Category | Team decision (delegated) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim.

**Source text:** M2-Brief §1: "Every tracked value needs an owning class and a method." The M2-Brief does not mention Linked Jobs, Short notice, Needs attention or the Travel Allowance.

**Decision:**
- **Linked Jobs (DEC-11, DEC-67) are retired.** The Manager places two Brands at one address on the same Crew by hand.
- **Short notice (DEC-52) is retired.** No decision depends on it.
- **Needs attention (DEC-19, DEC-51) is retired.** Its triggers (Leave approval, late changes, Certification expiry inside a Crew) no longer happen inside a published week under DEC-73 and DEC-74. Changes are made through UC-17.
- **Leave balance (DEC-13) is retired** (DEC-73).
- **The 0.5 h Travel Allowance (DEC-31) is kept.** It is part of Planned Hours and needs no stored data.

**Decided by:** Delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §1, §3; Claude Code session, 2026-11-06.

---

### DEC-91: M2 use-case structure

| Category | Team decision | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by JunKeatLim.

**Source text:** M2-Brief §5.4: "**Remove:** UC-06 Manage Vans and Workshop Servicing; UC-14 Complete Job; leave-approval and late-availability parts of UC-09 / UC-12. **Add:** Upload CSV; Edit Hours / Update Roster; Set Standby Preference (replaces the preference part of UC-11)." "Re-check every «extend» for genuine optionality." M2-Brief §1: "check whether «extend» relationships are genuinely optional (Login → Reset Password, Allocate Jobs → Compare Staff)".

**Decision:**
1. UC-06 and UC-14 are Withdrawn.
2. New use cases: **UC-16 Upload CSV** (Manager), **UC-17 Update Roster and Hours** (Manager) and **UC-18 Set Standby Preference** (Technician).
3. Narrowed use cases:
   - UC-09 becomes **Decide Job Rejection Request**;
   - UC-11 becomes **Set Availability**;
   - UC-12 becomes **Submit Job Rejection Request**.
4. **«extend» check (delegated):**
   - **UC-02 Reset Password becomes a standalone use case** of User. A user starts it from the login page without logging in, and it does not continue or change the login, so it is not an extension of UC-01.
   - **UC-08 Compare Staff keeps «extend» to UC-07.** Allocating needs no comparison, and the Manager optionally opens it at the extension point "Compare Staff".
5. UC-15 Notify Staff is included by UC-05, UC-07, UC-09 and UC-17. Its actors are the «system» actors Email Service and SMS Gateway, which replace the combined "Email/Phone" stick figure.
6. Email Service also serves UC-01 (new-device confirmation), UC-02 and UC-03.
7. HR and the van vendor are not actors.

The 18 IDs give 16 active use cases.

**Decided by:** Team (M2-Brief §5.4); item 4 and the new names delegated to Claude Code · **Decision date:** 2026-11-06 · **Decision source:** M2-Brief §1, §5.4; Claude Code session, 2026-11-06.

---

### DEC-92: ID policy for M2 and the report's numbering

| Category | Team decision (delegated) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim; revised 2026-11-07 after DEC-72.

**Source text:** AGENTS.md: "**IDs are never reused or renumbered.** Mark a dropped item `Status: Withdrawn` and keep its row." M2-Brief §5.4: "Renumber FRs and update every trace reference after removals." M2-Brief §1 cites the lecturer's feedback using "FR-47 (forgotten password), FR-46 (keeping past records), FR-10 (12-month tracking) and FR-40–42 (notifications)".

**Decision:**
1. M2 keeps the **submitted M1 report's IDs** (DEC-72), because they are the numbers the lecturer marked and quoted.
2. Removed items are marked Withdrawn in place. New items take the next free ID: FR-51 onwards, NFR-13 onwards, UC-16 onwards.
3. Report §1.2 lists the active requirements and an "Updates from M1" table (SRS §9) of every withdrawn, changed and new ID. This meets the brief's "renumber and update trace references" goal without changing numbers the lecturer has already seen.
4. The lecturer's references now match: FR-47 is password reset (backed by PasswordResetToken, FR-47 in v4.0); FR-46 is leaver records and NFR-10 is 12-month retention (backed by RetentionJob, FR-58); FR-39 and FR-40 cover notifications (backed by Notification and NotificationService).

**Team check:** the lecturer's "FR-10 (12-month tracking)" does not match the report's FR-10 (post-publication changes). It most likely means NFR-10 (data retention). Confirm with the lecturer if it matters for the resubmission.

**Decided by:** Delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-07 · **Decision source:** AGENTS.md ID conventions; DEC-72; M2-Brief §1, §5.4.

---

### DEC-93: Architecture and design pattern

| Category | Team decision (delegated) | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim.

**Source text:** Report template §3.2: "Identify and evaluate ONE design patterns that are applicable to your system." Rubric M2 Detailed Design: "ONE (1) suitable design pattern that addresses an identified design problem in the system". JunKeatLim, 2026-11-06: "Prioritise the Milestone 2 template since that is the format the professor wants." M2-Brief §6.1–§6.2.

**Decision:**
1. **Architecture:** layered (3-tier) with MVC in the web tier, on one on-site server:
   - Presentation (the «boundary» pages are the Views);
   - Application (the «control» classes are the Controllers and services);
   - Data (the «entity» classes are the Model, held in the on-site database).
2. **Design pattern for report §3.2: Strategy.**
   - Interface: `TechnicianRanking`.
   - Concrete strategies: `WorkloadRanking` (crew forming) and `ActivationRanking` (Standby activation).
   - Contexts: `CrewFormingService` and `StandbyActivationService`.
   - Problem solved: two fairness orderings that the client may change, kept out of the algorithm code.
3. `CsvRowMapper` and `NotificationChannel` are also «interface» classes in the final class diagram. They are not written up as patterns.

**Decided by:** Delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** brief/report-template-m2.md §3; brief/rubric-m2.md; M2-Brief §6.

---

### DEC-94: M2 testing targets; close DEC-21 and DEC-26

| Category | Rubric | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim.

**Source text:** Report template §4.1: "design the decision table black box testing". §4.2: "The selected methods for 4.1 and 4.2 should be different. Write the pseudocode for the method." Rubric M2 Whitebox: "a CFG containing at least eight nodes and two decision points". §5: "Provide wireframe screenshots for all implemented use cases."

**Decision:**
1. **Black box (decision table):** `StandbyPreferenceController.submitPick()` (FR-51).
2. **White box (pseudocode, CFG, cyclomatic complexity, basis paths):** `CrewFormingService.classifyTechnicians()` (FR-54 steps 1–4).
3. The EP/BVA targets in M2-Brief §6.3 are kept as extra test notes, not as the report's method.
4. **DEC-21 is answered:** M2 delivers wireframes and pseudocode, not a working app.
5. **DEC-26 is answered:** the template was received on 2026-11-06 ([brief/report-template-m2.md](brief/report-template-m2.md)).

**Decided by:** Delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** brief/report-template-m2.md §4–§5; brief/rubric-m2.md.

---

### DEC-95: M2 report numbering and §1.2 content

| Category | Rubric | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Raised:** 2026-11-06 by Claude Code for JunKeatLim.

**Source text:** The template's table of contents lists "1.4 Component Diagram", but its body has "2 Component Diagram", "3 Detailed Design", "4 Testing" and "5 Wireframe". Rubric M2 B.1.1 Introduction: "Description of updates from M1 (if any)", "Summary of final features /use cases that are tied to the wireframe".

**Decision:**
1. The report follows the **body** numbering (1 Introduction, 2 Component Diagram, 3 Detailed Design, 4 Testing, 5 Wireframe) and regenerates the table of contents.
2. §1.2 contains three things:
   - the active requirements;
   - an "Updates from M1" table (DEC-92);
   - a use-case summary that maps each use case to its wireframe screen.

**Decided by:** Delegated to Claude Code by JunKeatLim · **Decision date:** 2026-11-06 · **Decision source:** brief/report-template-m2.md; brief/rubric-m2.md B.1.1.

---

### DEC-96: Active Hours, minimum Standby credit and activated days

| Category | Team clarification | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Source and decision date:** Requesting team member, M2 review conversation, 2026-11-07. The member stated "the 4hrs credit is not the same as the 'Active Hours'", specified 2 active / 4 total and 5 active / 5 total hours, and accepted "Once per activated day for simplicity". The member authorised updating all relevant repository artefacts.

**Decision:**
1. **Active Hours** are the Planned Hours of Jobs attributed to the Staff member, including direct Standby duties and replacement Jobs. Keep planned duration plus the existing Travel Allowance; do not add actual start/end tracking. A reasoned Hours Edit corrects Active Hours.
2. **Total Credited Hours** per date are Active Hours on a normal Crew day; for a Technician rostered on Standby that day they are `max(4, Active Hours)`, activated or not. Apply the minimum once per date, not per Job/call. Keep the Standby record after activation. Full-day Leave without duties gives 0 h; a mid-day departure preserves earlier Job attribution.
3. Examples (Active / Total Credited): unused Standby 0/4; 2 h duty 2/4; 4 h duty 4/4; 5 h duty 5/5. Two duties of 2 h and 3 h give 5/5.
4. **Workload** is Total Credited Hours over the week/month. Use it for the 40 h weekly target, lowest-Workload dashboard and strictly-above-40 h highlight. The target does not create hours if work/availability is insufficient.
5. Crew rotation and the Dual-Certified >=20 h rule use last week's **Active Hours**. Keep projected-credited-hours >=40 h demotion, then order by last week's Active Hours, projected Active Hours and staff ID. Before Jobs are allocated estimate 8 Active/8 Credited per Crew day and 0 Active/4 Credited per Standby day. Actual Assignment-based totals replace estimates after allocation.
6. Activation count is distinct activated Standby dates in the rolling 12 months: first activation on a date adds one; later duties that date add no further count. Low count gives eligible Staff priority, not a misconduct label. Unsuccessful calls/non-attendance remain a Manager matter; the existing Audit Log can record the outcome without awarding an activation.

**Supersedes:** DEC-78's replacement-of-4-h formula and the hours/count definitions in DEC-80/81. Historical entries remain unchanged.

---

### DEC-97: Direct Standby duties and replacements with per-Job history

| Category | Team clarification | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Source and decision date:** Requesting team member, M2 review conversation, 2026-11-07: Standby Staff "go to the job directly using paid transport for extra jobs then go back if there aren't anymore", or travel "to join the existing crew" when someone leaves early. The member accepted filtering eligible replacements before activation-count/distance ranking, and described Alex doing Job 1 before Ben takes the remaining Jobs.

**Decision:**
1. Three valid active Crews are the minimum, not a fixed limit or one Crew per geographical Zone. The Manager assigns each Crew a set of the existing North/East/South/West/Central Zones, considering Standby home locations. Respect Van count; preserve Full Standby cover when adding Crews beyond the minimum.
2. Activation can assign a direct Job to one suitably certified Standby Technician without a Driver/Van, or replace a Technician in a Crew from a specified unstarted Job. Company-paid transport is arranged outside the system. Direct duties do not count towards the three initial Van Crews.
3. Filter availability/Leave, valid Certifications, person-level time/travel conflicts and Brand coverage for **all affected remaining Jobs** before ranking and again before saving. Rank by activated-day count, home-Zone distance, then staff ID. Algorithm-source Standby also uses home Zone; remove the forced Central base. A Technician already activated for a direct duty can take another non-overlapping duty; one committed to a replacement Crew is not offered elsewhere that day.
4. Retain one Standby record per Technician/date; activated changes false -> true only once. It records the original Standby duty and credit entitlement; it is not a simultaneous reserve commitment while the person is working.
5. Each Assignment stores its date and attributed Staff. Crew Assignments copy the effective members; direct Assignments have no Crew and exactly one Technician. A **Replacement** stores Crew, outgoing Staff, incoming Technician, starting Assignment, Manager, reason and time. Change attribution only on affected unstarted Jobs; keep earlier Job members and the initial Crew roster. Jobs subsequently added to the Crew use effective members after replacements.
6. UC-17 records replacement boundaries and Active Hours corrections without a Completed status or timesheet. Save activation, attribution, Hours Edits and audit entries atomically; notify after success.

**Supersedes:** whole-day-only attribution, replacement-only activation, forced Central Standby and single-Zone Crew coverage in DEC-10/39/77/80/81/84. Initial Crew composition still follows FR-26.

---

### DEC-98: Provisional preferences and binding confirmation after capacity checks

| Category | Team clarification | Ask whom | Team | Status | **Decided** |
|---|---|---|---|---|---|

**Source and decision date:** Requesting team member, M2 review conversation, 2026-11-07: "Managers can no longer override preferences"; "The minimum active rosters must be formed first before any standby can be confirmed". The member agreed to confirmation after the deadline and CSV checks: "Yes, they should be provisional as there still has to be a minimum no. of people being able to be in both the active roster and standby." The member reports professor feedback requiring preferences for work-life balance; this is member-reported feedback, not an invented lecturer transcript.

**Decision:**
1. Keep one requested day per Technician/week, one M Electric and one Dicon slot per date, first come first served. Before Wednesday's deadline Staff submit/change/withdraw a **Provisional** pick. Changing day/Brand resets submission time. A provisional slot is held against competing requests but is explicitly not guaranteed.
2. After the Availability Deadline and receipt of the week's HR/Van CSVs, process each day's provisional picks by submission time (staff ID breaks ties). Confirm only if eligibility remains valid and reserving the pick alongside earlier confirmed picks still permits at least three valid Crews **and Full Standby cover**. Algorithm/Leftover Technicians can be used to meet that minimum; the 20 h rotation preference must not cause a false shortage.
3. Set **Confirmed** or **NotConfirmed**, with decision time/reason, and notify through UC-15. Managers cannot favour a request or substitute another day. No new picks after the existing deadline. Only confirmed picks are reserved by crew formation.
4. Confirmation guarantees initial Standby placement, not a duty-free day. Manual removal or movement into an initial Crew is blocked even with an override reason. Genuine activation under UC-17 remains allowed. Leave takes precedence; retain the confirmed-request history.
5. Regeneration does not revoke confirmed picks or repeat notifications. Later imports/account changes causing shortages require Manager repair; never silently revoke another person's pick. Fewer than three valid initial Crews blocks publication. If three Crews can form but Full Standby cover cannot, confirm no further picks and retain the existing missing-cover warning because minimum Crews take priority.
6. A small feasibility search over the 11 Technicians is sufficient; no optimisation framework is needed. Return a valid arrangement as well as a Boolean result. The suggested roster uses that arrangement if its greedy ranking would otherwise strand a Brand or lose feasible minimum cover. This checks feasibility without promising the most Crews or optimal routing.
7. Technical safeguards: resolve/save each day's confirmations atomically; revalidate before publication. Refuse regeneration when Jobs or manual Crew/Standby edits exist instead of silently discarding them.

**Supersedes:** immediate guaranteed acceptance and Manager overrides in DEC-79, related DEC-80/89 rules and the fewer-than-three publication warning. Existing FR/UC IDs are retained.

---

### DEC-99: M2 consistency corrections after report review

| Category | Artefact consistency | Ask whom | Requesting team member / file owners | Status | **Recorded correction** |
|---|---|---|---|---|---|

**Raised and authorised:** 2026-11-10 by the requesting team member (identity not supplied), asking GPT-6.1 Sol to make minimal consistency fixes following the supplied Claude Opus 5.5 report review. Preserve agreed workflows and DEC-96–98; prepare local reviewable changes without committing or pushing. This records the current request, not a claim of ratification by all six members.

**Existing sources:** FR-04/05/08/39/40/45/46/48/51–55, NFR-07/09; DEC-74/93/94/96–98; UC-18 Alternatives. No new requirement or fairness policy is adopted.

**Corrections:**
1. Repair FR-36's broken sentence without changing the Total Credited Hours rule; identify FR-08 as changed in v4.1; correct NFR-09's permission-matrix reference to §4.1.
2. Align CD-final and CMP-system: suggestion goes through `RosterController.prepareSuggestion()` and preference confirmation; Job edits require IScheduling; account changes and approved requests delegate roster removal/unassignment to `RosterController`; application-layer `CsvImportController` owns `CsvRowMapper`.
3. Represent the existing 15-minute failure window, 30-day device-use rule and per-channel notification outcomes with Account timestamps and a Notification delivery-state map. Explain the existing Strategy configuration at application construction; runtime switching is not a requirement. Add the standard explanatory Strategy diagram to the source index.
4. Preserve the six black-box reduced rules, explicitly retaining submittedAt on a same-slot resubmission as UC-18 already states. Derive the Planning Week on pseudocode line 1 without changing CFG edges or complexity.
5. Correct sample roster eligibility, dates, hours, chronology and unsupported wording in a copy of the supplied HTML prototype. Direct duties remain operational updates to today's Published roster. A 2 h Planned Hours example may use a Manager-adjusted 1.5 h duration under FR-02; no new duration constraint is introduced.

**Append-only erratum:** DEC-94 decision item 2 says “FR-54 steps 1–4”; read this as **FR-55 steps 1–4**. FR-54 concerns CSV validation. The historical entry above is retained unchanged.

**Still unconfirmed:** actual M2 contributions/signatures; named authorship of the supplied HTML prototype; named decision-makers and team review/ratification of DEC-73–98. Existing sources retain their recorded status; this correction does not fabricate approval. The offline-storage and Draft deletion-notification conflicts are separately Open below.

---

### DEC-100: Offline Assignment view versus on-site-only storage

| Category | Requirement conflict | Ask whom | Team / client / IT Administrator | Status | **Open** |
|---|---|---|---|---|---|

**Raised:** 2026-11-10 during the M2 report consistency review (DEC-99).

**Source text:** NFR-05: “Staff must be able to view **today's** published Assignments without a connection. Changes are not accepted offline”. NFR-13: “The application and its database must run on an **on-site server**. Records and logs are stored only there”. Existing `LandingPage.loadCachedToday()` supports the offline view; DEC-89 records on-site deployment/storage.

**Question:** Does NFR-13 permit a per-user browser copy for NFR-05, and if so what data, protection and lifecycle apply, or must one requirement be revised? No cache exception or lifecycle is chosen in this correction. Keep both requirements and flag their unresolved boundary in the report and architecture notes.

---

### DEC-101: Notifications when deleting an Assigned Job in a Draft week

| Category | Requirement conflict | Ask whom | Team / Manager | Status | **Open** |
|---|---|---|---|---|---|

**Raised:** 2026-11-10 during the M2 report consistency review (DEC-99).

**Source text:** FR-04: “Deleting an Assigned Job notifies its attributed Staff first.” FR-39: “Draft Assignment changes send nothing until publication.” The separately recorded FR-51 exception concerns preference outcomes only (DEC-98).

**Question:** Does deletion of a Job assigned in a Draft week notify attributed Staff, or follow Draft suppression? Do not infer a new exception or silently amend either requirement. The corrected W-04 illustration uses an unstarted Job in a Published week, for which the current requirements agree that Staff are notified.

---

### DEC-102: Resolution of DEC-100 — bounded offline Assignment copy

| Category | Requirement clarification | Ask whom | Requesting team member | Status | **Decided** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity not supplied), M2 second-review conversation, 2026-11-10. The member expressly approved retaining offline viewing of today's Published Assignments through a limited per-user browser cache, cleared at logout and expired when its date passes, while authoritative database records and logs remain on-site. This records that authorisation, not ratification by all six members.

**Decision:** NFR-05 permits a read-only browser copy containing only the signed-in Staff member's Published Assignments for today. Clear it at logout and expire it when its Assignment date passes. Offline changes remain unavailable. NFR-13 requires the application, authoritative database records and logs to remain on the on-site server; this bounded copy is the explicit exception for offline viewing. No encryption method, authentication extension or further security policy is added by this resolution.

**Resolves:** DEC-100. Keep its historical Open entry unchanged and read it with this resolution. Update NFR-05/13, UC-01/13, the architecture and W-11 consistently. SRS v4.1.1 records this change.

---

### DEC-103: Resolution of DEC-101 — Draft deletion follows notification suppression

| Category | Requirement clarification | Ask whom | Requesting team member | Status | **Decided** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity not supplied), M2 second-review conversation, 2026-11-10. The member expressly approved no Staff notices when deleting an Assigned Job in a Draft, and notification when deleting it after publication. The existing preference-outcome exception is unchanged.

**Decision:** FR-04's deletion notice applies only to an Assignment in a Published Weekly Roster. Deleting an Assigned Job in a Draft sends no Staff notification, consistently with FR-39. For an eligible unstarted Published Job, notify attributed Staff before deleting the Job and its Assignment as already specified. FR-51's immediate preference-outcome notification remains the existing exception to Draft suppression; it does not expose Draft Assignments. The existing editing/deletion time limits remain unchanged.

**Resolves:** DEC-101. Keep its historical Open entry unchanged and read it with this resolution. Update FR-04/39, UC-05/15 and W-04 consistently. SRS v4.1.1 records this change.

---

### DEC-104: Second-review traceability and presentation corrections

| Category | Artefact consistency | Ask whom | Requesting team member / file owners | Status | **Recorded correction** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity not supplied), 2026-11-10, authorised the supplied second-review content fixes while preserving the agreed workflows. The member supplied screenshots titled **“What Makes a Requirement Good? (1/2)”** and **“What Makes a Requirement Good? (2/2)”**. No lecturer name, slide date or publication metadata was supplied.

**Corrections:**
1. Bump the SRS to **v4.1.1 (2026-11-10)** for DEC-99's requirement/use-case corrections and DEC-102/103. The report baseline is commit `0ab8f1e` plus the uncommitted corrections on `codex/m2-review-fixes`; do not describe that commit alone as containing them. Keep all FR/NFR/UC IDs. Label clauses within the longest requirement rows for clarity without changing policy, and distinguish the Mechanism column's design traceability from requirement statements.
2. Assess the actual requirements against the supplied lecture's seven traits: **Verifiable; Clear & Concise; Traceable; Viable; Consistent; Implementation Free; Complete**. Retain the lecture's indivisibility criterion under Traceable. Do not claim full atomicity for bundled legacy rows or verified viability without budget, schedule and skills evidence. Sourced operating/security constraints remain requirements; the design mechanism is separate.
3. Preserve the six reduced black-box rules. Add supplementary test **BB-07** for the existing UC-18 no-op case: an unchanged resubmission at 10:00 keeps the original 09:00 timestamp, slot and one Provisional request. No new cause, rule or behaviour is added.
4. Clarify the CSV validation hand-off: `CsvImport.parse(file)` returns parsed rows; application-layer `CsvImportController` uses its `CsvRowMapper` for column and row checks, collects whole-file errors and calls `CsvImport.recordValidation(errors)`. Only an error-free file is mapped/saved atomically and marked Committed; rejected files save no Leave Record or Van Availability. The entity does not depend upward on a mapper. This refines DEC-99's design representation of FR-52–54, not the validation workflow.
5. Apply FR-36's strictly-above-40 h highlight to Driver as well as Technician Workload in W-06. Label its illustrated state **Draft after Manager edits to the Suggested Roster**, rather than claiming raw algorithm output. W-11's offline illustration contains only today's Assigned data for its Staff member. Preserve the supplied original HTML and keep the revised prototype with M2 materials.
6. Explain the legitimate bidirectional application-component dependencies: Roster & Hours requests preference confirmation through IStaffInputs; Staff Inputs delegates approved Job unassignment through IRoster. These are different use-case operations within one layer, with no cross-layer upward dependency. Provide a whole-screen overview plus labelled detail panels for each screenshot set and check final pagination.

**Still requires human input:** named requester/AI attribution, original prototype authorship, actual contributions, signatures, dates and team review/ratification. No administrative facts are inferred and no commit, push or sharing change is authorised by this entry.


---

### DEC-105: Encrypted offline Assignment copy and local password unlock (Option A)

| Category | Requirement / design clarification | Ask whom | Requesting team member | Status | **Decided** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity not supplied), M2 review conversation, 2026-11-10. After reviewing the supplied Claude assessment, the member explicitly approved Option A and asked for the repository and M2 report to be updated. This records that requester approval, not ratification by all six members.

**Decision:** Retain NFR-08 encryption at rest for the bounded NFR-05 offline copy as well as the on-site store. Persist only this Staff member's Published Assignments for today in encrypted form. The stored device data must not reveal that copy without the Staff member's password: the encryption key is derived from or protected by that password, and no readable decryption key is persistently stored. This protects the persisted copy; it does not claim protection of a view that is already unlocked. The encryption algorithm, library and key derivation/protection technique remain implementation choices.

When the app was closed and the copy is reopened offline, require a local password unlock checked on the device only. No connection or server login is needed. An incorrect password keeps the copy locked and reveals no Assignment data; do not prompt again while the copy remains unlocked. This is a local unlock, separate from online login. Each successful online load of today's Published Assignments refreshes the encrypted per-user copy; refreshing within an existing authenticated online session must not require a fresh daily login. This records the directly related refresh-trigger clarification (D3) as well as Option A. Existing scope, read-only behaviour, logout clearing and date expiry from DEC-102 continue. Expiry prevents later viewing on the app's date check; no claim is made that a closed app can delete device data at midnight.

**Unresolved implementation follow-ups:** Specify and verify key protection and lifecycle across existing authenticated sessions, password change/reset handling and the relevant browser support before implementation acceptance. DEC-61's session/token-lifetime questions remain Open. No new offline attempt limit, password-reset behaviour, session duration or daily-login requirement is adopted from the supplied Claude assumptions. Those details must not be inferred from this decision.

**Artefacts:** SRS v4.1.2 (NFR-05/08 and quality/open-item notes); UC-13; CD-final LandingPage method/note; ARCH-layered; design/wireframe notes; traceability; W-11 locked, incorrect-password and unlocked prototype states; corresponding report requirements, architecture and screen descriptions. The prototype illustrates local sample transitions only and implements neither encryption nor credential checking. Historical DEC-102 and other entries stay unchanged. No commit, push or sharing change is authorised.


---

### DEC-106: Fourth-review D1–D4 editorial and transaction representation corrections

| Category | Editorial / design representation clarification | Ask whom | Requesting team member | Status | **Recorded** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity not supplied), 2026-11-11, explicitly requested the supplied fourth-review D1–D4 corrections in the repository and M2 report while preserving established workflows and decisions. This records that correction request, not ratification by all six members.

**Corrections (no new behavioural decision):**
1. Broaden the SRS §11/report seven-trait assessment: FR-04/32/33/39/40/51/55/57 and NFR-05 bundle obligations under retained IDs, so single-requirement/indivisibility conformance remains partial. Distinguish stakeholder evidence from team-decided constraints: NFR-08's backend-encryption goal cites INT-ITA [Q: Safeguards], salted hashes† are team-set, and offline password/key protection is DEC-105. DEC-105 is a valid team-decision source, not stakeholder testimony. FR-55 retains the agreed algorithmic policy in M2-Brief §4 / DEC-80, refined by DEC-96/98.
2. Make the existing successful CSV save boundary explicit across FR-52/54 mechanisms, UC-16, CD-final and design/report prose: after whole-file validation and mapping, one transaction replaces Leave Records or Van Availability for the dates in the file, marks the import Committed through CsvImport.commit(), and writes the successful-upload AuditLog entry. This clarifies existing atomicity; validation/rejection, upload logging and date-scoped replacement policies are unchanged.
3. Describe report figures as complete-screen views and labelled details, with the Saturday W-06 figures identified as additional details. Do not claim every screenshot set has an overview; no additional screenshot is required.
4. Replace the leftover report phrase “The draft preserves them” with “The SRS records them”.

**Limits:** Retain SRS v4.1.2, all requirement statements/IDs, policies, test design, diagrams' classes/relationships and the prototype. D5's optional offline metadata clause, cancelled-Leave representation, security/session/reset details and administrative items are outside this correction. Existing follow-ups remain open. Historical decisions and AI log rows are preserved; no commit, push or sharing change is authorised.


---

### DEC-107: Targeted M2 submission and cross-artefact corrections

| Category | Editorial / representation alignment | Ask whom | Requesting team member / file owners | Status | **Recorded correction** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity not confirmed), 2026-11-14, expressly authorised targeted corrections to the M2 report and repository following the supplied audit and revised review, with close template following, a short AI Usage paragraph, and contributions/declarations left for members. This records that request, not ratification by all six members.

**Corrections:**
1. SRS v4.1.3 expresses the existing actor capabilities as system obligations, including FR-01/07/12/38/44 and comparable rows. Roles, permissions, conditions, stable IDs and behavioural meaning are retained. No human is grammatically required to perform a system function; required inputs remain required.
2. FR-33 separates missing Van CSV from reasoned-overridable warnings. It is the existing FR-40 planning alert: show missing dates and return to UC-16, following UC-07's precondition that the week's HR and Van CSVs are present. No unknown Van count, manual capacity fallback or new per-date/whole-week policy is introduced. FR-32 and DEC-74/98 remain binding.
3. Label DP-strategy-ranking as an applied view. Its WorkloadRanking/ActivationRanking-to-Technician read dependencies elaborate the existing order(candidates, context) operations and ranking-value methods; they are not listed as extra explicit CD-final relationships. CD-final's 75 definitions and 96 explicit relationships are retained. Make the component-contract → provider-class → operations mapping visible in the report using the existing CMP-system legend; do not invent twelve new interface classes.
4. Correct only W-14's Awaiting CSV label in the revised prototype: Provisional request and Provisional (locked) held slot, with post-deadline editing locked. Preserve the supplied original HTML. Include Awaiting CSV and NotConfirmed/reason report evidence.
5. Follow the supplied template's cover/front-matter order and heading hierarchy, retaining Times New Roman and DEC-95 body numbering; generate the contents from headings and add page numbering/deliberate page breaks. Replace the report's long AI history with a short accurate disclosure. Remove internal workflow/provenance prose while retaining meaningful sources and unresolved technical limitations. Contributions, declarations and submission date remain human fields; no acceptance, signature or actual contribution is inferred.
6. Explain the adapted Domain Model/Data grouping in the layered design rather than redesigning it. Local lecture verification supports class/component provider/requirer correspondence (Component Diagram lecture, pp.37–38), the lecture's Business/Application placement of entities (Architectural Pattern lecture, p.30), and Strategy's interchangeable algorithms (Design Patterns lecture, p.19); it does not prescribe the two read-dependency edges.

**Preserved:** 45 active FRs, 14 active NFRs, all IDs and established policies; DEC-104/106 partial indivisibility and unverified viability; the complete/reduced black-box tables, BB-07, CFG and seven basis paths, and SC-01–15. No production test execution, team declaration, commit, push or sharing change is authorised by this correction.


---

### DEC-108: Complete weekly HR CSV snapshot and committed coverage

| Category | External data / planning readiness | Ask whom | Requesting team member / file owners | Status | **Adopted for the M2 working baseline** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member (identity unconfirmed), 2026-11-14, explicitly selected the complete weekly HR CSV snapshot approach and authorised its propagation through the report and repository. This records that instruction, not confirmation by all six members. Refines DEC-74/106 and SRS FR-52/54; Van CSV per-date counts remain unchanged.

**Decision:**
1. For HR import the Manager selects one Planning Week (Monday–Saturday) and confirms that the file is the complete HR export for that week, including an export with no Leave. A selected week alone does not make a partial/delta export complete; an unconfirmed or declared partial/delta export cannot be committed as a weekly snapshot.
2. Required headers remain `staff_id, date, type`. A correct-header file with zero data rows is valid and means no Leave Records in that week. A wholly blank file, missing headers, invalid rows or a row outside the selected week rejects the entire import. Exact duplicate rows are saved once.
3. Before replacement show the selected week and the replacement effect; require confirmation, with an explicit warning when zero rows would clear existing Leave Records. On success, one transaction replaces **all** Leave Records in the selected week (including removal of omitted/cancelled Leave), commits the import's week, completeness confirmation, uploader/time/outcome and successful Audit Log entry. Other weeks are unchanged. An import/save failure changes neither business records nor previous successful HR coverage.
4. HR readiness for UC-07/18 is a committed complete snapshot covering the selected week, not the presence or count of Leave Records. Valid zero-row coverage is ready. A later rejected attempt cannot invalidate earlier committed coverage. Van readiness still requires an explicit imported count for each working date; do not infer capacity from absent rows.
5. No Leave does not imply Available: Staff Availability is still required and no entry remains unavailable (DEC-03/83). Preserve existing later-clash alerts, Manager repair, confirmed-preference history and earlier per-Job attribution (DEC-97/98); importing/removing Leave does not silently rewrite operational history or revoke confirmed picks.

**Propagation:** SRS v4.2 (stable IDs); UC-16, UC-07/18 readiness; CsvImport metadata/coversWeek and CsvImportController whole-week validation/replacement; W-05 and readiness descriptions; supplemental CSV design scenarios. This is an intentional policy change from replacement of only the file's dates. The prototype illustrates states; production persistence and transaction execution are not claimed.

---

### DEC-109: Browser controller for the approved offline Assignment copy

| Category | Design responsibility allocation | Ask whom | Requesting team member / design owners | Status | **Recorded design correction** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member, 2026-11-14, authorised the validated architecture/View-responsibility correction; the orchestrating review accepted this minimal allocation. Local Architectural Pattern lecture p.38 states that the View does no processing. Existing offline behaviour remains DEC-102/105 and NFR-05/08/13.

**Decision:** Add browser-side `OfflineAssignmentController` within Web UI. `LandingPage` renders page data and forwards local-unlock/logout input; the controller obtains today's Published Assignment page data through `DashboardController`, refreshes the bounded encrypted local copy only after a successful online load, and owns `cacheToday`, `loadCachedToday`, `unlockCachedToday` and `clearCachedToday`. The browser's Presentation/client tier therefore contains both a View and a supporting Controller; MVC responsibility is distinct from physical deployment. Existing server authentication and login remain unchanged.

**Preserved:** Per-user today-only Published data, read-only offline access, local password unlock after reopening, no readable persisted decryption key, no repeated prompt while unlocked, logout clear and date expiry. Algorithm/library and existing-session/password-change/reset key lifecycle remain specification/verification follow-ups. No new cryptographic algorithm, offline attempt rule or production implementation is asserted.

**Model effect:** CD-final has 76 class/interface/enumeration definitions and 99 explicit relationships: one new controller; LandingPage → OfflineAssignmentController and OfflineAssignmentController → DashboardController; RosterController → CsvImport for DEC-108 coverage. The 96 earlier relationships remain. Existing two Strategy ranking-value read dependencies are still applied-view elaborations outside that explicit final-model count. Component topology and twelve architectural service contracts are unchanged; Web UI's existing IRoster requirement carries the online read.


---

### DEC-110: Plain report typography and source notation

| Category | Report presentation only | Ask whom | Requesting team member | Status | **Adopted presentation direction** |
|---|---|---|---|---|---|

**Source and authorisation:** Requesting team member, 2026-11-14, explicitly required consistent Times New Roman throughout report prose, tables, class/method references, pseudocode, headers and footers; bold/italic may provide emphasis. Replace prose role shorthand (`«E»`, `«B»`, `«C»` and ornamental role tags) with plain wording where needed, source `§` with “Section”, and dagger threshold markers with “(team-set target)” while retaining the provenance explanation.

**Scope:** Report text and styles only. Formal UML notation and mathematical/CFG symbols retain their technical meaning in diagrams; captured UI remains the illustrated interface. Canonical repository mechanisms and source citation notation are unchanged. SRS remains v4.2; report/source parity checks normalise these intentional presentation adaptations.
