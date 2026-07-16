from payment_abstract import PaymentProcessor


class CreditCardPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating using OTP")

    def process_payment(self, amount):
        print(f"Charging ₹{amount} to Credit Card")


class UPIPayment(PaymentProcessor):

    def authenticate(self):
        print("Authenticating using UPI PIN")

    def process_payment(self, amount):
        print(f"Debiting ₹{amount} through UPI")
