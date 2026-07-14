from product_abstract import Product


class CouponDecorator(Product):
    pass


class PercentageCouponDecorator(CouponDecorator):
    def __init__(self, product, percent):
        self.product = product
        self.percent = percent

    def get_price(self):
        price = self.product.get_price()
        return price - (price * self.percent)/100
    

class TypeCouponDecorator(CouponDecorator):
    def __init__(self, product, percent, type):
        self.product = product
        self.percent = percent
        self.type = type
        self.eligible_types = []

    def get_price(self):
        price = self.product.get_price()
        if self.type in self.eligible_types:
            return price - (price * self.percent)/100
        return price
        
        
