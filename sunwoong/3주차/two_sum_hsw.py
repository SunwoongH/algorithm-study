from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i, num in enumerate(nums):
            table[num] = i
        for i, num in enumerate(nums):
            find = target - nums[i]
            if find in table and table[find] != i:
                return [i, table[find]]