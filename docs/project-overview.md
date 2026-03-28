# Project Overview

## Purpose
This repository exists to make resume maintenance behave more like software maintenance than document editing.

The resume should be:
- structured
- validated
- public-safe by default
- easy to revise
- exportable without hand-formatting drift

## Intended audience
The primary audience is still you. A secondary audience is any technically minded person who wants to understand how you think about tooling, structure, and maintainability.

That means the repo should stay readable and coherent, not overengineered for its own sake.

## Core philosophy
The canonical resume is source data.

Everything else is derived:
- HTML is for visual iteration
- PDF is for final distribution
- validation protects source quality
- typed models protect code quality

## Current design bias
- fully Python
- virtual-environment friendly
- object-oriented code
- strong typing
- black-box component boundaries
- technical but readable layout

## Layout direction
The styling direction is inspired by developer-oriented resume themes:
- monospace headers
- clean sans-serif body copy
- strong whitespace
- compact metadata rail
- content-heavy main column
- print-first hierarchy

This should feel technical and deliberate without trying too hard to look clever.

## Export direction
ReportLab is the current target for final PDF output because it keeps page composition inside Python.

That gives up some of the flexibility of browser-driven layout, but gains determinism and clearer ownership of pagination.

## Privacy direction
The public source intentionally excludes direct address and phone. The public contact surface stays minimal unless there is a specific reason to expand it.

## Attribution direction
This project should remain honest about where ideas come from. Upstream references should be credited when they influenced:
- schema shape
- rendering ideas
- CLI workflow
- layout conventions

That credit belongs in docs, not hidden in commit history.
