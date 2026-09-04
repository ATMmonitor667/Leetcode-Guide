class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merger = [intervals[0]]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            print(start, end)
            if merger[-1][1] >= start:
                merger[-1][1] = max(merger[-1][1], end)
            else:
                merger.append([start, end])
        return merger

