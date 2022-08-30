import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        queue = collections.deque()
        for char in s:
            if char.isalnum():
                queue.append(char.lower())
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True