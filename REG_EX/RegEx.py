import re
text="for 3 items it cost me 500"
first_num= re.match(r'for',text)
search=re.search(r'cost',text)
all_num= re.findall(r'\d+',text)
'''
print(bool(first_num.group()))
print(bool(search))
print(all_num)
'''
for match in re.finditer(r'\d+', text):
    print(match.group(), match.start(), match.end())
