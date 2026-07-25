class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        while n:
            arr.append(-1*(n%10))
            n = n//10
        print(arr)
        heapq.heapify(arr)
        val1 = heapq.heappop(arr)
        val2 = heapq.heappop(arr)
        return val1 * val2
        