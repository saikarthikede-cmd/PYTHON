def validate_positive(func):
    def wrapper(*args):
        for i in args:
            if i <= 0:
                print("Invalid input")
                return
        return func(*args)
    return wrapper
@validate_positive
def product(a,b):
    return a* b

print(product(5,4))
