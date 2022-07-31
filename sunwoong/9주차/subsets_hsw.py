from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def dfs(depth: int, start: int) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                if len(path) < len(nums):
                    path.append(nums[i])
                    dfs(depth + 1, i + 1)
                    path.pop()
        dfs(0, 0)
        return result
                