class MyQueue:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        temp = []
        if self.empty():
            self.stack.append(x)
        else:
            while self.stack:
                temp.append(self.stack.pop())
            self.stack.append(x)
            while temp:
                self.stack.append(temp.pop())
    def pop(self) -> int:
        if self.empty():
            return False
        return self.stack.pop()
    def peek(self) -> int:
        if self.empty():
            return False
        return self.stack[-1]
    def empty(self) -> bool:
        return len(self.stack) == 0