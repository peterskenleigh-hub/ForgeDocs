from docx.document import Document

from src.models.profile import Profile


class HeaderComponent:

    def __init__(self, document: Document, profile: Profile):
        self.document = document
        self.profile = profile

    def build(self):

        self.document.add_heading(
            self.profile.full_name,
            level=1
        )

        self.document.add_paragraph(
            self.profile.professional_title
        )

        self.document.add_paragraph(
            f"📧 {self.profile.email}"
        )

        self.document.add_paragraph(
            f"📞 {self.profile.phone}"
        )

        self.document.add_paragraph(
            f"📍 {self.profile.location}"
        )