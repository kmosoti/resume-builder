from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Basics, Certificate, EducationEntry, Profile, Resume, SkillGroup, WorkEntry


class ResumeRepository:
    def __init__(self, source_path: Path) -> None:
        self._source_path = source_path

    def load_raw(self) -> dict[str, Any]:
        return json.loads(self._source_path.read_text(encoding="utf-8"))

    def load(self) -> Resume:
        raw = self.load_raw()
        basics_raw = raw["basics"]
        basics = Basics(
            name=basics_raw["name"],
            label=basics_raw["label"],
            email=basics_raw["email"],
            url=basics_raw.get("url"),
            summary=basics_raw.get("summary"),
            profiles=[
                Profile(
                    network=profile["network"],
                    url=profile["url"],
                    username=profile.get("username"),
                )
                for profile in basics_raw.get("profiles", [])
            ],
        )
        work = [
            WorkEntry(
                name=item["name"],
                position=item["position"],
                start_date=item["startDate"],
                end_date=item.get("endDate"),
                summary=item.get("summary"),
                highlights=item.get("highlights", []),
            )
            for item in raw.get("work", [])
        ]
        education = [
            EducationEntry(
                institution=item["institution"],
                area=item["area"],
                study_type=item["studyType"],
                end_date=item.get("endDate"),
            )
            for item in raw.get("education", [])
        ]
        certificates = [
            Certificate(name=item["name"], issuer=item.get("issuer"))
            for item in raw.get("certificates", [])
        ]
        skills = [
            SkillGroup(name=item["name"], keywords=item.get("keywords", []))
            for item in raw.get("skills", [])
        ]
        return Resume(
            basics=basics,
            work=work,
            education=education,
            certificates=certificates,
            skills=skills,
            meta=raw.get("meta", {}),
        )
