class Solution(object):
    def longestConsecutive(self, nums):
        seen = set(nums)
        globalCount = 0
        for i in nums:
            count = 1
            key = i
            if key+1 not in seen:
                while key-1 in seen:
                    key = key -1
                    count +=1
            globalCount = max(globalCount, count)
        return globalCount 

 