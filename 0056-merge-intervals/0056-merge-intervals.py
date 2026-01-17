class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        res = []
        for i, [s,e] in enumerate(intervals):
            if not res or res[-1][1] < intervals[i][0]:
                res.append([s,e])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res