# Diagrams (PlantUML)

All UML diagrams are kept as PlantUML source here, **one diagram per file**. The `.puml` file is the source of truth. Rendered images are git-ignored (`diagrams/out/`) and regenerated for the report.

## File naming

| Diagram | File name | Example |
|---|---|---|
| Use case diagram | `UCD-<slug>.puml` | `UCD-system.puml` |
| Activity diagram | `AD-nn-<slug>.puml` | `AD-01-submit-availability.puml` |
| Class diagram | `CD-<slug>.puml` | `CD-domain.puml` (M1), `CD-final.puml` (M2) |
| Sequence diagram | `SD-nn-<slug>.puml` | `SD-01-reject-job.puml` |
| Component diagram (M2) | `CMP-<slug>.puml` | `CMP-system.puml` |
| Architecture diagram (M2) | `ARCH-<slug>.puml` | `ARCH-layered.puml` |
| Design-pattern excerpt (M2) | `DP-<slug>.puml` | `DP-strategy-ranking.puml` |
| Control flow graph (M2 white-box) | `CFG-<slug>.puml` | `CFG-classify-technicians.puml` |

`UCD`, `CD`, `CMP`, `ARCH`, `DP` and `CFG` are file prefixes only. Traceable IDs are `UC`, `CL`, `AD` and `SD` (see [AGENTS.md](../AGENTS.md#id-conventions)).

## Conventions

- The file starts with `@startuml <ID>-<slug>` and ends with `@enduml`.
- Give every diagram a `title <ID>: <name>`, e.g. `title SD-01: Reject Job (UC-05)`.
- Names come from the glossary in AGENTS.md: actors, classes (`CL-` names without the prefix), lifelines and swimlanes.
- Add a header comment listing the traced IDs:
  ```
  ' Traces: UC-05, FR-10, FR-11
  ```
- Use correct UML 2.5 notation:
  - **Use case:** actors outside the system boundary (`rectangle`), `<<include>>` and `<<extend>>` with the correct arrow direction, and generalisation only where justified.
  - **Activity:** one initial node, final node(s), diamond decisions with guarded `[conditions]`, fork/join for parallel work, and swimlanes (`|Actor|`) for each actor.
  - **Class:** attributes and methods with visibility, multiplicities on every association, and composition, aggregation or inheritance only where they are semantically right.
  - **Sequence:** actor, then boundary/control/entity lifelines, activation bars, dashed return messages, and `alt`/`opt`/`loop` fragments with guards.
- Keep the layout readable. Split any diagram that no longer fits on one page.

## M2 diagram set (2026-11-07)

| File | Report section | Notes |
|---|---|---|
| `UCD-system.puml` | §1.2 | v3.1: 16 active use cases; Email Service and SMS Gateway as «system» boxes; UC-02 standalone (DEC-91) |
| `CD-final.puml` | §1.3 | Final class diagram; packages = components; three «interface» classes; clarified hours, direct Assignment, Replacement and provisional preferences (DEC-93, DEC-96–98) |
| `CMP-system.puml` | §2 | Components with provided (lollipop) and required («use») interfaces |
| `ARCH-layered.puml` | §3.1 | Layered 3-tier with MVC in the web tier |
| `DP-strategy-ranking.puml` | §3.2 | Strategy excerpt of CD-final |
| `CFG-classify-technicians.puml` | §4.2 | CFG for `CrewFormingService.classifyTechnicians()` |

`CD-domain`, `CD-control` and `CD-boundary` are the M1 analysis views (report Figures 4.1a–c), superseded by `CD-final` for M2. The status of the M1 activity and sequence diagrams after M2 is in [traceability.md §5](../traceability.md).

All six current M2 sources were rendered locally with PlantUML 1.2026.8 for the v4.1 update. Team review is still required. M1 sources below are historical and have not been rewritten.

## Rendering locally

Render **locally** only. The public PlantUML web server receives your diagram source, and the plagiarism declaration forbids making project material accessible to others.

- **VS Code:** install the "PlantUML" extension (jebbs.plantuml). Preview with `Alt+D`, and export via the command palette ("PlantUML: Export Current Diagram"). In its settings set `plantuml.render` to `Local`, which needs Java and Graphviz.
- **CLI:** install Java and Graphviz and download `plantuml.jar`, then run:
  ```sh
  java -jar plantuml.jar -tsvg -o out diagrams/*.puml
  # or -tpng for report images
  ```
- **JetBrains IDEs:** use the "PlantUML Integration" plugin.

## Checklist before merging a diagram

- [ ] The ID and title match the traced UC/SD/AD and `traceability.md` is updated
- [ ] All names match the glossary and the class diagram
- [ ] The notation is correct for the diagram type
- [ ] It renders without errors

## M1 sequence diagrams (submitted report numbering)

The submitted M1 report (9 Oct 2026) is the M1 source of truth (DEC-72). It shows **21 sequence diagrams, SD-01 to SD-21**, and the files here use its numbers and titles. The draft SD-18 Allocate Job is not in the report; it is kept in `archive/pre-report-2026-10-09/` with its draft number.

| Report ID | File | Use case | Draft ID before 2026-11-07 |
|---|---|---|---|
| SD-01 | SD-01-log-in-out.puml | UC-01 | SD-01 |
| SD-02 | SD-02-reset-password.puml | UC-02 | SD-02 |
| SD-03 | SD-03-create-user-account.puml | UC-03 | SD-03 |
| SD-04 | SD-04-manage-user-access.puml | UC-04 | SD-04 |
| SD-05 | SD-05-manage-job.puml | UC-05 | SD-05 |
| SD-06 | SD-06-manage-vans-and-workshop-servicing.puml | UC-06 | SD-06 |
| SD-07 | SD-07-form-crews-and-standby.puml | UC-07 | SD-17 |
| SD-08 | SD-08-publish-weekly-roster.puml | UC-07 | SD-19 |
| SD-09 | SD-09-compare-staff.puml | UC-08 | SD-08 |
| SD-10 | SD-10-decide-leave-request.puml | UC-09 | SD-20 |
| SD-11 | SD-11-decide-late-availability-change.puml | UC-09 | SD-21 |
| SD-12 | SD-12-decide-job-rejection-request.puml | UC-09 | SD-22 |
| SD-13 | SD-13-view-manpower-dashboard.puml | UC-10 | SD-10 |
| SD-14 | SD-14-set-availability-and-preferences.puml | UC-11 | SD-11 |
| SD-15 | SD-15-submit-leave-request.puml | UC-12 | SD-23 |
| SD-16 | SD-16-submit-late-availability-change.puml | UC-12 | SD-24 |
| SD-17 | SD-17-submit-job-rejection-request.puml | UC-12 | SD-25 |
| SD-18 | SD-18-view-my-assignments-and-workload.puml | UC-13 | SD-13 |
| SD-19 | SD-19-complete-job.puml | UC-14 | SD-14 |
| SD-20 | SD-20-notify-staff.puml | UC-15 | SD-15 |
| SD-21 | SD-21-handle-invalidated-crew.puml | FR-29 (no UC) | SD-16 |
| — | archive/pre-report-2026-10-09/SD-18-allocate-job.puml | UC-07 | SD-18 (not in the report) |

The class views are `CD-domain`, `CD-boundary` and `CD-control` (report Figures 4.1a–c). The activity diagrams AD-01 to AD-04 keep their numbers.

**History.** The review records `sequence-diagram-review.md`, `sequence-diagram-review-round-2.md`, `sequence-diagram-review-round-3.md`, `sequence-round-2-fixes.md` and `sequence-round-3-fixes.md`, and everything under `archive/`, are kept unchanged. They use the **draft** SD and FR numbers; read them with the table above and the FR mapping in [requirements.md §9](../requirements.md).

PlantUML 1.2026.8 can place a fragment border through a newly created entity label. After rendering, the optional local helper `render-layout.py` widens affected borders without changing source text:

```sh
python diagrams/render-layout.py --report diagrams/out/layout-fixes.json
```

For the large final class view, raise the renderer size limit to avoid clipping (for example Java option `-DPLANTUML_LIMIT_SIZE=24000`). SVG output preserves readable text when zoomed. Keep the generated images in ignored `diagrams/out/`.
