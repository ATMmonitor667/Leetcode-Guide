class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, target, i):
            if target == 0:
                res.append(path[:])
                return 
            if target < 0 or i >= len(candidates):
                return 
            else:
                dfs(path + [candidates[i]], target - candidates[i], i)
                dfs(path , target , i+1)
        dfs([], target, 0)
        return res
        

