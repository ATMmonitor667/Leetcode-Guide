class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        if "(" add it to the stack
        if "number" and previous is not "+" or "-" add it to the stack
        if "number" and previous is a "+" or "-" pop the end and then do an if statement
        if + then add the number to the end of the list if - then subtract the number to the end of the     list
        if ")" pop the value and the "(" and then add it to the the end of the arr
        """
        s = s.replace(" ", "")
        x = list(s)

        def evaluate(string):
            result = 0
            hold = ""
            sign = 1
            for i in string:
                if i != "+" and i != "-":
                    hold += i
                else:
                    result += sign * int(hold)
                    sign = 1 if i == "+" else -1
                    hold = ""
            result += sign * int(hold)
            return result

        def helper(string):
            if not string:
                return 0

            if string[0] == "(":
                # Find the corresponding closing parenthesis
                count = 1
                i = 1
                while i < len(string) and count > 0:
                    if string[i] == "(":
                        count += 1
                    elif string[i] == ")":
                        count -= 1
                    i += 1
                inner_result = helper(string[1:i - 1])
                return inner_result + helper(string[i:])

            sign = 1
            if string[0] == "-":
                sign = -1
                string = string[1:]

            word = ""
            i = 0
            while i < len(string) and string[i] not in ["+", "-", "(", ")"]:
                word += string[i]
                i += 1

            if i < len(string) and string[i] in ["+", "-"]:
                res = evaluate(word) * sign
                return res + helper(string[i:])

            return evaluate(word) * sign

        return helper(x)
    '''This solution does not quite work for all test cases but I will work on it later to the best of my ability.'''