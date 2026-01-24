class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # first we build the graph 
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        total = 0
        while q:
            u = q.popleft()
            total += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return total == numCourses





            

            
        