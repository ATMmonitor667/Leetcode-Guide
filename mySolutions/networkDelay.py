from collections import defaultdict
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #build the graph
        graph = defaultdict(list)
        for [u,v,w] in times:
            graph[u].append((v,w))
        def Dikstras(src):
            distance = [float('inf')]*(n+1)
            distance[src] = 0
            queue = [(0,src)]
            while queue:
                cost, node = heapq.heappop(queue)
                if cost > distance[node]:
                    continue
                for ( nei, newWeight) in graph[node]:
                    newOne = cost + newWeight
                    if distance[nei] > newOne:
                        distance[nei] = newOne
                        heapq.heappush(queue, (newOne, nei))
            return distance
