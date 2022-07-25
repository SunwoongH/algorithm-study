import sys

def star(n, idx):
  if n == 1:
    lst[idx][idx] = '*'
    return
    
  l = 4*n -3

  for i in range(idx, l+idx):
    lst[idx][i] = '*'
    lst[idx+l-1][i] = '*'

    lst[i][idx] = '*'
    lst[i][idx+l-1] = '*'

  return star(n-1, idx+2)

n = int(sys.stdin.readline().strip())
side = 4*n - 3
lst = [[' ' for j in range(side)] for i in range(side)]

star(n,0)

for i in range(side):
  for j in range(side):
    print(lst[i][j], end="")
  print()