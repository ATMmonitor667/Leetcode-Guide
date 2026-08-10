class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        heap = []
        for key,v in count.items():
            heapq.heappush(heap,[-1*v, key])
        ans = []
        while k:
            freq, char = heapq.heappop(heap)
            ans.append(char)
            k-=1
        return ans 
      