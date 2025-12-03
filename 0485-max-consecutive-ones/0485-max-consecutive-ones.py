class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        word = ''.join([str(i) for i in nums])
        word = word.split('0')
        length = 0
        for i in word:
            if length < len(i):
                length = len(i)
        return length 
            
