class Solution {
public:
    void dfs(
        int index,
        vector<int>& nums,
        vector<int>& path,
        vector<vector<int>>& result,
        int remaining
    ) {
        if (remaining == 0) {
            result.push_back(path);
            return;
        }

        if (index == nums.size() || remaining < 0) {
            return;
        }

        path.push_back(nums[index]);
        dfs(index, nums, path, result, remaining - nums[index]);
        path.pop_back();
        dfs(index + 1, nums, path, result, remaining);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> path;

        dfs(0, candidates, path, result, target);

        return result;
    }
};