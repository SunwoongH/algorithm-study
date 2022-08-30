from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = [0 for _ in range(len(temperatures))]
        temp = []
        for i, curr in enumerate(temperatures):
            if not temp or temp[-1][1] >= curr:
                temp.append((i, curr))
            else:
                while temp and temp[-1][1] < curr:
                    j, _ = temp.pop()
                    waiting[j] = i - j
                temp.append((i, curr))
        return waiting