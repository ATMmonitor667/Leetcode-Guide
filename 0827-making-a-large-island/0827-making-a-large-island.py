class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if A == B:
            return False
        if self.size[A] < self.size[B]:
            A, B = B, A
        self.parent[B] = A
        self.size[A] += self.size[B]
        return True


class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        val = n * n
        dsu = DSU(val)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def idx(x, y):
            return x * n + y

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            dsu.union(idx(i, j), idx(ni, nj))

        max_sz = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    root = dsu.find(idx(i, j))
                    max_sz = max(max_sz, dsu.size[root])

        if max_sz == n * n:
            return max_sz

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    sz = 1
                    root_set = set()
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            root = dsu.find(idx(ni, nj))
                            if root not in root_set:
                                sz += dsu.size[root]
                                root_set.add(root)
                    max_sz = max(max_sz, sz)

        return max_sz