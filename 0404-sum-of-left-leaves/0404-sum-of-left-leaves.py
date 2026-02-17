# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        def dfs(root, isLeft):
            if not root:
                return
            if root and root.left is None and root.right is None:
                if isLeft:
                    res.append(root.val)
                return 
            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, False)
        return sum(res)