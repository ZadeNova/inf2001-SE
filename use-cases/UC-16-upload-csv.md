# UC-16: Upload CSV

> **Status: M2 v1.2 (2026-11-14).** SRS v4.2; complete weekly HR snapshots and committed coverage (DEC-108). Van CSV retains per-date replacement.

| Field | Value |
|---|---|
| **ID** | UC-16 |
| **Name** | Upload CSV |
| **Primary actor** | Manager |
| **Secondary actors** | None. HR and the van vendor export files outside the system (M2-Brief §2) |
| **Description** | Import a complete HR snapshot for one selected Planning Week, or Van Availability counts for the file dates; validate the whole file before business changes. |
| **Trigger** | Before Thursday planning (A4), or an updated complete export arrives. |
| **Linked requirements** | FR-52, FR-53, FR-54, FR-49 |
| **Source** | M2-Brief §2, §3.2, §7; DEC-74; DEC-85; DEC-104; DEC-106; DEC-108 |
| **Classes** | CsvUploadPage, CsvImportController, CsvImport, CsvRowMapper, HrLeaveCsvMapper, VanAvailabilityCsvMapper, LeaveRecord, VanAvailability, AuditLog |
| **Wireframe** | W-05 |
| **Status** | Agreed |

## Preconditions

The Manager is logged in and has the export. HR import requires one selected Monday–Saturday Planning Week and confirmation that the export is complete, including any no-Leave export. A partial/delta file cannot be presented as a complete snapshot.

## Main flow

| Step | Actor | System |
|---|---|---|
| 1 | Chooses HR or van CSV and a file. For HR, selects the Planning Week and confirms complete weekly export. | Show expected headers. Explain HR whole-week replacement, no-Leave header-only exports, and separate per-date van counts. |
| 2 | Uploads for validation. | `CsvImportController.upload(file, type, week, completeExportConfirmed)` parses rows and validates required headers/each row through `CsvRowMapper`, whole-file errors and HR week membership/completeness. Correct-header zero-data-row HR is valid; wholly blank/missing-header files and empty van files are invalid. Exact duplicates are mapped once. |
| 3 | Reviews and confirms replacement. | Show selected HR coverage week, current/new Leave counts and replacement effect. Explicitly warn if a zero-row snapshot will clear existing Leave. Van replacement remains scoped to file dates. |
| 4 | Confirms. | In one transaction replace **all** selected-week Leave Records for HR (including omitted/cancelled Leave), or Van Availability for file dates; mark `CsvImport` Committed with uploader/time/outcome and HR week/completeness metadata, and write the successful `AuditLog`. Other HR weeks remain unchanged. |
| 5 | — | Show committed coverage week/counts/uploader/time for HR, or dates/counts for van. A zero-row HR result says no Leave Records and HR ready; it does not say Staff are Available. |

## Exceptions and cancellation

- Invalid row, unknown Staff/type, bad/Sunday date, missing headers, blank file or an HR row outside the selected week: reject the whole file and list errors. Save no business rows.
- Missing complete-export confirmation or declared partial/delta export: refuse HR commitment; obtain a complete weekly export.
- Cancel replacement: preserve records and previous committed coverage.
- Save/transaction failure: roll back business rows, committed coverage metadata and the successful Audit Log entry together. A rejected/failed later attempt does not invalidate earlier successful coverage. Upload attempts still retain their outcome under FR-54.

## Postconditions and readiness

Success: selected-week Leave Records exactly match the complete HR snapshot, even when empty, and `CsvImport.coversWeek(week)` is true for that committed import. Failure: previous records and successful coverage remain unchanged. UC-07/18 use committed complete coverage, never a nonzero Leave count; Van readiness still needs each working date's explicit count.

A Leave Record overrides Availability/initial Standby. Later clashes are flagged for Manager repair; preserve confirmed-request history and earlier per-Job attribution (DEC-97/98). Removing Leave does not silently rewrite operational history. No Leave does not imply Available: no Availability entry remains unavailable (DEC-03/83).
