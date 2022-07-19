
def lengthOfLongestSubstring(s):
  used = {}
  max_length = start = 0 #최대값과 시작값을 0으로 초기화
  for index, char in enumerate(s):
    
    if char in used and start <= used[char]: # 이미 사용한 값이면서 시작 값보다 key 값인 char의 value 값이 더 크면 
      start = used[char] +1 # value 값을 1 증가 시킴
    else:
      max_length = max(max_length, index- start +1) # 
      
    used[char] = index
  return max_length

s = 'abcabcbb'
print(lengthOfLongestSubstring(s))
