class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in operations:
            if len(stack) > 0 and i == 'C':
                stack.pop()
            elif len(stack) > 0 and i == 'D':
                stack.append(2*stack[-1])
            elif len(stack) >= 2 and i == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack) if len(stack) > 0 else 0