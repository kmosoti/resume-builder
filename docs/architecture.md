# Architecture

## Direction
The builder should stay fully Python.

The canonical input is structured resume data. Rendering and export are downstream concerns.

## Design priorities
- source first
- black-box components
- object-oriented code
- strong typing
- public-safe output by default
- easy for agents to update without touching rendered artifacts

## Proposed component split

### Domain layer
Typed models representing the resume itself.

Suggested objects:
- `Resume`
- `Basics`
- `Profile`
- `WorkEntry`
- `EducationEntry`
- `Certificate`
- `SkillGroup`

These should be plain, validated domain objects.

### Application layer
Services that orchestrate work.

Suggested services:
- `ResumeRepository` for loading and saving source data
- `ResumeValidator` for schema and business-rule checks
- `HtmlRenderer` for template-driven rendering
- `PdfExporter` for final PDF creation
- `BuildService` as the high-level facade used by CLI or agents

### Interface layer
Thin CLI entrypoints only.

The CLI should call services, not contain business logic.

## Layout direction
The visual direction should remain inspired by Developer Mono, but implemented locally in Python templates.

The current bias should be:
- monospace headings
- sans-serif body
- clean hierarchy
- wide whitespace
- print-friendly structure
- no gimmicks

A strong first layout is a two-column page with:
- left rail for profiles, certifications, compact skills
- main column for summary, work history, education

This mirrors the feel of technical resume themes while staying readable.

## PDF export direction
There are two realistic pure-Python paths.

### Option A
Render HTML from Jinja and convert to PDF with a Python-compatible renderer.

Pros:
- keeps styling centralized in HTML/CSS-like thinking
- easiest to iterate visually

Cons:
- pure-Python HTML-to-PDF options can be less predictable depending on CSS support

### Option B
Generate PDF directly with a Python PDF library such as ReportLab.

Pros:
- full control
- deterministic output
- no dependency on browser tooling

Cons:
- layout code is more verbose
- slower to iterate visually

## Recommended path
Use a hybrid progression:
1. finalize typed domain models
2. render stable HTML locally with Jinja
3. keep a simple local PDF exporter first
4. only later decide whether to stay direct-PDF or adopt a stronger HTML-to-PDF path

## Practical conclusion
Python should own the pipeline end to end.
The repo should not depend on Node for final rendering.
If an upstream theme is referenced, it should only inform layout ideas, not become a runtime dependency.
