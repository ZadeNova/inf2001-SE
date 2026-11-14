# AGENTS.md: shared context for humans and AI tools

This file applies to every contributor and every AI tool (Claude Code, Codex, etc.). `CLAUDE.md` only imports this file, so **edit this file only** and do not add tool-specific rule files.

## Project

This is the INF2001 Introduction to Software Engineering (SIT) team project for a 6-person team (Team P8-1; members are listed in the submitted M1 report). The client is an aircon retailer that wants a **web-based workload management system** for its aircon service team. The system will let Staff (Drivers and Technicians) see their Assignments and Workload, submit Availability and job preferences, and request Job rejections, which the Manager decides. It will let the Manager see manpower Availability up to 1 month in advance, see Workload at a glance and allocate Jobs weekly. IT Administrators add Staff and Managers. Weekly cycle: Availability is due Wednesday, planning starts Thursday and Assignments are issued Monday.

The source of truth is [brief/project-description.md](brief/project-description.md), which is binding and must not be edited except for the explicit DEC-45 scope redaction already recorded in that file. The **Lecturer clarifications** section at its end overrides the original wording where they conflict. The rules and rubrics are in [brief/](brief/).

For **M1 artefacts** (requirements, use cases, diagrams, glossary, WBS), the source of truth is the **submitted M1 report** (INF2001 P8-1 M1 Report, 9 Oct 2026). The repo follows its IDs and wording; where the repo and the report differ, the report wins (DEC-72). The root files `Glossary.md`, `AI Usage Declaration.md` and `WBS and Timeline.md` are transcribed from it. `SWE Assignment M1.md` is an earlier 7 Oct draft export and is **not** authoritative.

| Milestone | Scope                                                                        | Deadline (report, slides, peer eval) |
| --------- | ---------------------------------------------------------------------------- | ------------------------------------ |
| M1        | Requirements, use cases, OOA (class and sequence diagrams), WBS and timeline | **11:59PM, 9 Oct 2026 (Fri)**        |
| M2        | Final class diagram, component diagram, patterns, testing, wireframe         | **11:59PM, 20 Nov 2026 (Fri)**       |

Late work loses 20% per day, and anything more than 4 days late gets zero. See [brief/rubric-m1.md](brief/rubric-m1.md) and [brief/rubric-m2.md](brief/rubric-m2.md).

## Rules of engagement for AI

1. **AI is used to critique, not to author facts.** Appropriate uses: finding inconsistencies, checking traceability, preparing elicitation questions, analysing stakeholder notes we recorded, reviewing UML notation and tidying wording.

2. **Everything traces to a source.** Every FR, NFR, UC and CL, and every diagram element, must cite at least one of these:
   - `Brief R<n>` (initial requirement n), or `Brief §<section> ¶<n>` (narrative paragraph)
   - `MTG-<nn>` (a meeting note in `elicitation/`)
   - `INT-MGR|DCT|DRV|ITA [<question>]` (an interview transcript in `elicitation/interviews/`; format in `requirements.md` §1.4)
   - `DEC-<nn>` (a logged team decision in `decisions.md`)
   - `M1 Report §<n>` (the submitted M1 report, 9 Oct 2026)
   - `M2-Brief §<n>` (the team's M2 Design Update Brief in `m2/design-update-brief.md`; cite it through the DEC entry that records it where one exists)

   Items without a source are flagged, not merged.

3. **Ambiguity goes to `decisions.md`.** When the brief is unclear or contradictory, add or reference an open DEC entry and ask. Do not silently choose an interpretation, even a "reasonable" one.
4. **Log adopted AI output** in [ai-usage-log.md](ai-usage-log.md): the date, the member, the tool, what it was used for and what we changed. This feeds the mandatory AI-usage section of each milestone report.
5. **Keep the repo private.** The plagiarism declaration forbids sharing materials. Do not paste repo content into public tools or render services (see `diagrams/README.md`).
6. **Quote, don't paraphrase,** when citing the brief in analysis. Paraphrases drift.

## ID conventions

| Prefix           | Meaning                           | Example         | Lives in                            |
| ---------------- | --------------------------------- | --------------- | ----------------------------------- |
| `FR-nn`          | Functional requirement            | `FR-01`         | `requirements.md`                   |
| `NFR-nn`         | Non-functional requirement        | `NFR-01`        | `requirements.md`                   |
| `UC-nn`          | Use case                          | `UC-01`         | `use-cases/UC-01-<slug>.md`         |
| `CL-<ClassName>` | Class (PascalCase, glossary term) | `CL-Assignment` | class diagram and `traceability.md` |
| `SD-nn`          | Sequence diagram                  | `SD-01`         | `diagrams/SD-01-<slug>.puml`        |
| `AD-nn`          | Activity diagram                  | `AD-01`         | `diagrams/AD-01-<slug>.puml`        |
| `DEC-nn`         | Decision or open question         | `DEC-01`        | `decisions.md`                      |
| `MTG-nn`         | Stakeholder meeting               | `MTG-01`        | `elicitation/MTG-01-<date>.md`      |
| `W-nn`           | Wireframe screen (M2)             | `W-06`          | `m2/wireframes.md`                  |
| `A<n>`           | SRS assumption (M2)               | `A1`            | `requirements.md` §1.5              |
| `BB-nn` / `WB-nn`| Black-box / white-box test case   | `BB-01`         | `m2/testing.md`                     |

- Use two digits with zero padding. FR, NFR and SD IDs follow the **submitted M1 report** (FR-01–FR-50, NFR-01–NFR-12, SD-01–SD-21; M2 adds FR-51 onwards and NFR-13 onwards); the repo's earlier draft IDs were renumbered to match it on 2026-11-07 (DEC-72; mapping in `requirements.md` §9 and `diagrams/README.md`). From this baseline on, **IDs are never reused or renumbered**; mark a dropped item `Status: Withdrawn` and keep its row. History files (DEC-01 to DEC-71, review notes, archives) keep the draft IDs they were written with.
- Before creating an ID, check the highest existing one. If two people collide, the later commit renumbers.
- Slugs are kebab-case, e.g. `UC-03-reject-job.md`.

## Glossary (canonical terms)

Use these exact terms, capitalised, in requirements, use cases, class names and diagrams. Do not substitute the synonyms in the last column. Definitions follow the submitted M1 report (Table 1.3), the decisions in `decisions.md` and the SRS (`requirements.md` §1.3).

| Term | Meaning | Avoid |
| --- | --- | --- |
| **Staff** | Field employees who receive Assignments: Drivers and Technicians. Managers are not Staff (DEC-18) | employee, worker, user |
| **Manager** | Office-based user who uploads CSV files, records Jobs, reviews the suggested Weekly Roster, allocates and publishes it, updates the roster and hours, and decides Job Rejection Requests. May be several accounts with identical rights (DEC-18, DEC-73) | admin, supervisor |
| **IT Administrator** | Manages accounts, roles, lockouts, Technician profiles (home zone, Certifications) and views the Audit Log (Brief R11, DEC-17, DEC-75) | admin, sysadmin |
| **Driver** | Staff member who drives a Van; the only role allowed to drive. There are 6. Outside the scheduling logic: one per Crew, assumed always enough (DEC-82) | — |
| **Technician** | Staff member certified for one or both Brands; never drives. There are 11: 2 dual, 5 M Electric only, 4 Dicon only | engineer, installer |
| **Single-Brand Technician** | A Technician certified for only one Brand: M Electric (5 Technicians) or Dicon (4 Technicians) (FR-22; Brief) | — |
| **Dual-Certified Technician** | A Technician with valid Certifications for both Brands (2 Technicians). One can cover a Crew's Jobs of both Brands (FR-22, FR-27; M2-Brief §8) | dual-skilled, Dual-Certified |
| **Brand** | Aircon brand: `M Electric` or `Dicon` (exact spelling) | make, vendor |
| **Certification** | A Technician's qualification for a Brand (covers Installation and Servicing): Brand and expiry date only (DEC-75) | skill, license |
| **Van** | Service vehicle. Not stored: only the number available per date, from the van CSV; Crews are numbered Van 1…n per day (DEC-85) | truck, team |
| **Van Availability** | The number of Vans available on a date, imported from the van vendor CSV (DEC-74, DEC-85) | fleet |
| **Leave Record** | A read-only record that a Staff member is on Leave, Emergency Leave or MC on a date, imported from the HR CSV (DEC-74) | leave request |
| **CSV Import** | One Manager upload validated as a whole: HR is a confirmed complete snapshot for one selected Planning Week, including valid header-only no-Leave coverage; van is per-date counts (DEC-74, DEC-108) | sync |
| **Zone** | North, East, South, West or Central. Job zone comes from postal code; the Manager assigns one or more coverage Zones per Crew (DEC-77, DEC-97) | area, region |
| **Home Zone** | A Technician's base Zone, used to order Standby Staff (DEC-77) | base |
| **Crew** | Initial Driver plus 1–2 Technicians on one Van/date. Coverage may span Zones; per-Job Staff attribution preserves operational replacements (DEC-97) | team, van team |
| **Job** | One Installation or Servicing task for one Brand at one address, created by the Manager. Status `Unassigned` or `Assigned`; a cancelled Job is deleted (DEC-11, DEC-76) | task, order, ticket |
| **Job Type** | `Installation` or `Servicing` (FR-01) | — |
| **Standard Duration** | The default length of a Job: 1 h per unit for Servicing and 3 h per unit for Installation. The Manager can adjust it (FR-02) | — |
| **Van-day** | One Van number on one date, together with its Crew and Jobs (FR-26, DEC-85) | — |
| **Assignment** | A timed Job/date with attributed Staff: effective Crew members, or exactly one certified Standby Technician on a direct duty without a Van (DEC-97) | allocation (noun), booking |
| **Unassigned Job** | A Job with status Unassigned (FR-05, FR-34) | open job, pending job |
| **Job Allocation** | The Manager's weekly activity or page for reviewing the Suggested Roster and creating Assignments (R3, R4) | scheduling, planning page |
| **Suggested Roster** | The Draft Crews and Standby Staff the crew-forming algorithm proposes for a Planning Week; the Manager edits and publishes it (DEC-80) | auto-roster |
| **Planning Week** | A Monday–Saturday week; "the" Planning Week is the next unpublished one (DEC-04, DEC-16) | work week |
| **Weekly Roster** | All Crews, Standby Staff and Assignments of one Planning Week; `Draft` until published, then `Published` (DEC-16) | timetable, schedule |
| **Slot** | Half-day unit used only for a Job's preferred time: `Morning` 09:00–13:00 or `Afternoon` 14:00–18:00 (DEC-12, DEC-83) | shift, timeslot |
| **Availability** | Per-working-day `Available`/`Unavailable` set by Staff, up to **1 month in advance** (DEC-01, DEC-30, DEC-83); no entry = Not submitted = unavailable (DEC-03) | schedule, free time |
| **Availability Deadline** | 18:00 on the Wednesday 12 days before a Planning Week; that week's Availability and Standby Preferences then lock (DEC-02, DEC-79) | cut-off, lock |
| **Standby Preference** | One provisional requested day/Brand slot per Technician/week. Confirm after locked inputs and CSV checks permit >=3 Crews plus Full Standby cover; confirmed initial placement is binding, but activation/Leave still apply (DEC-98) | job preference |
| **Standby** | An initially reserved Technician, retained as one record per date after direct/replacement activation. Total Credited Hours = max(4, Active Hours); activated dates count once (DEC-96/97) | backup, reserve |
| **Standby Activation** | A Standby taking a direct Job or joining a Crew from a specified Job; count once per Technician/date regardless of repeated duties (DEC-96/97) | call-up |
| **Hours Edit** | Manager correction to Active Hours for a date, with reason and old/new values. Total Credited Hours remain derived with the Standby minimum (DEC-96) | timesheet |
| **Workload** | Total Credited Hours summed over the week/month, used for the 40 h target/highlight; distinct from Active Hours used for rotation (DEC-96) | load, utilisation |
| **Travel Allowance** | Fixed 0.5 h added to each Job's hours (DEC-31) | travel time |
| **Planned Hours** | A Job's duration + Travel Allowance (DEC-31, DEC-78) | — |
| **Overtime** | Workload strictly above 40 h in a Planning Week (DEC-04, DEC-86) | OT |
| **Job Rejection Request** | An attributed Staff member's request to unassign a Crew or direct Job; the Manager decides (DEC-42, DEC-97) | decline, cancel, rejection (alone) |
| **Audit Log** | Who did what, when and why, for account changes, CSV uploads, roster overrides and Hours Edits; kept 12 months (DEC-89) | history |
| **Notification** | A message to a recipient's Landing Page, with a handled state; Staff Notifications are also sent by email and SMS (FR-39, FR-40, DEC-88) | alert, message |
| **Landing Page** | The first page after login, specific to each role (FR-43) | home, dashboard |

The M1 terms and meanings follow the submitted M1 report (Table 1.3); M2 changes follow DEC-73 to DEC-98. Retired terms (do not use in M2 artefacts): Leave Request, Late Availability Change Request, Job Preference, Workshop Servicing, Actual Hours, Linked Jobs, Short notice, Needs attention (DEC-73, DEC-79, DEC-83, DEC-90).

When a new term is needed, add it here in the same commit and cite its source.

**Additional M2 terms (DEC-96/97):**

| Term | Meaning |
|---|---|
| **OfflineAssignmentController** | Browser-side Controller owning the approved encrypted today-only Assignment copy; LandingPage renders/forwards input (DEC-109) |
| **Active Hours** | Attributed Planned Hours including direct/replacement duties, corrected by any Hours Edit; unused Standby credit is excluded |
| **Total Credited Hours** | Active Hours on ordinary days; max(4, Active Hours) on a rostered Standby date, with no unused credit for full-day Leave |
| **Replacement** | Recorded outgoing/incoming Technician, Crew, starting Job/effective time, Manager, reason and timestamp; earlier Job Staff remain unchanged |

### Sequence analysis classes (DEC-53)

> M1 analysis view (report §4.2). The M2 final classes, including the new controllers, boundaries and «interface» classes, are in [diagrams/CD-final.puml](diagrams/CD-final.puml) (DEC-93).

These boundary and control names identify analysis responsibilities used by the active sequence diagrams. They do not add stakeholder requirements or prescribe implementation services.

| Class name | Responsibility and source |
|---|---|
| **LoginPage** | Login and password-reset interaction (UC-01, UC-02). Source: DEC-53; supplied sequence review section 3. |
| **LandingPage** | Role-specific Landing Page interaction (UC-01, UC-10, UC-13). Source: DEC-53; supplied sequence review section 3. |
| **AccountAdminPage** | Account creation and access-management interaction (UC-03, UC-04). Source: DEC-53; supplied sequence review section 3. |
| **JobPage** | Manager Job-management interaction (UC-05). Source: DEC-53; supplied sequence review section 3. |
| **VanPage** | Van and Workshop Servicing interaction (UC-06). Source: DEC-53; supplied sequence review section 3. |
| **JobAllocationPage** | Weekly planning and Staff comparison interaction (UC-07, UC-08). Source: DEC-53; supplied sequence review section 3. |
| **RequestReviewPage** | Manager Staff-request decision interaction (UC-09). Source: DEC-53; supplied sequence review section 3. |
| **AvailabilityPage** | Staff Availability and Job Preference interaction (UC-11). Source: DEC-53; supplied sequence review section 3. |
| **RequestPage** | Staff request-submission interaction (UC-12). Source: DEC-53; supplied sequence review section 3. |
| **JobCompletionPage** | Technician Job-completion interaction (UC-14). Source: DEC-53; supplied sequence review section 3. |
| **AuthController** | Coordinates login, reset and session flows (UC-01, UC-02). Source: DEC-53; supplied sequence review section 3. |
| **AccountController** | Coordinates account creation and access changes (UC-03, UC-04). Source: DEC-53; supplied sequence review section 3. |
| **JobController** | Coordinates Job create, link, edit and cancel flows (UC-05). Source: DEC-53; supplied sequence review section 3. |
| **VanController** | Coordinates Van and Workshop Servicing flows (UC-06). Source: DEC-53; supplied sequence review section 3. |
| **RosterController** | Coordinates Weekly Roster, Staff comparison and later Crew-event handling (UC-07, UC-08; SD-21). Source: DEC-53; supplied sequence review section 3. |
| **RuleValidator** | Checks shared blocking rules and warnings (FR-32, FR-33). Source: DEC-53; supplied sequence review section 3. |
| **RequestController** | Coordinates Staff request submission and Manager decisions (UC-09, UC-12). Source: DEC-53; supplied sequence review section 3. |
| **DashboardController** | Coordinates Manager and Staff Landing Page data (UC-10, UC-13). Source: DEC-53; supplied sequence review section 3. |
| **AvailabilityController** | Coordinates direct Availability and Job Preference submissions (UC-11). Source: DEC-53; supplied sequence review section 3. |
| **CompletionController** | Coordinates Technician completion validation and saving (UC-14). Source: DEC-53; supplied sequence review section 3. |
| **NotificationService** | Coordinates Landing Page, email and SMS notifications (UC-15). Source: DEC-53; supplied sequence review section 3. |

External sequence actors: **Email Service** delivers email (UC-01/02/03/15; DEC-49/56). **SMS Gateway** delivers the SMS phone channel (UC-15; DEC-48/56). These realise the existing Email/Phone delivery actor and are not domain classes. **Clock** is the external system-event actor for Job start (SD-12) and daily Certification-expiry checks (SD-21); it is a secondary actor of UC-09 for lapse, and of FR-22/29 system behaviour for expiry; it is not a domain class or a separate use case (DEC-59, DEC-68).

## Diagram rules

- Diagrams are PlantUML source in [diagrams/](diagrams/), **one diagram per `.puml` file**, named `<ID>-<slug>.puml`. Rendered images are git-ignored.
- Use correct UML 2.5 notation for the diagram type: actors and `<<include>>`/`<<extend>>` in use-case diagrams, initial/final nodes, decisions and swimlanes in activity diagrams, and lifelines, activation bars and return messages in sequence diagrams.
- Class, actor, lifeline and swimlane names must match the glossary and `CL-` IDs exactly. Put the diagram's ID in its `title`.
- Every diagram is listed in `traceability.md`. Full conventions are in [diagrams/README.md](diagrams/README.md).

## Repo map

`brief/` holds the source docs (read-only) and `requirements.md` holds the SRS (FR and NFR tables). `m2/` holds the M2 Design Update Brief and the M2 design, testing and wireframe working documents. `elicitation.md` is the brief for the report's elicitation-process chapter. `use-cases/` has one file per UC, `diagrams/` holds the PlantUML source and `elicitation/` holds the stakeholder meeting notes. The remaining files are `traceability.md`, `decisions.md` and `ai-usage-log.md`. Root files transcribed from the submitted M1 report: `Glossary.md`, `AI Usage Declaration.md`, `WBS and Timeline.md`. Review and history files (`M1 Report Gap Analysis.md`, `requirements-review.md`, `phases.md`, `SWE Assignment M1.md`) are kept as records and use draft IDs.

## Elicitation material

- Interview transcripts are in `elicitation/interviews/` (manager, dct, driver, ita). The team's brief review is in `elicitation/document-analysis.md`.
- **Read [elicitation/README.md](elicitation/README.md) first.** Open individual files only when asked or when verifying a source.
- Keep the two naming schemes apart: `F-1`..`F-30` are the document-analysis findings, and `AK-01`..`AK-14` are the Answer-key rows at the end of the manager and DCT transcripts. The answer-key rows are labelled `F-01`..`F-14` in those files, but they are a different set. The Answer keys are team summaries, not stakeholder statements.

## Collaboration rules

- **Never push to `main` directly.** Work on a branch (`<name>/<topic>`) and open a PR. At least one other member reviews it.
- **One owner per file.** Only the owner edits a file. Others propose changes through a PR comment or by asking the owner. Append-only logs (`decisions.md`, `ai-usage-log.md`) are open to everyone, but you only add rows and never edit other people's rows.
- **Do not rewrite, reformat or delete others' work without asking**, and that includes AI tools. AI tools must not run `git push`, force-push, rebase shared branches or commit on someone else's behalf.
- Commit small, with messages that say what changed and why.

### File ownership

Owners follow the accountable owners in the submitted M1 report's WBS (Table 5.1). Confirm or change them at the next team meeting.

| File / folder                    | Owner |
| -------------------------------- | ----- |
| `requirements.md` | Chee Long (WBS 1.2, 1.3) |
| `use-cases/` | Erfan (WBS 2.1) |
| `diagrams/` (use case, activity) | Erfan (use case, WBS 2.1.3); Damien (activity, WBS 2.2) |
| `diagrams/` (class, sequence) | Jeremy (class, WBS 2.3, 2.5); Jun Keat (sequence, WBS 2.4; design pattern, WBS 2.6) |
| `traceability.md` | Chee Long (WBS 1.3.2) |
| `elicitation/` | Chee Long (WBS 1.1) |
| `decisions.md` (curation) | — (not assigned in the WBS) |
| WBS / timeline | Brandon (WBS 6.1) |
| `AGENTS.md` | — (not assigned in the WBS) |
