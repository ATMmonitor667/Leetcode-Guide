class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        hold = 0
        for i in range(len(nums)):
            if nums[i] == maxNum:
                hold = i
            else:
                if not (maxNum >= 2 * nums[i]) :
                    return -1
        return hold