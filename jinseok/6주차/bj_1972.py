
import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()#\n을 없에 주기 위해

    if string =='*':
        break
    
    N = len(string)

    for D in range(1, N): #D-쌍을 의미

        D_check = set()
        
        for i in range(N-D): #D쌍별 조합

            D_value = string[i] + string[i+D]

            if D_value in D_check:
                print(string,"is NOT surprising.")
                break
            else:
                D_check.add(D_value)
        else:
            continue
        break

    else:
        print(string,"is surprising.")    



