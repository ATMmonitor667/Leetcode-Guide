# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def dfs(node):
            nonlocal total   # allow modification of outer variable
            if not node:
                return
            dfs(node.right)          # process larger values first
            total += node.val        # accumulate running sum
            node.val = total         # update node value
            dfs(node.left)           # then process smaller values

        dfs(root)
        return root