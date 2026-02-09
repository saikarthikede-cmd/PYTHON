class bankaccount():
    def __init__(self, bal=0):
        self._bal = bal
    def deposit(self,amt):
        if amt>0:
            self._bal+=amt
            return self._bal
    def withdraw(self,amt):
        if 0<amt<=self._bal:
            self._bal-=amt
            return self._bal
    def get_balance(self):
        return self._bal
a=bankaccount(100)
print(a.deposit(50))
print(a.withdraw(30))
print(a.get_balance())  
