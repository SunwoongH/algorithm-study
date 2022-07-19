

class my_circular_queue:

    def __init__(self, k: int):
      self.q = [None] *k
      self.maxlen = k
      self.p1 = 0
      self.p2 = 0

    def enQueue(self, value: int) -> bool:
      if self.q[self.p2] is None:
        self.q[self.p2] = value
        self.p2 = (self.p2 + 1) % self.maxlen
        return True
      else:
        return False

    def deQueue(self) -> bool:
      if self.q[self.p1] is None:
        return False
      else:
        self.q[self.p1] = None
        self.p1 = (self.p1 + 1) % self.maxlen
        return True

    def Front(self) -> int:
      return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
      return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
      return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
      return self.p1 == self.p2 and self.q[self.p1] is not None

my_circular_queue1 = my_circular_queue(5)

print(my_circular_queue1.enQueue(10))
print(my_circular_queue1.enQueue(20))
print(my_circular_queue1.enQueue(30))
print(my_circular_queue1.enQueue(40))
print(my_circular_queue1.Rear())
print(my_circular_queue1.isFull())
print(my_circular_queue1.deQueue())
print(my_circular_queue1.deQueue())
print(my_circular_queue1.enQueue(50))
print(my_circular_queue1.enQueue(60))
print(my_circular_queue1.Rear())
print(my_circular_queue1.Front())