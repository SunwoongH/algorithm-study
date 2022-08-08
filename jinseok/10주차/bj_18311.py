#왕복

import sys
# 입력 처리
input = sys.stdin.readline
N, K = map(int, input().split())

list_k = list(map(int, input().split()))

# 조건


#갔다가
# ??? 조건문 넣으면 틀림 이유??

#if K > sum(list_k):
for i in range(N):
    K -= list_k[i]
    if K < 0:
        print(i+1)
        break
else:
    # 왔다가
    for i in range(N-1, -1, -1): # range(start, stop, step) = stop은 포함되지 않음

        K -= list_k[i]
        if K < 0:
            print(i+1)
            break





