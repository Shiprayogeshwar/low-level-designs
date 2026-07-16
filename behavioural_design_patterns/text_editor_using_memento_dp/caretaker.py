class History:
    def __init__(self):
        self.history = []

    def push(self, memento):
        self.history.append(memento)

    def pop(self):
        return self.history.pop()
