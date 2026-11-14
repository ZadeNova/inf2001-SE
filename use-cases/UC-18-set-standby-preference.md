# UC-18: Set Standby Preference

> **Status: M2 v1.1 (2026-11-07).** Provisional requests become binding only after the post-deadline capacity check (DEC-98).

| Field | Value |
|---|---|
| **ID** | UC-18 |
| **Name** | Set Standby Preference |
| **Primary actor** | Technician |
| **Secondary actors** | Confirmation is triggered by Manager preparation in UC-07; notification through UC-15 |
| **Description** | Request one provisional day/Brand slot per Planning Week and view its capacity-checked outcome. A confirmed pick guarantees initial Standby placement. |
| **Trigger** | A Technician opens an unlocked week. |
| **Linked requirements** | FR-15, FR-51, FR-55, NFR-12 |
| **Source** | Brief R9; DEC-79, DEC-108, DEC-98 (including member-reported professor feedback on work-life balance) |
| **Classes** | StandbyPreferencePage, StandbyPreferenceController, StandbyPreference, RuleValidator, Technician, Certification, Availability, LeaveRecord, VanAvailability, NotificationService |
| **Wireframe** | W-14; confirmation status also W-06/W-08/W-11 |
| **Status** | Agreed |

## Preconditions
The Technician is logged in; requests/changes are before the Availability Deadline.

## Main flow: provisional submission

| Step | Actor | System |
|---|---|---|
| 1 | Opens a week. | Show day/Brand slots and their provisional/confirmed status. Explain that confirmation follows locked Availability, HR/Van CSVs and minimum staffing checks. |
| 2 | Selects a day and Brand. | One M Electric and one Dicon request slot per day; a dual may take either. |
| 3 | Submits. | submitPick() checks deadline, availability/no Leave, valid Certification and free slot in that order. Save Provisional with submittedAt; one pick per Technician/week and one request per day/Brand. |
| 4 | — | Show "Provisional — awaiting staffing check", never "Guaranteed" at this stage. |

## Later confirmation (UC-07, FR-51)
1. After the deadline, committed complete HR coverage for the Planning Week (including zero-row coverage) and explicit Van counts for each working date (DEC-108), confirmWeek() processes each day's Provisional picks by submittedAt, then staff ID.
2. Recheck eligibility. findMinimumCoverage() tests whether reserving this pick and earlier Confirmed picks permits at least three valid Crews **and Full Standby cover**. Use all eligible non-confirmed-pick Technicians, including Algorithm/Leftover Standby; do not mistake rotation preference for unavailability.
3. Save Confirmed or NotConfirmed with decidedAt and reason. Resolve a day's decisions atomically; unchanged decisions are idempotent on retry.
4. Notify the Technician via UC-15 even while the roster is Draft; expose only the preference decision, not unpublished Assignments.
5. Crew formation must honour Confirmed picks. Managers cannot revoke/move them into an initial Crew; genuine direct/replacement activation is permitted. Leave overrides initial placement and is shown without erasing confirmation history.

## Alternatives

- Change day/Brand before the deadline: check the new slot atomically, free the old slot and reset submittedAt. A no-op resubmission preserves its time.
- Withdraw before the deadline: remove the provisional pick and free the slot; audit.
- NotConfirmed: show the staffing/eligibility reason. Do not silently select a different day or permit late edits.
- Later Leave or staffing loss: flag for Manager repair; do not silently revoke someone else's confirmed preference.

## Exceptions

- Slot taken concurrently: refuse and refresh; no double booking.
- Deadline reached: refuse request/change/withdrawal.
- Missing committed complete HR week coverage, Van counts or locked-input prerequisites: defer confirmation, keep Provisional and explain why.
- Save failure: preserve the previous state and send no outcome notification.

## Postconditions

A provisional request or explicit decision is visible. Confirmed means initial Standby, not a guaranteed day without work. Drivers do not request Standby (DEC-82). Submission decision-table tests remain separate from confirmation feasibility scenarios.
