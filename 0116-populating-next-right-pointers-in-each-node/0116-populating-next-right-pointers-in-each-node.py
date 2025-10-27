"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            length = len(queue)
            prev = None  
            
            for i in range(length):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            prev.next = None
        
        return root
