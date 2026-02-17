# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(root, path):
            if not root:
                return 
            if root and root.left is None and root.right is None:
                ans = sum(path) + root.val
                if ans == targetSum:
                    path += [root.val]
                    res.append(path[:])
                    return 
                return 
            else:
                dfs(root.left, path + [root.val])
                dfs(root.right,path + [root.val])
        dfs(root, [])
        return res
        