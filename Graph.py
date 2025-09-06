
from typing import List, Tuple
import heapq
from collections import deque

INF = 10**18

class Solution:
    """
    ============================================================================
    GRAPH ALGORITHMS COMPREHENSIVE GUIDE
    ============================================================================
    This class contains implementations of fundamental graph algorithms used in
    competitive programming and technical interviews. Each algorithm is optimized
    for different scenarios and graph properties.
    """
    
    # ========================================================================
    # 1) DIJKSTRA'S ALGORITHM - Single Source Shortest Path
    # ========================================================================
    """
    CONCEPT & IDEA:
    Dijkstra's algorithm finds the shortest path from a source vertex to all other 
    vertices in a weighted graph with NON-NEGATIVE edge weights.
    
    KEY INSIGHT: 
    - Uses a greedy approach: always process the unvisited vertex with minimum distance
    - Guarantees optimality because once a vertex is processed, we've found its shortest path
    - This works ONLY with non-negative weights (negative weights break the greedy property)
    
    ALGORITHM STEPS:
    1. Initialize distances: source = 0, all others = infinity
    2. Use a min-heap (priority queue) to always get the vertex with minimum distance
    3. For each vertex u, relax all its neighbors v: if dist[u] + weight(u,v) < dist[v], update dist[v]
    4. Mark u as processed (never revisit)
    5. Repeat until all vertices are processed
    
    TIME COMPLEXITY: O((V + E) log V) with binary heap
    SPACE COMPLEXITY: O(V + E)
    
    WHEN TO USE:
    - Single source shortest path with non-negative weights
    - GPS navigation systems, network routing protocols
    - Any problem requiring "minimum cost" from one point to all others
    """
    def dijkstra(self, n: int, edges: List[Tuple[int,int,int]], src: int) -> List[int]:
        # Build adjacency list representation of the graph
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v, w))
        
        # Initialize distances: source = 0, all others = infinity
        dist = [INF]*n
        dist[src] = 0
        
        # Min-heap: (distance, vertex) - Python's heapq is a min-heap
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            # Skip stale entries (we might have updated this vertex's distance already)
            if d != dist[u]:
                continue
            
            # Relax all neighbors of vertex u
            for v, w in g[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        
        return dist

    # ========================================================================
    # 2) 0-1 BFS - Shortest Path with Binary Weights
    # ========================================================================
    """
    CONCEPT & IDEA:
    0-1 BFS is a specialized shortest path algorithm for graphs where edge weights
    are ONLY 0 or 1. It's faster than Dijkstra for this specific case.
    
    KEY INSIGHT:
    - Uses a deque (double-ended queue) instead of a priority queue
    - When relaxing an edge with weight 0: add to FRONT of deque (higher priority)
    - When relaxing an edge with weight 1: add to BACK of deque (lower priority)
    - This maintains the property that distances are processed in non-decreasing order
    
    WHY IT WORKS:
    - With only weights 0 and 1, the distance can only increase by 0 or 1
    - By using deque strategically, we process vertices in order of their distances
    - No need for expensive heap operations
    
    TIME COMPLEXITY: O(V + E) - much faster than Dijkstra's O((V+E) log V)
    SPACE COMPLEXITY: O(V + E)
    
    WHEN TO USE:
    - Grid problems where you can move with cost 0 or 1
    - Maze problems with special moves
    - Any shortest path problem with only binary weights
    """
    def zero_one_bfs(self, n: int, edges: List[Tuple[int,int,int]], src: int) -> List[int]:
        # Build adjacency list (edges must have weights 0 or 1)
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            # assert w in {0,1}  # Uncomment to enforce binary weights
            g[u].append((v, w))
        
        # Initialize distances
        dist = [INF]*n
        dist[src] = 0
        
        # Use deque for 0-1 BFS optimization
        dq = deque([src])
        
        while dq:
            u = dq.popleft()
            
            # Process all neighbors of current vertex
            for v, w in g[u]:
                new_dist = dist[u] + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    
                    # KEY OPTIMIZATION: 
                    # Weight 0: add to front (process immediately)
                    # Weight 1: add to back (process later)
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        
        return dist
    def zero_one_bfs(self, n: int, edges: List[Tuple[int,int,int]], src: int) -> List[int]:
        # Build adjacency list (edges must have weights 0 or 1)
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            # assert w in {0,1}  # Uncomment to enforce binary weights
            g[u].append((v, w))
        
        # Initialize distances
        dist = [INF]*n
        dist[src] = 0
        
        # Use deque for 0-1 BFS optimization
        dq = deque([src])
        
        while dq:
            u = dq.popleft()
            
            # Process all neighbors of current vertex
            for v, w in g[u]:
                new_dist = dist[u] + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    
                    # KEY OPTIMIZATION: 
                    # Weight 0: add to front (process immediately)
                    # Weight 1: add to back (process later)
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        
        return dist

    # ========================================================================
    # 3) FLOYD-WARSHALL ALGORITHM - All Pairs Shortest Path
    # ========================================================================
    """
    CONCEPT & IDEA:
    Floyd-Warshall finds the shortest path between ALL pairs of vertices in a 
    weighted directed graph. It can handle negative edge weights but detects 
    negative cycles.
    
    KEY INSIGHT:
    - Dynamic Programming approach: dp[i][j][k] = shortest path from i to j using vertices {0,1,...,k}
    - Space optimized: we only need 2D array since we process k in order
    - For each intermediate vertex k, check if path i→k→j is shorter than direct i→j
    
    ALGORITHM STEPS:
    1. Initialize: dist[i][j] = weight of edge i→j (or INF if no edge)
    2. For each possible intermediate vertex k (from 0 to n-1):
       For each pair (i,j): dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    3. After n iterations, dist[i][j] contains shortest path from i to j
    
    TIME COMPLEXITY: O(V³) - always, regardless of edge count
    SPACE COMPLEXITY: O(V²)
    
    WHEN TO USE:
    - Need shortest paths between ALL pairs of vertices
    - Graph is dense (many edges) - more efficient than running Dijkstra V times
    - Need to detect negative cycles
    - Small to medium sized graphs (V ≤ 400-500)
    """
    def floyd_warshall(self, n: int, edges: List[Tuple[int,int,int]]) -> List[List[int]]:
        # Initialize distance matrix
        dist = [[INF]*n for _ in range(n)]
        
        # Distance from vertex to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Set initial edge weights
        for u,v,w in edges:
            if w < dist[u][v]:  # Handle multiple edges, keep minimum
                dist[u][v] = w
        
        # Main Floyd-Warshall algorithm
        # Try each vertex k as an intermediate vertex
        for k in range(n):
            dk = dist[k]  # Optimization: cache dist[k] row
            for i in range(n):
                dik = dist[i][k]
                if dik == INF:  # No path from i to k, skip
                    continue
                di = dist[i]  # Optimization: cache dist[i] row
                for j in range(n):
                    # Check if path i→k→j is shorter than direct i→j
                    path_through_k = dik + dk[j]
                    if path_through_k < di[j]:
                        di[j] = path_through_k
        
        # Optional: Detect negative cycles
        # If dist[i][i] < 0 for any i, there's a negative cycle
        # has_neg_cycle = any(dist[i][i] < 0 for i in range(n))
        
        return dist
    def floyd_warshall(self, n: int, edges: List[Tuple[int,int,int]]) -> List[List[int]]:
        # Initialize distance matrix
        dist = [[INF]*n for _ in range(n)]
        
        # Distance from vertex to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Set initial edge weights
        for u,v,w in edges:
            if w < dist[u][v]:  # Handle multiple edges, keep minimum
                dist[u][v] = w
        
        # Main Floyd-Warshall algorithm
        # Try each vertex k as an intermediate vertex
        for k in range(n):
            dk = dist[k]  # Optimization: cache dist[k] row
            for i in range(n):
                dik = dist[i][k]
                if dik == INF:  # No path from i to k, skip
                    continue
                di = dist[i]  # Optimization: cache dist[i] row
                for j in range(n):
                    # Check if path i→k→j is shorter than direct i→j
                    path_through_k = dik + dk[j]
                    if path_through_k < di[j]:
                        di[j] = path_through_k
        
        # Optional: Detect negative cycles
        # If dist[i][i] < 0 for any i, there's a negative cycle
        # has_neg_cycle = any(dist[i][i] < 0 for i in range(n))
        
        return dist

    # ========================================================================
    # 4) BELLMAN-FORD ALGORITHM - Single Source with Negative Edges
    # ========================================================================
    """
    CONCEPT & IDEA:
    Bellman-Ford finds shortest paths from a source vertex to all other vertices
    in a weighted graph that may contain NEGATIVE edge weights. It also detects
    negative cycles reachable from the source.
    
    KEY INSIGHT:
    - Relaxes ALL edges repeatedly (unlike Dijkstra's greedy approach)
    - After (V-1) iterations, shortest paths are found if no negative cycles exist
    - If we can still relax edges in the V-th iteration, there's a negative cycle
    
    WHY (V-1) ITERATIONS?
    - Shortest path can have at most (V-1) edges (no repeated vertices)
    - Each iteration guarantees finding shortest paths with one more edge
    - After (V-1) iterations, all shortest paths are discovered
    
    ALGORITHM STEPS:
    1. Initialize: dist[source] = 0, all others = infinity
    2. Repeat (V-1) times: for each edge (u,v,w), try to relax: dist[v] = min(dist[v], dist[u] + w)
    3. Check for negative cycles: if any edge can still be relaxed, negative cycle exists
    
    TIME COMPLEXITY: O(VE) - slower than Dijkstra but handles negative edges
    SPACE COMPLEXITY: O(V)
    
    WHEN TO USE:
    - Graph has negative edge weights
    - Need to detect negative cycles
    - Currency arbitrage problems
    - Some dynamic programming problems on graphs
    """
    def bellman_ford(self, n: int, edges: List[Tuple[int,int,int]], src: int) -> Tuple[List[int], bool]:
        """
        Returns (distances, has_negative_cycle)
        has_negative_cycle=True means there's a negative cycle reachable from source
        """
        # Initialize distances: source = 0, all others = infinity
        dist = [INF]*n
        dist[src] = 0
        
        # Relax all edges (V-1) times
        for iteration in range(n-1):
            updated = False
            
            # Try to relax every edge
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            
            # Early termination: if no updates in this iteration, we're done
            if not updated:
                break
        
        # Check for negative cycles (V-th iteration)
        # If we can still relax any edge, there's a negative cycle
        has_negative_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_negative_cycle = True
                break
        
        return dist, has_negative_cycle
    def bellman_ford(self, n: int, edges: List[Tuple[int,int,int]], src: int) -> Tuple[List[int], bool]:
        """
        Returns (distances, has_negative_cycle)
        has_negative_cycle=True means there's a negative cycle reachable from source
        """
        # Initialize distances: source = 0, all others = infinity
        dist = [INF]*n
        dist[src] = 0
        
        # Relax all edges (V-1) times
        for iteration in range(n-1):
            updated = False
            
            # Try to relax every edge
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            
            # Early termination: if no updates in this iteration, we're done
            if not updated:
                break
        
        # Check for negative cycles (V-th iteration)
        # If we can still relax any edge, there's a negative cycle
        has_negative_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_negative_cycle = True
                break
        
        return dist, has_negative_cycle

    # ========================================================================
    # ALGORITHM COMPARISON & SELECTION GUIDE
    # ========================================================================
    """
    WHEN TO USE EACH ALGORITHM:
    
    1. DIJKSTRA'S ALGORITHM:
       ✅ Single source shortest path
       ✅ Non-negative edge weights ONLY
       ✅ Sparse graphs (E << V²)
       ✅ Need optimal performance for single source
       ❌ Cannot handle negative edges
    
    2. 0-1 BFS:
       ✅ Edge weights are only 0 or 1
       ✅ Faster than Dijkstra for binary weights
       ✅ Grid/maze problems with special moves
       ❌ Only works with binary weights
    
    3. FLOYD-WARSHALL:
       ✅ All pairs shortest path
       ✅ Can handle negative edges
       ✅ Dense graphs or small graphs
       ✅ Need to detect negative cycles
       ❌ O(V³) always - expensive for large graphs
    
    4. BELLMAN-FORD:
       ✅ Single source with negative edges
       ✅ Detects negative cycles
       ✅ Currency arbitrage, some DP problems
       ❌ Slower than Dijkstra: O(VE) vs O((V+E)log V)
    
    COMPLEXITY SUMMARY:
    - Dijkstra: O((V+E) log V) time, O(V+E) space
    - 0-1 BFS: O(V+E) time, O(V+E) space  
    - Floyd-Warshall: O(V³) time, O(V²) space
    - Bellman-Ford: O(VE) time, O(V) space
    """