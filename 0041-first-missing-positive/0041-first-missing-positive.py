class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = min(nums)
        maxi = max(nums)
        if mini > 1:
            return 1
        if maxi <= 0:
            return 1
        nums = set(nums)
        miniPositive = 1
        if miniPositive not in nums:
            return miniPositive
        flag = True
        while flag:
            if miniPositive + 1 in nums:
                miniPositive = miniPositive + 1
            if miniPositive + 1 not in nums:
                return miniPositive + 1