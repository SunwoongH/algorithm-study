import sys
input = sys.stdin.readline

sound=list(input().rstrip())
answer=[]

def next(prev,curr):
    for a in answer:
        if a[-1]==prev:
            a.append(curr)
            return True
    return False

flag=0
for s in sound:
    if s=='q':
        if not next('k','q'):
            answer.append(['q'])
    elif s=='u':
        if not next('q', 'u'):
            flag=1
            break
    elif s=='a':
        if not next('u', 'a'):
            flag = 1
            break
    elif s=='c':
        if not next('a', 'c'):
            flag = 1
            break
    else:
        if not next('c', 'k'):
            flag = 1
            break

count=0
for a in answer:
  if 'quack' in ''.join(a) and len(a)%5==0:
    count+=1
  else:
    flag=1
    break

if flag==1:
    print(-1)
else:
    print(count)