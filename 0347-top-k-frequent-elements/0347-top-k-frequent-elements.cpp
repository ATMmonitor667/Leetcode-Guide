class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;

        for (int x : nums) {
            mp[x]++; 
        }

        vector<pair<int,int>> freq;
        freq.reserve(mp.size());
        for (auto &p : mp) {
            freq.push_back({p.first, p.second});
        }

        sort(freq.begin(), freq.end(),
             [](const auto& a, const auto& b) {
                 return a.second > b.second;
             });

        vector<int> result;
        result.reserve(k);
        for (int i = 0; i < k; i++) {
            result.push_back(freq[i].first);
        }

        return result;
    }
};
