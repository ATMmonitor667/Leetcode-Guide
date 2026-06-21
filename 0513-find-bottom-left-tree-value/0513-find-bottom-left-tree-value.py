# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            inter = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                inter.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result = inter
        return result[0]
