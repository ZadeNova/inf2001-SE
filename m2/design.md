# M2 Design Notes (report §1.3, §2, §3)

> **Status: Draft v1.1.2 (2026-11-10).** Working text for the report, built from SRS v4.1.2 and the M2 diagrams (DEC-93/99/102–105). Diagrams are PlantUML sources in [diagrams/](../diagrams/). Render them **locally** only (see diagrams/README.md).

| Report section | Diagram |
|---|---|
| §1.3 Final class diagram | [CD-final](../diagrams/CD-final.puml) |
| §2 Component diagram | [CMP-system](../diagrams/CMP-system.puml) |
| §3.1 Architecture | [ARCH-layered](../diagrams/ARCH-layered.puml) |
| §3.2 Design pattern | [DP-strategy-ranking](../diagrams/DP-strategy-ranking.puml) |
| §3.2 Standard pattern structure | [DP-strategy-standard](../diagrams/DP-strategy-standard.puml) |
| §4.2 White-box CFG | [CFG-classify-technicians](../diagrams/CFG-classify-technicians.puml) |

---

## 1. Final class diagram (report §1.3)

### 1.1 What changed from M1

| M1 class | M2 | Why |
|---|---|---|
| Van, Workshop Servicing | Removed; **VanAvailability** (date, vansAvailable) added | Van details and servicing are the vendor's concern (DEC-85) |
| Leave Request, Late Availability Change Request | Removed; **LeaveRecord** (date, type) added | Leave comes read-only from the HR CSV; late changes happen outside the system (DEC-74, DEC-83) |
| Job Preference | Replaced by **StandbyPreference** (weekStart, chosenDay, brandSlot) | Provisional request; guaranteed initial placement only after capacity confirmation (DEC-98) |
| Certification | `number` removed | Not used by any decision (DEC-75) |
| Job | `actualStart`/`actualEnd`, completion and linking removed; `zone` added | Planned hours only; zones (DEC-76, DEC-77) |
| Crew | `needsAttention` removed; `vanNumber`, coverage `zones` added; effective per-Job membership | DEC-85, DEC-77, DEC-90 |
| Standby | `source`, `activated` added; `effectiveZone()`, `hours()`; retain record and count activated dates once | Activation and 4 h Standby hours (DEC-78, DEC-81) |
| Technician | `homeZone` added; hours and activation count are **methods** | DEC-77, DEC-87 |
| — | **PasswordResetToken**, **CsvImport**, **HoursEdit**, **Replacement** added | FR-47, FR-52, FR-53, FR-54, FR-57; DEC-96/97 |
| — | **CrewFormingService**, **StandbyActivationService**, **CsvImportController**, **HoursController**, **StandbyPreferenceController**, **RetentionJob** added | FR-51, FR-52, FR-53, FR-54, FR-55, FR-56, FR-57, FR-58 |
| VanController, CompletionController; VanPage, JobCompletionPage | Removed | UC-06 and UC-14 withdrawn |
| — | «interface» **TechnicianRanking**, **CsvRowMapper**, **NotificationChannel** | Template asks for «interface» classes; the Strategy pattern; CSV adapters; Email/SMS channels |

### 1.2 Mechanism check (lecturer's M1 feedback)

Every stored value has an owning class and a method that changes it (SRS §3 "Mechanism" column). The values the lecturer named:

| Lecturer's point | Class and method |
|---|---|
| Forgotten password | `PasswordResetToken.generate()`, `validate()`, `invalidateAll()` via `AuthController.resetPassword()` (FR-47) |
| Keeping past records / 12-month tracking | `RetentionJob.runDaily()` → `purgeOlderThan(12)` (FR-58). `Technician.activationCount(asOf)` counts distinct activated Standby dates within 12 months (DEC-87) |
| Notifications | `NotificationService.notify()` → `Notification` + `NotificationChannel.send()` (FR-39) |
| Standby and replacement end to end | `CrewFormingService` names Standby (FR-55) → `StandbyActivationService.listStandbysForJob()` (FR-56) → `HoursController.activateForJob()` / `recordReplacement()` and `editHours()` (FR-57) |
| Hours on planned time | `Staff.activeHoursOn(date)` sums attributed `Job.plannedHours()` or the latest Active Hours Edit; `hoursOn(date)` applies the once-daily max(4, Active Hours) Standby floor (DEC-96) |
| Zones | `Job.deriveZone()` via `Zone.fromPostalCode()`; `Crew.setZones()`; `Technician.homeZone`; `Zone.distanceTo()` |

Consistency corrections (DEC-99) make existing requirements explicit: `Account.firstFailedAt` anchors FR-48's 15-minute window; `knownDevices` maps device IDs to last-used timestamps for NFR-07; `Notification.deliveryState` retains email/SMS outcomes independently of Landing Page handling (FR-39/40). `AccountController` delegates future-roster removal and `RequestController` delegates approved unassignment to `RosterController`; `CsvImportController` owns the application-layer mapper (FR-05/45/46/52–54). `CsvImport.parse(file)` returns rows only. The controller checks columns/rows through `CsvRowMapper`, collects whole-file errors and calls `CsvImport.recordValidation(errors)`. Errors mark the import Rejected and save no business rows; otherwise the controller maps the validated rows and, in one transaction, replaces the Leave Records or Van Availability for the dates in the file, calls `CsvImport.commit()` to mark the import `Committed`, and writes the successful-upload `AuditLog` entry. The entity does not call upward into its mapper (DEC-104/106).

---

## 2. Component diagram (report §2)

The class diagram's packages correspond **one to one** with the components. Every component's control classes live in its package, and all entities live in Domain Model.

| Component | Classes (CD-final package) | Responsibility | Provides | Requires |
|---|---|---|---|---|
| **Web UI** | All «boundary» pages | Role-specific pages in the browser (NFR-11) | — | IAuthentication, IAccountAdmin, IStaffInputs, ICsvImport, IJobManagement, IScheduling (eligible Standby list only), IRoster |
| **Authentication** | AuthController | Login, new-device check, logout, password reset | IAuthentication | IDomainModel, INotify |
| **Account Management** | AccountController | Accounts, roles, lockouts, Technician profiles, Audit Log search | IAccountAdmin | IDomainModel, INotify, IRoster (remove future roster places) |
| **Staff Inputs** | AvailabilityController, StandbyPreferenceController, RequestController | Availability, provisional picks and post-deadline confirmation, Job Rejection submission and Manager-only decisions | IStaffInputs | IDomainModel, IScheduling (rule checks), IRoster (approved unassignment), INotify |
| **CSV Import** | CsvImportController, CsvRowMapper, HrLeaveCsvMapper, VanAvailabilityCsvMapper | Validates and commits HR and van CSV files | ICsvImport | IDomainModel |
| **Job Management** | JobController | Create, edit and delete Jobs; Unassigned list | IJobManagement | IDomainModel, IScheduling (edit validation), INotify |
| **Scheduling Engine** | CrewFormingService, StandbyActivationService, RuleValidator, TechnicianRanking (+2) | Suggested Roster, Standby ordering, all block and warn rules | IScheduling | IDomainModel |
| **Roster & Hours** | RosterController, HoursController, DashboardController | Prepare confirmations/suggestion, allocate Crew/direct duties, publish, replacements, Active Hours edits, dashboards | IRoster | IStaffInputs, IScheduling, IDomainModel, INotify |
| **Notification** | NotificationService, NotificationChannel, EmailChannel, SmsChannel | Stores and delivers notifications | INotify | IDomainModel, IEmailGateway, ISmsGateway |
| **Audit & Retention** | RetentionJob | Daily 12-month purge (Clock) | — | IDomainModel |
| **Domain Model** | All «entity» classes and enumerations | Business data and derived values (hours, activation count) | IDomainModel | IPersistence |
| **Workload database** | — | On-site persistent storage (NFR-13) | IPersistence | — |
| Email Service «system», SMS Gateway «system» | External | Deliver email and SMS | IEmailGateway, ISmsGateway | — |

**Design rationale.**
- The Scheduling Engine is a separate component, so the algorithm and its rules can change without touching the pages or roster storage. Roster & Hours, Staff Inputs and Job Management use IScheduling. The Web UI uses it only for the eligible Standby list; suggestion always goes through `RosterController.prepareSuggestion()` so confirmation runs first (FR-55).
- Notification is the only component that talks to the outside world, through one interface per gateway.
- Cross-layer dependencies point downwards (Web UI → application → Domain Model → database). Application components may collaborate through their required interfaces. The bidirectional Roster & Hours / Staff Inputs dependency serves distinct operations: Roster & Hours calls IStaffInputs for preference confirmation during UC-07, while Staff Inputs calls IRoster for approved Job unassignment during UC-09. Both are application-layer collaborations; neither reverses the layer direction nor requires the calls to recurse (DEC-104).

---

## 3. Architecture (report §3.1)

**Pattern:** layered (3-tier) architecture with MVC in the web tier ([ARCH-layered](../diagrams/ARCH-layered.puml)).

| Layer | MVC role | Classes | Responsibility |
|---|---|---|---|
| Presentation | View | «boundary» pages | Show data, collect input, show warnings and confirmations. No business rules |
| Application | Controller | «control» controllers and services | Carry out use cases, run the Suggested Roster, check rules, send notifications, purge records |
| Data | Model | «entity» classes + on-site database | Hold the state and derive hours and counts; persist on the on-site server |

**How the layers interact:** each layer calls only the one below it. A page calls an application controller; `StandbyListView` calls the eligible-list service for a read. Controllers call services (for example `RuleValidator`, `CrewFormingService`) and entities. Entities are persisted in the database. Results flow back up as page data. Suggestion always follows the controller preparation/confirmation route.

**Why this architecture:**
1. **It matches our analysis model.** The M1 Entity–Boundary–Control (ECB) classes map directly to View, Controller and Model, while the historical M1 sequence diagrams must be checked before reuse because scheduling behaviour changed.
2. **It separates the algorithm from the UI.** The crew-forming rules (DEC-80) are the part the client is most likely to change. They sit in one application component behind IScheduling.
3. **It fits a single on-site server** (NFR-13). The client asked for on-site storage. A small team of 17 Staff and 1–2 Managers needs no distributed design, so a monolith in three layers is enough.
4. **It supports the requirements.**
   - Role-based access (NFR-09) is checked in one place, the controllers.
   - The 12-month purge (FR-58) and backups (NFR-04) touch only the data layer.
   - Browser-only access (NFR-11) is the presentation layer.

**Use-case example (UC-07):** `JobAllocationPage.suggestRoster()` → `RosterController.prepareSuggestion(week)` → `StandbyPreferenceController.confirmWeek(week)` → `CrewFormingService.suggestRoster(week)` → reads `Availability`, `LeaveRecord`, `VanAvailability` and `StandbyPreference`, and writes `Crew` and `Standby` → the page shows the Draft roster.

DEC-102 resolves the NFR-05/13 boundary: the browser may keep a per-user read-only copy containing only the signed-in Staff member's Published Assignments for today. Clear it at logout and expire it when its date passes; authoritative database records and logs remain on-site. `LandingPage.cacheToday(staff, assignments)` refreshes the encrypted copy after each successful online load of today's Published Assignments, without requiring a fresh login in an existing authenticated session. `loadCachedToday()` checks Staff/date and locked state; `unlockCachedToday(password)` performs local password unlocking after app closure/reopening offline, with no connection or server login. Wrong passwords keep the copy locked; no repeated prompt is needed while it remains unlocked. `clearCachedToday()` clears it at logout. NFR-08 applies to this browser copy as well as on-site storage: a password-derived or password-protected key must prevent reading the persisted copy without the Staff member's password, with no readable persisted decryption key (DEC-105). This goal concerns stored data; it does not claim protection of an already unlocked view. Algorithm/library and key derivation/protection technique remain implementation choices. Existing-session key lifecycle, password changes/resets and broader authentication details still need specification/verification under DEC-61/105; no offline attempt limit or new session policy is adopted. Date expiry prevents later viewing when the app next checks the date; it does not promise deletion from a device while the app is closed. DEC-103 resolves FR-04/39: deleting an Assigned Draft Job sends no Staff notice; the Published deletion notice and existing preference-outcome exception remain. Historical DEC-100/101 entries are retained, with these later resolutions.

---

## 4. Design pattern (report §3.2): Strategy

**Design problem.** The system ranks Technicians in two places, with two different fairness rules:
- **Crew forming (FR-55):** last week's Active Hours, then projected Active Hours, then staff ID.
- **Standby activation (FR-56):** fewest distinct activated dates in 12 months, then zone distance, then staff ID.

The client has already changed these rules once (M2-Brief §4), and they are the most likely to change again. If the rules were coded inside `CrewFormingService` and `StandbyActivationService`, every change would mean editing and re-testing the algorithms themselves.

**Pattern.** Strategy defines a family of algorithms, puts each in its own class behind a common interface, and lets the client object (the Context) use any of them interchangeably.

**Standard structure:**

```text
Context ──────────────> «interface» Strategy
  -strategy               +algorithm()
  +operation()                 ▲            ▲
                               │            │
                     ConcreteStrategyA  ConcreteStrategyB
```

**Applied in our design** ([DP-strategy-ranking](../diagrams/DP-strategy-ranking.puml)):

| Pattern role | Our class |
|---|---|
| Strategy | «interface» `TechnicianRanking` with `order(candidates, context)` |
| ConcreteStrategy A | `WorkloadRanking` (crew-forming order) |
| ConcreteStrategy B | `ActivationRanking` (Standby activation order) |
| Context 1 | `CrewFormingService`, which uses `WorkloadRanking` in `classifyTechnicians()` and `ensureMinimumCrews()` |
| Context 2 | `StandbyActivationService`, which uses `ActivationRanking` in `listStandbysForJob()` |

At application construction, configure `CrewFormingService` with a `WorkloadRanking` implementation and `StandbyActivationService` with an `ActivationRanking` implementation, through their `TechnicianRanking` references (DEC-93). Tests may supply another implementation of the same ordering contract. Runtime switching by a Manager is not required. The pseudocode's context is the working date/Planning Week for workload ranking, or the selected duty's date and Job Zone for activation ranking; each caller supplies the values its strategy needs.

**How it improves the design:**
- A new fairness rule is a new class. For example, a seniority tie-break would be a `SeniorityRanking`, and the algorithms stay unchanged (open/closed principle).
- Each ranking can be unit-tested on its own with a list of Technicians.
- The same sorting code could be written as two comparators, but the interface gives the larger workflows a common replaceable test/configuration seam when the existing fairness rules change; it does not add a new fairness policy.
- The contexts depend only on the interface, which keeps the Scheduling Engine's internals loosely coupled.

**Alternatives considered:**
- *Observer* for notifications: it would decouple Roster & Hours from Notification, but the system has a single subscriber (NotificationService), so the benefit is small.
- *Adapter* for CSV files: `CsvRowMapper` is kept in the class diagram as an «interface», but it is not written up as the pattern.

## 5. Scheduling clarification model (DEC-96–98)

- **Two derived hour totals:** Active Hours come from per-Job attributed Staff or a reasoned correction. Workload/Total Credited Hours retain the 4 h daily minimum for all rostered Standby dates, including short activations. HoursEdit stores old/new Active Hours; it cannot override the credit floor. The 40 h demotion uses projected Credited Hours; tie-breaking/dual rotation use Active Hours.
- **Assignment owns participation:** store dutyDate and attributed Staff. A Crew Assignment copies Crew.membersFor(job); a direct duty has no Crew and exactly one certified Technician. The WeeklyRoster owns both kinds. Person-level schedule validation applies across both routes.
- **Replacement preserves history:** one new entity records Crew, outgoing/incoming Technician, fromJobId, effectiveFrom, Manager/reason/time. Only affected unstarted Assignment snapshots change. Earlier Jobs and the initial Crew stay intact. The stable Job identifier and effective time retain the boundary if a later unstarted Job is unassigned. A later Job uses effective members after all applicable replacements.
- **Retained Standby:** a unique Technician/date record persists after activation for entitlement and distinct-date counting. A second non-overlapping direct duty reuses that record. A replacement commits the Technician to that Crew; it cannot create a second Crew commitment. Full-day Leave without duties has no Standby minimum; a mid-day departure retains earlier credited duties.
- **Preference state:** Provisional requests reserve slots before the deadline. After locked inputs/CSVs, confirmWeek checks >=3 valid initial Crews plus Full Standby cover and resolves requests in submittedAt/staff-ID order. Persist decision reason/time; confirmation is idempotent and binding. Roster & Hours requires IStaffInputs. Outcome notifications bypass Draft Assignment suppression without exposing Jobs.
- **Capacity and zones:** use the same small feasible-arrangement check for confirmation and greedy fallback. Three is a minimum; direct duties do not count as initial Van Crews. Crew.zones is a set of the existing five Zones. All Standby candidates use home Zone, not a forced Central location. Transport stays outside the application.
- **Fairness limit:** low counts are recommendations among eligible people, not evidence of laziness or a guarantee against refusal. Failed-call outcomes can use the existing Audit Log; no penalty engine is introduced.

The current M2 diagrams are updated; the submitted M1 diagrams and source interviews are historical evidence and remain unchanged.
