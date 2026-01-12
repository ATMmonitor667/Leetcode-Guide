class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        mini = float('inf')
        for i in range(1, len(arr)):
            inter = arr[i]-arr[i-1]
            if inter < mini:
                mini = inter
        res = []
        for i in range(1, len(arr)):
            inter = arr[i]-arr[i-1]
            if inter == mini:
                res.append([arr[i-1],arr[i]])
        return res