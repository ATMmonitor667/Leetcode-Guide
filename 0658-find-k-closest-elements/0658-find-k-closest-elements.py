class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []

        ans = sorted([[abs(i - x), i] for i in arr])
        ans = sorted([i for j,i in ans][0:k])
        return ans


       