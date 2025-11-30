class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        at every index we either add it to the path or skip it
        at the end when we reach lenght of k we return the value stored
        """
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  
        vals.sort(key=lambda x: -x[1])
        vals = sorted(vals[:k])
        res = [val for idx, val in vals] 
        return res
