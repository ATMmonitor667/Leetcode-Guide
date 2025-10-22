class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min = float('inf')
        max = float('-inf')
        for x in nums:
            if x < min: 
                min = x
            if x > max: 
                max = x

        
        #sormadexin = (nums, k) 

        val = max - min
        return val * k