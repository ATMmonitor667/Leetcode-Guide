class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;

        auto func = [&](auto&& func,
                         vector<vector<int>>& result,
                         vector<int>& nums,
                         int index,
                         vector<int> path) -> void {

            if (index == nums.size()) {
                result.push_back(path);
                return;
            }

            path.push_back(nums[index]);
            func(func, result, nums, index + 1, path);

            path.pop_back();
            func(func, result, nums, index + 1, path);
        };

        vector<int> path;
        func(func, result, nums, 0, path);

        return result;
    }
};