from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, original_price, type):
        self.name = name
        self.original_price = original_price
        self.type = type

    @abstractmethod
    def get_price(self):
        pass
