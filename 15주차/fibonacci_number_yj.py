def fib(self, N):
  x, y = 0, 1
  for i in range(0,N):
    x,y = y, x+y
  return x