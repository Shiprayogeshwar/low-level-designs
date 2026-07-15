from room_element_interface import RoomElement


class SingleRoom(RoomElement):
    def __init__(self):
        self.price = 1000

    def accept(self, visitor):
        visitor.visit_room(self)


class DeluxeRoom(RoomElement):
    def __init__(self):
        self.price = 2000

    def accept(self, visitor):
        visitor.visit_room(self)


class FoodOrder(RoomElement):
    def __init__(self):
        self.price = 500

    def accept(self, visitor):
        visitor.visit_food(self)


class SpaOrder(RoomElement):
    def __init__(self):
        self.price = 800

    def accept(self, visitor):
        visitor.visit_spa(self)
