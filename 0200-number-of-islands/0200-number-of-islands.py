class Solution(object):
    def numIslands(self, grid):
        m = len(grid)-1
        n = len(grid[0])-1
        def dfs(r,c):
            if not(0 <= r<=m) or not(0<=c<=n) or grid[r][c] == '0':
                return 
            else:
                grid[r][c] = '0'
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count

            
     