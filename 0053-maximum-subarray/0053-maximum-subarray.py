class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [-2,1]
        [1]
        0
        return max(arr)
        if everything pos:
            sum(arr)
        negatives or positives:
          if ever total < -1, 0:
            anchored down, set = 0
          -1
          set = 0 
          positive
           += values 
           max(max, currRunningSum)
        """
        maxSum = 0
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum < 0:
                currSum = 0
            maxSum = max(currSum, maxSum)
        if maxSum == 0:
            return max(nums)
        return maxSum

        