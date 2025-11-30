class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        lookUp = set(nums)
        while original in lookUp:
            original = original * 2
        return original 
        