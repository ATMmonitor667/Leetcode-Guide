class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []

        for i in arr:
            heapq.heappush(heap, [abs(i - x), i])

        return sorted([value for distance, value in heapq.nsmallest(k, heap)])

       