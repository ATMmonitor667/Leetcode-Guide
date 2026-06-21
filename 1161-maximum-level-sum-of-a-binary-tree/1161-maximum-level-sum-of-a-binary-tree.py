# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque()
        queue.append(root)

        maxi = float('-inf')
        answer_level = 0
        level = 0

        while queue:
            level += 1
            length = len(queue)
            summation = 0

            for i in range(length):
                node = queue.popleft()
                summation += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if summation > maxi:
                maxi = summation
                answer_level = level

        return answer_level