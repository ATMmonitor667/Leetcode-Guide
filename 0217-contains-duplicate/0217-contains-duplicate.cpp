class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        auto find = [](vector<int>& nums)->bool{
        unordered_map<int,int>mp;
        for(auto num : nums)
        {
            if(mp.find(num) != mp.end())
            {
            return true;
            }
            mp[num]++;
        }
        return false;
        };
        return find(nums);
        
    }
};