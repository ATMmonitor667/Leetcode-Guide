class Solution(object):
    def maxProfit(self, prices):
        memo = {}

        def dfs(i, holding):
            if i == len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding == 0:
                ans = max(
                    dfs(i + 1, 0),                  
                    -prices[i] + dfs(i + 1, 1)     
                )
            else:
                ans = max(
                    dfs(i + 1, 1),                 
                    prices[i] + dfs(i + 1, 0)      
                )

            memo[(i, holding)] = ans
            return ans

        return dfs(0, 0)