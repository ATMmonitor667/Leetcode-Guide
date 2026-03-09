class Solution {
public:
 bool topologicalSort(int numCourses, vector<vector<int>>& graph, vector<int>& indegree, queue<int>& prior) {
        int coursesProcessed = 0;
        
        while (!prior.empty()) {
            int currentCourse = prior.front();
            prior.pop();
            coursesProcessed++;
            
            // Process all courses that depend on the current course
            for (int nextCourse : graph[currentCourse]) {
                indegree[nextCourse]--; // Remove the dependency
                
                // If all prerequisites are met, add to queue
                if (indegree[nextCourse] == 0) {
                    prior.push(nextCourse);
                }
            }
        }
        
        // If we processed all courses, there are no cycles
        return coursesProcessed == numCourses;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // 1. Initialize graph and indegree array
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // 2. Build the adjacency list and count incoming edges
        for (const auto& req : prerequisites) {
            int course = req[0];
            int prereq = req[1];
            
            graph[prereq].push_back(course); // Directed edge: prereq -> course
            indegree[course]++;
        }
        
        // 3. Find all courses with 0 prerequisites to start the BFS
        queue<int> prior;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                prior.push(i);
            }
        }
        
        // 4. Run the Topological Sort
        return topologicalSort(numCourses, graph, indegree, prior);
    }
};