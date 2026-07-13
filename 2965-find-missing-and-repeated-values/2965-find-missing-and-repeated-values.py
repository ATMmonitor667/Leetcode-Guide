class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        a = -1
        b = -1
        seen = set()
        n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in seen:
                    a = grid[i][j]
                seen.add(grid[i][j])
        for i in range(1, n*n+1):
            if i not in seen:
                b = i
        return [a,b]