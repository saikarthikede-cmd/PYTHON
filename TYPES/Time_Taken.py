import time

def time_taken(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper
@time_taken
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("Sum:", sum_n(10))
