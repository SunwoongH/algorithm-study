from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buy = 0
        is_possible = False
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                if not is_possible:
                    is_possible = True
                    buy = prices[i]
            elif prices[i] > prices[i + 1]:
                if is_possible:
                    is_possible = False
                    answer += prices[i] - buy
                    buy = 0
        if is_possible:
            answer += prices[-1] - buy
        return answer