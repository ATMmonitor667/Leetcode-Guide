class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(amount + 1)]
            for _ in range(len(coins) + 1)]

        # Base case: 1 way to make amount 0
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            coin_val = coins[i - 1]

            for curr in range(1, amount + 1):
                # Not take the coin
                dp[i][curr] = dp[i - 1][curr]

                # Take the coin
                if curr - coin_val >= 0:
                    dp[i][curr] += dp[i][curr - coin_val]
        return dp[len(coins)][amount]
