# Sequence Diagram Review: SD-01 to SD-16

**Reviewed:** 16 rendered SVGs (PlantUML 1.2026.8), checked against SRS v3.3 (`requirements.md`), UC-01 to UC-15, the brief and rubric M1.
**Reviewer:** Claude Opus 5.5 (AI critique only; the team decides and owns every fix, per AGENTS.md rule 1).
**Date:** 2026-10-04

## Verdict

**Usable for M1 once the blockers are fixed.** All 16 diagrams use correct basic UML: BCE lifelines, synchronous calls with dashed returns, `«create»`, guarded alt/opt/loop fragments, `ref` and numbered messages. Every use case has a diagram. These are the problems a marker would notice:

| # | Severity | Issue | Diagrams |
|---|---|---|---|
| B1 | **Blocker** | The diagrams cite DEC-48, 49, 51 and 52, which are not yet in `decisions.md` | SD-03, 09, 12, 15 |
| B2 | **Blocker** | Logic error: after the "refuse" step, the flow carries on anyway | SD-09 |
| B3 | **Blocker** | FR-64 breach: a valid edit to an Assigned Job does not notify the Crew | SD-05 |
| M1 | Major | The Assignment is saved before the Manager confirms the warnings, and there is no cancel path | SD-07 |
| M2 | Major | Workshop Servicing ignores Crews that already exist on that date, and the old date is never freed | SD-06 |
| M3 | Major | FR-66 audit coverage is uneven: some changes are logged and others are not | SD-05, 06, 07, 12, 16 |
| M4 | Major | `ref` fragments cover lifelines the referenced diagram does not use, and the trigger message is missing | SD-05, 06, 07, 09, 10, 11 |
| M5 | Major | SD-07, SD-09 and SD-12 are too large to read on an A4 report page | SD-07, 09, 12 (also 14) |
| m1–m10 | Minor | Notation polish (listed below) | various |

---

## Blockers

### B1. Citations to unrecorded decisions
| Diagram | Text | Missing |
|---|---|---|
| SD-03 legend | "Initial login details are emailed (DEC-49)" | DEC-49 |
| SD-09 legend | "SD-16 handles them (FR-70, DEC-51)" | DEC-51 |
| SD-12 note | "less than 48 h (DEC-52)" | DEC-52 |
| SD-15 legend | "Phone channel = SMS (DEC-48)" | DEC-48 |

AGENTS.md rule 2 says items without a source "are flagged, not merged". **Fix:** merge `CL/diagram-review-fixes` (DEC-48 to DEC-50), then add DEC-51 (FR-70 is the later-event exception to FR-44), DEC-52 (Short notice is under 48 h; exactly 48 h is normal) and DEC-53 (BCE lifelines; boundary and control classes are added to the CD). Do this **before** the SD PR. These are conditions C1 to C3 in `sequence-diagrams.md`.

### B2. SD-09: rejecting Leave without a reason does not stop the flow
Steps 8 and 9 read `opt [no reason given] → refuse until a reason is entered (FR-23)`, followed by an unconditional `reject(reason)` and an audit record. As drawn, the system refuses and then rejects anyway.
**Fix:** use `alt [no reason given] → refuse / else [reason given] → reject(reason)`, with the audit `record` inside the `else`.

### B3. SD-05: Crew not notified of a valid change
`ref SD-15 Notify Staff (Crew told of the change)` is inside `opt [edit breaks a rule]`. FR-64 says Staff are notified when one of their Assignments is "added, changed, cancelled…". An edit that keeps the Job Assigned (for example, a new start time) currently tells nobody.
**Fix:** move the SD-15 `ref` out of the inner `opt` so that it covers the whole `opt [Job is Assigned]` path. Use one message for "changed" and another for "made Unassigned".

---

## Major

### M1. SD-07: Assignment saved before the warning override
Order: `«create» Assignment (24)` → `markAssigned (25)` → `checkWarnings (26)` → `opt [warnings raised] → overrideWarnings (31)`. FR-45 requires the system to "warn, allow an override and log it". If the Manager declines, the Assignment already exists and there is no undo branch.
**Fix (choose one):**
- (a) Move `checkWarnings` before `«create»`, using `alt [warnings] → show → alt [override] create + record / [cancel] nothing saved`.
- (b) Keep the current order but add `[Manager cancels] → Assignment deleted, Job back to Unassigned`.

Option (a) is cleaner. Also add a note or self-call for FR-36: allocating one Linked Job places its linked Job on the same Van and date, or the allocation is blocked. That rule is not shown anywhere at the moment.

### M2. SD-06: Workshop Servicing vs existing Crews
FR-28 says "the Van is unavailable all that day". `generateServicing` and `adjust` call `markUnavailable(date)` on the Van, but unlike the breakdown branch they never release Crews or unassign Jobs that are already on that date. `adjust` also never frees the old date.
**Fix:**
- After `markUnavailable(newDate)`, add `markAvailable(oldDate)`.
- Add `opt [Crews already exist on the date]`, which either reuses the FR-29 release loop or blocks with a warning. The team needs to pick one and record a DEC, because the SRS is silent on this.
- Guard generation with `opt [month not yet generated]`. As drawn, every `openServicing(month)` creates the servicing records again.

### M3. SD-05, 06, 07, 12, 16: FR-66 audit gaps
FR-66 requires logging of "every change to Availability, Crews, Assignments, Jobs and Leave". The diagrams log some of these changes but not others:

| Missing `record(...)` | Diagram |
|---|---|
| Crew created, Standby named, Assignment created | SD-07 (only overrides and publication are logged) |
| Jobs linked | SD-05 |
| Crews released and Jobs unassigned by a breakdown | SD-06 |
| Leave Request / Late Change / Job Rejection submitted | SD-12 |
| Person removed from a Crew | SD-16 |

**Fix:** add one `record(actor, event)` to `:Audit Log` in each of these places. A marker comparing the diagrams with FR-66 will notice the gaps.

### M4. SD-05, 06, 07, 09, 10, 11: `ref` and gate mismatch
In UML, an interaction use must cover the lifelines that the referenced interaction uses. These do not:
- SD-15 uses `:NotificationService`, `:Notification` and `Email/Phone`, yet the callers' `ref SD-15` boxes span controllers and entities, and none of those lifelines appear in them.
- SD-16 uses `:RosterController`, `:Crew` and `:Standby`. In SD-09 and SD-10 there is no `:RosterController`, and nothing calls `handleCrewInvalidation(...)`.
- SD-11 refs SD-12, which uses `:RequestPage` and `:RequestController`, neither of which is in SD-11.

**Fix (the simplest valid form):** in each caller, add the first lifeline of the referenced diagram and draw the gate message to it. Then place the `ref` over that lifeline only. Examples:
- `RC -> NS : notify(event, recipients)` followed by `ref over NS : SD-15 Notify Staff`
- `ReqC -> RC : handleCrewInvalidation(staff, dates)` followed by `ref over RC : SD-16`

### M5. Size and readability
| Diagram | Rendered size | Problem |
|---|---|---|
| SD-07 | 2464 × 3604 | 9 lifelines, 48 messages; unreadable at A4 |
| SD-09 | 2840 × 2834 | 11 lifelines, three request types in one diagram |
| SD-12 | 2793 × 2425 | three request types in one diagram |
| SD-14 | 2550 wide | caused only by the long `enter(...)` and `complete(...)` labels |

The rubric asks for "clear lifelines, messages, and ordering". **Fix:**
- **SD-07:** split into SD-07a (Form Crews and Standby), SD-07b (Allocate Job) and SD-07c (Publish). Alternatively, move the publish block into a `ref`.
- **SD-09 and SD-12:** keep the top-level `alt`, but make each branch a `ref`, or create one diagram per request type.
- **SD-14:** shorten the labels to `enter(completionDetails)` and `complete(details)`, and give the field list in a note.

New IDs are allowed. Do not reuse SD-16; use SD-17 onwards or the a/b/c suffixes, and record the split in a DEC.

---

## Minor (polish, worth doing if time allows)

| # | Diagram | Issue | Fix |
|---|---|---|---|
| m1 | SD-01 | The lockout is only a note on `:Account`, so no message shows it | Add `recordFailedAttempt()` and `lock()` messages, plus an audit `record` for the lockout |
| m2 | SD-01 | The locked/inactive check comes after `checkCredentials` | Check status first (no password check against a locked account), or confirm the order matches UC-01 |
| m3 | SD-02 | The return is labelled `valid` but feeds an `alt` with two outcomes, and the token is never invalidated after use | Label it `valid / invalid`; add `invalidateToken()` and `record(user, password changed)` after `setPassword` |
| m4 | SD-03 | `«create»` on `newUser:User` while the legend says User is abstract | Name the lifeline after the concrete class, e.g. `newUser:Technician`, or add the note "concrete subclass per role" |
| m5 | SD-03, 04 | `checkAuthority()` has no refused branch | Add `opt [not IT Administrator] → refuse (NFR-12)` once, or state in the legend that it is covered by NFR-12 |
| m6 | SD-08, 11 | One message with alternatives in its label (`selectStaff() or close()`, `setSlot / setWholeDay / clear`) | Use an `alt`, or keep a single generic message (`editSlot(...)`) |
| m7 | SD-09 | `reject()` and `refuse()` take no argument, although `decideRequest` carries a reason; Late approval does `setState` once for many Slots | Pass `reason` through; wrap `setState` in `loop [for each Slot]` |
| m8 | SD-10 | `opt [a Crew is no longer valid]` has no check before it | Add the self-call `checkCrewsUsing(technician)` |
| m9 | SD-15 | `Email/Phone` is one lifeline, while SD-01 to SD-03 use `Email Service`; the 3 retries (NFR-09) are not shown | Split into `Email Service` and `SMS Gateway`; add `loop [up to 3 retries while failed]` |
| m10 | all | Boundary lifelines have no activation bars, and the `«create»` messages are drawn solid | Optional: add `activate` on pages; draw create messages as dashed open arrows (UML 2.5) with `-->>` |

---

## Checked and correct (no change needed)

- **SD-04:** removing future Assignments and making those Jobs Unassigned on a role change or deactivation matches **FR-04 and FR-05** exactly. It is right that it differs from SD-16, because FR-70 covers only Leave, Late Change and Certification expiry.
- **SD-06:** the breakdown branch (release Crew, unassign incomplete Jobs, notify) matches **FR-29**. The Sunday-to-Monday rule matches **FR-28**.
- **SD-09:** an approved Job Rejection unassigns the Job from the whole Van and increases the Unassigned count by 1, as **FR-46** requires. A request that lapses when the Job starts is covered (FR-63).
- **SD-13 and SD-14:** the offline paths (NFR-08), the Technician-only completion check (FR-39), and Actual Hours replacing Planned Hours (FR-53) are correct.
- **SD-16:** removes the person, marks the Van-day Needs attention, keeps the Jobs on the Van, and notifies the person and the Standby. This matches **FR-70** word for word.
- **SD-02:** the generic reply satisfies FR-06; the salted hash satisfies NFR-11.
- Titles follow `SD-nn: Name (UC-nn)`. SD-16 uses `(FR-70)` instead; list it in `traceability.md` as a shared fragment with no UC.

## Before the PR
1. Fix B1 to B3, then M1 to M5.
2. Fill the UC→SD column in `traceability.md`, plus a row for SD-16 and any split diagrams.
3. Add the boundary and control classes and the new operations to the CD in the **same PR**, so the CD and SDs agree (rubric: "no contradictions across artifacts").
4. Re-render locally with PlantUML. Do not use a public render server (AGENTS.md rule 5).
5. Add an `ai-usage-log.md` row: date, member, "Claude Opus 5.5: SD review", and what the team changed.
