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
