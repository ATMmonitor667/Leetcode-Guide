# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            # If both are None, continue
            if not node1 and not node2:
                continue

            # If only one is None, trees differ
            if not node1 or not node2:
                return False

            # If values differ, trees differ
            if node1.val != node2.val:
                return False

            # Add children (including None to preserve structure)
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)

        return not queue1 and not queue2