from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def dfs(nums: List[int], start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(nums, i + 1)
                path.pop()
        dfs(range(1, n + 1), 0)
        return result