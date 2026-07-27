class Solution {
public:
    void dfs(
        int index,
        vector<int> path,
        vector<vector<int>>& result,
        vector<int>& nums
    )
    {
        if (index == nums.size())
        {
            result.push_back(path);
            return;
        }

        path.push_back(nums[index]);
        dfs(index + 1, path, result, nums);

        path.pop_back();
        dfs(index + 1, path, result, nums);
    }

    vector<vector<int>> subsets(vector<int>& nums)
    {
        vector<vector<int>> result;
        dfs(0, {}, result, nums);
        return result;
    }
};