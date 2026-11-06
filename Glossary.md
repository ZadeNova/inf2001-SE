> **Source:** transcribed from §1.4 of the submitted M1 report (9 Oct 2026), the M1 source of truth (DEC-72). This replaces the 7 Oct draft export, whose "Defined in" column used draft requirement IDs.

## 1.4 Glossary

This report uses the following capitalised terms consistently in the requirements, use cases and diagrams. The last column gives the requirement that defines or uses the term most precisely.

*Table 1.3 – Glossary*

| Term | Meaning | Defined in |
|---|---|---|
| **Staff** | Field employees who receive Assignments: Drivers and Technicians. Managers are not Staff. | FR-43 |
| **Manager** | Office-based user who records Jobs, forms Crews, allocates and publishes the Weekly Roster, and decides Staff requests. There may be several Manager accounts with the same rights. | FR-43, FR-07 |
| **IT Administrator** | User who creates accounts, changes roles, deactivates and unlocks accounts, and views the Audit Log. | FR-44, FR-45, FR-46, FR-49 |
| **Driver** | Staff member who drives a Van. The only role allowed to drive. | FR-26 |
| **Technician** | Staff member holding a Certification for one or both Brands. A Technician never drives. | FR-22, FR-26 |
| **Single-Brand Technician** | A Technician certified for only one Brand: M Electric (5 Technicians) or Dicon (4 Technicians). | FR-22; Project Brief |
| **Dual-Certified Technician** | A Technician certified for both Brands (2 Technicians). One Dual-Certified Technician can cover a Van's Jobs of both Brands. | FR-22, FR-27; Project Brief |
| **Brand** | Aircon brand: M Electric or Dicon. | FR-01 |
| **Certification** | A Technician's qualification for a Brand, recorded as Brand, certificate number and expiry date. It is valid for a Job when its expiry date is on or after the Job's date. | FR-22 |
| **Van** | Service vehicle, recorded by number and licence plate. The company currently has six. | FR-23 |
| **Crew** | One Driver and one or two Technicians assigned to one Van for one working day. | FR-26 |
| **Van-day** | One Van on one date, together with its Crew and Jobs. | FR-29 |
| **Job** | One Installation or Servicing task for one Brand at one address, created by the Manager. | FR-01 |
| **Job Type** | Installation or Servicing. | FR-01 |
| **Standard Duration** | The default length of a Job: 1 h per unit for Servicing and 3 h per unit for Installation. The Manager can adjust it. | FR-02 |
| **Linked Jobs** | Jobs of different Brands at the same address. They must be allocated to the same Van on the same date. | FR-03 |
| **Assignment** | A Job placed on a Van for a date. Every Crew member of that Van-day holds the Assignment. | FR-07, FR-35 |
| **Unassigned Job** | A Job with status Unassigned. Cancelled Jobs are not counted. | FR-05, FR-34 |
| **Job Allocation** | The Manager's weekly activity of creating Assignments. | FR-07 |
| **Planning Week** | A Monday-to-Saturday week. "The" Planning Week is the next unpublished one. | FR-07, FR-36 |
| **Weekly Roster** | All Crews and Assignments of one Planning Week. It is Draft until the Manager publishes it, then Published. | FR-09 |
| **Slot** | Half-day unit: Morning or Afternoon. Jobs run within 09:00–18:00 and skip lunch (13:00–14:00). | FR-12, FR-08 |
| **Availability** | A Staff member's per-Slot setting of Available or Unavailable, entered up to one month in advance. A Slot with no entry is Not submitted and counts as unavailable. | FR-12, FR-13 |
| **Availability Deadline** | 18:00 on the Wednesday 12 days before a Planning Week's Monday. After it, that week's Availability and Job Preference are locked. | FR-15 |
| **Late Availability Change Request** | A Staff request to set or change Availability for a locked week, with a reason. The Manager approves or rejects it. | FR-16 |
| **Job Preference** | A Staff member's advisory weekly preference for area, days, Slot and Job Type. A Job that breaks it raises a warning, not a block. | FR-17 |
| **Workload** | Hours credited to a Staff member: Planned Hours of Assigned Jobs plus Actual Hours of Completed Jobs, summed per Planning Week and per calendar month. | FR-35, FR-36 |
| **Travel Allowance** | A fixed 0.5 h added to each Job's hours. | FR-08, FR-35 |
| **Planned Hours / Actual Hours** | Planned Hours are a Job's duration plus the Travel Allowance. Actual Hours are the actual end minus the actual start, plus the Travel Allowance. | FR-35 |
| **Overtime** | Workload strictly above 40 h in a Planning Week. | FR-36 |
| **Job Rejection Request** | A Crew member's request to take a Job off their Van, made after a warning to discuss it with the Manager. The Manager approves or refuses it. | FR-37, FR-38 |
| **Short notice** | A Job Rejection Request submitted when the Job starts in less than 48 hours. | FR-37 |
| **Standby** | A Staff member named by the Manager to back up a working day's Jobs. Not in any Crew that day, and counted as 0 h unless placed in a Crew. | FR-30 |
| **Leave** | Annual leave in full working days: 7 per calendar year, with no carry-over. | FR-21 |
| **Leave Request** | A Staff application for Leave. The Manager approves or rejects it. | FR-18, FR-19 |
| **Workshop Servicing** | A Van's maintenance day, generated from a two-monthly rotation. The Van is unavailable that day. | FR-24 |
| **Needs attention** | A Van-day whose Crew became invalid after a later event, such as approved Leave or an expired Certification. | FR-29 |
| **Landing Page** | The first page after login, specific to each role. | FR-43 |
| **Notification** | A message to a recipient's Landing Page, with a handled state. Staff Notifications are also sent by email and phone. | FR-40, FR-39 |
| **Audit Log** | A record of who changed what and when. Only the IT Administrator can view it. | FR-49 |
