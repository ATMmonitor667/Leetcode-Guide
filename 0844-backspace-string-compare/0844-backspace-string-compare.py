class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def transform(string):
            word = ""
            stack = []
            for i in range(len(string)):
                if string[i] != "#":
                    stack.append(string[i])
                elif len(stack) and string[i] == "#":
                    stack.pop()
            return ''.join(stack)
        return transform(s) == transform(t)
       