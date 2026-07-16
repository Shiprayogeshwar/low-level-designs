from payments import CreditCardPayment, UPIPayment


if __name__ == "__main__":
    payment = CreditCardPayment()
    payment.make_payment(1000)

    print()

    payment = UPIPayment()
    payment.make_payment(500)
