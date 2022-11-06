from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            total = 0
            count = 0
            j = i
            while count < n: 
                total += gas[j % n] - cost[j % n]
                if total < 0: 
                    break
                count += 1
                j += 1
            if count == n and total >= 0: 
                return i
        return -1