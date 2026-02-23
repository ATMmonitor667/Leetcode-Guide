class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int odd{0};
        int even{0};
        unordered_map<int, int> mp;
        for(auto i : position)
        {
            if(mp.contains(i))
            {
                mp[i]++;
            }
            else{
                mp[i] = 1;
            }
        }
        for(auto[num, count] : mp)
        {
            if(num%2 == 0)
            {
                even+=count;
            }
            else{
                odd+=count;
            }
        }
        return min(odd, even);
    }
};