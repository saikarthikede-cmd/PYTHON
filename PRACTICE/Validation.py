import re
emails=["123@4.5","12@3.4", "abc@gmail.com", "sai@gmail.com"]
phone_no=["+91-9876543210","+91-1234567890","+919876543210","9876543210"]
pattern1=r'^\w+@\w+\.\w+$'
pattern2=r'^\+91-\d{10}$'
for email in emails:
    if re.match(pattern1,email):
        print(email,"is valid")
    else:
        print(email,"is invalid")
for phoneno in phone_no:
    if re.match(pattern2,phoneno):
        print(phoneno,"is valid")
    else:
        print(phoneno,"is invalid")
