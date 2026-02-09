nums=[10,15,20,25,30,35,40]
d={}
for i in nums:
    if i%3==0 and i%5==0:
        continue
    else:
        if i%2==0:
            d[i]="even"
        else:
            d[i]="odd"
print(d)