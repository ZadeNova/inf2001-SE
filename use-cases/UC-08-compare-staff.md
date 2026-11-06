# UC-08: Compare Staff

> **Status: M2 v1.0 (2026-11-06).** Keeps «extend» to UC-07: comparison is optional during allocation (DEC-91). Shows the Standby pick, zone and activation count.

| Field | Value |
|---|---|
| **ID** | UC-08 |
| **Name** | Compare Staff |
| **Primary actor** | Manager |
| **Secondary actors** | None |
| **Description** | While allocating, the Manager compares up to three Staff side by side for a date. |
| **Trigger** | The Manager selects Staff to compare at UC-07's Compare Staff extension point. |
| **Extends** | UC-07 at "Compare Staff", condition {Manager selects 1–3 Staff} |
| **Linked requirements** | FR-31 |
| **Source** | Brief R4, R5; DEC-06; DEC-77; DEC-79; DEC-91 |
| **Classes** | JobAllocationPage, RosterController, Staff, Technician, Certification, StandbyPreference, Availability |
| **Wireframe** | W-07 Compare Staff |
| **Status** | Agreed |

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Selects up to three Staff and a date. | `RosterController.compare(selection, date)`. |
| 2 | — | Shows for each: Availability that day and week, Workload this week and last week, Certifications with expiry, their Standby pick, their location that day (Crew zone or home zone) and their activation count (FR-31). |
| 3 | Closes the panel. | Returns to UC-07. |

## Exception flows

### E1: A fourth selection

1. The system refuses it (FR-31).
