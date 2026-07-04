# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
            
        arr = []
        queue = deque([root])
        curr_level = 0
        
        while queue:
            level_size = len(queue)
            level_vals = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr_level % 2 == 1:
                level_vals.reverse()
                
            arr.extend(level_vals)
            curr_level += 1
            
            
        nodes = []
        for val in arr:
            nodes.append(TreeNode(val))
            
        for i in range(len(nodes)):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
                
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
                
        return nodes[0]
