from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def make_payment(self, amount):
        self.validate(amount)
        self.authenticate()
        self.process_payment(amount)
        self.generate_receipt(amount)
        self.send_notification()

    def validate(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        print("Payment validated")
    
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    def generate_receipt(self, amount):
        print(f"Receipt generated for ₹{amount}")

    def send_notification(self):
        print("Payment notification sent")
