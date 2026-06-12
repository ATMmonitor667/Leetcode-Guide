# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        def dfs(root, path):
            if root is None:
                return 
            if root and root.left is None and root.right is None:
                path = path + str(root.val)
                result.append(path)
                return
            else:
                dfs(root.left, path + str(root.val) + "->")
                dfs(root.right, path + str(root.val) + "->")
        dfs(root, "")
        return result
