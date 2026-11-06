# UC-04: Manage User Access

> **Status: M2 v1.0 (2026-11-06).** Adds Technician profile updates (home zone, Certification expiry). The IT Administrator now owns these updates (DEC-75).

| Field | Value |
|---|---|
| **ID** | UC-04 |
| **Name** | Manage User Access |
| **Primary actor** | IT Administrator |
| **Secondary actors** | None |
| **Description** | The IT Administrator changes roles, unlocks or deactivates accounts, updates Technician profiles and views the Audit Log. |
| **Trigger** | A role change, lockout, leaver, renewed Certification, moved home, or audit question. |
| **Linked requirements** | FR-45, FR-46, FR-48, FR-22, FR-49 |
| **Source** | INT-ITA [Q: Role change/leaver], [Q: Passwords], [Q: Audit]; DEC-17; DEC-34; DEC-75 |
| **Classes** | AccountAdminPage, AuditLogPage, AccountController, RosterController, Account, Technician, Certification, AuditLog |
| **Wireframe** | W-13 IT Admin account management |
| **Status** | Agreed |

## Preconditions

1. The IT Administrator is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Searches for a user and opens the account. | Shows role, status and, for a Technician, home zone and Certifications. |
| 2 | Chooses an action: change role, unlock, deactivate, or update Technician profile. | Shows the action's form. |
| 3 | Confirms. | Applies the action and logs it (FR-49). |

## Alternative flows

### A1: Change role or deactivate (branches at step 3)

1. `Account.setRole()` or `Account.deactivate()`.
2. `RosterController.removeFromFutureRoster(staff)` removes future Crew places and Standby days, and the affected Jobs become Unassigned (FR-45, FR-46).

### A2: Unlock (branches at step 3)

1. `Account.unlock()` (FR-48).

### A3: Update Technician profile (branches at step 3)

1. `AccountController.updateTechnicianProfile()` calls `Technician.setHomeZone()` and `Certification.renew(expiryDate)`, or adds or removes a Certification (FR-22).
2. A Technician must keep at least one Certification.

### A4: View Audit Log (branches at step 1)

1. The IT Administrator opens the Audit Log page and filters by who, action or date (`AuditLog.search()`).

## Exception flows

### E1: Unauthorised actor (branches at step 2)

1. The system refuses the operation (NFR-09).

### E2: Save fails (branches at step 3)

1. The system follows the NFR-06 retry and failure-message rule.

## Postconditions

- **Success:** The change is saved and logged.
- **Failure:** Nothing changes.
