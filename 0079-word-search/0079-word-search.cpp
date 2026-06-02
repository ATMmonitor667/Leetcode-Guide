class Solution {
public:
    bool dfs(
        int index,
        vector<vector<char>>& board,
        string& word,
        int row,
        int col
    ) {
        if (index == word.size()) {
            return true;
        }

        if (
            row < 0 || col < 0 ||
            row >= board.size() || col >= board[0].size() ||
            board[row][col] != word[index]
        ) {
            return false;
        }

        char temp = board[row][col];
        board[row][col] = '&';

        bool result =
            dfs(index + 1, board, word, row, col + 1) ||
            dfs(index + 1, board, word, row + 1, col) ||
            dfs(index + 1, board, word, row - 1, col) ||
            dfs(index + 1, board, word, row, col - 1);

        board[row][col] = temp;

        return result;
    }

    bool exist(vector<vector<char>>& board, string word) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                if (dfs(0, board, word, i, j)) {
                    return true;
                }
            }
        }

        return false;
    }
};