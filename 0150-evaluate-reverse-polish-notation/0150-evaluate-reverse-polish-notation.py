class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        ops = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in ops:
                stack.append(int(t))  # handles negatives like "-11"
                continue

            b = stack.pop()
            a = stack.pop()

            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else: 
                q = abs(a) // abs(b)
                stack.append(q if a * b >= 0 else -q)

        return stack[0]