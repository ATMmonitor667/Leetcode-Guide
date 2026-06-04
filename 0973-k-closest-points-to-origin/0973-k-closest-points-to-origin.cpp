class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), [](const auto& a, const auto& b) {
            int distA = a[0] * a[0] + a[1] * a[1];
            int distB = b[0] * b[0] + b[1] * b[1];

            return distA < distB;
        });

        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};