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

- Use two digits with zero padding. FR, NFR and SD IDs follow the **submitted M1 report** (FR-01–FR-50, NFR-01–NFR-12, SD-01–SD-21); the repo's earlier draft IDs were renumbered to match it on 2026-11-07 (DEC-72; mapping in `requirements.md` §9 and `diagrams/README.md`). From this baseline on, **IDs are never reused or renumbered**; mark a dropped item `Status: Withdrawn` and keep its row. History files (DEC-01 to DEC-71, review notes, archives) keep the draft IDs they were written with.
- Before creating an ID, check the highest existing one. If two people collide, the later commit renumbers.
- Slugs are kebab-case, e.g. `UC-03-reject-job.md`.

## Glossary (canonical terms)

Use these exact terms, capitalised, in requirements, use cases, class names and diagrams. Do not substitute the synonyms in the last column. Definitions follow the submitted M1 report (Table 1.3), the decisions in `decisions.md` and the SRS (`requirements.md` §1.3).

| Term | Meaning | Avoid |
| --- | --- | --- |
| **Staff** | Field employees who receive Assignments: Drivers and Technicians. Managers are not Staff (FR-43) | employee, worker, user |
| **Manager** | Office-based user who records Jobs, forms Crews, allocates and publishes the Weekly Roster, and decides Staff requests. There may be several Manager accounts with the same rights (FR-43, FR-07) | admin, supervisor |
| **IT Administrator** | User who creates accounts, changes roles, deactivates and unlocks accounts, and views the Audit Log (FR-44, FR-45, FR-46, FR-49) | admin, sysadmin |
| **Driver** | Staff member who drives a Van. The only role allowed to drive (FR-26). There are 6 | — |
| **Technician** | Staff member holding a Certification for one or both Brands. A Technician never drives (FR-22, FR-26). There are 11 | engineer, installer |
| **Single-Brand Technician** | A Technician certified for only one Brand: M Electric (5 Technicians) or Dicon (4 Technicians) (FR-22; Brief) | — |
| **Dual-Certified Technician** | A Technician certified for both Brands (2 Technicians). One Dual-Certified Technician can cover a Van's Jobs of both Brands (FR-22, FR-27; Brief) | dual-skilled |
| **Brand** | Aircon brand: `M Electric` or `Dicon` (exact spelling) (FR-01) | make, vendor |
| **Certification** | A Technician's qualification for a Brand, recorded as Brand, certificate number and expiry date. It is valid for a Job when its expiry date is on or after the Job's date (FR-22) | skill, license |
| **Van** | Service vehicle, recorded by number and licence plate. The company currently has six (FR-23) | truck, team |
| **Crew** | One Driver and one or two Technicians assigned to one Van for one working day (FR-26) | team, van team |
| **Van-day** | One Van on one date, together with its Crew and Jobs (FR-29) | — |
| **Job** | One Installation or Servicing task for one Brand at one address, created by the Manager (FR-01) | task, order, ticket |
| **Job Type** | `Installation` or `Servicing` (FR-01) | — |
| **Standard Duration** | The default length of a Job: 1 h per unit for Servicing and 3 h per unit for Installation. The Manager can adjust it (FR-02) | — |
| **Linked Jobs** | Jobs of different Brands at the same address. They must be allocated to the same Van on the same date (FR-03) | — |
| **Assignment** | A Job placed on a Van for a date. Every Crew member of that Van-day holds the Assignment (FR-07, FR-35) | allocation (noun), booking |
| **Unassigned Job** | A Job with status Unassigned. Cancelled Jobs are not counted (FR-05, FR-34) | open job, pending job |
| **Job Allocation** | The Manager's weekly activity of creating Assignments (FR-07) | scheduling, planning page |
| **Planning Week** | A Monday-to-Saturday week. "The" Planning Week is the next unpublished one (FR-07, FR-36) | work week |
| **Weekly Roster** | All Crews and Assignments of one Planning Week. It is Draft until the Manager publishes it, then Published (FR-09) | timetable, schedule |
| **Slot** | Half-day unit: `Morning` or `Afternoon`. Jobs run within 09:00–18:00 and skip lunch (13:00–14:00) (FR-12, FR-08) | shift, timeslot |
| **Availability** | A Staff member's per-Slot setting of Available or Unavailable, entered up to one month in advance. A Slot with no entry is Not submitted and counts as unavailable (FR-12, FR-13) | schedule, free time |
| **Availability Deadline** | 18:00 on the Wednesday 12 days before a Planning Week's Monday. After it, that week's Availability and Job Preference are locked (FR-15) | cut-off, lock |
| **Late Availability Change Request** | A Staff request to set or change Availability for a locked week, with a reason. The Manager approves or rejects it (FR-16) | late request |
| **Job Preference** | A Staff member's advisory weekly preference for area, days, Slot and Job Type. A Job that breaks it raises a warning, not a block (FR-17) | — |
| **Workload** | Hours credited to a Staff member: Planned Hours of Assigned Jobs plus Actual Hours of Completed Jobs, summed per Planning Week and per calendar month (FR-35, FR-36) | load, utilisation |
| **Travel Allowance** | A fixed 0.5 h added to each Job's hours (FR-08, FR-35) | travel time |
| **Planned Hours / Actual Hours** | Planned Hours are a Job's duration plus the Travel Allowance. Actual Hours are the actual end minus the actual start, plus the Travel Allowance (FR-35) | — |
| **Overtime** | Workload strictly above 40 h in a Planning Week (FR-36) | OT |
| **Job Rejection Request** | A Crew member's request to take a Job off their Van, made after a warning to discuss it with the Manager. The Manager approves or refuses it (FR-37, FR-38) | decline, cancel, rejection (alone) |
| **Short notice** | A Job Rejection Request submitted when the Job starts in less than 48 hours (FR-37) | — |
| **Standby** | A Staff member named by the Manager to back up a working day's Jobs. Not in any Crew that day, and counted as 0 h unless placed in a Crew (FR-30) | backup, reserve |
| **Leave** | Annual leave in full working days: 7 per calendar year, with no carry-over (FR-21) | holiday, time off |
| **Leave Request** | A Staff application for Leave. The Manager approves or rejects it (FR-18, FR-19) | leave form |
| **Workshop Servicing** | A Van's maintenance day, generated from a two-monthly rotation. The Van is unavailable that day (FR-24) | maintenance |
| **Needs attention** | A Van-day whose Crew became invalid after a later event, such as approved Leave or an expired Certification (FR-29) | — |
| **Landing Page** | The first page after login, specific to each role (FR-43) | home, dashboard |
| **Notification** | A message to a recipient's Landing Page, with a handled state. Staff Notifications are also sent by email and phone (FR-40, FR-39) | alert, message |
| **Audit Log** | A record of who changed what and when. Only the IT Administrator can view it (FR-49) | history |

The terms and meanings follow the submitted M1 report, Table 1.3; the "Avoid" column is the repo's own. 

When a new term is needed, add it here in the same commit and cite its source.

### Sequence analysis classes (DEC-53)

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

`brief/` holds the source docs (read-only) and `requirements.md` holds the SRS (FR and NFR tables). `elicitation.md` is the brief for the report's elicitation-process chapter. `use-cases/` has one file per UC, `diagrams/` holds the PlantUML source and `elicitation/` holds the stakeholder meeting notes. The remaining files are `traceability.md`, `decisions.md` and `ai-usage-log.md`. Root files transcribed from the submitted M1 report: `Glossary.md`, `AI Usage Declaration.md`, `WBS and Timeline.md`. Review and history files (`M1 Report Gap Analysis.md`, `requirements-review.md`, `phases.md`, `SWE Assignment M1.md`) are kept as records and use draft IDs.

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
