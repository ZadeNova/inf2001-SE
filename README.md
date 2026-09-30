# INF2001 Team Project: Aircon Retailer Workload Management System

Private working repo for our INF2001 team project. **Read [AGENTS.md](AGENTS.md) first.** It holds the rules for humans and AI tools, the ID conventions and the glossary.

## Folder map

```
brief/                      Source docs converted from the PDFs (read-only)
  project-description.md      Client brief: Aircon Retailer, Brief R1–R11
  assessment-overview.md      Assessment, AI usage, declaration, stakeholder rules
  rubric-m1.md                Milestone 1 deliverables and rubric (due 9 Oct 2026)
  rubric-m2.md                Milestone 2 deliverables and rubric (due 20 Nov 2026)
AGENTS.md                   Shared context and rules (CLAUDE.md imports it)
requirements.md             FR / NFR tables and brief coverage check
use-cases/                  One file per use case (copy UC-TEMPLATE.md)
diagrams/                   PlantUML sources, one diagram per file (see README)
elicitation/                Stakeholder register, meeting notes (MEETING-TEMPLATE.md)
traceability.md             Requirement → use case → class → diagram matrix
decisions.md                Open questions and team decisions (DEC-nn)
ai-usage-log.md             AI usage log for the milestone reports
```

## Workflow

1. Check `decisions.md` for open questions and take them to stakeholder meetings.
2. Record meetings in `elicitation/`, then update decisions and requirements with a citation to the MTG.
3. Write use cases and diagrams from agreed requirements, and keep `traceability.md` in sync.
4. Work on a branch and open a PR. Never push to `main`.
