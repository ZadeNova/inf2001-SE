# Requirements Elicitation

**Read this index first.** Open individual files only when asked to or when verifying a source.

## Index of elicitation material

"TBC" means the file itself doesn't state it. Do not fill these fields in by guessing.

| File | What it is | Role | Date | Interviewer | Interviewee |
|---|---|---|---|---|---|
| [interviews/manager.md](interviews/manager.md) | Interview transcript, "Part A: Manager interview". The file says the session was recorded and transcribed on Zoom. It ends with an **Answer key** table | Manager (introduces themselves as "the operations manager") | TBC | TBC | TBC |
| [interviews/dct.md](interviews/dct.md) | Interview transcript, "Part B: Dual Certified Technician interview". The file says the session was recorded and transcribed on Zoom. It ends with an **Answer key** table | Dual Certified Technician (DCT) | TBC | TBC | TBC |
| [interviews/driver.md](interviews/driver.md) | Interview answers to 17 numbered questions, with no opening or closing dialogue | Driver | TBC | TBC | TBC |
| [interviews/ita.md](interviews/ita.md) | Interview transcript (Interviewer / IT admin dialogue) | IT Administrator (ITA) | TBC | TBC | TBC |
| [planned-interview.md](planned-interview.md) | **Plan** (not yet held) for follow-up validation sessions on SRS v3.0: Manager (MTG-01), IT Administrator (MTG-02), Staff (MTG-03), with the items to validate and how results feed back into the SRS | Manager, IT Administrator, DCT or Driver | Planned | — | — |
| [document-analysis.md](document-analysis.md) | "INF2001 Milestone 1: Document Analysis": the team's line-by-line review of the brief, with findings **F-1 to F-30** mapped to interview questions | — (team document, not a stakeholder source) | Sep 25, 2026 (stated) | — | — (author stated as "@Zade") |

## Notes on using this material

- **The transcripts are the primary source.** Cite what the stakeholder said in the transcript.
- **The "Answer key" tables are a team summary, not stakeholder statements.** They appear at the end of `manager.md` and `dct.md`, labelled "For your write-up and SRS. Not read aloud." The two tables are currently identical.
- **Two separate ID schemes. Never treat them as the same thing:**
  - `AK-01` to `AK-14`: rows of the Answer key tables. In the files these rows are labelled `F-01` to `F-14`, but always refer to them as `AK-nn`.
  - `F-1` to `F-30`: findings in `document-analysis.md`.
  - For example, AK-01 ("Planning cycle") is **not** F-1 (the availability horizon).
- **The provenance of the Driver and IT Administrator transcripts is unconfirmed (TBC).** We don't yet know who was interviewed, when, how or by whom.
- **The stakeholder question guide** that `document-analysis.md` refers to is **not in the repo yet**.
- **The team has not yet reviewed these files for inconsistencies.** Some contradictions between files are expected. Do not silently reconcile them. Raise each one in `decisions.md` when the review happens.

### Conversion notes

The files were copied from the team's exports. Except for the explicitly recorded DEC-45 scope redactions in `manager.md`, the DCT Answer key and `document-analysis.md`, the wording was not changed, rewritten, summarised or reordered. The following export artefacts were also fixed:

- **All four exported files** (`manager.md`, `dct.md`, `driver.md`, `document-analysis.md`): Google Docs backslash escapes were removed (`\[ \] \. \+ \= \> \< \)`), as were trailing spaces and whitespace-only lines.
- **`driver.md`:** a stray `*.*` after "mileage logs" became `.`.
- **`document-analysis.md`:** an empty `1.` list item before the §3 table was removed.
- **`ita.md`:**
  - The source file `IT_admin.md` was actually a PDF.
  - The text came from the team member's paste. It was checked word for word against the PDF text, and all 1,317 words match.
  - Blank lines were added between speaker turns so that Markdown keeps them as separate paragraphs.
  - The first two lines were marked as headings (`#`, `##`).

The raw source files remain in the uploader's Downloads folder and are not committed.

## Rules (from Appendix A)

Source: [brief/assessment-overview.md, Appendix A](../brief/assessment-overview.md#appendix-a---instructions-to-engage-stakeholders-for-team-project).

- Engage **at least 5 Stakeholder Representatives**, with **at most 2 from our own team**.
- Representatives may come from our team, other teams or the real industry.
- Meetings may be arranged **from Week 2** of the trimester. Aim for in-person meetings as early as possible.
- **All engagement (in-person, email, virtual) must end by Week 6.**
- It is our responsibility to brief representatives on the project context and requirements **in advance**.
- **Record attendance** for every meeting, because it goes in the Milestone Report.
- Representatives may add requirements, but Brief R1–R11 remain the minimum deliverable.
- A student may act as Stakeholder Representative for at most two teams, including their own. For the "same project" restriction see DEC-28.
- Keep other teams' engagement discussions confidential.

## Stakeholder register

| Rep ID | Name | Own team? (Y/N) | Role played | Meetings attended |
|---|---|---|---|---|
| SR-01 | | | | |

Check: at least 5 reps in total, and no more than 2 marked "Y".

## Meeting log

| MTG ID | Date | Mode (in-person/online/email) | Technique(s) | Reps present | Notes file |
|---|---|---|---|---|---|
| MTG-01 | | | | | |

## Process

1. Pick the open DECs in [decisions.md](../decisions.md) to raise, and draft questions (AI may help draft them).
2. Send the brief and the agenda to the representatives beforehand.
3. Run the meeting. Techniques the rubric names include interviews, surveys and document analysis. Record the technique used.
4. Write up `MTG-nn-<yyyy-mm-dd>.md` from [MEETING-TEMPLATE.md](MEETING-TEMPLATE.md) within 24 hours. Record **only what stakeholders actually said**.
5. Update `decisions.md` (cite the MTG) and `requirements.md` (cite the MTG) based on the outcomes.

AI may summarise or analyse notes we wrote. It must never produce or embellish stakeholder statements.
