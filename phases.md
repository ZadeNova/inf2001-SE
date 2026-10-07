# M1 phases: start to report submission

> **Status:** v1.0, 2026-10-01. Deadline: **11:59PM Fri 9 Oct 2026** (report, slides, peer evaluation). Aim to submit on **8 Oct**, with 9 Oct as buffer. Late work loses 20% per day.
> The presentation date is unconfirmed (DEC-27), probably the week of 5 Oct, so slides and diagrams must be ready by about 7 Oct.
> Tick boxes as work completes. Owners are blank until the team fills the ownership table in [AGENTS.md](AGENTS.md).

Phases 1 to 3 are done. Phases 4 to 7 can run in parallel once the use-case list is frozen. Phase 8 onwards is sequential.

## Overview

| # | Phase | Report chapter | Rubric | Status | Target date | Owner |
|---|---|---|---|---|---|---|
| 0 | Repo, brief and rules set up | n/a | n/a | Done | Sep | |
| 1 | Elicitation: interviews and document analysis stored | §2.1 | RE 4% | Partly done | 5 Oct | |
| 2 | SRS v3.0 | §2.2 | RE 4% | Done | 30 Sep | |
| 3 | Use-case list v1.0 | §3 | UC 5% | Done | 30 Sep | |
| 4 | Use cases: formal text, use-case diagram, activity diagrams | §3 | UC 5% | Not started | 5 Oct | |
| 5 | OOA: class diagram, sequence diagrams | §4 | OOA 4% | Not started | 6 Oct | |
| 6 | Project management: WBS and timeline | §5 | PM 2% | Not started | 3 Oct | |
| 7 | Elicitation write-up and validation sessions | §2.1 | RE 4% | Not started | 5 Oct | |
| 8 | Introduction | §1 | Content | Not started | 6 Oct | |
| 9 | Assembly, traceability and consistency sweep | all | Formatting 2% | Not started | 7 Oct | |
| 10 | Slides and rehearsal | n/a | Presentation 3% | Not started | 7 Oct | |
| 11 | Submit | n/a | n/a | Not started | 8 Oct | |

## Phase 0: Setup (done)

- [x] Private repo, AGENTS.md, CLAUDE.md, templates
- [x] Brief and rubrics converted to `brief/`
- [x] Lecturer clarification recorded (DEC-01)

## Phase 1: Elicitation material (partly done)

- [x] Document analysis (F-1 to F-30)
- [x] Transcripts stored: Manager, DCT, Driver, IT Admin
- [ ] Fill in the stakeholder register: at least 5 representatives, at most 2 from our team ([elicitation/README.md](elicitation/README.md))
- [ ] Fill in dates, interviewer and interviewee for each transcript (currently TBC)
- [ ] Add the question guide the document analysis refers to
- [ ] Record attendance for every meeting
- [ ] Short survey (the rubric names surveys explicitly)

**All engagement must end by Week 6.** Do not describe a session in the report unless it happened.

## Phase 2: SRS (done)

- [x] `requirements.md` v3.0 baseline, tag `srs-v3.0`
- [x] 70 FR rows (FR-68 withdrawn) and 17 NFRs, each traced to a source
- [ ] Optional v3.1: accessibility, PDPA and maintainability NFRs. Needs a new DEC and a version bump.
- [ ] Remaining open DECs: 21, 25, 26, 28, 29, and 27 (asked)

## Phase 3: Use-case list (done)

- [x] [use-cases/use-case-list.md](use-cases/use-case-list.md) v1.0, 28 use cases, IDs frozen
- [ ] **Open check:** confirm with the lecture slides that system-only included use cases (UC-27, UC-28) are acceptable, and whether Log In is a precondition or an include

## Phase 4: Use cases (report §3)

Depends on: Phase 3.

- [ ] Use-case diagram(s) in PlantUML, split by actor (2 to 3 diagrams). Include Email Service.
- [ ] Formal use cases from [use-cases/UC-TEMPLATE.md](use-cases/UC-TEMPLATE.md): 23 main in full, the 5 supporting ones short. Each has name, actors, preconditions, main flow, alternative flows and postconditions.
- [ ] Activity diagrams (about 5, UML notation, swimlanes):
  - [ ] AD-01 Weekly cycle
  - [ ] AD-02 Job Rejection Request and approval
  - [ ] AD-03 Leave Request
  - [ ] AD-04 Notify Staff
  - [ ] AD-05 Complete Job
- [ ] Check that the diagram matches the text exactly (rubric: consistent with textual use cases)

## Phase 5: Object-oriented analysis (report §4)

Can start now from the glossary. Finish after Phase 4 so the diagrams align with the use cases.

- [ ] Class diagram: classes named `CL-<GlossaryTerm>`, with attributes, methods, inheritance and associations
- [ ] Sequence diagrams (SD-01 to about SD-08) for the key use cases, using only classes that exist in the class diagram
- [ ] Every diagram has its ID in the title and is listed in [traceability.md](traceability.md)

## Phase 6: Project management (report §5)

Independent of other phases. Start now.

- [ ] WBS with numbering (1.1, 1.1.1) and levels phases → tasks → subtasks
- [ ] WBS covers requirements, design, implementation, testing, documentation and project management
- [ ] Timeline (Gantt) with dates, durations, dependencies and milestones, running **through M2 (20 Nov)**, not just M1

## Phase 7: Elicitation write-up (report §2.1)

Can start now with `elicitation.md` as the brief.

- [ ] Run the follow-up sessions in [elicitation/planned-interview.md](elicitation/planned-interview.md) (MTG-01 Manager, MTG-02 IT Admin, MTG-03 Staff), write each up from [elicitation/MEETING-TEMPLATE.md](elicitation/MEETING-TEMPLATE.md) within 24 hours, then update the DECs and SRS
- [ ] Write the chapter: techniques used, why, who was involved, attendance, and how the SRS was derived
- [ ] Describe the sessions as they actually happened

## Phase 8: Introduction (report §1)

- [ ] Cover page
- [ ] Team members and their contributions (real, per person)
- [ ] Plagiarism declaration, verbatim from the overview PDF, with team name (P8-1), member list and the submission date
- [ ] AI usage section: how and where AI was used, and what we changed (draw from [ai-usage-log.md](ai-usage-log.md))

## Phase 9: Assembly and consistency (all chapters)

- [ ] Assemble in the required report template (check it exists, see DEC-24)
- [ ] [traceability.md](traceability.md) complete: requirement → use case → class → sequence diagram
- [ ] Same terms everywhere (check against the glossary in [AGENTS.md](AGENTS.md))
- [ ] No contradictions between the SRS, use cases and diagrams
- [ ] Captions on every figure and table, numbered headings, references where needed (the brief cites Guest 2002 and Lupu and Ruiz-Castro 2021)
- [ ] Mock marking against [brief/rubric-m1.md](brief/rubric-m1.md)

## Phase 10: Slides and rehearsal

- [ ] Slides cover the key deliverable of each chapter, not every detail
- [ ] Declaration included
- [ ] Rehearse within the allocated time
- [ ] Q&A drill: every member can explain any diagram, including the AI section

## Phase 11: Submit

- [ ] Zip `INF2001-M1-P8-1.zip` containing the report and slides only
- [ ] Submit by **8 Oct** (deadline 11:59PM 9 Oct)
- [ ] Each member completes the peer evaluation by 11:59PM 9 Oct (late = 10% penalty)
- [ ] Push the final repo state. Never push without the team agreeing.

## Day-by-day plan

| Date | Work |
|---|---|
| 1–2 Oct | Assign owners. Confirm the use-case list against the slides. Start the WBS and timeline, the use-case diagram and the class diagram. Book the follow-up meetings and the survey. |
| 2–5 Oct | Formal use cases and activity diagrams. Run MTG-01 to MTG-03 and the survey. |
| 5–6 Oct | Sequence diagrams, elicitation chapter and introduction. |
| 6–7 Oct | Assemble the report, make the slides, consistency sweep, mock presentation. |
| 8 Oct | Zip, submit, peer evaluations. |
| 9 Oct | Buffer only. |

## Risks

| Risk | Mitigation |
|---|---|
| Presentation falls before 9 Oct | Have slides and diagrams ready by 7 Oct |
| Follow-up meetings can't be held before Week 6 ends | Drop them from the report rather than describe sessions that didn't happen |
| Two people edit the same file | Fill in the ownership table today |
| Diagrams and text drift apart | Update [traceability.md](traceability.md) as each artefact is made, not at the end |
| Terminology inconsistent | Use only the glossary terms in AGENTS.md |
