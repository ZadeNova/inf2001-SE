# Task brief: Requirement Elicitation Process (M1 report chapter)

> **Assigned to:** ______ · **Reviewer:** ______ · **Target date:** ______ (before the M1 report is assembled; M1 is due 11:59PM, 9 Oct 2026)
>
> This is a reminder and working outline, not the chapter itself. Write the chapter in the team's report template. Keep this file updated as items are ticked off.

## 1. What the rubric grades

This chapter is half of **Requirement Engineering (4%)**. The SRS ([requirements.md](requirements.md)) is the other half. From [brief/rubric-m1.md](brief/rubric-m1.md):

> **Requirement Elicitation Process:**
> • Comprehensive use of elicitation techniques (interviews, surveys, document analysis).
> • Clearly documented process, rationale, and stakeholder involvement.

The presentation rubric also asks that "Requirements and stakeholder inputs are clearly explained, showing how the team identified, organised, and prioritised the proposed system needs."

Appendix A adds: "Record the attendance of the meeting and include it in your Milestone Report."

So the chapter must show **what** techniques were used, **why** each was chosen, **who** took part, and **how** their input became requirements.

## 2. Suggested chapter outline

| § | Section | What to write | Where the material is |
|---|---|---|---|
| 1 | Overview | The elicitation approach in one paragraph: document analysis first, then clarification with the client (lecturer), then stakeholder interviews, then resolving conflicts into decisions and requirements. Include a simple process diagram (flowchart) | This file, §3 |
| 2 | Stakeholders | Table of Stakeholder Representatives: name, role played (Manager, Dual Certified Technician, Driver, IT Administrator, …), own team Y/N, sessions attended | [elicitation/README.md](elicitation/README.md) stakeholder register (**to fill in**) |
| 3 | Technique 1: Document analysis | Method, output (30 findings F-1 to F-30), rationale | [elicitation/document-analysis.md](elicitation/document-analysis.md) |
| 4 | Technique 2: Client clarification | The written query to the lecturer (client) about the availability horizon, and the answer | [decisions.md](decisions.md) DEC-01; [brief/project-description.md](brief/project-description.md) Lecturer clarifications |
| 5 | Technique 3: Interviews | Format (structured sections), who, when, how recorded, question themes, key findings per role | [elicitation/interviews/](elicitation/interviews/) |
| 6 | Other techniques (if used) | Survey, prototype walkthrough, etc. Only include what was actually done | **Team to confirm** |
| 7 | Analysis and conflict resolution | How ambiguities and conflicts were logged and resolved: 41 DEC entries, 11 of them conflicts between interviews (DEC-31 to DEC-41), with examples | [decisions.md](decisions.md) |
| 8 | From findings to requirements | Traceability: each FR/NFR cites its source; the MoSCoW prioritisation rules | [requirements.md](requirements.md) §1.4, §5 |
| 9 | Attendance records | Attendance table per session (date, mode, attendees) | **To fill in** |

## 3. What we already know (use these facts, check them against the files)

**Document analysis:**
- File: `elicitation/document-analysis.md`, dated **Sep 25, 2026**, author "@Zade".
- Method stated in the file: the brief was reviewed line by line against six checks. These were contradictions, undefined terms, missing processes, business rules with unclear edge cases, numerical constraints, and missing non-functional detail. Duplicates were merged, and each finding was matched to an interview question (new questions were added where needed).
- Output: 30 findings (F-1 to F-30), plus a list of the 5 findings with the biggest scope impact (§3 of that file).

**Client (lecturer) clarification:**
- The contradiction between "one month" and "5 weeks" was raised in writing with the lecturer (client).
- Answer: "It should be "1 month" for consistency." and "earlier" is changed to "in advance". Recorded in DEC-01.

**Interviews:**

| Role | File | What the file states about format | Structure |
|---|---|---|---|
| Manager | `interviews/manager.md` | "recorded and transcribed on Zoom" | Opening, Process, Clarifications, Conflicts and edge cases, System, Closing |
| Dual Certified Technician | `interviews/dct.md` | "recorded and transcribed on Zoom" | Opening, Clarifications, Process, Conflicts, System, Closing |
| Driver | `interviews/driver.md` | Not stated | 17 numbered questions in 3 groups: operational/daily routine; route, scheduling and contingency; availability, preferences and system interaction |
| IT Administrator | `interviews/ita.md` | Not stated | Accounts and permissions, security, performance, availability, recovery, retention, devices, integration, closing |

**Analysis:**
- 41 decision entries: DEC-01 to DEC-30 from the brief and rubric review, and DEC-31 to DEC-41 from conflicts between interviews.
- Examples of conflicts worth describing:
  - **Travel time** (DEC-31): the Manager wants a fixed 30-minute allowance, while the Driver wants estimated driving time.
  - **Overtime approval** (DEC-32): the Driver expects an approval step, while the Manager only wants a warning.
  - **Deleting leavers' accounts vs keeping records for a year** (DEC-34): both statements come from the IT Administrator.
- Resolution rule used: the Manager's answer was adopted as process owner where one existed. Otherwise the simplest option consistent with the brief was chosen, and each decision says which parts were chosen by the team.
- **Team decisions that override a stakeholder statement** (from the team review on 30 Sep):
  - **DEC-42, rejections need the Manager's approval.** The Manager and DCT both said no approval was needed.
  - **DEC-43, daily Standby Staff.** The Manager said "No dedicated standby staff".

  Explain both in the chapter, with the rationale recorded in `decisions.md` §I. Markers check that requirements match their sources, so an unexplained override looks like an error.

**Result:** the SRS has 70 FRs and 17 NFRs, each citing its source, prioritised with MoSCoW (§5 of the SRS).

## 4. To-do checklist

- [ ] **Stakeholder register:** fill in `elicitation/README.md` with names, role played and own team Y/N. Check against Appendix A (at least 5 representatives, at most 2 from our own team).
- [ ] **Interview metadata:** date, interviewer, interviewee and mode for all four interviews. The index in `elicitation/README.md` currently has these as TBC.
- [ ] **Attendance table** for every session (Appendix A requires it in the report).
- [ ] **Lecturer email date:** `document-analysis.md` F-1 says the client clarified on **27 Sep 2026**, while DEC-01 says "recorded 2026-09-30". Confirm the actual email date and correct DEC-01 if needed.
- [ ] **Stakeholder question guide:** `document-analysis.md` refers to a question guide that is **not in the repo**. Add it (it shows the interviews were planned), or drop the references.
- [ ] **Surveys:** the rubric names surveys. If one was run, add the questions and a results summary. If not, don't claim one.
- [ ] **Rationale** for each technique, one or two sentences each. For example: document analysis first, to find gaps before meeting stakeholders; interviews, because the process depends on individual roles and edge cases; written clarification, because contradictions in the brief are the client's to resolve.
- [ ] **Team review and overrides:** describe how the team reviewed the draft SRS (round 1 on 30 Sep: 16 rows agreed, DEC-42 to DEC-44 decided), and justify the two overrides (DEC-42, DEC-43).
- [ ] **Process diagram** (optional but recommended): document analysis → questions → client clarification + interviews → DEC log → SRS.
- [ ] **AI usage:** the report's AI section must mention where AI helped (e.g. the SRS draft, the DEC analysis). Use [ai-usage-log.md](ai-usage-log.md).

## 5. Rules to keep

- **Cite transcripts, not Answer keys.** The "Answer key" tables at the end of `manager.md` and `dct.md` are team summaries, not stakeholder statements.
- **Keep the two ID schemes apart:** F-1 to F-30 are document-analysis findings, and AK-01 to AK-14 are Answer-key rows (see [AGENTS.md](AGENTS.md)).
- **Don't invent names, dates or attendance.** Leave TBC until confirmed.
- **Quote exactly** when quoting a stakeholder.
- **Use glossary terms** from AGENTS.md (Staff, Crew, Job, Availability, …).
