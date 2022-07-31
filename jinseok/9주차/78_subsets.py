#부분집합
from itertools import combinations
list_k = [1,2,3]
result = []

for i in range(len(list_k)+ 1):
  result += list(combinations(list_k, i)) # 해당 길이를 가지는 부분 집합

print(result)