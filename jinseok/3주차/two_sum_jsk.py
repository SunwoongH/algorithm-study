from ctypes.wintypes import tagRECT


nums = [2,7,11,15]
target = 9
num_result = {}

for i, num in enumerate(nums):
    if target - num in num_result:
        print([ num_result[target - num],i])
    num_result[num] = i


