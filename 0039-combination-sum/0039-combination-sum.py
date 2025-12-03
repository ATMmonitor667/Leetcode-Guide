class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(index, path, targetSum):
            if targetSum == 0:
                res.append(path[:])
                return

            if targetSum < 0 or index == len(candidates):
                return

            dfs(index, path + [candidates[index]], targetSum - candidates[index])

            dfs(index + 1, path, targetSum)

        dfs(0, [], target)
        return res

      