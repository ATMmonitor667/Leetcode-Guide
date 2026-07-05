class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        memo = {}

        def best(r, c):
            if r < 0 or c < 0 or r >= n or c >= n:
                return float("-inf")

            if board[r][c] == "X":
                return float("-inf")

            if (r, c) == (0, 0):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            val = 0
            if board[r][c].isdigit():
                val = int(board[r][c])

            res = val + max(
                best(r - 1, c),
                best(r, c - 1),
                best(r - 1, c - 1)
            )

            memo[(r, c)] = res
            return res

        maxScore = best(n - 1, n - 1)

        if maxScore < 0:
            return [0, 0]

        memo2 = {}

        def count(r, c):
            if r < 0 or c < 0 or r >= n or c >= n:
                return 0

            if board[r][c] == "X":
                return 0

            if (r, c) == (0, 0):
                return 1

            if (r, c) in memo2:
                return memo2[(r, c)]

            val = 0
            if board[r][c].isdigit():
                val = int(board[r][c])

            ways = 0

            for nr, nc in [
                (r - 1, c),
                (r, c - 1),
                (r - 1, c - 1)
            ]:
                if best(nr, nc) + val == best(r, c):
                    ways += count(nr, nc)

            memo2[(r, c)] = ways % MOD
            return memo2[(r, c)]

        return [maxScore, count(n - 1, n - 1)]

     
        