# UC-11: Set Availability

> **Status: M2 v1.0 (2026-11-06).** Renamed from "Set Availability + Preferences". The preference part moved to UC-18. Availability is per working day; late changes happen outside the system (DEC-79, DEC-83, DEC-91). File name kept for link stability.

| Field | Value |
|---|---|
| **ID** | UC-11 |
| **Name** | Set Availability |
| **Primary actor** | Staff |
| **Secondary actors** | None |
| **Description** | A Staff member marks each working day Available or Unavailable up to 1 month in advance, before the Availability Deadline. |
| **Trigger** | The Staff member wants to declare or change Availability for an open week. |
| **Linked requirements** | FR-12, FR-13, FR-15, NFR-12 |
| **Source** | Brief R8 + Lecturer clarification; DEC-01; DEC-02; DEC-03; DEC-30; DEC-83 |
| **Classes** | AvailabilityPage, AvailabilityController, RuleValidator, Availability |
| **Wireframe** | W-12 Set Availability |
| **Status** | Agreed |

## Preconditions

1. The Staff member is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Availability and picks a week. | `AvailabilityController.loadWeek()` shows Monday–Saturday with each day's state and the week's deadline. |
| 2 | Marks days Available or Unavailable, or clears a day. | Shows a cleared day as Not submitted (FR-12). |
| 3 | Submits. | `checkWindowDeadline()` checks the 1-month window and `RuleValidator.availabilityDeadline()`, then `Availability.setState()` / `clear()` save the changes (FR-13, FR-15). |

## Exception flows

### E1: Week locked (step 3)

1. The system refuses the change and says to contact the Manager. Late changes are handled outside the system (DEC-83).

### E2: Date outside the window (step 1 or 3)

1. Those dates are not editable (FR-13).

## Postconditions

- **Success:** Availability is saved for the open week.
- **Failure:** Earlier entries are unchanged.
