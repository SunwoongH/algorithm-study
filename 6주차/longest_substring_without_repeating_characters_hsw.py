import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = set()
        queue = collections.deque()
        pos = 0
        while pos < len(s):
            while s[pos] in seen:
                seen.remove(queue.popleft())
            seen.add(s[pos])
            queue.append(s[pos])
            result = max(result, len(queue))
            pos += 1
        return result