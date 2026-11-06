# INF2001 P8-1: M2 Design Update Brief

> **Source record.** This is the team's M2 Design Update Brief (`M2_Design_Update_Brief.md`), copied into the repo on 2026-11-06 so that M2 decisions can cite it as `M2-Brief §<n>`. Sections 1–4 are final team decisions. Sections 5–6 are suggestions. Section 7 was resolved by the team on 2026-11-06 (see DEC-73 to DEC-95 in [decisions.md](../decisions.md)). The wording below is unchanged from the supplied file, except that the availability horizon in §5.1 ("5 weeks") is superseded by DEC-01 (1 month), as recorded in DEC-83.

## How to use this document

You are helping our team update our Software Engineering project (Aircon Retailer Workload Management System) from **Milestone 1 (M1)** to **Milestone 2 (M2)**.

- **Section 1–4** are **final team decisions**. Treat them as fixed. Do not reintroduce anything listed as removed.
- **Section 5** is the instruction for updating the **final class diagram** (the only M1 artefact carried into M2).
- **Section 6** lists the M2 deliverables, with **suggestions** for each. These are suggestions, not team decisions: propose them, but let the team confirm.
- **Section 7** lists items that are **still open or kept aside**. Do not invent answers for them; flag them instead.

Writing rules from our prof's M1 feedback:
- Use **"must"** instead of "shall" in all requirements.
- **For every requirement, show the mechanism**: which class holds the data, which method changes it, who triggers it, and when. If no decision depends on a piece of data, do not store it (PDPA principle: don't collect what you don't need).
- External services (Email/SMS) are **non-human actors**, not stick figures.

---

## 1. Background: what the prof said about M1

- The system tracked too many attributes without showing who updates them or how. Every tracked value needs an owning class and a method.
- Too much unnecessary data was stored (certificate numbers, van licence plates, workshop servicing, job completion details).
- The standby/replacement process was not defined end to end.
- Job preferences were "one-sided": the system accepted preferences it could not guarantee. If the system offers a preference, it must follow it.
- Zones were missing. Singapore should be divided so vans don't travel across the island.
- Hours must be tracked on **planned** time, not actual time (people could stall to inflate hours).
- FR-47 (forgotten password), FR-46 (keeping past records), FR-10 (12-month tracking) and FR-40–42 (notifications) were not backed by classes.
- Use case diagram: check whether «extend» relationships are genuinely optional (Login → Reset Password, Allocate Jobs → Compare Staff). Email/Phone services must be non-human actors; check association direction.
- The sequence diagrams were fine. The class diagram must be corrected before resubmission.

---

## 2. Scope

- The system is **primarily focused on schedule planning**. Nothing else.
- The following happen **outside the system**:
  - job completion
  - leave applications and approvals
  - overtime approval (settled between the manager and the technician)
  - van management and van servicing
  - contacting standbys when they are activated (manager phones them)
- **External data enters the system by CSV upload.** The manager downloads a CSV from each external system and uploads it into our system:
  - **HR system CSV:** who is on leave / emergency leave / MC, and on which dates.
  - **Van vendor CSV:** how many vans are available on each date.
- The HR system and the van vendor are **not actors** in our use case diagram, because they never interact with our system directly. The Manager is the actor who uploads the files.

---

## 3. Final decisions

### 3.1 Removed (do not reintroduce)

| Item | Notes |
|---|---|
| Certificate number | Keep only **Brand** and **expiry date**. The expiry check still blocks assigning a technician whose certification has expired. |
| UC-06 Manage Vans and Workshop Servicing | Van details (number, licence plate), the Van list and the Workshop Servicing rotation are removed. Van availability comes from the vendor CSV. |
| Job completion tracking (UC-14 Complete Job) | No actual start/end time, remark, follow-up flag or invoice photo. No "Completed" job status. |
| Actual Hours | Hours are based on planned time only (plus manager edits). |
| Leave Request (apply/approve) | Leave is read-only, imported from the HR CSV. No leave balance tracking. |
| Late Availability Change Request / last-minute absence requests | Handled outside the system. |
| Overtime approval | Handled outside the system. |

### 3.2 Kept or added

| Item | Decision |
|---|---|
| **CSV Upload** (new use case) | Manager uploads the HR leave CSV and the van availability CSV. |
| **Job Rejection** | Kept (brief requirement 10). Staff press Reject, the system shows a warning to discuss it with their manager first, then the manager is notified. |
| **Edit Hours / Update Roster** (new use case) | Manager edits hours after the fact and updates the roster. Covers OT, standby activations, "who took over from whom", and corrections. |
| **Audit Log** | Every hours edit and every manager override of the suggested roster is logged: who, what changed, why, when. |
| **Job status** | Only **Assigned** or **Unassigned**. |
| **Cancelled jobs** | When a customer cancels, the job is **deleted**. Affected staff are notified. |
| **Zones** | Jobs are sorted into **North, East, South, West, Central**. The manager decides which zone each van/crew covers; the algorithm does not. |
| **Crews** | Stay together **all day**. They **can go home** after their last job (no reporting back to base). |
| **Home zone** | New attribute on every technician. Used to find the closest standby. |
| **Manager availability page** | Shows who is available and not on leave (from the HR CSV). |
| **Notifications** | Sent for the **initial roster publication and every later change** (roster changes, job changes, deletions, standby assignment, job rejection outcomes). |
| **Forgot password** | New class (e.g. password reset token) to back FR-47. |
| **Notification class** | New/explicit class to back FR-40–42. |
| **Storage** | Records and logs are saved on an **on-site server backend** (persistent storage). |
| **Retention** | Records and logs are kept for a **rolling 12 months**, then purged. |
| **40-hour highlight** | Kept (brief requirement 6). Manager landing page shows the 3 lowest-workload staff and highlights anyone over 40 h. |

### 3.3 Hours and workload

- **Workload** = a technician's **active hours**: planned job hours + activated standby hours + manager edits.
- An **unused standby day** counts as **half hours** (e.g. 4 h for an 8 h day).
- If a standby is **activated**, the actual hours entered by the manager **replace** the half hours (not added on top).
- **Leave does not count as hours.**
- Half hours **do** count toward the 40-hour highlight.
- The crew-forming algorithm ranks technicians by **last week's hours**, then this week's running total.

### 3.4 Preferences (standby day)

- The only preference is the **standby day**: each technician picks **one standby day per week**.
- Each day allows **at most 2 picks: one M Electric slot and one Dicon slot**, first come first served. A dual-brand technician can take either slot. Once both slots are taken, that day is greyed out.
- Because the system only accepts picks that still have room, **every accepted preference is guaranteed** (this answers the prof's "if you offer it, you must follow it" point).
- Priority order: **leave / emergency leave / MC > preference pick > normal standby**.
- A technician already on standby should not take leave; but leave approved earlier in the HR system always wins.
- The manager sees each technician's standby-day pick when comparing staff (brief requirement 5).

### 3.5 Standby

- **Standby** = technicians who are available but were not placed in a crew that day.
- **Minimum standby per day:** one team covering both brands (1 M Electric + 1 Dicon, or 1 dual). No maximum.
- If there are not enough people for both 3 crews and a standby team, **3 crews win**.
- Duals moved to standby by the algorithm are based in **Central** (they can reach any zone and cover either brand: the "trump card").
- Standby and active work are **paid the same**.
- The system tracks each technician's **activation count** over a **rolling 12 months**, so the manager can spread activations fairly.

### 3.6 Drivers

- Drivers are deliberately kept simple: **assumed always available, one per van**. The system's scheduling logic (ranking, preferences, standby) applies to **technicians only**.
- State this explicitly as an assumption in the report.

### 3.7 Certifications

- Store only **Brand** and **expiry date** per technician.
- A technician may hold one or both brands (dual).
- The system blocks placing a technician in a crew for a brand whose certification has expired.

---

## 4. Crew-forming algorithm (final)

The algorithm **suggests** a roster. The **manager reviews, edits and publishes** it (the brief says the manager allocates; the algorithm only assists).

### Before planning
1. Manager uploads the **HR leave CSV** and the **van availability CSV**.
2. Technicians submit their **standby-day pick** for the week (max 2 per day, one per brand, first come first served).

### For each working day of the Planning Week
3. **Remove** technicians on leave, emergency leave or MC.
4. Put technicians who **picked today** as their standby day **on standby**.
5. **Duals with 20 h or more last week** go on **standby, based in Central**.
6. **Rank** the remaining technicians:
   - by **last week's hours** (lowest first), then
   - by **this week's hours so far** (lowest first);
   - anyone at **40 h or more** goes to the **bottom**;
   - ties broken by **staff ID**; new staff start at **0 h**.
7. **Suggest crews** from the top of the ranked list. Each crew must **cover both brands** (one dual, or one M Electric + one Dicon). Max 3 people per van (1 driver + up to 2 technicians).
8. If **fewer than 3 crews** can be formed, bring standbys back into crews, **starting with the step 5 duals**. Never use someone on leave.
9. Everyone left over is **on standby** (assumed: usually at least 1 per brand).
10. **Update hours** (including half hours for unused standby) before planning the next day.

### After planning
11. Manager **reviews and edits** the suggestion, then **publishes**. Overrides are **logged**. Staff are **notified**.

### During the day (standby activation)
12. If someone drops out, the system lists **today's standbys**, sorted by:
    1. **fewest activations** (rolling 12 months), then
    2. **closest home zone** to the job's zone.
13. The manager **phones the top person outside the system**, then uses **Update Roster / Edit Hours** to record who took over from whom and the hours worked. Activated hours **replace** the half hours, and the technician's **activation count +1**. Staff are notified of the roster change.

### Intended effects (state these in the report)
- Technicians who were short of 40 h last week get priority this week; those who hit 40 h step back or go to standby. Hours alternating between heavier and lighter weeks is **intended** fair rotation.
- Someone returning from leave has low hours and gets priority, which helps them reach 40 h. This is **intended**.
- Ranking uses planned hours, so working slowly gains nothing (answers the prof's "people will delay on purpose" point).

---

## 5. Final class diagram: update instructions

Only the **final class diagram** from M1 carries into M2. Update it so that **every decision above has a class, an attribute and a method behind it**. Keep the ECB (Entity–Boundary–Control) structure from M1.

The attribute and method names below are **suggestions** to make the mechanism visible. Rename freely, but keep the mechanism.

### 5.1 Entity classes

| M1 class | Action | Changes |
|---|---|---|
| User (abstract) | Keep | name, email, contactNumber |
| Account | Keep | passwordHash, role, isActive/isLocked. Link to new PasswordResetToken. |
| **PasswordResetToken** | **Add** | token, expiresAt, used. `generate()`, `validate()`, `invalidateAll()`. Backs FR-47. |
| Manager | Keep | Methods for: upload CSV, review/publish roster, edit hours, update roster, compare staff, manage jobs. |
| IT Administrator | Keep | Creates accounts, sets home zone and certifications at creation, views Audit Log. |
| Staff (abstract) | Modify | Remove leave balance. Keep it simple; most logic now sits on Technician. |
| Driver | Keep (minimal) | No scheduling logic. One per crew. Note the "always available" assumption. |
| Technician | Modify | **Add** homeZone, lastWeekHours, currentWeekHours, activationCount (rolling 12 months). Remove job-completion methods. e.g. `getActiveHours()`, `incrementActivation()`. |
| Certification | Modify | **Remove** certificate number. Keep brand, expiryDate. `isValidOn(date)`. |
| Van | **Remove** as a managed entity | Replace with **VanAvailability** (below). Crew may keep a simple vanNumber reference from the CSV. |
| Workshop Servicing | **Remove** | Vendor's concern. |
| **VanAvailability** | **Add** | date, vansAvailable. Created from the van vendor CSV. Caps how many crews can be formed. |
| **LeaveRecord** | **Add** (replaces Leave Request) | technician, date, type (Leave / Emergency Leave / MC). Read-only, created from the HR CSV. |
| **CsvImport** | **Add** | type (HR / Van), uploadedBy, uploadedAt, status, errors. `parse()`, `validate()`. |
| Leave Request | **Remove** | Replaced by LeaveRecord. |
| Late Availability Change Request | **Remove** | Handled outside the system. |
| Availability | Keep | Staff still indicate availability up to 5 weeks ahead (brief requirement 8). *[Superseded: 1 month in advance, DEC-01, DEC-83.]* |
| Job Preference | **Replace** with **StandbyPreference** | technician, weekStart, chosenDay, brandSlot (M Electric / Dicon). One per technician per week. Max 2 per day (one per brand), first come first served. |
| Job | Modify | **Remove** actual times, remark, follow-up flag, invoice photo, Completed status. **Add** zone (N/E/S/W/C). Status = Assigned / Unassigned. Cancelled = deleted. Keep customer/address/postal code, brand, job type, units, preferred date/slot, planned duration. |
| Weekly Roster | Keep | weekStart, status (Draft / Published). `publish()` triggers notifications. |
| Crew | Modify | date, zone, members (1 driver + 1–2 technicians), must cover both brands. Stays together all day. |
| Assignment | Simplify | Links Job to Crew on a date. Remove completion-related history. |
| Standby | Modify | technician, date, source (Preference / Algorithm / Leftover), activated (bool), basedInCentral (for duals). Unused = half hours; activated = actual hours. |
| **HoursEdit** (or put on Audit Log) | **Add** | technician, date, oldHours, newHours, reason, editedBy. Created by Edit Hours. Supports "who took over whom". |
| Job Rejection Request | Simplify | requester, assignment, reason, status (Pending / Approved / Declined). Warning shown before submission. Approved → job becomes Unassigned. |
| Audit Log | Keep | who, what, when, why. Logs hours edits and roster overrides. Retention: rolling 12 months. |
| Notification | Keep / make explicit | recipient, type, message, sentAt, channel. Sent on publish and every change. Backs FR-40–42. |

### 5.2 Control classes

| Class | Action | Responsibility |
|---|---|---|
| **CrewFormingService** (or RosterSuggestionEngine) | **Add** | Runs the Section 4 algorithm. e.g. `suggestRoster(week)`, `rankTechnicians(day)`, `assignStandby(day)`, `ensureMinimumCrews(day)`. |
| **StandbyActivationService** | **Add** | `listStandbysForJob(job)` sorted by activation count then home-zone distance. |
| **CsvImportController** | **Add** | Handles upload, parsing, validation; creates LeaveRecord / VanAvailability. |
| **HoursController** | **Add** | Edit Hours and Update Roster; writes HoursEdit + Audit Log; recalculates workload. |
| RuleValidator | Keep | Hard rules: certification expiry, brand coverage per crew, max 3 per van, no double booking, standby cap per day, ≥3 crews per day. |
| NotificationService | Keep | Sends notifications on publish and every change. |
| **RetentionJob** (or a method on a storage class) | **Add** | Purges records and logs older than 12 months. Backs FR-10 / FR-46. |
| Existing controllers for login, accounts, jobs, roster, requests | Keep, trimmed | Remove leave-approval and job-completion logic. |

### 5.3 Boundary classes

Keep LoginPage, LandingPage, AccountAdminPage, JobAllocationPage, RequestPage. Add or adjust:
- **CsvUploadPage** (Manager)
- **StandbyPreferencePage** (Technician picks one day per week; full days greyed out)
- **EditHoursPage / UpdateRosterPage** (Manager)
- **StandbyListView** (Manager: today's standbys, sorted)
- Remove completion and leave-application pages.

### 5.4 Use case list (for consistency with the class diagram)

- **Remove:** UC-06 Manage Vans and Workshop Servicing; UC-14 Complete Job; leave-approval and late-availability parts of UC-09 / UC-12.
- **Add:** Upload CSV; Edit Hours / Update Roster; Set Standby Preference (replaces the preference part of UC-11).
- **Keep:** Log in/out, Reset Password, Create/Manage Accounts, Manage Job, Allocate Jobs / Set Weekly Schedule (now with suggested roster), Compare Staff, View Manpower Dashboard, Set Availability, Submit Job Rejection, View My Assignments and Workload, Notify Staff.
- Re-check every «extend» for genuine optionality. Draw Email/SMS as non-human actors (e.g. «system» boxes). HR and the van vendor are not actors.
- Renumber FRs and update every trace reference after removals.

---

## 6. M2 deliverables (suggestions; team to confirm)

### 6.1 Architecture pattern
- **Suggested: Layered / 3-tier architecture with MVC in the web tier.** Presentation (web pages) → Application/business logic (controllers, CrewFormingService, RuleValidator) → Data (on-site server database).
- Fits the M1 ECB split directly: Boundary = View, Control = Controller/Service, Entity = Model.
- Justify with: maintainability, separation of the scheduling algorithm from the UI, single on-site server.

### 6.2 Design patterns (pick 2–4 and show them in the class diagram)
| Pattern | Where it fits |
|---|---|
| **Strategy** | Ranking rules in CrewFormingService (e.g. `RankingStrategy` by last-week hours; standby activation ordering). Lets rules change without rewriting the engine. |
| **Observer** | NotificationService observes roster/job changes and notifies affected staff. |
| **Adapter** (or Factory) | CsvImport: one adapter per external format (HR CSV, Van CSV) converting to LeaveRecord / VanAvailability. |
| **Singleton** | A single NotificationService or database connection (only if justified). |
| **Facade** | One scheduling facade the Manager pages call, hiding CrewFormingService + RuleValidator + StandbyActivationService. |

### 6.3 Testing: black box and white box
**Black-box (equivalence partitioning + boundary value analysis)**, good test targets:
- Dual 20 h threshold: 19.5 / 20 / 20.5 h last week.
- 40 h rule: 39.5 / 40 / 40.5 h.
- Standby pick cap: 0, 1, 2 picks on a day; 3rd pick rejected; same-brand second pick rejected.
- Unused standby = half hours; activated standby replaces half hours.
- Minimum 3 crews: 2 / 3 / 4 crews formable.
- Certification expiry: expires the day before / on / after the job date.
- CSV upload: valid file, wrong columns, empty file, duplicate rows.
- Forgot password: valid token, expired token, reused token.

**White-box (statement / branch / path coverage)**, good targets:
- `rankTechnicians()`: branches for ≥40 h, ties, new staff at 0 h.
- `ensureMinimumCrews()`: path where standbys are pulled back, starting with duals.
- `listStandbysForJob()`: sort by activation count, then distance.
- Show a control-flow graph and cyclomatic complexity for at least one of these.

### 6.4 Wireframes (screens to draw)
- Login / Forgot password
- Manager landing page (workload bars, 40 h highlight, 3 lowest-workload staff)
- CSV upload page
- Job allocation page with the suggested roster, per-day crews, zones and standby list; compare up to 3 staff (showing their standby-day pick)
- Edit Hours / Update Roster page
- Standby activation list (today's standbys, sorted)
- Technician landing page (weekly assignments, weekly and monthly workload)
- Standby preference page (pick one day; full days greyed out)
- Job rejection with warning dialog
- IT Admin account creation (with home zone and certifications)

### 6.5 Component diagram (suggested components)
- Web UI (pages)
- Authentication (login, password reset)
- Job Management
- Scheduling Engine (CrewFormingService, RuleValidator, StandbyActivationService)
- Roster & Hours (Weekly Roster, Edit Hours)
- CSV Import (HR adapter, Van adapter)
- Notification (→ external Email/SMS gateway interface)
- Audit & Retention
- Database (on-site server)
Show provided/required interfaces between them, e.g. Scheduling Engine requires Job, Leave and Van data; Notification requires the Email/SMS gateway.

---

## 7. Still open / kept aside (do not invent answers; flag them)

- **Kept aside:** what happens when an uploaded HR CSV adds leave on a day someone already holds a standby pick or roster place (likely: the system flags the clash, and the manager resolves it).
- How a job gets its zone (suggestion: automatically from postal code).
- CSV upload details: deadline (before Thursday planning?), what happens to an already-published roster if a newer CSV changes availability, and handling of badly formatted files.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| Dual / dual-brand technician | Certified for both M Electric and Dicon. |
| Crew | 1 driver + 1–2 technicians on one van for one day, covering both brands. |
| Standby | Available technician not placed in a crew that day. |
| Activation | A standby being called in to replace someone during the day. |
| Active hours | Planned job hours + activated standby hours + manager edits (+ half hours for unused standby). |
| Planning Week | The week being scheduled; allocation runs one week at a time. |
| Zone | North, East, South, West or Central. |
| Home zone | A technician's base zone, used to find the closest standby. |
