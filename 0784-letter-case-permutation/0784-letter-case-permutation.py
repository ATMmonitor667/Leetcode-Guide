class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = []

        def backtracking(i, path):

            if i == len(s):
                res.append(''.join(path))
                return

            char = s[i]

            if char.isdigit():
                backtracking(i + 1, path + [char])

            else:
                backtracking(i + 1, path + [char.lower()])

                backtracking(i + 1, path + [char.upper()])

        backtracking(0, [])
        return res

        