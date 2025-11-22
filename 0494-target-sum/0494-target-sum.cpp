class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        unordered_map<string, int> memo;
        return dfs(0, 0, nums, target, memo);

       
    }
    int dfs(int index, int curr, vector<int>& nums, int target, unordered_map<string,int>& memo) {
        if (index == nums.size()) {
            return curr == target ? 1 : 0;
        }

        string key = to_string(index) + "," + to_string(curr);

        if (memo.count(key))
            return memo[key];

        int add = dfs(index + 1, curr + nums[index], nums, target, memo);
        int sub = dfs(index + 1, curr - nums[index], nums, target, memo);

        memo[key] = add + sub;
        return memo[key];
    }
     
};