class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax = 0
        currMax = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currMax +=1
                globalMax = max(globalMax, currMax)

            else:
                currMax = 0
        return globalMax

   
            
