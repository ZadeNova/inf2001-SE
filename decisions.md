# Decisions and Open Questions

> Every ambiguity, contradiction or gap in the brief or the rubrics gets a DEC entry **before** anyone picks an interpretation (see [AGENTS.md](AGENTS.md)).
> Anyone may add entries, but never edit someone else's entry. Resolve an entry by filling in Decision / Decided by / Source and setting its Status.
> IDs are never reused.

**Status:** `Open` (not asked yet) · `Asked` (waiting for an answer) · `Decided` · `Superseded by DEC-nn`
**Ask whom:** `Stakeholder` (via an elicitation meeting) · `Lecturer` (course admin/rubric) · `Team` (internal design choice)

Quotes are verbatim from [brief/project-description.md](brief/project-description.md) ("Brief") and [brief/rubric-m1.md](brief/rubric-m1.md) / [brief/rubric-m2.md](brief/rubric-m2.md) / [brief/assessment-overview.md](brief/assessment-overview.md).
DEC-01 to DEC-30 were raised on 2026-09-30 (AI-assisted analysis, see `ai-usage-log.md`). The options listed are possibilities for discussion and are **not recommendations**. The index shows which entries have since been decided.

## Index

| ID | Topic | Category | Ask whom | Status |
|---|---|---|---|---|
| DEC-01 | Availability horizon: one month vs 5 weeks | Contradiction | Lecturer | **Decided**: 1 month in advance |
| DEC-02 | Availability Deadline mechanics (Wed / Thu / Mon) | Ambiguity | Stakeholder | Open |
| DEC-03 | Availability granularity, default and deletion | Missing definition | Stakeholder | Open |
| DEC-04 | Workload unit and the period behind the 40-hour highlight | Ambiguity | Stakeholder | Open |
| DEC-05 | "Top three staff with the lowest workload" | Ambiguity | Stakeholder | Open |
| DEC-06 | "Up to three staff" on the allocation page | Ambiguity | Stakeholder | Open |
| DEC-07 | What a Job Preference is | Missing definition | Stakeholder | Open |
| DEC-08 | "Staff's location at a particular date" | Missing definition | Stakeholder | Open |
| DEC-09 | Van crew composition and capacity | Ambiguity | Stakeholder | Open |
| DEC-10 | Unit of assignment: Staff or Van crew | Ambiguity | Stakeholder | Open |
| DEC-11 | What a Job contains and who creates Jobs | Missing definition | Stakeholder | Open |
| DEC-12 | Working days: Saturday, Sunday, public holidays | Ambiguity | Stakeholder | Open |
| DEC-13 | How Leave is handled | Missing definition | Stakeholder | Open |
| DEC-14 | Van Workshop Servicing in the system | Missing definition | Stakeholder | Open |
| DEC-15 | What happens after a Job Rejection | Missing definition | Stakeholder | Open |
| DEC-16 | Allocate one week vs visualise one month | Ambiguity | Stakeholder | Open |
| DEC-17 | IT Administrator: distinct actor and scope | Missing definition | Stakeholder | Open |
| DEC-18 | Roles: Staff vs Manager vs "administrative staff" | Ambiguity | Stakeholder | Open |
| DEC-19 | Does the system enforce the business rules? | Missing definition | Stakeholder | Open |
| DEC-20 | "Working hours engaged/assigned" | Ambiguity | Stakeholder | Open |
| DEC-21 | Deliverable scope: working web app vs wireframe | Rubric | Lecturer | Open |
| DEC-22 | Job volume and duration vs crew capacity | Missing definition | Stakeholder | Open |
| DEC-23 | M1 activity diagram examples ("subscription, announcement, notification") | Rubric | Lecturer | Open |
| DEC-24 | M1 Formatting rubric lists M2 artefacts and a "required template" | Rubric | Lecturer | Open |
| DEC-25 | Appendix C subsections labelled B.1–B.4 | Rubric | Lecturer | Open |
| DEC-26 | M2 "provided report template" not in our materials | Rubric | Lecturer | Open |
| DEC-27 | Week numbering and M1 presentation timing | Rubric | Lecturer | Open |
| DEC-28 | Stakeholder rule: "same project" restriction | Rubric | Lecturer | Open |
| DEC-29 | Weighting labels and unweighted Introduction items | Rubric | Lecturer | Open |
| DEC-30 | How "1 month in advance" is measured | Ambiguity | Team | Open |

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

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-03: Availability granularity, default and deletion

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief R8: "Staff can add and edit their availabilities up to 5 weeks ahead of time." Brief R5: "...and availabilities for the week should be shown"

**Question:** Is Availability recorded per day, per half-day (AM/PM) or per time slot? Are Staff assumed available unless they say otherwise, or unavailable unless they declare Availability? R8 says "add and edit". Can Staff also delete an entry?

**Why it matters:** This shapes the Availability class attributes, the input UI and how "available" is computed for allocation.

**Options:**
1. Whole-day available/unavailable, defaulting to available.
2. Half-day slots, defaulting to available.
3. Explicit time ranges, defaulting to unavailable.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-16: Allocate one week at a time vs visualise one month

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

## B. Workload and the Manager's views

### DEC-04: Workload unit and the period behind the 40-hour highlight

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-05: "Top three staff with the lowest workload"

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-06: "Up to three staff" on the allocation page

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-20: "Working hours engaged/assigned"

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief §Intro ¶3: "an interactive and visual way for the employee to see their job assignments, working hours engaged/assigned"

**Question:** Does "engaged" mean hours actually worked, which would need Job completion or time recording, or is it a synonym for "assigned"? Is Job completion recorded in the system at all?

**Why it matters:** If actual hours count, a new use case is needed (record completion or hours) along with new attributes.

**Options:**
1. Assigned hours only, with no completion tracking.
2. Staff or the Manager mark Jobs completed and actual hours are recorded.

**Decision:** — · **Decided by:** — · **Decision source:** —

## C. Staff inputs

### DEC-07: What a Job Preference is

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief R9: "Staff can indicate their job preference for the week". Brief R5: "staff's job preference"

**Question:** What can Staff express as a preference: Brand, Job Type (installation vs servicing), area or region, particular days, or preferred colleagues or Van? Does it apply to Drivers? Is it binding or advisory? Does it share the Wednesday deadline?

**Why it matters:** The JobPreference class attributes and the preference UI both depend on this.

**Options:**
1. Job Type only.
2. Job Type plus area/region.
3. Free text shown to the Manager.
4. A structured set of fields to be agreed with stakeholders.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-08: "Staff's location at a particular date"

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief R5: "When displaying the staff availability, the workload assigned, staff's job preference, staff's location at a particular date, and availabilities for the week should be shown"

**Question:** Where does this location come from? Possibilities include the location of the Staff member's assigned Job that day (derived), a location the Staff member enters with their Availability, their home or base area, or live GPS. Who enters it, and at what granularity (address, postal district, region)?

**Why it matters:** This decides whether location is derived from the Job, becomes a Staff input field, or needs an external integration. Live GPS would bring privacy NFRs.

**Options:**
1. Derived from the address of the Job assigned on that date.
2. Staff enter an expected location or region with each day's Availability.
3. A fixed home or base region stored on the Staff profile.
4. Live device location (out of scope?).

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-15: What happens after a Job Rejection

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

## D. Domain: Vans, Jobs, Leave, calendar

### DEC-09: Van crew composition and capacity

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-10: Unit of assignment: Staff or Van crew

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-11: What a Job contains and who creates Jobs

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-12: Working days: Saturday, Sunday, public holidays

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶4: "there should be at least three vans can be on service daily except for Sunday and public holidays."

**Question:**
- Is Saturday a normal working day?
- Does the Sunday and public holiday exception mean no work at all, or only that the minimum of three Vans does not apply?
- Which public-holiday calendar applies, and who maintains it in the system?
- What are the working hours per day?

**Why it matters:** Availability calendars, the minimum-Vans check and Workload baselines (e.g. how 40 hours relates to a 5.5- or 6-day week) all depend on this.

**Options:**
1. Mon–Sat working, no work on Sundays or public holidays.
2. Mon–Sat working, with Sunday and public holiday work allowed but no minimum.
3. A configurable working calendar maintained by the Manager or IT Administrator.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-13: How Leave is handled

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-14: Van Workshop Servicing in the system

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶5: "A van will be sent to the workshop for servicing every two months."

**Question:** Should the system record Van Workshop Servicing dates so the Van shows as unavailable? Who schedules them? For how long is a Van out? Must the three-Van minimum still hold on workshop days?

**Why it matters:** This decides whether Van availability is modelled at all, i.e. whether Van needs its own availability or status.

**Options:**
1. Not modelled: the Manager just doesn't allocate that Van.
2. Van unavailability dates entered by the Manager.
3. The system auto-schedules servicing every two months.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-22: Job volume and duration vs crew capacity

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
|---|---|---|---|---|---|

**Source text:** Brief §Company ¶5: "On average, there are more than 20 jobs for aircon installation and servicing daily." ¶4: "at least three vans can be on service daily"

**Question:** What is the typical duration of an installation vs a servicing Job? How many Jobs can one Van do per day? This is needed to check whether 3–6 Vans can realistically cover more than 20 Jobs a day.

**Why it matters:** It sets data-volume and performance NFRs (e.g. more than 20 Jobs/day × 1 month ≈ 500+ Jobs in view, per DEC-01) and realistic Workload hours.

**Options:**
1. Stakeholders provide standard durations per Job Type.
2. Duration is entered per Job.

**Decision:** — · **Decided by:** — · **Decision source:** —

## E. Actors and system rules

### DEC-17: IT Administrator: distinct actor and scope

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-18: Roles: Staff vs Manager vs "administrative staff"

| Category | Ambiguity | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-19: Does the system enforce the business rules?

| Category | Missing definition | Ask whom | Stakeholder | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

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

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:** Rubric M1 B.4, Activity diagrams: "Clear workflows modelled for all key processes (subscription, announcement, notification)."

**Question:** The Aircon Retailer brief has no subscription or announcement process, and notification is at most implied by DEC-15. This looks like a template carry-over from another project. Should we model *our* key processes (e.g. submit Availability, allocate Jobs, reject Job) instead?

**Why it matters:** Activity diagrams are part of the 5% Use Cases component. We need to know which processes will be graded as "key".

**Options:**
1. Treat it as a carry-over and model this project's key processes, with a sentence in the report explaining our choice.
2. Also model a notification process if one emerges from DEC-15.

**Decision:** — · **Decided by:** — · **Decision source:** —

### DEC-24: M1 Formatting rubric lists M2 artefacts and a "required template"

| Category | Rubric | Ask whom | Lecturer | Status | Open |
|---|---|---|---|---|---|

**Source text:**
- Rubric M1 B.4, Presentation / Formatting: "Professionally structured report following the required template..." and "Strong alignment and traceability across requirements, use cases, final class diagram, component diagram, detailed design, testing artefacts, and prototype wireframes."
- Rubric M1 B.1.2.1, by contrast: "All artifacts align (e.g., requirements ↔ use cases ↔ diagrams)."

**Question:** The M1 B.4 Formatting row is identical to the M2 row and lists artefacts that don't exist in M1. Is there an M1 report template we should be following? If not, is the B.1.2.1 wording the one that applies to M1?

**Why it matters:** This is 2% of the M1 grade, and we need to know which template or structure is expected.

**Options:**
1. Assume a carry-over: follow B.1.2.1 and the M1 chapter list.
2. Obtain and follow the M2 template for M1 as well.

**Decision:** — · **Decided by:** — · **Decision source:** —

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

| Category | Rubric | Ask whom | Lecturer | Status | Open |
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

**Decision:** — · **Decided by:** — · **Decision source:** —

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

| Category | Ambiguity | Ask whom | Team | Status | Open |
|---|---|---|---|---|---|

**Raised:** 2026-09-30, as a follow-up to DEC-01

**Source text:** Lecturer's reply (DEC-01): "It should be "1 month" for consistency." and "the "earlier" is now changed to "in advance"."

**Question:** How exactly is the 1-month window computed? For example, if today is 30 Sep, is the last allowed date 30 Oct (calendar month), 29 Oct (30 days), or the end of the last planning week that starts within the month? What happens on 31 Jan (there is no 31 Feb)? Does the window start today or at the next planning week?

**Why it matters:** This is the exact boundary for the Availability date validation FR and the M2 black-box test cases. It is a design choice within the lecturer's ruling, so the team can decide it, and optionally confirm it with a stakeholder.

**Options:**
1. Same date next calendar month (clamped to month end), inclusive.
2. Fixed 30 days from today.
3. Whole planning weeks (Mon–Sun) that start within one calendar month from today.

**Decision:** — · **Decided by:** — · **Decision source:** —

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
