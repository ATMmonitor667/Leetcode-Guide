
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        auto function = [](vector<int> &v, int target) -> vector<int>
            {
            unordered_map<int, int>mp;
            for(size_t i = 0; i < v.size(); i++)
            {
                int complement = target - v[i];
                if(mp.find(complement) != mp.end())
                {
                return {mp[complement], static_cast<int>(i)};
                }
                mp[v[i]] = i;
            }
            return {-1,-1};
            };
      return function(nums, target);
                    
    }
};