class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        def function(arr):
            arr.sort(reverse=True)
        input = []
        for i in grid:
            temp = function(i)
            input.append(i)
        ans = []
        for i in range(len(input)):
            tempList = input[i][0:limits[i]]
            ans += tempList
        ans.sort(reverse = True)
        print(ans)
        sums = 0
        i = 0
        while k:
           sums+= ans[i]
           i+=1
           k-=1
        return sums
        print(sums)
        