from editor_memento import EditorMemento

class TextEditor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def save(self):
        return EditorMemento(self.content)
    
    def restore(self, memento):
        self.content = memento.content

    def show(self):
        print(self.content)
