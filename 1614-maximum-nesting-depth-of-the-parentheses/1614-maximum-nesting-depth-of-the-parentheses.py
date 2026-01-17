class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxCount = 0
        for i in s:
            if i == "(":
                count +=1
                maxCount = max(maxCount, count)
            elif i == ")":
                count -=1
        return maxCount
        