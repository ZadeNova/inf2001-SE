# UC-03: Create User Account

> **Status: M1 submitted v1.0 (2026-11-07).** Transcribed from §3.2 of the submitted M1 report (9 Oct 2026), which is the M1 source of truth (DEC-72). The Source row is kept from the repo; the report does not print it.

| Field | Value |
|---|---|
| **ID** | UC-03 |
| **Name** | Create User Account |
| **Primary actor** | IT Administrator |
| **Secondary actors** | Email Service |
| **Description** | The IT Administrator creates a Staff or Manager account. |
| **Trigger** | A new Staff member or Manager needs system access. |
| **Linked requirements** | FR-44, FR-22, FR-49, NFR-06, NFR-09 |
| **Source** | Brief R11; INT-ITA [Q: Account info], [Q: Permissions]; INT-MGR [Clarification Q2]; DEC-35; DEC-47; DEC-49; DEC-58; DEC-72 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-04](../diagrams/AD-04-create-user-account.puml); [SD-03](../diagrams/SD-03-create-user-account.puml) |
| **Status** | Agreed |

## Preconditions

1. The IT Administrator is logged in.
2. The email address is not already assigned to an account.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Chooses to create an account. | Displays required name, email, contact number and role fields (FR-44). |
| 2 | Enters the details and selects Staff subtype or Manager. | Shows Certification fields when the account is for a Technician (FR-22). |
| 3 | Supplies required Certification details where applicable and submits. | Validates required fields, email uniqueness and role authority (FR-44, NFR-09). |
| 4 | — | Creates the account with an initial password, logs the change and emails the initial login details to the user (FR-44, FR-49). |
| 5 | Reviews the confirmation. | Makes the account available for UC-01. |

## Alternative flows

None.

## Exception flows

### E1: Missing or duplicate data (branches at step 3)

1. The system refuses the account and identifies the invalid fields (FR-44).

### E2: Save fails (branches at step 4)

1. The system follows the NFR-06 retry and failure-message rule.

### E3: Initial-login email fails (branches at step 4)

1. Warn the IT Administrator that email submission failed and offer a resend.
2. Keep the saved account; do not create a second account to resend.

## Postconditions

- **Success:** A valid account exists with the selected role and any initial Technician Certifications.
- **Failure:** No invalid account is created.

## Business rules / notes

- Only the IT Administrator may create accounts or assign roles (NFR-09).
- Ongoing role, account-status and lockout changes belong to UC-04.
- Ongoing Certification maintenance is done by the Manager in UC-10.
- If initial-login email submission fails, warn the IT Administrator and offer a resend. The saved account remains available; a channel failure does not undo creation.

## Open questions

- None.
