from auction_mediator import AuctionMediator

class Auction(AuctionMediator):

    def __init__(self):
        self.bidders = []
        self.highest_bid = 0
        self.highest_bidder = None

    def place_bid(self, bidder, amount):
        if amount <= self.highest_bid:
            print(f"The bid of {bidder.name} of amount {amount} was rejected!")
            return

        self.highest_bid = amount
        self.highest_bidder = bidder

        print(f"Highest bid received is {amount} from {bidder.name}")

        for b in self.bidders:
            if b is not bidder:
                b.receive_notification(bidder.name, amount)

    
    def add_bidder(self, bidder):
        self.bidders.append(bidder)
