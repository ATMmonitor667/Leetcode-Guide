class Solution(object):
    def twoSum(self, nums, target):
        mymap = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in mymap:
                return [mymap[complement], i]
            mymap[val] = i
        return [-1]

        