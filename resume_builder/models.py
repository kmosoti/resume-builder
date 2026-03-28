from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Profile:
    network: str
    url: str
    username: str | None = None


@dataclass(slots=True)
class Basics:
    name: str
    label: str
    email: str
    url: str | None = None
    summary: str | None = None
    profiles: list[Profile] = field(default_factory=list)


@dataclass(slots=True)
class WorkEntry:
    name: str
    position: str
    start_date: str
    end_date: str | None = None
    summary: str | None = None
    highlights: list[str] = field(default_factory=list)


@dataclass(slots=True)
class EducationEntry:
    institution: str
    area: str
    study_type: str
    end_date: str | None = None


@dataclass(slots=True)
class Certificate:
    name: str
    issuer: str | None = None


@dataclass(slots=True)
class SkillGroup:
    name: str
    keywords: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Resume:
    basics: Basics
    work: list[WorkEntry]
    education: list[EducationEntry] = field(default_factory=list)
    certificates: list[Certificate] = field(default_factory=list)
    skills: list[SkillGroup] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)
