def counter(func):
    cnt=0
    def wrapper():
        #nonlocal lets wrapper modify cnt from the outer function
        nonlocal cnt
        cnt+=1
        print("called",cnt,"times")
        func()
    return wrapper
@counter
def greet():
    print("Hello World!!")
greet()
greet()
