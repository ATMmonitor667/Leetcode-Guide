class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        // set a count 
        for loop 
        a certain condition
        while condition holds count +=1
        when condition breaks restart 

        """
        if k <= 1:
            return 0
        
        product = 1
        count = 0
        l = 0
        
        for r in range(len(nums)):
            product *= nums[r]
            
            # shrink window while product >= k
            while product >= k:
                product //= nums[l]
                l += 1
            
            # all subarrays ending at r and starting from [l..r] are valid
            count += (r - l + 1)
        
        return count

        