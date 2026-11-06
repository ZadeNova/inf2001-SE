# UC-02: Reset Password

> **Status: M2 v1.0 (2026-11-06).** Now a standalone use case of User, no longer «extend» UC-01 (DEC-91). Backed by the PasswordResetToken class (FR-47).

| Field | Value |
|---|---|
| **ID** | UC-02 |
| **Name** | Reset Password |
| **Primary actor** | User |
| **Secondary actors** | Email Service «system» |
| **Description** | A User who has forgotten the password gets a single-use link by company email and sets a new password. |
| **Trigger** | The User chooses "Forgot password" on the Login page. |
| **Linked requirements** | FR-47, FR-49, NFR-06, NFR-08 |
| **Source** | INT-ITA [Q: Passwords], [Q: Audit], [Q: Safeguards]; DEC-56; DEC-61; DEC-71; DEC-91; M2-Brief §3.2 |
| **Classes** | LoginPage, AuthController, Account, PasswordResetToken, AuditLog, EmailChannel |
| **Wireframe** | W-02 Forgot password |
| **Status** | Agreed |

## Preconditions

1. The User has an active account with a company email address.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Enters the company email and requests a reset. | `AuthController.requestReset()` replies the same way whether or not the account exists. |
| 2 | — | `PasswordResetToken.generate(account)` stores a hashed token with an expiry time, emails the link through Email Service and logs the request (FR-47, FR-49, NFR-08). |
| 3 | Opens the link and enters a new password. | `AuthController.resetPassword()`: `PasswordResetToken.validate()`, `Account.setPassword()`, then `PasswordResetToken.invalidateAll(account)`, all in one save (DEC-71). |
| 4 | — | Confirms the reset and returns to the Login page. |

## Alternative flows

### A1: Request is resubmitted (branches at step 1)

1. The system processes the latest valid request and sends a reset email. Resubmission does not itself revoke previous links; after any successful reset, all outstanding reset tokens for that Account are invalidated.

## Exception flows

### E1: Token expired, already used or invalidated (branches at step 3)

1. The system refuses the reset and offers to send a new link.

### E2: Submission fails

1. The system retries up to 3 times, then shows the NFR-06 message.

## Postconditions

- **Success:** The password is replaced, every outstanding token for the Account is unusable, and both events are logged.
- **Failure:** The old password stays valid.

## Open questions

- Token lifetime and password complexity remain open in DEC-61. No number is assumed.
