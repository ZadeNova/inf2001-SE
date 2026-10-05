# Opus round-3 correction response — 22 sequence diagrams

Date: 2026-10-05. Local branch CL/sequence-diagrams; Google Docs unchanged. This package is for review and does not claim Opus approval.

| Finding | Resolution |
|---|---|
| B1 | Local DEC-48 to DEC-63 already existed and are packaged. Separate DEC-64 (Draft privacy), DEC-65 (Leave balance) and DEC-66 (Pending limit) replace the three policy citations to the combined DEC-58. Preserve the historical entry append-only. DEC-67/68 record this round. Human main-branch integration is still pending; no remote merge/push is claimed. |
| M6 | Existing active and Withdrawn rows are retained in traceability.md under DEC-57. Exactly 22 active SDs. The proposed report wording is below; no report edit. |
| M8 | Clock is recorded in UC-09 secondary actors and trigger; its lapse branch needs no Manager session. Local UCD footnote records Clock for UC-09 and FR-10/70. SD-16 title/index explicitly say no UC. DEC-68 clarifies DEC-59 without rewriting it. |
| M9 | Member confirmed active Linked partners are also unassigned. SD-05 invalid edit/cancel and SD-22 approval loop across the affected Jobs and placements within the transaction. Cancellation cancels only the selected Job. Completed/Cancelled partners are unchanged. UC-05/09 and controller operations align (DEC-67). |
| m1 | Affected labels are shortened; maxMessageSize/wrapWidth increased to 420 only for changed SDs. Long consolidated workflows remain complete. Full-resolution PNG and zoomable SVG are supplied; SD-05 and SD-20 need dedicated report space or vector zoom. Scaling to 1200 px alone does not solve text density, so source-resolution exports are retained. No report formatting was changed. |
| m13 | SD-11 says Blank (Not submitted) counts as unavailable; no Creole heading. |
| m14 | Removed reviewer-facing phrases from SD-16 and SD-25 legends. |
| m15 | SD-06 breakdown mutation is in atomic Van unavailability save, followed by mutually exclusive failure/commit paths. Notifications occur only after commit. |
| m16 | SD-19 uses RuleValidator.weekWorkload(week); legend describes publication recipients. Matching control operation added. |
| m17 | SD-10 and SD-11 participant order makes referenced participants contiguous, excluding unrelated lifelines from the frame. SD-11 no longer repeats the open call; SD-24's gate starts it and returns its outcome. |
| m18 | SD-08 uses one s:Staff lifeline. In the Technician branch, certifications() is the concrete Technician operation on that same object. No second object or generic Driver certification operation is added. |
| m19 | Member confirmed one Pending request per shared Assignment across all Crew members (DEC-66). SD-22 singular lookup returns zero or one; loop guard matches SD-25 and UC-12. |
| m20 | SD-01 branches on confirmation-email failure: generic failure/retry later; no code prompt or authenticated session. |
| m21 | SD-25 retains one authoritative validation pass inside its atomic save. Page prevalidation is optional; the saved-state eligibility, Pending limit and Short-notice checks are preserved. |
| m22 | SD-16 says FR-70, no UC; traceability explains shared system behaviour and FR-10/70. |

Proposed report note (not inserted): UC-07 is shown in SD-17 to SD-19; UC-09 in SD-20 to SD-22; UC-12 in SD-23 to SD-25. SD-16 models shared Crew invalidation and Clock-triggered Certification expiry. SD-07/09/12 are Withdrawn, not missing.

Unchanged SD-02, SD-03, SD-14, SD-17 and SD-23 are carried forward byte-for-byte (source and PNG/SVG). Supporting class views are not additional sequence diagrams. SRS and binding brief are unchanged. Open implementation policy DEC-61/62 remains open.
