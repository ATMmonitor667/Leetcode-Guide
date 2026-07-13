class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        a = -1
        b = -1
        hashMap = {}
        n = len(grid)
        for i in range(1, n*n+1):
            hashMap[i] = 0
        for i in range(n):
            for j in range(n):
                hashMap[grid[i][j]] = hashMap.get(grid[i][j], 0) +1
        for key, value in hashMap.items():
            if value == 0:
                b = key
            elif value == 2:
                a = key
        return [a,b]
