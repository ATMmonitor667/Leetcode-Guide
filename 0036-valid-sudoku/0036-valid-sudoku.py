class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        grid = []

        # Convert strings into integers, using 0 for empty cells
        for rows in range(len(board)):
            intermediate = []

            for cols in range(len(board[0])):
                if board[rows][cols] == '.':
                    intermediate.append(0)
                else:
                    intermediate.append(int(board[rows][cols]))

            grid.append(intermediate)

        # Check every row and column
        for i in range(len(grid)):
            rowSet = set()
            colSet = set()

            for j in range(len(grid)):
                rowValue = grid[i][j]
                colValue = grid[j][i]

                if rowValue != 0:
                    if rowValue in rowSet:
                        return False

                    rowSet.add(rowValue)

                if colValue != 0:
                    if colValue in colSet:
                        return False

                    colSet.add(colValue)

        # Check every 3 x 3 sub-box
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                boxSet = set()

                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        value = grid[row][col]

                        if value == 0:
                            continue

                        if value in boxSet:
                            return False

                        boxSet.add(value)

        return True