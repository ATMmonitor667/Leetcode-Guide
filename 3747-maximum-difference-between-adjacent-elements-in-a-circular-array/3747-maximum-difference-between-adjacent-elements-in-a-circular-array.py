class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        return max(abs(nums[0] - nums[len(nums)-1]), max([abs(nums[i-1]-nums[i]) for i in range(len(nums))]))
    