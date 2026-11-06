# UC-11: Set Availability + Preferences

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-11 |
| **Name** | Set Availability + Preferences |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | Staff record per-Slot Availability and optional weekly Job Preference before the Availability Deadline. |
| **Trigger** | A Staff member needs to declare or revise Availability or Job Preference for an open week. |
| **Linked requirements** | FR-12, FR-13, FR-15, FR-17 |
| **Source** | Brief R5, R8, R9 and Lecturer clarification; INT-MGR [Clarification Q4], [Clarification Q6 follow-up]; INT-DCT [Questionnaire C6], [Questionnaire C7]; INT-DRV [Q10]; DEC-01; DEC-02; DEC-03; DEC-07; DEC-30; DEC-45; DEC-47; DEC-58; DEC-70; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-02](../diagrams/AD-02-set-availability.puml); [SD-14](../diagrams/SD-14-set-availability-and-preferences.puml); [SD-16](../diagrams/SD-16-submit-late-availability-change.puml) |
| **Status** | Agreed |

## Preconditions

1. The Staff member is logged in.
2. The selected dates are between today and the same calendar date next month, inclusive.
3. The Planning Week is not locked.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Availability for an editable week. | Shows Monday–Saturday with Morning and Afternoon Slots and the deadline (FR-12, FR-13, FR-15). |
| 2 | Marks each Slot Available or Unavailable, uses the whole-day shortcut, or clears an entry. | Shows blank Slots as Not submitted and treats them as unavailable for allocation (FR-12). |
| 3 | Opens Job Preference for the same week. | Shows optional area, day, Slot and Job Type fields (FR-17). |
| 4 | Enters any preferences and submits. | Validates the date window and deadline, then saves both records. |

## Alternative flows

### A1: No Job Preference (branches at step 3)

1. The Staff member leaves every preference field blank.
2. The system saves Availability without a preference (FR-17).

## Exception flows

### E1: Week is locked (branches at step 4)

1. The system refuses the direct Availability or preference change.
2. It offers UC-12; if the Staff member accepts, the system opens a Late Availability Change Request (FR-16).

### E2: Date outside the one-month window (branches at steps 1 or 4)

1. The system refuses the affected dates (FR-13).

### E3: Save fails

1. The system follows NFR-06.

## Postconditions

- **Success:** Availability and any Job Preference are saved for the open week.
- **Failure:** Prior records remain unchanged.

## Business rules / notes

- Job Preference is advisory; violating it creates a warning in UC-07, not a block.
- Sunday Slots are not offered.
- The Manager cannot directly overwrite Staff Availability.
- Staff explicitly chooses to request a Late Availability Change after direct changes are refused. Setting a blank Slot creates Availability; clearing a blank Slot makes no record. Recheck the deadline at save time.

## Open questions

- Confirm whether pre-deadline reminders are in scope, including timing, recipients and channels. Confirm how exact-hour Availability responses map to the adopted Morning/Afternoon Slots; the Slot model remains unchanged.
