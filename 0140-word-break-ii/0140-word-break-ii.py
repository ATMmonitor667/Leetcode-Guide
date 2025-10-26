class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        res = set()

        def dfs(index, path):
            if index == len(s):
                res.add(path.strip()) 
                return
            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordSet:
                    dfs(i, path + s[index:i] + " ")

        dfs(0, "")
        return list(res)
