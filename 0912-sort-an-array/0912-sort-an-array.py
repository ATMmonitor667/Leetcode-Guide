class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return heapq.nlargest(len(nums), nums)[::-1]
