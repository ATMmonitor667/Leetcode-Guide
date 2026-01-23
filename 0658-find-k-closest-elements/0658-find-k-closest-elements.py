class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = sorted(arr, key=lambda y: abs(x - y))[:k]
        res.sort()
        return res
        
        print(res)
        