# UC-03: Create User Account

> **Status: M2 v1.0 (2026-11-06).** Adds the Technician home zone. Certifications are Brand and expiry only (DEC-75, DEC-77).

| Field | Value |
|---|---|
| **ID** | UC-03 |
| **Name** | Create User Account |
| **Primary actor** | IT Administrator |
| **Secondary actors** | Email Service «system» |
| **Description** | The IT Administrator creates a Staff or Manager account; a Technician also gets a home zone and Certifications. |
| **Trigger** | A new employee joins. |
| **Linked requirements** | FR-44, FR-22, FR-49, NFR-08, NFR-14 |
| **Source** | Brief R11; INT-ITA [Q: Account info]; DEC-35; DEC-49; DEC-75; DEC-77 |
| **Classes** | AccountAdminPage, AccountController, User, Staff, Driver, Technician, Manager, Account, Certification, AuditLog, EmailChannel |
| **Wireframe** | W-13 IT Admin account creation |
| **Status** | Agreed |

## Preconditions

1. The IT Administrator is logged in.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens Create Account and enters name, email, contact number and role. | Shows the role-specific fields. |
| 2 | For a Technician, picks the home zone and adds one or two Certifications (Brand, expiry date). | Validates required fields (FR-44, FR-22). |
| 3 | Submits. | `AccountController.createAccount()` creates the User subclass, Account and Certifications and logs the change (FR-49). |
| 4 | — | Emails the initial login details through Email Service (DEC-49). |

## Exception flows

### E1: Missing field, duplicate email, Technician without home zone or Certification (branches at step 3)

1. The system refuses the save and highlights the field.

### E2: Save fails (branches at step 3)

1. The system follows the NFR-06 retry and failure-message rule.

### E3: Initial-login email fails (branches at step 4)

1. Warn the IT Administrator that email submission failed and offer a resend.
2. Keep the saved account; do not create a second account to resend.

## Postconditions

- **Success:** The account exists and the user can log in.
- **Failure:** No account is created.
