class Solution {
public:
    void dfs(vector<int>& candidates, int index, int target,
             vector<int>& path, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(path);
            return;
        }
        if (index >= candidates.size() || target < 0) {
            return;
        }

        // include current candidate (stay on same index for reuse)
        path.push_back(candidates[index]);
        dfs(candidates, index, target - candidates[index], path, result);
        path.pop_back();

        // exclude current candidate (move to next index)
        dfs(candidates, index + 1, target, path, result);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(candidates, 0, target, path, res);
        return res;
    }
};