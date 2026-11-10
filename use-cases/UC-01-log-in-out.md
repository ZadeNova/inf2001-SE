# UC-01: Log In/out

> **Status: M2 v1.0.1 (2026-11-10).** Updated for SRS v4.1.1; the logout cache lifecycle follows DEC-102. Reset Password is now a standalone use case, not an extension (DEC-91).

| Field | Value |
|---|---|
| **ID** | UC-01 |
| **Name** | Log In/out |
| **Primary actor** | User |
| **Secondary actors** | Email Service «system» (new-device confirmation) |
| **Description** | A User signs in to reach the role-specific Landing Page and ends the session when finished. |
| **Trigger** | The User opens the web application or chooses Log Out. |
| **Linked requirements** | FR-43, FR-48, NFR-05, NFR-07, NFR-09, NFR-11 |
| **Source** | Brief R1, R2, R7, R11; INT-ITA [Q: Passwords], [Q: Safeguards], [Q: Permissions]; DEC-17; DEC-18; DEC-41; DEC-91; DEC-102 |
| **Classes** | LoginPage, LandingPage, AuthController, Account |
| **Wireframe** | W-01 Login (m2/wireframes.md) |
| **Status** | Agreed |

## Preconditions

1. The User has an active account.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Enters email and password on the Login page. | `AuthController.logIn()` checks `Account.checkCredentials()` and the account status (FR-48). |
| 2 | — | If `Account.isKnownDevice()` is true, creates a session (NFR-07). |
| 3 | — | Shows the Landing Page for `Account.role` (FR-43). |
| 4 | Chooses Log Out when finished. | `LandingPage.logOut()` clears this Staff member's offline Assignment copy through `clearCachedToday()`, ends the session and returns to the Login page (NFR-05; DEC-102). |

## Alternative flows

### A1: New device (branches at step 2)

1. The system emails a confirmation code through Email Service (NFR-07).
2. The User enters the code. The system validates it, calls `Account.rememberDevice()` and continues at step 3. A wrong or expired code creates no session.

## Exception flows

### E1: Wrong password (branches at step 1)

1. `Account.recordFailedAttempt()` runs. On the 5th consecutive failure within 15 minutes, `Account.lock()` runs and the User is told to contact the IT Administrator (FR-48).

### E2: Account locked or deactivated (branches at step 1)

1. Login is refused without revealing other details.

## Postconditions

- **Success:** A session exists for the User's role, or the session has ended.
- **Failure:** No session is created.

## Business rules / notes

- The User can open UC-02 from the Login page without logging in. UC-02 is a separate goal, not an extension (DEC-91).
