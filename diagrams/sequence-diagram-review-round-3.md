# Sequence Diagram Review, Round 3: SD-01 to SD-25

**Reviewed:** 22 rendered SVGs (PlantUML 1.2026.8): SD-01 to 06, SD-08, SD-10, SD-11 and SD-13 to SD-25.
**Checked against:**
- `brief/rubric-m1.md`: OOA row, "Sequence diagrams for the use cases **with the identified classes**", needing "all key use cases represented with correct UML interactions" and "clear lifelines, messages, and ordering". The Formatting row also asks for "consistent terminology" and "strong alignment and traceability" across artefacts;
- `brief/project-description.md` and `brief/assessment-overview.md`;
- the SRS (`requirements.md`) and UC-01 to UC-15;
- `AGENTS.md`, and `decisions.md` as it stands on `main` (still stops at **DEC-47**; `git fetch` shows no other branch).

**Reviewer:** Claude Opus 5.5. This is AI critique only; the team decides and owns every fix (AGENTS.md rule 1).
**Date:** 2026-10-05. This replaces the round-2 review.

---

## 1. Verdict

**Very good. The diagrams themselves are now at A standard.** All six round-2 Major findings about diagram content are fixed, and so are 11 of the 12 minor items. What stands between this set and an A is mostly **repo paperwork** (B1, M6) plus **two cross-artifact consistency points** (M8, M9). A marker checking traceability would find all four.

| # | Severity | Finding | Diagrams | Status |
|---|---|---|---|---|
| B1 | **Blocker** | 11 DEC numbers are cited but none exists on `main`; DEC-58 is cited for three unrelated rules | 01–06, 10, 15, 16, 20, 22, 25 | ❌ Open, and larger |
| M6 | Major | SD-07, 09 and 12 are missing, and their status is not recorded | traceability | ❌ Open |
| M8 | Major (new) | The `«system» Clock` actor appears in SDs but not in the UCD or the UCs | SD-16, 22 | 🆕 |
| M9 | Major (new) | Unassigning one Linked Job leaves its partner on the Van (FR-36) | SD-05, 22 | 🆕 |
| m1 | Minor | Long labels still wrap; SD-05 and SD-20 are about 3,900 px tall | various | ◑ Partly fixed |
| m13–m22 | Minor (new) | Polish | various | 🆕 |

---

## 2. Fixed since round 2 (verified in the new renders)

| Round-2 item | Status | Evidence |
|---|---|---|
| M1: Draft-week notification inconsistent (FR-49) | ✅ Fixed | Fixed in one place: SD-15 `partitionByWeek` and `alt [roster event for a Draft week] suppressDraftDelivery`. SD-04/05/06/16 route through it, and SD-17/18 keep `opt [week already Published]` |
| M2: time events not drawn | ✅ Fixed | SD-16 `Clock → checkCertificationExpiry(today)`; SD-22 `Clock → onJobStart(assignment)` → `lapse()`, audit and notify |
| M3: Leave balance not re-checked | ✅ Fixed | SD-20 msgs 22–25: `leaveBalance(year)`, `validateLeave`, `alt [exceeds balance or overlap] → refuse`, all inside the atomic box |
| M4: Crew invalidation outside the transaction | ✅ Fixed | SD-20/21 call `ref SD-16` inside the atomic box; SD-16's caller branch says "joins the caller's atomic save"; delivery follows commit |
| M5: ref scope | ✅ Fixed | SD-01 `ref SD-02` now spans User→Email Service; SD-17 `ref SD-08` spans Manager→RosterController; SD-02/08/15/16/24 enter and leave through gates |
| M7: SD-04 leaves user in Crews | ✅ Fixed | `opt [deactivation or Staff becomes Manager]`: `removeMember`, `markNeedsAttention`, end Assignments, notify via SD-15. The guard matches FR-04/05 exactly |
| m2 mid-loop return (SD-06) | ✅ | `recordConflict` self-call with a note |
| m3 unused `:Standby` (SD-16) | ✅ | Removed |
| m4 invalid 2FA code (SD-01) | ✅ | `[confirmation code invalid or expired] → generic login failure; no session` |
| m5 email failure (SD-03) | ✅ | `opt [email failed]` → warn and offer resend |
| m6 FR-36 on link (SD-05) | ✅ | `checkLinkable` → `[same Brand, different address or conflicting placement] refuse` |
| m7 late change entry (SD-11) | ✅ | `opt [Staff requests a Late Availability Change] → ref SD-24`; `«create» new:Availability` for blank Slots (SD-11, SD-21) |
| m8 two opts (SD-20) | ✅ | One `alt [reject] / [approve]`; FR-24 note "Leave days count as Unavailable" |
| m9 lapse and short notice | ✅ | SD-22 lapse audited and notified; SD-25 `classifyShortNotice` (< 48 h) and `hasPendingRejection` |
| m10 unreferenced gates | ✅ | SD-23/25 legends state the entry point |
| m11 Draft current week (SD-13) | ✅ | `alt [current week Published] / [current week Draft]`, plus a next-week branch |
| m12 Alert vs Notification (SD-10) | ✅* | `alert:Notification` of kind DashboardAlert (DEC-63). *Depends on B1 |
| m1 wrapping | ◑ | Lifeline names are fixed (`:JobPage`, `:RosterController`). About 20 message labels still wrap (see m1) |

---

## 3. Blocker

### B1. Cited decisions do not exist on `main`
`decisions.md` on `main` still ends at DEC-47. The diagrams now cite:

| DEC | Used for | Where |
|---|---|---|
| DEC-48, DEC-56 | Email Service and SMS Gateway realise the Email/Phone actor; DEC-56 also covers single-use reset tokens | SD-15, SD-02 |
| DEC-49 | Initial login details use email | SD-03 |
| DEC-52 | Short notice is < 48 h; exactly 48 h is normal | SD-25 |
| DEC-54 | Blocked servicing dates are unbooked proposals | SD-06 |
| **DEC-58** | ① Draft roster delivery suppressed; ② Leave balance check serialized per Staff and year; ③ at most one Pending Job Rejection Request per Assignment | ① SD-04, 15, 17; ② SD-20; ③ SD-25 |
| DEC-59 | Clock checks: expiry at 00:00 after expiryDate; lapse at Job start | SD-10, 16, 22 |
| DEC-60 | Account cleanup flags Van-days Needs attention and unassigns Jobs | SD-04, 16 |
| DEC-61 *(open)* | Confirmation-code lifetime, token lifetime, password complexity | SD-01, 02 |
| DEC-62 *(open)* | Notification acknowledgement and deduplication | SD-15 |
| DEC-63 | Dashboard alerts are Notifications of kind DashboardAlert | SD-10 |

**What to do:**
1. Merge the branch that holds DEC-48 onward, or append these entries now. Each one needs a source: MTG, INT or Brief (AGENTS.md rule 2).
2. **DEC-58 is cited for three unrelated rules.** Either it really is one combined "SD review round 2" decision (then say so in its title and list all three rules), or split it into three DECs and re-cite. One ID per decision reads far better in traceability.
3. DEC-50, 51, 53, 55 and 57 are never cited. If they exist, fine. If they don't, there is no problem, because IDs are only reserved once they are written.

---

## 4. Major

### M6. SD-07, SD-09 and SD-12 are still missing (open from round 2)
UC-07 is drawn as SD-17/18/19, UC-09 as SD-20/21/22 and UC-12 as SD-23/24/25. That coverage is complete, but the ID gap looks like missing work to a marker. **Cheapest fix (no new diagrams):** add rows to `traceability.md`:

```
SD-07 | UC-07 | Status: Withdrawn — split into SD-17, SD-18, SD-19 (DEC-xx)
SD-09 | UC-09 | Status: Withdrawn — split into SD-20, SD-21, SD-22 (DEC-xx)
SD-12 | UC-12 | Status: Withdrawn — split into SD-23, SD-24, SD-25 (DEC-xx)
```
Add one DEC entry for the split. Also add a one-line note in the report's SD section, for example "UC-07 is shown in three diagrams: SD-17 to SD-19."

### M8. `«system» Clock` is an actor that the UCD and UCs don't have (new)
SD-16 and SD-22 draw the Clock as an actor stick figure. The UCD and UC-09 list no time or clock actor, and FR-70 has no UC at all. A marker checking "alignment between requirements, use cases, diagrams" will see a new actor appear from nowhere.

Choose one fix:
- **(Recommended)** Keep the Clock and record it: DEC-59 states "time-triggered checks are started by a system Clock; the Clock is a secondary actor of UC-09 (lapse) and of FR-70." Add it to UC-09's secondary actors. Also add it to the UCD, or footnote the UCD.
- Or draw it as a non-actor lifeline, `participant "«timer» Clock"`, and still mention it in DEC-59.

Also give **SD-16** a traceability row, because its title has no UC: `SD-16 | FR-70, FR-10 | no UC: system behaviour (DEC-59)`.

### M9. Linked Jobs can be split by an unassign (FR-36) (new)
FR-36: "Linked Jobs **must be allocated to the same Van on the same date**." SD-18 enforces this with `expandLinkedJobs`, but two other paths unassign **one** Job only:
- **SD-05 edit** `opt [edit breaks a rule]` → `endPlacement(); markUnassigned()` on that Job only;
- **SD-22 approval** → the Job "leaves the whole Van", and its Linked partner stays.

In both cases the partner remains on the Van alone. SD-05 cancel raises a smaller form of the same question. This is an ambiguity, so log it rather than guess (AGENTS.md rule 3):
1. Open a DEC: "When one Linked Job is unassigned or cancelled, is the partner (a) also unassigned, (b) kept but flagged Needs attention, or (c) unaffected?"
2. Then draw the answer once: either a `loop [Job and its Linked Jobs]` in SD-05 and SD-22, as in SD-18, or an `opt [has Linked Job] → flag`.

---

## 5. Minor (polish for the A)

| # | Diagram | Finding | Fix |
|---|---|---|---|
| m1 | various | Still wrapping: SD-04 msgs 14/18/21; SD-06 32; SD-10 26; SD-13 11/24/29; SD-16 8/11/17; SD-18 20; SD-21 16/18; SD-22 16/20; SD-25 2/9. **SD-05 (3,915 px) and SD-20 (3,867 px, up from 3,045)** won't fit a report page legibly | Shorten audit labels to `record(event)` and give the event in a note, or raise `maxMessageSize`. For the report, export with `scale max 1200 width` and place SD-05/SD-20 on their own page |
| m13 | SD-11 | Legend glitch: "Blank = Not submitted" then **"unavailable."** in large bold. A line starting with `=` became a Creole heading | Write "Blank (Not submitted) counts as unavailable", or escape the `=` as `~=` |
| m14 | SD-16, SD-25 | Legends contain wording aimed at reviewers: "No unused Standby lifeline", "no reference gate is needed" | Delete those phrases; a legend should describe the system, not the review |
| m15 | SD-06 | Breakdown path (msgs 25–35) changes the Van, Crews, Assignments and Jobs with **no atomic fragment and no save-failure `alt`**, unlike every other mutation in the set | Wrap 27–32 in `group atomic Van unavailability save` and add `alt [save still fails after 3 retries]`, as in SD-04 |
| m16 | SD-19 | Copied from SD-18: `proposedWorkload(week, hours)` at publication, and the legend lines "Proposed Workload…" and "Only saved Published changes notify Staff" | Rename to `weekWorkload(week)`; rewrite the legend for publication, e.g. "Publication notifies every Crew member and Standby of that week" |
| m17 | SD-10, SD-11 | `ref` boxes cover lifelines the referenced SD never uses: SD-10→SD-16 covers `:Staff` and `alert:Notification`; SD-11→SD-24 covers `:AvailabilityController`, `:Availability` and `:JobPreference`. In SD-11, msg 6 ends on `:RequestPage` and is then repeated as SD-24 msg 1 | Narrow both refs to the lifelines actually used. In SD-11, let msg 6 end at the ref frame (the gate), or drop it and let the ref start the interaction |
| m18 | SD-08 | One selected Staff member is drawn as two lifelines, `:Staff` and `:Technician` | Use one lifeline `s:Staff` and keep `opt [Technician] certifications()` on it, or use `t:Technician` only inside the opt with a note |
| m19 | SD-22, SD-25 | SD-25: "at most one Pending request **per Assignment**". The Assignment is shared by the whole Crew (DEC-39), so a Pending request from one Technician blocks the Driver's request. SD-22 meanwhile loops over `pendingRejectionsFor(assignment)` as if there could be several | State in DEC-58 (or its split) whether the limit is per Assignment or per Staff and Assignment, then make SD-22's loop guard match |
| m20 | SD-01 | `sendConfirmation` can return `failed` (msg 16), but no branch handles it, so the user waits for a code that never arrives | `alt [email failed] → generic failure; ask the user to retry later`, or route it to the existing failure operand |
| m21 | SD-25 | Every check runs twice: before the atomic save (8–14) and again inside it (16–22). This is correct but adds about 400 px | Optional: keep only the in-transaction checks, and add a note that the page pre-validates |
| m22 | SD-16 | Title `(FR-70)` breaks the `SD-nn: Name (UC-nn)` convention in AGENTS.md | Acceptable if the traceability row in M8 explains it. Otherwise retitle `(FR-70, no UC)` |

---

## 6. Per-diagram status

| SD | UC | Status | Open items |
|---|---|---|---|
| 01 Log In/out | UC-01 | ◑ | m20 |
| 02 Reset Password | UC-02 | ✅ | (B1 citations) |
| 03 Create User Account | UC-03 | ✅ | (B1) |
| 04 Manage User Access | UC-04 | ✅ | m1 |
| 05 Manage Job | UC-05 | ◑ | **M9**, m1 (height) |
| 06 Vans and Workshop Servicing | UC-06 | ◑ | m15, m1 |
| 08 Compare Staff | UC-08 | ◑ | m18 |
| 10 Manpower Dashboard | UC-10 | ◑ | m17, m1 |
| 11 Availability + Preferences | UC-11 | ◑ | m13, m17 |
| 13 My Assignments and Workload | UC-13 | ✅ | m1 |
| 14 Complete Job | UC-14 | ✅ | — |
| 15 Notify Staff | UC-15 | ✅ | — |
| 16 Invalidated Crew / Cert expiry | FR-70 | ◑ | **M8**, m14, m22 |
| 17 Form Crews and Standby | UC-07 | ✅ | — |
| 18 Allocate Job | UC-07 | ✅ | m1 |
| 19 Publish Weekly Roster | UC-07 | ◑ | m16 |
| 20 Decide Leave Request | UC-09 | ✅ | m1 (height) |
| 21 Decide Late Availability Change | UC-09 | ✅ | m1 |
| 22 Decide/Lapse Job Rejection | UC-09 | ◑ | **M8, M9**, m19 |
| 23 Submit Leave Request | UC-12 | ✅ | — |
| 24 Submit Late Availability Change | UC-12 | ✅ | — |
| 25 Submit Job Rejection Request | UC-12 | ◑ | m14, m19, m21 |

✅ = diagram ready; ◑ = small edits needed. No diagram has a notation error any more.

---

## 7. Rubric M1 alignment

| Criterion | Assessment |
|---|---|
| All key UCs represented | ✅ All 15 UCs are covered (UC-07, 09 and 12 by three SDs each), plus SD-16 for FR-70. M6 is only a record-keeping gap |
| …**with the identified classes** | ◑ Lifelines match glossary and CL- names. The CD must now contain every boundary and control class (`JobAllocationPage`, `RosterController`, `RuleValidator`, `NotificationService`…) and every operation called (see §8, step 4); otherwise this criterion fails across artefacts |
| Correct UML interactions | ✅ Sync and return messages, dashed `«create»`, guarded `alt`/`opt`/`loop`, `ref` with gates, found messages from the Clock, and execution specifications are all correct. Only polish remains (m17, m18) |
| Clear lifelines, messages, ordering | ✅ Consistent order throughout: validate → atomic mutate + audit → commit/fail `alt` → notify. Readability of the two tallest diagrams is the one weakness (m1) |
| Consistency and traceability (Formatting row) | ◑ B1 (DEC references), M8 (Clock actor vs UCD) and M9 (FR-36) are the remaining cross-artifact gaps |

---

## 8. Before the PR (in order)
1. **B1:** add DEC-48 to DEC-63 to `decisions.md` with sources, and resolve the three-topic DEC-58. Add new open DECs for M9 (Linked partner) and m19 (Pending limit).
2. **M8:** update DEC-59 and UC-09's secondary actors, and add the Clock to the UCD. **M9:** draw the decided Linked-partner rule in SD-05 and SD-22.
3. Cheap minors: m13 (one legend line), m14, m16, m15, m20, then m1 label shortening.
4. **Class diagram, same PR:** add the boundary and control classes, plus the operations introduced in this round:
   - `partitionByWeek`, `suppressDraftDelivery`, `markChannelFailed`;
   - `checkCertificationExpiry`, `findExpiredCertifications`, `validOn`, `findEligibleStandby`, `retainPreviousState`;
   - `onJobStart`, `pendingRejectionsFor`, `recheckStatusAndStart`, `lapse`;
   - `checkStillPending`, `leaveBalance`, `validateLeave`, `findCrewsOn`;
   - `findFutureCrews`, `findFutureAssignments`, `removeMember`, `markNeedsAttention`;
   - `checkLinkable`, `link`, `standardDuration`;
   - `isEligible`, `hasPendingRejection`, `hoursUntilStart`, `classifyShortNotice`;
   - `resendInitialLogin`, `validateDeviceCode`, `rememberDevice`.

   Add a `kind` attribute (DashboardAlert) to `Notification` for DEC-63.
5. **`traceability.md`:** add SD rows for SD-01 to SD-25, including the Withdrawn rows for SD-07/09/12 (M6) and the FR-70 row for SD-16. The file currently has **0** SD rows.
6. Commit the `.puml` files to `diagrams/` as `SD-nn-<slug>.puml` (it still has only README.md). Render locally only (AGENTS.md rule 5).
7. Add an `ai-usage-log.md` row: date, member, "Claude Opus 5.5: SD review round 3", and what the team changed.
8. Work on a branch such as `<name>/sequence-diagrams` and open a PR; never push to `main`.
