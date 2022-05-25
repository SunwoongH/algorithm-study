#1. Palindrome Algorithm 유효한 팰린드롬 판별하기
# 팰린드롬 : 거꾸로 읽어도 제대로 읽는 것

def Valid_Palindrome(self, s:str) -> str:
    for i in range(len(s)):
        for j in range(i+1):
            temp =  s[j: len(s) - i+j]
            if temp == temp [: : -1]:
                return temp