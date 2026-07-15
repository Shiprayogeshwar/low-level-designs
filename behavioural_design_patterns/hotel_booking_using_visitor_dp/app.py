from rooms import SingleRoom, DeluxeRoom, FoodOrder, SpaOrder
from booking import Booking
from visitors import BillingVisitor, TaxVisitor, DiscountVisitor


if __name__ == "__main__":
    booking = Booking()
    single_room = SingleRoom()
    deluxe_room = DeluxeRoom()
    food_order = FoodOrder()
    spa_order = SpaOrder()

    booking.add_item(deluxe_room)
    booking.add_item(food_order)
    booking.add_item(spa_order)

    billing = BillingVisitor()
    booking.accept(billing)

    tax = TaxVisitor()
    booking.accept(tax)

    discount = DiscountVisitor()
    booking.accept(discount)

    print(f"All services total: {billing.total}")
    print(f"Tax: {tax.tax}")
    print(f"Discount: {discount.discount}")

    print(f"Total: {billing.total} + {tax.tax} - {discount.discount}")