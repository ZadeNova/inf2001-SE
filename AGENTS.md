# AGENTS.md: shared context for humans and AI tools

This file applies to every contributor and every AI tool (Claude Code, Codex, etc.). `CLAUDE.md` only imports this file, so **edit this file only** and do not add tool-specific rule files.

## Project

This is the INF2001 Introduction to Software Engineering (SIT) team project for a 5-person team. The client is an aircon retailer that wants a **web-based workload management system** for its aircon service team. The system will let Staff (Drivers and Technicians) see their Assignments and Workload, submit Availability and job preferences, and request Job rejections, which the Manager decides. It will let the Manager see manpower Availability up to 1 month in advance, see Workload at a glance and allocate Jobs weekly. IT Administrators add Staff and Managers. Weekly cycle: Availability is due Wednesday, planning starts Thursday and Assignments are issued Monday.

The source of truth is [brief/project-description.md](brief/project-description.md), which is binding and must not be edited. The **Lecturer clarifications** section at its end overrides the original wording where they conflict. The rules and rubrics are in [brief/](brief/).

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

- Use two digits with zero padding. **IDs are never reused or renumbered.** Mark a dropped item `Status: Withdrawn` and keep its row.
- Before creating an ID, check the highest existing one. If two people collide, the later commit renumbers.
- Slugs are kebab-case, e.g. `UC-03-reject-job.md`.

## Glossary (canonical terms)

Use these exact terms, capitalised, in requirements, use cases, class names and diagrams. Do not substitute the synonyms in the last column. Definitions follow the decisions in `decisions.md` and the SRS (`requirements.md` §1.3).

| Term                                 | Meaning                                                                                                                                                                  | Avoid                              |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| **Staff**                            | Field employees who receive Assignments: Drivers and Technicians. Managers are not Staff (DEC-18)                                                                        | employee, worker, user             |
| **Manager**                          | Office-based user who records Jobs, forms Crews, allocates and publishes the Weekly Roster, and decides requests. May be several accounts with identical rights (DEC-18) | admin, supervisor                  |
| **IT Administrator**                 | Manages accounts, roles, lockouts, public holidays and the audit log (Brief R11, DEC-17)                                                                                 | admin, sysadmin                    |
| **Driver**                           | Staff member who drives a Van; the only role allowed to drive. There are 6                                                                                               | —                                  |
| **Technician**                       | Staff member certified for one or both Brands; never drives. There are 11: 2 dual, 5 M Electric only, 4 Dicon only                                                       | engineer, installer                |
| **Brand**                            | Aircon brand: `M Electric` or `Dicon` (exact spelling)                                                                                                                   | make, vendor                       |
| **Certification**                    | A Technician's qualification for a Brand (covers Installation and Servicing): Brand, number, expiry (DEC-35)                                                             | skill, license                     |
| **Van**                              | Service vehicle (number, licence plate). There are currently 6                                                                                                           | truck, team                        |
| **Crew**                             | The Driver plus 1–2 Technicians assigned to one Van for one working day (DEC-09)                                                                                         | team, van team                     |
| **Job**                              | One Installation or Servicing task for one Brand at one address, created by the Manager (DEC-11)                                                                         | task, order, ticket                |
| **Job Type**                         | `Installation` or `Servicing`                                                                                                                                            | —                                  |
| **Linked Jobs**                      | Jobs of different Brands at the same address; must go on the same Van and date (DEC-11)                                                                                  | —                                  |
| **Assignment**                       | A Job placed on a Van on a date; every Crew member of that Van-day holds the Assignment (DEC-10, DEC-39)                                                                 | allocation (noun), booking         |
| **Unassigned Job**                   | A Job with status Unassigned; excludes Cancelled Jobs (FR-38, FR-46)                                                                                                     | open job, pending job              |
| **Job Allocation**                   | The Manager's weekly activity or page for creating Assignments (R3, R4)                                                                                                  | scheduling, planning page          |
| **Planning Week**                    | A Monday–Saturday week; "the" Planning Week is the next unpublished one (DEC-04, DEC-16)                                                                                 | work week                          |
| **Weekly Roster**                    | All Crews and Assignments of one Planning Week; `Draft` until published, then `Published` (DEC-16)                                                                       | timetable, schedule                |
| **Slot**                             | Half-day unit: `Morning` 09:00–13:00 or `Afternoon` 14:00–18:00 (DEC-03, DEC-12)                                                                                         | shift, timeslot                    |
| **Availability**                     | Per-Slot `Available`/`Unavailable` set by Staff, up to **1 month in advance** (DEC-01, DEC-30); no entry = Not submitted = unavailable (DEC-03)                          | schedule, free time                |
| **Availability Deadline**            | 18:00 on the Wednesday 12 days before a Planning Week; that week's Availability and Job Preference then lock (DEC-02)                                                    | cut-off, lock                      |
| **Late Availability Change Request** | Staff request to set or change Availability for a locked week; Manager decides (DEC-02)                                                                                  | late request                       |
| **Job Preference**                   | Weekly advisory preference: area, days, Slot, Job Type (R9, DEC-07)                                                                                                      | —                                  |
| **Workload**                         | Hours credited to a Staff member in a Planning Week or calendar month: Planned Hours of Assigned Jobs plus Actual Hours of Completed Jobs (DEC-04, DEC-39, DEC-40)       | load, utilisation                  |
| **Travel Allowance**                 | Fixed 0.5 h added to each Job's hours (DEC-31)                                                                                                                           | travel time                        |
| **Planned Hours / Actual Hours**     | Duration + Travel Allowance / (actual end − start) + Travel Allowance (DEC-40)                                                                                           | —                                  |
| **Overtime**                         | Workload strictly above 40 h in a Planning Week (DEC-04)                                                                                                                 | OT                                 |
| **Job Rejection Request**            | A Crew member's request to take a Job off their Van, after a warning; the Manager approves or refuses it. Within 48 h it is marked Short notice (R10, DEC-42)            | decline, cancel, rejection (alone) |
| **Standby**                          | Staff member named by the Manager to back up a working day's Jobs; not in any Crew that day; 0 h unless placed into a Crew (DEC-43)                                      | backup, reserve                    |
| **Leave**                            | Annual leave: full working days, 7 per calendar year, no carry-over (DEC-13)                                                                                             | holiday, time off                  |
| **Leave Request**                    | Staff application for Leave; Manager approves or rejects (DEC-13)                                                                                                        | leave form                         |
| **Workshop Servicing**               | Van maintenance day, generated from the two-monthly rotation (DEC-14)                                                                                                    | maintenance                        |
| **Needs attention**                  | A Van-day whose Crew became invalid after a later event (DEC-19, FR-70)                                                                                                  | —                                  |
| **Landing Page**                     | First page after login, role-specific (R2, R6, R7)                                                                                                                       | home, dashboard                    |

When a new term is needed, add it here in the same commit and cite its source.

## Diagram rules

- Diagrams are PlantUML source in [diagrams/](diagrams/), **one diagram per `.puml` file**, named `<ID>-<slug>.puml`. Rendered images are git-ignored.
- Use correct UML 2.5 notation for the diagram type: actors and `<<include>>`/`<<extend>>` in use-case diagrams, initial/final nodes, decisions and swimlanes in activity diagrams, and lifelines, activation bars and return messages in sequence diagrams.
- Class, actor, lifeline and swimlane names must match the glossary and `CL-` IDs exactly. Put the diagram's ID in its `title`.
- Every diagram is listed in `traceability.md`. Full conventions are in [diagrams/README.md](diagrams/README.md).

## Repo map

`brief/` holds the source docs (read-only) and `requirements.md` holds the SRS (FR and NFR tables). `elicitation.md` is the brief for the report's elicitation-process chapter. `use-cases/` has one file per UC, `diagrams/` holds the PlantUML source and `elicitation/` holds the stakeholder meeting notes. The remaining files are `traceability.md`, `decisions.md` and `ai-usage-log.md`.

## Elicitation material

- Interview transcripts are in `elicitation/interviews/` (manager, dct, driver, ita). The team's brief review is in `elicitation/document-analysis.md`.
- **Read [elicitation/README.md](elicitation/README.md) first.** Open individual files only when asked or when verifying a source.
- Keep the two naming schemes apart: `F-1`..`F-30` are the document-analysis findings, and `AK-01`..`AK-14` are the Answer-key rows at the end of the manager and DCT transcripts. The answer-key rows are labelled `F-01`..`F-14` in those files, but they are a different set. The Answer keys are team summaries, not stakeholder statements.

## Collaboration rules

- **Never push to `main` directly.** Work on a branch (`<name>/<topic>`) and open a PR. At least one other member reviews it.
- **One owner per file.** Only the owner edits a file. Others propose changes through a PR comment or by asking the owner. Append-only logs (`decisions.md`, `ai-usage-log.md`) are open to everyone, but you only add rows and never edit other people's rows.
- **Do not rewrite, reformat or delete others' work without asking**, and that includes AI tools. AI tools must not run `git push`, force-push, rebase shared branches or commit on someone else's behalf.
- Commit small, with messages that say what changed and why.

### File ownership (fill in)

| File / folder                    | Owner |
| -------------------------------- | ----- |
| `requirements.md`                |       |
| `use-cases/`                     |       |
| `diagrams/` (use case, activity) |       |
| `diagrams/` (class, sequence)    |       |
| `traceability.md`                |       |
| `elicitation/`                   |       |
| `decisions.md` (curation)        |       |
| WBS / timeline                   |       |
| `AGENTS.md`                      |       |
