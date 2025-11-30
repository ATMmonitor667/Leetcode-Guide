# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        res = []
        def dfs(root):
            if root is None:
                return 
            else:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        kth = heapq.nsmallest(k, res)[-1]
        return kth

    