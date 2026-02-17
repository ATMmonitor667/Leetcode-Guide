class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        freq = {}
        
        def dfs(root):
            # FIXED: Must return 0 so single-child math doesn't crash
            if not root:
                return 0 
                
            # YOUR EXACT LEAF NODE LOGIC
            if root and root.left is None and root.right is None:
                if root.val in freq:
                    freq[root.val] += 1
                else:
                    freq[root.val] = 1
                return root.val
                
            # YOUR EXACT NON-LEAF NODE LOGIC
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                
                # Because null nodes return 0, this math is now perfectly safe
                inter = root.val + left + right
                
                if inter in freq:
                    freq[inter] += 1
                else:
                    freq[inter] = 1
                    
                return inter
                
        # 1. Run your recursive function to populate the dictionary
        dfs(root)
        
        # --- FINISHING THE PROBLEM OFF ---
        
        # 2. Find what the highest frequency actually is
        max_freq = max(freq.values())
        
        # 3. Create an array of all subtree sums that hit that max frequency
        ans = []
        for key in freq:
            if freq[key] == max_freq:
                ans.append(key)
                
        return ans