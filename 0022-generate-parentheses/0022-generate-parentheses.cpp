class Solution {
public:
    vector<string> generateParenthesis(int n){
        vector<string> res;

        auto check = [](const string &valid) {
            int count = 0;
            for (char c : valid) {
                if (c == ')') {
                    if (count == 0)
                        return false;
                    count--;
                } else {
                    count++;
                }
            }
            return count == 0;
        };


        function<void(string, int)> dfs = [&](string path, int index) {
            if (path.size() == 2 * n) {
                if (check(path)) res.push_back(path);
                return;
            }
            dfs(path + "(", index + 1);
            dfs(path + ")", index + 1);
        };

        dfs("", 0);
        return res;
    }
};