class MinStack(object):

    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, val):
        self.arr.append(val)
        mini = min(self.minStack[-1], val) if len(self.minStack) != 0 else val
        self.minStack.append(mini)

    def pop(self):
        self.arr.pop()
        self.minStack.pop()

    def top(self):
        return self.arr[-1]

    def getMin(self):
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()