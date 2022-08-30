class Solution:
    def palindrome(self, s: str, isOdd: bool) -> str:
        result = ''
        ratio = 2 if isOdd else 1
        for pivot in range(len(s) - 1):
            left, right = pivot, pivot + ratio
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            result = max(result, s[left + 1:right], key=lambda x: len(x))
        return result
            
    def longestPalindrome(self, s: str) -> str:
        result = ''
        return max(result, self.palindrome(s, True), self.palindrome(s, False), key=lambda x: len(x)) if len(s) > 1 else s