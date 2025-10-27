class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo = {}
        def dfs(index, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if (index, amount) in memo:
                return memo[(index, amount)]
            else:
                res = 0
                if index < len(coins):
                   res = dfs(index, amount -coins[index]) + dfs(index+1, amount)
                memo[(index, amount)] = res
                return res
        val = dfs(0, amount)
        return val
        