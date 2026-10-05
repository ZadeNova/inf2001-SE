# UC-03: Create User Account

> **Status: Draft v0.3 (2026-10-03).**

| Field | Value |
|---|---|
| **ID** | UC-03 |
| **Name** | Create User Account |
| **Primary actor** | IT Administrator |
| **Secondary actors** | Email Service |
| **Description** | The IT Administrator creates a Staff or Manager account. |
| **Trigger** | A new Staff member or Manager needs system access. |
| **Linked requirements** | FR-02, FR-10, FR-66, NFR-09, NFR-12 |
| **Source** | Brief R11; INT-ITA [Q: Account info], [Q: Permissions]; INT-MGR [Clarification Q2]; DEC-35; DEC-47; DEC-49; DEC-58 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-04](../diagrams/AD-04-create-user-account.puml); [SD-03](../diagrams/SD-03-create-user-account.puml) |
| **Status** | Draft |

## Preconditions

1. The IT Administrator is logged in.
2. The email address is not already assigned to an account.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Chooses to create an account. | Displays required name, email, contact number and role fields (FR-02). |
| 2 | Enters the details and selects Staff subtype or Manager. | Shows Certification fields when the account is for a Technician (FR-10). |
| 3 | Supplies required Certification details where applicable and submits. | Validates required fields, email uniqueness and role authority (FR-02, NFR-12). |
| 4 | — | Creates the account with an initial password, logs the change and emails the initial login details to the user (FR-02, FR-66, DEC-49). |
| 5 | Reviews the confirmation. | Makes the account available for UC-01. |

## Alternative flows

None.

## Exception flows

### E1: Missing or duplicate data (branches at step 3)

1. The system refuses the account and identifies the invalid fields (FR-02).

### E2: Save fails (branches at step 4)

1. The system follows the NFR-09 retry and failure-message rule.

### E3: Initial-login email fails (branches at step 4)

1. Warn the IT Administrator that email submission failed and offer a resend (DEC-58).
2. Keep the saved account; do not create a second account to resend.

## Postconditions

- **Success:** A valid account exists with the selected role and any initial Technician Certifications.
- **Failure:** No invalid account is created.

## Business rules / notes

- Only the IT Administrator may create accounts or assign roles (NFR-12).
- Ongoing role, account-status and lockout changes belong to UC-04.
- Ongoing Certification maintenance is available through UC-10 under the finalized merged structure (DEC-45).

- If initial-login email submission fails, warn the IT Administrator and offer a resend. The saved account remains available; a channel failure does not undo creation (DEC-58).

## Open questions

- None identified for the current draft.
