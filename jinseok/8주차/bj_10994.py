import sys

def stars(depth, x):
    if depth == 1:
        Map[x][x] = '*'
        return
    l = 4 * depth -3
    
    for i in range(x, l+x):
        Map[x][i] = '*' #위
        Map[x+l-1][i] = '*'#아래
        Map[i][x] = '*' # 왼쪽
        Map[i][x+l-1] = '*' # 오른쪽
        
    stars(depth-1, x+2)
    return
    
    
n = int(sys.stdin.readline())
length = 4 * n-3

Map = [[' '] * length for _ in range(length)] # 2차원 배열 만드는 방법

stars(n,0)

for i in range(length):
    for j in range(length):
        print(Map[i][j], end="")
    print()