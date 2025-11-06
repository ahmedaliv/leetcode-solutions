class MinStack:
    # the idea here is to use the prefix min approach(for each element compute the current min for it)
    # but this is making it O(N) memory
    # can we improve that ?    
    def __init__(self):
        self.data = []
        self.mn_stk = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.mn_stk) == 0:
            self.mn_stk.append(val)
        else:
            self.mn_stk.append(min(self.mn_stk[-1],val))

    def pop(self) -> None:
        self.data.pop()
        self.mn_stk.pop()
        

    def top(self) -> int:
        return self.data[-1] 

    def getMin(self) -> int:
        return self.mn_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()