class Solution {
public:
    void dfs(
        vector<int>& candidates,
        int target,
        vector<vector<int>>& result,
        vector<int>& path,
        int current,
        int index
    ) {
        if (current == target) {
            result.push_back(path);
            return;
        }

        if (current > target || index >= candidates.size()) {
            return;
        }

        path.push_back(candidates[index]);
        dfs(candidates, target, result, path, current + candidates[index], index);
        path.pop_back();
        dfs(candidates, target, result, path, current, index + 1);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(candidates, target, result, path, 0, 0);
        return result;
    }
};