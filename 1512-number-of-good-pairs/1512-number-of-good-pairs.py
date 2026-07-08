class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        x = 0

        for index, num in enumerate(nums):
            if num in lookup:
                x += lookup[num]
            
            lookup[num] = lookup.get(num, 0) + 1

        return x