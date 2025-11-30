class Solution(object):
    def numDecodings(self, s):
        memo = {}
        # Convert string to list of integers once for easier access
        s_list = [int(i) for i in s] 
        
        # dfs(index, current_number_being_built)
        def dfs(idx, num):
            # Base Case: We reached the end of the string.
            if idx == len(s_list):
                # SUCCESS Condition: The final number we were building is valid (1-26)
                return 1 if 1 <= num <= 26 else 0
            
            # Check Memoization
            if (idx, num) in memo:
                return memo[(idx, num)]
            
            current_digit = s_list[idx]
            res = 0
            
            # --- OPTION 1: EXTEND the current number ---
            # e.g. We have '1', read '2' -> make '12'
            val_extended = num * 10 + current_digit
            if 1 <= val_extended <= 26:
                res += dfs(idx + 1, val_extended)

            # --- OPTION 2: SPLIT (Start a new number) ---
            # e.g. We have '1', read '2' -> finish '1', start new '2'
            # This is only allowed if:
            # 1. The number we are finishing (num) is valid (1-26).
            # 2. The new number starting (current_digit) is not 0.
            if 1 <= num <= 26 and current_digit != 0:
                res += dfs(idx + 1, current_digit)
            
            memo[(idx, num)] = res
            return res

        # Start with index 0 and a "dummy" 0 as the previous number.
        # This forces the first step to be an "Extend" (starting the first number).
        return dfs(0, 0)

        