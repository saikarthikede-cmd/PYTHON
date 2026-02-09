emails=["test@gmail.com","hello@abc","user@yahoo.com","admin@site.org"]
for email in emails:
    if "@" in email and email.endswith(".com"):
        print(f"{email}")
    else:
        continue