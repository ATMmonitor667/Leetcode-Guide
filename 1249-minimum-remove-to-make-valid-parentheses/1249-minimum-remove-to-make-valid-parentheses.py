class Solution(object):
    def minRemoveToMakeValid(self, s):
        ans = []
        count = 0
        for i in range(len(s)):
            if s[i] != "(" and s[i] != ")":
                ans.append(s[i])

            if s[i] == ")" and count == 0:
                continue

            if s[i] == "(":
                ans.append("(")
                count += 1

            if s[i] == ")" and count > 0:
                ans.append(")")
                count -= 1

        word = ''.join(ans)

        removeStack = []

        for index, char in enumerate(word):
            if char == "(":
                removeStack.append((char, index))
            elif char == ")":
                removeStack.pop()

        removeIndex = set()

        for char, index in removeStack:
            removeIndex.add(index)

        word = ''.join(
            char for index, char in enumerate(word)
            if index not in removeIndex
        )

        return word