class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        memo = {}

        def dfs(r, c1, c2):

            # out of bounds
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return float('-inf')

            # last row
            if r == rows - 1:
                if c1 == c2:
                    return grid[r][c1]
                return grid[r][c1] + grid[r][c2]

            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]

            cherries = 0

            if c1 == c2:
                cherries = grid[r][c1]
            else:
                cherries = grid[r][c1] + grid[r][c2]

            best = float('-inf')

            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:

                    best = max(
                        best,
                        dfs(r + 1, c1 + dc1, c2 + dc2)
                    )

            memo[(r, c1, c2)] = cherries + best
            return memo[(r, c1, c2)]

        return dfs(0, 0, cols - 1)