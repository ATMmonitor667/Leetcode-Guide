class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = set(nums)
        maxLength = 1
        visit = [False]*len(nums)
        if not nums:
            return 0
        if len(nums)==1:
            return 1

        for i in range(len(nums)):
            val = nums[i]
            length = 1
            if val+1 not in seen:
                continue
            while val+1 in seen:
                length+=1
                val = val+1
            maxLength = max(maxLength, length)
        return maxLength
      