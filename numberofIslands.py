class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        visit = set()
        def dfs(r,c):
            if  not ( (0 <= r < m) and (0<=c < n)) or (r,c) in visit or grid[r][c] == "0":
                return
            visit.add((r,c))
            for [x,y] in direction:
                dx = r+x
                dy = c+y
                dfs(dx,dy)

        count = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1" and (i,j) not in visit):
                    dfs(i,j)
                    count += 1
        return count
