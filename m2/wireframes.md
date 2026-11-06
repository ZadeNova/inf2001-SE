# M2 Wireframe Plan (report §5)

> **Status: Draft v1.0 (2026-11-06).** One screen list for the team to draw (for example in Figma, kept private). Every active use case has at least one screen. Every screen names its use case, requirements and the boundary class it represents, so the report's §5 descriptions and the class diagram match (rubric: "clearly mapped to the corresponding use case(s)").
> Widths: Staff screens at 360 px, Manager and IT Administrator screens at 1366 px (NFR-11).

| ID | Screen | Role | Boundary class | Use case | Requirements | Must show / key interactions |
|---|---|---|---|---|---|---|
| W-01 | Login | All | LoginPage | UC-01 | FR-43, FR-48, NFR-07 | Email and password; "Forgot password" link; new-device code step; locked-account message |
| W-02 | Forgot / reset password | All | LoginPage | UC-02 | FR-47 | Enter email → "If the account exists, a link was sent"; new-password form; expired or used link message |
| W-03 | Manager Landing Page | Manager | LandingPage | UC-10, UC-15 | FR-36, FR-40 | Workload bars for every Driver and Technician with a 40 h line and Overtime highlight (> 40 h); the three lowest-Workload Drivers and Technicians; today's Crews with zones and Standby; Unassigned count; pending Job Rejection Requests; expiring Certifications; "no van CSV" days; current / Planning Week switch |
| W-04 | Job form | Manager | JobPage | UC-05 | FR-01, FR-02, FR-04 | Customer, address, postal code → zone shown read-only; Brand, Job Type, units → duration pre-filled; preferred date and Slot; Delete (customer cancelled) with a confirmation that names the Crew to be notified |
| W-05 | CSV upload | Manager | CsvUploadPage | UC-16 | FR-52, FR-53, FR-54 | Choose type (HR leave / van availability); expected columns; upload; success summary or a row-error list ("Row 4: unknown staff ID T99") with nothing saved |
| W-06 | Job Allocation: Suggested Roster | Manager | JobAllocationPage | UC-07 | FR-26, FR-27, FR-07, FR-08, FR-32, FR-33, FR-34, FR-09, FR-11, FR-30, FR-55 | Week tabs Mon–Sat; "Suggest roster" button; per day: Van 1…n cards (zone dropdown, Driver, 1–2 Technicians with Brand badges), Standby list with source tags (Pick / Central / Leftover), Van count from CSV; Unassigned Jobs panel to drag onto a Crew with a start time; warning pane (override with reason); Publish |
| W-07 | Compare Staff panel | Manager | JobAllocationPage | UC-08 | FR-31 | Up to 3 columns: Availability day and week; Workload this week and last week; Certifications with expiry; Standby pick; location (Crew zone or home zone); activation count. A 4th selection is disabled |
| W-08 | Availability grid | Manager | LandingPage | UC-10 | FR-14 | Staff × next 1 month; colours for Available, Leave / Emergency Leave / MC, Unavailable / Not submitted; Standby-pick marker; legend |
| W-09 | Update Roster and Hours | Manager | UpdateRosterPage | UC-17 | FR-10, FR-57 | Pick date and Crew; "Replace member" (who out, who in, from which Job, reason); per-person hours field with reason; history of Hours Edits for the day |
| W-10 | Standby list | Manager | StandbyListView | UC-17 | FR-56 | For the affected Job: today's Standby Staff ordered by activations (12 months), zone distance and staff ID; each row shows phone, Brands, zone and count; "Phone outside the system, then select" hint |
| W-11 | Staff Landing Page | Driver, Technician | LandingPage | UC-13, UC-15 | FR-35, FR-36, FR-41, FR-42, FR-39, NFR-05 | This week's calendar of Assignments and Standby days; weekly Workload against 40 h; month Workload; notifications list; Assignment detail sheet (customer, address, zone, Brand, units, time, Van number, Crew-mates); offline banner |
| W-12 | Set Availability | Driver, Technician | AvailabilityPage | UC-11 | FR-12, FR-13, FR-15 | Week picker within 1 month; Mon–Sat toggles Available / Unavailable / clear; deadline shown; locked-week message ("contact your Manager") |
| W-13 | Account administration | IT Administrator | AccountAdminPage, AuditLogPage | UC-03, UC-04 | FR-44, FR-45, FR-46, FR-48, FR-22, FR-49 | Create account (role; for a Technician, home zone and 1–2 Certifications with expiry); account list with role change, unlock, deactivate, edit profile; Audit Log search |
| W-14 | Standby Preference | Technician | StandbyPreferencePage | UC-18 | FR-15, FR-51 | Mon–Sat cards, each with an M Electric slot and a Dicon slot; taken slots and days the Technician can't take greyed out; current pick with Change / Withdraw; deadline shown |
| W-15 | Job rejection | Driver, Technician | RequestPage | UC-12 | FR-37 | "Reject" on an Assignment → warning dialog ("Please discuss this with your Manager first", Cancel / Continue) → reason (Personal emergency / Missing equipment or parts / Other + comment) → submitted, status Pending |
| W-16 | Request review | Manager | RequestReviewPage | UC-09 | FR-38 | Pending Job Rejection Requests with Job, date, Crew and reason; Approve / Refuse with optional reason; result shows the Job moving to Unassigned |

## Use case → screen coverage

| UC | Screens |
|---|---|
| UC-01 | W-01 |
| UC-02 | W-02 |
| UC-03, UC-04 | W-13 |
| UC-05 | W-04 |
| UC-07 | W-06 |
| UC-08 | W-07 |
| UC-09 | W-16 |
| UC-10 | W-03, W-08 |
| UC-11 | W-12 |
| UC-12 | W-15 |
| UC-13 | W-11 |
| UC-15 | W-11 (notification list), W-03 (alerts) |
| UC-16 | W-05 |
| UC-17 | W-09, W-10 |
| UC-18 | W-14 |

## Demo flow for the presentation (suggested)

1. W-05: upload the HR and van CSVs.
2. W-06: Suggest roster, set zones, override one warning with a reason, then Publish.
3. W-11: a Technician sees the published week.
4. W-15 → W-16: a Job Rejection Request is submitted and approved.
5. W-09 / W-10: a Crew member drops out; the Manager picks the top Standby and records 5 h.
6. W-03: the Manager sees the updated Workload with the 40 h highlight.
