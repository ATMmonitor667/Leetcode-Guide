from collections import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Apply diskstras shortest path when the path hits i == n-1 and j == m-1
        return max min length
        queue should have a i, j, weight where (i,j) are the indexes and weight is the weight at that index
        we will have Dikstras implemented and at every minimum cost pop we will record its distance
        and max it with itself and the currMax
        then return the current max"""
        m = len(grid)
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cost, r, c = heapq.heappop(pq)
            if (r, c) == (m - 1, n - 1):
                return cost
            if cost != dist[r][c]:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = max(cost, grid[nr][nc])
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))

        return -1  # unreachable