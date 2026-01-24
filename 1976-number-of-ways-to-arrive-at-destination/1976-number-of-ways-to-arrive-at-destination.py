class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7

        distance = [float('inf')] * n
        ways = [0] * n

        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        distance[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  

        while pq:
            cost, node = heapq.heappop(pq)

            if cost > distance[node]:
                continue

            for neigh, w in graph[node]:
                newDistance = cost + w

                if newDistance < distance[neigh]:
                    distance[neigh] = newDistance
                    ways[neigh] = ways[node]
                    heapq.heappush(pq, (newDistance, neigh))

                elif newDistance == distance[neigh]:
                    ways[neigh] = (ways[neigh] + ways[node]) % MOD

        return ways[n - 1] % MOD