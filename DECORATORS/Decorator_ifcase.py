'''Decorator + Functions (Week 2)
Write a decorator named @validate_positive that:
Checks if all arguments passed to a function are positive numbers
If valid → execute the function
Else → print "Invalid input"
Apply this decorator to a function that returns the product of two numbers.
'''
def validation(prod):
    def wrapper(*args):
        for i in args:
            if i<=0:
                print("invalid input")
                return
        return prod(*args)
    return wrapper
@validation
def prod(a,b):
    return a*b
print(prod(5,4))