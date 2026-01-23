class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []
        for i in arr:
            heapq.heappush(heap, [abs(i-x),i])
        ans = []
        while heap and k:
            val = heapq.heappop(heap)
            ans.append(val[1])
            k-=1
        print(ans)
        ans.sort()
        return ans

        