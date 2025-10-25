class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        this is harder queue and is slightly different because we are either going completely down
        or completely to the right no in between. In every intmdiate call we see set the in value at that spot from an "X" to an "." and then continue to repeat this. make sure all the values in the grid are "." by the end of it
        """
        if not board:
            return 0
        
        output =0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    q = deque([(i, j)])
                    board[i][j]='#'
                    while q:
                        r, c = q.popleft()
                        for x, y in directions:
                            nr = r + x
                            nc = c + y
                            if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]) and board[nr][nc]=='X':
                                q.append((nr, nc))
                                board[nr][nc] = '#'

                    output +=1
        return output
            

        