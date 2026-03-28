from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import Resume


class HtmlRenderer:
    def __init__(self, templates_dir: Path, template_name: str) -> None:
        self._environment = Environment(
            loader=FileSystemLoader(templates_dir),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._template_name = template_name

    def render(self, resume: Resume) -> str:
        template = self._environment.get_template(self._template_name)
        return template.render(resume=resume)
