from character_style import CharacterStyle
class CharacterStyleFactory:
    def __init__(self):
        self.styles = {}

    def get_style(self, font, size, colour, bold=False, italic=False):
        key = (font, size, colour, bold, italic)
        if key not in self.styles:
            self.styles[key] = CharacterStyle(font, size, colour, bold, italic)
        return self.styles[key]
