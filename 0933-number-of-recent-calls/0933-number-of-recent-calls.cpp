class RecentCounter {
private:
    vector<int> hold;

public:
    RecentCounter() {}

    int ping(int t) {
        hold.push_back(t);

        int count = 0;
        for (int i : hold) {
            if (i >= t - 3000 && i <= t) {
                count++;
            }
        }

        return count;
    }
};
/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */