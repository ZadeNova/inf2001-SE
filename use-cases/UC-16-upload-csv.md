# UC-16: Upload CSV

> **Status: M2 v1.1 (2026-11-07).** New in M2 (DEC-74, DEC-91).

| Field | Value |
|---|---|
| **ID** | UC-16 |
| **Name** | Upload CSV |
| **Primary actor** | Manager |
| **Secondary actors** | None. HR and the van vendor are not actors: the Manager downloads their files outside the system (M2-Brief §2) |
| **Description** | The Manager uploads the HR leave CSV or the van availability CSV. The system validates the whole file before saving anything. |
| **Trigger** | Before planning starts on Thursday (assumption A4), or when an updated file arrives. |
| **Linked requirements** | FR-52, FR-53, FR-54, FR-49 |
| **Source** | M2-Brief §2, §3.2, §7; DEC-74; DEC-85 |
| **Classes** | CsvUploadPage, CsvImportController, CsvImport, CsvRowMapper, HrLeaveCsvMapper, VanAvailabilityCsvMapper, LeaveRecord, VanAvailability, AuditLog |
| **Wireframe** | W-05 CSV upload |
| **Status** | Agreed |

## Preconditions

1. The Manager is logged in and has the exported file.

## Main flow (basic path)

| Step | Actor | System |
|---|---|---|
| 1 | Opens CSV Upload, picks the file type (HR leave or van availability) and chooses the file. | Shows the expected columns for that type (`CsvRowMapper.requiredColumns()`). |
| 2 | Uploads. | `CsvImportController.upload()` creates a `CsvImport`; `parse()` and `validate()` check every row through the matching `CsvRowMapper` (FR-54). |
| 3 | — | No errors: `commit()` replaces the Leave Records or Van Availability for the dates in the file and logs the upload (FR-52, FR-53, FR-49). |
| 4 | — | Shows a summary: rows saved, dates covered, duplicates merged. |

## Exception flows

### E1: The file has errors (step 2)

1. `status = Rejected`. Nothing is saved, and every row error is listed (missing column, unknown staff ID, bad date or type, negative Van count, empty file).
2. The Manager fixes the file and uploads again.

## Postconditions

- **Success:** Leave Records or Van Availability for the file's dates match the file, and the upload is logged.
- **Failure:** Existing records are unchanged.

## Business rules / notes

- A Leave Record overrides Availability and any Standby pick for that day (FR-52). A later clash with an existing placement is flagged for Manager repair (A3, DEC-98); preserve confirmed-request history and earlier Job attribution. CSV readiness is required before provisional picks can be confirmed.
