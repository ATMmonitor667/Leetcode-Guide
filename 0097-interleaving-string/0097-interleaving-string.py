class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(i, j, idx):
            if idx == len(s3):
                return i == len(s1) and j == len(s2)
            if (i, j) in memo:
                return memo[(i, j)]
            res = False
            if i < len(s1) and s1[i] == s3[idx]:
                res = dfs(i + 1, j, idx + 1)
            if not res and j < len(s2) and s2[j] == s3[idx]:
                res = dfs(i, j + 1, idx + 1)
            memo[(i, j)] = res
            return res
        return dfs(0, 0, 0)