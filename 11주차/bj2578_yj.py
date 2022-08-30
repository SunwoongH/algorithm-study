import sys
input = sys.stdin.readline

def check(x,y):
    global cnt
    
    if not row_check[x] and not sum(board[x]):
        row_check[x] = True
        cnt += 1

    if not col_check[y]:
        for i in range(5):
            if board[i][y]:
                break
        else:
            col_check[y] = True
            cnt += 1

    if x==y and not diagonal_check[0]:
        for i in range(5):
            if board[i][i]:
                break
        else:
            diagonal_check[0] = True
            cnt += 1
            
    if x+y==4 and not diagonal_check[1]:
        for i in range(5):
            if board[i][4-i]:
                break
        else:
            diagonal_check[1] = True
            cnt += 1

    if cnt >= 3:
        return True
    return False

def call(n):
    for i in range(5):
        for j in range(5):
            if board[i][j]==n:
                board[i][j]=0

                if check(i,j):
                    return True
                return False

board = [list(map(int, input().split())) for _ in range(5)]
call_list = [list(map(int, input().split())) for _ in range(5)]

row_check = {i: False for i in range(5)}
col_check = {i: False for i in range(5)}
diagonal_check = {i: False for i in range(2)}

cnt = 0
for i in range(5):
    for j in range(5):
        if call(call_list[i][j]):
            answer = i*5+j+1
            print(answer)
            exit()