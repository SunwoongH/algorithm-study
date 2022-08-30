from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def dfs(candidates: List[int], start: int, num: int) -> None:
            if num > target:
                return
            elif num == target:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(candidates, i, num + candidates[i])
                path.pop()
        dfs(candidates, 0, 0)
        return result