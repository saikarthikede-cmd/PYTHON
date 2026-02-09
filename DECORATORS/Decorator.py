def my_decorator(func):
    def wrapper():
        print("Before function")   #when fn is called 1st executes
        func()   #function is called here
        print("After function")
    return wrapper
@my_decorator
def hello():
    print("Hello World!!")
hello()
