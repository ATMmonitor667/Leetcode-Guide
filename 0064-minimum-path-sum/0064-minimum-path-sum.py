class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) - 1
        n = len(grid[0]) - 1
        memo = {}

        def dfs(r, c):
            if r > m or c > n:
                return float('inf')
            
            if r == m and c == n:
                return grid[m][n]
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            best = grid[r][c] + min(dfs(r+1, c), dfs(r, c+1))
            
            memo[(r, c)] = best
            return best
            
        return dfs(0, 0)

