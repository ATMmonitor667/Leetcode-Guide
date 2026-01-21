class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        Khans algorithm:
        have an array of Indegrees
        construct a graph
        have a queue
        all the nodes in the queue which have 0 indegree add to the queue
        run while loop
        pop a node
        subtract 1 from all its neigbors
        if indegree 0 add to topological seqeunce
        else do nothing

        """
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for [u,v] in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        order = []
       
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
