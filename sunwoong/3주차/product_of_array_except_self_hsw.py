from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pivot = 1
        for i in range(len(nums)):
            output.append(pivot)
            pivot *= nums[i]
        pivot = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= pivot
            pivot *= nums[i]
        return output