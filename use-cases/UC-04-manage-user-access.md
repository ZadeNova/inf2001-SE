# UC-04: Manage User Access

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-04 |
| **Name** | Manage User Access |
| **Primary actor** | IT Administrator |
| **Secondary actors** | Email/Phone through UC-15 |
| **Description** | The IT Administrator changes roles, unlocks accounts, deactivates leavers and reviews the access-related audit record. |
| **Trigger** | An account's access, role or lock state requires administration. |
| **Linked requirements** | FR-45, FR-46, FR-48, FR-49, NFR-09, NFR-10 |
| **Source** | INT-ITA [Q: Permissions], [Q: Role change/leaver], [Q: Retention], [Q: Passwords], [Q: Audit]; DEC-17; DEC-34; DEC-45; DEC-47; DEC-58; DEC-60; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-04](../diagrams/SD-04-manage-user-access.puml) |
| **Status** | Agreed |

## Preconditions

1. The IT Administrator is logged in.
2. The target account exists.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Searches for and selects an account. | Shows its role, status and lock state. |
| 2 | Selects an allowed access action and supplies any required change. | Validates that the actor is an IT Administrator (NFR-09). |
| 3 | Confirms the change. | Saves it and writes an audit entry with who, what and when (FR-49). |
| 4 | Reviews the result. | Shows the updated account state and any affected future Assignments (FR-45, FR-46). |

## Alternative flows

### A1: Change role (branches at step 2)

1. The IT Administrator selects a new role.
2. The system applies it from the User's next login; if Staff becomes Manager, future Assignments are removed and their Jobs become Unassigned (FR-45).

### A2: Deactivate a leaver (branches at step 2)

1. The system prevents later login, removes future Assignments, returns those Jobs to Unassigned, and retains past records (FR-46, NFR-10).

### A3: Unlock an account (branches at step 2)

1. The system clears the FR-48 lock so the User can try UC-01 again.

### A4: View audit log (branches at step 1)

1. The IT Administrator opens the read-only audit log and filters or reviews entries (FR-49).

## Exception flows

### E1: Unauthorised actor (branches at step 2)

1. The system refuses the operation (NFR-09).

### E2: Save fails (branches at step 3)

1. The system follows the NFR-06 retry and failure-message rule.

## Postconditions

- **Success:** The selected access state is updated and audited, or the audit log is displayed.
- **Failure:** The account and its Assignments remain unchanged.

## Business rules / notes

- Historical records are retained for 12 months from their date (NFR-10).
- Audit-log viewing is part of this use case (A4).
- Account deactivation and Staff-to-Manager changes atomically remove future Crew membership, flag affected Van-days Needs attention, end future Assignments, make the Jobs Unassigned and audit the changes. Notify affected Crew/eligible Standby after commit; hide Draft roster events through SD-20.

## Open questions

- Confirm how active sessions behave after deactivation or a role change.
