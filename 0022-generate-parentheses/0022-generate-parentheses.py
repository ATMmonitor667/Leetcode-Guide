class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        one way we can solve it is by a count system.
        if the count is ever negative that measns that
        the parenthesis is invalid and therefore the string 
        as a whole is invalid and we therefore return out 
        of there
        if the number is more than 0 its good 
        at the end if the number is 0 then the path is valid and we add it to the 
        ans
        """
        res = []
        def dfs(path, count):
            if len(path) == 2 * n:
                if count == 0:
                    res.append(path[:])
                    return
                return 
            if len(path) < 2 * n and count < 0:
                return 
            else:
                dfs(path + "(", count + 1)
                dfs(path + ")", count - 1)
        dfs("", 0)
        return res


