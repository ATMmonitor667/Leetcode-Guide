class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.size = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) + 1 <= self.size:
            self.stack.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        m = min(k, len(self.stack))
        for i in range(m):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)