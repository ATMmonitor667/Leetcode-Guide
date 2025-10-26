class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        word_set = set(wordDict)
        memo = {}

        def dfs(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            
            for end in range(index + 1, len(s) + 1):
                if s[index:end] in word_set and dfs(end):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False
        
        return dfs(0)

        