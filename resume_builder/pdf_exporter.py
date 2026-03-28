from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from .models import Resume


class ReportLabPdfExporter:
    def __init__(self) -> None:
        styles = getSampleStyleSheet()
        self._name_style = ParagraphStyle(
            "ResumeName",
            parent=styles["Title"],
            fontName="Courier-Bold",
            fontSize=22,
            leading=26,
            spaceAfter=8,
        )
        self._headline_style = ParagraphStyle(
            "ResumeHeadline",
            parent=styles["Normal"],
            fontName="Courier",
            fontSize=11,
            leading=14,
            spaceAfter=14,
        )
        self._section_style = ParagraphStyle(
            "ResumeSection",
            parent=styles["Heading2"],
            fontName="Courier-Bold",
            fontSize=12,
            leading=14,
            spaceBefore=12,
            spaceAfter=6,
        )
        self._body_style = styles["BodyText"]

    def export(self, resume: Resume, target: Path) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        doc = SimpleDocTemplate(
            str(target),
            pagesize=letter,
            rightMargin=0.65 * inch,
            leftMargin=0.65 * inch,
            topMargin=0.65 * inch,
            bottomMargin=0.65 * inch,
        )
        story: list[object] = []
        story.append(Paragraph(resume.basics.name, self._name_style))
        story.append(Paragraph(resume.basics.label, self._headline_style))
        if resume.basics.summary:
            story.append(Paragraph(resume.basics.summary, self._body_style))
            story.append(Spacer(1, 0.18 * inch))
        story.append(Paragraph("Experience", self._section_style))
        for job in resume.work:
            story.append(Paragraph(f"<b>{job.position}</b> — {job.name}", self._body_style))
            end_date = job.end_date or "Present"
            story.append(Paragraph(f"{job.start_date} – {end_date}", self._body_style))
            if job.summary:
                story.append(Paragraph(job.summary, self._body_style))
            for item in job.highlights:
                story.append(Paragraph(f"• {item}", self._body_style))
            story.append(Spacer(1, 0.12 * inch))
        if resume.education:
            story.append(Paragraph("Education", self._section_style))
            for edu in resume.education:
                line = f"<b>{edu.study_type} {edu.area}</b> — {edu.institution}"
                story.append(Paragraph(line, self._body_style))
                if edu.end_date:
                    story.append(Paragraph(edu.end_date, self._body_style))
        doc.build(story)
