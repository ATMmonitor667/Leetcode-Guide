class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        dir = [(1,0), (0,1), (-1, 0), (0,-1)]
        memo = {}
        MOD = int(1e9 + 7)
        def dfs(i,j):
            if (i, j) in memo:
                return memo[(i,j)]
            else:
                best = 1
                for (x,y) in dir:
                    dx,dy = i+x, j+y
                    if 0<= dx< m and 0<= dy< n and grid[dx][dy] > grid[i][j]:
                        best += dfs(dx,dy)
                memo[(i,j)] = best
                return best
        val = 0
        for i in range(m):
            for j in range(n):
                val = (val + dfs(i,j)) % MOD
        return val