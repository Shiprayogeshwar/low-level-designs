class Booking:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def accept(self, visitor):
        for item in self.items:
            item.accept(visitor)
