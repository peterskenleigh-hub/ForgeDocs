from pathlib import Path

from docx import Document
from docx.shared import Inches

from src.models.profile import Profile
from src.components.header_component import HeaderComponent


class CVBuilder:

    def __init__(self, profile: Profile):
        self.profile = profile

    def build(self):

        document = Document()

        # Configure page margins
        section = document.sections[0]
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)

        # Build header
        HeaderComponent(
            document,
            self.profile
        ).build()

        # Ensure output folder exists
        output = Path("output")
        output.mkdir(exist_ok=True)

        # Save document
        document.save(output / "Kenleigh_Peters_CV.docx")