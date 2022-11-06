from typing import List
import collections

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookie = collections.deque(sorted(s))
        g.sort()
        i = 0
        count = 0
        while cookie and i < len(g):
            cookie_size = cookie.popleft()
            if cookie_size >= g[i]:
                i += 1
                count += 1
        return count