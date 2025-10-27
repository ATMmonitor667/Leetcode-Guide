class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

class Solution(object):

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        total = m * n
        edges = []
        dirs = [(1, 0), (0, 1)]  
        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        diff = abs(heights[r][c] - heights[nr][nc])
                        edges.append((diff, r * n + c, nr * n + nc))
        edges.sort(key=lambda x: x[0])
        dsu = DSU(total)
        for effort, a, b in edges:
            dsu.union(a, b)
            if dsu.find(0) == dsu.find(total - 1):
                return effort
        return 0
        