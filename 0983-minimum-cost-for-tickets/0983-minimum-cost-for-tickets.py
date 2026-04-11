class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        memo = {}
        def dfs(index, current):
            if index == len(days):
                return 0
            if current >= days[index]:
                return dfs(index+1, current)
            if (index, current) in memo:
                return memo[(index, current)]
            else:
                res = float('inf')
                day = costs[0] + dfs(index+1, days[index] + 1 - 1)
                week = costs[1] + dfs(index+1, days[index] + 7 - 1 )
                month = costs[2] + dfs(index+1, days[index] + 30 -1 )
                res = min(res, day, week, month)
                memo[(index, current)] = res
                return res
        return dfs(0, 0)
        