"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = deque([])
        queue.append(root)
        res = []
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    for child in node.children:
                        if child:
                            queue.append(child)
            if level:
                res.append(level)
        return res
