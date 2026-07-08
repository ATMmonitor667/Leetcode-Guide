class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        lookup = set(nums)
        ans = []
        invar = 1
        while invar < length:
            if invar not in lookup:
                ans.append(invar)
            invar +=1
        if invar == length and invar not in nums:
            ans.append(length)
        return ans
       
        

        