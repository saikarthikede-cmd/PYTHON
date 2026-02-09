num = int(input("Enter a num :"))
if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif num < 0:
    print("Negitive")
else:
    print("ZERO")
