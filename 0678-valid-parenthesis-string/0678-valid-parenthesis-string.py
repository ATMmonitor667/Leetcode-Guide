class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        memo = {}

        def dfs(idx, count):
            if count < 0:
                return False

            if idx == len(s):
                return count == 0

            if (idx, count) in memo:
                return memo[(idx, count)]

            if s[idx] == "*":
                res = (
                    dfs(idx+1, count) or       
                    dfs(idx+1, count + 1) or    
                    dfs(idx+1, count - 1)       
                )
            elif s[idx] == "(":
                res = dfs(idx+1, count + 1)
            else:  
                res = dfs(idx+1, count - 1)

            memo[(idx, count)] = res
            return res

        return dfs(0, 0)
