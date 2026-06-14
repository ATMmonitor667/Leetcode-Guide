# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            length = len(queue)
            levelSum = 0
            levelNode = 0
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    levelSum += node.val
                    levelNode+=1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result = float(levelSum)/float(levelNode)
            res.append(result)
        return res

        