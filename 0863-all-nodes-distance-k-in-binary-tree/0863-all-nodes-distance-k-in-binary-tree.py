# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        graph = defaultdict(list)

        def dfs(node, parent):
            if not node:
                return

            if parent:
                graph[node].append(parent)
                graph[parent].append(node)

            dfs(node.left, node)
            dfs(node.right, node)

        # Step 1: build graph
        dfs(root, None)

        # Step 2: BFS from target
        q = deque()
        q.append((target, 0))

        seen = set()
        seen.add(target)

        ans = []

        while q:
            node, dist = q.popleft()

            if dist == k:
                ans.append(node.val)
                continue

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, dist + 1))

        return ans