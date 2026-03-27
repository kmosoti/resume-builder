# resume-builder

A Python-first, agent-friendly resume generator built around structured resume data.

## Design
This repo treats the resume as source data first and render output second.

Primary workflow:
- Python virtual environment for local tooling
- Python CLI as the main entrypoint
- Structured `resume.json` as canonical content
- Optional theme rendering path that can target JSON Resume themes such as Developer Mono

## Quick start
Create and activate a virtual environment.

Install Python dependencies.

Then run the builder:
- `python -m resume_builder validate`
- `python -m resume_builder render-html`
- `python -m resume_builder export-pdf`

## Layout
- `src/resume.json` canonical resume source
- `resume_builder/` Python package and CLI entrypoint
- `templates/` local render templates
- `dist/` generated artifacts
- `docs/reference-sources.md` upstream references and attribution notes

## Notes
- Phone number is intentionally omitted from the public source.
- Current email can later be swapped to a custom domain.
- The long-term goal is a source-first system that agents can safely update without editing PDFs directly.
