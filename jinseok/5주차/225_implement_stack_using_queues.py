from collections import deque


class my_stack:
  
  def __init__(self):
    self.q1 = deque()
    self.q2 = deque()
  
  def push(self, x: int) -> None:
    while self.q1:
      self.q2.append(self.q1.pop())
    self.q1.append(x)
    while self.q2:
      self.q1.append(self.q2.popleft())
      
  def pop(self) -> int:
    
    return self.q1.popleft()
  
  def top(self) -> int:
    return self.q1[0]
  
  def empty(self) -> bool:
    return len(self.q1) == 0
  
my_stack = my_stack()

print(my_stack.push(1))
print(my_stack.push(2))
print(my_stack.top())
print(my_stack.pop())
print(my_stack.empty())



