class Solution(object):

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        directions  = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = [(0, 0, 0)]
        rows = len(heights)
        cols = len(heights[0])
        end = (rows-1, cols-1)
        distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 0
        while queue:
            height, row, col = heapq.heappop(queue)
            if (row, col) == (rows - 1, cols - 1):
                return height
            if height > distance[row][col]:
                continue
            else:
                for x, y in directions:
                    nx = row + x
                    ny = col + y

                    if 0 <= nx < rows and 0 <= ny < cols:
                        edge_cost = abs(
                            heights[row][col] -
                            heights[nx][ny]
                        )

                        newHeight = max(height, edge_cost)

                        if newHeight < distance[nx][ny]:
                            distance[nx][ny] = newHeight
                            heapq.heappush(queue, (newHeight, nx, ny))
        return float('inf')


