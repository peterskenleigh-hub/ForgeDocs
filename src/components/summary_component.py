from src.models.profile import Profile


class SummaryComponent:

    def __init__(self, document, profile: Profile):
        self.document = document
        self.profile = profile

    def build(self):

        self.document.add_heading("Professional Summary", level=2)

        self.document.add_paragraph(
            self.profile.summary
        )