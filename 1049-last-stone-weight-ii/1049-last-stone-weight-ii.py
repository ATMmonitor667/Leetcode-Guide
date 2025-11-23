class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        @lru_cache(maxsize=None)
        def dfs(index: int, sum1: int, sum2: int) -> int:
            if index == n:
                return abs(sum1 - sum2)

            # Option 1: put current stone in pile 1
            diff1 = dfs(index + 1, sum1 + stones[index], sum2)
            # Option 2: put current stone in pile 2
            diff2 = dfs(index + 1, sum1, sum2 + stones[index])

            return min(diff1, diff2)

        return dfs(0, 0, 0)