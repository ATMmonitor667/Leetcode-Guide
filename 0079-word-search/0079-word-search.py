class Solution(object):
    def exist(self, board, word):
        seen = set()

        def dfs(idx, r, c):
            if idx == len(word):
                return True

            if (
                r < 0 or r >= len(board) or
                c < 0 or c >= len(board[0]) or
                (r, c) in seen or
                board[r][c] != word[idx]
            ):
                return False

            seen.add((r, c))

            res = (
                dfs(idx + 1, r + 1, c) or
                dfs(idx + 1, r - 1, c) or
                dfs(idx + 1, r, c + 1) or
                dfs(idx + 1, r, c - 1)
            )

            seen.remove((r, c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True

        return False