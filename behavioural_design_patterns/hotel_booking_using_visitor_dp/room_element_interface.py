from abc import ABC, abstractmethod


class RoomElement(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass
