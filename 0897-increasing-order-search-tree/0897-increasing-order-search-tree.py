from collections import deque

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.sort()

        dummy = TreeNode(0)
        cursor = dummy

        for val in result:
            cursor.right = TreeNode(val)
            cursor = cursor.right

        return dummy.right

