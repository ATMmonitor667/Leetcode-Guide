# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            length = len(queue)
            maxLeft = float('-inf')
            
            for i in range(length):
                node = queue.popleft()
                maxLeft = max(maxLeft, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(maxLeft)
        
        return ans
        