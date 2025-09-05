class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        m = rows
        n = cols if the cols are the same then they are in the same as in the prev row
        same group no need to inc
        if reaches the base case and the groups arent equal then return a super large number
        if it reaches the base and the groups are equal then return grid value
        memozed the solution in a memo[(row, col, target)]
        def(row, col, target):
            if row == len(houses):
                if target != 0:
                    return inf
                if target == 0:
                    return 1
            prevCol = col
            res = inf
            for i in range(col):
                if prevCol == col:
                    res = min(res, cost[row][col] + dfs(row+1, col, target))
                else:
                    res = min(res, cost[row][col] + dfs(row+1, col, target + 1))
            memo[(row, col, target)] = res
            return res


        def dfs()
        """
        INF = float('inf')
        memo = {}

        def dfs(i, prev_color, t):
            if i == m:
                return 0 if t == 0 else INF

            if (i, prev_color, t) in memo:
                return memo[(i, prev_color, t)]

            if houses[i] != 0:
                color = houses[i]
                if color == prev_color:
                    ans = dfs(i + 1, color, t)
                else:
                    ans = dfs(i + 1, color, t - 1)
                memo[(i, prev_color, t)] = ans
                return ans

            min_cost = INF
            for color in range(1, n + 1):
                paint_cost = cost[i][color - 1]
                if color == prev_color:
                    total = paint_cost + dfs(i + 1, color, t)
                else:
                    total = paint_cost + dfs(i + 1, color, t - 1)
                min_cost = min(min_cost, total)

            memo[(i, prev_color, t)] = min_cost
            return min_cost

        res = dfs(0, 0, target)
        return res if res != INF else -1