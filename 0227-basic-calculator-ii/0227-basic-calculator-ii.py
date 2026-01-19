class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        op = '+'  
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if (ch in '+-*/') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] = stack[-1] * num
                elif op == '/':
                    stack[-1] = int(stack[-1] / float(num))

                op = ch
                num = 0

        return sum(stack)
        