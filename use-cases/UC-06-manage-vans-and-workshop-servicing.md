# UC-06: Manage Vans and Workshop Servicing

> **Status: Draft v0.1 (2026-10-01).**

| Field | Value |
|---|---|
| **ID** | UC-06 |
| **Name** | Manage Vans and Workshop Servicing |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | The Manager maintains Van records, reviews generated Workshop Servicing dates and records other Van unavailability. |
| **Trigger** | A Van is added or changed, a servicing date needs review, or a Van becomes unavailable. |
| **Linked requirements** | FR-27, FR-28, FR-29, FR-38, FR-64 |
| **Source** | Brief §Company ¶3, ¶5; INT-MGR [Process Q3], [Conflicts Q4]; INT-DRV [Q2], [Q8]; DEC-14; DEC-45 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The Manager is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Van management. | Lists Van numbers, licence plates and generated Workshop Servicing dates (FR-27, FR-28). |
| 2 | Selects a Van or adds a Van record. | Displays editable number and licence-plate details. |
| 3 | Enters or changes the details and submits. | Validates and saves the Van record (FR-27). |
| 4 | Reviews the servicing schedule. | Generates dates using the odd/even-month rotation and moves a Sunday date to Monday (FR-28). |
| 5 | Confirms or adjusts a generated date. | Marks the Van unavailable for the whole servicing day. |

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

## Postconditions

- **Success:** Van data or unavailable dates are recorded; affected future Jobs and Crews follow FR-29.
- **Failure:** Existing Van, Crew and Job records remain unchanged.

## Business rules / notes

- The current six-Van rotation is data, while FR-27 permits additional Vans.
- Sunday is the only non-working day in the current SRS scope (DEC-45).

## Open questions

- Define automatic Workshop Servicing generation for Vans added beyond the current six.

