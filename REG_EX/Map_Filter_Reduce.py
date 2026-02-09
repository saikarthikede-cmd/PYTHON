from functools import reduce
words=["Python","java","C","javascript","Go"]
filtered=filter(lambda x:len(x)>3,words)
lowercased=list(map(lambda x:x.lower(),filtered))
total_length=reduce(lambda x,y:x+len(y),lowercased,0)
print(total_length)
