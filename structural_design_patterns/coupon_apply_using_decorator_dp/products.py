from product_abstract import Product


class Coke(Product):
    def get_price(self):
        return self.original_price
    

class Apple(Product):
    def get_price(self):
        return self.original_price
