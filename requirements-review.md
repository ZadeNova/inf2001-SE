# SRS review: findings and verdict

> **Historical review updated for current scope (2026-10-01, DEC-45):** this review assessed an earlier SRS. Current scope and requirement status are in SRS v3.1.

**Reviewed:** 30 September 2026 (Singapore time).  
**Reviewer:** OpenAI Codex.  
**Scope:** All 68 Functional Requirements (FR-01 to FR-68) and all 17 Non-Functional Requirements (NFR-01 to NFR-17) in [requirements.md](requirements.md).  
**Baseline:** Git commit `b8211f8eb6b8dc212eecff849c4a37e119ecbecd`; initially clean working tree. Review branch: `CL/requirements-review`.

## 1. Verdict

**Keep this as a useful draft for team review; do not baseline or submit it as an agreed, fully consistent SRS yet.**

The draft represents all eleven initial requirements and correctly uses the lecturer's **1 month in advance** clarification rather than five weeks. It also captures substantial interview detail, separates blocking rules from warnings, provides verification notes, and openly identifies several assumptions. These are strengths.

However, a coverage reference is not proof that the resulting behaviour satisfies the brief. The highest-priority problems are the Staff permission rule, altered retention wording, unresolved Assignment/Workload semantics, interpretation of the lowest-three and minimum-Van rules, and incomplete acceptance criteria. Some additions are supported by interviews but their citation format and provenance have not been approved under the repository rules.

| Review disposition | Functional | Non-functional | Total |
|---|---:|---:|---:|
| Retain the basic requirement | 14 | 1 | 15 |
| Revise wording, boundaries or verification | 37 | 14 | 51 |
| Hold the affected rule until a decision is recorded | 17 | 2 | 19 |
| **Individually reviewed** | **68** | **17** | **85** |

These are **review recommendations**, not changes to the SRS's Status column. “Retain” does not mean “Agreed” or certify its dependencies. “Hold” concerns finalisation of the affected behaviour; draft work can continue around it. There is no recommendation to discard or renumber the requirements wholesale.

Approximately **20 use cases are feasible** from this scope. The rubric requires coverage of major goals, not a fixed number. A candidate grouping follows the SRS audit in section 6.

## 2. Evidence and authority

The actual source folder is [brief/](brief/). Reviewed:

- [Project description and binding lecturer clarifications](brief/project-description.md).
- [Milestone 1 requirements and rubric](brief/rubric-m1.md).
- [Milestone 2 requirements and rubric](brief/rubric-m2.md).
- [Assessment overview and stakeholder instructions](brief/assessment-overview.md).
- [AGENTS.md](AGENTS.md), [decisions.md](decisions.md), [traceability.md](traceability.md), [AI usage log](ai-usage-log.md), and the [use case template](use-cases/UC-TEMPLATE.md).
- [Elicitation index](elicitation/README.md), read before verifying the four primary transcripts: [Manager](elicitation/interviews/manager.md), [Dual Certified Technician](elicitation/interviews/dct.md), [Driver](elicitation/interviews/driver.md), and [IT Administrator](elicitation/interviews/ita.md).

The review treats the brief and lecturer clarifications as binding. Interview additions are evidence for proposals, not permission to silently override a minimum requirement. The Answer-key tables are team summaries and were not used as stakeholder statements. No external searches, public rendering services, or publication were used.

In the audit tables, **MGR**, **DCT**, **DRV** and **ITA** mean the corresponding primary transcript above. Question labels match the SRS citation scheme; they identify audit evidence without endorsing `INT-` as an approved repository citation format.

### 2.1 Brief R1–R11 coverage

The quotations below preserve the brief's wording, including its typos. R8's original wording is overridden by the lecturer clarification immediately after the table.

| Brief source and exact wording | Draft mapping | Assessment |
|---|---|---|
| **Brief R1:** “The app should be Web-based in a language of your choosing” | NFR-17; NFR-14 supports browser compatibility | Covered as a constraint. Language choice remains the team's. |
| **Brief R2:** “The manager should be able to visualise the staff workload immediately on the landing page” | FR-56; NFR-01 | Feature covered, but values depend on held Workload rules. The response criterion still needs agreement. |
| **Brief R3:** “The manager should be able to allocate jobs to staff for one week at a time” | FR-41 | Weekly scope covered. Job-to-Van-to-Staff Assignment ownership must be made explicit. |
| **Brief R4:** “The manager should be able to view up to three staff availability and any relevant information to make the job assignment easier on the job allocation page” | FR-43 | Selected comparison is supported by MGR [System Q3]. Specify the week/date being compared. |
| **Brief R5:** “When displaying the staff availability, the workload assigned, staff's job preference, staff's location at a particular date, and availabilities for the week should be shown” | FR-43, FR-21; FR-15 is another Availability view | Comparison fields covered. Clarify whether R5 also applies to the separate Availability calendar and whether “so far this week” means the week being allocated. |
| **Brief R6:** “On the manager'slanding page, the top three staff with the lowest workload should be shown, and highlight all staff over 40 hours of jobs allocated” | FR-55, FR-56, FR-57 | Strictly greater than 40 is correct. Separate per-role lists, Leave exclusions, ranking period and ties need DEC-05 closure. Workload calculations remain held. |
| **Brief R7:** “Staff should be able to view their weekly job assignments and overall workload for the month on their landing page” | FR-58, FR-59 | Feature covered. The month definition and published-week selection remain unspecified. |
| **Brief R8:** “Staff can add and edit their availabilities up to 5 weeks ahead of time.” | FR-13, FR-14 | Correctly superseded by the lecturer's one-month ruling. Exact boundary remains open in DEC-30. |
| **Brief R9:** “Staff can indicate their job preference for the week” | FR-21 | Covered. Missing preference, editing deadline and advisory matching need acceptance rules. |
| **Brief R10:** “Staff can reject jobs assigned to them, but they will be warned to discuss the jobs with their manager before proceeding with the rejection” | FR-62, FR-63 | Warning is preserved. Crew-wide consequences of a rejection need DEC-15 closure. |
| **Brief R11:** “The company's IT administrators will oversee adding new staff and managers to the system” | FR-02, supported by FR-01 and FR-03 | Account creation covered. Import and account removal are additional scope, not necessary to demonstrate R11. |

**Binding override:** The lecturer says, “It should be "1 month" for consistency.” and “to avoid the ambiguity, the "earlier" is now changed to "in advance".” See [Lecturer clarifications](brief/project-description.md#lecturer-clarifications), DEC-01 and DEC-30. The Driver's five-week answer does not reinstate five weeks.

### 2.2 Narrative business constraints

| Exact brief quotation | Relevant requirements | Review result |
|---|---|---|
| Brief §Company ¶1: “work allocation is assigned weekly every Monday. The workload allocation planning will start every Thursday of the week.” | FR-16, FR-17, FR-41, FR-49 | Interview supplies a specific two-week lead-in example. Record its adoption in DEC-02 and specify publication/visibility semantics. |
| Brief §Company ¶1: “If employees miss the weekly deadline, requests would be dealt with on a case-by-case basis.” | FR-17 | Include first late submission, not only changing an existing entry. |
| Brief §Company ¶2: “Only certified technicians for the brand are qualified to do the installation or servicing.” | FR-10, FR-31, FR-32, FR-44 | Brand checks are present. Expiry validity at the Job date needs an agreed rule. |
| Brief §Company ¶3: “Currently, there are six vans.” | FR-27, FR-28, FR-51 | Initial fleet covered. “Currently” is not evidence for permanently hard-coding six as a maximum. |
| Brief §Company ¶4: “there should be at least three vans can be on service daily except for Sunday”. | FR-45, FR-49 | Draft allows an override and measures crewed Vans. Confirm the service-count definition and exception treatment in DEC-19. Current scope follows DEC-45. |
| Brief §Company ¶4: “The minimum manpower for a van is two and the maximum is three.” | FR-30, FR-32, FR-44 | Bounds covered. Apply them to operational Vans and record the emergency exception to fixed daily Crews. |
| Brief §Company ¶4: “All staff are given 7 days annual leave.” | FR-22 to FR-25 | Entitlement covered; yearly/no-carry-over details are supported by MGR [Process Q4]. Balance and cancellation boundaries still need definition. |
| Brief §Company ¶5: “A van will be sent to the workshop for servicing every two months.” | FR-28, FR-29 | Detailed rotation is supported by MGR [Process Q3]. Input/generated dates and calendar-change effects remain open. |
| Brief §Company ¶5: “On average, there are more than 20 jobs for aircon installation and servicing daily.” | FR-34 to FR-51; NFR-01, NFR-03 | No representative Job/history dataset is defined for verification. More than 20 Jobs is an operational volume, not a use-case count. |

## 3. Findings that affect the verdict

### 3.1 Source references are present, but 59 rows lack an allowed source citation

**59 of 85 source cells cite only interviews: 45 FRs and 14 NFRs.** AGENTS.md permits `Brief`, `MTG-nn` and `DEC-nn`; it says, “Items without a source are flagged, not merged.” SRS §1.4 acknowledges that `INT-` is proposed.

This is a citation-policy gap, not a claim that those 59 rows have no evidence. The team should either approve the citation scheme through the AGENTS.md owner or register genuine interview records under MTG IDs. Do not invent attendance, names or dates. An open DEC reference identifies an unresolved question; it is not an adopted answer.

### 3.2 Permissions exceed the described Staff capabilities

NFR-12 says Staff “view and edit only their own Availability, Job Preference, Leave and Assignments”. Read literally, this grants Assignment editing. The Manager allocates and reassigns under FR-41/FR-50, while Staff reject or complete Jobs under FR-62/FR-39. “Own record” is not sufficient permission for every action on it.

Replace the broad wording with an agreed actor × resource × action matrix. Distinguish viewing an Assignment, rejecting it, recording completion, moving it, approving Leave, and changing permissions. Also resolve when a role change affects active sessions. Link this to DEC-17/DEC-18/DEC-37.

### 3.3 Retention reverses the primary-source qualifier

ITA [Retention] says: **“All schedules should exist up to one year in our system”**. NFR-13 says **“at least 1 year”**. These are not equivalent. The yearly-review rationale does not authorise silently selecting the latter.

DEC-34 should settle the retention period, its start date, deletion/deactivation/anonymisation on departure, treatment of past/current/future records, and the relationship to audit history. FR-05, FR-67 and NFR-13 must agree. Do not adopt a destructive account-removal flow while that policy remains open.

### 3.4 The central Workload model is still unresolved

FR-52/53/54 are correctly marked Blocked. They govern travel, Technician attribution and actual-time replacement. Their unresolved definitions also affect comparison, suggestions, warnings, ranking, Landing Pages and monthly metrics: FR-43/45/48/55–58/60 and parts of FR-50.

Record one consistent calculation contract covering:

- Which Staff are assigned to each Job when a Van has two Technicians.
- Driver hours, travel treatment, lunch/break exclusions, and emergency Crew changes.
- Planned versus actual hours and how cancelled/rejected Jobs affect totals.
- The selected planning week, the Landing Page's default week, and calendar versus rolling month.

DEC-04/DEC-10/DEC-20/DEC-31/DEC-39/DEC-40 contain these questions. Keep designing views, but label calculation-dependent results provisional.

### 3.5 Two brief interpretations need explicit closure

FR-57 implements **three Drivers plus three Technicians**, with Leave exclusions. MGR [added follow-up: lowest three] explicitly requests this: **“No, separately.”** It is a defensible interpretation of the ambiguous R6 wording, not an invention. Nevertheless, DEC-05 is still Open. A list of six people does not itself establish the intended ranking interpretation. Agree whether role lists satisfy R6 or whether an overall trio is also needed; define ties, fewer than three eligible Staff, and partial-week Leave.

FR-45/49 permit fewer than three Vans because MGR [Conflicts Q1] says: **“The system shouldn't stop me from publishing”**. The brief still states the service minimum. This is an exception-handling question, not proof that the minimum can be ignored. DEC-19 must define how a shortage is warned about, recorded, and counted. “Crewed” can include a Van with no Jobs; it is not automatically the same as “on service”.

### 3.6 Rejection, cancellation and publication states are incomplete

FR-63 makes rejection immediate, without approval. FR-56/65 nevertheless categorise rejections with “pending requests”. A rejection can be pending reassignment; it should not silently become a Manager approval request.

DEC-15 must specify whether one Staff rejection releases the whole Van Job or only that Staff Assignment, and how other Crew lists, Workload and notifications change. FR-38 also needs a transition table distinguishing Job cancellation from Assignment removal. A Cancelled Job should not be counted as an Unassigned Job merely because its Assignment is removed.

Draft versus published roster visibility is not defined. Staff must be able to see the published following week while still using their current week's Assignments; the published-week selection and revisions need explicit rules.

### 3.7 Validation is specified for too few entry points

FR-44 covers allocation and Crew changes. Existing Assignments can also become invalid after Job edits, Leave approval, Availability approval, emergency unavailability, Certification changes, Van breakdown or holiday updates.

For each active entry point, specify whether the change is blocked, accepted with affected Assignments flagged, or followed by reassignment. FR-18 is Withdrawn by DEC-45; FR-29 explicitly makes Jobs Unassigned. Preserve the approved history policy. Resolve the remaining distinctions using DEC-09/DEC-10/DEC-13/DEC-14/DEC-19/DEC-34/DEC-35.

### 3.8 Several acceptance notes add or omit consequential rules

- **FR-34:** Only the model is labelled optional, and its test refuses omitted required fields. This appears to make notes mandatory. DCT [job info] says **“Notes are useful too”**, not that blank notes prevent Job creation.
- **FR-11:** A 30-day fixture does not settle “one month”. Use the agreed calendar boundary.
- **FR-28:** Verify the Sunday-to-Monday rule under the current DEC-45 scope.
- **FR-39/40:** “A Crew member” and optional photo capability do not settle whether only Technicians complete Jobs or whether the invoice photo is mandatory. MGR asks Technicians to complete with a photo; DEC-40 remains open.
- **FR-15:** Available/Morning/Afternoon/Leave omits fully unavailable and not-yet-submitted states.
- **FR-30/42:** Half-day Availability, a fixed daily Crew and Jobs longer than one Slot need consistent timing rules. Do not assume that a six-hour Installation fits a four-hour preferred Slot.
- **FR-66:** “assumed IT Administrator” is not an agreed audit-viewing permission.

### 3.9 NFRs need measurement contracts, not just numbers

The M1 rubric requires: **“Each requirement measurable and justified.”** NFR-01/04/05/16 visibly retain TBCs. Other rows need workload fixtures, measurement start/end points, allowed failure rates, supported versions/devices, or conflict behaviour.

Define a representative dataset including more than 20 daily Jobs and the agreed history period, alongside the concurrency workload. Fifty sessions is different from fifty distinct people on multiple devices. An hourly backup schedule is not proof of a one-hour maximum data loss.

Offline submission, retry and email 2FA also introduce observable functions; they need use-case flows or supporting functional specifications, even if retained under quality categories. New numerical targets or HTTPS/password-storage controls must be labelled team proposals with a source/decision, not attributed to a stakeholder who did not state them.

### 3.10 Some “conflicts” are unconfirmed scope questions

Keep the entries open, but do not overstate their evidence:

- **DEC-35:** The Manager requests Certification information and reminders. The transcript does not say who edits Certifications. ITA's exclusive permission-management authority is not necessarily exclusive Certification-data maintenance. The Answer key's claim about Manager maintenance is not stakeholder evidence.
- **DEC-36:** Manual ongoing onboarding and a one-off account import can coexist. The Manager's Jobs spreadsheet and ITA's employee-portal schedules may be different datasets. Confirm the interface scope before calling them a direct contradiction.
- **DEC-37:** Different information needs for Managers and Staff are not inherently conflicting; the missing detail is which role the ITA visibility rule applies to.
- **DEC-41:** Email 2FA, simplicity and offline reading create a design trade-off, not a proven impossibility.

### 3.11 Assessment evidence and downstream traceability remain incomplete

There are four transcript files, but that alone proves neither four distinct representatives nor failure to meet the minimum five. The register and interview metadata do not establish compliance with Appendix A: **“at least 5 Stakeholder Representatives with at most 2 representatives from your own team”**. Record actual attendance and provenance; a fifth representative need not be a fifth system actor.

The repository contains no concrete `UC-nn-...` files or `.puml` diagrams; traceability.md is a scaffold. This is downstream readiness context, not a defect merely because this document is an SRS. However, the SRS cannot yet demonstrate the rubric's end-to-end alignment.

The existing AI log still says human changes after Claude output are to be completed. Record the actual accepted/changed/withdrawn rows after team review, rather than treating this second AI review as human agreement.

## 4. Individual review of all 68 Functional Requirements

All rows below are subject to the global citation and adoption findings in section 3. Labels are recommendations for the requirement's substance, not approved statuses.

| ID | Subject | Verdict | Evidence | Finding / required action |
|---|---|---|---|---|
| FR-01 | Roles and Landing Pages | Retain | Brief R2/R7/R11; ITA [Onboarding, Permissions] | Role separation is supported. Retain; settle multiple-role/Manager inheritance questions in DEC-18 before freezing the class model. |
| FR-02 | Create accounts | Revise | Brief R11; ITA [Account info]; MGR [Clarification Q2] | Required account creation is supported. Separate creation from the password-change capability; define required fields and role-specific validation rather than testing both as one undifferentiated requirement. |
| FR-03 | Permission ownership | Retain | ITA [Permissions] | Exclusive IT Administrator control is explicit. Retain and enforce it on every role/permission-changing entry point. |
| FR-04 | Change role | Revise | ITA [Role change/leaver] | Specify when changed permissions affect existing sessions. The test assumes next-login activation although the description does not. Resolve future Assignments when Staff become Managers (DEC-17/18). |
| FR-05 | Remove leaver account | Hold | ITA [Role change/leaver, Retention]; DEC-34 | Hold delete versus deactivate and record disposition. Do not cascade-delete historical Workload merely to satisfy account removal. |
| FR-06 | Forgotten password | Retain | ITA [Passwords] | Email-based recovery is supported. Retain; its recovery flow belongs alongside authentication and account-access handling. |
| FR-07 | Lock and unlock | Revise | ITA [Passwords] | The lockout threshold is TBC; define reset/window behaviour and successful IT Administrator unlocking, not only a negative actor test. These are proposed acceptance details, not sourced numbers. |
| FR-08 | Employee CSV import | Hold | ITA [Existing systems, Priorities]; DEC-36 | Hold import scope/schema and one-off versus ongoing operation. Manual creation does not inherently contradict migration. Invalid/duplicate rows and permission assignment need agreed outcomes. |
| FR-09 | Non-working-day calendar | Withdrawn | DEC-45 | Removed from current scope; ID retained. |
| FR-10 | Certification data | Hold | Brief §Company ¶2/4; MGR [Clarification Q2 follow-up, Q5]; DEC-35 | Data fields are supported; the maintenance actor is not identified by the primary transcript. Hold that actor/permission decision and link qualification to the agreed date-validity rule. |
| FR-11 | Expiry reminder | Revise | MGR [Clarification Q2 follow-up] | Retain the reminder need, but define calendar-month arithmetic, trigger frequency and delivery channel. A 30-day test is not an agreed interpretation of one month. |
| FR-12 | Certification scan | Retain | MGR [Clarification Q2 follow-up] | Supported explicitly as non-essential. Retain as Could; file-format/size choices remain acceptance proposals, not additional stakeholder facts. |
| FR-13 | Half-day Availability | Revise | Brief R8 as clarified; MGR [Clarification Q4]; DCT [Clarification Q2] | Define unavailable, missing and deleted entries under DEC-03; distinguish a preferred Slot from actual Availability. Apply the horizon and lock rules to all entry paths. |
| FR-14 | One-month entry horizon | Hold | Brief R8 + lecturer clarification; DEC-01/30 | One month is correct. Hold the exact date boundary until DEC-30 settles inclusivity and month-end behaviour; do not reinstate five weeks. |
| FR-15 | Manager Availability calendar | Revise | Brief §Intro ¶4 as clarified; MGR [System Q2, Clarification Q6] | Add fully unavailable/not-submitted display states. Specify the date boundary and whether R5 details are available from this view (DEC-03/06/08/30). |
| FR-16 | Wednesday lock | Hold | Brief §Company ¶1; MGR [Process Q1, Clarification Q6 follow-up]; DEC-02 | The 12-day lead-in matches the Manager's example; it is not an arithmetic error. Hold its adoption, timezone and exact cutoff semantics before finalising tests. |
| FR-17 | Late Availability request | Revise | Brief §Company ¶1; MGR [Conflicts Q2]; DCT [deadline follow-up] | Support first late submission as well as changes. Define pending/approved/rejected effects and conflicts with published Assignments (DEC-02/10/19). |
| FR-18 | Manager Availability override | Withdrawn | DEC-45 | Staff set their own Availability or submit a Late Availability Change Request; ID retained. |
| FR-19 | Copy prior Availability | Retain | DCT [Clarification Q2] | Explicit optional request. Retain as Could; copied dates must still obey FR-14/16 and the holiday rules. |
| FR-20 | Manager excluded from Workload | Retain | MGR [Clarification Q1] | Explicitly supported. Retain. Do not infer unrelated Manager Leave entitlement or additional administrative roles from this statement. |
| FR-21 | Weekly Job Preference | Revise | Brief R9/R5; DCT [Clarification Q4]; DRV [Q10]; MGR [ordering follow-up] | Fields and advisory use are supported. Define missing preference, edit deadline, area matching and week context under DEC-07/08. |
| FR-22 | Submit Leave | Revise | Brief §Company ¶4; MGR [Process Q4]; DCT [Process Q3] | The application flow is supported. Resolve full/half days, non-working days, overlapping requests and whether withdrawal is supported (DEC-13); do not silently add these behaviours. |
| FR-23 | Approve/reject Leave | Retain | MGR [Process Q4 and follow-up] | Decision visibility and rejection reason are supported. Retain; approval must obey the shared balance and Assignment-consistency rules. |
| FR-24 | Leave blocks Assignment | Revise | MGR [Process Q4]; DRV [Q15] | New allocation blocking is supported. Define the effect of approving Leave after publication and its interaction with already-entered Availability (DEC-13/19). |
| FR-25 | Leave balance | Revise | Brief §Company ¶4; MGR [Process Q4]; DCT [Process Q3] | Seven days/calendar year/no carry-over is grounded. Specify charging across years, insufficient balance, duplicate approval and cancellation effects (DEC-13). |
| FR-26 | Crewable-Van count | Revise | MGR [Process Q4]; explicitly labelled derived | A useful derived proposal, not a direct feature request. Define whether the count uses existing Crews or feasible alternative Crews and which Brands/Slots constrain it (DEC-09/13/19). |
| FR-27 | Van number/plate | Retain | Brief §Company ¶3; DRV [Q2]; MGR [Process Q3] | Required reference data is supported. Retain; this does not itself authorise a fleet CRUD interface or a permanent six-Van maximum. |
| FR-28 | Workshop rotation | Revise | Brief §Company ¶5; MGR [Process Q3]; DEC-14; DEC-45 | Rotation details are grounded. Resolve manual versus generated dates and input actor; verify Sunday-to-Monday movement. |
| FR-29 | Breakdown/date range | Revise | MGR [Conflicts Q4]; DRV [Q8] | Unassignment is supported. Define remaining Crew availability, notifications and Workload updates; agree treatment of in-progress/Completed Jobs instead of unassigning every record indiscriminately. |
| FR-30 | Daily Crew composition | Revise | Brief §Company ¶3/4; MGR [Process Q1, Clarification Q4 follow-up] | Revise 'each Van' to avoid requiring Crews for unavailable Vans. Make FR-33's emergency exception explicit and resolve half-day Availability versus fixed daily Crews (DEC-09/10). |
| FR-31 | Technician cannot drive | Retain | MGR [Clarification Q3]; DCT [Clarification Q1] | Explicit separation of duties. Retain as a blocking rule. |
| FR-32 | Crew Brand coverage | Revise | Brief §Company ¶2/3; MGR [ordering]; DCT [Conflicts Q1 follow-up] | One DCT on a mixed-Brand Van is supported by primary testimony. Specify collective Brand coverage, individual Job attribution and Certification expiry validity (DEC-09/19/35/39). |
| FR-33 | Emergency Crew change | Revise | MGR [Clarification Q4 follow-up]; DRV [Q7] | Supported exception. Define effective time, remaining Jobs, old/new recipients and preservation of completed-work attribution; a whole-day swap must not silently rewrite hours. |
| FR-34 | Create Job and fields | Revise | MGR [Process Q2]; DCT [job-info follow-up]; DRV [Q2] | Notes appear mandatory without source support; model is explicitly optional. Define a field/validation table, including positive unit counts and date/Slot rules (DEC-11/12/22). |
| FR-35 | Default/edit duration | Retain | MGR [duration follow-up, Clarification Q5 follow-up]; DCT [Clarification Q3 follow-up] | One/three hours per unit and adjustment are explicit. Retain. Timing of a duration longer than one Slot still needs the allocation rules. |
| FR-36 | Single Brand/grouped Jobs | Revise | MGR [Process Q2]; DCT [job-info follow-up] | Supported two-Job representation. Define how related Jobs are identified and whether they must share a Van; address alone can group unrelated visits (DEC-11). |
| FR-37 | Update/cancel Job | Revise | MGR [cancellations follow-up] | Supported. Revalidate changed Brand, units/date/duration against existing Crews and Slots; distinguish cancellation from deletion and update totals/recipients. |
| FR-38 | Job status | Revise | MGR [Conflicts Q3/Q4, cancellations, completion] | Define allowed transitions and distinguish Job status, Assignment status and roster publication. 'At least' plus 'each transition' does not give an executable transition specification. |
| FR-39 | Record completion | Hold | DCT/MGR [completion follow-up]; DEC-40 | Hold whether any Crew member or Technicians perform completion. Define time validation, break treatment, repeat submission/correction and Workload effects. |
| FR-40 | Signed invoice photo | Hold | MGR [completion follow-up]; DEC-40 | Hold required versus optional evidence. The Manager requests completion with a photo; 'shall be able to attach' and Should priority do not establish optionality. |
| FR-41 | Allocate a week | Hold | Brief R3; MGR [Process Q1, Clarification Q6]; DEC-10/16/39 | Weekly allocation is supported. Hold final Assignment ownership: Van/Crew Jobs must produce coherent individual Staff views, rejection rights and Workload. |
| FR-42 | Job order/time | Revise | DRV [Q5]; MGR [preferred Slot] | Manager-set order is supported. Define precise times versus Slots, travel/lunch treatment, overlap and overrun behaviour; the test covers order but not time (DEC-12/22/31). |
| FR-43 | Compare up to three Staff | Revise | Brief R4/R5; MGR [System Q3] | Fields and selected comparison are grounded. Resolve current versus selected Planning Week and scheduled-location aggregation/no-Job state (DEC-04/06/08/16). |
| FR-44 | Hard blocking rules | Revise | MGR [System Q4, Process Q3, Clarification Q8] | Retain the block/warn distinction. Define double booking, Certification validity and Slot coverage; apply agreed validation to Job edits, approvals and imports as well as allocation. |
| FR-45 | Overridable warnings | Hold | Brief §Company ¶4/R6; MGR [System Q4, Conflicts Q1]; DEC-19/32 | Hold Overtime approval scope and the minimum-Van exception/counting policy. A warning must not override FR-44's hard errors. |
| FR-46 | Unassigned list/count | Revise | MGR [Conflicts Q1, ranking follow-up] | Define count membership and exclusions. Use a specified unassignment event such as FR-29/63 in the test; distinguish Assignment removal from cancelling the Job. |
| FR-47 | Available unallocated Staff | Revise | MGR [standby follow-up] | Supported. Define whether freedom is per day/Slot and whether Crew membership without Jobs counts as assigned (DEC-03/10/39). |
| FR-48 | Replacement suggestions | Revise | MGR [staff-cancellation follow-up] | Specify Driver versus Technician eligibility, required Brand, available Van/Crew capacity, time window and ranking ties. Workload ordering depends on held calculations. |
| FR-49 | Publish roster | Revise | MGR [Process Q1, Conflicts Q1, notifications] | Define target week, Monday publication policy, draft visibility and revisions. Permit agreed warnings while refusing hard invalidity; define which Staff receive a publication with no Jobs. |
| FR-50 | Change published Assignments | Revise | MGR [Conflicts Q5, staff-cancellation follow-up] | Supported. Apply validation and update old/new Staff views, Workload, notifications and history consistently; distinguish current/future changes from historical corrections. |
| FR-51 | Van timeline | Retain | MGR [System Q2] | Explicitly supported view. Retain; show unavailable Vans clearly and make the displayed week explicit. |
| FR-52 | Planned hours/travel | Hold | MGR [Clarification Q7]; DCT [System Q1]; DEC-31 | Correctly held. Settle fixed allowance versus driving estimates and treatment of shared-address Jobs, initial/return travel and breaks before fixing the formula. |
| FR-53 | Staff hour attribution | Hold | MGR [Clarification Q5 follow-up, Q7]; DEC-39 | Correctly held. A Van-level Job link does not determine each Technician's hours on a two-Technician Crew; emergency transfers need consistent attribution. |
| FR-54 | Actual replaces planned | Hold | MGR [Clarification Q7, Conflicts Q5]; DCT [Conflicts Q3]; DEC-40 | Correctly held. Agree actual-time/travel/break calculation and correction behaviour; do not assume end minus start is the complete Workload formula. |
| FR-55 | Weekly >40 highlight | Retain | Brief R6; MGR [Clarification Q7, Conflicts Q5] | Strictly greater than 40 is correct; Monday–Saturday is interview-supported. Retain this threshold rule, while calculation and any approval workflow remain provisional. |
| FR-56 | Manager Landing Page | Revise | Brief R2/R6; MGR [landing-page follow-up, System Q2] | Supported visual elements. Correct pending-rejection semantics, define the default period, and disclose calculation dependencies rather than treating seeded totals as agreed results. |
| FR-57 | Lowest three per role | Hold | Brief R6; MGR [lowest-three follow-up]; DEC-05 | Hold adopted ranking interpretation, ties, fewer-than-three results and partial-week Leave exclusions. Preserve the stated brief minimum while resolving the role-list expansion. |
| FR-58 | Staff Landing Page/month | Hold | Brief R7; DCT [System Q2]; DRV [Q13/Q1]; DEC-04 | Hold monthly-period calculation. Define current versus newly published week selection and show coherent weekly/monthly hours using the agreed model. |
| FR-59 | Assignment information | Retain | DRV [Q1/Q2]; DCT [job-info follow-up] | Contents are supported. Retain; Crew names within one's Assignment do not automatically authorise access to colleagues' private schedules (DEC-37). |
| FR-60 | Manager monthly metrics | Revise | MGR [System Q1, ranking follow-up] | Supported additional views. Define month/date attribution, Completed-Job counting and Leave totals; dependencies on DEC-04/13/39/40 remain. |
| FR-61 | Monthly Van usage | Revise | MGR [System Q1, ranking follow-up] | Supported as nice-to-have. Define 'on the road': a Crew row alone is not proof of use when all Jobs were cancelled or the Van broke down. |
| FR-62 | Warn and reject Job | Revise | Brief R10/§Intro ¶3; MGR [Conflicts Q3, early rejection]; DCT [Process Q2]; DRV [Q17] | Warning and reasons are grounded. Define Other-comment requirements and repeated/late attempts; 48-hour notice is a preference, not a sourced hard rejection ban. |
| FR-63 | Rejection effects | Hold | MGR [Conflicts Q3]; DCT [after-reject follow-up]; DEC-15 | Hold the effect on remaining Crew members and Workload. Immediate no-approval rejection is supported, but 'only this Staff list' versus globally Unassigned must be reconciled. |
| FR-64 | Staff notifications | Revise | MGR [notifications/cancellations, Conflicts Q5]; DCT [updates, Conflicts Q2]; DRV [Q7] | Define recipient/channel per trigger and measurable timeliness, especially old/new Crews and approval decisions. Do not promise instant email using a one-minute data-refresh test. |
| FR-65 | Manager notifications | Revise | MGR [Conflicts Q3, landing-page follow-up] | Separate new rejection events awaiting reassignment from requests awaiting approval. Keep Manager email optional/TBC until sourced; specify notification dismissal/processing semantics. |
| FR-66 | Audit records | Revise | ITA [Audit] | Audit need is grounded. Remove the assumed viewer permission; agree actor access, event coverage and retention. Logging existence is different from an actor being able to retrieve history. |
| FR-67 | Schedule deletion rule | Hold | ITA [Retention]; DEC-34 | Hold the combined retention/departure/deletion policy. Specify authorised actors and distinguish physical deletion from cancellation, including audit-record survival. |
| FR-68 | Schedule CSV import | Hold | ITA [Existing systems]; DEC-36 | Correctly held. Confirm what the portal exports and how it relates to Manager-entered Jobs; define schema, duplicates and validation before adding an import use case. |

## 5. Individual review of all 17 Non-Functional Requirements

| ID | Verdict | Evidence | Finding / measurement needed |
|---|---|---|---|
| NFR-01 | Revise | ITA [Response time]; Brief R2 | Five seconds is one of the interview's suggestions, not a confirmed target. Agree percentile/failure budget, client/server measurement, network and data workload. The underlying Landing Page feature remains Must even if its performance target is Should. |
| NFR-02 | Revise | ITA [Response time] | Specify propagation/refresh mechanism and measurement conditions. 'Within one minute' sharpens 'less than a minute or so'; confirm the boundary and distinguish it from immediate rejection/change notifications. |
| NFR-03 | Revise | ITA [Concurrency]; Brief §Company ¶4 | The approximate 50 target is grounded. Define distinct users versus sessions, devices per person and operations/request rate; testing 50 sessions does not demonstrate 50 multi-device users. |
| NFR-04 | Revise | ITA [Concurrency] | Rate limiting is supported, but no rate/window/burst scope or recovery criterion is specified. Agree measurable values and behaviour; do not invent them as stakeholder facts. |
| NFR-05 | Revise | ITA [Hours, Outage]; DEC-38 | Separate service hours from uptime percentage and planned downtime. Define measurement interval, exclusions and actual maintenance windows; resolve the Thursday peak interpretation. |
| NFR-06 | Revise | ITA [Outage, Restore] | The one-day recovery scale is grounded. Define when recovery timing starts, which functions/data must be restored, the precise boundary and representative failure/restore conditions. |
| NFR-07 | Revise | ITA [Restore, Outage] | An hour of tolerable loss is supported as a draft target. Verify actual recoverable data age after failure; scheduled hourly backups alone do not prove it, especially after a failed backup. |
| NFR-08 | Revise | DCT [System Q3]; ITA [Outage, Connection failure] | Offline reading is explicit. DCT says updates can wait until back online; queued offline completion is stronger functionality. Confirm that scope, cached-date/freshness behaviour and reconnect conflict handling. |
| NFR-09 | Revise | ITA [Connection failure] | The source qualifies holding a submission with 'if possible'. Agree retry limits, failure indication and duplicate/conflicting submission outcomes, particularly for Leave approval, rejection and completion. |
| NFR-10 | Hold | ITA [Safeguards]; DEC-41 | Email confirmation is a supported suggestion. Hold all-login/new-device/role scope and recovery/remembered-session behaviour; represent authentication flow explicitly if adopted. |
| NFR-11 | Revise | ITA [Safeguards] | Backend encryption supports the intent, but define storage scope and verification of protected data at rest. A plaintext field inspection is not a complete encryption test. HTTPS and password controls remain separately sourced team proposals. |
| NFR-12 | Revise | ITA [Onboarding, Permissions]; DEC-17/18/37 | Correct the apparent blanket right to edit one's Assignments. Use an action-level permission matrix aligned with FR-17/23/39/41/50/62 and distinguish Crew-name visibility from access to colleagues' private records. |
| NFR-13 | Hold | ITA [Retention]; DEC-34 | 'Up to one year' was changed to 'at least one year'. Hold minimum/maximum period, age origin and departure/deletion treatment before choosing or testing a retention policy. |
| NFR-14 | Revise | ITA [Devices] | Named browser coverage is supported. 'Current versions' is moving scope: record the browser/version/OS matrix and acceptance flows for the milestone; no particular version is selected by this review. |
| NFR-15 | Revise | DCT [System Q3]; DRV [Q14]; ITA [Devices] | Mobile/tablet/laptop needs are supported. Agree representative viewport/device, zoom and task criteria. The 360-pixel example is a marked proposal, not a stakeholder requirement. |
| NFR-16 | Revise | MGR [Closing] | Simplicity is grounded but not measurable. Agree representative non-technical participants, tasks, success rate/time/help criteria; the three-minute example remains a proposal. |
| NFR-17 | Retain | Brief R1 | The browser-based constraint is explicit and testable. Retain; it does not settle whether M2 requires production implementation or a wireframe (DEC-21). |

## 6. A practical plan for approximately 20 use cases

The M1 rubric says **“All major use cases identified and formalized (name, actors, preconditions, main/alt flows, postconditions).”** It does not prescribe 20 use cases, 68 use cases or one use case per FR. Twenty is a planning target, not a reason to manufacture extra goals.

The numbers below are **local candidate labels**, not allocated `UC-nn` IDs. No formal use-case files or diagram elements have been created by this review. Check existing/reserved IDs before adoption. Source references show why each candidate exists; open DECs are dependencies, not approvals.

| Candidate | Goal | Primary actor | FR coverage | Evidence / decision link | Scope and cautions |
|---|---|---|---|---|---|
| 01 | Sign In / Recover Access | Staff, Manager, IT Administrator | FR-01, FR-02, FR-06, FR-07 | Brief R2/R7/R11; DRV Q1; ITA Passwords | Reset/initial password change are supporting flows; IT Administrator unlocking belongs to 03. Email 2FA awaits DEC-41. |
| 02 | Add Staff or Manager Account | IT Administrator | FR-02, FR-03 | Brief R11; ITA Account info/Permissions | Separate account creation from later role changes; keep mandatory field validation explicit. |
| 03 | Maintain Account Access | IT Administrator | FR-03, FR-04, FR-05, FR-07 | DEC-17/34; ITA Role change/leaver | Role changes and unlocking are supported. Departure/removal is a held variant until DEC-34. |
| 04 | Maintain Certifications | Actor TBC | FR-10, FR-11, FR-12 | Brief §Company ¶2/4; DEC-35; MGR Certification follow-up | Actor/permissions held. Expiry reminders are supporting timed behaviour; scan upload is Could. |
| 05 | Withdrawn calendar candidate | — | FR-09 (Withdrawn) | DEC-45 | No active goal; historical candidate label retired. |
| 06 | Set Availability | Staff | FR-13, FR-14, FR-16, FR-19 | Brief R8 as clarified; DEC-01/02/03/30 | Add/edit main flow; copy is optional. Cover lock, missing entry and month boundary alternatives. |
| 07 | Request Late Availability Change | Staff | FR-17 | Brief §Company ¶1; DEC-02; MGR Conflicts Q2 | Include first late submission, reason, pending state and existing Assignment conflict. |
| 08 | Handle Availability Exceptions | Manager | FR-17 (FR-18 Withdrawn) | DEC-02/13; DEC-45 | Review Late Availability Change Requests through the merged Manager request use case. |
| 09 | Set Weekly Job Preference | Staff | FR-21 | Brief R9/R5; DEC-07 | Advisory preferences; missing and late-edit cases still need agreement. |
| 10 | Request Leave | Staff | FR-22, FR-25 | Brief §Company ¶4; DEC-13 | Application with optional note; show balance and define invalid/overlapping request outcomes. |
| 11 | Review Leave Request | Manager | FR-23, FR-24, FR-25, FR-26 | DEC-13/19; MGR Process Q4 | Approve/reject with reason; update balance/Availability and handle existing Assignments. |
| 12 | Record Van Unavailability | Manager | FR-27, FR-28, FR-29 | Brief §Company ¶5; DEC-14; MGR Process Q3/Conflicts Q4 | Workshop and breakdown variants; FR-27 is reference data, not evidence for an unsourced fleet CRUD goal. |
| 13 | Maintain Job | Manager | FR-34, FR-35, FR-36, FR-37, FR-38 | DEC-11/22; MGR Process Q2/cancellations | Create, update and cancel need distinct flows/postconditions. Split them if necessary; do not use one create flow to claim all three are formalised. |
| 14 | Form or Change Van Crew | Manager | FR-30, FR-31, FR-32, FR-33, FR-44 | Brief §Company ¶2–4; DEC-09/10/19 | Normal daily formation and emergency change variants; enforce composition and qualification. |
| 15 | Allocate or Reassign Jobs | Manager | FR-41, FR-42, FR-43, FR-44, FR-45, FR-46, FR-47, FR-48, FR-50, FR-51 | Brief R3/R4/R5; DEC-10/16/19/32 | Comparison/suggestions/ordering support allocation. Separate initial allocation and published-change flows; blocked errors and warnings have distinct outcomes. |
| 16 | Publish Weekly Roster | Manager | FR-49, FR-51, FR-64 | Brief §Company ¶1; DEC-02/19; MGR Process Q1 | Specify week, visibility transition, warnings, hard-error refusal and notifications. |
| 17 | View Manpower Availability and Workload | Manager | FR-15, FR-20, FR-51, FR-55, FR-56, FR-57, FR-60, FR-61, FR-65 | Brief R2/R6/§Intro ¶4; DEC-04/05 | Landing Page and drill-down variants; monthly/Van metrics can remain optional. Calculations and ranking are provisional. |
| 18 | View Own Assignments and Workload | Staff | FR-25, FR-55, FR-58, FR-59 | Brief R7; DEC-04/37 | Current/published week, monthly total and Assignment details; offline reading is an alternative condition. |
| 19 | Reject Job | Staff | FR-62, FR-63, FR-64, FR-65 | Brief R10/§Intro ¶3; DEC-15 | Warning, cancel-at-warning, reason, confirmation, unassignment and notification. Crew cascade held. |
| 20 | Record Job Completion | Actor TBC: Technician or permitted Crew member | FR-39, FR-40, FR-54 | DEC-20/40; MGR/DCT completion follow-ups | Actual times, remark, follow-up flag and evidence. Actor, photo obligation and calculation await DEC-40. |

**Coverage outside standalone actor goals:**

- **FR-52/53/54/55:** Workload rules used by allocation, completion and views. “Calculate Workload” need not be a separate actor use case.
- **FR-64/65:** Notifications support the triggering use cases. Avoid counting each channel/trigger as an independent user goal.
- **FR-66/67:** Audit and deletion rules apply across mutating cases. An audit-inspection goal needs an agreed actor and retrieval permission before it is added.
- **FR-08/68:** Optional, held migration scope. If adopted, account/schedule import may justify one or two additional formal cases. Do not conceal them in manual account creation to keep the count exactly 20.
- **NFR-01–17:** Attach relevant acceptance constraints to these cases; performance or encryption does not automatically become an actor use case.

This covers all 68 FRs through actor goals, shared rules or explicitly conditional scope. It is acceptable to end with 19, 21 or 22 cases if that produces clearer, complete flows. In particular, large “Maintain” cases must document every included operation, or be split.

For each adopted case, use the repository template and add: precise trigger/actor, authoritative linked sources, preconditions, actor/system main steps, alternative and exception flows, success/failure postconditions, business-rule references, and relevant NFRs. Connect it to classes and sequence/activity diagrams in traceability.md. Do not invent class IDs merely to fill the matrix.

## 7. What decisions.md means, and whether every entry must be answered

**No: all 41 entries do not have to be answered before drafting proceeds.**

[decisions.md](decisions.md) is a question/decision register. It preserves the source ambiguity, who should resolve it, options, status and the eventual recorded decision. It is not a list of 41 extra system features, and “Open” does not always mean another interview is needed.

At this review snapshot, **DEC-01 is the only Decided entry; the other 40 remain Open**. SRS §6 summarises many interview answers, but explicitly leaves the decision statuses unchanged. A team member can record adoption of an already-evidenced answer after review; further elicitation is needed only when the evidence is insufficient or conflicting.

| When to address it | Entries | Practical action |
|---|---|---|
| Already settled | DEC-01 | Apply one month in advance. Do not reopen five weeks. |
| Before freezing Assignment, Crew and Workload behaviour | DEC-04/05/09/10/15/19/20/31/32/39/40 | Settle shared definitions once; reuse them in all affected requirements, cases and diagrams. Some portions already have clear interview answers. |
| Before finalising affected dates, inputs and permissions | DEC-02/03/07/08/12/13/14/16/17/18/22/30/35/37 | Review the recorded answers; close answered parts and retain specific residual questions. DEC-06's selected comparison and DEC-11's Job definition also have clear interview answers to adopt. |
| Before adopting removal, imports, delay reporting or 2FA scope | DEC-33/34/36/41 | Resolve the relevant feature or explicitly defer/withdraw it; do not build an assumed destructive or extra workflow. Retention still needs settlement if records are in scope. |
| For M1 report, WBS and stakeholder compliance in parallel | DEC-21/23/24/26/27/28/29 | Confirm implementation/prototype scope, report/template expectations, process-diagram examples, engagement dates and representative rules where they affect this milestone. These need not stop the core SRS critique. |
| Later design/verification detail | DEC-25/38 and remaining detailed acceptance questions | Resolve when the affected artefact is prepared; avoid pretending the issue is already settled. Peak assumptions still need agreement before load verification. |

An entry can contain an answered part and an unresolved part: DEC-04 has a supported weekly threshold but an open monthly period; DEC-03 has half-day granularity but unknown defaults/deletion. Write the outstanding question precisely instead of reopening the whole topic.

If a decision changes a retained minimum feature, it must be settled before that behaviour is presented as final. Optional Could/Should features can be explicitly deferred; preserve their IDs and record their disposition. Appendix A says **“All engagements (in-person, email, virtually) must end by Week 6 of the trimester.”** Do not plan late stakeholder interviews beyond that permitted window.

The review does not resolve any DEC on the team's behalf. Suggested choices and missing acceptance rules are proposals, not new stakeholder facts.

## 8. Rubric readiness and next actions

| Rubric expectation | Current assessment |
|---|---|
| FRs: “Clear, complete, consistent, and well-structured list.” | Structure is good; permission/state/Workload inconsistencies and unresolved rules prevent a full pass. |
| FRs: “Requirements are specific, testable, and cover all key system features.” | All initial features are mapped. Several acceptance notes are incomplete or add assumptions; key formula tests remain held. |
| NFRs: “Comprehensive and realistic (performance, usability, security, etc.).” | Broad coverage is good. Feasibility of 24/7, recovery, offline updates and email authentication needs agreed scope. |
| NFRs: “Each requirement measurable and justified.” | Not yet met: TBCs and missing measurement contracts remain; NFR-13 alters its source. |
| Major formal use cases and aligned diagrams | About 20 goal groups are available, but formal cases/diagrams and populated traceability do not yet exist. |
| Elicitation process and stakeholder involvement | Transcripts are useful; actual representative count, attendance and provenance remain undocumented. |
| M2 alignment/testing/wireframe | FR-32/44 offer meaningful decision-table candidates. Confirm rules first. White-box scope still needs pseudocode/CFG with the rubric's at least eight nodes and two decision points; no such artefact is claimed here. |

**Recommended order under time pressure:**

1. Correct NFR-12's action permissions, flag NFR-13's changed qualifier, and agree one consistent Assignment/Workload/rejection model. Keep affected acceptance criteria visibly provisional until decisions are recorded.
2. Close already-answered high-impact DECs with exact transcript evidence; ask only the residual questions. Resolve the one-month/monthly-period boundaries and brief interpretations.
3. Fix the per-row issues in sections 4–5. Preserve IDs; do not silently renumber, delete or declare all rows Agreed. Confirm MoSCoW priorities: only the initial brief capabilities are automatically minimum deliverables, not every interview addition.
4. Formalise the candidate use cases and diagrams from the retained scope, then populate traceability. Treat comparison, validation, calculations and notifications as supporting behaviour where appropriate.
5. Complete representative/attendance records, the approved citation scheme and the AI declaration. Record the team's actual changes on top of both AI drafts.

**Final verdict:** The Claude-assisted SRS is a substantial starting point with good feature coverage. It needs targeted revision and decision closure, especially around its central domain model and test criteria. It can support approximately 20 use cases; it cannot yet be certified as an agreed, fully compliant SRS.

## 9. Review boundaries

This report is a critique, not a replacement specification. The original requirements, binding briefs, transcripts, decision entries and traceability scaffold were not edited. The only other intended repository change is an appended AI-usage row recording this requested review, with human adoption still pending.

No code, use cases or diagrams were authored, and no requirements were approved. No commits, pushes or PRs were made. Review recommendations must be adopted by the appropriate file owners and reviewed through the team's normal process.
