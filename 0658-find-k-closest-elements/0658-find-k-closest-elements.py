class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []

        for i in arr:
            heapq.heappush(heap, [abs(i - x), i])

        ans = []

        while k:
            distance, value = heapq.heappop(heap)
            ans.append(value)
            k -= 1

        ans.sort()
        return ans
       