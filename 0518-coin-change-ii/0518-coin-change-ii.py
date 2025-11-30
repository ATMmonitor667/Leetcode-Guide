class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo = {}
        def dfs(index = 0, target = amount ):
            if(index < len(coins) and target == 0):
                return 1
            if index >= len(coins) or target < 0:
                return 0
            if ((index, target) in memo):
                return memo[(index, target)]
            else:
                memo[(index, target)] = dfs(index, target - coins[index]) + dfs(index+1, target)
                return memo[(index, target)]
        return dfs()

 
