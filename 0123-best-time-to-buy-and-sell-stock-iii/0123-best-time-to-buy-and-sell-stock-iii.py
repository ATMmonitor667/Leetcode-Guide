class Solution(object):
    def maxProfit(self, prices):
        # memoization dictionary to cache (index, flag)
        memo = {}

        def dfs(index, flag):
            # Base cases
            if index == len(prices) or flag == 4:
                return 0
            
            if (index, flag) in memo:
                return memo[(index, flag)]

            # If flag is even, we can either BUY or SKIP
            if flag % 2 == 0:
                buy = -prices[index] + dfs(index + 1, flag + 1)
                skip = dfs(index + 1, flag)
                ans = max(buy, skip)
                
            # If flag is odd, we can either SELL or SKIP
            else:
                sell = prices[index] + dfs(index + 1, flag + 1)
                skip = dfs(index + 1, flag)
                ans = max(sell, skip)

            memo[(index, flag)] = ans
            return ans

        return dfs(0, 0)