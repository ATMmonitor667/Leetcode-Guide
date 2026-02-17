# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root, value):
            nonlocal res
            if not root:
                return
            
            if root.val == 1:
                value = (value << 1) | 1
            else:
                value = (value << 1)

            if root.left is None and root.right is None:
                res += value
                return
            
            dfs(root.left, value)
            dfs(root.right, value)
        
        dfs(root, 0)
        return res

        