class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [index, seen[complement]]
            seen[number] = index
        return [-1,-1]