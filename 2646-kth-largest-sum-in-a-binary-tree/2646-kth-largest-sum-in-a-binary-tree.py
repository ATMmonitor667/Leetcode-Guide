# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
        valSum = []
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            length = len(queue)
            levelSum = 0
            for i in range(length):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            valSum.append( levelSum)
        heapq.heapify(valSum)
        if level < k:
            return -1
        val = heapq.nlargest(k, valSum)
        return val[-1]