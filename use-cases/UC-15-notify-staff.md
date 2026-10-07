# UC-15: Notify Staff

> **Status: Draft v0.5 (2026-10-04).** Included system behaviour using Email/Phone.

| Field | Value |
|---|---|
| **ID** | UC-15 |
| **Name** | Notify Staff |
| **Primary actor** | Email/Phone |
| **Secondary actors** | Calling use case |
| **Description** | The system delivers required Landing Page, email and phone notifications to Staff after roster, Crew, Assignment, Standby or request-decision events. |
| **Trigger** | A calling use case commits an FR-64 or FR-71 notification event. |
| **Linked requirements** | FR-49, FR-64, FR-71, NFR-01, NFR-09 |
| **Source** | INT-MGR [added follow-up: notifications], [Conflicts Q5], [added follow-up: cancellations]; INT-DCT [Process Q1 follow-up: updates], [Conflicts Q2]; INT-DRV [Q7]; DEC-42; DEC-43; DEC-45; DEC-46; DEC-47; DEC-48; DEC-50; DEC-56; DEC-58; DEC-59; DEC-62 |
| **Related diagrams** | [UCD-system](../diagrams/UCD-system.puml); [AD-01](../diagrams/AD-01-weekly-roster.puml); [AD-03](../diagrams/AD-03-job-rejection.puml); [SD-15](../diagrams/SD-15-notify-staff.puml) |
| **Status** | Draft |

## Preconditions

1. A calling use case has successfully saved a notification-triggering business event.
2. The recipients can be identified from the saved Crew, Assignment, Standby or request data.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Calling use case supplies the event and recipients. | Builds the notification from the saved event. |
| 2 | - | Adds the notification to each recipient's Landing Page (FR-64). |
| 3 | Email/Phone accepts the outbound notification request. | Generates an email and a phone notification for each recipient (FR-64). |
| 4 | Email/Phone reports whether each delivery request was accepted. | Records the result for both external channels and makes the saved change visible within 60 seconds (NFR-01). |

## Alternative flows

### A1: Weekly Roster publication

1. Notify every Staff member with Assignments or Standby days in the published week.

### A2: Published roster or Crew change

1. Notify removed and added Staff when an Assignment or Crew changes, and notify affected Crew when a Job is changed or cancelled.

### A3: Standby event

1. Notify Staff when named as Standby and when someone they can replace drops out (FR-71).

### A4: Request decision

1. Notify the requester of the saved decision and reason where applicable; also notify a newly saved Job-start lapse (DEC-59).
2. For an approved Job Rejection Request, also notify the other Crew members and eligible Standby Staff.

### A5: Draft roster event

1. Withhold the Draft roster payload and recipients before creating a Landing Page message or sending email/SMS (FR-49, DEC-58).
2. For mixed-week events, process Published and non-roster portions separately.

## Exception flows

### E1: Email or phone delivery submission fails (branches at step 4)

1. After an initial failed send, the system retries the failed email or SMS channel automatically up to three times (NFR-09, DEC-56).
2. If still unsuccessful, it records the failed channel for operational follow-up and preserves the Landing Page notification.

## Postconditions

- **Success:** For eligible Published/non-roster events, each intended recipient has a Landing Page notification, and email and phone notifications have been submitted.
- **Failure:** The saved business event remains committed; failed delivery is visible for operational follow-up.

## Business rules / notes

- The phone channel is SMS; the external actor remains Email/Phone (DEC-48).
- SD-15 shows separate Email Service and SMS Gateway lifelines for the existing external Email/Phone actor (DEC-56).
- UC-15 is included system behaviour; Email/Phone is its external delivery actor in the finalized list.
- Callers include UC-05, UC-06, UC-07 and UC-09; other requirement-defined events may also invoke it.

- SD-15 partitions events by affected week and withholds Draft roster messages on all channels; non-roster request decisions remain visible (DEC-58).
- Notify the requester of a newly saved Job-start lapse (DEC-59). This resolves the earlier lapse-notification question.

## Open questions

- External acknowledgement and delivery deduplication remain open in DEC-62.
