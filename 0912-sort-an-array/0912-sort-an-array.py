class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        heapq.heapify(nums)
        ans = []
        while nums:
            value = heapq.heappop(nums)
            ans.append(value)
        return ans