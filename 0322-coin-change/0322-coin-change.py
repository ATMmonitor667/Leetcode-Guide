class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for curr in range(coin, amount + 1):
                dp[curr] = min(dp[curr], dp[curr - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1