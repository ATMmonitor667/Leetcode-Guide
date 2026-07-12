class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0