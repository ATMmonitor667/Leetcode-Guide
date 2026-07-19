class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> seen;
        for(auto i: nums)
        {
            if(seen.find(i) != seen.end())
            {
                return true;
            }
            else{
                seen.insert(i);
            }
        }
        return false;
    }
};