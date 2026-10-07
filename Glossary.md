## 1.4 Glossary

This report uses the following capitalised terms consistently in the requirements, use cases and diagrams. The last column gives the requirement that defines or uses the term most precisely.

| Term | Meaning | Defined in |
|---|---|---|
| **Staff** | Field employees who receive Assignments: Drivers and Technicians. Managers are not Staff. | FR-01; §3.1 |
| **Manager** | Office-based user who records Jobs, forms Crews, allocates and publishes the Weekly Roster, and decides Staff requests. There may be several Manager accounts with the same rights. | FR-01, FR-41 |
| **IT Administrator** | User who creates accounts, changes roles, deactivates and unlocks accounts, and views the Audit Log. | FR-02, FR-04, FR-05, FR-66 |
| **Driver** | Staff member who drives a Van. The only role allowed to drive. | FR-30 |
| **Technician** | Staff member holding a Certification for one or both Brands. A Technician never drives. | FR-10, FR-30 |
| **Single-Brand Technician** | A Technician certified for only one Brand: M Electric (5 Technicians) or Dicon (4 Technicians). | FR-10; Brief, The Company, para 4 |
| **Dual-Certified Technician** | A Technician certified for both Brands (2 Technicians). One Dual-Certified Technician can cover a Van's Jobs of both Brands. | FR-10, FR-32; Brief, The Company, para 4 |
| **Brand** | Aircon brand: M Electric or Dicon. | FR-34 |
| **Certification** | A Technician's qualification for a Brand, recorded as Brand, certificate number and expiry date. It is valid for a Job when its expiry date is on or after the Job's date. | FR-10 |
| **Van** | Service vehicle, recorded by number and licence plate. The company currently has six. | FR-27 |
| **Crew** | One Driver and one or two Technicians assigned to one Van for one working day. | FR-30 |
| **Van-day** | One Van on one date, together with its Crew and Jobs. | FR-70 |
| **Job** | One Installation or Servicing task for one Brand at one address, created by the Manager. | FR-34 |
| **Job Type** | Installation or Servicing. | FR-34 |
| **Standard Duration** | The default length of a Job: 1 h per unit for Servicing and 3 h per unit for Installation. The Manager can adjust it. | FR-35 |
| **Linked Jobs** | Jobs of different Brands at the same address. They must be allocated to the same Van on the same date. | FR-36 |
| **Assignment** | A Job placed on a Van for a date. Every Crew member of that Van-day holds the Assignment. | FR-41, FR-53 |
| **Unassigned Job** | A Job with status Unassigned. Cancelled Jobs are not counted. | FR-38, FR-46 |
| **Job Allocation** | The Manager's weekly activity of creating Assignments. | FR-41 |
| **Planning Week** | A Monday-to-Saturday week. "The" Planning Week is the next unpublished one. | FR-41, FR-55 |
| **Weekly Roster** | All Crews and Assignments of one Planning Week. It is Draft until the Manager publishes it, then Published. | FR-49 |
| **Slot** | Half-day unit: Morning or Afternoon. Jobs run within 09:00–18:00 and skip lunch (13:00–14:00). | FR-13, FR-42 |
| **Availability** | A Staff member's per-Slot setting of Available or Unavailable, entered up to one month in advance. A Slot with no entry is Not submitted and counts as unavailable. | FR-13, FR-14 |
| **Availability Deadline** | 18:00 on the Wednesday 12 days before a Planning Week's Monday. After it, that week's Availability and Job Preference are locked. | FR-16 |
| **Late Availability Change Request** | A Staff request to set or change Availability for a locked week, with a reason. The Manager approves or rejects it. | FR-17 |
| **Job Preference** | A Staff member's advisory weekly preference for area, days, Slot and Job Type. A Job that breaks it raises a warning, not a block. | FR-21 |
| **Workload** | Hours credited to a Staff member: Planned Hours of Assigned Jobs plus Actual Hours of Completed Jobs, summed per Planning Week and per calendar month. | FR-53, FR-55 |
| **Travel Allowance** | A fixed 0.5 h added to each Job's hours. | FR-42, FR-53 |
| **Planned Hours / Actual Hours** | Planned Hours are a Job's duration plus the Travel Allowance. Actual Hours are the actual end minus the actual start, plus the Travel Allowance. | FR-53 |
| **Overtime** | Workload strictly above 40 h in a Planning Week. | FR-55 |
| **Job Rejection Request** | A Crew member's request to take a Job off their Van, made after a warning to discuss it with the Manager. The Manager approves or refuses it. | FR-62, FR-63 |
| **Short notice** | A Job Rejection Request submitted when the Job starts in less than 48 hours. | FR-62 |
| **Standby** | A Staff member named by the Manager to back up a working day's Jobs. Not in any Crew that day, and counted as 0 h unless placed in a Crew. | FR-71 |
| **Leave** | Annual leave in full working days: 7 per calendar year, with no carry-over. | FR-25 |
| **Leave Request** | A Staff application for Leave. The Manager approves or rejects it. | FR-22, FR-23 |
| **Workshop Servicing** | A Van's maintenance day, generated from a two-monthly rotation. The Van is unavailable that day. | FR-28 |
| **Needs attention** | A Van-day whose Crew became invalid after a later event, such as approved Leave or an expired Certification. | FR-70 |
| **Landing Page** | The first page after login, specific to each role. | FR-01 |
| **Notification** | A message to a recipient's Landing Page, with a handled state. Staff Notifications are also sent by email and phone. | FR-56, FR-64 |
| **Audit Log** | A record of who changed what and when. Only the IT Administrator can view it. | FR-66 |
