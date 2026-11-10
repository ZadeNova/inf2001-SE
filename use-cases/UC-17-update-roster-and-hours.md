# UC-17: Update Roster and Hours

> **Status: M2 v1.1 (2026-11-07).** Direct Standby duties, Crew replacements and Active Hours corrections (DEC-96/97).

| Field | Value |
|---|---|
| **ID** | UC-17 |
| **Name** | Update Roster and Hours |
| **Primary actor** | Manager |
| **Secondary actors** | Email Service, SMS Gateway through UC-15 |
| **Description** | Activate eligible Standby Staff for direct Jobs or Crew replacements, preserve who handled each Job, and correct Active Hours. |
| **Trigger** | Extra Jobs need cover, a Technician leaves a Crew, or hours need correction. |
| **Linked requirements** | FR-07, FR-08, FR-10, FR-27, FR-30, FR-32, FR-35, FR-49, FR-56, FR-57 |
| **Source** | M2-Brief §3.2; DEC-96, DEC-97, DEC-98 |
| **Classes** | UpdateRosterPage, StandbyListView, HoursController, StandbyActivationService, ActivationRanking, RuleValidator, Assignment, Replacement, Crew, Standby, HoursEdit, AuditLog, NotificationService |
| **Wireframe** | W-09; W-10 |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in.
2. Operational activations/replacements concern today's Published roster and unstarted Jobs. Hours-only corrections may concern any date retained within 12 months.
3. A Standby record exists for the selected Technician/date. A confirmed preference permits genuine activation, but not rewriting initial placement.

## Main flow: replace a Technician from a specified Job

| Step | Actor | System |
|---|---|---|
| 1 | Selects Crew, outgoing Technician and first unstarted Job to be taken over. | Shows earlier Jobs and attributed Staff, remaining Jobs, effective members and Active/Total Credited Hours. |
| 2 | Opens the eligible Standby list. | Filter first: availability/Leave, Certification, coverage for every remaining Job, person-level time/travel conflicts and existing Crew commitment. Rank eligible Staff by activated dates in 12 months, home-Zone distance to the first Job, then staff ID (FR-56). |
| 3 | Phones a candidate outside the system and selects the person who agrees. | Recheck eligibility immediately before saving; a failed call records no activation. No candidate is labelled lazy solely from a low count. |
| 4 | Records the replacement and reason, optionally correcting Active Hours. | HoursController.recordReplacement() stores a Replacement (who out/in, Crew, fromJobId, effectiveFrom, Manager, reason, timestamp). Change Staff attribution only on affected unstarted Assignments. Keep initial Crew members and earlier Job Staff; Crew.membersFor() supplies effective members for later added Jobs. |
| 5 | Saves. | Atomically save attribution, replacement, idempotent Standby.activate(), any HoursEdit and audit entries. Retain Standby history. Recompute Active Hours from attributed Planned Hours; Total Credited = max(4, Active Hours) for the Standby date. Activation count gains one only if this was the first activation that date. |
| 6 | — | Notify affected Staff/Crew after commit through UC-15. |

## Alternative flows

### A1: Direct Standby Job
1. Select an extra Unassigned Job and start time.
2. Filter and rank as above for that Job's Brand and schedule. A Technician with an earlier direct duty can appear if the new duty fits; a replacement-Crew member cannot be offered elsewhere.
3. Phone the person, then HoursController.activateForJob() creates an Assignment with dutyDate, no Crew, and exactly that certified Technician as attributed Staff.
4. Company-paid transport is arranged outside the system. No Driver/Van is invented; the Technician may return after the duty and later accept another compatible direct Job.
5. Apply the same atomic save, hours floor, once-per-date count, audit and notifications.

### A2: Hours correction only
Select Staff/date, enter corrected Active Hours (0–24) and reason. HoursController.editHours() stores oldActiveHours/newActiveHours, Manager and timestamp. Total Credited Hours are derived; the Manager cannot erase the Standby minimum by typing a smaller credited total. Earlier Job membership is not rewritten.

### A3: No eligible/agreeing Standby
Show no suitable candidate. The Manager can move/unassign unstarted Jobs through UC-07; never force an invalid replacement or count an unsuccessful call as an activation.

## Exceptions

- Expired Certification, wrong Brand, Leave, overlap, insufficient travel or a conflicting Crew commitment: refuse the save.
- Missing reason or Active Hours outside 0–24: refuse.
- Started/past Job selected as replacement boundary: refuse; earlier attribution remains read-only.
- Concurrent changes or save failure: revalidate/rollback; no partial activation, count change or notification.

## Postconditions and examples

- Alex on Job 1 (2 credited planned hours), Ben from Job 2 (6 remaining planned hours): Alex retains 2 Active/2 Credited; Ben has 6 Active/6 Credited. Job 1 still names Alex.
- Standby with 2 h direct duty: 2 Active/4 Credited/count +1. Later 3 h direct duty: day totals 5/5/count still +1.
- Unused Standby: 0 Active/4 Credited/count +0. Full-day Leave without duties: 0/0.
- These are Planned Hours (including the agreed Travel Allowance), not stopwatch times or a new job-completion workflow.
