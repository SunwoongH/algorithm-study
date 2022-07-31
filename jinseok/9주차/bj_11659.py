#구간의 합 구하기 4
import sys

# def for_sumpfs(i, j):
#   sum_pfs = 0
#   for k in range(i-1,j):
#     sum_pfs = sum_pfs + pfs[k]
#   print(sum_pfs)
  
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_list = [0]
result = 0
for i in range(len(arr)):
    result += arr[i]
    sum_list.append(result)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])
  # for_sumpfs(i, j)
  

  