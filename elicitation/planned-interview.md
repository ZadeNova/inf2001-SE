# Planned follow-up interviews: SRS v3.0 validation

> **Purpose:** validate the parts of the SRS (v3.0, tag `srs-v3.0`) that go **against** or **beyond** what stakeholders said in the first interviews, and replace the team-set numbers (†) with stakeholder answers.
> **Status:** planned, not yet held. Owner: ______ · Target: before stakeholder engagement closes (end of Week 6; see DEC-27).

## 1. Ground rules

- **New sessions, new records.** Each session is recorded as a new meeting note, `elicitation/MTG-nn-<date>.md`, made from [MEETING-TEMPLATE.md](MEETING-TEMPLATE.md), with date, mode and attendance. **The original transcripts in `interviews/` are never edited.**
- **The rep answers in character.** Give each rep their persona brief (§3) beforehand. They may **accept, adjust or reject** each point, as Appendix A allows ("The Stakeholder Representative is allowed to add requirements as they deem fit"). Don't script their answers.
- **Record what is actually said.** Quote exactly where possible, and mark the team's interpretation as *[Team note]*.
- **Ask neutrally.** Describe the current design, then ask whether it works. Don't lead ("You agree that…?").
- **Priorities:** ⭐ items must be covered. The rest are covered if time allows.

## 2. Session plan

| Session | Rep (role played) | Length | Items | Why this person |
|---|---|---|---|---|
| MTG-01 | Manager | 30 min | V-01 to V-18 | Owns the process. Most team decisions go against or beyond the Manager's answers |
| MTG-02 | IT Administrator | 20 min | T-01 to T-14 | All team-set † numbers are theirs to confirm |
| MTG-03 | Dual Certified Technician **or** Driver | 15 min | S-01 to S-09 | The Staff-side view of the rejection flow, Standby and Workload |

Two of these can be combined into one sitting if needed, but keep a separate record per rep.

## 3. Persona briefs (send before the session)

**All reps.** You are playing a stakeholder of an aircon retailer's service team (6 Vans, 6 Drivers, 11 Technicians, two Brands: M Electric and Dicon). The team has turned the first interviews into a requirements specification. Some decisions go beyond or against what your character said. Please react **in character**: say whether each works for you, what you'd change, and why. There are no right answers.

- **Manager:** you are the operations manager who plans the weekly roster (your earlier answers are in `interviews/manager.md`). You care most about "Allocating jobs with valid crews, and seeing the workload at a glance".
- **IT Administrator:** you manage accounts, security and backups (your earlier answers are in `interviews/ita.md`). You care most about "The access permission allocation, backups, and transferring of old data into the new system."
- **Technician or Driver:** you work in the field on a van crew (earlier answers are in `interviews/dct.md` and `interviews/driver.md`).

## 4. MTG-01: Manager validation

| # | SRS rows (DEC) | What the SRS says now | What was said before | Question to ask |
|---|---|---|---|---|
| ⭐ V-01 | FR-62, FR-63 (DEC-42) | Every Job Rejection is a **request the Manager approves**. The Job stays assigned until the Manager decides. A request still pending when the Job starts lapses | "It doesn't need my approval to go through, but the job goes back to unassigned, and I get notified straight away so I can reassign it." (Conflicts Q3) | "In the current design, every rejection comes to you to approve, and the Job stays with the crew until you decide. Does that work for you, or should some rejections go through without approval?" |
| ⭐ V-02 | FR-62 (DEC-42) | Within 48 h of the Job, a written explanation is required and the request is flagged **Short notice** | "I'd like at least 48 hours' notice unless it's an emergency." | "Is an explanation plus a 'Short notice' flag the right way to handle rejections within 48 hours?" |
| ⭐ V-03 | FR-62 (DEC-42) | Reasons: Personal emergency; Missing equipment or parts; Other + comment. "Clash with another job" and "Not qualified" were removed because the system already blocks those | "A short list works: personal emergency, clash with another job, not qualified or missing equipment, or other, with a comment box." | "We dropped 'clash' and 'not qualified' because the system prevents them. Is anything missing, e.g. 'previous job running late'?" |
| ⭐ V-04 | FR-71 (DEC-43) | The Manager names **daily Standby Staff** (at least 1 Driver, plus Technicians covering both Brands). They back up every Job that day. Missing cover gives a warning, not a block. Standby counts 0 h unless called in | "No dedicated standby staff. But anyone who marked themselves available and didn't get allocated is effectively on standby, so I'd like the system to show me who that is." (Conflicts Q2 follow-up) | "Would you name Standby Staff each day, or keep the informal 'whoever's free' approach? Is a warning enough when you can't find cover?" |
| ⭐ V-05 | FR-53 (DEC-39) | Every crew member, **Technicians included**, is credited with the hours of all Jobs on their van that day | "A technician's allocated hours are just the total of their jobs, plus travel." and "Drivers get the same hours as the van they're on" | "On a van with two Technicians, should each get the whole van's hours, or only the Jobs they worked on?" |
| ⭐ V-06 | FR-54 (DEC-40) | Actual Hours = actual end − start **plus** the 30-min travel allowance | "The hours should show the planned time first, and once a job is completed, use the actual time instead." | "When a Job is completed, should the 30 minutes of travel still be added to the actual time?" |
| ⭐ V-07 | FR-39, FR-40 (DEC-40) | Only a **Technician** can mark a Job completed, and the **invoice photo is mandatory** | "They should mark the job as completed in the system with a photo of the invoice signed by the customer." | "Should the photo be required every time, and should Drivers also be able to mark Jobs complete?" |
| ⭐ V-08 | FR-69 (DEC-16) | Each week's roster is **Draft** until you publish it. Staff see nothing before then | You publish on Monday; staff "always get a week's notice" | "Is it right that staff see nothing until you press Publish?" |
| ⭐ V-09 | FR-70 (DEC-19) | When approved leave or sickness breaks a crew, the person is **removed automatically** and the van-day is flagged for you. Jobs stay on the van | You mark people unavailable yourself; "Any jobs on that van become unassigned" (only for van breakdowns) | "Is automatic removal plus a flag what you want, or should you be asked first?" |
| V-10 | FR-57 (DEC-05) | Lowest-three lists: ties broken by name; anyone with **any** leave day that week is excluded | "Anyone on leave that week should be left out." | "Should one day of leave exclude someone for the whole week? How should ties be shown?" |
| V-11 | FR-22 (DEC-13) | Leave is **full days only**, and can't exceed the remaining balance | You described days of leave, with no mention of half days | "Is full-day leave enough, or do staff need half days?" |
| V-12 | FR-28 (DEC-14) | The system **generates** workshop dates from your rotation. You can adjust them, and add extra days if servicing overruns | You described the fixed rotation; "I'd like the system to record these dates" | "Should the system generate the dates, or would you rather enter them yourself?" |
| V-13 | FR-42, FR-45 | Jobs are scheduled 09:00–18:00 with lunch skipped and 30 min between Jobs. You get a warning if a Job starts outside the customer's preferred half-day | Morning 9–1, afternoon 2–6, lunch 1–2; a 30-min travel allowance | "Is 30 minutes between Jobs realistic? Do you want a warning when a Job misses the customer's preferred half-day?" |
| V-14 | FR-14 (DEC-30) | Staff can enter availability up to the **same date next month** | "I can view availability up to a month ahead" | "Is 'up to the same date next month' what you'd expect by 'a month ahead'?" |
| V-15 | FR-36 (DEC-11) | Linked two-brand Jobs **must** go on the same van and day | "I log it as two jobs at the same address and put both on a mixed-brand van." | "Should the system enforce this, or only suggest it?" |
| V-16 | FR-37 | If an edit breaks a rule (e.g. the brand changes), the Job becomes **Unassigned** and you're told why | Customer changes: "I update or cancel the job in the system." | "Is it OK for an edited Job to drop off the van automatically?" |
| V-17 | FR-10 (DEC-35) | IT enters certifications at account creation, and **you maintain them** afterwards. An expired certification blocks that brand | "the system should remind me a month before one expires" | "Will you be the one updating certificates after renewal?" |
| V-18 | FR-27 | **You** maintain the van list (numbers, plates) | Not discussed | "Who should add or retire vans in the system?" |

## 5. MTG-02: IT Administrator validation

| # | SRS rows | Team-set value now (†) | What was said before | Question to ask |
|---|---|---|---|---|
| ⭐ T-01 | FR-07 | Lock after **5** failed logins within **15 min**; only IT unlocks | Lockouts go to IT, but no number was given | "How many failed attempts before locking, and over what period?" |
| ⭐ T-02 | NFR-01 | **95%** of actions within **5 s** | "something like maybe 3 or 5 seconds will be enough per schedule request" | "Should it be 3 or 5 seconds? Is 95% of requests an acceptable measure?" |
| ⭐ T-03 | NFR-03 | **50** sessions, up to **3** devices per person, 25 Jobs a day, 13 months of data | "we should try to support 50 or so" | "Are 50 sessions and 3 devices per person enough?" |
| ⭐ T-04 | NFR-04 | **120** requests per minute per user | "We need to also have rate limits" | "Is 120 requests a minute per user sensible?" |
| ⭐ T-05 | NFR-05 | **99%** monthly uptime; maintenance **00:00–05:00**, never Mon/Thu | "24/7" and maintenance "early morning or late night" | "What uptime is acceptable? Is that maintenance window right?" |
| ⭐ T-06 | NFR-10 (DEC-41) | Email 2FA only on a **new device**, remembered **30 days** | "2FA when logging in would be good, send confirmation to user email before they can login." | "Is 2FA on new devices enough, or every login? Is 30 days right?" |
| ⭐ T-07 | FR-05, NFR-13 (DEC-34) | Leavers are **deactivated, not deleted**; records kept **12 months**, then may be purged | "IT admin will delete their account" and "All schedules should exist up to one year in our system" | "Deletion would remove the history you need for yearly reviews. Is deactivation acceptable?" |
| T-08 | FR-08 (DEC-36) | **One-off** CSV import at go-live, then manual creation. No schedule import | "we need to have all employees from that ported over" and "Ideally, we manually create the user" | "Is a one-off import enough? Do old schedules need importing?" |
| T-09 | NFR-09 | **3** automatic retries, then an error message | "it should try to hold it until it can submit it" | "Is 3 retries reasonable?" |
| T-10 | NFR-11 | Encrypted at rest; **salted password hashes** | "encrypted properly in the backend" | "Does this meet your encryption expectation?" |
| T-11 | FR-66 (DEC-17) | **Only IT** can view the audit log | "we can pull out the records in the event of it being needed" | "Should anyone besides IT see the audit log?" |
| T-12 | FR-04 (DEC-17) | Role changes take effect at **next login** | "the IT admin will change the permissions" | "Is next login acceptable, or must it be immediate?" |
| T-13 | NFR-05 (DEC-38) | Thursday peak read as the **Manager's planning day** | "Another peak period would be Thursday since they can start scheduling their slots then." | "Who is 'scheduling their slots' on Thursday?" |
| T-14 | NFR-14, NFR-15 | Supported: iOS as well as Android; phones **360 px** wide, laptops **1366 px** | "all modern phones" | "Are iPhones in use? Are these screen sizes right?" |

## 6. MTG-03: Staff-side validation (DCT or Driver)

| # | SRS rows (DEC) | What the SRS says now | What was said before | Question to ask |
|---|---|---|---|---|
| ⭐ S-01 | FR-62, FR-63 (DEC-42) | Your rejection is a request; the Job stays on your list until the Manager decides | DCT: "The job should disappear from my list, and the manager gets told, so he can give it to someone else." | "The Job now stays with you until the Manager approves. Does that work in practice?" |
| ⭐ S-02 | FR-71, FR-64 (DEC-43) | You may be named **Standby** for a day and notified if needed | Not discussed | "Would you accept being on Standby some days? How should you be told?" |
| ⭐ S-03 | FR-53 (DEC-39) | You get the whole van's hours for the day | DCT: "The job time and the travel between jobs." | "Does counting the whole van day feel fair to you?" |
| ⭐ S-04 | FR-52 (DEC-31) | Travel is a fixed **30 min per Job** | Driver: "We track this workload by correlating estimated route hours alongside the vehicle's daily mileage logs." | "Is a fixed 30 minutes per Job acceptable instead of mileage-based travel?" |
| S-05 | FR-55 (DEC-32) | Overtime (over 40 h) is **highlighted only**, with no approval step | Driver: "overtime (OT) is automatically flagged for approval if we must complete it that evening." | "Is a highlight enough, or do you expect overtime approval?" |
| S-06 | FR-13 | You can set a **whole day** in one tap, or each half day | DCT: "It would be nice to copy last week's availability instead of entering it all again." | "Would the whole-day shortcut and copy-last-week cover your needs?" |
| S-07 | FR-21, FR-16 (DEC-07) | Job Preference **locks** with availability at the Wednesday deadline | Not discussed | "Is it OK that preferences lock with availability?" |
| S-08 | NFR-10 (DEC-41) | Email confirmation when logging in on a **new phone** | Not discussed | "Would an email confirmation on a new phone be a problem?" |
| S-09 | NFR-08 | **Today's** Jobs visible offline; completions queued | DCT: "I'd like to at least see today's jobs when I lose connection" | "Is today's list enough offline, or do you need tomorrow's too?" |

## 7. After the sessions: feeding results into the SRS

| Outcome for an item | Action |
|---|---|
| **Confirmed** | Add `MTG-nn` to the SRS row's Source and to the DEC's Decision source. For a † number, remove the † and cite the MTG |
| **Adjusted** | Record a new DEC (citing the MTG), change the SRS rows, and bump the version (v3.1) |
| **Rejected** | Record a new DEC with the stakeholder's view and the team's final call, update the SRS, and bump the version |
| **New requirement raised** | Record it in the MTG note, then add it via a DEC as a new FR/NFR ID (IDs are never reused) |

Then:
- [ ] Add each rep to the stakeholder register and meeting log in [README.md](README.md), with attendance
- [ ] Update `elicitation.md` (the report brief): add "requirements validation" as a technique, with outcomes
- [ ] Log the SRS changes in `ai-usage-log.md` if AI helped apply them
- [ ] If use cases already exist, update any that cite changed rows
