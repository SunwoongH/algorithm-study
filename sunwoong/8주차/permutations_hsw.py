from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def dfs(nums: List[int]) -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(nums)
                    path.pop()
        dfs(nums)
        return result