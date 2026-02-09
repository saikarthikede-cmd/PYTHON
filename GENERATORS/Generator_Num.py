def generator(n):
    for i in range(1,n):
        if i%3==0 and i%5==0:
            yield i
print(list(generator(50)))
