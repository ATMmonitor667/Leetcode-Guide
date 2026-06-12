from collections import defaultdict, Counter

class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Group nodes by their value
        value_to_nodes = defaultdict(list)
        for node, value in enumerate(vals):
            value_to_nodes[value].append(node)

        # Union-Find setup
        parent = list(range(n))
        size = [1] * n

        def find(x):
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            # Union by size
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

        ans = 0

        # Process values from small to large
        for value in sorted(value_to_nodes.keys()):
            nodes = value_to_nodes[value]

            # Phase 1: connect current-value nodes to all neighbors
            # whose value is <= current value
            for node in nodes:
                for nei in graph[node]:
                    if vals[nei] <= value:
                        union(node, nei)

            # Phase 2: count current-value nodes by component
            component_count = Counter()

            for node in nodes:
                root = find(node)
                component_count[root] += 1

            # If a component has k nodes with this value,
            # it contributes k * (k + 1) // 2 good paths
            for count in component_count.values():
                ans += count * (count + 1) // 2

        return ans


