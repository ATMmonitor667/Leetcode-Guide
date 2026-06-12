class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            temp = grid[r][c]
            grid[r][c] = 0  # mark visited

            best_next = max(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            )

            grid[r][c] = temp  # backtrack

            return temp + best_next

        max_gold = 0

        for i in range(m):
            for j in range(n):
                max_gold = max(max_gold, dfs(i, j))

        return max_gold

        