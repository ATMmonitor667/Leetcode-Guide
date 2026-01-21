class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def khans_topo(edges, n):
            indegree = [0]*n
            graph = defaultdict(list)
            for u,v in edges:
                graph[u].append(v)
                indegree[v]+=1
            q = deque([i for i in range(len(indegree)) if indegree[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -=1
                    if indegree[nei] == 0:
                        q.append(nei)
            if len(order) == n:
                return order
            return []
        return len(khans_topo(prerequisites, numCourses)) == numCourses

            

            
        