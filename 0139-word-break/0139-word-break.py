class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordSet = set(wordDict)
        memo = {}

        def dfs(index, path):
            if index == len(s):
                return path == "" or path in wordSet

            if (index, path) in memo:
                return memo[(index, path)]

            res = False

            
            new_path = path + s[index]
            if new_path in wordSet:
                res = dfs(index + 1, "") or dfs(index + 1, new_path)
            else:
                res = dfs(index + 1, new_path)

            memo[(index, path)] = res
            return res

        return dfs(0, "")

        