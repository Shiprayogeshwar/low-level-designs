from coupon_decorator import PercentageCouponDecorator, TypeCouponDecorator

class Cart:
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        product = PercentageCouponDecorator(product, 10)

        product = TypeCouponDecorator(product, 20, "Fruits")

        self.products.append(product)

    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.get_price()

        return total
