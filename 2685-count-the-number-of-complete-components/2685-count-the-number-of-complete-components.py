from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]  # this is really size

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.rank[rootA] += self.rank[rootB]

        return True


class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)

        nodeCount = defaultdict(int)
        edgeCount = defaultdict(int)

        for node in range(n):
            root = dsu.find(node)
            nodeCount[root] += 1

        for u, v in edges:
            root = dsu.find(u)
            edgeCount[root] += 1

        ans = 0

        for root in nodeCount:
            nodes = nodeCount[root]
            edges_inside = edgeCount[root]

            if edges_inside == nodes * (nodes - 1) // 2:
                ans += 1

        return ans