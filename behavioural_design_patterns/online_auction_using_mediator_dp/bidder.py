from bidder_interface import BidderInterface


class Bidder(BidderInterface):

    def __init__(self, name, auction):
        self.name = name
        self.auction = auction

    def bid(self, amount):
        print(f"{self.name} bids {amount}")
        self.auction.place_bid(self, amount)

    def receive_notification(self, bidder_name, amount):
        print(f"{self.name} notified:"
              f"{bidder_name} placed bid {amount}")
