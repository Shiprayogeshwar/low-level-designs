from visitor_interface import VisitorInterface


class BillingVisitor(VisitorInterface):
    def __init__(self):
        self.total = 0

    def visit_room(self, room):
        self.total += room.price

    def visit_food(self, food):
        self.total += food.price

    def visit_spa(self, spa):
        self.total += spa.price


class TaxVisitor(VisitorInterface):
    def __init__(self):
        self.tax = 0

    def visit_room(self, room):
        self.tax += room.price * 0.18

    def visit_food(self, food):
        self.tax += food.price * 0.05

    def visit_spa(self, spa):
        self.tax += spa.price * 0.12


class DiscountVisitor(VisitorInterface):
    def __init__(self):
        self.discount = 0

    def visit_room(self, room):
        self.discount += room.price * 0.10

    def visit_food(self, food):
        self.discount += food.price * 0.05

    def visit_spa(self, spa):
        self.discount += spa.price * 0.15