from typing import List, Tuple, Callable
from functools import lru_cache
import math
INF = 10**18


class Solution:
    '''
    This is the programming template for various DP on bitmasks problems.
    This is also known as the traveling salesman problem (TSP) pattern.
    '''
    # dist: n x n matrix, non-negative
    #---------------------------------------------------------------
    def tsp(self, dist: List[List[int]]) -> int:
        n = len(dist)
        @lru_cache(None)
        def dp(mask: int, u: int) -> int:
            if mask == (1 << n) - 1:
                return dist[u][0]  # return-to-start; drop if path not cycle
            best = INF
            m2 = mask
            for v in range(n):
                if not (m2 >> v) & 1:
                    best = min(best, dist[u][v] + dp(mask | (1 << v), v))
            return best
        return dp(1, 0)
    #--------------------------------------------------------------
    def min_actions_cover(self, cover_sets: List[int], nbits: int) -> int:
        # cover_sets[i] is a bitmask of positions covered by action i
        target = (1 << nbits) - 1
        dp = [INF] * (1 << nbits)
        dp[0] = 0
        for s in range(1 << nbits):
            if dp[s] == INF:
                continue
            for c in cover_sets:
                ns = s | c
                if dp[ns] > dp[s] + 1:
                    dp[ns] = dp[s] + 1
        return dp[target] if dp[target] < INF else -1
        # Count numbers in [0, R] with a customizable state.
        #-----------------------------------------------------------
    # Example state: (pos, tight, started, sum_mod) -> count
    def digit_dp(self, R: int, K: int) -> int:
        digits = list(map(int, str(R)))
        n = len(digits)

        @lru_cache(None)
        def dfs(i: int, tight: bool, started: bool, mod_sum: int) -> int:
            if i == n:
                # accept only if started and sum mod K == 0 (example)
                return int(started and mod_sum % K == 0)
            hi = digits[i] if tight else 9
            total = 0
            for d in range(hi + 1):
                ntight = tight and (d == hi)
                nstarted = started or (d != 0)
                nmod = (mod_sum + (d if nstarted else 0)) % K
                # put extra predicate checks here (e.g., forbid certain patterns)
                total += dfs(i + 1, ntight, nstarted, nmod)
            return total

        return dfs(0, True, False, 0)
    #-----------------------------------------------------------
    def knapsack_01(self, weights: List[int], values: List[int], W: int) -> int:
        n = len(weights)
        dp = [0] * (W + 1)
        for i in range(n):
            w, v = weights[i], values[i]
            for j in range(W, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + v)
        return dp[W]
    #-----------------------------------------------------------
    def knapsack_unbounded(self, weights: List[int], values: List[int], W
    ) -> int:
        n = len(weights)
        dp = [0] * (W + 1)
        for i in range(n):
            w, v = weights[i], values[i]
            for j in range(w, W + 1):
                dp[j] = max(dp[j], dp[j - w] + v)
        return dp[W]
    #-----------------------------------------------------------
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0
    #-----------------------------------------------------------
    def edit_distance(self, word1: str, word2: str) -> int:
        '''From my experiance this is the hardest DP problem on LeetCode which is stated as a medium problem.'''
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,    # delete
                                   dp[i][j - 1] + 1,    # insert
                                   dp[i - 1][j - 1] + 1)
        return dp[n][m]
    #-----------------------------------------------------------
    def knuth_opt(self, a: List[int]) -> int:
        '''Dont fully understand this algorithm yet but will work on it later.'''
        n = len(a)
        ps = [0]
        for x in a: ps.append(ps[-1] + x)

        def cost(i: int, j: int) -> int:
            return ps[j] - ps[i]

        dp = [[0]* (n+1) for _ in range(n+1)]
        opt = [[0]* (n+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][i+1] = 0
            opt[i][i+1] = i

        for len_ in range(2, n+1):
            for i in range(0, n - len_ + 1):
                j = i + len_
                dp[i][j] = INF
                # monotone range of optimal k
                L = opt[i][j-1]
                R = opt[i+1][j] if i+1 <= j else j-1
                if R < L:
                    L, R = R, L
                bestk = L
                for k in range(L, R+1):
                    val = dp[i][k] + dp[k][j] + cost(i, j)
                    if val < dp[i][j]:
                        dp[i][j] = val
                        bestk = k
                opt[i][j] = bestk
        return dp[0][n]
    #-----------------------------------------------------------
    def min_elements_sum(self, nums: List[int], target: int) -> int:
        dp = [INF] * (target + 1)
        dp[0] = 0
        for s in range(target + 1):
            if dp[s] == INF:
                continue
            for x in nums:
                ns = s + x
                if ns <= target and dp[ns] > dp[s] + 1:
                    dp[ns] = dp[s] + 1
        return dp[target] if dp[target] < INF else -1
    #-----------------------------------------------------------
