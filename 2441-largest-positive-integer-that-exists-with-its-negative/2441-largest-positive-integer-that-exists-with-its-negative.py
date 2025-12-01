class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookUp = set(nums)
        maxNum = 0
        for i in nums:
            if i > maxNum and -1 * i in lookUp:
                maxNum = i 
        return maxNum if maxNum != 0 else -1
