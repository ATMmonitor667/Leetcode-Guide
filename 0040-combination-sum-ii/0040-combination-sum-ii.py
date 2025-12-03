class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(candidates)
        res = []

        def dfs(index, path, target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > target:
                    break
                dfs(i + 1, path + [nums[i]], target - nums[i])

        dfs(0, [], target)
        return res
