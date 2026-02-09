#test
import re
emails=["test@gmail.com", "abc.com", "user@domain"]
for email in emails:
    if email.endswith(".com") and bool(re.search("@",email))==True:
        print("Valid email")
    else:
        print("InValid email")
