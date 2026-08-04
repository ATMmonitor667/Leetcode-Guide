class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini = min(nums)
        maxi = max(nums)
        seen = set(nums)
        ans = []
        for i in range(mini, maxi+1):
            if i not in seen:
                ans.append(i)
        return ans 