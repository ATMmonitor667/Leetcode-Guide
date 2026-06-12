class Solution(object):
    def longestIncreasingPath(self, matrix):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            m = len(matrix)
            n = len(matrix[0])
            memo = {}

            def dfs(r, c):
                if (r, c) in memo:
                    return memo[(r, c)]

                res = 1

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        matrix[nr][nc] > matrix[r][c]
                    ):
                        res = max(res, 1 + dfs(nr, nc))

                memo[(r, c)] = res
                return res
            ans = 0

            for r in range(m):
                for c in range(n):
                    ans = max(ans, dfs(r, c))

            return ans
                                    

        