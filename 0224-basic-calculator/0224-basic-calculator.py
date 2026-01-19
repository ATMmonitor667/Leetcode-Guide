class Solution(object):
    def calculate(self, s):
        stack = []
        res = 0
        number = 0
        sign = 1

        i = 0
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                res += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                res += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                stack.append((res, sign))
                res = 0
                sign = 1
                number = 0

            elif ch == ')':
                res += sign * number
                number = 0
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign * res

            i += 1

        return res + sign * number