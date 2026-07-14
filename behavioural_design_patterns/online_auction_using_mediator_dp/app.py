from bidder import Bidder
from auction import Auction


if __name__ == "__main__":
    auction = Auction()

    b1 = Bidder("Messi", auction)
    b2 = Bidder("Neymar", auction)
    b3 = Bidder("Ronaldo", auction)

    
    auction.add_bidder(b1)
    auction.add_bidder(b2)
    auction.add_bidder(b3)

    b1.bid(100)
    b2.bid(200)
    b3.bid(1000)
