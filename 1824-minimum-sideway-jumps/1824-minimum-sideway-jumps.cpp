class Solution {
private:
    vector<array<int, 4>> memo;
    vector<int>* obstacles;
    int n;

    int dfs(int index, int lane) {
        if (index == n - 1) {
            return 0;
        }

        int& answer = memo[index][lane];

        if (answer != -1) {
            return answer;
        }

        if ((*obstacles)[index + 1] != lane) {
            return answer = dfs(index + 1, lane);
        }

        int best = INT_MAX;

        for (int newLane = 1; newLane <= 3; ++newLane) {
            if (newLane == lane) {
                continue;
            }

            if ((*obstacles)[index] == newLane) {
                continue;
            }

            best = min(best, 1 + dfs(index, newLane));
        }

        return answer = best;
    }

public:
    int minSideJumps(vector<int>& obs) {
        obstacles = &obs;
        n = obs.size();
        memo.assign(n, array<int, 4>{-1, -1, -1, -1});

        return dfs(0, 2);
    }
};