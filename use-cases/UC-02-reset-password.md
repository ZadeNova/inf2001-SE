# UC-02: Reset Password

> **Status: Draft v0.1 (2026-10-01).** Extends UC-01.

| Field | Value |
|---|---|
| **ID** | UC-02 |
| **Name** | Reset Password |
| **Primary actor** | User |
| **Secondary actors** | Email Service |
| **Description** | A User who cannot remember the password obtains a reset link through company email and sets a new password. |
| **Trigger** | The User selects Forgot Password from UC-01. |
| **Linked requirements** | FR-06, FR-66, NFR-09, NFR-11 |
| **Source** | INT-ITA [Q: Passwords], [Q: Audit], [Q: Connection failure], [Q: Safeguards]; DEC-17 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The User has an active account with a company email address.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Enters the company email and requests a reset. | Accepts the request without disclosing whether another person's account exists (FR-06). |
| 2 | — | Sends a reset link to the company email and logs the request (FR-06, FR-66). |
| 3 | Opens the link and enters a new password. | Validates and stores the new password as a salted hash (NFR-11). |
| 4 | Returns to UC-01. | Confirms the reset and allows login with the new password. |

## Alternative flows

### A1: Request is resubmitted (branches at step 1)

1. The system processes the latest valid request and sends a reset email.

## Exception flows

### E1: Link cannot be used (branches at step 3)

1. The system refuses the reset and tells the User to request another link.

### E2: Submission fails (branches at steps 1 or 3)

1. The system retries up to three times.
2. If saving still fails, it states that the request was not saved and advises retrying or contacting the IT Administrator (NFR-09).

## Postconditions

- **Success:** The password is replaced and the request is logged.
- **Failure:** The existing password remains unchanged.

## Business rules / notes

- This use case extends UC-01.
- Exact token lifetime and password-complexity rules are not stated in the SRS.

## Open questions

- Confirm reset-link lifetime, single-use behaviour and password-complexity policy before implementation.

