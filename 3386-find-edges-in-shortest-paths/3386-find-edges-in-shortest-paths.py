class Solution(object):
    def findAnswer(self, n, edges):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstras(start):
            dist = {node: float('inf') for node in range(n)}
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, node = heapq.heappop(heap)
                if d > dist[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_d = d + weight
                    if new_d < dist[neighbor]:
                        dist[neighbor] = new_d
                        heapq.heappush(heap, (new_d, neighbor))
            return dist

        begin = dijkstras(0)
        end = dijkstras(n - 1)
        shortest_path = begin[n - 1]

        if shortest_path == float("inf"):
            return [False] * len(edges)

        ans = [False] * len(edges)

        for i, (u, v, w) in enumerate(edges):
            if begin[u] + w + end[v] == shortest_path or begin[v] + w + end[u] == shortest_path:
                ans[i] = True

        return ans