from caretaker import History
from originator import TextEditor


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hey")
    history.push(editor.save())

    editor.write(" Shipra")
    history.push(editor.save())

    editor.write("!!!")

    editor.show()

    # Undo
    editor.restore(history.pop())
    editor.show()

    # Undo again
    editor.restore(history.pop())
    editor.show()