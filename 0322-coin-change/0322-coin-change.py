class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        memo = {}

        def dfs(index, remain):
            if remain == 0:
                return 0

            if index == n or remain < 0:
                return float('inf')
            
            if (index, remain) in memo:
                return memo[(index, remain)]

           
            take = 1 + dfs(index, remain - coins[index])
            skip = dfs(index + 1, remain)

            memo[(index, remain)] = min(take, skip)
            return memo[(index, remain)]

        res = dfs(0, amount)
        return res if res != float('inf') else -1