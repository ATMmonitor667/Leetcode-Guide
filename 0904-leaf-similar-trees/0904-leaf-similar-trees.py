# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        res = []
        def dfs(root):
            if not root:
                return []
            if root and root.left is None and root.right is None:
                return [root.val]
            else:
                return dfs(root.left) + dfs(root.right)
                
        return dfs(root1) == dfs(root2)
        print(res)