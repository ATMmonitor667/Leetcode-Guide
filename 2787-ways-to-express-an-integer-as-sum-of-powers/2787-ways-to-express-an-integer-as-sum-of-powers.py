class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        a = 1
        while True:
            value = a ** x
            if value > n:
                break
            for j in range(n, value - 1, -1):
                dp[j] = (dp[j] + dp[j - value]) % MOD
            a += 1

        return dp[n]