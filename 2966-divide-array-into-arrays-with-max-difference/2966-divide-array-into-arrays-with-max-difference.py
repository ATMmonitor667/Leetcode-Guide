class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        
        res = []
        
        for i in range(0, len(nums), 3):
            chunk = nums[i : i+3]
            
            if chunk[2] - chunk[0] > k:
                return [] 
            
            res.append(chunk)
            
        return res
