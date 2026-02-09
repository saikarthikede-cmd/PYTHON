#Task 2:
'''
Create a Python decorator called execution_logger that performs the following:
Displays a message before a function runs:
 Starting execution of <function_name>
Displays a message after the function completes:
 Completed execution of <function_name>
Define a function multiply_numbers(x, y) that:
Takes two numbers as arguments
Returns their multiplication result
Apply the execution_logger decorator to the multiply_numbers function.
'''

def exection_logger(func):
    def wrapper(*args):
        print(f"starting exection")
        print(func(*args))
        print(f"completed exection")
        return
    return wrapper
@exection_logger
def prod(a,b):
    return a*b

print(prod(2,3))
