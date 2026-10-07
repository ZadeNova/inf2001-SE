# Current Technician questionnaire

## Provenance

Primary source: [INF2001 Air-con Technician Requirements Questionnaire (Responses)](https://docs.google.com/spreadsheets/d/1TU2Pv0-ahIVvNoVVaNKNX6l9tSZ-i5tLSPNE9FemRvw/edit?gid=959930065#gid=959930065), Form Responses 1, A1:AA12. Inspected on 2026-10-07 without editing the Sheet or its permissions.

The requesting member identified this Sheet as the current source, superseding the older DCT interview for current Technician findings. The older transcript is retained as historical evidence. The Sheet contains 11 response records: DB01 and DB02 are dual-Brand; ME01-ME05 represent M Electric; DI01-DI04 represent Dicon. Response timestamps are displayed as `10/1/2026 17:46:24` through `10/1/2026 17:50:18`; that display is preserved without guessing a date locale. Participant IDs are not assumed to be confirmed real names or attendance records.

Citation format: `INT-DCT [Questionnaire C18: DB01]` identifies a question and response ID in this current Sheet. `INT-DCT [Questionnaire C18]` covers responses to that question across both Technician roles. The `Questionnaire` qualifier distinguishes these citations from historical transcript tags.

## Question set (verbatim, trailing whitespace removed)

- P1. Which Technician role are you representing?
- P2. Participant name or agreed participant ID
- S1. Which Brand are you certified for or representing?
- S2. How is work currently divided when your Crew handles Jobs for different Brands
- D1. How does being qualified for both brands affect the work you are assigned?
- D2. What should the Manager check before moving you to cover another Technician’s work?
- C1. How do you currently receive and check your assigned Jobs and schedule changes?
- C2. How do you currently apply for Leave?
- C3. How do you currently inform the Manager of your availability?
- C4. What difficulties, if any, do you encounter when submitting Leave requests or updating your availability?
- C5. Which Job details do you need to find quickly before starting work? Select all that apply.
- C6. In what units do you currently provide your availability? Select all that apply
- C7. What Job preferences, if any, do you currently communicate to the Manager?
- C8. What difficulties, if any, would the proposed submission deadline cause?
- C9. How are your working hours currently calculated or recorded?
- C10. What information would you need in a weekly or monthly work calendar to understand your schedule and workload?
- C11. What information do you need to track your Leave Request from submission to a decision?
- C12. What do you currently do when your availability changes after the submission deadline?
- C13. What should the system show about your Availability while a late-change request is pending and after a decision?
- C14. In what situations would you need to ask the Manager to remove or reassign an assigned Job?
- C15. What practical problems, if any, could arise while waiting for the Manager to decide a Job Rejection Request?
- C16. What information must a notification contain for you to act on a change or request decision?
- C17. How do you currently record and report that a Job has been completed?
- C18. What feedback do you need to know whether an offline completion is waiting to upload, has been saved, or has failed?
- C19. What device, browser/application and connection would you normally use at work?
- C20. What important need or concern have these questions missed?

## Exact excerpts supporting the refinements

### D2 / DB01

> Check that both certificates are valid for the Job date, my Availability and existing Jobs, travel time, the tools and parts needed, and whether moving me leaves my original Crew without the required Brand coverage. Confirm the revised schedule with everyone affected.

### C13 / DB01

> Show the current Availability and the proposed change with a pending status. After approval, update it and notify me; if refused, keep the current slot and explain the decision.

### C13 / DB02

> Keep the original Availability visible while pending. Show the requested slot and decision separately so I do not mistake a request for an approved change.

### C16 / DB01

> Which Job changed, its Brand and date, the new time or Crew, what happens to my previous assignment, and a link to the current roster. Request decisions should include the reason.

### C18 / DB01

> Show each queued Job and whether its invoice photo is included. Confirm receipt after reconnecting, preserve failed uploads for retry and prevent a second completion being created by repeated taps.

### C18 / DB02

> Use clear words: saved on this device, waiting to upload, received, or failed. If only the photo fails, tell me that and let me retry it without losing the completed details.

### C9 / DB02

> I write the actual Job times and notes and pass them to the office. I am not certain how breaks and travel are reflected in the total, so I would want that explained in the workload view.

### C10 / DB01

> Show each Job’s Brand, timing and status, plus daily and weekly hours. A monthly total and assigned/completed Job counts help, but counts alone are misleading when I handle a long installation. Mark locked Availability separately.

### C8 / DB02

> The deadline is generally fine for planned commitments. I need a clear late-change process for unexpected events and a reminder showing exactly which week is about to lock.

## Analysis summary (team interpretation, not verbatim answers)

The responses support Manager-decided requests with operational data unchanged while Pending. They ask for original/proposed late-change visibility, meaningful change/decision messages and clear per-Job offline completion/photo feedback with retained retry data and no duplicate completion. C19 includes Android and iOS phones using Chrome, Firefox or Edge and a Windows/Edge laptop; the existing NFR-14 platform coverage remains sufficient.

The new responses do not independently confirm the adopted fixed Travel Allowance, exact Workload formula, 40-hour threshold or Standard Durations. Those remain grounded in the brief, Manager/Driver sources and existing decisions. Availability reminders, additional calendar statistics/overlays, request-history timestamps and mandatory refusal explanations remain scope questions in DEC-70. This source adds no inventory or equipment-management use case.
