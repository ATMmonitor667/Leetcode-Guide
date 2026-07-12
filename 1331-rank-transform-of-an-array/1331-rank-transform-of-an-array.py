class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        diction = {}
        nums = sorted(arr)
        index = 0
        value = 1
        while index < len(nums):
            if nums[index] in diction:
                index+=1
            else:
                diction[nums[index]] = value
                index+=1
                value+=1
        print(arr, nums)
        ans = []
        for i in arr:
            ans.append(diction[i])
        return ans 
        