# UC-01: Log In/out

> **Status: Draft v0.1 (2026-10-01).** Based on SRS v3.1 and the finalized list v2.0.

| Field | Value |
|---|---|
| **ID** | UC-01 |
| **Name** | Log In/out |
| **Primary actor** | User |
| **Secondary actors** | Email Service |
| **Description** | A User authenticates to reach the role-specific Landing Page and ends the authenticated session when finished. |
| **Trigger** | The User opens the web application or chooses Log Out. |
| **Linked requirements** | FR-01, FR-07, NFR-10, NFR-12, NFR-14 |
| **Source** | Brief R1, R2, R7, R11; INT-ITA [Q: Passwords], [Q: Safeguards], [Q: Permissions]; DEC-17; DEC-18; DEC-41; DEC-45 |
| **Related diagrams** | Pending OOA and diagram selection |
| **Status** | Draft |

## Preconditions

1. The User has an active account.
2. The web application is available in a supported browser.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the login page and enters credentials. | Validates the credentials and account status (FR-07). |
| 2 | Confirms the login. | If the device was used within the last 30 days, creates an authenticated session (NFR-10). |
| 3 | — | Displays the Landing Page for the User's role (FR-01). |
| 4 | Chooses Log Out when finished. | Ends the authenticated session and returns to the login page (DEC-45). |

## Alternative flows

### A1: New or unremembered device (branches at step 2)

1. The system sends an email confirmation and pauses login (NFR-10).
2. The User follows the confirmation step.
3. The system authenticates the User and continues at step 3.

### A2: Forgotten password (branches at step 1)

1. The User invokes UC-02 Reset Password.
2. After resetting the password, the User resumes at step 1.

## Exception flows

### E1: Invalid credentials or locked account (branches at step 2)

1. The system refuses login and records the failed attempt (FR-07).
2. After five consecutive failures within 15 minutes, the account is locked until the IT Administrator unlocks it.

### E2: Inactive account (branches at step 2)

1. The system refuses login without creating a session (FR-05).

## Postconditions

- **Success:** An authenticated session exists and the correct Landing Page is displayed, or the selected session has been ended.
- **Failure:** No authenticated session is created and protected data remains unavailable.

## Business rules / notes

- Access after login follows the SRS permission matrix (NFR-12).
- Password-reset behaviour belongs to UC-02.
- Logout was added by the finalized team structure and is traced to DEC-45.

## Open questions

- None identified for the current draft.
