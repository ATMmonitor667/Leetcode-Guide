class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        remaining = 0
        max_end = -1

        for start, end in intervals:
            if end <= max_end:
                continue

            remaining += 1
            max_end = end

        return remaining
        