
class Solution:
    def maxSlidingWindow(self, nums, k):
        pq = []
        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))
        
        ans = [-pq[0][0]]  
        
        l, r = 0, k
        while r < len(nums):
            heapq.heappush(pq, (-nums[r], r))  
            l += 1             
            while pq and pq[0][1] < l:
                heapq.heappop(pq)    
            ans.append(-pq[0][0])  
            r += 1 
        
        return ans