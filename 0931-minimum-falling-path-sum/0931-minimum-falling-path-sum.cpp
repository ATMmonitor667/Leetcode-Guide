class Solution {
public:
   
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int j = 0; j < n; j++) dp[0][j] = matrix[0][j];
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int best = dp[i - 1][j];                
                if (j - 1 >= 0) best = min(best, dp[i - 1][j - 1]);   
                if (j + 1 < n) best = min(best, dp[i - 1][j + 1]);   

                dp[i][j] = matrix[i][j] + best;
            }
        }

        int ans = dp[m - 1][0];
        for (int j = 1; j < n; j++) ans = min(ans, dp[m - 1][j]);
        return ans;
    }
};