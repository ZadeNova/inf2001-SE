# INF2001 P8-1: M2 Design Update Brief

> **Source record and revision.** The team's original M2 Design Update Brief was copied here on 2026-11-06. This working copy now incorporates the member-confirmed 2026-11-07 clarifications in DEC-96–98 and SRS v4.1; the unchanged original is available in git history. Sections 1–4 contain the current team decisions; sections 5–6 retain design guidance. The availability horizon is 1 month (DEC-01/83).

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
| **Zones** | Jobs are sorted into **North, East, South, West, Central**. The manager decides which Zone or group of Zones each van/crew covers; the algorithm does not. |
| **Crews** | Start with a fixed Crew; recorded replacements take effect from a specified Job. They **can go home** after their last job (no reporting back to base). |
| **Home zone** | New attribute on every technician. Used to find the closest standby. |
| **Manager availability page** | Shows who is available and not on leave (from the HR CSV). |
| **Notifications** | Sent for the **initial roster publication and every later change** (roster changes, job changes, deletions, standby assignment, job rejection outcomes). |
| **Forgot password** | New class (e.g. password reset token) to back FR-47. |
| **Notification class** | New/explicit class to back FR-40–42. |
| **Storage** | Records and logs are saved on an **on-site server backend** (persistent storage). |
| **Retention** | Records and logs are kept for a **rolling 12 months**, then purged. |
| **40-hour highlight** | Kept (brief requirement 6). Manager landing page shows the 3 lowest-workload staff and highlights anyone over 40 h. |

### 3.3 Hours and workload (DEC-96)

- Active Hours are the Planned Hours of Jobs attributed to each person, including direct/replacement duties and audited Active Hours corrections.
- Total Credited Hours are Active Hours on ordinary days; on a rostered Standby day use **max(4, Active Hours)**. Apply that minimum once per date. Full-day Leave without duties gives zero; preserve earlier Jobs on a mid-day departure.
- Workload sums Total Credited Hours for the week/month. Use it for the 40 h target/highlight and display Active Hours separately.
- Crew rotation uses last week's Active Hours, including the dual >=20 h rule. Projected Credited >=40 h is demoted; then rank by last week's Active, projected Active and staff ID.
- Before Job allocation, estimate Active/Credited as Crew 8/8 and Standby 0/4. After allocation use attributed Planned Hours.
- Standby examples Active/Credited: unused 0/4, 2 h duty 2/4, 4 h duty 4/4, 5 h duty 5/5. Two duties of 2+3 h give 5/5.

### 3.4 Preferences (DEC-98)

- One provisional day/Brand slot request per Technician/week; one M Electric and one Dicon slot per day, first come first served. Change/withdraw before Wednesday's deadline.
- After inputs lock and HR/Van CSVs arrive, process by submittedAt/staff ID. Confirm only when valid eligibility, **three initial Crews and Full Standby cover** remain feasible with previously confirmed picks reserved.
- Store Provisional / Confirmed / NotConfirmed, decision time and reason; notify outcomes. A provisional slot is not a guarantee.
- Confirmed means initial Standby placement. Managers cannot override it. Leave takes precedence; activation for genuine direct/replacement work remains permitted.
- Re-running the suggestion preserves confirmations. Later shortages are flagged for repair; no silent revocation.
- The member reports the professor's work-life-balance clarification as the basis for binding confirmation (DEC-98).

### 3.5 Standby (DEC-96/97)

- Standby initially means an available Technician outside the active Van Crews. Keep the record after activation for history and credit.
- Full Standby cover means valid coverage for both Brands (one M Electric + one Dicon, or a dual); no maximum.
- Required initial Crews take priority; no preference is confirmed unless both minimum Crews and Full Standby cover are feasible.
- Standby uses the Technician's **home Zone**, including Algorithm-source duals. Three Crews can cover groups of the existing five Zones.
- A direct activation may send a certified Technician to extra Jobs using paid transport without a Driver/Van, then return when finished. A replacement travels to join a Crew from an unstarted Job. Transport booking/payment remains outside the system.
- Filter eligibility first, then rank by distinct activated dates over 12 months, home-Zone distance and staff ID. Recheck before saving.
- Repeated duties/call-outs on one date count **one activated day**. Low count earns priority; it does not prove laziness or prevent refusal by itself.
- Standby and active work are paid the same; this application does not calculate payroll.

### 3.6 Drivers

- Drivers are deliberately kept simple: **assumed always available, one per van**. The system's scheduling logic (ranking, preferences, standby) applies to **technicians only**.
- State this explicitly as an assumption in the report.

### 3.7 Certifications

- Store only **Brand** and **expiry date** per technician.
- A technician may hold one or both brands (dual).
- The system blocks placing a technician in a crew for a brand whose certification has expired.

---

## 4. Crew-forming algorithm (DEC-96–98)

1. Staff submit Availability and provisional preference requests before Wednesday's deadline. Manager uploads HR/Van CSVs before Thursday planning.
2. Resolve requests in submission order using a feasible minimum arrangement: >=3 valid initial Crews plus Full Standby cover, while reserving earlier confirmations. Record outcomes and notify.
3. Per date, exclude unavailable/Leave Staff and reserve confirmed picks. Put duals with >=20 **Active Hours** last week on Algorithm Standby.
4. Rank the remaining Technicians: projected **Credited** <40 first; then last week's Active Hours, projected Active Hours, staff ID.
5. Form both-Brand Crews (one dual or an opposite-Brand pair), up to Van count. Beyond three, preserve Full Standby cover. If below three, recall Algorithm then Leftover Standby, lowest-ranked first; never take confirmed picks.
6. If greedy pairing loses a feasible minimum/cover arrangement, use the feasibility result. This is a small search over 11 Technicians, not an optimisation framework.
7. Put leftovers on Standby; assign available Drivers by ID. Project Crew 8/8 and Standby 0/4 Active/Credited before the next date.
8. Manager reviews, sets coverage Zones, allocates Jobs and publishes. Confirmed picks are hard constraints. Publication below three valid initial Crews is blocked; missing full cover can still be a reasoned warning where the minimum Crews take priority.
9. During the day, activate eligible Standby for direct Jobs or replacements. Store per-Job attributed Staff and Replacement boundaries; preserve earlier members. Recompute the two hours figures and count the activated date once.
10. Regeneration preserves confirmations and is refused when Jobs/manual edits would be discarded.

**Intended effects:** unused Standby credit cannot trap duals in the >=20 Active Hours branch. Lower Active Hours give crew priority; fewer activated dates give call-up priority. These rules distribute opportunities among eligible Staff; the Manager handles non-attendance. Planned duration avoids rewards for stalling.

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
| Technician | Modify | homeZone; derived lastWeekActiveHours, projectedActiveHours, projectedCreditedHours and distinct activated-day count. No stored mutable fairness counter. |
| Certification | Modify | **Remove** certificate number. Keep brand, expiryDate. `isValidOn(date)`. |
| Van | **Remove** as a managed entity | Replace with **VanAvailability** (below). Crew may keep a simple vanNumber reference from the CSV. |
| Workshop Servicing | **Remove** | Vendor's concern. |
| **VanAvailability** | **Add** | date, vansAvailable. Created from the van vendor CSV. Caps how many crews can be formed. |
| **LeaveRecord** | **Add** (replaces Leave Request) | technician, date, type (Leave / Emergency Leave / MC). Read-only, created from the HR CSV. |
| **CsvImport** | **Add** | type (HR / Van), uploadedBy, uploadedAt, status, errors. `parse()`, `validate()`. |
| Leave Request | **Remove** | Replaced by LeaveRecord. |
| Late Availability Change Request | **Remove** | Handled outside the system. |
| Availability | Keep | Staff still indicate availability up to 1 month ahead (brief requirement 8). *[Superseded: 1 month in advance, DEC-01, DEC-83.]* |
| Job Preference | Replace with StandbyPreference | weekStart, chosenDay, brandSlot, submittedAt, status, decidedAt, decisionReason; provisional request then capacity-checked confirmation. |
| Job | Modify | **Remove** actual times, remark, follow-up flag, invoice photo, Completed status. **Add** zone (N/E/S/W/C). Status = Assigned / Unassigned. Cancelled = deleted. Keep customer/address/postal code, brand, job type, units, preferred date/slot, planned duration. |
| Weekly Roster | Keep | weekStart, status (Draft / Published). `publish()` triggers notifications. |
| Crew | Modify | date, vanNumber, coverage zones, initial Driver/Technicians; membersFor(job) applies recorded replacements. |
| Assignment | Modify | Job, dutyDate, startTime and attributed Staff. Optional Crew; a direct duty has exactly one Technician. Earlier Job Staff survive replacements. |
| Standby | Modify | Technician/date/source/activated; retained after activation. Home Zone for ranking, max(4, Active Hours) credit, activated date counted once. |
| **HoursEdit** | Add | Staff/date/oldActiveHours/newActiveHours/reason/Manager/time. Correct Active Hours, derive credited total. |
| **Replacement** | Add | Crew, outgoing/incoming Technician, fromJobId, effectiveFrom, Manager/reason/time. Preserve earlier Job attribution. |
| Job Rejection Request | Simplify | requester, assignment, reason, status (Pending / Approved / Declined). Warning shown before submission. Approved → job becomes Unassigned. |
| Audit Log | Keep | who, what, when, why. Logs hours edits and roster overrides. Retention: rolling 12 months. |
| Notification | Keep / make explicit | recipient, type, message, sentAt, channel. Sent on publish and every change. Backs FR-40–42. |

### 5.2 Control classes

| Class | Action | Responsibility |
|---|---|---|
| **CrewFormingService** (or RosterSuggestionEngine) | **Add** | Runs the Section 4 algorithm. e.g. `suggestRoster(week)`, `rankTechnicians(day)`, `assignStandby(day)`, `ensureMinimumCrews(day)`. |
| **StandbyActivationService** | Add | Filter eligible candidates for direct/replacement duty before ordering by activated-day count, home-Zone distance and staff ID. |
| **CsvImportController** | **Add** | Handles upload, parsing, validation; creates LeaveRecord / VanAvailability. |
| **HoursController** | **Add** | Edit Hours and Update Roster; writes HoursEdit + Audit Log; recalculates workload. |
| RuleValidator | Keep | Certifications, person-level conflicts, Crew size/capacity, confirmed preferences, minimum-Crew feasibility plus standby coverage. No overall Standby cap. |
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
| **Strategy** | Ranking rules in CrewFormingService (e.g. `RankingStrategy` by last-week Active Hours; standby activation ordering). Lets rules change without rewriting the engine. |
| **Observer** | NotificationService observes roster/job changes and notifies affected staff. |
| **Adapter** (or Factory) | CsvImport: one adapter per external format (HR CSV, Van CSV) converting to LeaveRecord / VanAvailability. |
| **Singleton** | A single NotificationService or database connection (only if justified). |
| **Facade** | One scheduling facade the Manager pages call, hiding CrewFormingService + RuleValidator + StandbyActivationService. |

### 6.3 Testing: black box and white box
**Black-box (equivalence partitioning + boundary value analysis)**, good test targets:
- Dual 20 h threshold: 19.5 / 20 / 20.5 Active Hours last week.
- 40 h rule: 39.5 / 40 / 40.5 h.
- Standby pick cap: 0, 1, 2 picks on a day; 3rd pick rejected; same-brand second pick rejected.
- Standby daily minimum: Active/Credited 0/4, 2/4, 4/4, 5/5; multiple duties share one floor/count.
- Minimum 3 crews: 2 / 3 / 4 crews formable.
- Certification expiry: expires the day before / on / after the job date.
- CSV upload: valid file, wrong columns, empty file, duplicate rows.
- Forgot password: valid token, expired token, reused token.

**White-box (statement / branch / path coverage)**, good targets:
- `rankTechnicians()`: branches for ≥40 h, ties, new staff at 0 h.
- `ensureMinimumCrews()`: path where standbys are pulled back, starting with duals.
- `listStandbysForJob()`: filter eligibility, then sort by activated-day count and distance.
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

- **Resolved in DEC-98:** later Leave overrides placement, is flagged for Manager repair and does not silently revoke other confirmed preferences.
- Job Zone derives from postal sector (DEC-77); the actual lookup table remains to be supplied (SRS A6).
- CSV upload details: deadline (before Thursday planning?), what happens to an already-published roster if a newer CSV changes availability, and handling of badly formatted files.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| Dual / dual-brand technician | Certified for both M Electric and Dicon. |
| Crew | Initial Driver + 1–2 Technicians on a Van/date, with one or more coverage Zones and effective membership per Job. |
| Standby | Initially reserved Technician; record retained after activation for daily credit/history. |
| Activation | Direct Standby duty or Crew replacement; repeated duties count one activated date. |
| Active hours | Attributed Planned Hours of actual assigned duties; unused Standby credit is excluded. |
| Total Credited Hours / Workload | Active Hours on ordinary days; max(4, Active Hours) on rostered Standby dates. |
| Planning Week | The week being scheduled; allocation runs one week at a time. |
| Zone | North, East, South, West or Central. |
| Home zone | A technician's base zone, used to find the closest standby. |
