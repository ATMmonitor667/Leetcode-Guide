class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        val = len(nums)//2
        print(count)
        for k,v in count.items():
            if v> val:
                return k 
        return -1