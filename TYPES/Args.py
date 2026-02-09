def add_numbers(*args):
    total = 0
    for num in args:
        total=total+num
    return total
print(add_numbers(10, 20, 30))
