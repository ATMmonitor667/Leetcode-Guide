class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        n,k, target
        n = 1, k = 6
        target = 3
    n dices, k faces and target
    3 dices, 6 faces, sum = 13
    sum([ .... ] | [ .... ] | [.... ]) = 13
    1 1-6 1-6 = 13
    2 1-6 1-6
    3.
    ..
    ..
    ..
    dfs(n, k, target):
        if target == 0:
            return 1
        if target < 0:
            return = 0 
        else:
            res = 0
            for j in range(k):
                res+=dfs(n-1, k, target-k)
            return res
    memo = {}
    dfs(n,k, target):
       if target == 0:
        if n == 0:
          return 1
        return 0
        if target < 0:
            return 0
        if (n, target) in memo:
            return memo[(n,target)]
        else:
            res = 0
            for i in range(k):
                res+=dfs(n-1, k, target-k)
            memo[(n,target)] = res
            return res
        
        """
        MOD = 10**9 + 7
        memo = {}

        def dfs(d, t):
            if d == 0:
                return 1 if t == 0 else 0
            if t < d or t > d * k:   
                return 0
            if (d, t) in memo:
                return memo[(d, t)]

            res = 0
            for face in range(1, k + 1):
                res = (res + dfs(d - 1, t - face)) % MOD

            memo[(d, t)] = res
            return res

        return dfs(n, target)


        