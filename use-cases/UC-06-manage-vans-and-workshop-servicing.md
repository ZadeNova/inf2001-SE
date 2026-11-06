# UC-06: Manage Vans and Workshop Servicing

> **Status: Withdrawn (2026-11-07, DEC-85, DEC-91).** Out of M2 scope (DEC-73). The ID is kept and never reused. The text below is the M1 report record (UC-06/UC-14 as submitted) and is not part of the M2 baseline.

| Field | Value |
|---|---|
| **ID** | UC-06 |
| **Name** | Manage Vans and Workshop Servicing |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager maintains Van records, reviews generated Workshop Servicing dates and records other Van unavailability. |
| **Trigger** | A Van is added or changed, a servicing date needs review, or a Van becomes unavailable. |
| **Linked requirements** | FR-23, FR-24, FR-25, FR-05, FR-39 |
| **Source** | Brief §Company ¶3, ¶5; INT-MGR [Process Q3], [Conflicts Q4]; INT-DRV [Q2], [Q8]; DEC-14; DEC-45; DEC-54; DEC-58; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-06](../diagrams/SD-06-manage-vans-and-workshop-servicing.puml) |
| **Status** | Withdrawn |

## Preconditions

1. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Van management. | Lists Van numbers, licence plates and generated Workshop Servicing dates (FR-23, FR-24). |
| 2 | Selects a Van or adds a Van record. | Displays editable number and licence-plate details. |
| 3 | Enters or changes the details and submits. | Validates and saves the Van record (FR-23). |
| 4 | Reviews the servicing schedule. | Generates the month once using the odd/even-month rotation and moves a Sunday date to Monday (FR-24). |
| 5 | Confirms or adjusts a generated date. | Checks that no Crew exists on the proposed date, then books servicing and marks the Van unavailable all day. After a date change, frees the previous booked date only if no other unavailability reason applies. |

## Alternative flows

### A1: Record a breakdown or extra servicing days (branches at step 1)

1. The Manager selects a Van and date range.
2. The system marks the Van unavailable, releases its Crews, and makes its not-yet-completed Jobs Unassigned (FR-25).
3. The system invokes UC-15 for released Crew members (FR-39).

## Exception flows

### E1: Unavailability affects completed work (branches at A1 step 2)

1. The system leaves Completed Jobs unchanged (FR-25, FR-05).

### E2: Save fails

1. The system follows NFR-06 and does not confirm unsaved changes.

### E3: Workshop Servicing date has an existing Crew (branches at steps 4 or 5)

1. Block that servicing date and warn the Manager; preserve the Crew and Jobs.
2. Keep a generated conflict as an unbooked proposal. The Manager selects another date; changing a booked date is refused until a conflict-free date is supplied.

## Postconditions

- **Success:** Van data or unavailable dates are recorded; affected future Jobs and Crews follow FR-25.
- **Failure:** Existing Van, Crew and Job records remain unchanged.

## Business rules / notes

- The current six-Van rotation is data, while FR-23 permits additional Vans.
- Reopening a generated month does not create duplicate servicing records.
- Sunday is the only non-working day in the current SRS scope.
- Generated-date conflicts are collected during the loop and returned once. Breakdown notifications are sent after the save, and Draft roster events are withheld (SD-20).

## Open questions

- Define automatic Workshop Servicing generation for Vans added beyond the current six.
