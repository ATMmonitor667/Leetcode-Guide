class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        memo = {1: 0}
        def dfs(number):
            if number in memo:
                return memo[number]
            else:
                if number%2 == 0:
                    memo[number] = 1 + dfs(number//2)
                else:
                    memo[number] = 1 + dfs( number*3 +1)
                return memo[number]
        res = []
        for x in range(lo, hi + 1):
            power = dfs(x)
            res.append((power, x))
            
        res.sort()
        
        return res[k-1][1]

        