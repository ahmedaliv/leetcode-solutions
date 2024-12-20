class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_e = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_e:
            self.min_stack.append(val)
            self.min_e = self.min_stack[-1]

    def pop(self) -> None:
        if self.stack:
            top = self.top()
            self.stack.pop()
            if self.min_stack and top == self.min_stack[-1]:
                self.min_stack.pop()
                self.min_e = self.min_stack[-1] if self.min_stack else float('inf')

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_e if self.stack else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
