'''Generator + Loop 
Create a generator function that:
Generates numbers from 1 to n
Yields only numbers divisible by both 3 and 5
Print the generated values using a loop.'''
def gen(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            yield i
print(list(gen(50)))