import heapq

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])

        distance = [
            [[float("inf")] * (k + 1) for _ in range(C)]
            for _ in range(R)
        ]

        distance[0][0][0] = 0

        pq = [(0, 0, 0, 0)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]

        while pq:
            cost, r, c, used = heapq.heappop(pq)

            if cost > distance[r][c][used]:
                continue

            if r == R - 1 and c == C - 1:
                return cost

            for x, y in directions:
                dx = r + x
                dy = c + y

                if 0 <= dx < R and 0 <= dy < C:
                    new_used = used + grid[dx][dy]

                    if new_used > k:
                        continue

                    new_cost = cost + 1

                    if new_cost < distance[dx][dy][new_used]:
                        distance[dx][dy][new_used] = new_cost

                        heapq.heappush(
                            pq,
                            (new_cost, dx, dy, new_used)
                        )

        return -1

        