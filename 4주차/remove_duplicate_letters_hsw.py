import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        seen = set()
        letters = []
        for char in s:
            count[char] -= 1
            if char in seen:
                continue
            while letters and letters[-1] > char and count[letters[-1]] > 0:
                seen.remove(letters.pop())
            letters.append(char)
            seen.add(char)
        return ''.join(letters)