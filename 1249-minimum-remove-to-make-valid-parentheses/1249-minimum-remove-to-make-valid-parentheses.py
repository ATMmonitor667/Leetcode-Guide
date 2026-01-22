class Solution(object):
    def minRemoveToMakeValid(self, s):
        # PASS 1: Remove invalid ')'
        stack = []
        count = 0  # Tracks open parentheses
        
        for char in s:
            if char == '(':
                stack.append(char)
                count += 1
            elif char == ')':
                if count > 0:
                    stack.append(char)
                    count -= 1
                # Else: count is 0, so this ')' is invalid. Skip it (do not append).
            else:
                stack.append(char)
        
        # If count is 0, we are done!
        if count == 0:
            return "".join(stack)
            
        # PASS 2: Remove excess '(' from the end
        # We iterate backwards through our temporary 'stack'
        ans = []
        for char in reversed(stack):
            if char == '(' and count > 0:
                # This is an extra '('. Skip it.
                count -= 1
            else:
                ans.append(char)
        
        # Since we built 'ans' backwards, reverse it again to finish
        return "".join(ans[::-1])
