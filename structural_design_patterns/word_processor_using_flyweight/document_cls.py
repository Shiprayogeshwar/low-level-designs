class Document:
    """ Document is a collection of character objects
    """
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def render(self):
        for ch in self.characters:
            ch.display()
