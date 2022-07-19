from collections import deque
# 잘모르겠음

class my_queue:
  
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
  
  def push(self, x: int) -> None:
    while self.stack1:
      self.stack2.append(self.stack1.pop())
    self.stack1.append(x)
    while self.stack2:
      self.stack1.append(self.stack2.pop())
      
  def pop(self) -> int:
    
    return self.stack1.pop()
  
  def peek(self) -> int:
    return self.stack1[-1]
  
  def empty(self) -> bool:
    return len(self.stack1) == 0
  
my_queue = my_queue()

print(my_queue.push(1))
print(my_queue.push(2))
print(my_queue.peek())
print(my_queue.pop())
print(my_queue.empty())



