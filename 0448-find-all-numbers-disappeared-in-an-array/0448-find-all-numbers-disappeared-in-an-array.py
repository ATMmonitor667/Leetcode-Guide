class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        length = len(nums)
        lookup = set(nums)
        ans = []
        while length:
            if length not in lookup:
                ans.append(length)
            length -=1
        return ans 

        