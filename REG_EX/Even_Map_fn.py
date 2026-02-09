import re
nums = [1, 2, 3, 4, 5]
filtered =filter(lambda x: (x*x)%2==0 ,nums)
even = map(lambda x: x*x ,filtered  )
print(list(even))

