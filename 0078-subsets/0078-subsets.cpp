class Solution {
public:

void dfs(
        int index,
        vector<int>& nums,
        vector<int>& path,
        vector<vector<int>>& result
    ) {
        if (index == nums.size()) {
            result.push_back(path);
            return;
        }

        path.push_back(nums[index]);
        dfs(index + 1, nums, path, result);
        path.pop_back();
        dfs(index + 1, nums, path, result);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(0, nums, path, result);
        return result;
    }
};