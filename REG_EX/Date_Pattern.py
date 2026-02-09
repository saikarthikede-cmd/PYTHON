import re
date= "23-12-2024"
pattern=r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
pattern1="^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
print(bool(re.findall(pattern,date)))
print(bool(re.findall(pattern1,date)))