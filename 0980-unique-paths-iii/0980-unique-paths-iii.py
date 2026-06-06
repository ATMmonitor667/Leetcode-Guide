class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        start_r, start_c = 0, 0
        remain = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] != -1:
                    remain += 1

                if grid[r][c] == 1:
                    start_r, start_c = r, c

        def dfs(r, c, remain):
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                grid[r][c] == -1
            ):
                return 0

            if grid[r][c] == 2:
                return 1 if remain == 1 else 0

            temp = grid[r][c]
            grid[r][c] = -1  
            paths = (
                dfs(r + 1, c, remain - 1) +
                dfs(r - 1, c, remain - 1) +
                dfs(r, c + 1, remain - 1) +
                dfs(r, c - 1, remain - 1)
            )
            grid[r][c] = temp 
            return paths

        return dfs(start_r, start_c, remain)