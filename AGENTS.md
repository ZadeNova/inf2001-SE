# AGENTS.md: shared context for humans and AI tools

This file applies to every contributor and every AI tool (Claude Code, Codex, etc.). `CLAUDE.md` only imports this file, so **edit this file only** and do not add tool-specific rule files.

## Project

This is the INF2001 Introduction to Software Engineering (SIT) team project for a 5-person team. The client is an aircon retailer that wants a **web-based workload management system** for its aircon service team. The system will let Staff (Drivers and Technicians) see their Assignments and Workload, submit Availability and job preferences, and reject Jobs. It will let the Manager see manpower Availability up to 1 month in advance, see Workload at a glance and allocate Jobs weekly. IT Administrators add Staff and Managers. Weekly cycle: Availability is due Wednesday, planning starts Thursday and Assignments are issued Monday.

The source of truth is [brief/project-description.md](brief/project-description.md), which is binding and must not be edited. The **Lecturer clarifications** section at its end overrides the original wording where they conflict. The rules and rubrics are in [brief/](brief/).

| Milestone | Scope | Deadline (report, slides, peer eval) |
|---|---|---|
| M1 | Requirements, use cases, OOA (class and sequence diagrams), WBS and timeline | **11:59PM, 9 Oct 2026 (Fri)** |
| M2 | Final class diagram, component diagram, patterns, testing, wireframe | **11:59PM, 20 Nov 2026 (Fri)** |

Late work loses 20% per day, and anything more than 4 days late gets zero. See [brief/rubric-m1.md](brief/rubric-m1.md) and [brief/rubric-m2.md](brief/rubric-m2.md).

## Rules of engagement for AI

1. **AI is used to critique, not to author facts.** Appropriate uses: finding inconsistencies, checking traceability, preparing elicitation questions, analysing stakeholder notes we recorded, reviewing UML notation and tidying wording.
2. **AI must not invent stakeholder input, requirements, use cases or decisions.** If something is missing, say so and propose a question for a stakeholder or the lecturer. Never fill the gap with a plausible guess.
3. **Everything traces to a source.** Every FR, NFR, UC and CL, and every diagram element, must cite at least one of these:
   - `Brief R<n>` (initial requirement n), or `Brief §<section> ¶<n>` (narrative paragraph)
   - `MTG-<nn>` (a meeting note in `elicitation/`)
   - `DEC-<nn>` (a logged team decision in `decisions.md`)

   Items without a source are flagged, not merged.
4. **Ambiguity goes to `decisions.md`.** When the brief is unclear or contradictory, add or reference an open DEC entry and ask. Do not silently choose an interpretation, even a "reasonable" one.
5. **Log adopted AI output** in [ai-usage-log.md](ai-usage-log.md): the date, the member, the tool, what it was used for and what we changed. This feeds the mandatory AI-usage section of each milestone report.
6. **Keep the repo private.** The plagiarism declaration forbids sharing materials. Do not paste repo content into public tools or render services (see `diagrams/README.md`).
7. **Quote, don't paraphrase,** when citing the brief in analysis. Paraphrases drift.

## ID conventions

| Prefix | Meaning | Example | Lives in |
|---|---|---|---|
| `FR-nn` | Functional requirement | `FR-01` | `requirements.md` |
| `NFR-nn` | Non-functional requirement | `NFR-01` | `requirements.md` |
| `UC-nn` | Use case | `UC-01` | `use-cases/UC-01-<slug>.md` |
| `CL-<ClassName>` | Class (PascalCase, glossary term) | `CL-Assignment` | class diagram and `traceability.md` |
| `SD-nn` | Sequence diagram | `SD-01` | `diagrams/SD-01-<slug>.puml` |
| `AD-nn` | Activity diagram | `AD-01` | `diagrams/AD-01-<slug>.puml` |
| `DEC-nn` | Decision or open question | `DEC-01` | `decisions.md` |
| `MTG-nn` | Stakeholder meeting | `MTG-01` | `elicitation/MTG-01-<date>.md` |

- Use two digits with zero padding. **IDs are never reused or renumbered.** Mark a dropped item `Status: Withdrawn` and keep its row.
- Before creating an ID, check the highest existing one. If two people collide, the later commit renumbers.
- Slugs are kebab-case, e.g. `UC-03-reject-job.md`.

## Glossary (canonical terms)

Use these exact terms, capitalised, in requirements, use cases, class names and diagrams. Do not substitute the synonyms in the last column. Definitions marked *(open: DEC-nn)* depend on an unresolved decision.

| Term | Meaning (from the brief) | Avoid |
|---|---|---|
| **Staff** | Field employees who receive Assignments, i.e. Drivers and Technicians. Whether Managers count as Staff is *(open: DEC-18)* | employee, worker, user |
| **Manager** | The administrative staff member who views manpower and allocates Jobs ("administrative staff (usually the manager)") | admin, supervisor |
| **IT Administrator** | Company IT staff who add new Staff and Managers (R11). Their scope is *(open: DEC-17)* | admin, sysadmin |
| **Driver** | Staff member who drives a Van. There are 6 | — |
| **Technician** | Staff member certified for one or both Brands. There are 11: 2 dual, 5 M Electric only, 4 Dicon only | engineer, installer |
| **Brand** | Aircon brand: `M Electric` or `Dicon` (exact spelling) | make, vendor |
| **Certification** | A Technician's qualification to install or service a Brand | skill, license |
| **Van** | Service vehicle whose crew is 1 Driver plus 1–2 Technicians (2–3 people). There are 6. Composition rules are *(open: DEC-09)* | truck, team |
| **Job** | One aircon installation or servicing task. Its attributes are *(open: DEC-11)* | task, order, ticket |
| **Job Type** | `Installation` or `Servicing` | — |
| **Assignment** | The link between a Job and the Staff (or Van) doing it *(open: DEC-10)* | allocation (noun), booking |
| **Job Allocation** | The Manager's weekly activity or page for creating Assignments (R3, R4) | scheduling, planning page |
| **Availability** | Staff-declared dates and times they can work, entered and viewable **up to 1 month in advance** (DEC-01, lecturer-confirmed). The exact window calculation is *(open: DEC-30)* | schedule, free time |
| **Availability Deadline** | Wednesday cut-off for the following week's planning | cut-off |
| **Job Preference** | Staff's stated preference for the week (R9). Its content is *(open: DEC-07)* | — |
| **Workload** | Hours of Jobs assigned to a Staff member over a period *(open: DEC-04)* | load, utilisation |
| **Job Rejection** | Staff declining an Assignment after a warning (R10) | decline, cancel |
| **Leave** | Annual leave, 7 days per Staff member. Handling is *(open: DEC-13)* | holiday, time off |
| **Workshop Servicing** | Van maintenance, every two months | maintenance |
| **Weekly Roster** | The full set of Assignments for one week | timetable |
| **Landing Page** | First page after login, which is role-specific (R2, R6, R7) | home, dashboard |

When a new term is needed, add it here in the same commit and cite its source.

## Diagram rules

- Diagrams are PlantUML source in [diagrams/](diagrams/), **one diagram per `.puml` file**, named `<ID>-<slug>.puml`. Rendered images are git-ignored.
- Use correct UML 2.5 notation for the diagram type: actors and `<<include>>`/`<<extend>>` in use-case diagrams, initial/final nodes, decisions and swimlanes in activity diagrams, and lifelines, activation bars and return messages in sequence diagrams.
- Class, actor, lifeline and swimlane names must match the glossary and `CL-` IDs exactly. Put the diagram's ID in its `title`.
- Every diagram is listed in `traceability.md`. Full conventions are in [diagrams/README.md](diagrams/README.md).

## Repo map

`brief/` holds the source docs (read-only) and `requirements.md` holds the FR and NFR tables. `use-cases/` has one file per UC, `diagrams/` holds the PlantUML source and `elicitation/` holds the stakeholder meeting notes. The remaining files are `traceability.md`, `decisions.md` and `ai-usage-log.md`.

## Collaboration rules

- **Never push to `main` directly.** Work on a branch (`<name>/<topic>`) and open a PR. At least one other member reviews it.
- **One owner per file.** Only the owner edits a file. Others propose changes through a PR comment or by asking the owner. Append-only logs (`decisions.md`, `ai-usage-log.md`) are open to everyone, but you only add rows and never edit other people's rows.
- **Do not rewrite, reformat or delete others' work without asking**, and that includes AI tools. AI tools must not run `git push`, force-push, rebase shared branches or commit on someone else's behalf.
- Commit small, with messages that say what changed and why.

### File ownership (fill in)

| File / folder | Owner |
|---|---|
| `requirements.md` | |
| `use-cases/` | |
| `diagrams/` (use case, activity) | |
| `diagrams/` (class, sequence) | |
| `traceability.md` | |
| `elicitation/` | |
| `decisions.md` (curation) | |
| WBS / timeline | |
| `AGENTS.md` | |
