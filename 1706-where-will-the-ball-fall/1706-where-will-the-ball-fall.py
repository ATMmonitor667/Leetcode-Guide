class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        for loop thorugh all the indecies
        observation 1 is that if the adj cells are both the same sign you go to the next cell in the next rot, if the adjacent cells are opposite signs you stop and you die returning -1, if you make it to the last row you win and ans.append(col on the last row), couple of things is that there can be out of of bounds, if cell is 1 -> row+1, col+1, if the cell is -1, row+1, col-1
        if cell col and cell at col+1, 
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row == rows:
                return col

            direction = grid[row][col]
            next_col = col + direction

            if next_col < 0 or next_col >= cols:
                return -1


            if grid[row][next_col] != direction:
                return -1

            return dfs(row + 1, next_col)

        ans = []

        for starting_col in range(cols):
            ans.append(dfs(0, starting_col))

        return ans
            
        