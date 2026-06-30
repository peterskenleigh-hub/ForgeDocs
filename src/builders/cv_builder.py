from docx import Document

from src.models.profile import Profile
from src.components.header_component import HeaderComponent


class CVBuilder:

    def __init__(self, profile: Profile):
        self.profile = profile

    def build(self):

        document = Document()

        HeaderComponent(
            document,
            self.profile
        ).build()

        document.save("output/Kenleigh_Peters_CV.docx")