class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        gifts = [-1*i for i in gifts]
        heapq.heapify(gifts)
        while k:
            gift = -1*heapq.heappop(gifts)
            gift = int(floor(sqrt(gift)))
            heapq.heappush(gifts, -1*gift)
            k-=1
        ans = sum([-1*i for i in gifts])
        return ans 