class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def dfs(index, target):
            if target == 0:
                return 1 
            if target < 0 or index > len(nums)-1 :
                return 0
            if (index, target) in memo:
                return memo[(index, target)]
            else:
                res = 0
                for i in range(0, len(nums)):
                    res += dfs(i, target - nums[i])
                memo[(index, target)] = res
                return res
        
        return dfs(0, target)