from pathlib import Path
import json
import click
from jsonschema import Draft7Validator
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "resume.json"
DIST = ROOT / "dist"
TEMPLATES = ROOT / "templates"


def load_resume() -> dict:
    return json.loads(SRC.read_text(encoding="utf-8"))


def built_in_schema() -> dict:
    return {
        "type": "object",
        "required": ["basics", "work"],
        "properties": {
            "basics": {"type": "object"},
            "work": {"type": "array"},
            "education": {"type": "array"},
            "skills": {"type": "array"},
            "certificates": {"type": "array"},
            "meta": {"type": "object"}
        }
    }


@click.group()
def main() -> None:
    """Source-first resume builder."""


@main.command("validate")
def validate() -> None:
    data = load_resume()
    validator = Draft7Validator(built_in_schema())
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        for error in errors:
            click.echo(f"INVALID: {list(error.path)} {error.message}")
        raise SystemExit(1)
    click.echo("Resume source is valid against local schema guardrails.")


@main.command("render-html")
def render_html() -> None:
    DIST.mkdir(exist_ok=True)
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("developer_mono.html.j2")
    output = template.render(resume=load_resume())
    target = DIST / "resume.html"
    target.write_text(output, encoding="utf-8")
    click.echo(f"Wrote {target}")


@main.command("export-pdf")
def export_pdf() -> None:
    click.echo("PDF export is intentionally left as the next step. The repo is scaffolded so this can target either a Python-native PDF path or a JSON Resume theme render pipeline.")


if __name__ == "__main__":
    main()
