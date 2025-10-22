class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols          = len(matrix), len(matrix[0])
        total               = rows * cols
        directions          = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        d                   = 0          # index into directions
        r = c               = 0          # current position
        visited             = set()
        res                 = []

        for _ in range(total):
            res.append(matrix[r][c])
            visited.add((r, c))

            # candidate next step
            nr, nc = r + directions[d][0], c + directions[d][1]

            # turn when we hit an edge or a visited cell
            if not (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                d = (d + 1) % 4          # rotate 90°
                nr, nc = r + directions[d][0], c + directions[d][1]

            r, c = nr, nc

        return res
            
        