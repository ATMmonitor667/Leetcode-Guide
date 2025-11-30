class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

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
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def idx(r, c):
            return r * cols + c   

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '1':
                                dsu.union(idx(r, c), idx(nr, nc))

        roots = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    roots.add(dsu.find(idx(r, c)))

        return len(roots)