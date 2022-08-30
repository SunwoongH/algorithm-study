class MyCircularQueue:
    def __init__(self, k: int):
        self.circular_queue = [None] * k
        self.max_len = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.circular_queue[self.p2] = value
            if self.p2 == self.max_len - 1:
                self.p2 = 0
            else:
                self.p2 += 1
            return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.circular_queue[self.p1] = None
            if self.p1 == self.max_len - 1:
                self.p1 = 0
            else:
                self.p1 += 1
            return True
        
    def Front(self) -> int:
        if self.circular_queue[self.p1] != None:
            return self.circular_queue[self.p1]
        return -1

    def Rear(self) -> int:
        if self.circular_queue[self.p2-1] != None: 
            return self.circular_queue[self.p2-1]
        return -1
    
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and not self.circular_queue[self.p1]

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.circular_queue[self.p1]