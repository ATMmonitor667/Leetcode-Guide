class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        stack = []
        i = 0
        n = len(intervals)
        while i < n:
            j = i + 1
            inter = intervals[i] 
            while j < n and inter[1] >= intervals[j][0]:
                inter[1] = max(inter[1], intervals[j][1])
                j += 1
            
            stack.append(inter)
            i = j
            
        return stack