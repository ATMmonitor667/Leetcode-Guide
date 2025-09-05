class Solution(object):
    def distinctSequences(self, n):
        """
        :type n: int
        :rtype: int
        what are the states? well we have a path
        Observation is that n = 4 ans = 184, if n =10^4 the answer will be something stupid large
        a Dice has exactly 6 faces could that be one of the states? What are the states in this problems?
        How do the states relate with one another. the roll itself is a state the number of rolls itself
        is another state, the two states are the number of rolls n and the 6 possible values for
        each of the rolls. Then there
        First brute force

        def dfs(index, path):
            if index == n and path satisfys coindition:
                return 1
            if index > n or path does not satisfy condition:
                return 0
            for i in range(1, 7):
                dfs(index+1, path + [i])
        refined solution
        dfs(index, currNumber, preNumber, preprev):
            if index == n:
                return 1
            else
                logic where it returns 0
        """
        MOD = 10**9 + 7

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return abs(a)

        memo = {}

        def dfs(index, prev, doubleprev):
            if index == n:
                return 1
            if (index, prev, doubleprev) in memo:
                return memo[(index, prev, doubleprev)]

            res = 0
            for i in range(1, 7):
                if prev != 0 and gcd(i, prev) != 1:
                    continue
                if i == prev or i == doubleprev:
                    continue
                res = (res + dfs(index + 1, i, prev)) % MOD

            memo[(index, prev, doubleprev)] = res
            return res

        return dfs(0, 0, 0)