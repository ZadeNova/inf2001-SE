# M1 Report Gap Analysis: what stands between this report and an A / A-

> **Perspective:** written as a marker applying the INF2001 M1 rubric (Appendix B) to the report as submitted.
> **Report version reviewed:** Markdown export of the Google Doc, saved 7 Oct 2026, 17:19, plus the team's later fix of the † markers in Google Docs.
> **Rule used:** the report is marked as a standalone document. Anything a marker cannot see inside the report counts as missing.
> **Grade boundaries:** the brief does not state them. This file assumes **A- ≈ 80%** and **A ≈ 85%** of the report marks. Adjust if the module states otherwise.

---

## 1. Score summary

The report is worth 17 marks before the 3% group presentation. Estimates are per rubric item.

| Rubric item | Weight | Current estimate | After "Must" fixes | After all fixes |
|---|---|---|---|---|
| Requirement Engineering | 4 | 3.25 | 3.50 | 3.75 |
| Use Cases | 5 | 3.75 | 4.00 | 4.50 |
| Object-oriented Analysis | 4 | 3.25 | 3.50 | 3.75 |
| Project Management | 2 | 1.25 | 1.75 | 1.75 |
| Presentation: Formatting | 2 | 1.25 | 1.50 | 1.75 |
| **Total** | **17** | **12.75 (75%)** | **14.25 (84%)** | **15.50 (91%)** |

**To reach A-:** complete every item marked **Must** in section 3.
**To reach A:** also complete the **Should** items.

---

## 2. How to read this file

Each gap has the same fields, so people and AI tools can work through it in order.

| Field | Meaning |
|---|---|
| **ID** | Stable identifier (GAP-nn). Refer to gaps by ID when splitting work. |
| **Priority** | **Must** = needed for A-. **Should** = needed for A. **Could** = polish. |
| **Rubric** | The exact rubric wording the gap fails. |
| **Where** | Report section or figure. |
| **Problem** | What a marker sees now. |
| **Fix** | What to change. |
| **Needs team facts?** | **Yes** = only the team knows the answer; do not invent it. **No** = can be written from the report alone. |

---

## 3. Gaps by rubric item

### 3.1 Introduction (required content; affects every mark)

> Rubric B.1.1: "Cover page; Team members and their contributions; Plagiarism declarations; Elaborations on AI usage and declarations with changes made on the AI outputs."

#### GAP-01: Placeholders on the cover and declaration
- **Priority:** Must
- **Where:** cover page; Declaration
- **Problem:** `[Insert Date]`, `INF2001-M1-[Team X].zip`, `Declared by (Group Name): [Insert]` and `Date: [Insert date of submission]` are unfilled. The group name also reads "P8 -1".
- **Fix:** fill in the submission date (twice), the zip name `INF2001-M1-P8-1.zip`, the group name `P8-1`.
- **Needs team facts?** Yes (submission date)

#### GAP-02: Team contributions incomplete
- **Priority:** Must
- **Where:** §1.2
- **Problem:** the Role column is empty for all six members. Jun Keat and Jeremy are both credited with "Google Form Creation", but the WBS credits only Jeremy. Jun Keat's cell reads "Diagrams Report".
- **Fix:** add a role for each member. Make each contribution specific and consistent with the WBS owners in §5.1 (for example "Activity diagrams AD-01 to AD-04"). Peer evaluation uses this table.
- **Needs team facts?** Yes

#### GAP-03: AI declaration has an unfilled cell
- **Priority:** Must
- **Where:** §1.3, Claude row
- **Problem:** `[Team to complete: what you changed in the §2.1.1, WBS and timeline drafts.]` is still visible.
- **Fix:** state what the team changed in those drafts. Every member must be able to explain any AI-assisted part, because "all teams will be asked to elaborate on random parts during presentations".
- **Needs team facts?** Yes

---

### 3.2 Requirement Engineering (4%)

> Rubric: "Comprehensive use of elicitation techniques (interviews, surveys, document analysis). Clearly documented process, rationale, and stakeholder involvement."
> Appendix A of the project overview: "engage at least 5 Stakeholder Representatives with at most 2 representatives from your own team" and "Record the attendance of the meeting and include it in your Milestone Report."

#### GAP-04: No attendance records; stakeholder rule not demonstrated
- **Priority:** Must
- **Where:** §2.1.3
- **Problem:** the log lists six team members and no interviewees. §1.2 says Damien interviewed the Driver and Brandon the IT Administrator, so the names look like interviewers. Jeremy's row is blank. A marker cannot verify "at least 5 representatives, at most 2 from your own team", and there is no attendance record.
- **Fix:** rebuild the table with one row per session:

  | Session | Date | Mode | Interviewee (role played) | Own team? | Team members present |
  |---|---|---|---|---|---|

  Remove or explain Jeremy's row. Remove "Prototype Review" unless a prototype review took place.
- **Needs team facts?** Yes. Do not invent names or dates. If the rule was not met, state that honestly rather than fabricate attendance.

#### GAP-05: Appendix A does not contain the interview guides
- **Priority:** Must
- **Where:** Appendix A; cited by §2.1 and §2.1.1
- **Problem:** only the Technician questionnaire is covered, and only by a Google Sheets link. The Manager, Dual-Certified Technician, Driver and IT Administrator guides are missing. The template line "Attach completed, filled-in interview notes/attendance records…" is still there.
- **Fix:** paste each role's question set, the questionnaire questions and a short results summary into the appendix. Delete the template line.
- **Risk:** the link ends in `usp=sharing`. If it is open to anyone with the link, it may conflict with the declaration ("We did not share our materials… for public access"). Markers may also be unable to open it. Restrict it, and keep the content inside the report.
- **Needs team facts?** Yes (the guides)

#### GAP-06: Questionnaire date left unresolved in the text
- **Priority:** Should
- **Where:** §2.1.4 intro
- **Problem:** "we retain that display until its date format and mapping to the attendance records are confirmed" tells the marker the team does not know its own data.
- **Fix:** confirm the date (10/1/2026 in US format is 1 Oct 2026) and state it plainly.
- **Needs team facts?** Yes (confirm)

#### GAP-07: Document-analysis citations
- **Priority:** Should
- **Where:** §2.1.2, F-1 and F-4
- **Problem:** F-1 cites "(Overview, p.1)", which reads as the module's Team Project Overview, which §2.1.2 says is *not* a requirements source. F-1 also quotes "one month in advance", but the brief says "one month earlier". F-4 lists only a Manager question, while §2.1.1 says the questionnaire covered F-4.
- **Fix:** cite "(Aircon Retailer Project Description, opening section, p.1)", quote "earlier", and mention both sources for F-4.
- **Needs team facts?** No

#### GAP-08: Unexplained gaps in requirement IDs
- **Priority:** Could
- **Where:** §2.2 intro
- **Problem:** IDs jump (FR-02 → FR-04, FR-07 → FR-10…). "Gaps reflect withdrawn requirements" points at nothing in the report.
- **Fix:** one sentence listing the withdrawn IDs, or drop the sentence.
- **Needs team facts?** No

---

### 3.3 Use Cases (5%)

> Rubric: "Use case diagrams: Complete, correct, and neatly drawn UML diagram with all actors, relationships, and use cases. Consistent with textual use cases." Activity diagrams: "Clear workflows modelled for all key processes… Correct UML notation."

#### GAP-09: UC-15 actor notation is incorrect
- **Priority:** Must
- **Where:** §3.2 UC-15
- **Problem:** "Primary actor: Email/Phone" and "Secondary actors: Calling use case". A use case is not an actor, and the delivery service is a supporting (secondary) actor.
- **Fix:** primary actor: none (included use case, initiated by the including use case) or "System"; secondary actor: Email/Phone. Say it is included by UC-05, UC-06, UC-07 and UC-09.
- **Needs team facts?** No

#### GAP-10: Use case diagram is inconsistent with the text
- **Priority:** Must
- **Where:** Figure 3.1 vs UC-04 and UC-10
- **Problem:** UC-04 lists "Email/Phone through UC-15" and UC-10 can trigger notifications through FR-70, but the diagram has no `«include»` from either to UC-15. The diagram also shows two email actors ("Email Service" and "Email/Phone") without explaining the difference.
- **Fix:** add the two `«include»` links, or remove the claims from the text. Explain or merge the two email actors in §3.1.
- **Needs team facts?** No (decision only)

#### GAP-11: Design and implementation language in the use cases
- **Priority:** Should
- **Where:** §3.2 business-rule notes, e.g. UC-02, UC-04, UC-05, UC-09, UC-14
- **Problem:** "atomically", "after commit", "transaction", "balance-serialization rule", "SD-15 Draft protection". These are design terms; use cases describe observable behaviour.
- **Fix:** rewrite as what the user sees, e.g. "the decision and the Crew change are saved together; if saving fails, neither is applied".
- **Needs team facts?** No

#### GAP-12: Activity diagram coverage
- **Priority:** Could
- **Where:** §3.4
- **Problem:** four activity diagrams cover roster, Availability, Job rejection and account creation. The rubric's example list includes "notification", which has no diagram of its own.
- **Fix:** add a fifth diagram for Notify Staff (UC-15) or Complete Job (UC-14).
- **Needs team facts?** No

#### GAP-13: UC-07 name differs between sections
- **Priority:** Could
- **Where:** §3.2 vs §4.3 heading
- **Problem:** "Allocate Jobs/set weekly schedule (includes forming Van Crew and publishing Weekly Roster)" vs "Allocate Jobs / Set Weekly Schedule".
- **Fix:** use one name everywhere.
- **Needs team facts?** No

---

### 3.4 Object-oriented Analysis (4%)

> Rubric: "Comprehensive and accurate. Shows key entities, attributes, methods, and relationships… Aligns with use cases." Sequence diagrams: "Diagrams show clear lifelines, messages, and ordering."

#### GAP-14: Large diagrams are unreadable at page width
- **Priority:** Must
- **Where:** Figures 4.1a, 4.1c, 4.15 (SD-17) and other large sequence diagrams
- **Problem:** text inside the diagrams cannot be read at normal zoom. A marker cannot award "clear lifelines, messages" for what they cannot read.
- **Fix:** put large diagrams on landscape pages, split them, or add full-size copies in an appendix. Check the exported PDF, not just the Doc.
- **Needs team facts?** No

#### GAP-15: Figure numbering out of order
- **Priority:** Must
- **Where:** §4.3
- **Problem:** order is 4.7, **4.15, 4.16, 4.17**, 4.8, **4.18–4.20**, 4.9, 4.10, **4.21–4.23**, 4.11…
- **Fix:** renumber 4.2 to 4.23 in document order.
- **Needs team facts?** No

#### GAP-16: Manager associations missing from the domain class diagram
- **Priority:** Should
- **Where:** Figure 4.1a vs §4.1
- **Problem:** §4.1 says the Manager "manages Jobs, Vans, Crews, Weekly Rosters and Staff requests", but the diagram links Manager only to Notification.
- **Fix:** add the associations, or reword §4.1 to say the Manager acts on these through the control classes.
- **Needs team facts?** No

---

### 3.5 Project Management (2%)

> Rubric: WBS "covers all major project phases… Clear hierarchy with correct levels (phases → tasks → subtasks). Proper numbering." Timeline "clearly maps tasks from WBS, with realistic start/end dates, task durations, dependencies, and milestones. Readable and professional."

#### GAP-17: Gantt chart contradicts the WBS and timeline
- **Priority:** Must
- **Where:** §5.2, both Gantt tables
- **Problem:** owners are "Member 1" to "Member 6" while the WBS names people; WBS codes, phases and dates differ from §5.1 and §5.2; class diagrams are given to Chee Long in the chart but Jeremy in the WBS; "Document analysis (F-1 to F-30)" cites findings the report does not show. The second table has a "Current Week" column inside the phase header row.
- **Fix:** rebuild both tables from the §5.2 timeline (same codes, names, dates), or delete them. A mismatched chart costs more than no chart.
- **Needs team facts?** No

#### GAP-18: WBS owners do not match §1.2
- **Priority:** Must
- **Where:** §5.1, task 1.1.4
- **Problem:** the WBS gives all interviews to Chee Long. §1.2 says Erfan, Damien and Brandon interviewed.
- **Fix:** name the real interviewers in 1.1.4, consistent with §1.2 and §2.1.3.
- **Needs team facts?** Yes (confirm)

#### GAP-19: Presentation dates not stated
- **Priority:** Could
- **Where:** §5.2 rows 5.1.3 and 5.2.4
- **Problem:** "Week 6" and "Week 12" instead of dates.
- **Fix:** insert the real dates once known.
- **Needs team facts?** Yes

---

### 3.6 Presentation: Formatting (2%)

> Rubric: "Professionally structured report… with clear headings, numbering, captions, figures/tables, references where needed, and consistent formatting throughout. Clear and grammatically correct language, with consistent terminology… Strong alignment and traceability… No major contradictions, inconsistent naming, missing labels."

#### GAP-20: Working-process wording a reader cannot follow
- **Priority:** Must
- **Where:** throughout
- **Problem and fix:**

  | Find | Replace with |
  |---|---|
  | "We adopted the repository's current SRS v3.4 baseline:" (§2.2) | "The SRS contains" |
  | "interview subtabs" (§2.1.4) | "interview records (Appendix A)" |
  | "in the approved UCD" (§3.1) | "in the use case diagram (Figure 3.1)" |
  | "Round-3 Linked Jobs clarification" / "Round-3 clarification" (UC-05, UC-09) | "Linked Jobs rule" / "Clarification" |
  | "under the finalized merged structure", "in the finalized list" (UC-03, UC-04, UC-15) | delete the phrase |
  | "as corrected by the user" (UC-08) | delete |
  | "No remaining open question in this draft", "None identified for the current draft" | "None." |
  | "The finalized scope" (§2.1.5) | "The adopted scope" |

- **Needs team facts?** No

#### GAP-21: Inconsistent role names
- **Priority:** Must
- **Where:** throughout
- **Problem:** the same role appears as "Dual-Certified Technician", "dual-certified", "Dual-Brand Technician", "dual-Brand" and "Dual Certified". "Employee" appears where the glossary term is Staff.
- **Fix:** use the glossary terms (§1.4): **Dual-Certified Technician**, **Single-Brand Technician**, **Staff**.
- **Needs team facts?** No

#### GAP-22: No traceability matrix
- **Priority:** Must
- **Where:** new section, e.g. §2.3
- **Problem:** the rubric names "alignment and traceability" explicitly. Nothing in the report links the brief's requirements to the SRS, use cases and diagrams.
- **Fix:** add a table: Brief R1–R11 → FR IDs → UC IDs → AD/SD figures.
- **Needs team facts?** No

#### GAP-23: Table of contents and headings
- **Priority:** Must
- **Where:** Table of Contents; §2 heading; empty headings
- **Problem:** every page number is "1"; the note "Right-click the table above and select 'Update Field'…" is still present; §1.4 Glossary is not listed; "2. Requirement Engineering" is not styled as a heading; empty headings remain near §2.1.2 and §4.2.
- **Fix:** style the §2 heading, delete empty headings and the note, then regenerate the contents (Insert → Table of contents in Google Docs).
- **Needs team facts?** No

#### GAP-24: No references section
- **Priority:** Should
- **Where:** new section before the appendix
- **Problem:** the rubric asks for "references where needed". The report relies on the Project Description and the lecturer's clarification but cites neither formally.
- **Fix:** add References: the INF2001 Team Project Description (Aircon Retailer), the INF2001 Team Project Overview, the lecturer's clarification (date), and the two works the brief cites if used.
- **Needs team facts?** Yes (clarification date)

#### GAP-25: Tables have no captions
- **Priority:** Should
- **Where:** all tables
- **Problem:** all 30 figures are captioned; no table is.
- **Fix:** add "Table x.y – …" captions to the major tables (FR groups, NFRs, permission matrix, actors, key classes, WBS, timeline, glossary).
- **Needs team facts?** No

#### GAP-26: Final proofread and export check
- **Priority:** Should
- **Where:** whole report
- **Problem:** text from several authors and tools differs in style; Markdown exports have dropped symbols before (the † markers).
- **Fix:** one full read for grammar and consistency; export to PDF and check every page, especially diagrams, symbols and table breaks.
- **Needs team facts?** No

---

## 4. Submission requirements (not marked, but penalised if missed)

| ID | Requirement | Source | Status |
|---|---|---|---|
| SUB-01 | Presentation slides covering requirements, use cases, OO analysis and project management | Rubric B.1.2.2 | Not started |
| SUB-02 | Declaration on the slides as well as the report | Project overview, Non-plagiarism Declaration | Not started |
| SUB-03 | One zip named `INF2001-M1-P8-1.zip` with report and slides | Rubric B.2 | Not started |
| SUB-04 | Submitted by 11:59 PM, Fri 9 Oct 2026 (20% per day late) | Rubric B.2 | Pending |
| SUB-05 | Every member completes peer evaluation by 11:59 PM, Fri 9 Oct (10% penalty otherwise) | Rubric B.3 | Pending |
| SUB-06 | Every member can explain any section, including AI-assisted ones | Project overview, AI Usage | Pending |

---

## 5. Already resolved (do not redo)

| Item | Where |
|---|---|
| Student IDs consistent between cover and §1.2 | Cover, §1.2 |
| Mark weightings removed from headings | §2–§5 |
| Glossary added (39 terms) | §1.4 |
| § 2.1.1 elicitation techniques, rationale and reconciliation | §2.1.1 |
| Questionnaire data (11 responses, response IDs) | §2.1.1, §2.1.4 |
| AI declaration rewritten, one row per tool | §1.3 |
| Three-level WBS with numbering and an Implementation phase | §5.1 |
| Timeline with dates, durations, dependencies and milestones | §5.2 |
| Team-set markers (†) restored | §2.2 |
| FR/NFR counts verified: 50 FR (45 Must, 5 Should), 12 NFR (8 Must, 4 Should) | §2.2 |
| All 15 formal use cases present with full structure | §3.2 |
| 22 sequence diagrams covering all 15 use cases | §4.3 |

---

## 6. Suggested order of work

| Step | Gaps | Why first |
|---|---|---|
| 1 | GAP-01, 02, 03 | Compulsory content; quick once facts are known |
| 2 | GAP-04, 05, 18 | Largest Requirement Engineering loss; need team facts |
| 3 | GAP-17 | One contradiction undermines the whole PM section |
| 4 | GAP-20, 21, 23 | Find-and-replace; fast Formatting marks |
| 5 | GAP-09, 10, 14, 15 | UML correctness and readability |
| 6 | GAP-22, 24, 25 | Traceability and references |
| 7 | GAP-06, 07, 11, 16, 26 | Polish for A |
| 8 | SUB-01 to SUB-06 | Slides, zip, peer evaluation |
