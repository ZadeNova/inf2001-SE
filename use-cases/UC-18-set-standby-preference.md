# UC-18: Set Standby Preference

> **Status: M2 v1.0 (2026-11-06).** New in M2. It replaces the M1 Job Preference part of UC-11 and meets Brief R9 (DEC-79, DEC-91).

| Field | Value |
|---|---|
| **ID** | UC-18 |
| **Name** | Set Standby Preference |
| **Primary actor** | Technician |
| **Secondary actors** | None |
| **Description** | A Technician picks one Standby day per Planning Week in a free Brand slot. Each accepted pick is guaranteed. |
| **Trigger** | The Technician wants a Standby day in an open week. |
| **Linked requirements** | FR-15, FR-51, NFR-12 |
| **Source** | Brief R9; M2-Brief §1, §3.4; DEC-79 |
| **Classes** | StandbyPreferencePage, StandbyPreferenceController, RuleValidator, StandbyPreference, Technician, Certification, Availability, LeaveRecord |
| **Wireframe** | W-14 Standby Preference |
| **Status** | Agreed |

## Preconditions

1. The Technician is logged in. The week is before its Availability Deadline.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Standby Preference for a week. | `StandbyPreferenceController.loadWeek()` shows Monday–Saturday with the M Electric and Dicon slot of each day. A day is greyed out when no slot the Technician could take is free, or when they are not Available or have a Leave Record that day. |
| 2 | Picks a day and Brand slot. | — |
| 3 | Confirms. | `submitPick()` calls `RuleValidator.checkStandbyPick()` (deadline, Available, valid Certification for the Brand on that day, slot free), then saves the `StandbyPreference` (FR-51). |

## Alternative flows

### A1: Change the pick (branches at step 2)

1. The Technician picks a different day or slot. The old slot is freed and the new one is checked as in step 3.

### A2: Withdraw (branches at step 2)

1. `withdrawPick()` deletes the pick and frees the slot.

## Exception flows

### E1: The slot was taken a moment earlier (step 3)

1. The save is refused (first come first served), and the page refreshes the free slots.

### E2: After the deadline (step 3)

1. Refused (FR-15).

## Postconditions

- **Success:** The pick is saved, and FR-55 puts the Technician on Standby that day.

## Business rules / notes

- Drivers do not pick (DEC-82).
- The Manager sees picks in UC-08 and on the Availability grid. Moving a pick into a Crew needs a logged override (FR-33).
