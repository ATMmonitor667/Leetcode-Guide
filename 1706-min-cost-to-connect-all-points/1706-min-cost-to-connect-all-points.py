class Solution(object):
    class DSU:
        def __init__(self, n):
            self.parent = [i for i in range(n + 1)]
            self.rank = [0 for _ in range(n + 1)]

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            pa, pb = self.find(a), self.find(b)
            if pa == pb:
                return False
            if self.rank[pa] < self.rank[pb]:
                self.parent[pa] = pb
            elif self.rank[pa] > self.rank[pb]:
                self.parent[pb] = pa
            else:
                self.parent[pb] = pa
                self.rank[pa] += 1
            return True

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        edges.sort(key=lambda x: x[0])

        dsu = self.DSU(n - 1)
        cost = 0
        count = 0

        for dist, u, v in edges:
            if dsu.union(u, v):
                cost += dist
                count += 1
                if count == n - 1:
                    break

        return cost