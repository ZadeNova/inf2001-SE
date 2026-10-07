# Sequence Diagram Review, Round 2: SD-01 to SD-25

**Reviewed:** 22 rendered SVGs (PlantUML 1.2026.8): SD-01 to 06, SD-08, SD-10, SD-11 and SD-13 to SD-25.
**Checked against:**
- the SRS v3.3 (`requirements.md`) and UC-01 to UC-15;
- `brief/project-description.md` and `brief/rubric-m1.md`;
- `AGENTS.md`, and `decisions.md` as it stands on `main` (it stops at DEC-47).

**Reviewer:** Claude Opus 5.5. This is AI critique only; the team decides and owns every fix (AGENTS.md rule 1).
**Date:** 2026-10-04 (replaces the round-1 review)

---

## 1. Verdict

**Good. This is now an A-grade set, once the one remaining blocker and six Major findings are fixed.**

Since round 1, 2 of 3 blockers, all of the old Major findings except one, and all 10 minor items are resolved:
- **Big diagrams split:** UC-07 is now SD-17/18/19, UC-09 is SD-20/21/22 and UC-12 is SD-23/24/25.
- **UML is now correct:** `«create»` messages are dashed, activations sit on boundaries, and gates go to `:NotificationService` and `:RosterController`.
- **Main paths are complete:** every main path has an atomic save, an NFR-09 failure path and an FR-66 audit record.

What is left is mostly consistency between diagrams, plus two behaviours driven by time that no diagram shows.

| # | Severity | Finding | Diagrams |
|---|---|---|---|
| B1 | **Blocker** | The diagrams cite DEC-48, 49, 51, 52, 54 and 56; none of them exists on `main` | SD-02, 03, 06, 15, 16, 25 |
| M1 | Major | Draft-week changes notify Staff in some diagrams and not in others (FR-49) | SD-05, 06, 16 vs SD-17, 18 |
| M2 | Major | Time-triggered events are claimed in legends but never drawn (FR-63 lapse, FR-70 expiry) | SD-10, 16, 22 |
| M3 | Major | Leave approval never re-checks the balance, so 7 days can be exceeded (FR-22, FR-25) | SD-20 |
| M4 | Major | Crew invalidation runs after the approval commits, in a separate transaction | SD-20, 21 |
| M5 | Major | Two `ref` fragments cover too few lifelines | SD-01→02, SD-17→08 |
| M6 | Major | SD-07, 09 and 12 are no longer supplied, and their status is not recorded | traceability |
| M7 | Major | Deactivating a user or changing their role leaves them inside future Crews | SD-04 |
| m1–m12 | Minor | Readability and polish | various |

---

## 2. Fixed since round 1 (verified in the new renders)

| Round-1 item | Status | Evidence |
|---|---|---|
| B2: Leave rejected even when refused | ✅ Fixed | SD-20 uses `alt [reason missing] / [reason supplied]` |
| B3: valid Job edit sends no notification | ✅ Fixed | SD-05 uses `alt [made Unassigned] / [remains valid]`, both followed by SD-15 |
| M1: Assignment saved before warnings confirmed | ✅ Fixed | SD-18: `confirmWarningChoice` comes before the atomic save, and a cancel branch exists. FR-36 is handled by `expandLinkedJobs` |
| M2: Workshop Servicing conflicts | ✅ Fixed | SD-06: generation is guarded, existing Crews block the date (DEC-54), and the old date is freed by `markAvailable(oldDate)` |
| M3: FR-66 audit gaps | ✅ Fixed | Recorded in SD-05 (link), 06 (release), 16 (member removed), 17 (Crew/Standby), 18 (Assignment), 23/24/25 (submissions) |
| M4: ref gates | ◑ Mostly fixed | Gate messages to `:NotificationService` and `:RosterController` are now drawn. Two scoping errors remain (M5 below) |
| M5: diagram size | ✅ Fixed | Splits made; SD-14 labels shortened |
| m1–m10 | ✅ Fixed | Lockout messages, status checked before password, token invalidated, concrete-subclass note, authority branches, `alt` instead of "or" labels, `loop` over Slots, `checkCrewsUsing`, separate Email Service and SMS Gateway with retries, dashed `«create»` |

---

## 3. Blocker

### B1. Decisions cited in the diagrams do not exist yet
`decisions.md` on `main` ends at **DEC-47**, but the diagrams cite later decisions:

| Cited | Where |
|---|---|
| DEC-48, DEC-56 | SD-15 legend; SD-02 legend (DEC-56) |
| DEC-49 | SD-03 legend |
| DEC-51 | SD-16 legend |
| DEC-52 | SD-25 legend |
| DEC-54 | SD-06 note and legend |

AGENTS.md rule 2 says items without a source "are flagged, not merged".

**Fix, before the SD PR:**
1. Merge `CL/diagram-review-fixes` (DEC-48 to DEC-50).
2. Append DEC-51 to DEC-56 as rows, in ID order. DEC-53 (the BCE lifelines and extra CD classes) and DEC-55 are not cited anywhere. Either record and cite them, or state what they are.
3. Some legends say an item "remains open": SD-02 (token lifetime and password complexity) and SD-15 (acknowledgement and deduplication). Each of these should be an **open** DEC entry that the legend cites. Do not leave the text free-standing.

---

## 4. Major

### M1. Notifications for Draft weeks are inconsistent (FR-49)
FR-49 says *"Staff see Assignments only after publication."* SD-17 and SD-18 follow it correctly, with `opt [week already Published] → notify`. These diagrams notify without that guard:
- **SD-05:** the edit and cancel branches notify the Crew whenever the Job "was Assigned". That includes a Draft week.
- **SD-06:** the breakdown branch notifies the released Crew members for any date.
- **SD-16:** notifies the removed person and the Standby. It is also reached from SD-10, SD-20 and SD-21, which can hit Draft weeks.

The result is that Staff could be told about an Assignment they are not allowed to see.

**Fix:** wrap each `notify(...)` in `opt [affected week Published]`, as SD-17 and SD-18 already do. Alternatively, put the rule once inside SD-15 as an `opt [week Published or event not roster-related]`, and say so in its legend.

### M2. Time-triggered behaviour is promised but not drawn
Two requirements depend on the clock, not on a user action:
- **FR-63:** a Job Rejection Request "still pending when the Job starts" lapses. SD-22 lapses it only when the Manager opens it. Its legend says an *"independent Job-start event"* does it, but no diagram shows that event.
- **FR-70:** a Certification **expiry** invalidates a Crew. SD-10 only handles a Manager *editing* a Certification. A Certification that expires overnight never triggers SD-16.

A marker checking "all key behaviour represented" will see that these legends promise something no diagram shows.

**Fix:** add one small diagram, **SD-26: Run Scheduled Checks**. It starts with a found message from a «system» `Clock` actor and contains two parts:
- `loop [each Pending Job Rejection Request whose Job has started]`: `lapse()` → `record` → notify the requester.
- `loop [each Certification expired today]`: `checkCrewsUsing` → `handleCrewInvalidation` → `ref SD-16`.

Add a DEC for the schedule (for example, every 15 minutes and at 00:00), and cite SD-26 from the SD-16 and SD-22 legends.

### M3. SD-20: Leave approval can exceed 7 days
FR-22 checks the balance only at **submission**, and FR-25 deducts the days at **approval**. Two pending, non-overlapping requests can each fit the balance on their own, for example 4 days and 4 days against a balance of 7. As drawn, SD-20 approves both, and the balance goes negative. Round 1's SD-09 had a `leaveBalance(year)` call on the approve path; the split dropped it.

**Fix:** in the `[still Pending]` branch, before `approve()`, add `RC → requester:Staff : leaveBalance(year)` and `alt [days > remaining] → refuse "insufficient balance"`. Optionally, SD-23 can also count pending days when it validates a new request.

### M4. SD-20 and SD-21: Crew invalidation is not part of the approval transaction
The approval is saved inside `atomic approval save`, and `handleCrewInvalidation(...)` (SD-16) runs afterwards in a separate `opt`. If SD-16 fails, the Leave or late change is approved, but the person is still in the Crew, and FR-24/FR-70 are broken.

**Fix (choose one):**
- (a) Move the `handleCrewInvalidation` call and its `ref SD-16` inside the atomic box, and send only the notifications after the commit.
- (b) Keep the current order, but add a legend line that SD-16 retries under NFR-09 and that the Van-day stays flagged until it succeeds.

Option (a) is cleaner and matches SD-18.

### M5. Two `ref` fragments cover too few lifelines
In UML, an interaction use must cover **every lifeline in the enclosing diagram** that the referenced interaction uses.
- **SD-01 → SD-02:** `ref SD-02` covers only `:LoginPage`. SD-02 also uses User, `:AuthController`, `:Account`, `:Audit Log` and Email Service, and all of these are present in SD-01.
  - **Fix:** `ref over User, LP, AC, Acc, AL, Email : SD-02 Reset Password`.
- **SD-17 → SD-08:** `ref SD-08` covers only `:RosterController`. SD-08 also uses the Manager and `:JobAllocationPage`, because the comparison is shown and chosen there. SD-08 also returns "selected Staff / closed" through a right-hand gate, after the Page and Manager have already finished.
  - **Fix:** in SD-08, make the entry a gate into `:JobAllocationPage` (Manager → Page → RC), and end with the return to the Page. In SD-17, put the `ref` over Manager, Page and RC.

### M6. SD-07, SD-09 and SD-12 are missing, with no recorded status
The UCs are covered by the splits (UC-07 → SD-17/18/19, UC-09 → SD-20/21/22, UC-12 → SD-23/24/25), but the old IDs are simply missing. AGENTS.md says IDs are *"never reused or renumbered"*, and dropped items keep their row.

**Fix (choose one):**
- (a) **Recommended.** Keep SD-07, SD-09 and SD-12 as **overview** diagrams that only `alt`/`loop` across `ref SD-17/18/19` (and so on). This gives the report one entry diagram per UC, and it is quick to read.
- (b) Mark them `Status: Withdrawn (split into SD-xx)` in `traceability.md`, and record the split in a DEC.

### M7. SD-04: a deactivated user stays in future Crews
FR-04 and FR-05 are met: future Assignments end and the Jobs become Unassigned. But the person is never removed from their future **Crews**. A deactivated Driver therefore remains the Driver of a Van-day, and the Crew record is invalid. The other Crew members also silently lose those Jobs.

**Fix:**
- Inside the deactivation loop, and the role-change loop, add `loop [each future Crew of user] → :Crew.removeMember(user)`, followed by `record(...)`.
- After the commit, notify the affected Crew members through SD-15, guarded by M1.
- Log a DEC covering whether the Van-day also becomes "Needs attention". Reusing SD-16 would be the most consistent choice.

---

## 5. Minor (polish for the A)

| # | Diagram | Issue | Fix |
|---|---|---|---|
| m1 | all | Lifeline names wrap onto two lines (`:Job` / `Page`, `:Rule` / `Validator`), so they read as "Job Page" rather than the CL name `JobPage`. Message labels also wrap onto 3 to 5 lines (`record(` / `Manager,` / …). This is what makes SD-05 3,953 px and SD-20 3,045 px tall | Raise `skinparam maxMessageSize` to about 300, and stop participant names wrapping (`skinparam wrapWidth 300`). Re-check the heights afterwards; if SD-05 is still too tall, split it into Create/Link and Edit/Cancel |
| m2 | SD-06 | Message 11, "block date; show warning", is a **return** sent in the middle of the loop, which ends the controller's activation while the loop carries on | Use a self-call `recordConflict(van, date)` and keep the single return at message 15 |
| m3 | SD-16 | The `:Standby` lifeline receives no messages | Make it `RC → :Standby : findEligible(date)`, or remove the lifeline |
| m4 | SD-01 | No branch for a wrong or expired 2FA code. `refuse(reason)` for a missing account could reveal whether an account exists | Add `alt [code invalid] → refuse`. Show the same generic message for missing, locked and inactive accounts |
| m5 | SD-03 | `sendInitialLogin` can return `failed` and nothing happens, so the account exists but the user never gets their credentials | Add `opt [email failed] → warn the IT Administrator; offer resend` |
| m6 | SD-05 | Link Jobs has no validation branch for FR-36 (same Brand, different address, or already placed on a different Van or date) | Add `checkLinkable` followed by `alt [invalid] → refuse` |
| m7 | SD-11 | When the week is locked, the page opens the late-change form with no action from Staff. `setState` assumes an entry exists, but a blank Slot has none (FR-13) | Add `Staff → page : requestLateChange()`. In the set branch, use `«create» :Availability` if absent |
| m8 | SD-20 | Two consecutive `opt`s ("save fails" and "saved") are mutually exclusive. Approval should make the Staff member unavailable (FR-24), but no message shows it | Merge them into one `alt`. Add a note or call that Leave days count as Unavailable |
| m9 | SD-22, SD-25 | `lapse()` is neither recorded nor notified. `«create»` in SD-25 doesn't show the Short-notice flag. No check prevents a second pending request for the same Assignment | Add a `record` and a notify for lapse. Pass `shortNotice` to the create. Add a duplicate check inside `isEligible` |
| m10 | SD-23, SD-25 | Message 1 is a gate, but no diagram references these SDs, and the legend says "Staff navigation" | Draw the message from the Staff actor, or add `opt [request rejection] → ref SD-25` to SD-13's Assignment details |
| m11 | SD-13 | `isPublished()` returns true/false for the current week, but there is no branch for a Draft current week | Add `alt [current week Draft] → show "not yet published"` |
| m12 | SD-10 | Alerts are handled through the `:Notification` entity, but "Needs attention" and Unassigned-count alerts are not Notifications | Either model alerts as Notifications in the CD, or add an `Alert` class (DEC + CD) |

---

## 6. Per-diagram status

| SD | UC | Status | Open items |
|---|---|---|---|
| 01 Log In/out | UC-01 | ✅ after fixes | M5, m4 |
| 02 Reset Password | UC-02 | ✅ after fixes | B1 (DEC-56), open items → DEC |
| 03 Create User Account | UC-03 | ✅ | B1 (DEC-49), m5 |
| 04 Manage User Access | UC-04 | Fix | M7 |
| 05 Manage Job | UC-05 | Fix | M1, m1 (height), m6 |
| 06 Manage Vans and Workshop Servicing | UC-06 | ✅ after fixes | B1 (DEC-54), M1, m2 |
| 07 / 09 / 12 | UC-07/09/12 | Missing | M6 |
| 08 Compare Staff | UC-08 | Fix | M5 |
| 10 View Manpower Dashboard | UC-10 | ✅ after fixes | M2, m12 |
| 11 Set Availability and Preferences | UC-11 | ✅ | m7 |
| 13 View My Assignments and Workload | UC-13 | ✅ | m11 |
| 14 Complete Job | UC-14 | ✅ Clean | none |
| 15 Notify Staff | UC-15 | ✅ | B1 (DEC-48/56) |
| 16 Handle Invalidated Crew | FR-70 | ✅ after fixes | B1 (DEC-51), M1, m3 |
| 17 Form Crews and Standby | UC-07 | ✅ after fixes | M5 |
| 18 Allocate Job | UC-07 | ✅ Clean | none |
| 19 Publish Weekly Roster | UC-07 | ✅ Clean | none |
| 20 Decide Leave Request | UC-09 | Fix | M3, M4, m8 |
| 21 Decide Late Availability Change | UC-09 | Fix | M4 |
| 22 Decide Job Rejection Request | UC-09 | ✅ after fixes | M2, m9 |
| 23 Submit Leave Request | UC-12 | ✅ | m10 |
| 24 Submit Late Availability Change | UC-12 | ✅ Clean | none |
| 25 Submit Job Rejection Request | UC-12 | ✅ | B1 (DEC-52), m9, m10 |

---

## 7. Rubric M1 alignment ("all key use cases represented with correct UML interactions… clear lifelines, messages, and ordering")

| Criterion | Assessment |
|---|---|
| All key UCs represented | ✅ UC-01 to UC-15 all have at least one SD. M6 restores one entry diagram for each split UC |
| Correct UML interactions | ✅ Synchronous and return messages, dashed `«create»`, guarded `alt`/`opt`/`loop`, `ref` with gates, and execution specifications are all correct. Two ref scopes need fixing (M5) |
| Clear lifelines | ◑ BCE naming is consistent, but wrapped names blur the CL- names (m1) |
| Clear messages and ordering | ✅ Autonumbered. Validation happens before mutation, mutation before audit, and audit before notification. M4 is the one ordering gap |
| No contradictions across artifacts | ◑ M1 (FR-49), B1 (DEC references) and m12 (Alert vs Notification) are the remaining contradictions |

---

## 8. Before the PR
1. **B1:** merge the DEC branch and append DEC-51 to DEC-56, including the open-question entries.
2. Fix M1 to M7, then the cheap minors: m1 (skinparams), m2, m3 and m8.
3. In `traceability.md`, fill the UC → SD column, including SD-16 to SD-26 and the status of SD-07/09/12.
4. Update the CD in the **same PR**:
   - add the boundary and control classes;
   - add the new operations (`recordFailedAttempt`, `lock`, `invalidateToken`, `expandLinkedJobs`, `confirmWarningChoice`, `checkCrewsOn`, `markAvailable`, `lapse`, `changeMembers`, `retainGeneratedMonth`, `checkLockedWeekAndSlots` and so on);
   - add `Alert`, if you choose that option for m12.
5. Render locally only, never on a public PlantUML server (AGENTS.md rule 5). Commit the `.puml` files to `diagrams/` as `SD-nn-<slug>.puml`; `diagrams/` currently contains only its README.
6. Add an `ai-usage-log.md` row: the date, the member, "Claude Opus 5.5: SD review round 2", and what the team changed.
