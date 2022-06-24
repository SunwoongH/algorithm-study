from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_max = []
        left = 0
        for h in height:
            left = max(left, h)
            left_max.append(left)
        right = 0
        for i in range(len(height) - 1, -1, -1):
            right = max(right, height[i])
            water += min(left_max[i], right) - height[i]
        return water