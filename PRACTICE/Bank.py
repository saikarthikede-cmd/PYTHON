class Payment:
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        raise NotImplementedError
class CreditCardPayment(Payment):
    def pay(self):
        return f"Paid {self.amount} using Credit Card"
class UPIPayment(Payment):
    def pay(self):
        return f"Paid {self.amount} using UPI"
def process_payment(payment_obj):
    print(payment_obj.pay())

p1 = CreditCardPayment(1000)
p2 = UPIPayment(500)
process_payment(p1)
process_payment(p2)
