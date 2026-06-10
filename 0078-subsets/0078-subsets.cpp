
vector<int> operator+(vector<int> lhs, int x)
{
    lhs.push_back(x);
    return lhs;
}

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;

        auto dfs = [&](auto&& dfs,
                       int index,
                       vector<int> path) -> void {

            if (index == nums.size()) {
                result.push_back(path);
                return;
            }

            dfs(dfs, index + 1, path + nums[index]);
            dfs(dfs, index + 1, path);
        };

        dfs(dfs, 0, vector<int>{});

        return result;
    }
};