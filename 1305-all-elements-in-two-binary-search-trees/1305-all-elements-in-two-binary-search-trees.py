# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def dfs(root):
            if root is None:
                return 
            if root:
                result.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root1)
        dfs(root2)
        result.sort()
        return result