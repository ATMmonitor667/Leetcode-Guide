"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root):
            if root is None:
                return 0
            else:
                maxDepth = 1
                for children in root.children:
                    maxDepth =  max(maxDepth, 1 + dfs(children))
                return maxDepth
        return dfs(root)
        