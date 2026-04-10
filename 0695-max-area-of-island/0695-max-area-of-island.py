class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        
        # Use the actual length
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r, c):
            # Standard boundary and condition check
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            
            # Accumulate the area from all 4 directions
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        # Loop through the entire grid
        for i in range(rows):
            for j in range(cols):
                # Start DFS if we find unvisited land
                if grid[i][j] == 1 and (i, j) not in visit:
                    max_area = max(max_area, dfs(i, j))
                    
        return max_area