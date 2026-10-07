# UC-06: Manage Vans and Workshop Servicing

> **Status: Draft v0.2 (2026-10-04).**

| Field | Value |
|---|---|
| **ID** | UC-06 |
| **Name** | Manage Vans and Workshop Servicing |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager maintains Van records, reviews generated Workshop Servicing dates and records other Van unavailability. |
| **Trigger** | A Van is added or changed, a servicing date needs review, or a Van becomes unavailable. |
| **Linked requirements** | FR-27, FR-28, FR-29, FR-38, FR-64 |
| **Source** | Brief §Company ¶3, ¶5; INT-MGR [Process Q3], [Conflicts Q4]; INT-DRV [Q2], [Q8]; DEC-14; DEC-45; DEC-54; DEC-58 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-06](../diagrams/SD-06-manage-vans-and-workshop-servicing.puml) |
| **Status** | Draft |

## Preconditions

1. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Van management. | Lists Van numbers, licence plates and generated Workshop Servicing dates (FR-27, FR-28). |
| 2 | Selects a Van or adds a Van record. | Displays editable number and licence-plate details. |
| 3 | Enters or changes the details and submits. | Validates and saves the Van record (FR-27). |
| 4 | Reviews the servicing schedule. | Generates the month once using the odd/even-month rotation and moves a Sunday date to Monday (FR-28, DEC-54). |
| 5 | Confirms or adjusts a generated date. | Checks that no Crew exists on the proposed date, then books servicing and marks the Van unavailable all day. After a date change, frees the previous booked date only if no other unavailability reason applies (DEC-54). |

## Alternative flows

### A1: Record a breakdown or extra servicing days (branches at step 1)

1. The Manager selects a Van and date range.
2. The system marks the Van unavailable, releases its Crews, and makes its not-yet-completed Jobs Unassigned (FR-29).
3. The system invokes UC-15 for released Crew members (FR-64).

## Exception flows

### E1: Unavailability affects completed work (branches at A1 step 2)

1. The system leaves Completed Jobs unchanged (FR-29, FR-38).

### E2: Save fails

1. The system follows NFR-09 and does not confirm unsaved changes.

### E3: Workshop Servicing date has an existing Crew (branches at steps 4 or 5)

1. Block that servicing date and warn the Manager; preserve the Crew and Jobs (DEC-54).
2. Keep a generated conflict as an unbooked proposal. The Manager selects another date; changing a booked date is refused until a conflict-free date is supplied.

## Postconditions

- **Success:** Van data or unavailable dates are recorded; affected future Jobs and Crews follow FR-29.
- **Failure:** Existing Van, Crew and Job records remain unchanged.

## Business rules / notes

- The current six-Van rotation is data, while FR-27 permits additional Vans.
- Reopening a generated month does not create duplicate servicing records (DEC-54).
- Sunday is the only non-working day in the current SRS scope (DEC-45).

- Generated-date conflicts are collected during the loop and returned once. Breakdown notifications pass through SD-15 Draft protection after the atomic business save (DEC-58); servicing-conflict handling remains DEC-54.

## Open questions

- Define automatic Workshop Servicing generation for Vans added beyond the current six.

