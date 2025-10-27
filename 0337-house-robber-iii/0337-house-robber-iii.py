# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        memo = {}
        
        def dfs(node, can_take):
            if not node:
                return 0
            if (id(node), can_take) in memo:
                return memo[(id(node), can_take)]
            
            skip = dfs(node.left, True) + dfs(node.right, True)
            
            take = 0
            if can_take:
                take = node.val + dfs(node.left, False) + dfs(node.right, False)
            
            res = max(take, skip)
            memo[(id(node), can_take)] = res
            return res
        
        return dfs(root, True)

        