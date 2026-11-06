# UC-17: Update Roster and Hours

> **Status: M2 v1.0 (2026-11-06).** New in M2: Edit Hours / Update Roster (DEC-78, DEC-81, DEC-91).

| Field | Value |
|---|---|
| **ID** | UC-17 |
| **Name** | Update Roster and Hours |
| **Primary actor** | Manager |
| **Secondary actors** | Email Service, SMS Gateway «system» through UC-15 |
| **Description** | During or after a working day, the Manager records who replaced whom, activates a Standby and corrects hours. |
| **Trigger** | A Crew member drops out, Overtime was worked, or hours need correcting. |
| **Linked requirements** | FR-10, FR-35, FR-49, FR-56, FR-57 |
| **Source** | M2-Brief §3.2, §3.3, §4 steps 12–13; DEC-78; DEC-81; DEC-89 |
| **Classes** | UpdateRosterPage, StandbyListView, HoursController, StandbyActivationService, TechnicianRanking, ActivationRanking, RuleValidator, Crew, Standby, HoursEdit, AuditLog, NotificationService |
| **Wireframe** | W-09 Update Roster and Hours; W-10 Standby list |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in. The date is today or within the last 12 months.

## Main flow (basic path): replace a Crew member with a Standby

| Step | Actor | System |
|---|---|---|
| 1 | Opens Update Roster for the day and selects the Crew and the person dropping out. | Shows the Crew, its Jobs and each member's day hours. |
| 2 | Opens the Standby list for the affected Job. | `StandbyActivationService.listStandbysForJob()` orders unactivated Standby Staff by fewest activations in 12 months, then zone distance, then staff ID (FR-56). |
| 3 | Phones the top person **outside the system**, then selects whoever agreed. | `RuleValidator.checkCrew()` checks Brands and that they are not already in a Crew (FR-32). |
| 4 | Enters the hours worked by each person and a reason. | `HoursController.recordReplacement()`: `Standby.activate()` and `Crew.changeMembers()`; then `editHours()` creates an `HoursEdit` for each person, replacing their day hours (FR-57). |
| 5 | — | Logs the change and notifies both people and the Crew through UC-15 (FR-39, FR-49). |

## Alternative flows

### A1: Hours correction only (branches at step 1)

1. The Manager picks a Staff member and date and enters the new hours and a reason (for example Overtime worked).
2. `HoursController.editHours()` records `oldHours` and `newHours`. The change is logged and the person notified.

### A2: No suitable Standby (branches at step 2)

1. The Manager unassigns the Job or moves it to another Crew (UC-07 A4).

## Exception flows

### E1: Missing reason, or hours outside 0–24 (step 4)

1. The save is refused (FR-57).

## Postconditions

- **Success:** The Crew, Standby and hours reflect what happened. The activation count rises by 1 and all changes are logged.
- **Failure:** Nothing changes.
