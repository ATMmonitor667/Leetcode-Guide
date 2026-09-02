class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def prune(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
            return grid
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return
            else:
                grid[r][c] = 0
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r, c-1)
                dfs(r, c+1)
        grid = prune(grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count +=1
                    dfs(i,j)
        return count 
        