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
                return 
            else:
                dfs(root.left)
                dfs(root.right)
                if root and root.left is None and root.right is None:
                    res.append(root.val)
                    return 
        dfs(root1)
        res1 = res
        res = []
        dfs(root2)
        res2 = res
        print(res1, res2)
        return res1 == res2
        