# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        zig = 0
        queue = deque([root])
        while queue:
            length = len(queue)
            inter = []
            for i in range(length):
                node = queue.popleft()

                inter.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if(zig%2 == 0):
                ans.append(inter)
            if(zig%2 == 1):
                
                ans.append(inter[::-1])
            zig+=1
        return ans
                
        