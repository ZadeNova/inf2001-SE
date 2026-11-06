# M2 Design Notes (report §1.3, §2, §3)

> **Status: Draft v1.0 (2026-11-06).** Working text for the report, built from SRS v4.0 and the M2 diagrams (DEC-93). Diagrams are PlantUML sources in [diagrams/](../diagrams/). Render them **locally** only (see diagrams/README.md).

| Report section | Diagram |
|---|---|
| §1.3 Final class diagram | [CD-final](../diagrams/CD-final.puml) |
| §2 Component diagram | [CMP-system](../diagrams/CMP-system.puml) |
| §3.1 Architecture | [ARCH-layered](../diagrams/ARCH-layered.puml) |
| §3.2 Design pattern | [DP-strategy-ranking](../diagrams/DP-strategy-ranking.puml) |
| §4.2 White-box CFG | [CFG-classify-technicians](../diagrams/CFG-classify-technicians.puml) |

---

## 1. Final class diagram (report §1.3)

### 1.1 What changed from M1

| M1 class | M2 | Why |
|---|---|---|
| Van, Workshop Servicing | Removed; **VanAvailability** (date, vansAvailable) added | Van details and servicing are the vendor's concern (DEC-85) |
| Leave Request, Late Availability Change Request | Removed; **LeaveRecord** (date, type) added | Leave comes read-only from the HR CSV; late changes happen outside the system (DEC-74, DEC-83) |
| Job Preference | Replaced by **StandbyPreference** (weekStart, chosenDay, brandSlot) | A preference the system can guarantee (DEC-79) |
| Certification | `number` removed | Not used by any decision (DEC-75) |
| Job | `actualStart`/`actualEnd`, completion and linking removed; `zone` added | Planned hours only; zones (DEC-76, DEC-77) |
| Crew | `needsAttention` removed; `vanNumber`, `zone` added | DEC-85, DEC-77, DEC-90 |
| Standby | `source`, `activated` added; `effectiveZone()`, `hours()` | Activation and 4 h Standby hours (DEC-78, DEC-81) |
| Technician | `homeZone` added; hours and activation count are **methods** | DEC-77, DEC-87 |
| — | **PasswordResetToken**, **CsvImport**, **HoursEdit** added | FR-47, FR-52, FR-53, FR-54, FR-57 |
| — | **CrewFormingService**, **StandbyActivationService**, **CsvImportController**, **HoursController**, **StandbyPreferenceController**, **RetentionJob** added | FR-51, FR-52, FR-53, FR-54, FR-55, FR-56, FR-57, FR-58 |
| VanController, CompletionController; VanPage, JobCompletionPage | Removed | UC-06 and UC-14 withdrawn |
| — | «interface» **TechnicianRanking**, **CsvRowMapper**, **NotificationChannel** | Template asks for «interface» classes; the Strategy pattern; CSV adapters; Email/SMS channels |

### 1.2 Mechanism check (lecturer's M1 feedback)

Every stored value has an owning class and a method that changes it (SRS §3 "Mechanism" column). The values the lecturer named:

| Lecturer's point | Class and method |
|---|---|
| Forgotten password | `PasswordResetToken.generate()`, `validate()`, `invalidateAll()` via `AuthController.resetPassword()` (FR-47) |
| Keeping past records / 12-month tracking | `RetentionJob.runDaily()` → `purgeOlderThan(12)` (FR-58). `Technician.activationCount(asOf)` counts activated Standby records within 12 months (DEC-87) |
| Notifications | `NotificationService.notify()` → `Notification` + `NotificationChannel.send()` (FR-39) |
| Standby and replacement end to end | `CrewFormingService` names Standby (FR-55) → `StandbyActivationService.listStandbysForJob()` (FR-56) → `HoursController.recordReplacement()` and `editHours()` (FR-57) |
| Hours on planned time | `Staff.hoursOn(date)` uses `Job.plannedHours()`, 4 h Standby or an `HoursEdit` (FR-35); no actual times are stored |
| Zones | `Job.deriveZone()` via `Zone.fromPostalCode()`; `Crew.setZone()`; `Technician.homeZone`; `Zone.distanceTo()` |

---

## 2. Component diagram (report §2)

The class diagram's packages correspond **one to one** with the components. Every component's control classes live in its package, and all entities live in Domain Model.

| Component | Classes (CD-final package) | Responsibility | Provides | Requires |
|---|---|---|---|---|
| **Web UI** | All «boundary» pages | Role-specific pages in the browser (NFR-11) | — | IAuthentication, IAccountAdmin, IStaffInputs, ICsvImport, IJobManagement, IScheduling, IRoster |
| **Authentication** | AuthController | Login, new-device check, logout, password reset | IAuthentication | IDomainModel, INotify |
| **Account Management** | AccountController | Accounts, roles, lockouts, Technician profiles, Audit Log search | IAccountAdmin | IDomainModel, INotify, IRoster (remove future roster places) |
| **Staff Inputs** | AvailabilityController, StandbyPreferenceController, RequestController | Availability, Standby picks, Job Rejection Requests | IStaffInputs | IDomainModel, IScheduling (rule checks), INotify |
| **CSV Import** | CsvImportController, CsvRowMapper, HrLeaveCsvMapper, VanAvailabilityCsvMapper | Validates and commits HR and van CSV files | ICsvImport | IDomainModel |
| **Job Management** | JobController | Create, edit and delete Jobs; Unassigned list | IJobManagement | IDomainModel, INotify |
| **Scheduling Engine** | CrewFormingService, StandbyActivationService, RuleValidator, TechnicianRanking (+2) | Suggested Roster, Standby ordering, all block and warn rules | IScheduling | IDomainModel |
| **Roster & Hours** | RosterController, HoursController, DashboardController | Allocation, Crew and Standby edits, publish, timeline, replacements, Hours Edits, dashboards | IRoster | IScheduling, IDomainModel, INotify |
| **Notification** | NotificationService, NotificationChannel, EmailChannel, SmsChannel | Stores and delivers notifications | INotify | IDomainModel, IEmailGateway, ISmsGateway |
| **Audit & Retention** | RetentionJob | Daily 12-month purge (Clock) | — | IDomainModel |
| **Domain Model** | All «entity» classes and enumerations | Business data and derived values (hours, activation count) | IDomainModel | IPersistence |
| **Workload database** | — | On-site persistent storage (NFR-13) | IPersistence | — |
| Email Service «system», SMS Gateway «system» | External | Deliver email and SMS | IEmailGateway, ISmsGateway | — |

**Design rationale.**
- The Scheduling Engine is a separate component, so the algorithm and its rules can change without touching the pages or the roster storage. Roster & Hours and Staff Inputs reach it only through IScheduling.
- Notification is the only component that talks to the outside world, through one interface per gateway.
- All dependencies point downwards (Web UI → application → Domain Model → database), matching the layered architecture.

---

## 3. Architecture (report §3.1)

**Pattern:** layered (3-tier) architecture with MVC in the web tier ([ARCH-layered](../diagrams/ARCH-layered.puml)).

| Layer | MVC role | Classes | Responsibility |
|---|---|---|---|
| Presentation | View | «boundary» pages | Show data, collect input, show warnings and confirmations. No business rules |
| Application | Controller | «control» controllers and services | Carry out use cases, run the Suggested Roster, check rules, send notifications, purge records |
| Data | Model | «entity» classes + on-site database | Hold the state and derive hours and counts; persist on the on-site server |

**How the layers interact:** each layer calls only the one below it. A page calls a controller. The controller calls services (for example `RuleValidator`, `CrewFormingService`) and entities. Entities are persisted in the database. Results flow back up as page data.

**Why this architecture:**
1. **It matches our analysis model.** The M1 Entity–Boundary–Control (ECB) classes map directly to View, Controller and Model, so the M1 sequence diagrams stay valid.
2. **It separates the algorithm from the UI.** The crew-forming rules (DEC-80) are the part the client is most likely to change. They sit in one application component behind IScheduling.
3. **It fits a single on-site server** (NFR-13). The client asked for on-site storage. A small team of 17 Staff and 1–2 Managers needs no distributed design, so a monolith in three layers is enough.
4. **It supports the requirements.**
   - Role-based access (NFR-09) is checked in one place, the controllers.
   - The 12-month purge (FR-58) and backups (NFR-04) touch only the data layer.
   - Browser-only access (NFR-11) is the presentation layer.

**Use-case example (UC-07):** `JobAllocationPage.suggestRoster()` → `CrewFormingService.suggestRoster(week)` → reads `Availability`, `LeaveRecord`, `VanAvailability` and `StandbyPreference`, and writes `Crew` and `Standby` → the page shows the Draft roster.

---

## 4. Design pattern (report §3.2): Strategy

**Design problem.** The system ranks Technicians in two places, with two different fairness rules:
- **Crew forming (FR-55):** last week's Workload, then projected hours, then staff ID.
- **Standby activation (FR-56):** fewest activations in 12 months, then zone distance, then staff ID.

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

**How it improves the design:**
- A new fairness rule is a new class. For example, a seniority tie-break would be a `SeniorityRanking`, and the algorithms stay unchanged (open/closed principle).
- Each ranking can be unit-tested on its own with a list of Technicians.
- The contexts depend only on the interface, which keeps the Scheduling Engine's internals loosely coupled.

**Alternatives considered:**
- *Observer* for notifications: it would decouple Roster & Hours from Notification, but the system has a single subscriber (NotificationService), so the benefit is small.
- *Adapter* for CSV files: `CsvRowMapper` is kept in the class diagram as an «interface», but it is not written up as the pattern.
