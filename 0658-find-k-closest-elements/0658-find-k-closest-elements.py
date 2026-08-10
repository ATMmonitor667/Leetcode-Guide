class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []

        for i in arr:
            heapq.heappush(heap, [abs(i - x), i])

        ans = [value for distance, value in heapq.nsmallest(k, heap)]

        return sorted(ans)