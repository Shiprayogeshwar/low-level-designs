from products import Coke, Apple
from cart import Cart


if __name__ == "__main__":
    coke = Coke("coke", 50, "drinks")
    apple = Apple("apple", 20, "Fruit")

    cart = Cart()

    cart.add_to_cart(coke)
    cart.add_to_cart(apple)

    print(f"Total after discount {cart.get_total_price()}")
