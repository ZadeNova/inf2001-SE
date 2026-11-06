# UC-01: Log In/out

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-01 |
| **Name** | Log In/out |
| **Primary actor** | User |
| **Secondary actors** | Email Service |
| **Description** | A User authenticates to reach the role-specific Landing Page and ends the authenticated session when finished. |
| **Trigger** | The User opens the web application or chooses Log Out. |
| **Linked requirements** | FR-43, FR-48, NFR-07, NFR-09, NFR-11 |
| **Source** | Brief R1, R2, R7, R11; INT-ITA [Q: Passwords], [Q: Safeguards], [Q: Permissions]; DEC-17; DEC-18; DEC-41; DEC-45; DEC-58; DEC-61; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [SD-01](../diagrams/SD-01-log-in-out.puml) |
| **Status** | Agreed |

## Preconditions

1. The User has an active account.
2. The web application is available in a supported browser.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens the login page and enters credentials. | Validates the credentials and account status (FR-48). |
| 2 | Confirms the login. | If the device was used within the last 30 days, creates an authenticated session (NFR-07). |
| 3 | — | Displays the Landing Page for the User's role (FR-43). |
| 4 | Chooses Log Out when finished. | Ends the authenticated session and returns to the login page. |

## Alternative flows

### A1: New or unremembered device (branches at step 2)

1. The system sends an email confirmation and pauses login (NFR-07).
2. The User follows the confirmation step.
3. The system validates the email confirmation before authenticating; a wrong or expired code creates no session.

### A2: Forgotten password (branches at step 1)

1. The User invokes UC-02 Reset Password.
2. After resetting the password, the User resumes at step 1.

## Exception flows

### E1: Invalid credentials or locked account (branches at step 2)

1. The system refuses login and records the failed attempt (FR-48).
2. After five consecutive failures within 15 minutes, the account is locked until the IT Administrator unlocks it.

### E2: Inactive account (branches at step 2)

1. The system refuses login without creating a session (FR-46).

## Postconditions

- **Success:** An authenticated session exists and the correct Landing Page is displayed, or the selected session has been ended.
- **Failure:** No authenticated session is created and protected data remains unavailable.

## Business rules / notes

- Access after login follows the SRS permission matrix (NFR-09).
- Password-reset behaviour belongs to UC-02.
- Log Out ends the session and returns the User to the login page.
- Generic failure wording covers missing, locked, inactive and invalid-password accounts. Invalid or expired new-device confirmation creates no session. Confirmation-code lifetime is open.

## Open questions

- Confirmation-code lifetime remains open.
