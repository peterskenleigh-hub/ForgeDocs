import json
from pathlib import Path

from src.models.profile import Profile


def load_profile(profile_name: str) -> Profile:
    """
    Loads a profile from a JSON file and returns a Profile object.
    """

    profile_path = Path("data") / "profiles" / f"{profile_name}.json"

    with profile_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return Profile(
        full_name=data["full_name"],
        professional_title=data["professional_title"],
        email=data["email"],
        phone=data["phone"],
        location=data["location"],
        summary=data["summary"],
    )