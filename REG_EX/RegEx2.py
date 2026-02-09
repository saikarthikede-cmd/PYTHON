import re
text="for 3 items it cost me 500"
for match in re.finditer(r'\d+', text):
    print(match.group(), match.start(), match.end())
result = re.split(r'\s', text)
print(result)
