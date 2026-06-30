from docx.shared import Pt
from docx.shared import RGBColor


class Theme:

    # Typography
    NAME_SIZE = Pt(24)
    TITLE_SIZE = Pt(13)
    BODY_SIZE = Pt(10)

    FONT = "Calibri"

    # Colours
    PRIMARY = RGBColor(34, 40, 49)
    SECONDARY = RGBColor(100, 100, 100)

    # Spacing
    SECTION_SPACE_BEFORE = Pt(12)
    SECTION_SPACE_AFTER = Pt(6)

    PAGE_MARGIN = 0.6