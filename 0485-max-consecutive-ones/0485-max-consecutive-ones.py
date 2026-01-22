class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        currLength = 0  
        
        for num in nums:
            if num == 1:
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                currLength = 0  
                
        return maxLength
   
            
