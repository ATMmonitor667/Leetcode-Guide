class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def dfs(index = 0, targetSum = target):
            if(index == len(nums)):
                if(targetSum == 0):
                    return 1
                return 0
            if((index, targetSum) in memo):
                return memo[(index, targetSum)]
            else:
                memo[(index, targetSum)] = dfs(index+1, targetSum + nums[index])+dfs(index+1, targetSum - nums[index])
                return memo[(index, targetSum)]
        return dfs()
        