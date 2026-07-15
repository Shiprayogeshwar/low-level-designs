from abc import ABC, abstractmethod


class VisitorInterface(ABC):
    @abstractmethod
    def visit_room(self, room):
        pass

    @abstractmethod
    def visit_food(self, food):
        pass

    @abstractmethod
    def visit_spa(self, spa):
        pass
