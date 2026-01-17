class Solution(object):
    def twoSum(self, nums, target):
        myMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in myMap:
                return [myMap[complement], i]
            myMap[nums[i]] = i
        return -1


        