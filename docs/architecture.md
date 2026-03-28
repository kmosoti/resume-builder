# Architecture

## Layers

### Domain
Typed resume models.

Suggested classes:
- `Resume`
- `Basics`
- `Profile`
- `WorkEntry`
- `EducationEntry`
- `Certificate`
- `SkillGroup`

These objects should represent resume data, not rendering concerns.

### Repository
Responsible for loading and mapping canonical source data into domain objects.

### Validation
Responsible for schema checks and business-rule guardrails.

### Rendering
Responsible for turning domain objects into output formats.

Current output targets:
- HTML for layout iteration
- PDF for final distribution

### CLI
Thin wrapper only. The CLI should call services, not contain business logic.

## ReportLab direction
The PDF path should be built around reusable layout primitives rather than one giant export function.

Useful primitives:
- page metrics
- text style registry
- section block
- heading block
- bullet list block
- left rail block
- page break strategy

The exporter should be deterministic and easy to reason about. Small content changes should not cause chaotic layout shifts.

## Styling direction
The project should preserve the visual feel of a technical resume without depending on external theme runtimes.

Bias:
- monospace headings
- readable body copy
- two-column or rail-based structure
- compact metadata
- print-first spacing
