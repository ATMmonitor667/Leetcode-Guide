class Solution {
public:
    vector<int> countBits(int n) {
        auto def = [](int nums) -> int {
            int count = 0;
            while (nums != 0) {
                int digit = nums % 2;
                if (digit == 1) count++;
                nums = nums / 2;
            }
            return count;
        };

        vector<int> ans;
        for (int i = 0; i <= n; i++) {
            ans.push_back(def(i));
        }
        return ans;
    }
};