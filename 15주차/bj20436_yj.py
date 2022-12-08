import sys
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

left, right = input().split()
str = sys.stdin.readline().strip()
distance = 0

def check_position(key):
  for i in range(3):
    if key in keyboard[i]:
      return i, keyboard[i].index(key)

left_x, left_y = check_position(left)
right_x, right_y = check_position(right)

for i in str:
  x, y = check_position(i)

  if (x <= 1 and y <= 4) or (x == 2 and y <= 3):
    distance += abs(left_x - x) + abs(left_y - y)
    left_x = x
    left_y = y

  else:
    distance += abs(right_x - x) + abs(right_y - y)    
    right_x = x
    right_y = y

time = len(str) + distance
print(time)