class Solution(object):
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True
            if not (0 <= r < m) or not (0 <= c < n):
                return False
            if board[r][c] == '' or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '' 

            res = (
                dfs(i + 1, r + 1, c) or
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r, c + 1) or
                dfs(i + 1, r, c - 1)
            )

            board[r][c] = temp  # restore original character
            return res

        for r in range(m):
            for c in range(n):
                if dfs(0, r, c):
                    return True

        return False