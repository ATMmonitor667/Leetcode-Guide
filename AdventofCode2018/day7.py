from collections import defaultdict
import heapq

def dataloader(filename):
    graph = defaultdict(list)
    indegree = {}

    with open(filename, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 8:
                src = parts[1]   
                dst = parts[7]
                weight = ord(dst) - ord('A') + 1
                graph[src].append((weight, dst))
                indegree[dst] = indegree.get(dst, 0) + 1
                if src not in indegree:
                    indegree[src] = 0
    return graph, indegree


def topo_sort(graph, indegree):
    # queue holds just the letter, but we sort alphabetically
    # (weights are stored in graph but not used for ordering in this puzzle)
    heap = [node for node in indegree if indegree[node] == 0]
    heapq.heapify(heap)

    order = []
    while heap:
        node = heapq.heappop(heap)
        order.append(node)
        for weight, nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                heapq.heappush(heap, nei)
    return "".join(order)


graph, indegree = dataloader("day7.txt")
print(topo_sort(graph, indegree))

#{'J': 8, 'X': 4, 'D': 3, 'K': 5, 'P': 7, 'F': 7, 'B': 3, 'U': 3, 'A': 4, 'E': 4, 'H': 7, 'O': 7, 'Q': 2, 'V': 4, 'T': 6, 'S': 2, 'Y': 3, 'Z': 4, 'M': 4, 'L': 5, 'N': 2, 'I': 2, 'C': 2, 'G': 2, 'R': 1}
