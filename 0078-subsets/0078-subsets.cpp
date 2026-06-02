class Solution {
public:
    void dfs(
        vector<int>& nums,
        int index, 
        vector<int>& path,
        vector<vector<int>>&result
    )
    {
        if(index == nums.size())
        {
            result.push_back(path);
            return;
        }
        else{
            path.push_back(nums[index]);
            dfs(nums, index+1, path, result);
            path.pop_back();
            dfs(nums, index+1, path, result);
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int>path;
        dfs(nums, 0, path, result);
        return result;
    }
};