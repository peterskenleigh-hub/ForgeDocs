from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class Skill:
    """Represents a single professional skill."""

    name: str
    category: str = ""


@dataclass(slots=True)
class Experience:
    """Represents one job in a person's career."""

    job_title: str
    employer: str
    start_date: str
    end_date: str
    summary: str
    achievements: List[str] = field(default_factory=list)


@dataclass(slots=True)
class Education:
    """Represents one educational qualification."""

    qualification: str
    institution: str
    year_completed: str


@dataclass(slots=True)
class Profile:
    """Represents an entire professional profile."""

    full_name: str
    professional_title: str
    email: str
    phone: str
    location: str
    summary: str

    skills: List[Skill] = field(default_factory=list)
    experience: List[Experience] = field(default_factory=list)
    education: List[Education] = field(default_factory=list)