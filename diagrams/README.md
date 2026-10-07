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

`UCD`, `CD` and `CMP` are file prefixes only. Traceable IDs are `UC`, `CL`, `AD` and `SD` (see [AGENTS.md](../AGENTS.md#id-conventions)).

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

## Consolidated sequence review exports (DEC-53 to DEC-57)

Exactly 22 sequence diagrams are active: SD-01 to SD-06, SD-08, SD-10, SD-11 and SD-13 to SD-25. Original IDs retain their meanings; the eight redundant IDs are Withdrawn and are never reused. The mapping is in [traceability.md](../traceability.md#sequence-source-index).

- UC-07: SD-17 forms or changes Crews and names Standby; SD-18 allocates Jobs and confirms warnings before saving; SD-19 validates and publishes the Weekly Roster.
- UC-09: SD-20 decides Leave (including approval and rejection), SD-21 decides Late Availability Changes and SD-22 decides Job Rejections.
- UC-12: SD-23/24/25 submit the respective three request types.
- SD-11 calls SD-24 for the locked-week route. SD-15 is shared notification delivery. SD-16 is the shared FR-70 later-event interaction with no separate use case.
- SD-07/09/12 overview steps are folded into the detailed workflows. SD-26/27 are folded into SD-17; SD-28/29 into SD-20; SD-30 into SD-18/19.

The exact previous sources remain in the repository archive, diagrams/archive/sequence-r2-2026-10-04/. The review ZIP contains only the 22 active SD sources and exports, with separate supporting class views, traceability and verification evidence.

The model remains 43 identified classes: 22 domain entities in CD-domain, ten boundaries in CD-boundary and eleven controls in CD-control. JobAllocationPage.confirmWarningChoice(choice) and RequestReviewPage.confirm(choice) are explicit receiving-page operations after consolidation. Match receiving lifeline operations to their class views. External Email Service and SMS Gateway realise the existing Email/Phone actor (DEC-48/56). Hidden class links arrange boxes only.

PlantUML 1.2026.8 can place a fragment border through a newly created entity label. After both PNG and SVG exports, the optional local helper widens affected borders and separates three class multiplicity labels without changing source or SVG text:

```sh
python diagrams/render-layout.py --report diagrams/out/layout-fixes.json
```

The helper uses Python with lxml/Pillow and Node.js with Sharp. Select local runtimes with --node or --sharp-module. PNGs retain PlantUML source metadata. Rendered outputs remain git-ignored in diagrams/out/.

The adopted critique is [sequence-diagram-review.md](sequence-diagram-review.md). DEC-48 to DEC-63 are present locally; human branch integration and PR review remain pending. Opus review is required before adding sequence diagrams or the expanded class model to Google Docs. Approved report figures, SRS and brief remain unchanged.

## Round-2 correction draft (2026-10-05)

The adopted second critique is [sequence-diagram-review-round-2.md](sequence-diagram-review-round-2.md), with the response in [sequence-round-2-fixes.md](sequence-round-2-fixes.md). Exactly 22 SDs remain active (DEC-57/59); no retired ID is reused.

- SD-15 partitions mixed-week events and suppresses Draft roster information before any Staff message/email/SMS is created (FR-49).
- SD-16 has a drawn 00:00 Clock expiry branch and a callable branch that joins approval/edit transactions. SD-20/21/10 commit invalidating Crew changes with their business data, then notify.
- SD-22 draws the independent Job-start lapse event; each newly saved lapse is audited and notified to its requester.
- SD-20 rechecks the annual balance inside approval, serializing check/deduction. SD-04 removes future Crew membership and applies the member-confirmed Needs attention flag while preserving FR-04/05 unassignment.
- SD-10 uses typed Notification dashboard alerts (DEC-63); no new Alert class is added. The 43 classes remain; their receiving operations match the sequence messages.
- DEC-61/62 explicitly record unresolved token/complexity and external notification policies. Values are not invented.

Local decision records and Withdrawn rows resolve the missing provenance/status in the review package. Main-branch integration and human PR review remain pending; no automated commit, push or merge. Google Docs and the approved UCD/activity sources remain unchanged.

Render SVG and PNG locally with output directory out/r3. Then run render-layout.py with --render-dir diagrams/out/r3 and --report diagrams/out/r3/layout-fixes.json. This changes only overlapping frame/multiplicity positions in renders; sources and text are preserved.

## Round-3 correction draft (2026-10-05)

Latest critique: [sequence-diagram-review-round-3.md](sequence-diagram-review-round-3.md). The correction response is [sequence-round-3-fixes.md](sequence-round-3-fixes.md). Keep exactly 22 SDs and preserve unaffected sources/exports. DEC-64/65/66 give individual rule citations; DEC-67 records the member-approved Linked partner policy; DEC-68 aligns Clock and presentation. Only changed sources are rendered into out/r4. Use the local layout helper after rendering. Main integration is still pending; no commit, push or Google Docs update.
