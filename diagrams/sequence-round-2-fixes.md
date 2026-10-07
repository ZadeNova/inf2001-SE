# Opus round-2 correction response — 22 SDs

Date: 2026-10-05. Branch: CL/sequence-diagrams. This is a local draft for Opus review. Google Docs has not been edited.

| Finding | Resolution and evidence |
|---|---|
| B1 | DEC-48 to DEC-57 already existed locally, including DEC-53 analysis classes and DEC-55 prior split. The ZIP includes the local decision file. Append DEC-58 to DEC-63; open token/complexity questions cite DEC-61 and acknowledgement/deduplication questions cite DEC-62. Main-branch integration/human PR review remain pending; no merge is claimed. |
| M1 | SD-15 partitions by affected week; Draft roster payloads create no Staff message/email/SMS. Request decisions and Published events still deliver after commit. |
| M2 | User confirmed keeping 22. Clock expiry is drawn in SD-16; independent Job-start lapse is drawn in SD-22. DEC-59 records at-Job-start and 00:00 expiry checking, inclusive expiry-date validity. No SD-26 reuse or SD-31. |
| M3 | SD-20 queries requester:Staff.leaveBalance inside the atomic approval, refuses excess, and serializes recheck/deduction per Staff/year. |
| M4 | SD-20/21 and Certification edit in SD-10 call SD-16 within their atomic saves. Callable SD-16 mutates/audits and returns events; caller notifies only after commit. Clock branch has its own atomic save. |
| M5 | SD-01→02 ref spans User/LoginPage/AuthController/Account/AuditLog/Email Service. SD-17→08 spans Manager/JobAllocationPage/RosterController; SD-08 gate enters/returns through the active page. |
| M6 | Existing DEC-57 and eight Withdrawn rows are retained. SD-07/09/12 remain retired; replacement coverage is SD-17/18/19, SD-20/21/22 and SD-23/24/25. |
| M7 | SD-04 removes future Crew membership, marks Needs attention (explicit member choice, DEC-60), unassigns future Jobs and audits atomically, then notifies eligible affected Staff. FR-04/05 cleanup stays distinct from FR-70, which keeps Jobs. |
| m1 | maxMessageSize/wrapWidth 300; canonical lifeline labels have no forced breaks. Keep 22 as requested; export sizes are recorded in verification. |
| m2 | SD-06 self-call recordConflict collects clashes; no controller-ending return inside the generation loop. |
| m3 | Removed unused Standby lifeline from SD-16; RosterController queries eligibility. |
| m4 | SD-01 uses generic login failure and refuses invalid/expired confirmation without a session. |
| m5 | SD-03 warns the IT Administrator on initial-login email failure and offers resend. |
| m6 | SD-05 checks linked Jobs' Brands, address and existing placements before link mutation. |
| m7 | SD-11 has an explicit Staff requestLateChange action. Blank Slots create Availability in SD-11 and late approval SD-21. |
| m8 | SD-20 uses mutually exclusive failed/committed branches and states that approved Leave is Unavailable. |
| m9 | SD-22 audits/notifies new lapse. SD-25 creates with shortNotice and atomically rechecks one Pending request per Assignment. Less than 48 h is Short notice; exactly 48 h is normal. |
| m10 | SD-23/25 start with Staff navigation. SD-24 keeps a gate because SD-11 references it. |
| m11 | SD-13 has a current-week Draft branch with no Draft Assignment disclosure. |
| m12 | NotificationKind distinguishes Manager DashboardAlert from StaffMessage in CD-domain (DEC-63); SD-10 alerts do not go through SD-15. No Alert class is added. |

The SRS, binding brief, five approved UCD/activity sources and the previous ZIP remain unchanged. Local class views are supporting analysis artifacts; the report class diagram is not edited.

Open implementation policy questions are recorded, not silently resolved. Existing other UC questions remain pending where no review fix needed a choice. Do not infer that this ZIP has already received Opus approval.
