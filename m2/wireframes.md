# M2 Wireframe Plan (report §5)

> **Status: Draft v1.1 (2026-11-07).** One screen list for the team to draw (for example in Figma, kept private). Every active use case has at least one screen. Every screen names its use case, requirements and the boundary class it represents, so the report's §5 descriptions and the class diagram match (rubric: "clearly mapped to the corresponding use case(s)").
> Widths: Staff screens at 360 px, Manager and IT Administrator screens at 1366 px (NFR-11).

| ID | Screen | Role | Boundary class | Use case | Requirements | Must show / key interactions |
|---|---|---|---|---|---|---|
| W-01 | Login | All | LoginPage | UC-01 | FR-43, FR-48, NFR-07 | Email and password; "Forgot password" link; new-device code step; locked-account message |
| W-02 | Forgot / reset password | All | LoginPage | UC-02 | FR-47 | Enter email → "If the account exists, a link was sent"; new-password form; expired or used link message |
| W-03 | Manager Landing Page | Manager | LandingPage | UC-10, UC-15 | FR-36, FR-40 | Total Credited Workload bars with a 40 h target and >40 h highlight; separate Active Hours; lowest-Workload Drivers/Technicians; activated-day counts; today's Crews/coverage and Standby; staffing shortage and missing CSV alerts; Unassigned Jobs and rejection requests |
| W-04 | Job form | Manager | JobPage | UC-05 | FR-01, FR-02, FR-04 | Customer, address, postal code → zone shown read-only; Brand, Job Type, units → duration pre-filled; preferred date and Slot; Delete (customer cancelled) with a confirmation that names the Crew to be notified |
| W-05 | CSV upload | Manager | CsvUploadPage | UC-16 | FR-52, FR-53, FR-54 | Choose type (HR leave / van availability); expected columns; upload; success summary or a row-error list ("Row 4: unknown staff ID T99") with nothing saved |
| W-06 | Job Allocation: Suggested Roster | Manager | JobAllocationPage | UC-07 | FR-26, FR-27, FR-07, FR-08, FR-32, FR-33, FR-34, FR-09, FR-11, FR-30, FR-55 | Suggest roster first resolves provisional requests after locked inputs/CSV checks. Show Confirmed/NotConfirmed with reasons, >=3 Crew check, Full Standby cover and Van capacity. Crew cards: multi-select coverage Zones, initial members/Brand badges. Show per-Job effective members, direct duties separately, Standby tags (Preference / Algorithm / Leftover / Manager). Confirmed picks have no override control. Refuse destructive regeneration. Publish blocked for insufficient Crews or hard violations |
| W-07 | Compare Staff panel | Manager | JobAllocationPage | UC-08 | FR-31 | Up to three Staff: Availability, Active Hours and Total Credited Workload this/last week, Certifications, preference status/reason, current duty/coverage or home Zone, distinct activated-day count |
| W-08 | Availability grid | Manager | LandingPage | UC-10 | FR-14 | Staff × next month: availability/Leave/not-submitted states; distinct provisional/confirmed/not-confirmed preference markers and reasons; later Leave overrides placement visibly |
| W-09 | Update Roster and Hours | Manager | UpdateRosterPage | UC-17 | FR-10, FR-57 | Choose direct extra Job or Crew replacement. Replacement: outgoing Technician, eligible incoming Technician, first unstarted Job and reason; show earlier attribution read-only. Direct: Job/start time/Technician, paid transport/no Van. Show Active and Total Credited Hours, 4 h floor and once-per-day count. Edit Active Hours only (0–24, reason); retain history |
| W-10 | Standby list | Manager | StandbyListView | UC-17 | FR-56 | Eligible candidates only, checking every remaining replacement Job or selected direct Job before sorting. Show valid Brands, home Zone/distance, activated dates, Active/Credited Hours and commitments. Highlight recommended candidate; phone outside system and recheck on save. Explain no eligible candidate; do not label low counts as lazy |
| W-11 | Staff Landing Page | Driver, Technician | LandingPage | UC-13, UC-15 | FR-35, FR-36, FR-41, FR-42, FR-39, NFR-05 | Published Crew/direct Assignments with per-Job attributed Staff; original Standby date and activation indicator; weekly Total Credited Workload against 40 h, separate Active Hours, monthly total. Preference status/reason visible even before publication. Direct duties labelled paid transport/no Van. Notifications and offline banner |
| W-12 | Set Availability | Driver, Technician | AvailabilityPage | UC-11 | FR-12, FR-13, FR-15 | Week picker within 1 month; Mon–Sat toggles Available / Unavailable / clear; deadline shown; locked-week message ("contact your Manager") |
| W-13 | Account administration | IT Administrator | AccountAdminPage, AuditLogPage | UC-03, UC-04 | FR-44, FR-45, FR-46, FR-48, FR-22, FR-49 | Create account (role; for a Technician, home zone and 1–2 Certifications with expiry); account list with role change, unlock, deactivate, edit profile; Audit Log search |
| W-14 | Standby Preference | Technician | StandbyPreferencePage | UC-18 | FR-15, FR-51 | One provisional request per week; one slot per Brand/day. Show provisional reservation, Change/Withdraw before deadline and submission order. Explain that confirmation follows locked inputs/CSV staffing checks. Show Confirmed or NotConfirmed with reason; confirmed means initial Standby and remains callable |
| W-15 | Job rejection | Driver, Technician | RequestPage | UC-12 | FR-37 | "Reject" on an Assignment → warning dialog ("Please discuss this with your Manager first", Cancel / Continue) → reason (Personal emergency / Missing equipment or parts / Other + comment) → submitted, status Pending |
| W-16 | Request review | Manager | RequestReviewPage | UC-09 | FR-38 | Pending rejection requests with Job/date, Crew or direct Technician, reason; Approve/Refuse and notify attributed Staff. Approved Job becomes Unassigned |

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
5. W-09 / W-10: filter eligible Standby; activate a direct 2 h duty (2 Active/4 Credited/count +1), then a 3 h duty (5/5/count unchanged). Demonstrate a separate replacement from Job 2 preserving Job 1's Staff.
6. W-03: the Manager sees the updated Workload with the 40 h highlight.

**Consistency checks (DEC-96–98):** never label a provisional request guaranteed; do not offer a confirmed-pick override; do not award 4+active hours; distinguish per-Job members from initial Crew; confirm that SC-01–15 in testing.md can be demonstrated. These are screen specifications, not a claim that finished wireframe screenshots exist.
