from character_style_factory import CharacterStyleFactory
from document_cls import Document
from character_cls import Character

def app():
    factory = CharacterStyleFactory()
    style = factory.get_style("Arial", 12, "Black")
    doc = Document()

    doc.add_character(Character("H", 0, 0, style))
    doc.add_character(Character("E", 0, 1, style))
    doc.add_character(Character("L", 0, 2, style))
    doc.add_character(Character("L", 0, 3, style))
    doc.add_character(Character("O", 0, 4, style))

    doc.render()


if __name__ == '__main__':
    app()