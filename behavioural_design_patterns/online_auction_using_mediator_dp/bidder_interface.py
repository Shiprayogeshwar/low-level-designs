from abc import ABC, abstractmethod


class BidderInterface(ABC):
    @abstractmethod
    def bid(self, amount):
        pass

    @abstractmethod
    def receive_notification(self, bidder_name, amount):
        pass
