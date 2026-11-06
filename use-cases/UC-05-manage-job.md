# UC-05: Manage Job

> **Status: M2 v1.0 (2026-11-06).** The zone comes from the postal code. A customer cancellation deletes the Job. Linked Jobs and Completed status are removed (DEC-76, DEC-77, DEC-90).

| Field | Value |
|---|---|
| **ID** | UC-05 |
| **Name** | Manage Job |
| **Primary actor** | Manager |
| **Secondary actors** | Email Service, SMS Gateway «system» through UC-15 |
| **Description** | The Manager creates, edits or deletes a customer Job. |
| **Trigger** | A customer books, changes or cancels a service. |
| **Linked requirements** | FR-01, FR-02, FR-04, FR-05, FR-34, FR-50 |
| **Source** | INT-MGR [Process Q2], [added follow-up: cancellations]; DEC-11; DEC-22; DEC-76; DEC-77 |
| **Classes** | JobPage, JobController, RuleValidator, NotificationService, Job, Assignment, AuditLog |
| **Wireframe** | W-04 Job form |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in.

## Main flow (basic path): create

| Step | Actor | System |
|---|---|---|
| 1 | Opens New Job and enters the customer, address, postal code, Brand, Job Type, units, preferred date and Slot. | Pre-fills the duration from `JobController.standardDuration()` (FR-02). |
| 2 | Adjusts the duration if needed and saves. | `JobController.createJob()` creates the Job as Unassigned, and `Job.deriveZone()` sets its zone from the postal code (FR-01). |

## Alternative flows

### A1: Edit (branches at step 1)

1. The Manager changes a future Job. `Job.changeDetails()` runs and, if the Job is Assigned, `RuleValidator.checkBlocking()`.
2. If the edit breaks a rule, `Job.markUnassigned(reason)` runs and the Manager is told why. If the Job is still Assigned, the Crew is notified (UC-15).

### A2: Customer cancels (branches at step 1)

1. The Manager chooses Delete and confirms.
2. If the Job is Assigned, its Crew is notified through UC-15 first. `JobController.deleteJob()` then removes the Job and its Assignment and logs it (FR-04).

## Exception flows

### E1: Invalid field (branches at step 2)

1. Units below 1, a Sunday date, a missing field or an unknown postal sector → the save is refused.

### E2: Past or started Job (branches at A1 or A2)

1. No edit or delete is offered (FR-50).

### E3: Save fails

1. The system follows NFR-06.

## Postconditions

- **Success:** The Job is saved, changed or deleted, and the change is logged.
- **Failure:** The Job is unchanged.
