class MinStack:

    def __init__(self):
        self.custom_length = 0
        self.min_value_stack = list()
        self.custom_stack = list()

    def push(self, val: int) -> None:
        self.custom_stack.append(val)
        self.min_value_stack.append(min(val, self.min_value_stack[-1] if self.min_value_stack else val))
        self.custom_length +=1

    def pop(self) -> None:
        self.custom_stack.pop()
        self.min_value_stack.pop()
        self.custom_length -= 1

    def top(self) -> int:
        return self.custom_stack[self.custom_length-1]

    def getMin(self) -> int:
        return int(self.min_value_stack[-1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()