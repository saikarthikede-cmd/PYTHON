def prime(n):
    for i in range(2,n):
        count=0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                count=count+1
        if count==0:
            print(i)
print(prime(10))