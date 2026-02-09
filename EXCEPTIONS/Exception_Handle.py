'''Exception Handling + Functions (Week 1)
Write a function that:
Accepts two numbers from the user
Performs division
Handles:
ZeroDivisionError
ValueError
Prints a proper message in each case
Executes a finally block
'''
def division(a,b):
    if isinstance(a,int) and isinstance(b,int):
        try:
            result=a//b
            return result
        except ZeroDivisionError:
            print("numbers cant be zero")
        except TypeError:
            print("TypeError check again")
        finally:
            print("executed")
        print(result)
print(division(4,'x'))

    