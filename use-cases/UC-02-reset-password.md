# UC-02: Reset Password

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-02 |
| **Name** | Reset Password |
| **Primary actor** | User |
| **Secondary actors** | Email Service |
| **Description** | A User who cannot remember the password obtains a reset link through company email and sets a new password. |
| **Trigger** | The User selects Forgot Password from UC-01. |
| **Linked requirements** | FR-47, FR-49, NFR-06, NFR-08 |
| **Source** | INT-ITA [Q: Passwords], [Q: Audit], [Q: Connection failure], [Q: Safeguards]; DEC-17; DEC-56; DEC-61; DEC-71; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-02](../diagrams/SD-02-reset-password.puml) |
| **Status** | Agreed |

## Preconditions

1. The User has an active account with a company email address.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Enters the company email and requests a reset. | Accepts the request without disclosing whether another person's account exists (FR-47). |
| 2 | — | Sends a reset link to the company email and logs the request (FR-47, FR-49). |
| 3 | Opens the link and enters a new password. | Validates the link and atomically stores the new password as a salted hash (NFR-08), invalidates all outstanding reset tokens for that Account, and logs the password change (FR-49). |
| 4 | Returns to UC-01. | Confirms the reset and allows login with the new password. |

## Alternative flows

### A1: Request is resubmitted (branches at step 1)

1. The system processes the latest valid request and sends a reset email. Resubmission does not itself revoke previous links; after any successful reset, all outstanding reset tokens for that Account are invalidated.

## Exception flows

### E1: Link cannot be used (branches at step 3)

1. The system refuses the reset and tells the User to request another link.

### E2: Submission fails (branches at steps 1 or 3)

1. The system retries up to three times.
2. If saving still fails, it states that the request was not saved and advises retrying or contacting the IT Administrator (NFR-06).

## Postconditions

- **Success:** The password is replaced and all outstanding reset tokens for the Account are unusable, and the request and password change are logged.
- **Failure:** The existing password remains unchanged.

## Business rules / notes

- This use case extends UC-01. Reset-token validation, the password change and invalidation of all outstanding reset tokens occur atomically. Concurrent or repeated resets recheck token validity at save time; a failed transaction preserves the prior password and token state.
- Exact token lifetime and password-complexity rules are not stated in the SRS.
- Reset-token lifetime and password complexity remain open; no numeric policy is assumed.

## Open questions

- Confirm reset-link lifetime and password-complexity policy before implementation. Single-use behaviour is adopted.
