#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <chrono>
#include <cmath>
#include <complex>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <optional>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

using ll       = long long;
using ull      = unsigned long long;
using pii      = pair<int,int>;
template<class T> using min_heap =
    priority_queue<T, vector<T>, greater<T>>;   // generic min-heap
using veci = vector<int>;
using vecll =  vector<long long>;
template<class K, class V>
using umap = unordered_map<K, V>;
using MinPQ    = min_heap<int>;                 // int min-heap
using MaxPQ    = priority_queue<int>;           // int max-heap
using MinPQll  = min_heap<long long>;           // ll min-heap


class Solution {
public:
    vector<int> topologicalSort(int numCourses, vector<vector<int>>& graph, vector<int>& indegree, queue<int>& prior) {
        vector<int> order;
        while(!prior.empty())
        {
            int current = prior.front();
            prior.pop();
            order.push_back(current);
            for(int state : graph[current])
            {
                indegree[state]--;
                if(indegree[state] == 0)
                {
                    prior.push(state);
                }
            }
        }
        if(order.size() == numCourses)
        {
            return order;
        }
        return {};
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites)    
    {
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        for (const auto& req : prerequisites) {
            int course = req[0];
            int prereq = req[1];
            graph[prereq].push_back(course); 
            indegree[course]++;
        }
        queue<int> prior;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                prior.push(i);
            }
        }
        return topologicalSort(numCourses, graph, indegree, prior);
       
    }
};