class Solution(object):
     def decodeString(self, s):
        stack = []
        currString = ""
        currNum = 0

        for ch in s:
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)

            elif ch.isalpha():
                currString += ch

            elif ch == "[":
                stack.append((currString, currNum))
                currString = ""
                currNum = 0

            elif ch == "]":
                prevString, num = stack.pop()
                currString = prevString + num * currString

        return currString