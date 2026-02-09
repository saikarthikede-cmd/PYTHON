import re
Pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
password = input("Enter your password: ")
if re.match(Pattern, password):
    print("Password is strong")
else:
    print("Password is weak")
