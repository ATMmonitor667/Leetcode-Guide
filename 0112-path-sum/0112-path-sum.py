# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, pathSum):
            if not root:
                return False
            if root and root.left is None and root.right is None:
                pathSum += root.val
                if pathSum == targetSum:
                    return True
                return False
            
            return dfs(root.left, pathSum + root.val) or dfs(root.right, pathSum + root.val)
        return dfs(root, 0)
