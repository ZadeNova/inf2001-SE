# UC-15: Notify Staff

> **Status: M2 v1.0 (2026-11-06).** Delivery goes through the «system» actors Email Service and SMS Gateway via the NotificationChannel interface (DEC-88, DEC-91).

| Field | Value |
|---|---|
| **ID** | UC-15 |
| **Name** | Notify Staff |
| **Primary actor** | None (included use case, started by the including use case) |
| **Secondary actors** | Email Service «system»; SMS Gateway «system» |
| **Description** | The system stores a Notification for each affected person, shows it on the Landing Page and sends it by email and SMS. |
| **Trigger** | UC-05, UC-07, UC-09 or UC-17 commits a notifying event (FR-39). |
| **Included by** | UC-05, UC-07, UC-09, UC-17 |
| **Linked requirements** | FR-09, FR-39, NFR-06 |
| **Source** | M2-Brief §3.2; DEC-46; DEC-48; DEC-62; DEC-64; DEC-88 |
| **Classes** | NotificationService, NotificationChannel, EmailChannel, SmsChannel, Notification |
| **Wireframe** | W-11 (notification list); W-03 (Manager alerts) |
| **Status** | Agreed |

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | — | `NotificationService.notify(event, recipients)` skips Staff events for a Draft week (DEC-64). |
| 2 | — | Creates one `Notification` per recipient with what changed, the date and a link (FR-39). |
| 3 | Email Service, SMS Gateway | Each `NotificationChannel.send()` delivers it, and `Notification.markSent(channel)` records the delivery. |

## Exception flows

### E1: A channel fails

1. `Notification.markFailed(channel)`; the message stays on the Landing Page and is retried under NFR-06.
