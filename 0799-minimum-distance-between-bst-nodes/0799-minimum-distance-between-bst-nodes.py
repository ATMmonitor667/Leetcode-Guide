# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        def dfs(root):
            if not root:
                return 
            else:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        res.sort()
        mini = float('inf')
        for i in range(1, len(res)):
            if((abs(res[i]-res[i-1])) < mini):
                mini = (abs(res[i]-res[i-1]))
        return mini

        