class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        To solve this problem we need to implement dfs
        we should only be able to move left right up and down so we need a dirs
        array with all the directions, we then will need a visit array
        which if we see it in the visit array we will not visit it again
        The visit array is what is stopping the exponential explosion.

        Outside the DFS function we will simply use a forloop.
        """
        m = len(grid)-1
        n = len(grid[0])-1
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visit = set()
        def dfs(r,c):
            if r < 0 or r > m or c < 0 or c > n or grid[r][c] == "0" or (r,c) in visit:
                return
            visit.add((r,c))
            for x,y in directions:
                dfs(r+x, c+y)
        count = 0
        
        for i in range(m+1):
            for j in range(n+1):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    count += 1
        return count