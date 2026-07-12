class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return [-1* j for j in heapq.nlargest(len(nums), [-1*i for i in nums])]
