class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        # one stack only
        # self.stack.append(value)
        
        self.stack.append(value)
        if len(self.min_stack) == 0:
            self.min_stack.append(value)
        else:
            small = self.min_stack[-1]
            if value <= small:
                self.min_stack.append(value)
                                

    def pop(self) -> None:
        # one stack only
        # self.stack.pop()
        
        if len(self.stack) == 0:
            return -1
        small = self.stack.pop()
        if small == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # one stack only
        # smallist = min(self.stack)
        # return smallist

        if len(self.min_stack) == 0:
            return -1
        else:
            smallist = self.min_stack[-1]
            return smallist
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()