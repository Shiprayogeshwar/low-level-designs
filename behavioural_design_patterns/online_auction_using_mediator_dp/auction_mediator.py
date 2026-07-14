from abc import ABC, abstractmethod


class AuctionMediator(ABC):

    @abstractmethod
    def place_bid(self, bidder, amount):
        pass

    @abstractmethod
    def add_bidder(self, bidder):
        pass
