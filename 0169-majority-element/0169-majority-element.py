class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        n = len(nums)
        for k,v in count.items():
            if v > int(n//2):
                return k 
        return -1
        