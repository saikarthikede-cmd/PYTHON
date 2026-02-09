import re
#text = "that cat rat"
#print(re.findall(r'.at', text))

#text = "cat caaat ct"
#print(re.findall(r'ca*t', text))
#print(re.findall(r'ca+t', text))

text = "color colour"
print(re.findall(r'colo?r', text))
