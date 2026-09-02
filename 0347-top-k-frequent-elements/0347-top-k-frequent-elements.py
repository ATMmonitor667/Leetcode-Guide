class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        arr = []
        for key, v in count.items():
            arr.append((-1*v,key))
        heapq.heapify(arr)
        ans = []
        while k:
            value, val = heapq.heappop(arr)
            ans.append(val)
            print("hi")
            k-=1
        return ans 

       

        
        