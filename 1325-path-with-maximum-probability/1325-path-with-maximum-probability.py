class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], succProb[i]])
            graph[edges[i][1]].append([edges[i][0], succProb[i]])
        def Dijkstra(src):
            distance = [0.0] * n
            distance[src] = 1.0
            pq = [(-1.0, src)]  
            while pq:
                prob, node = heapq.heappop(pq)
                prob = -prob  
                if prob < distance[node]:
                    continue

                for nei, weight in graph[node]:
                    new_prob = prob * weight
                    if new_prob > distance[nei]:
                        distance[nei] = new_prob
                        heapq.heappush(pq, (-new_prob, nei))

            return distance

        distance = Dijkstra(start_node)
        return distance[end_node]


        