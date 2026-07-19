class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        for (int num : nums) {
            freq[num]++;
        }

        vector<pair<int, int>> hold;

        for (auto &p : freq) {
            hold.push_back({p.second, p.first}); 
        }

        sort(hold.rbegin(), hold.rend());

        vector<int> ans;

        for (int i = 0; i < k; i++) {
            ans.push_back(hold[i].second);
        }

        return ans;
    }
};