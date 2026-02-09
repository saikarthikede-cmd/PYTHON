import re
def matching(nums):
    for num in nums:
        pattern=r"^\d+"
        if re.match(pattern, str(num)):
            yield num
nums=[1234567890,123,5869]
print(list((matching(nums))))