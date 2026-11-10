# UC-08: Compare Staff

> **Status: M2 v1.1 (2026-11-07).** Keeps «extend» to UC-07: comparison is optional during allocation (DEC-91). Shows the Standby pick, zone and activated-day count.

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
| 2 | — | Shows for each: Availability that day and week, Active Hours and Total Credited Workload this week and last week, Certifications with expiry, their provisional/confirmed/not-confirmed Standby pick, their location that day (current duty/Crew coverage zones or home Zone) and their activated-day count (FR-31). |
| 3 | Closes the panel. | Returns to UC-07. |

## Exception flows

### E1: A fourth selection

1. The system refuses it (FR-31).

**v1.1 basis:** DEC-96–98; SRS v4.1. Historical M1 sequence sources require review before reuse.
