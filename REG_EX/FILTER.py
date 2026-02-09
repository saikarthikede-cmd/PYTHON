nums = [1, 2, 3, 4, 5, 6]
filtered = filter(lambda x: x % 2 == 0, nums)
mapped = map(lambda x: x * x, filtered)
print(list(mapped))