import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(lambda x: x[1] if x[0] in jewels else 0, collections.Counter(stones).items()))