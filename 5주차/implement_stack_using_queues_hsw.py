from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        if self.empty():
            self.queue.append(x)
        else:
            self.queue.append(x)
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        if self.empty():
            return False
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return len(self.queue) == 0