class Solution(object):
    def pathSum(self, root, targetSum):
        self.count = 0

        # Count paths that START at this node
        def dfs_from_node(node, currSum):
            if not node:
                return

            currSum += node.val

            if currSum == targetSum:
                self.count += 1

            dfs_from_node(node.left, currSum)
            dfs_from_node(node.right, currSum)

        # Try every node as a starting point
        def start_from_every_node(node):
            if not node:
                return

            dfs_from_node(node, 0)

            start_from_every_node(node.left)
            start_from_every_node(node.right)

        start_from_every_node(root)
        return self.count
            
        