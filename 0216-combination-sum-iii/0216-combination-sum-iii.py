class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(start, target, path):
            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return
            
            if target < 0:
                return

            for i in range(start, 10):
                path.append(i)
                dfs(i + 1, target - i, path)
                path.pop()

        dfs(1, n, [])
        return res