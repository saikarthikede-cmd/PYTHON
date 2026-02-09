class Calculator:
    def mult(self, *args):
        result = 1
        for i in args:
            result *= i
        return result
calcu = Calculator()
print(calcu.mult(1, 2, 3, 4))