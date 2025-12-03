class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7  
        memo = {}

        def dfs(pos, last, cnt):
            if pos == n:
                return 1

            key = (pos, last, cnt)
            if key in memo:
                return memo[key]

            res = 0
            for face in range(6):
                if face == last:
                    if cnt == rollMax[face]:  
                        continue
                    res += dfs(pos + 1, face, cnt + 1)
                else:
                    res += dfs(pos + 1, face, 1)

            res %= MOD
            memo[key] = res
            return res

        return dfs(0, -1, 0)
                
        