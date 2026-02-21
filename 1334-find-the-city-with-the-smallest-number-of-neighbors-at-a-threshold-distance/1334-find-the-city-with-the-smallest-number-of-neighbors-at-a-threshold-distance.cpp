class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {

        vector<vector<pair<int,int>>> graph(n);

        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        int minReachable = INT_MAX;
        int answer = -1;

        for (int i = 0; i < n; i++) {
            vector<int> dist(n, INT_MAX);
            dist[i] = 0;

            using T = pair<int,int>;
            priority_queue<T, vector<T>, greater<T>> pq;
            pq.push({0, i});

            while (!pq.empty()) {
                auto [cost, node] = pq.top();
                pq.pop();

                if (cost > dist[node]) continue;

                for (auto [neighbor, weight] : graph[node]) {
                    int newCost = cost + weight;
                    if (newCost < dist[neighbor]) {
                        dist[neighbor] = newCost;
                        pq.push({newCost, neighbor});
                    }
                }
            }

            int count = 0;
            for (int j = 0; j < n; j++) {
                if (j != i && dist[j] <= distanceThreshold)
                    count++;
            }

            // If tie, take larger index
            if (count <= minReachable) {
                minReachable = count;
                answer = i;
            }
        }

        return answer;
    }
};