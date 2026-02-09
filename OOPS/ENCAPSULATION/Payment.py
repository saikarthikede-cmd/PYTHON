
class payment_system:
    def __init__(self, amount):  #encapsulation
        self.amount=amount
    def pay(self):
        print(f"Processing Pay payment of {self.amount}")
class credit_card(payment_system):
    def process_payment(self):
        print(f"Processing credit card payment of {self.amount}")
class upi(payment_system):
    def process_payment(self):
        print(f"Processing UPI payment of {self.amount}")
def process_payment(payment_method):
    payment_method.process_payment()
p1=credit_card(100)
p2=upi(150)
process_payment(p1)
process_payment(p2)