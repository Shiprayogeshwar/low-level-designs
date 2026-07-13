class CharacterStyle:
    def __init__(self, font, size, colour, bold=False, italic=False):
        self.font = font
        self.size = size
        self.colour = colour
        self.bold = bold
        self.italic = italic

    def __str__(self):
        return f"{self.font}, {self.size}, {self.colour}"
